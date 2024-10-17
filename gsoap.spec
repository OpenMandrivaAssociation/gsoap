%define ver %(echo %{version} |cut -d. -f1-2)

Summary:	Development tookit for SOAP/XML Web services in C/C++
Name:		gsoap
Version:	2.8.134
Release:	1
Group:		Development/Other
License:	gSOAP Public License
Url:		https://www.cs.fsu.edu/~engelen/soap.html
Source0:	https://downloads.sourceforge.net/project/gsoap2/gsoap_%{version}.zip
Source100:	%{name}.rpmlintrc

Patch0:	Makefile.am.patch
Patch1:	gsoap-2.8.66-ssl.patch
#Patch2:	gsoap-2.8-automake.patch
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
%autosetup -p0 -n %{name}-%{ver}

# make automake more happy
sed -i -e 's,\(^AM_INIT_AUTOMAKE(\[\),\1subdir-objects ,' configure.ac

# fix build with glibc >= 2.27
sed -i -e 's,xlocale.h,locale.h,g' ./gsoap/stdsoap2.h

# remove the binaries
rm -rf gsoap/bin

find . -name "*.o" -exec rm {} \;
rm -rf gsoap/ios_plugin/examples/GeoIPService/build
rm -rf gsoap/ios_plugin/examples/Calc/build
rm -rf gsoap/samples/wcf/WS/DualHttp/calculator
rm -rf gsoap/samples/link++/xmas

%build
autoreconf -vfi
%configure --enable-shared

# keep a copy of source code (used by some TPM tools for Intel Classmate)
rm -rf %{name}-source
cp -a . ../%{name}-source
mv ../%{name}-source .

# remove pre-built binaries and libraries in source tree
find %{name}-source -name "*.so" -exec rm {} \;
find %{name}-source -name "*.o" -exec rm {} \;
find %{name}-source -name "*.dll" -exec rm {} \;
find %{name}-source -name "*.exe" -exec rm {} \;
find %{name}-source -name "*.la" -exec rm {} \;
find %{name}-source -name "*.a" -exec rm {} \;
find %{name}-source -name "*.pdf" -exec rm {} \;
find %{name}-source -name "*.doc" -exec rm {} \;

# next files make debuginfo failing:
rm -rf %{name}-source/%{name}/ios_plugin/examples/Calc/build/Debug-iphonesimulator/Calc.app/Calc
rm -rf %{name}-source/%{name}/ios_plugin/examples/GeoIPService/build/Debug-iphonesimulator/GeoIPService.app/GeoIPService
rm -rf %{name}-source/%{name}/samples/link++/xmas
rm -rf %{name}-source/%{name}/samples/wcf/WS/DualHttp/calculator

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
%doc LICENSE.txt NOTES.txt README.txt license.pdf %{name}/doc
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
