Summary:	Skin for fvwm2
Summary(pl):	Skórka do fvwm2
Name:		fvwm-crystal
Version:	0.8
Release:	0.1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.linuxpl.org/software/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
