
#	TODO:	
#

Summary:	Desktop Environment
Summary(pl):	Graficzne �rodowisko robocze
Name:		fvwm-crystal
Version:	3.0
Release:	0.1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://download.berlios.de/fvwm-crystal/%{name}-%{version}.tar.gz
# Source0-md5:	412f9b6148e35f07b7f1e76759f781b5
URL:		http://fvwm-crystal.berlios.de/
Requires:	aterm
Requires:	fvwm2 >= 2.5.13
Requires:	fvwm2-perl
Requires:	habak
Requires:	ImageMagick
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
FVWM-Crystal jest zestawem plik�w konfiguracyjnych dla F* Virtual 
Window Manager (FVWM), dzi�ki kt�rym stworzone mo�e by� dobrze 
wygl�daj�ce i bardzo funkcjonalne �rodowisko robocze.

%prep
%setup -q -n %{name}-%{version}

%build

%configure --prefix=%{_prefix} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
    bindir=$RPM_BUILD_ROOT%{_prefix}/bin \
    datadir=$RPM_BUILD_ROOT%{_prefix}/share
    
sed -i 's#\%\%\%INSTALLPATH\%\%\%#"%{_datadir}/%{name}/fvwm"#g' $RPM_BUILD_ROOT%{_bindir}/%{name}

install -d $RPM_BUILD_ROOT%{_prefix}/share/xsessions/
install addons/fvwm-crystal.desktop $RPM_BUILD_ROOT%{_prefix}/share/xsessions/fvwm-crystal.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only note, not full GPL text
%doc doc/* AUTHORS INSTALL COPYING NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_prefix}/share/xsessions/fvwm-crystal.desktop
