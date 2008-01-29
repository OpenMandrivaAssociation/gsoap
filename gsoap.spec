%define ver 2.7
%define subver 10
%define release  %mkrel 1

Name: gsoap
Version: %{ver}.%{subver}
Release: %release
Summary: Development tookit for SOAP/XML Web services in C/C++
Group: Development/Other
License: gSOAP Public License
Source: http://prdownloads.sourceforge.net/gsoap2/%{name}_%{version}.tar.bz2
URL: http://www.cs.fsu.edu/~engelen/soap.html\
BuildRequires: automake
BuildRequires: bison
BuildRequires: libstdc++-devel openssl-devel zlib-devel
BuildRequires: flex
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
The gSOAP Web services development toolkit offers an XML to C/C++ language
binding to ease the development of SOAP/XML Web services in C and C/C++.

%prep
rm -rf %{buildroot}
%setup -q -n %{name}-%{ver}

%build
%configure
make

%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %buildroot/%_includedir/import
cp -R %name/import %buildroot/%_includedir

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %name/uddi2/uddi2-typemap.dat %name/WS %name/stdsoap2.cpp %name/stdsoap2.c LICENSE.txt NOTES.txt README.txt *.html gpl.txt license.pdf %name/doc
%defattr(-,root,root)
%{_bindir}/soapcpp2
%{_bindir}/wsdl2h
%{_includedir}/stdsoap2.h
%{_includedir}/import/*
%{_libdir}/libgsoap++.a
%{_libdir}/libgsoap.a
%{_libdir}/libgsoapck++.a
%{_libdir}/libgsoapck.a
%{_libdir}/libgsoapssl++.a
%{_libdir}/libgsoapssl.a
%{_libdir}/pkgconfig/gsoapssl++.pc
%{_libdir}/pkgconfig/gsoapssl.pc
%{_libdir}/pkgconfig/gsoap++.pc
%{_libdir}/pkgconfig/gsoap.pc
%{_libdir}/pkgconfig/gsoapck++.pc
%{_libdir}/pkgconfig/gsoapck.pc


