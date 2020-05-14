#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtimageformats
Version  : 5.15.0
Release  : 27
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.0/submodules/qtimageformats-everywhere-src-5.15.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.0/submodules/qtimageformats-everywhere-src-5.15.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 libtiff
Requires: qtimageformats-lib = %{version}-%{release}
Requires: qtimageformats-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : buildreq-scons
BuildRequires : libwebp-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : qtbase-dev
BuildRequires : tiff-dev

%description
[Useful links]
* http://en.wikipedia.org/wiki/Apple_Icon_Image_format - Wikipedia article about ICNS format
* http://www.macdisk.com/maciconen.php - Unofficial tech info about the format

%package dev
Summary: dev components for the qtimageformats package.
Group: Development
Requires: qtimageformats-lib = %{version}-%{release}
Provides: qtimageformats-devel = %{version}-%{release}
Requires: qtimageformats = %{version}-%{release}

%description dev
dev components for the qtimageformats package.


%package lib
Summary: lib components for the qtimageformats package.
Group: Libraries
Requires: qtimageformats-license = %{version}-%{release}

%description lib
lib components for the qtimageformats package.


%package license
Summary: license components for the qtimageformats package.
Group: Default

%description license
license components for the qtimageformats package.


%prep
%setup -q -n qtimageformats-everywhere-src-5.15.0
cd %{_builddir}/qtimageformats-everywhere-src-5.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1589475387
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtimageformats
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtimageformats/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtimageformats/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtimageformats/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtimageformats/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/LICENSE.GPLv2 %{buildroot}/usr/share/package-licenses/qtimageformats/87d17bf05b5aba91a2091b17a89336fb6a8954e2
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/LICENSE.GPLv3 %{buildroot}/usr/share/package-licenses/qtimageformats/7d974f34cf5fd474f0fdf6ebc8d410ea5c8b72de
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtimageformats/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/LICENSE.LGPLv21 %{buildroot}/usr/share/package-licenses/qtimageformats/fe04fe44c5e1a407572a5cca79d39afd674bccf3
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtimageformats/d8b489a3c3d500a6601181e3db39bec6124b86fc
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/src/3rdparty/libtiff/COPYRIGHT %{buildroot}/usr/share/package-licenses/qtimageformats/a2f64f2a85f5fd34bda8eb713c3aad008adbb589
cp %{_builddir}/qtimageformats-everywhere-src-5.15.0/src/3rdparty/libwebp/COPYING %{buildroot}/usr/share/package-licenses/qtimageformats/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9
%make_install

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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtimageformats/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtimageformats/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9
/usr/share/package-licenses/qtimageformats/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtimageformats/7d974f34cf5fd474f0fdf6ebc8d410ea5c8b72de
/usr/share/package-licenses/qtimageformats/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtimageformats/87d17bf05b5aba91a2091b17a89336fb6a8954e2
/usr/share/package-licenses/qtimageformats/a2f64f2a85f5fd34bda8eb713c3aad008adbb589
/usr/share/package-licenses/qtimageformats/d8b489a3c3d500a6601181e3db39bec6124b86fc
/usr/share/package-licenses/qtimageformats/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtimageformats/f45ee1c765646813b442ca58de72e20a64a7ddba
/usr/share/package-licenses/qtimageformats/fe04fe44c5e1a407572a5cca79d39afd674bccf3
