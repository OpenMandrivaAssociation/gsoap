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
make SOAPCPP2_IMPORTPATH="-DSOAPCPP2_IMPORT_PATH=\"\\\"%{_datadir}/%{name}/import\"\\\"" WSDL2H_IMPORTPATH="-DWSDL2H_IMPORT_PATH=\"\\\"%{_datadir}/%{name}/WS\"\\\""

%install
rm -rf %{buildroot}

mkdir -p %buildroot/%_datadir/%name
cp -R %name/import %buildroot/%_datadir/%name
cp -R %name/WS %buildroot/%_datadir/%name
cp -R %name/uddi2 %buildroot/%_datadir/%name
cp %name/stdsoap2.cpp %buildroot/%_datadir/%name
cp %name/stdsoap2.c %buildroot/%_datadir/%name
%makeinstall


%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt NOTES.txt README.txt *.html gpl.txt license.pdf %name/doc
%defattr(-,root,root)
%{_bindir}/soapcpp2
%{_bindir}/wsdl2h
%{_includedir}/stdsoap2.h
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
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


