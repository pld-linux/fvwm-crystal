
#	TODO:	- fix requires, because the new version needs some more,
#			  like Python for scripts or mpc/xmms-shell for music.

%define	_rc	RC1

Summary:	Theme for fvwm2
Summary(pl):	Skórka do fvwm2
Name:		fvwm-crystal
Version:	3.0
Release:	0.%{_rc}.1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://download.berlios.de/fvwm-crystal/%{name}-%{version}.%{_rc}.tar.gz
# Source0-md5:	ddc3437763b7dc6b140560a9ba829e8d
URL:		http://fvwm-crystal.berlios.de/
Requires:	aterm
Requires:	fvwm2 >= 2.5.13
Requires:	fvwm2-perl
Requires:	habak
Requires:	scrot
Requires:	xdaliclock
Requires:	trayer
Requires:	rox
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
%setup -q -n %{name}-%{version}.%{_rc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}

install bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a fvwm/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only note, not full GPL text
%doc doc/* AUTHORS INSTALL COPYING NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
