%define		glibmm_ver	2.54.0
%define		gtkmm3_ver	3.24.0
Summary:	Documentation and examples for gtkmm - C++ API for GTK+
Summary(pl.UTF-8):	Dokumentacja i przykłady do gtkmm - API C++ dla GTK+
Name:		gtkmm3-documentation
Version:	3.24.4
Release:	1
License:	FDL v1.2+ (documentation), GPL v2 (examples)
Group:		Documentation
Source0:	https://download.gnome.org/sources/gtkmm-documentation/3.24/gtkmm-documentation-%{version}.tar.xz
# Source0-md5:	e6a5ecca71dead8adb598fdc6e615dc3
URL:		https://www.gtkmm.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd50-xml
BuildRequires:	glibmm-devel >= %{glibmm_ver}
BuildRequires:	gtkmm3-devel >= %{gtkmm3_ver}
BuildRequires:	itstool
BuildRequires:	libstdc++-devel >= 6:5.1
BuildRequires:	mm-common >= 0.9.10
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	gtkmm3-apidocs >= %{gtkmm3_ver}
Suggests:	glibmm-devel >= %{glibmm_ver}
Suggests:	gtkmm3-devel >= %{gtkmm3_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the documentation and example programs for
gtkmm 3.x - C++ API for GTK+ 3.x.

%description -l pl.UTF-8
Ten pakiet zawiera dokumentację oraz programy przykładowe do
gtkmm 3.x - API C++ dla GTK+ 3.x.

%prep
%setup -q -n gtkmm-documentation-%{version}

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' examples/book/buildapp/step1/install-cmd.py

%build
mm-common-prepare --copy --force
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/gtkmm3-%{version}
cp -pr examples/{book,others,README} $RPM_BUILD_ROOT%{_examplesdir}/gtkmm3-%{version}

%find_lang gtkmm-tutorial --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gtkmm-tutorial.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.md
%{_docdir}/gtkmm-3.0/tutorial
%{_examplesdir}/gtkmm3-%{version}
