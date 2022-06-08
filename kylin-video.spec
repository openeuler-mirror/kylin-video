%global debug_package %{nil}

Name:           kylin-video
Version:        3.1.3
Release:        1
Summary:        A powerful video player
License:        GPL-2.0-or-later
URL:            https://github.com/UbuntuKylin/kylin-video
Source0:        kylin-video-3.1.3.tar.gz
Patch1:         0001-modify-compile-error-of-kylin-video.patch

BuildRequires:  qt5-devel
BuildRequires:  qtchooser
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  libX11-devel
BuildRequires:  libcrystalhd-devel
BuildRequires:  zlib-devel 
BuildRequires:  ffmpeg-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  mpv-libs-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  wayland-devel
BuildRequires:  libzen-devel  
BuildRequires:  libmediainfo-devel
BuildRequires:  ffmpegthumbnailer-devel
BuildRequires:  ukui-interface

Requires:       mesa-vdpau-drivers libcrystalhd-devel mpv ffmpegthumbnailer-devel


%description
Front-end for MPlayer and MPV Qt5 Mplayer and MPV front-end, with basic features like playing videos and audios to more advanced features.
It supports both x86 and ARM platform, and supports most of the audio and video formatsprep

%prep
%setup -q
%patch1 -p1


%build
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd 

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 

%files
%{_bindir}/kylin-video-new
%{_datadir}/applications/kylin-video.desktop
%{_datadir}/kylin-user-guide/data/guide/kylin-video/*
%{_datadir}/kylin-video/translations/kylin-video_zh_CN.qm


%changelog   
* Wed Jun 8 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.3-1
- update version to 3.1.3

* Wed Sep 8 2021 peijiankang <peijiankang@kylinos.cn> - 2.1.1.1-2
- add mpv requires

* Fri Aug 20 2021 tongzong <2505108658@qq.com> - 2.1.1.1-1   
- package init

