Summary: Multitech IntelligentSerialInternal (ISI) Support Tools
Summary(pt_BR): Ferramentas de suporte a Multitech IntelligentSerialInternal (ISI)
Summary(es): Multitech IntelligentSerialInternal (ISI) Support Tools
Name: isicom
Version: 1.0
Release: 2cl
Copyright: GPL (not Firmware)
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
URL: http://www.multitech.com/
Source: isicom.tar.gz
Patch0: isicom-make.patch
BuildRoot: /var/tmp/%{name}-%{PACKAGE_VERSION}-root

%description
Binary images and loader for Multitech IntelligentSerialInternal (ISI) data
files.

%description -l pt_BR
Imagens binárias e "loader" para a Multitech IntelligentSerialInternal (ISI)

%description -l es
Binary images and loader for Multitech IntelligentSerialInternal (ISI) data
files.

%prep
%setup -n isicom
%patch0 -p1

%build
make clean
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{share/isicom,sbin}
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 firmld $RPM_BUILD_ROOT/usr/sbin
#install -m 755 isild $RPM_BUILD_ROOT/etc/rc.d/init.d/
install -m 644 *.bin $RPM_BUILD_ROOT/usr/share/isicom

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (644, root, root)
%attr (755,root,root) /usr/sbin/firmld
/usr/share/isicom/*.bin

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- sanitized the spec file
