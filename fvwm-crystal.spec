Summary:	Theme for fvwm2
Summary(pl):	Skórka do fvwm2
Name:		fvwm-crystal
Version:	20040929
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://fvwm-crystal.berlios.de/files/files/fvwm-crystal/%{name}-%{version}.tar.gz
# Source0-md5:	067558677408dfa2f846a2c343f5705d
Patch0:		%{name}-paths.patch
URL:		http://fvwm-crystal.berlios.de/
Requires:	aterm
Requires:	fvwm2 >= 2.5.8
Requires:	fvwm2-perl
Requires:	habak
Requires:	scrot
Requires:	xdaliclock
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A theme for fvwm2.

%description -l pl
Skórka do fvwm2, bardzo rozbudowana.

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
