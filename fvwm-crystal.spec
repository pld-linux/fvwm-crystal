%define pre	pre1
Summary:	Theme for fvwm2
Summary(pl):	Skórka do fvwm2
Name:		fvwm-crystal
Version:	1.0
Release:	0.%{pre}.1
License:	GPL v2
Group:		X11/Window Managers
Source0:	ftp://ftp.linuxpl.org/%{name}/tarballs/%{name}-%{version}-%{pre}.tar.gz
# Source0-md5:	bdd9aa01f1e5665183b33c08fb7f9de6
URL:		http://www.linuxpl.org/software/fvwm-crystal/
BuildRequires:	rpm-perlprov
Requires:	fvwm2 >= 2.5.8
Requires:	fvwm2-perl
Requires:	scrot
Requires:	Esetroot
Requires:	aterm
Requires:	xdaliclock
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A theme for fvwm2.

%description -l pl
Skórka do fvwm2, bardzo rozbudowana.

%prep
%setup -q -n %{name}-%{version}-%{pre}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}

find -type d -name CVS | xargs rm -rf

mv bin/* $RPM_BUILD_ROOT%{_bindir}/
mv images config $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/[ACFIT]*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
