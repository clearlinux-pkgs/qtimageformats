#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtimageformats
Version  : 5.10.0
Release  : 5
URL      : http://download.qt.io/official_releases/qt/5.10/5.10.0/submodules/qtimageformats-everywhere-src-5.10.0.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.10/5.10.0/submodules/qtimageformats-everywhere-src-5.10.0.tar.xz
Summary  : A library of functions for manipulating MNG format files.
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 JasPer-2.0 LGPL-2.1 LGPL-3.0 W3C libtiff
Requires: qtimageformats-lib
BuildRequires : libwebp-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : python-dev
BuildRequires : qtbase-dev
BuildRequires : scons
BuildRequires : tiff-dev

%description
libmng - library for reading, writing, displaying and examing
Multiple-Image Network Graphics. MNG is the animation extension to the
popular PNG image-format.

%package dev
Summary: dev components for the qtimageformats package.
Group: Development
Requires: qtimageformats-lib
Provides: qtimageformats-devel

%description dev
dev components for the qtimageformats package.


%package lib
Summary: lib components for the qtimageformats package.
Group: Libraries

%description lib
lib components for the qtimageformats package.


%prep
%setup -q -n qtimageformats-everywhere-src-5.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
`pkg-config --variable=host_bins Qt5Core $(sed -n '/MODULE_VERSION */s///p' .qmake.conf 2>/dev/null)`/qmake --
test -r config.log && cat config.log

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QICNSPlugin.cmake
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QTgaPlugin.cmake
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QTiffPlugin.cmake
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QWbmpPlugin.cmake
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QWebpPlugin.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/imageformats/libqicns.so
/usr/lib64/qt5/plugins/imageformats/libqtga.so
/usr/lib64/qt5/plugins/imageformats/libqtiff.so
/usr/lib64/qt5/plugins/imageformats/libqwbmp.so
/usr/lib64/qt5/plugins/imageformats/libqwebp.so
