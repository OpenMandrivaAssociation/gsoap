%define ver 2.8
%define subver 14

Name:		gsoap
Version:	%{ver}.%{subver}
Release:	1
Summary:	Development tookit for SOAP/XML Web services in C/C++
Group:		Development/Other
License:	gSOAP Public License
Source0:	http://prdownloads.sourceforge.net/gsoap2/%{name}_%{version}.zip
Patch0:		Makefile.am.patch
Patch2:		gsoap-2.8-automake-1.13.patch
URL:		http://www.cs.fsu.edu/~engelen/soap.html
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	flex

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
%setup -q -n %{name}-%{ver}
{
cd gsoap
#%patch0 -p0 -b .fPIC
cd -
}
%patch2 -p1 -b .automake13~
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
%configure --enable-debug

# keep a copy of source code (used by some TPM tools for Intel Classmate)
rm -rf %{name}-source
cp -a . ../%{name}-source
mv ../%{name}-source .

make SOAPCPP2_IMPORTPATH="-DSOAPCPP2_IMPORT_PATH=\"\\\"%{_datadir}/%{name}/import\"\\\"" WSDL2H_IMPORTPATH="-DWSDL2H_IMPORT_PATH=\"\\\"%{_datadir}/%{name}/WS\"\\\""

%install
rm -rf %{buildroot}

mkdir -p %buildroot/%_datadir/%name
cp -R %name/import %buildroot/%_datadir/%name
cp -R %name/WS %buildroot/%_datadir/%name
cp -R %name/uddi2 %buildroot/%_datadir/%name
cp %name/stdsoap2.cpp %buildroot/%_datadir/%name
cp %name/stdsoap2.c %buildroot/%_datadir/%name
%makeinstall STRIP=/bin/true

install -d %{buildroot}%{_prefix}/src/
cp -a %{name}-source %{buildroot}%{_prefix}/src/%{name}

find %{buildroot} -type d -perm 0744 -exec chmod 0755 '{}' \;
find %{buildroot} -type f -perm 0744 -exec chmod 0644 '{}' \;
find %{buildroot}%{_prefix}/src -name "*.xml" -exec chmod 0644 '{}' \;
 
%files
%defattr(644,root,root,755)
%doc LICENSE.txt NOTES.txt README.txt *.html license.pdf %name/doc
%attr(0755,root,root) %{_bindir}/soapcpp2
%attr(0755,root,root) %{_bindir}/wsdl2h
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


%changelog
* Tue Jul 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.8.9-1
+ Revision: 810048
- version update 2.8.9

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.8.8-1
+ Revision: 786781
- version update 2.8.8

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.7.17-2
+ Revision: 664932
- mass rebuild

* Fri Sep 17 2010 Angelo Naselli <anaselli@mandriva.org> 2.7.17-1mdv2011.0
+ Revision: 579205
- New version 2.7.17

* Thu Apr 15 2010 Angelo Naselli <anaselli@mandriva.org> 2.7.16-1mdv2010.1
+ Revision: 535062
- new version 2.7.16

* Thu Apr 08 2010 Eugeni Dodonov <eugeni@mandriva.com> 2.7.15-3mdv2010.1
+ Revision: 533161
- P2: build properly with new openssl 1.0.0.

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 2.7.15-2mdv2010.1
+ Revision: 511571
- rebuilt against openssl-0.9.8m

* Fri Nov 20 2009 Angelo Naselli <anaselli@mandriva.org> 2.7.15-1mdv2010.1
+ Revision: 467734
- new version 2.7.15

* Wed Sep 09 2009 Angelo Naselli <anaselli@mandriva.org> 2.7.14-1mdv2010.0
+ Revision: 435055
- New version 2.7.14

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.7.13-2mdv2010.0
+ Revision: 425050
- rebuild

* Sun Mar 22 2009 Angelo Naselli <anaselli@mandriva.org> 2.7.13-1mdv2009.1
+ Revision: 360085
- new version 2.7.13

* Wed Feb 04 2009 Olivier Blin <blino@mandriva.org> 2.7.12-2mdv2009.1
+ Revision: 337458
- add gsoap-source package (to be used by some TPM tools for Intel Classmate)
- fix fprintf with no string literal (sourceforce request #2564094)

* Thu Oct 23 2008 Angelo Naselli <anaselli@mandriva.org> 2.7.12-1mdv2009.1
+ Revision: 296729
- new version 2.7.12

* Thu Oct 23 2008 Angelo Naselli <anaselli@mandriva.org> 2.7.11-3mdv2009.1
+ Revision: 296716
- Added -fPIC option to use it on x86_64

* Wed Jul 30 2008 Angelo Naselli <anaselli@mandriva.org> 2.7.11-2mdv2009.0
+ Revision: 254911
- Updated with a new upstream tarball

* Mon Jul 28 2008 Angelo Naselli <anaselli@mandriva.org> 2.7.11-1mdv2009.0
+ Revision: 251135
- New version 2.7.11

* Thu Jun 26 2008 Angelo Naselli <anaselli@mandriva.org> 2.7.10-3mdv2009.0
+ Revision: 229303
- Fixed Url

* Thu Jun 26 2008 Angelo Naselli <anaselli@mandriva.org> 2.7.10-2mdv2009.0
+ Revision: 229282
- Fixed bug #41665: gsoap is looking for file in rpm build environnement
- Moved WS and import under /usr/share/gsoap

* Tue Jan 29 2008 Angelo Naselli <anaselli@mandriva.org> 2.7.10-1mdv2008.1
+ Revision: 159685
- New version 2.7.10

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 12 2007 Angelo Naselli <anaselli@mandriva.org> 2.7.9l-1mdv2008.1
+ Revision: 108262
- new version 2.7.9l

* Tue Aug 28 2007 Angelo Naselli <anaselli@mandriva.org> 2.7.9k-1mdv2008.0
+ Revision: 72614
- new version 2.7.9k

* Wed Aug 01 2007 Angelo Naselli <anaselli@mandriva.org> 2.7.9j-1mdv2008.0
+ Revision: 57285
- New version 2.7.9j

* Thu Jul 12 2007 Angelo Naselli <anaselli@mandriva.org> 2.7.9i-1mdv2008.0
+ Revision: 51688
- New version 2.7.9i

* Mon Jul 02 2007 Angelo Naselli <anaselli@mandriva.org> 2.7.9h-1mdv2008.0
+ Revision: 47086
- New version 2.7.9h

* Fri Apr 27 2007 Angelo Naselli <anaselli@mandriva.org> 2.7.9f-1mdv2008.0
+ Revision: 18630
- New version 2.7.9f

* Wed Apr 18 2007 Angelo Naselli <anaselli@mandriva.org> 2.7.9e-1mdv2008.0
+ Revision: 14846
- new version 2.7.9e

