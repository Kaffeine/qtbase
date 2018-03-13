/****************************************************************************
**
** Copyright (C) 2018 Open Mobile Platform LLC
** Contact: https://www.qt.io/licensing/
**
** This file is part of the plugins of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or (at your option) the GNU General
** Public license version 3 or any later version approved by the KDE Free
** Qt Foundation. The licenses are as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-2.0.html and
** https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#include "qsailfishtheme.h"

#include <private/qguiapplication_p.h>
#include <qpa/qplatformtheme_p.h>
#include <qpa/qplatformthemefactory_p.h>
#include <qpa/qplatformintegration.h>

QT_BEGIN_NAMESPACE

// Default system font, corresponding to the value returned by 4.8 for
// XRender/FontConfig which we can now assume as default.
static const char defaultSystemFontNameC[] = "Sans Serif";
static const int defaultSystemFontSize = 9;

class QSailfishThemePrivate : public QPlatformThemePrivate
{
public:
    QSailfishThemePrivate()
        : QPlatformThemePrivate()
    {
        const QSettings settings(QSettings::SystemScope, QStringLiteral("QtProject"), QStringLiteral("QPlatformTheme"));

        const QString systemFontName(settings.value(QStringLiteral("GenericUnixTheme/SystemFont"), QLatin1String(defaultSystemFontNameC)).toString());
        const int systemFontSize(settings.value(QStringLiteral("GenericUnixTheme/SystemFontSize"), defaultSystemFontSize).toInt());
        systemFont = QFont(systemFontName, systemFontSize);

        const QString fixedFontName(settings.value(QStringLiteral("GenericUnixTheme/FixedFont"), QStringLiteral("monospace")).toString());
        const int fixedFontSize(settings.value(QStringLiteral("GenericUnixTheme/FixedFontSize"), static_cast<int>(defaultSystemFontSize)).toInt());
        fixedFont = QFont(fixedFontName, fixedFontSize);
        fixedFont.setStyleHint(QFont::TypeWriter);

        systemIconFallbackThemeName = settings.value(QStringLiteral("GenericUnixTheme/SystemIconFallbackThemeName"), QStringLiteral("hicolor"));
        iconThemeSearchPaths = settings.value(QStringLiteral("GenericUnixTheme/IconThemeSearchPaths"));
        if (iconThemeSearchPaths.isNull()) {
            iconThemeSearchPaths = QGenericUnixTheme::xdgIconThemePaths();
        }

        dialogButtonBoxButtonsHaveIcons = settings.value(QStringLiteral("GenericUnixTheme/DialogButtonBoxButtonsHaveIcons"), true);
        styleNames = settings.value(QStringLiteral("GenericUnixTheme/StyleNames"), QStringList() << QStringLiteral("Fusion") << QStringLiteral("Windows"));
        keyboardScheme = settings.value(QStringLiteral("GenericUnixTheme/KeyboardScheme"), static_cast<int>(QPlatformTheme::X11KeyboardScheme));
        passwordMaskDelay = settings.value(QStringLiteral("GenericUnixTheme/PasswordMaskDelay"), 1000);
        startDragDistance = settings.value(QStringLiteral("GenericUnixTheme/StartDragDistance"), 20);
    }

    ~QSailfishThemePrivate()
    {
        delete baseTheme;
    }

    static QPlatformTheme *createBaseTheme()
    {
        QPlatformTheme *theme = nullptr;
        const QStringList names = QGuiApplicationPrivate::platform_integration->themeNames();
        // 1) Look for a theme plugin.
        for (const QString &name : names) {
            theme = QPlatformThemeFactory::create(name, nullptr);
            if (theme) {
                break;
            }
        }

        // 2) If no theme plugin was found ask the platform integration to create a theme
        if (!theme) {
            for (const QString &name : names) {
                theme = QGuiApplicationPrivate::platform_integration->createPlatformTheme(name);
                if (theme) {
                    break;
                }
            }
            // No error message; not having a theme plugin is allowed.
        }
        // 3) Fall back on the built-in "null" platform theme.
        if (!theme) {
            theme = new QPlatformTheme;
        }
        return theme;
    }

    QFont systemFont;
    QFont fixedFont;
    QVariant systemIconFallbackThemeName;
    QVariant iconThemeSearchPaths;
    QVariant dialogButtonBoxButtonsHaveIcons;
    QVariant styleNames;
    QVariant keyboardScheme;
    QVariant passwordMaskDelay;
    QVariant startDragDistance;
    QPlatformTheme *baseTheme = nullptr;
};

QSailfishTheme::QSailfishTheme()
    : QPlatformTheme(new QSailfishThemePrivate)
{
    Q_D(QSailfishTheme);
    d->baseTheme = QSailfishThemePrivate::createBaseTheme();
}

QPlatformMenuItem *QSailfishTheme::createPlatformMenuItem() const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->createPlatformMenuItem();
}

QPlatformMenu *QSailfishTheme::createPlatformMenu() const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->createPlatformMenu();
}

QPlatformMenuBar *QSailfishTheme::createPlatformMenuBar() const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->createPlatformMenuBar();
}

void QSailfishTheme::showPlatformMenuBar()
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->showPlatformMenuBar();
}

bool QSailfishTheme::usePlatformNativeDialog(DialogType type) const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->usePlatformNativeDialog(type);
}

QPlatformDialogHelper *QSailfishTheme::createPlatformDialogHelper(DialogType type) const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->createPlatformDialogHelper(type);
}

#ifndef QT_NO_SYSTEMTRAYICON
QPlatformSystemTrayIcon *QSailfishTheme::createPlatformSystemTrayIcon() const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->createPlatformSystemTrayIcon();
}
#endif

const QPalette *QSailfishTheme::palette(Palette type) const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->palette(type);
}

const QFont *QSailfishTheme::font(Font type) const
{
    Q_D(const QSailfishTheme);
    switch (type) {
    case QPlatformTheme::SystemFont:
        return &d->systemFont;
    case QPlatformTheme::FixedFont:
        return &d->fixedFont;
    default:
        break;
    }
    return d->baseTheme->font(type);
}

QVariant QSailfishTheme::themeHint(ThemeHint hint) const
{
    Q_D(const QSailfishTheme);
    switch (hint) {
    case QPlatformTheme::SystemIconFallbackThemeName:
        return d->systemIconFallbackThemeName;
    case QPlatformTheme::IconThemeSearchPaths:
        return d->iconThemeSearchPaths;
    case QPlatformTheme::DialogButtonBoxButtonsHaveIcons:
        return d->dialogButtonBoxButtonsHaveIcons;
    case QPlatformTheme::StyleNames:
        return d->styleNames;
    case QPlatformTheme::KeyboardScheme:
        return d->keyboardScheme;
    case QPlatformTheme::PasswordMaskDelay:
        return d->passwordMaskDelay;
    case QPlatformTheme::StartDragDistance:
        return d->startDragDistance;
    default:
        break;
    }
    return d->baseTheme->themeHint(hint);
}

QPixmap QSailfishTheme::standardPixmap(StandardPixmap sp, const QSizeF &size) const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->standardPixmap(sp, size);
}

#if (QT_VERSION >= QT_VERSION_CHECK(5, 8, 0))
QIcon QSailfishTheme::fileIcon(const QFileInfo &fileInfo,
                               QPlatformTheme::IconOptions iconOptions) const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->fileIcon(fileInfo, iconOptions);
}
#else
QPixmap QSailfishTheme::fileIconPixmap(const QFileInfo &fileInfo, const QSizeF &size, QPlatformTheme::IconOptions iconOptions) const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->fileIconPixmap(fileInfo, size, iconOptions);
}
#endif

QIconEngine  *QSailfishTheme::createIconEngine(const QString &iconName) const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->createIconEngine(iconName);
}

QList<QKeySequence> QSailfishTheme::keyBindings(QKeySequence::StandardKey key) const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->keyBindings(key);
}

QString QSailfishTheme::standardButtonText(int button) const
{
    Q_D(const QSailfishTheme);
    return d->baseTheme->standardButtonText(button);
}

QT_END_NAMESPACE
