Summary:	Theme for fvwm2
Summary(pl):	Skórka do fvwm2
Name:		fvwm-crystal
Version:	0.8
Release:	0.1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.linuxpl.org/software/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7217cb361ba42e3cdb1537c8a3cdcd84
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
install -d $RPM_BUILD_ROOT%{_datadir}/fvwm/
cp -r Crystal $RPM_BUILD_ROOT%{_datadir}/fvwm/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc
%{_datadir}/fvwm/Crystal/
