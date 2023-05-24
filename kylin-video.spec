Name:           kylin-video
Version:        3.1.4
Release:        3
Summary:        A powerful video player
License:        GPL-2.0+
URL:            https://gitee.com/openkylin/kylin-video
Source0:        kylin-video-3.1.4.tar.gz
Patch01:         0001-fix-compile-error-of-kylin-video.patch
Patch02:        0002-Repair-the-user-guide-does-not-work.patch

BuildRequires:  ffmpeg-devel
BuildRequires:  libcrystalhd-devel
BuildRequires:  ffmpegthumbnailer-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  libmediainfo-devel
BuildRequires:  mpv-libs-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  ukui-interface
BuildRequires:  wayland-devel
BuildRequires:  libX11-devel
BuildRequires:  libzen-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qtchooser
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  zlib-devel 
BuildRequires:  libkysdk-qtwidgets-devel
BuildRequires:  libkysdk-waylandhelper-devel
BuildRequires:  qtav-devel

Requires:       mesa-vdpau-drivers libcrystalhd-devel mpv ffmpegthumbnailer-devel libqtavwidgets

%description
Front-end for MPlayer and MPV Qt5 Mplayer and MPV front-end, with basic features like playing videos and audios to more advanced features.
It supports both x86 and ARM platform, and supports most of the audio and video formatsprep

%prep
%setup -q
%patch01 -p1
%patch02 -p1

%build
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build} -j4
popd 

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 

%files
%license debian/copyright
%{_bindir}/kylin-video
%{_datadir}/applications/kylin-video.desktop
%{_datadir}/kylin-user-guide/data/guide/kylin-video/*
%{_datadir}/kylin-video/translations/*


%changelog   
* Mon Mar 06 2023 peijiankang <peijiankang@kylinos.cn> - 3.1.4-3
- Repair the user guide does not work

* Tue Feb 07 2023 peijiankang <peijiankang@kylinos.cn> - 3.1.4-2
- add build debuginfo and debugsource

* Thu Dec 1 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.4-1
  update verison to 3.1.4(2022.12.01)

* Thu Sep 8 2022 huayadong <huayadong@kylinos.cn> - 3.1.3-7
  Fix the window jump problem when dragging the window

* Mon Aug 22 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.3-6
- Fix about background not changing with style 

* Mon Aug 22 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.3-5
- modify version is error 

* Fri Aug 19 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.3-4
- add tinyxml2 requires

* Thu Jun 9 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.3-3
- Fix the problem of the help manual button

* Wed Jun 8 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.3-2
- add copyright file

* Wed Jun 8 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.3-1
- update version to 3.1.3

* Wed Sep 8 2021 peijiankang <peijiankang@kylinos.cn> - 2.1.1.1-2
- add mpv requires

* Fri Aug 20 2021 tongzong <2505108658@qq.com> - 2.1.1.1-1   
- package init

