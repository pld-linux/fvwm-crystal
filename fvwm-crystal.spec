Summary:	Desktop Environment
Summary(pl.UTF-8):	Graficzne środowisko robocze
Name:		fvwm-crystal
Version:	3.0.6
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://download.gna.org/fvwm-crystal/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	82e2800882abb2c822519f1aa4dc0c72
URL:		http://www.fvwm-crystal.org/
BuildRequires:	sed >= 4.0
Requires:	ImageMagick
Requires:	aterm
Requires:	fvwm2 >= 2.5.13
Requires:	fvwm2-perl
Requires:	habak
Requires:	mpc
Requires:	mpd
Requires:	python
Requires:	rox
Requires:	scrot
Requires:	sudo
Requires:	trayer
Requires:	xmms-shell
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

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/share/xsessions
install addons/fvwm-crystal.desktop $RPM_BUILD_ROOT%{_prefix}/share/xsessions
rm -f   addons/fvwm-crystal.desktop

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__make} install-doc \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only note, not full GPL text
%doc doc/* AUTHORS INSTALL COPYING NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/fvwm
%dir %{_datadir}/%{name}/addons
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
%{_datadir}/xsessions/fvwm-crystal.desktop
