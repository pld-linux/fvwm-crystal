Summary:	Theme for fvwm2
Summary(pl):	Skórka do fvwm2
Name:		fvwm-crystal
Version:	20050306
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://fvwm-crystal.berlios.de/files/files/fvwm-crystal/%{name}-%{version}.tar.gz
# Source0-md5:	fae57bbbfb34ec7cfde92364b8edad5a
# Patch0:		%{name}-paths.patch
URL:		http://fvwm-crystal.berlios.de/
Requires:	aterm
Requires:	fvwm2 >= 2.5.8
Requires:	fvwm2-perl
Requires:	habak
Requires:	scrot
Requires:	xdaliclock
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
# %patch0 -p1

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
