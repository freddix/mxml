Summary:	Small XML parsing library
Name:		mxml
Version:	2.7
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.easysw.com/pub/mxml/2.7/%{name}-%{version}.tar.gz
# Source0-md5:	76f2ae49bf0f5745d5cb5d9507774dc9
Patch0:		%{name}-link.patch
URL:		http://www.easysw.com/~mike/mxml/software.php
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mini-XML is a small XML parsing library.

%package devel
Summary:	Header files for mxml library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for mxml library.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/mxml

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libmxml.so.1
%attr(755,root,root) %{_libdir}/libmxml.so.1.5
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_libdir}/libmxml.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*

