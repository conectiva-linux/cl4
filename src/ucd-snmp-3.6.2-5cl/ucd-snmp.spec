Summary: A collection of SNMP protocol tools from UC-Davis.
Summary(pt_BR): Agente SNMP da UCD
Summary(es): Agente SNMP de la UCD
Name: ucd-snmp
Version: 3.6.2
Release: 5cl
Copyright: BSDish
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://ucd-snmp.ucdavis.edu/ucd-snmp-%{version}.tar.bz2
Source1: ucd-snmpd.init
Source2: snmpd.conf.redhat
Patch0: ucd-snmp-3.6.1-confdir.patch
Patch3: ucd-snmp-3.5-ipfwacc.patch
Patch6: ucd-snmp-3.5.3-glibc21.patch

BuildRoot: /var/tmp/ucd-snmp-root
Prereq: chkconfig
Obsoletes: cmu-snmp

%description
SNMP (Simple Network Management Protocol) is a protocol used for network
management (hence the name).  The UCD-SNMP project includes various SNMP
tools:  an extensible agent, an SNMP library, tools for requesting or
setting information from SNMP agents, tools for generating and handling
SNMP traps, a version of the netstat command which uses SNMP, and a
Tk/Perl mib browser.  This package contains the snmpd and snmptrapd
daemons, documentation, etc.

Install the ucd-snmp package if you need network management tools.
You will probably also want to install the ucd-snmp-utils package, which
contains UCD-SNMP utilities.

%description -l pt_BR
Este pacote é derivado da implementação do Protocolo Simples de
Gerenciamento de Redes versão 2 (SNMPv2) da Universidade Carnegie Mellon.
Útil para gerenciar redes e fazer contabilidade.

%description -l es
Este paquete se deriva de la implementación del Protocolo Simple
de Gestión de Redes versión 2 (SNMPv2) de la Universidad Carnegie
Mellon.  Útil para administrar redes y hacer contabilidad.

%package utils
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Summary: Network management utilities using SNMP, from the UCD-SNMP project.
Summary(pt_BR): Utilitários do SNMP da UCD
Summary(es): Utilitarios del SNMP de la UCD
Requires: ucd-snmp
Obsoletes: cmu-snmp-utils

%description utils
The ucd-snmp package contains various utilities for use with the
UCD-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol.  You'll also need to install the ucd-snmp
package.

%description -l pt_BR utils
Vários utilitários para uso com o SNMP da UCD. Contém utilitários como:
snmpwalk, snmptest e outros.

%description -l es utils
Varios utilitarios para uso con el SNMP de la UCD. Contiene
utilitarios como: snmpwalk, snmptest y otros.

%package devel
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Summary: The development environment for the UCD-SNMP project.
Summary(pt_BR): Arquivos de inclusão e bibliotecas para desenvolvimento no SNMP da UCD.
Summary(es): Archivos de inclusión y bibliotecas para desarrollo en el SNMP de la UCD.
Requires: ucd-snmp
Obsoletes: cmu-snmp-devel

%description devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the UCD-SNMP project's network management
tools.

Install the ucd-snmp-devel package if you would like to develop
applications for use with the UCD-SNMP project's network management
tools. You'll also need to have the ucd-snmp and ucd-snmp-utils packages
installed.

%description -l pt_BR devel
Estas são as bibliotecas e arquivos de inclusão para desenvolvimento
com o SNMP da UCD.
Com este pacote é possível a criação de programas para uso no
gerenciamento de redes.

%description -l es devel
Estas son las bibliotecas y archivos de inclusión para desarrollo
con el SNMP de la UCD.  Con este paquete es posible la creación de
programas para uso en la gestión de redes.

%prep
%setup -q
%patch0 -p1 -b .confdir
#%patch3 -p1 -b .ipfwacc
%patch6 -p1 -b .glibc21

find . -type f | xargs perl -pi -e "s|/usr/local/bin/perl5|/usr/bin/perl|g"
find . -type f | xargs perl -pi -e "s|/usr/local/bin/perl|/usr/bin/perl|g"

%build
autoconf

# First build the static library
%configure				\
	--with-cc=egcs --with-cflags="$RPM_OPT_FLAGS"\
	--with-ldflags="-s" 	 			\
	--with-sys-location="Unknown"			\
	--with-logfile="/var/log/snmpd.log"		\
	--with-mib-modules="host"			\
	--with-libwrap=-lwrap				\
	--prefix=/usr					\
	--sysconfdir=/etc				\
	--disable-debugging				\
	--with-sys-contact="root@localhost"		\
	--with-logfile="/var/log"			\

make -C snmplib libsnmp.a
mv snmplib/libsnmp.a .
make -C snmplib clean

# Now configure everything to build with a shared library
%configure --enable-shared		\
	--with-cc=egcs --with-cflags="$RPM_OPT_FLAGS"\
	--with-ldflags="-s" 	 			\
	--with-sys-location="Unknown"			\
	--with-logfile="/var/log/snmpd.log"		\
	--with-mib-modules="host"			\
	--with-libwrap=-lwrap				\
	--prefix=/usr					\
	--sysconfdir=/etc				\
	--disable-debugging				\
	--with-sys-contact="root@localhost"		\
	--with-logfile="/var/log"			\

# XXX Grrr -- build shared library with soname versioning
make -C snmplib				\
	SHLIB_EXTENSION=so.0.%{version}	\
	SHLIB_CFLAGS="-fpic"		\
	SHLIB_LD_CMD="gcc -shared -Wl,-soname -Wl,libsnmp.so.0 -o"	\
	RANLIB=/bin/echo		\
	libsnmp.so.0.%{version}
ln -sf libsnmp.so.0.%{version} snmplib/libsnmp.so.0
ln -sf libsnmp.so.0 snmplib/libsnmp.so

# XXX Finally ...
make LDFLAGS="-Wl,-rpath -Wl,/usr/lib" all

# Remove backup file
rm -f local/snmp~

%install
rm -rf $RPM_BUILD_ROOT

make	prefix=$RPM_BUILD_ROOT/usr	\
	exec_prefix=$RPM_BUILD_ROOT/usr \
	install 

# XXX Install hand-crafted libraries
install -m 0644 libsnmp.a $RPM_BUILD_ROOT/usr/lib
install -m 0755 snmplib/libsnmp.so.0.%{version} $RPM_BUILD_ROOT/usr/lib

# XXX just in case
{ pushd $RPM_BUILD_ROOT/usr/lib
  rm -f libsnmp.so.0
  ln -s libsnmp.so.0.%{version} libsnmp.so.0
  rm -f libsnmp.so
  ln -s libsnmp.so.0 libsnmp.so
  popd
}

install -d $RPM_BUILD_ROOT/etc/snmp
install -m 644 %SOURCE2 $RPM_BUILD_ROOT/etc/snmp/snmpd.conf
install -m 644 /dev/null $RPM_BUILD_ROOT/etc/snmp/snmpd.local.conf
for f in README acl.conf context.conf party.conf view.conf
do
	install -m 644 etc/$f $RPM_BUILD_ROOT/etc/snmp
done

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 %SOURCE1 $RPM_BUILD_ROOT/etc/rc.d/init.d/snmpd

# Strip binaries
strip $RPM_BUILD_ROOT/usr/bin/* || :

%post
/sbin/ldconfig

#/sbin/chkconfig --add snmpd 
#if [ ! -f /etc/snmpd.agentinfo ]; then
#  touch /etc/snmpd.agentinfo
#fi

%postun
/sbin/ldconfig
if [ $1 = 0 ]; then
   /sbin/chkconfig --del snmpd
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc	ChangeLog EXAMPLE.conf FAQ NEWS PORTING README TODO bug-report local

%dir	/etc/snmp
%config /etc/snmp/snmpd.conf
%config(missingok) /etc/snmp/snmpd.local.conf
%config	/etc/snmp/acl.conf
%config	/etc/snmp/context.conf
%config	/etc/snmp/party.conf
%config	/etc/snmp/view.conf

%config /etc/rc.d/init.d/snmpd

%dir	/usr/share/snmp
%dir	/usr/share/snmp/mibs
%attr(0644,root,root)	/usr/share/snmp/mibs/*

/usr/lib/libsnmp.so.0.%{version}
/usr/sbin/snmpd
/usr/sbin/snmptrapd
%attr(0644,-,-)	/usr/man/man1/snmpd.1
%attr(0644,-,-)	/usr/man/man5/snmpd.conf.5
%attr(0644,-,-)	/usr/man/man5/variables.5
%attr(0644,-,-)	/usr/man/man8/snmptrapd.8

%files utils
%defattr(-,root,root,-)
/usr/bin/snmpbulkwalk
/usr/bin/snmpdelta
/usr/bin/snmpget
/usr/bin/snmpgetnext
/usr/bin/snmpnetstat
/usr/bin/snmpset
/usr/bin/snmpstatus
/usr/bin/snmptable
/usr/bin/snmptest
/usr/bin/snmptranslate
/usr/bin/snmptrap
/usr/bin/snmpwalk
/usr/bin/tkmib

%attr(0644,-,-)	/usr/man/man1/snmpbulkwalk.1
%attr(0644,-,-)	/usr/man/man1/snmpcmd.1
%attr(0644,-,-)	/usr/man/man1/snmpdelta.1
%attr(0644,-,-)	/usr/man/man1/snmpget.1
%attr(0644,-,-)	/usr/man/man1/snmpgetnext.1
%attr(0644,-,-)	/usr/man/man1/snmpnetstat.1
%attr(0644,-,-)	/usr/man/man1/snmpset.1
%attr(0644,-,-)	/usr/man/man1/snmpstatus.1
%attr(0644,-,-)	/usr/man/man1/snmptable.1
%attr(0644,-,-)	/usr/man/man1/snmptest.1
%attr(0644,-,-)	/usr/man/man1/snmptranslate.1
%attr(0644,-,-)	/usr/man/man1/snmptrap.1
%attr(0644,-,-)	/usr/man/man1/snmpwalk.1

%files devel
%defattr(0644,root,root,0755)
/usr/lib/libsnmp.so
/usr/lib/libsnmp.a
/usr/include/ucd-snmp
%attr(0644,-,-)	/usr/man/man3/mib_api.3
%attr(0644,-,-)	/usr/man/man3/snmp_api.3

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- i18n initscripts (snmpd)

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Sat Jun 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 3.6.1 to 3.6.2

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed Prereq:

* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- i18n initscripts

* Thu Apr  8 1999 Wes Hardaker <wjhardaker@ucdavis.edu>
- fix Source0 location.
- fix the snmpd.conf file to use real community names.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 3.6.1, fix configuration file stuff.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- restore host resources mib
- simplified config file
- rebuild for 6.0.

* Tue Dec 22 1998 Bill Nottingham <notting@redhat.com>
- remove backup file to fix perl dependencies

* Tue Dec  8 1998 Jeff Johnson <jbj@redhat.com>
- add all relevant rpm scalars to host resources mib.

* Sun Dec  6 1998 Jeff Johnson <jbj@redhat.com>
- enable libwrap (#253)
- enable host module (rpm queries over SNMP!).

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Fri Oct  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.5.3.
- don't include snmpcheck until perl-SNMP is packaged.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- ucd-snmpd.init: start daemon w/o -f.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- don't start snmpd unless requested
- start snmpd after pcmcia.

* Sun Jun 21 1998 Jeff Johnson <jbj@redhat.com>
- all but config (especially SNMPv2p) ready for prime time

* Sat Jun 20 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.5.

* Tue Dec 30 1997 Otto Hammersmith <otto@redhat.com>
- created the package... possibly replace cmu-snmp with this.
