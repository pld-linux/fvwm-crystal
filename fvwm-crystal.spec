Summary:	Theme for fvwm2
Summary(pl):	Skórka do fvwm2
Name:		fvwm-crystal
Version:	0.8
Release:	0.1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://www.linuxpl.org/software/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7217cb361ba42e3cdb1537c8a3cdcd84
BuildRequires:	rpm-perlprov
Requires:	fvwm2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A theme for fvwm2.

%description -l pl
Skórka do fvwm2, bardzo rozbudowana.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/fvwm

cp -r Crystal $RPM_BUILD_ROOT%{_datadir}/fvwm
find $RPM_BUILD_ROOT%{_datadir}/fvwm/ -type d -name CVS | xargs rm -rf

install -D addons/crystal-wallpaper $RPM_BUILD_ROOT%{_bindir}/crystal-wallpaper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/[ADFIMRTcr]* addons/Xresources
%attr(755,root,root) %{_bindir}/*
%{_datadir}/fvwm/Crystal
