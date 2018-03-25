# libQtPlatformSupport is not built as a shared library, only as a
# static .a lib-archive. By default the OBS build removes all discovered
# libFOO.a files and as such rpmlint never complains about
# installed-but-unpackaged static libs.
# This flag tells rpmbuild to behave.
%define keepstatic 1

# Version is the date of latest commit in qtbase, followed by 'g' + few
# characters of the last git commit ID.
# NOTE: tarball's prefix is 'qt5-base' until version number starts to
# make sense. This allows to update spec contents easily as snapshots
# evolve.

Name:       qt%{_qt5_version}
Summary:    Cross-platform application and UI framework
Version:    5.6.3
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv3 with exception or GPLv3
URL:        https://www.qt.io/
Source0:    qt-%{version}.tar.bz2
Source100:  qtbase-rpmlintrc
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(libsystemd-journal)
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  flex
# Package not available but installed in OBS?
#BuildRequires:  gcc-g++
BuildRequires:  libjpeg-devel
#BuildRequires:  libtiff-devel
BuildRequires:  pam-devel
BuildRequires:  readline-devel
BuildRequires:  sharutils
#BuildRequires:  gdb
BuildRequires:  python
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  qt5-rpm-macros

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

%global platform linux-g++-sailfish

%package tools
Summary:    Development tools for qtbase
Requires:   qtchooser

%description tools
This package contains useful tools for Qt development

%package qtcore
Summary:    The QtCore library
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
Requires:   xdg-utils

Conflicts:  qt%{_qt5_version}-qtdbus < %{version}
Conflicts:  qt%{_qt5_version}-qtgui < %{version}
Conflicts:  qt%{_qt5_version}-qtnetwork < %{version}
Conflicts:  qt%{_qt5_version}-qtopengl < %{version}
Conflicts:  qt%{_qt5_version}-qtsql < %{version}
Conflicts:  qt%{_qt5_version}-qtwidgets < %{version}
Conflicts:  qt%{_qt5_version}-qtconcurrent < %{version}

%description qtcore
This package contains the QtCore library

%package qtcore-devel
Summary:    Development files for QtCore
Requires:   %{name}-qmake
Requires:   %{name}-tools
Requires:   %{name}-qtcore = %{version}-%{release}
Requires:   fontconfig-devel
Requires:   qtchooser

%description qtcore-devel
This package contains the files necessary to develop applications
that use the QtCore


%package qmake
Summary:    QMake
Requires:   qtchooser
Requires:   qt5-rpm-macros

%description qmake
This package contains qmake


%package plugin-bearer-connman
Summary:    Connman bearer plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-connman
This package contains the connman bearer plugin


%package plugin-bearer-generic
Summary:    Connman generic plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-generic
This package contains the connman generic bearer plugin


%package plugin-bearer-nm
Summary:    Connman generic plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-bearer-nm
This package contains the connman NetworkManager bearer plugin


%package plugin-imageformat-gif
Summary:    Gif image format plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-gif
This package contains the gif imageformat plugin


%package plugin-imageformat-ico
Summary:    Ico image format plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-ico
This package contains the ico imageformat plugin


%package plugin-imageformat-jpeg
Summary:    JPEG image format plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-imageformat-jpeg
This package contains the JPEG imageformat plugin


#%package plugin-imageformat-tiff
#Summary:    TIFF image format plugin
#
#%description plugin-imageformat-tiff
#This package contains the TIFF imageformat plugin


%package plugin-platform-minimal
Summary:    Minimal platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-minimal
This package contains the minimal platform plugin

%package plugin-platform-offscreen
Summary:    Offscreen platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-offscreen
This package contains the offscreen platform plugin

%package plugin-platform-eglfs
Summary:    Eglfs platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description plugin-platform-eglfs
This package contains the eglfs platform plugin

%package plugin-platform-eglfs-devel
Summary:    Development files for Qt EGLFS platform plugin
Requires:   %{name}-plugin-platform-eglfs = %{version}-%{release}

%description plugin-platform-eglfs-devel
This package contains the files necessary to develop
applications that use Qt EGLFS platform plugin

%package plugin-platform-minimalegl
Summary:    Minimalegl platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-minimalegl
This package contains the minimalegl platform plugin

%package plugin-platform-linuxfb
Summary:    Linux framebuffer platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-linuxfb
This package contains the linuxfb platform plugin for Qt

%package plugin-platform-vnc
Summary:    VNC client platform plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platform-vnc
This package contains the VNC client plugin for Qt

%package plugin-printsupport-cups
Summary:    CUPS print support plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-printsupport-cups
This package contains the CUPS print support plugin

%package plugin-sqldriver-sqlite
Summary:    Sqlite sql driver plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-sqldriver-sqlite
This package contains the sqlite sql driver plugin


%package plugin-platforminputcontext-ibus
Summary:    ibus platform import context plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-platforminputcontext-ibus
This package contains the ibus platform input context plugin

%package plugin-generic-evdev
Summary:    evdev generic plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-generic-evdev
This package contains evdev plugins

%package plugin-generic-tuiotouch
Summary:    tuio touch generic plugin
Requires:   %{name}-qtcore = %{version}-%{release}

%description plugin-generic-tuiotouch
This package contains tuio touch plugins


%package qtdbus
Summary:    The QtDBus library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtdbus
This package contains the QtDBus library


%package qtdbus-devel
Summary:    Development files for QtDBus
Requires:   %{name}-qtdbus = %{version}-%{release}
Requires:   pkgconfig(dbus-1)

%description qtdbus-devel
This package contains the files necessary to develop
applications that use QtDBus


%package qtgui
Summary:    The QtGui Library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtgui
This package contains the QtGui library


%package qtgui-devel
Summary:    Development files for QtGui
Requires:   %{name}-qtgui = %{version}-%{release}
Requires:   libGLESv2-devel
Requires:   libEGL-devel

%description qtgui-devel
This package contains the files necessary to develop
applications that use QtGui


%package qtnetwork
Summary:    The QtNetwork library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtnetwork
This package contains the QtNetwork library


%package qtnetwork-devel
Summary:    Development files for QtNetwork
Requires:   %{name}-qtnetwork = %{version}-%{release}

%description qtnetwork-devel
This package contains the files necessary to develop
applications that use QtNetwork



%package qtopengl
Summary:    The QtOpenGL library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtopengl
This package contains the QtOpenGL library


%package qtopengl-devel
Summary:    Development files for QtOpenGL
Requires:   %{name}-qtopengl = %{version}-%{release}
Requires:   libGLESv2-devel
Requires:   libEGL-devel

%description qtopengl-devel
This package contains the files necessary to develop
applications that use QtOpenGL


%package qtsql
Summary:    The QtSql library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtsql
This package contains the QtSql library


%package qtsql-devel
Summary:    Development files for QtSql
Requires:   %{name}-qtsql = %{version}-%{release}

%description qtsql-devel
This package contains the files necessary to develop
applications that use QtSql


%package qttest
Summary:    The QtTest library
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qttest
This package contains the QtTest library


%package qttest-devel
Summary:    Development files for QtTest
Requires:   %{name}-qttest = %{version}-%{release}

%description qttest-devel
This package contains the files necessary to develop
applications that use QtTest


%package qtxml
Summary:    The QtXml library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtxml
This package contains the QtXml library

%package qtxml-devel
Summary:    Development files for QtXml
Requires:   %{name}-qtxml = %{version}-%{release}

%description qtxml-devel
This package contains the files necessary to develop
applications that use QtXml


%package qtwidgets
Summary:    The QtWidgets library
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtwidgets
This package contains the QtWidgets library

%package qtwidgets-devel
Summary:    Development files for QtWidgets
Requires:   %{name}-qtwidgets = %{version}-%{release}

%description qtwidgets-devel
This package contains the files necessary to develop
applications that use QtWidgets

%package qtplatformsupport-devel
Summary:    Development files for QtPlatformSupport
Requires: %{name}-qtwidgets = %{version}-%{release}
Requires: %{name}-qteventdispatchersupport-devel = %{version}-%{release}
Requires: %{name}-qtdevicediscoverysupport-devel = %{version}-%{release}
Requires: %{name}-qtfbsupport-devel = %{version}-%{release}
Requires: %{name}-qtthemesupport-devel = %{version}-%{release}
Requires: %{name}-qtfontdatabasesupport-devel = %{version}-%{release}
Requires: %{name}-qtinputsupport-devel = %{version}-%{release}
Requires: %{name}-qtservicesupport-devel = %{version}-%{release}
Requires: %{name}-qtplatformcompositorsupport-devel = %{version}-%{release}
Requires: %{name}-qteglsupport-devel = %{version}-%{release}
Requires: %{name}-qtaccessibilitysupport-devel = %{version}-%{release}

%description qtplatformsupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport

%package qteventdispatchersupport-devel
Summary: Development files for QtPlatformSupport/EventDispatcher

%description qteventdispatchersupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport EventDispatcher library

%package qtdevicediscoverysupport-devel
Summary: Development files for QtPlatformSupport/DeviceDiscovery

%description qtdevicediscoverysupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport DeviceDiscovery library

%package qtfbsupport-devel
Summary: Development files for QtPlatformSupport/Fb

%description qtfbsupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport Fb library

%package qtthemesupport-devel
Summary: Development files for QtPlatformSupport/Theme

%description qtthemesupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport Theme library

%package qtfontdatabasesupport-devel
Summary: Development files for QtPlatformSupport/FontDatabase

%description qtfontdatabasesupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport FontDatabase library

%package qtinputsupport-devel
Summary: Development files for QtPlatformSupport/Input

%description qtinputsupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport Input library

%package qtservicesupport-devel
Summary: Development files for QtPlatformSupport/Service

%description qtservicesupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport Service library

%package qtplatformcompositorsupport-devel
Summary: Development files for QtPlatformSupport/PlatformCompositor

%description qtplatformcompositorsupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport PlatformCompositor library

%package qteglsupport-devel
Summary: Development files for QtPlatformSupport/Egl

%description qteglsupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport Egl library

%package qtaccessibilitysupport-devel
Summary: Development files for QtPlatformSupport/Accessibility

%description qtaccessibilitysupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport Accessibility library

%package qtbootstrap-devel
Summary:    Development files for QtBootstrap

%description qtbootstrap-devel
This package contains the files necessary to develop
applications that use QtBootstrap

%package qtprintsupport
Summary:    The QtPrintSupport
Requires:   %{name}-qtcore = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtprintsupport
This package contains the QtPrintSupport library

%package qtprintsupport-devel
Summary:    Development files for QtPrintSupport
Requires:   %{name}-qtprintsupport = %{version}-%{release}

%description qtprintsupport-devel
This package contains the files necessary to develop
applications that use QtPrintSupport

%package qtconcurrent
Summary:    QtConcurrent library
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtconcurrent
This package contains the QtConcurrent library

%package qtconcurrent-devel
Summary:    Development files for QtConcurrent
Requires:   %{name}-qtconcurrent = %{version}-%{release}

%description qtconcurrent-devel
This package contains the files necessary to develop
applications that use QtConcurrent


##### Build section

%prep
%setup -q -n qt-%{version}

%build
touch .git

if [ -f "./config.status" ]; then
    echo "config.status already exists, not running configure to save time";
else
MAKEFLAGS=%{?_smp_mflags} \
./configure --disable-static \
    -confirm-license \
    -platform %{platform} \
    -prefix "%{_qt5_prefix}" \
    -bindir "%{_qt5_bindir}" \
    -libdir "%{_qt5_libdir}" \
    -docdir "%{_qt5_docdir}" \
    -headerdir "%{_qt5_headerdir}" \
    -datadir "%{_qt5_datadir}" \
    -plugindir "%{_qt5_plugindir}" \
    -importdir "%{_qt5_importdir}" \
    -translationdir "%{_qt5_translationdir}" \
    -sysconfdir "%{_sysconfdir}/xdg" \
    -examplesdir "%{_qt5_examplesdir}" \
    -archdatadir "%{_qt5_archdatadir}" \
    -testsdir "%{_libdir}/qt5/tests" \
    -qmldir "%{_qt5_qmldir}" \
    -libexecdir "%{_qt5_libexecdir}" \
    -opensource \
    -accessibility \
    -fontconfig \
    -no-sql-ibase \
    -no-sql-mysql \
    -no-sql-odbc \
    -no-sql-psql \
    -plugin-sql-sqlite \
    -no-sql-sqlite2 \
    -no-sql-tds \
    -system-sqlite \
    -system-zlib \
    -system-libpng \
    -system-libjpeg \
    -no-rpath \
    -optimized-qmake \
    -dbus-linked \
    -no-strip \
    -no-separate-debug-info \
    -verbose \
    -no-gtk \
    -opengl es2 \
    -no-opengles3 \
    -no-openvg \
    -nomake tests \
    -nomake examples \
    -no-xkbcommon \
    -no-xcb \
    -no-xinput2 \
%ifarch aarch64
	-no-pch \
%endif
    -qreal float \
    -journald
fi # config.status check
#%if ! 0%{?qt5_release_build}
#    -developer-build \
#%endif

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
#
# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_qt5_headerdir}/Qt

# Fix wrong path in pkgconfig files
find %{buildroot}%{_qt5_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;

# these manage to really royally screw up cmake
find %{buildroot}%{_libdir} -type f -name "*_*Plugin.cmake" \
-exec rm {} \;

find %{buildroot}%{_qt5_docdir}/ -type f -exec chmod ugo-x {} \;

# Make sure these are around
mkdir -p %{buildroot}%{_qt5_headerdir}/
mkdir -p %{buildroot}%{_qt5_datadir}/
mkdir -p %{buildroot}%{_qt5_plugindir}/
mkdir -p %{buildroot}%{_qt5_importdir}/
mkdir -p %{buildroot}%{_qt5_translationdir}/
mkdir -p %{buildroot}%{_qt5_examplesdir}/

#
%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_includedir}
%fdupes %{buildroot}/%{_datadir}


#### Pre/Post section

%post qtcore -p /sbin/ldconfig
%postun qtcore -p /sbin/ldconfig

%post qtdbus -p /sbin/ldconfig
%postun qtdbus -p /sbin/ldconfig

%post qtsql -p /sbin/ldconfig
%postun qtsql -p /sbin/ldconfig

%post qtnetwork -p /sbin/ldconfig
%postun qtnetwork -p /sbin/ldconfig

%post qtgui -p /sbin/ldconfig
%postun qtgui -p /sbin/ldconfig

%post qttest -p /sbin/ldconfig
%postun qttest -p /sbin/ldconfig

%post qtopengl -p /sbin/ldconfig
%postun qtopengl -p /sbin/ldconfig

%post qtxml -p /sbin/ldconfig
%postun qtxml -p /sbin/ldconfig

%post qtprintsupport -p /sbin/ldconfig
%postun qtprintsupport -p /sbin/ldconfig

%post qtwidgets -p /sbin/ldconfig
%postun qtwidgets -p /sbin/ldconfig

%post qtconcurrent -p /sbin/ldconfig
%postun qtconcurrent -p /sbin/ldconfig

%post plugin-platform-eglfs -p /sbin/ldconfig
%postun plugin-platform-eglfs -p /sbin/ldconfig


%files tools
%defattr(-,root,root,-)
%{_qt5_bindir}/moc
%{_qt5_bindir}/rcc
%{_qt5_bindir}/syncqt.pl
%{_qt5_bindir}/uic
%{_qt5_bindir}/qlalr
%{_qt5_bindir}/fixqt4headers.pl
%{_qt5_docdir}/*

%files qtcore
%defattr(-,root,root,-)
%dir %{_qt5_prefix}/
%dir %{_qt5_headerdir}/
%dir %{_qt5_datadir}/
%dir %{_qt5_bindir}/
%dir %{_qt5_plugindir}/
%dir %{_qt5_plugindir}/platforms/
%dir %{_qt5_importdir}/
%dir %{_qt5_translationdir}/
%dir %{_qt5_examplesdir}/
%{_qt5_libdir}/libQt5Core.so.*

%files qtcore-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtCore/
%{_qt5_libdir}/libQt5Core.prl
%{_qt5_libdir}/libQt5Core.so
%{_qt5_libdir}/pkgconfig/Qt5Core.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_core.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_core_private.pri
%{_qt5_libdir}/cmake/

%files qmake
%defattr(-,root,root,-)
%{_qt5_bindir}/qmake
%{_qt5_archdatadir}/mkspecs/aix-*/
%{_qt5_archdatadir}/mkspecs/android-*/
%{_qt5_archdatadir}/mkspecs/common/
%{_qt5_archdatadir}/mkspecs/cygwin-*/
%{_qt5_archdatadir}/mkspecs/darwin-*/
%{_qt5_archdatadir}/mkspecs/devices/
%{_qt5_archdatadir}/mkspecs/dummy/
%{_qt5_archdatadir}/mkspecs/features/
%{_qt5_archdatadir}/mkspecs/freebsd-*/
%{_qt5_archdatadir}/mkspecs/haiku-g++/
%{_qt5_archdatadir}/mkspecs/hpuxi-*
%{_qt5_archdatadir}/mkspecs/hurd-*/
%{_qt5_archdatadir}/mkspecs/integrity-*/
%{_qt5_archdatadir}/mkspecs/linux-*/
%{_qt5_archdatadir}/mkspecs/lynxos-*/
%{_qt5_archdatadir}/mkspecs/macx-*/
%{_qt5_archdatadir}/mkspecs/netbsd-*/
%{_qt5_archdatadir}/mkspecs/openbsd-*/
%{_qt5_archdatadir}/mkspecs/qconfig.pri
%{_qt5_archdatadir}/mkspecs/qdevice.pri
%{_qt5_archdatadir}/mkspecs/qmodule.pri
%{_qt5_archdatadir}/mkspecs/qnx-*/
%{_qt5_archdatadir}/mkspecs/solaris-*/
%{_qt5_archdatadir}/mkspecs/unsupported/
%{_qt5_archdatadir}/mkspecs/win32-*/
%{_qt5_archdatadir}/mkspecs/winrt-*/

%files qtdbus
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5DBus.so.*


%files qtdbus-devel
%defattr(-,root,root,-)
%{_qt5_bindir}/qdbuscpp2xml
%{_qt5_bindir}/qdbusxml2cpp
%{_qt5_headerdir}/QtDBus/
%{_qt5_libdir}/libQt5DBus.so
%{_qt5_libdir}/libQt5DBus.prl
%{_qt5_libdir}/pkgconfig/Qt5DBus.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dbus.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dbus_private.pri


%files qtgui
%defattr(-,root,root,-)
%dir %{_qt5_plugindir}/imageformats/
%dir %{_qt5_plugindir}/platforminputcontexts/
%dir %{_qt5_plugindir}/platformthemes/
%{_qt5_plugindir}/platformthemes/*
%{_qt5_libdir}/libQt5Gui.so.*


%files qtgui-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtGui/
%{_qt5_headerdir}/QtPlatformHeaders/
%{_qt5_libdir}/libQt5Gui.prl
%{_qt5_libdir}/libQt5Gui.so
%{_qt5_libdir}/pkgconfig/Qt5Gui.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_gui.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_gui_private.pri


%files qtnetwork
%defattr(-,root,root,-)
%dir %{_qt5_plugindir}/bearer/
%{_qt5_libdir}/libQt5Network.so.*


%files qtnetwork-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtNetwork/
%{_qt5_libdir}/libQt5Network.prl
%{_qt5_libdir}/libQt5Network.so
%{_qt5_libdir}/pkgconfig/Qt5Network.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_network.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_network_private.pri


%files qtopengl
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5OpenGL.so.*


%files qtopengl-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtOpenGL/
%{_qt5_headerdir}/QtOpenGLExtensions/
%{_qt5_libdir}/libQt5OpenGL.prl
%{_qt5_libdir}/libQt5OpenGLExtensions.prl
%{_qt5_libdir}/libQt5OpenGL.so
%{_qt5_libdir}/libQt5OpenGLExtensions.a
%{_qt5_libdir}/pkgconfig/Qt5OpenGL.pc
%{_qt5_libdir}/pkgconfig/Qt5OpenGLExtensions.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_opengl.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_opengl_private.pri
%{_qt5_archdatadir}/mkspecs/android-g++/qmake.conf
%{_qt5_archdatadir}/mkspecs/android-g++/qplatformdefs.h
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_openglextensions.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_openglextensions_private.pri


%files qtsql
%defattr(-,root,root,-)
%dir %{_qt5_plugindir}/sqldrivers/
%{_qt5_libdir}/libQt5Sql.so.*


%files qtsql-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtSql/
%{_qt5_libdir}/libQt5Sql.prl
%{_qt5_libdir}/libQt5Sql.so
%{_qt5_libdir}/pkgconfig/Qt5Sql.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_sql.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_sql_private.pri


%files qttest
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5Test.so.*

%files qttest-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtTest/
%{_qt5_libdir}/libQt5Test.prl
%{_qt5_libdir}/libQt5Test.so
%{_qt5_libdir}/pkgconfig/Qt5Test.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_testlib.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_testlib_private.pri

%files qtxml
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5Xml.so.*

%files qtxml-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtXml/
%{_qt5_libdir}/libQt5Xml.prl
%{_qt5_libdir}/libQt5Xml.so
%{_qt5_libdir}/pkgconfig/Qt5Xml.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_xml.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_xml_private.pri

%files qtwidgets
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5Widgets.so.*

%files qtwidgets-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtWidgets/
%{_qt5_libdir}/libQt5Widgets.prl
%{_qt5_libdir}/libQt5Widgets.so
%{_qt5_libdir}/pkgconfig/Qt5Widgets.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_widgets.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_widgets_private.pri

# Platform support libraries
%files qteventdispatchersupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtEventDispatcherSupport/
%{_qt5_libdir}/libQt5EventDispatcherSupport.prl
%{_qt5_libdir}/libQt5EventDispatcherSupport.a
#%{_qt5_libdir}/pkgconfig/Qt5EventDispatcherSupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_eventdispatcher_support_private.pri

%files qtdevicediscoverysupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtDeviceDiscoverySupport/
%{_qt5_libdir}/libQt5DeviceDiscoverySupport.prl
%{_qt5_libdir}/libQt5DeviceDiscoverySupport.a
#%{_qt5_libdir}/pkgconfig/Qt5DeviceDiscoverySupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_devicediscovery_support_private.pri

%files qtfbsupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtFbSupport/
%{_qt5_libdir}/libQt5FbSupport.prl
%{_qt5_libdir}/libQt5FbSupport.a
#%{_qt5_libdir}/pkgconfig/Qt5FbSupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_fb_support_private.pri

%files qtthemesupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtThemeSupport/
%{_qt5_libdir}/libQt5ThemeSupport.prl
%{_qt5_libdir}/libQt5ThemeSupport.a
#%{_qt5_libdir}/pkgconfig/Qt5ThemeSupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_theme_support_private.pri

%files qtfontdatabasesupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtFontDatabaseSupport/
%{_qt5_libdir}/libQt5FontDatabaseSupport.prl
%{_qt5_libdir}/libQt5FontDatabaseSupport.a
#%{_qt5_libdir}/pkgconfig/Qt5FontDatabaseSupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_fontdatabase_support_private.pri

%files qtinputsupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtInputSupport/
%{_qt5_libdir}/libQt5InputSupport.prl
%{_qt5_libdir}/libQt5InputSupport.a
#%{_qt5_libdir}/pkgconfig/Qt5InputSupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_input_support_private.pri

%files qtservicesupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtServiceSupport/
%{_qt5_libdir}/libQt5ServiceSupport.prl
%{_qt5_libdir}/libQt5ServiceSupport.a
#%{_qt5_libdir}/pkgconfig/Qt5ServiceSupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_service_support_private.pri

%files qtplatformcompositorsupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtPlatformCompositorSupport/
%{_qt5_libdir}/libQt5PlatformCompositorSupport.prl
%{_qt5_libdir}/libQt5PlatformCompositorSupport.a
#%{_qt5_libdir}/pkgconfig/Qt5PlatformCompositorSupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_platformcompositor_support_private.pri

%files qteglsupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtEglSupport/
%{_qt5_libdir}/libQt5EglSupport.prl
%{_qt5_libdir}/libQt5EglSupport.a
#%{_qt5_libdir}/pkgconfig/Qt5EglSupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_egl_support_private.pri

%files qtaccessibilitysupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtAccessibilitySupport/
%{_qt5_libdir}/libQt5AccessibilitySupport.prl
%{_qt5_libdir}/libQt5AccessibilitySupport.a
#%{_qt5_libdir}/pkgconfig/Qt5AccessibilitySupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_accessibility_support_private.pri

%files qtbootstrap-devel
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5Bootstrap.prl
%{_qt5_libdir}/libQt5Bootstrap.a
#%{_qt5_libdir}/pkgconfig/Qt5Bootstrap.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_bootstrap_private.pri

%files qtprintsupport
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5PrintSupport.so.*

%files qtprintsupport-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtPrintSupport/
%{_qt5_libdir}/libQt5PrintSupport.prl
%{_qt5_libdir}/libQt5PrintSupport.so
%{_qt5_libdir}/pkgconfig/Qt5PrintSupport.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_printsupport.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_printsupport_private.pri

%files qtconcurrent
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5Concurrent.so.*

%files qtconcurrent-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtConcurrent/
%{_qt5_libdir}/libQt5Concurrent.prl
%{_qt5_libdir}/libQt5Concurrent.so
%{_qt5_libdir}/pkgconfig/Qt5Concurrent.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_concurrent.pri
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_concurrent_private.pri




%files plugin-bearer-connman
%defattr(-,root,root,-)
%{_qt5_plugindir}/bearer/libqconnmanbearer.so

%files plugin-bearer-generic
%defattr(-,root,root,-)
%{_qt5_plugindir}/bearer/libqgenericbearer.so

%files plugin-bearer-nm
%defattr(-,root,root,-)
%{_qt5_plugindir}/bearer/libqnmbearer.so

%files plugin-imageformat-gif
%defattr(-,root,root,-)
%{_qt5_plugindir}/imageformats/libqgif.so

%files plugin-imageformat-ico
%defattr(-,root,root,-)
%{_qt5_plugindir}/imageformats/libqico.so

%files plugin-imageformat-jpeg
%defattr(-,root,root,-)
%{_qt5_plugindir}/imageformats/libqjpeg.so

#%files plugin-imageformat-tiff
#%defattr(-,root,root,-)
#%{_qt5_plugindir}/imageformats/libqtiff.so

%files plugin-platform-minimal
%defattr(-,root,root,-)
%{_qt5_plugindir}/platforms/libqminimal.so

%files plugin-platform-offscreen
%defattr(-,root,root,-)
%{_qt5_plugindir}/platforms/libqoffscreen.so

%files plugin-platform-eglfs
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5EglFSDeviceIntegration.so.*
%{_qt5_libdir}/libQt5EglFSDeviceIntegration.prl
%{_qt5_plugindir}/platforms/libqeglfs.so
%{_qt5_plugindir}/egldeviceintegrations/libqeglfs-emu-integration.so
%if %{with X11}
%{_qt5_plugindir}/egldeviceintegrations/libqeglfs-x11-integration.so
%endif
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_eglfsdeviceintegration_private.pri

%files plugin-platform-eglfs-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/QtEglFSDeviceIntegration/
%{_qt5_libdir}/libQt5EglFSDeviceIntegration.so

%files plugin-platform-minimalegl
%defattr(-,root,root,-)
%{_qt5_plugindir}/platforms/libqminimalegl.so

%files plugin-platform-linuxfb
%defattr(-,root,root,-)
%{_qt5_plugindir}/platforms/libqlinuxfb.so

%files plugin-platform-vnc
%defattr(-,root,root,-)
%{_qt5_plugindir}/platforms/libqvnc.so

%files plugin-printsupport-cups
%defattr(-,root,root,-)
%{_qt5_plugindir}/printsupport/libcupsprintersupport.so

%files plugin-sqldriver-sqlite
%defattr(-,root,root,-)
%{_qt5_plugindir}/sqldrivers/libqsqlite.so

%files plugin-platforminputcontext-ibus
%defattr(-,root,root,-)
%{_qt5_plugindir}/platforminputcontexts/libibusplatforminputcontextplugin.so

%files plugin-generic-evdev
%defattr(-,root,root,-)
%{_qt5_plugindir}/generic/libqevdev*plugin.so

%files plugin-generic-tuiotouch
%defattr(-,root,root,-)
%{_qt5_plugindir}/generic/libqtuiotouchplugin.so

#### No changelog section, separate $pkg.changes contains the history
