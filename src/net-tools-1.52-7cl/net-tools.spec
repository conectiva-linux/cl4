Summary: The basic tools for setting up networking.
Summary(pt_BR): Ferramentas básicas de Rede
Summary(es): Herramientas básicas de Red
Name: net-tools
Version: 1.52
Release: 7cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source0: http://www.tazenda.demon.co.uk/phil/net-tools/net-tools-%{version}.tar.bz2
Source1: net-tools-1.48-config.h
Source2: net-tools-pt_BR.po
Source700: net-tools-man-pt_BR.tar
Patch0: net-tools-1.51-jbj.patch
Patch1: net-tools-1.51-masq_vpn_protos.patch
Patch2: net-tools-1.52-bufovr.patch
BuildRoot: /var/tmp/%{name}-root
Serial: 2
# XXX dunno minimum required kernel version
#BuildRequires: kernel-headers >= 2.1.100

%description
The net-tools package contains the basic tools needed for setting
up networking:  arp, rarp, ifconfig, netstat, ethers and route.

%description -l pt_BR
Essa é uma coleção de ferramentas básicas necessárias para a
configuração da rede em uma máquina Linux. Inclui ifconfig, route,
netstat, rarp, e algumas outras ferramentas menores.

%description -l es
Esta es una colección de herramientas básicas necesarias para la
configuración de la red en una máquina Linux. Incluye ifconfig,
route, netstat, rarp, y algunas otras herramientas menores.

%prep
%setup -q
%patch0 -p1 -b .jbj
%patch1 -p1 -b .proto
%patch2 -p1 -b .bufovr

cp %SOURCE1 ./config.h
cp -f ${RPM_SOURCE_DIR}/net-tools-pt_BR.po po/pt_BR.po

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{bin,sbin,usr/man/man{1,5,8}}

make BASEDIR=$RPM_BUILD_ROOT install

{ cd $RPM_BUILD_ROOT
  strip ./sbin/* ./bin/* || :
} 


rm -rf $RPM_BUILD_ROOT/usr/man/pt_BR/
mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/net-tools-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/arp
/sbin/ifconfig
/sbin/rarp
/sbin/route
/sbin/slattach
/sbin/plipconfig
/sbin/ipmaddr
/sbin/iptunnel
/bin/dnsdomainname
/bin/domainname
/bin/hostname
/bin/netstat
/bin/nisdomainname
/bin/ypdomainname
/usr/man/man[158]/*
/usr/man/fr_FR/man[18]/*
/usr/share/locale/*/LC_MESSAGES/net-tools.mo
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Thu Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- removed original pt_BR man pages

* Tue Jun 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed
- included pt_BR updated translation by Rodrigo Stulzer Lopes <rodrigo@conectiva.com>

* Thu Jun 17 1999 Jeff Johnson <jbj@redhat.com>
- plug potential buffer overruns.

* Sat Jun 12 1999 John Hardin <jhardin@wolfenet.com>
- patch to recognize ESP and GRE protocols for VPN masquerade

* Fri Apr 23 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.52.

* Thu Mar 25 1999 Jeff Johnson <jbj@redhat.com>
- update interface statistics continuously (#1323)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.51.
- strip binaries.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.50.
- added slattach/plipconfig/ipmaddr/iptunnel commands.
- enabled translated man pages.

* Tue Dec 15 1998 Jakub Jelinek <jj@ultra.linux.cz>
- update to 1.49.

* Sat Dec  5 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.48.

* Thu Nov 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.47.

* Wed Sep  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.46

* Thu Jul  9 1998 Jeff Johnson <jbj@redhat.com>
- build root
- include ethers.5

* Thu Jun 11 1998 Aron Griffis <agriffis@coat.com>
- upgraded to 1.45
- patched hostname.c to initialize buffer
- patched ax25.c to use kernel headers

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- added config patch

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- changed to net-tools 1.432
- removed old glibc 2.1 patch
 
* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added extra patches for glibc 2.1

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- included complete set of network protocols (some were removed for
  initial glibc work)

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- updated glibc patch for glibc 2.0.5

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- updated to 1.33
