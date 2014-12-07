%define ver 2.8
%define subver 18

Summary:	Development tookit for SOAP/XML Web services in C/C++
Name:		gsoap
Version:	%{ver}.%{subver}
Release:	2
Group:		Development/Other
License:	gSOAP Public License
Url:		http://www.cs.fsu.edu/~engelen/soap.html
Source0:	http://prdownloads.sourceforge.net/gsoap2/%{name}_%{version}.zip
Source100:	%{name}.rpmlintrc

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	stdc++-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)

%description
The gSOAP Web services development toolkit offers an XML to C/C++ language
binding to ease the development of SOAP/XML Web services in C and C/C++.

%package	source
Summary:	Source files of %{name}
Group:		Development/C

%description	source
The gSOAP Web services development toolkit offers an XML to C/C++ language
binding to ease the development of SOAP/XML Web services in C and C/C++.

This package contains the source code.

%prep
%setup -qn %{name}-%{ver}
aclocal
automake --add-missing
autoreconf
# remove the binaries
rm -rf gsoap/bin
find . -name "*.o" -exec rm {} \;
rm -rf gsoap/ios_plugin/examples/GeoIPService/build
rm -rf gsoap/ios_plugin/examples/Calc/build
rm -rf gsoap/samples/wcf/WS/DualHttp/calculator
rm -rf gsoap/samples/link++/xmas

%build
%configure

# keep a copy of source code (used by some TPM tools for Intel Classmate)
rm -rf %{name}-source
cp -a . ../%{name}-source
mv ../%{name}-source .

make SOAPCPP2_IMPORTPATH="-DSOAPCPP2_IMPORT_PATH=\"\\\"%{_datadir}/%{name}/import\"\\\"" WSDL2H_IMPORTPATH="-DWSDL2H_IMPORT_PATH=\"\\\"%{_datadir}/%{name}/WS\"\\\""

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -R %{name}/import %{buildroot}/%{_datadir}/%{name}
cp -R %{name}/WS %{buildroot}/%{_datadir}/%{name}
cp -R %{name}/uddi2 %{buildroot}/%{_datadir}/%{name}
cp %{name}/stdsoap2.cpp %{buildroot}/%{_datadir}/%{name}
cp %{name}/stdsoap2.c %{buildroot}/%{_datadir}/%{name}
%makeinstall STRIP=/bin/true

install -d %{buildroot}%{_prefix}/src/
cp -a %{name}-source %{buildroot}%{_prefix}/src/%{name}

find %{buildroot} -type d -perm 0744 -exec chmod 0755 '{}' \;
find %{buildroot} -type f -perm 0744 -exec chmod 0644 '{}' \;
find %{buildroot}%{_prefix}/src -name "*.xml" -exec chmod 0644 '{}' \;
 
%files
%doc LICENSE.txt NOTES.txt README.txt *.html license.pdf %{name}/doc
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

%files source
%{_prefix}/src/%{name}

