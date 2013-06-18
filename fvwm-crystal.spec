Summary:	Desktop Environment
Summary(pl.UTF-8):	Graficzne środowisko robocze
Name:		fvwm-crystal
Version:	3.2.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://downloads.sourceforge.net/fvwm-crystal/%{name}-%{version}.tar.gz
# Source0-md5:	80027c0f487ebc1826659850c117ceb3
Patch0:		%{name}-temperature.patch
URL:		http://www.fvwm-crystal.org/
BuildRequires:	sed >= 4.0
Requires:	ImageMagick
Requires:	Thunar
Requires:	alsa-utils
Requires:	awk
Requires:	bc
Requires:	coreutils
Requires:	feh
Requires:	fvwm2 >= 2.6.5
Requires:	fvwm2-perl
Requires:	gksu
Requires:	mplayer
Requires:	mrxvt
Requires:	sed
Requires:	stalonetray
Requires:	sudo
Requires:	urxvt
Requires:	xorg-app-transset
Requires:	xorg-app-xcompmgr
Requires:	xorg-app-xrandr
Requires:	xorg-app-xwd
Requires:	xscreensaver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FVWM-Crystal is a set of configuration files for F* Virtual Window
Manager (FVWM), which can create for you a good looking, very
functional desktop environment.

%description -l pl.UTF-8
FVWM-Crystal jest zestawem plików konfiguracyjnych dla F* Virtual
Window Manager (FVWM), dzięki którym stworzone może być dobrze
wyglądające i bardzo funkcjonalne środowisko robocze.

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -dv $RPM_BUILD_ROOT%{_bindir}
install -dv $RPM_BUILD_ROOT%{_datadir}/%{name}/fvwm
install -dv $RPM_BUILD_ROOT%{_datadir}/xsessions
install -dv $RPM_BUILD_ROOT%{_sysconfdir}/X11/Sessions
install -dv $RPM_BUILD_ROOT%{_mandir}/man1
install -dv $RPM_BUILD_ROOT%{_docdir}/%{name}
install -dv $RPM_BUILD_ROOT%{_datadir}/%{name}/addons

cp -v bin/fvwm-crystal* $RPM_BUILD_ROOT%{_bindir}
cp -rv fvwm/* $RPM_BUILD_ROOT%{_datadir}/%{name}/fvwm
cp -v man/* $RPM_BUILD_ROOT%{_mandir}/man1
cp -rv addons/* $RPM_BUILD_ROOT%{_datadir}/%{name}/addons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only note, not full GPL text
%doc doc/* AUTHORS Contribute COPYING NEWS ChangeLog Export.README README INSTALL
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/fvwm
%dir %{_datadir}/%{name}/addons
%dir %{_sysconfdir}/X11/Sessions
%attr(755,root,root) %{_datadir}/%{name}/fvwm/Applications
%{_datadir}/%{name}/fvwm/colorsets
%{_datadir}/%{name}/fvwm/components
%{_datadir}/%{name}/fvwm/config
%{_datadir}/%{name}/fvwm/decorations
%{_datadir}/%{name}/fvwm/icons
%{_datadir}/%{name}/fvwm/locale
%{_datadir}/%{name}/fvwm/preferences
%{_datadir}/%{name}/fvwm/recipes
%{_datadir}/%{name}/addons/*
%attr(755,root,root) %{_datadir}/%{name}/fvwm/scripts
%{_datadir}/%{name}/fvwm/wallpapers
%{_mandir}/man1/*.1*
