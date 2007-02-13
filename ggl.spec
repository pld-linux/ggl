Summary:	ggl - High level game API
Summary(pl.UTF-8):	ggl - wysokopoziomowe API dla gier
Name:		ggl
Version:	0.2.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ceu.fi.udc.es/pub/os/linux/gpul/%{name}-%{version}.tar.bz2
# Source0-md5:	1b021f0723ba7004522fb75c91cf2297
BuildRequires:	libggi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
ggl - High level game API.

%description -l pl.UTF-8
ggl - wysokopoziomowe API dla gier.

%package devel
Summary:	ggl devel
Summary(pl.UTF-8):	ggl - część dla programistów
Group:		Development/Libraries

%description devel
ggl developement files.

%description devel -l pl.UTF-8
Pliki developerskie ggi.

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

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
