Summary:	ggl - High level game API.
Summary(pl):	ggl - "wysoko-poziomowe" API dla gier.
Name:		ggl
Version:	0.2.0
Release:	1
License:	GPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ceu.fi.udc.es/pub/os/linux/gpul/%name-%version.tar.bz2
Patch0:		
BuildRequires:	libggi-devel
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description

%description -l pl

%package devel
Summary:	ggl devel	
Summary(pl):	ggl devel
Group:		Development/Libraries
Group(fr):	Development/Librairies
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
