Summary: An Internet name server.
Summary(pt_BR): BIND - Servidor de nomes DNS
Summary(es): BIND - Servidor de nombres DNS
Name: bind
Version: 8.2
Release: 10cl
Copyright: distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://ftp.isc.org/isc/bind/src/%{version}/bind-%{version}-src.tar.bz2
Source1: ftp://ftp.isc.org/isc/bind/src/%{version}/bind-%{version}-doc.tar.bz2
Source2: ftp://ftp.isc.org/isc/bind/src/%{version}/bind-%{version}-contrib.tar.bz2
Source3: named.init
Source18: named.init.i18n
Url: http://www.isc.org/bind.html
Patch0: bind-8.1.2-rh.patch
Patch1: bind-8.1.2-nonlist.patch
Patch2: bind-8.1.2-fds.patch
Patch3: bind-8.2-glibc21.patch
Patch4: bind-8.2-host.patch
Patch5: bind-8.2-nslookup.patch
Patch99: patch1
Buildroot: /var/tmp/%{name}-root
Prereq: chkconfig

%description
Bind includes the named name server, which resolves host names to IP
addresses (and vice versa), and a resolver library (a set of routines
in a system library that provide the interface for programs to use when
accessing domain name services).  A name server is a network service which
enables clients to name resources or objects and share this information
with other network machines.  The named name server can be used on
workstations as a caching name server, but is generally only needed on
one machine for an entire network.  Note that the configuration files for
making bind act as a simple caching nameserver are included in the
caching-nameserver package.  

Install the bind package if you need a name server for your network.  If
you want bind to act a caching name server, you will also need to install
the caching-nameserver package.

%description -l pt_BR
Inclui o servidor de nomes (DNS), que é usado para traduzir nomes
para IP (e vice-versa). Pode ser usado em estações de trabalho como
um servidor de nomes cache, mas geralmente só é necessário em uma
máquina para toda a rede.

%description -l es
Incluye el servidor de nombres (DNS), que se usa para traducir
nombres para IP (y viceversa). Puede ser usado en estaciones de
trabajo como un servidor de nombres caché, pero generalmente sólo
hace falta en una máquina para toda la red.

%package utils
Summary: DNS utilities:  host, dig, dnsquery, and nslookup.
Summary(pt_BR): Utilitários DNS - host, dig, dnsquery e nslookup
Summary(es): Utilitarios DNS - host, dig, dnsquery y nslookup
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema

%description utils
Bind-utils contains a collection of utilities for querying DNS (Domain
Name Service) name servers to find out information about Internet hosts.
These tools will provide you with the IP addresses for given host names,
as well as other information about registered domains and network 
addresses.

You should install bind-utils if you need to get information from DNS name
servers.

%description -l pt_BR utils
Conjunto de utilitários para consulta a servidores de nomes.
Estas ferramentas permitem a determinação de endereços IP para
nomes de máquinas informados e busca informações sobre domínios
registrados e endereços de rede.

%description -l es utils
Conjunto de utilitarios para consulta a servidores de nombres.
Estas herramientas permiten la determinación de direcciones IP para
nombres de máquinas informados y busca información sobre dominios
registrados y direcciones de red.

%package devel
Summary: Include files and libraries needed for bind DNS development.
Summary(pt_BR): Arquivos de inclusão e bibliotecas para desenvolvimento DNS
Summary(es): Archivos de inclusión y bibliotecas para desarrollo DNS
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
The bind-devel package contains all the include files and the 
library required for DNS (Domain Name Service) development
for bind versions 8.x.x.

You should install bind-devel if you want to develop bind DNS
applications. If you install bind-devel, you'll need to install
bind, as well.

%description -l pt_BR devel
Todos os arquivos de inclusão e bibliotecas necessários para o
desenvolvimento com o bind 8.x.x.

%description -l es devel
Todos los archivos de inclusión y bibliotecas necesarios al
desarrollo DNS para el bind 8.x.x

%prep
%setup -q -c -a 1 -a 2
%patch0 -p0 -b .rh
%patch1 -p0 -b .nonlist
%patch2 -p1 -b .fds
%patch3 -p1 -b .glibc21
%patch4 -p1 -b .host
%patch5 -p1 -b .view
%patch99 -p0 -b .patch1
rm -f compat/include/sys/cdefs.h

%build
make -C src
make clean all -C src SUBDIRS=../doc/man

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/usr/{bin,lib,sbin}
mkdir -p ${RPM_BUILD_ROOT}/usr/man/{man1,man3,man5,man7,man8}
mkdir -p ${RPM_BUILD_ROOT}/etc/rc.d/{init,rc0,rc1,rc2,rc3,rc4,rc5,rc6}.d

make DESTDIR=$RPM_BUILD_ROOT install -C src
make DESTDIR=$RPM_BUILD_ROOT INSTALL=install install -C src SUBDIRS=../doc/man

install -m 755 $RPM_SOURCE_DIR/named.init.i18n ${RPM_BUILD_ROOT}/etc/rc.d/init.d/named

#strip things
strip $RPM_BUILD_ROOT/usr/bin/* || :
strip $RPM_BUILD_ROOT/usr/sbin/* || :

%post
#/sbin/chkconfig --add named
if [ -f /etc/named.boot -a ! -f /etc/named.conf ]; then
  if [ -x /usr/doc/bind-%{version}/named-bootconf.pl ]; then
    cat /etc/named.boot | /usr/doc/bind-%{version}/named-bootconf.pl > /etc/named.conf
    chmod 644 /etc/named.conf
  fi
fi

%preun
if [ $1 = 0 ]; then
   /sbin/chkconfig --del named
fi

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc src/README src/INSTALL src/Version src/CHANGES 
%doc src/TODO src/bin/named-bootconf
%doc doc/bog doc/html doc/misc doc/notes doc/port doc/rfc doc/tmac

%config /etc/rc.d/init.d/named

/usr/sbin/dnskeygen
/usr/sbin/irpd
/usr/sbin/named
/usr/sbin/named-bootconf
/usr/sbin/named-xfer
/usr/sbin/ndc

/usr/man/man5/named.conf.5
/usr/man/man7/hostname.7
/usr/man/man8/named.8
/usr/man/man8/ndc.8
/usr/man/man8/named-bootconf.8
/usr/man/man8/named-xfer.8
     
%files utils
%defattr(-,root,root)
/usr/bin/addr
/usr/bin/dig
/usr/bin/dnsquery
/usr/bin/host
/usr/bin/mkservdb
/usr/bin/nslookup
/usr/bin/nsupdate
/usr/lib/nslookup.help
/usr/man/man1/dig.1
/usr/man/man1/dnsquery.1
/usr/man/man1/host.1
/usr/man/man5/irs.conf.5
/usr/man/man5/resolver.5
/usr/man/man8/nslookup.8
/usr/man/man8/nsupdate.8

%files devel
%defattr(-,root,root)
/usr/lib/bind

%changelog
* Mon Jun 21 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- named.i18n without msg "done"
- recompressed sources
- chkconfig --add removed, so that the user has to enable the service start
- fixed Prereqs:
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun May 30 1999 Jeff Johnson <jbj@redhat.com>
- nslookup fixes (#2463).
- missing files (#3152).

* Sat May  1 1999 Stepan Kasal <kasal@math.cas.cz>
- nslookup patched:
  to count numRecords properly
  to fix subsequent calls to ls -d
  to parse "view" and "finger" commands properly
  the view hack updated for bind-8 (using sed)

* Wed Mar 31 1999 Bill Nottingham <notting@redhat.com>
- add ISC patch
- add quick hack to make host not crash
- add more docs

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add probing information in the init file to keep linuxconf happy
- dont strip libbind

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- removed 'done' output at named shutdown.

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- version 8.2

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to use the __FDS_BITS macro
- build for glibc 2.1

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- change named.restart to /usr/sbin/ndc restart

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- install man pages correctly.
- change K10named to K45named.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- don't start if /etc/named.conf doesn't exist.

* Sat Aug  8 1998 Jeff Johnson <jbj@redhat.com>
- autmagically create /etc/named.conf from /etc/named.boot in %post
- remove echo in %post

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- merge in 5.1 mods

* Sun Apr 12 1998 Manuel J. Galan <manolow@step.es>
- Several essential modifications to build and install correctly.
- Modified 'ndc' to avoid deprecated use of '-'

* Mon Dec 22 1997 Scott Lampert <fortunato@heavymetal.org>
- Used buildroot
- patched bin/named/ns_udp.c to use <libelf/nlist.h> for include
  on Redhat 5.0 instead of <nlist.h>

