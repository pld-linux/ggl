Summary:	ggl - High level game API
Summary(pl):	ggl - wysokopoziomowe API dla gier
Name:		ggl
Version:	0.2.0
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ceu.fi.udc.es/pub/os/linux/gpul/%name-%version.tar.bz2
BuildRequires:	libggi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
ggl - High level game API.

%description -l pl
ggl - wysokopoziomowe API dla gier.

%package devel
Summary:	ggl devel
Summary(pl):	ggl - czЙ╤Ф dla programistСw
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки

%description devel
ggl developement files.

%description devel -l pl
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
