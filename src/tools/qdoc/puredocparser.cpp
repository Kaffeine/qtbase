/****************************************************************************
**
** Copyright (C) 2012 Nokia Corporation and/or its subsidiary(-ies).
** Contact: http://www.qt-project.org/
**
** This file is part of the tools applications of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** GNU Lesser General Public License Usage
** This file may be used under the terms of the GNU Lesser General Public
** License version 2.1 as published by the Free Software Foundation and
** appearing in the file LICENSE.LGPL included in the packaging of this
** file. Please review the following information to ensure the GNU Lesser
** General Public License version 2.1 requirements will be met:
** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** In addition, as a special exception, Nokia gives you certain additional
** rights. These rights are described in the Nokia Qt LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU General
** Public License version 3.0 as published by the Free Software Foundation
** and appearing in the file LICENSE.GPL included in the packaging of this
** file. Please review the following information to ensure the GNU General
** Public License version 3.0 requirements will be met:
** http://www.gnu.org/copyleft/gpl.html.
**
** Other Usage
** Alternatively, this file may be used in accordance with the terms and
** conditions contained in a signed written agreement between you and Nokia.
**
**
**
**
**
**
** $QT_END_LICENSE$
**
****************************************************************************/

/*
  puredocparser.cpp
*/

#include <qfile.h>
#include <stdio.h>
#include <errno.h>
#include "codechunk.h"
#include "config.h"
#include "tokenizer.h"
#include "tree.h"
#include <qdebug.h>
#include "puredocparser.h"

QT_BEGIN_NAMESPACE

PureDocParser::PureDocParser()
{
}

PureDocParser::~PureDocParser()
{
}

QStringList PureDocParser::sourceFileNameFilter()
{
    return QStringList() << "*.qdoc" << "*.qtx" << "*.qtt" << "*.js";
}

/*!
  Parse the source file identified by \a filePath and add its
  parsed contents to the big \a tree. \a location is used for
  reporting errors.
 */
void PureDocParser::parseSourceFile(const Location& location,
                                    const QString& filePath,
                                    Tree *tree)
{
    QFile in(filePath);
    if (!in.open(QIODevice::ReadOnly)) {
        location.error(tr("Can't open source file '%1' (%2)").arg(filePath).arg(strerror(errno)));
        return;
    }
    createOutputSubdirectory(location, filePath);

    reset(tree);
    Location fileLocation(filePath);
    Tokenizer fileTokenizer(fileLocation, in);
    tokenizer = &fileTokenizer;
    readToken();

    /*
      The set of active namespaces is cleared before parsing
      each source file. The word "source" here means cpp file.
     */
    activeNamespaces_.clear();

    processQdocComments();
    in.close();
}

/*!
  This is called by parseSourceFile() to do the actual parsing
  and tree building. It only processes qdoc comments. It skips
  everything else.
 */
bool PureDocParser::processQdocComments()
{
    QSet<QString> topicCommandsAllowed = topicCommands();
    QSet<QString> otherMetacommandsAllowed = otherMetaCommands();
    QSet<QString> metacommandsAllowed = topicCommandsAllowed + otherMetacommandsAllowed;

    while (tok != Tok_Eoi) {
        if (tok == Tok_Doc) {
            /*
              lexeme() returns an entire qdoc comment.
             */
            QString comment = lexeme();
            Location start_loc(location());
            readToken();

            Doc::trimCStyleComment(start_loc,comment);
            Location end_loc(location());

            /*
              Doc parses the comment.
             */
            Doc doc(start_loc,end_loc,comment,metacommandsAllowed);

            QString topic;
            ArgList args;

            QSet<QString> topicCommandsUsed = topicCommandsAllowed & doc.metaCommandsUsed();

            /*
              There should be one topic command in the set,
              or none. If the set is empty, then the comment
              should be a function description.
             */
            if (topicCommandsUsed.count() > 0) {
                topic = *topicCommandsUsed.begin();
                args = doc.metaCommandArgs(topic);
            }

            NodeList nodes;
            QList<Doc> docs;

            if (topic.isEmpty()) {
                doc.location().warning(tr("This qdoc comment contains no topic command "
                                          "(e.g., '\\%1', '\\%2').")
                                       .arg(COMMAND_MODULE).arg(COMMAND_PAGE));
            }
            else {
                /*
                  There is a topic command. Process it.
                 */
                if ((topic == COMMAND_QMLPROPERTY) ||
                        (topic == COMMAND_QMLATTACHEDPROPERTY)) {
                    Doc nodeDoc = doc;
                    Node* node = processTopicCommandGroup(topic,args);
                    if (node != 0) {
                        nodes.append(node);
                        docs.append(nodeDoc);
                    }
                }
                else {
                    ArgList::ConstIterator a = args.begin();
                    while (a != args.end()) {
                        Doc nodeDoc = doc;
                        Node* node = processTopicCommand(nodeDoc,topic,*a);
                        if (node != 0) {
                            nodes.append(node);
                            docs.append(nodeDoc);
                        }
                        ++a;
                    }
                }
            }

            NodeList::Iterator n = nodes.begin();
            QList<Doc>::Iterator d = docs.begin();
            while (n != nodes.end()) {
                processOtherMetaCommands(*d, *n);
                (*n)->setDoc(*d);
                if ((*n)->isInnerNode() && ((InnerNode *)*n)->includes().isEmpty()) {
                    InnerNode *m = static_cast<InnerNode *>(*n);
                    while (m->parent() != tree_->root())
                        m = m->parent();
                    if (m == *n)
                        ((InnerNode *)*n)->addInclude((*n)->name());
                    else
                        ((InnerNode *)*n)->setIncludes(m->includes());
                }
                ++d;
                ++n;
            }
        }
        else {
            readToken();
        }
    }
    return true;
}


QT_END_NAMESPACE
