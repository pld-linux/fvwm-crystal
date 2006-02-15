Summary:	Desktop Environment
Summary(pl):	Graficzne ¶rodowisko robocze
Name:		fvwm-crystal
Version:	3.0.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://download.berlios.de/fvwm-crystal/%{name}-%{version}.tar.gz
# Source0-md5:	5830cce7456274efccc2e51fef8675ae
URL:		http://fvwm-crystal.berlios.de/
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FVWM-Crystal is a set of configuration files for F* Virtual Window 
Manager (FVWM), which can create for you a good looking, very 
functional desktop environment.

%description -l pl
FVWM-Crystal jest zestawem plików konfiguracyjnych dla F* Virtual 
Window Manager (FVWM), dziêki którym stworzone mo¿e byæ dobrze 
wygl±daj±ce i bardzo funkcjonalne ¶rodowisko robocze.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

make PREFIX=$RPM_BUILD_ROOT%{_prefix} install  

sed -i  's#installpath=.*$#installpath=/usr/share/fvwm-crystal/fvwm#g' $RPM_BUILD_ROOT%{_bindir}/%{name} 
#install -d $RPM_BUILD_ROOT%{_prefix}/share/xsessions
#install addons/fvwm-crystal.desktop $RPM_BUILD_ROOT%{_prefix}/share/xsessions/fvwm-crystal.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only note, not full GPL text
%doc doc/* AUTHORS INSTALL COPYING NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/fvwm/Applications
%{_datadir}/%{name}/fvwm/colorsets
%{_datadir}/%{name}/fvwm/components
%{_datadir}/%{name}/fvwm/config
%{_datadir}/%{name}/fvwm/decorations
%{_datadir}/%{name}/fvwm/icons
%{_datadir}/%{name}/fvwm/locale
%{_datadir}/%{name}/fvwm/preferences
%{_datadir}/%{name}/fvwm/recipes
%attr(755,root,root) %{_datadir}/%{name}/fvwm/scripts
%{_datadir}/%{name}/fvwm/wallpapers
#%{_prefix}/share/xsessions/fvwm-crystal.desktop
