Summary: NetWare file and print servers which run on Linux systems.
Summary(pt_BR): Servidor de arquivos e impressão NetWare que roda no Linux
Summary(es): Servidor de archivos e impresión NetWare que se ejecuta en Linux
Name: mars-nwe
Version: 0.99pl15
Release: 6cl
Copyright: GPL
Source:  ftp://ftp.gwdg.de/pub/linux/misc/ncpfs/mars_nwe-0.99.pl13.tar.bz2
Source1: mars_nwe-mk.li
Source2: mars_nwe-config.h
Source3: mars_nwe-nwserv.conf
Source4: mars_nwe-readme.txt
Source5: mars_nwe.init
Source6: mars_nwe.log
Patch: mars_nwe-0.99.pl14.gz
Patch1: mars_nwe-glibc21.patch
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Prereq: chkconfig
BuildRoot: /var/tmp/marsnwe-root

%description
The mars_nwe (MARtin Stover's NetWare Emulator) package enables Linux to
provide both file and print services for NetWare clients (i.e., providing
the services of a Novell NetWare file server).  Mars_nwe allows the
sharing of files between Linux machines and Novell NetWare clients, using
NetWare's native IPX protocol suite.

Install the mars_nwe package if you need a Novell NetWare file server
on your Red Hat Linux system.

%description -l pt_BR
MARS é um servidor de arquivo e impressão compatível com NetWare. Ele
deixa você usar uma máquina Linux como um servidor de arquivo
e impressão para clientes de NetWare usando o protocolo nativo
IPX NetWare.

%description -l es
MARS es un servidor de archivo y impresión compatible con
NetWare. Deja que uses una máquina Linux como un servidor de archivo
y impresión para clientes de NetWare usando el protocolo nativo
IPX NetWare.

%prep
%setup -n mars_nwe
%patch -p1 -b .pl14
%patch1 -p1 -b .glibc21
cp -f $RPM_SOURCE_DIR/mars_nwe-config.h ./config.h
cp -f $RPM_SOURCE_DIR/mars_nwe-mk.li ./mk.li

%build
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
for I in sys/login sys/public sys/system bindery; do \
	mkdir -p --mode=0755 $RPM_BUILD_ROOT/var/mars_nwe/$I
done

mkdir -p $RPM_BUILD_ROOT/var/log $RPM_BUILD_ROOT/var/run
install -m644 $RPM_SOURCE_DIR/mars_nwe-readme.txt $RPM_BUILD_ROOT/var/mars_nwe/sys/readme.txt
:> $RPM_BUILD_ROOT/var/log/mars_nwe.log
chmod 0644 $RPM_BUILD_ROOT/var/log/mars_nwe.log
:> $RPM_BUILD_ROOT/var/run/mars_nwe.routes
chmod 0644 $RPM_BUILD_ROOT/var/run/mars_nwe.routes

mkdir -p $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/usr/sbin
install -m644 examples/nwserv.stations $RPM_BUILD_ROOT/etc/nwserv.stations
for I in nwserv nwconn ncpserv nwclient nwbind; do
	install -s -m 755 $I $RPM_BUILD_ROOT/usr/sbin/$I
done
install -m600 $RPM_SOURCE_DIR/mars_nwe-nwserv.conf $RPM_BUILD_ROOT/etc/nwserv.conf

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d $RPM_BUILD_ROOT/etc/logrotate.d
install -m755 $RPM_SOURCE_DIR/mars_nwe.init $RPM_BUILD_ROOT/etc/rc.d/init.d/mars-nwe
install -m644 $RPM_SOURCE_DIR/mars_nwe.log $RPM_BUILD_ROOT/etc/logrotate.d/mars-nwe.log

#%post
#/sbin/chkconfig --add mars-nwe

%postun
if [ $0 = 0 ]; then
    /sbin/chkconfig --del mars-nwe
fi

%files
%dir /var/mars_nwe
/var/mars_nwe/sys
%dir /var/mars_nwe/bindery
%ghost /var/log/mars_nwe.log
%ghost /var/run/mars_nwe.routes
%config /etc/nwserv.conf
%config /etc/nwserv.stations
%config /etc/logrotate.d/mars-nwe.log
%doc README COPYING doc examples
/usr/sbin/nwserv
/usr/sbin/nwconn
/usr/sbin/ncpserv
/usr/sbin/nwclient
/usr/sbin/nwbind
%config /etc/rc.d/init.d/mars-nwe

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- i18n initscripts (mars-nwe)

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start
- sources recompressed

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate fixes

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Mar  9 1999 Bill Nottingham <notting@redhat.com>
- update to 0.99.pl15

* Tue Feb 23 1999 Bill Nottingham <notting@redhat.com>
- update to 0.99.pl14

* Tue Aug 18 1998 Cristian Gafton <gafton@redhat.com>
- buildroot

* Sun May 10 1998 Alan Cox <alan@redhat.com>
- Made it compile with 2.1.* kernels and also gcc 2.0.7 where sysv_signal
  is correctly hidden as __sysv_signal.

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 0.99pl6
- enhanced initscripts

* Tue Jan 13 1998 Erik Troan <ewt@redhat.com>
- use sysv_signal everywhere instead of normal signal -- this makes signal
  handlers not block signals, which mars_nwe expects
- changed _ to - in name of logrotate config file

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated for chkconfig
- doesn't start by default
- added status, restart options to init script

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
