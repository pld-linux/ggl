Summary:	ggl - High level game API.
Summary(pl):	ggl - "wysoko-poziomowe" API dla gier.
Name:		ggl
Version:	0.2.0
Release:	1
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ceu.fi.udc.es/pub/os/linux/gpul/%name-%version.tar.bz2
#Patch:		
BuildRequires:	libggi-devel
#Requires:	
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description

%description -l pl

%package devel
Summary:	ggl devel	
Summary(pl):	ggl devel
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki

%description devel

%description -l pl devel

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)

%files devel
%defattr(644,root,root,755)
%doc
#%attr(,,)
