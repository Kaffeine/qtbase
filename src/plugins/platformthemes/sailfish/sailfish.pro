TARGET = qsailfish

QT += core-private dbus gui-private

isEqual(QT_MAJOR_VERSION, 5) {
    lessThan(QT_MINOR_VERSION, 8) {
        QT += platformsupport-private
    } else {
        # Platformsupport libraries are modularized since 5.8.0
        QT += theme_support-private
    }
}

HEADERS += \
    qsailfishtheme.h

SOURCES += \
    main.cpp \
    qsailfishtheme.cpp

PLUGIN_TYPE = platformthemes
PLUGIN_EXTENDS = -
PLUGIN_CLASS_NAME = QSailfishTheme
load(qt_plugin)
