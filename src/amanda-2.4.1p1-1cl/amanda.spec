Name: amanda
Version: 2.4.1p1
Release: 1cl
Copyright: distributable
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
URL: http://www.amanda.org
Summary: A network-capable tape backup solution
Summary(pt_BR): Ferramenta de backup para redes
Summary(es): Una herramienta de backup para red
#Source: ftp://ftp.amanda.org/pub/amanda/amanda-2.4.1p1.tar.gz
Source: amanda-2.4.1p1.tar.bz2
Patch: amanda-2.4.1p1-glibc21.patch
BuildRoot: /var/tmp/amanda-root

%description 
A network-capable tape backup solution.

%description -l pt_BR
Uma ferramenta de backup para rede

%description -l es
Una herramienta de backup para red

%package client
Summary: The client side of Amanda
Summary(pt_BR): A parte cliente do Amanda
Summary(es): El cliente del Amanda
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema

%description client
This package should be installed on machines that are to be backed
up by Amanda.  (Including, the server if it should be backed up.)

%description -l pt_BR client
Este pacote deve ser instalado em máquinas que devem ser arquivadas
pelo Amanda. (Incluindo o servidor em que serão feitos os backups.)

%description -l es client
Una herramienta de backup para red.

%package server
Summary: The server side of Amanda
Summary(pt_BR): A parte servidor do Amanda
Summary(es): El servidor del Amanda
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Requires: gnuplot

%description server
This package should be installed on the machine that has the device
(such as a tape drive) where backups will be written.

%description -l pt_BR server
Este pacote deve ser instalado na máquina que tem o dispositivo
(Um drive de fita, por exemplo) onde os backups serão criados.

%description -l es server
El servidor del Amanda.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--sysconfdir=/etc \
	--libexecdir=\${exec_prefix}/lib/amanda \
	--with-index-server=localhost \
	--with-amandahosts --with-user=operator --with-group=disk
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_OPT_FLAGS/etc 
chmod 755 $RPM_BUILD_ROOT/usr/lib/lib*.so.*

%clean 
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%post client -p /sbin/ldconfig

%post server -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%postun client -p /sbin/ldconfig

%postun server -p /sbin/ldconfig

%files
/usr/lib/libamanda*
/usr/lib/libamtape*
/usr/lib/amanda/amidxtaped
/usr/sbin/amrestore
/usr/man/man8/amrestore.8

%files server
/usr/lib/libamserver*
/usr/lib/amanda/amindexd
/usr/lib/amanda/amtrmidx
/usr/lib/amanda/driver
/usr/lib/amanda/dumper
/usr/lib/amanda/getconf
/usr/lib/amanda/planner
#/usr/lib/amanda/reporter
/usr/lib/amanda/taper
/usr/lib/amanda/chg-chio
/usr/lib/amanda/chg-manual
/usr/lib/amanda/chg-multi
/usr/lib/amanda/chg-mtx
/usr/lib/amanda/chg-rth
/usr/lib/amanda/chg-chs
/usr/lib/amanda/amcat.awk
/usr/lib/amanda/amplot.awk
/usr/lib/amanda/amplot.g
/usr/lib/amanda/amplot.gp
/usr/sbin/amadmin
/usr/sbin/amcheck
/usr/sbin/amflush
/usr/sbin/amlabel
/usr/sbin/amtape
/usr/sbin/amcheckdb
/usr/sbin/amcleanup
/usr/sbin/amdump
/usr/sbin/amoverview
/usr/sbin/amrmtape
/usr/sbin/amtoc
/usr/sbin/amverify
/usr/sbin/amplot
/usr/sbin/amreport
/usr/sbin/amstatus
/usr/man/man8/amadmin.8
/usr/man/man8/amrmtape.8
/usr/man/man8/amtape.8
/usr/man/man8/amtoc.8
/usr/man/man8/amanda.8
/usr/man/man8/amcheck.8
/usr/man/man8/amcleanup.8
/usr/man/man8/amdump.8
/usr/man/man8/amflush.8
/usr/man/man8/amlabel.8
/usr/man/man8/amplot.8
/usr/man/man8/amreport.8
/usr/man/man8/amstatus.8

%files client
/usr/lib/libamclient*
/usr/lib/amanda/versionsuffix
/usr/lib/amanda/amandad
/usr/lib/amanda/calcsize
/usr/lib/amanda/rundump
/usr/lib/amanda/runtar
/usr/lib/amanda/selfcheck
/usr/lib/amanda/sendbackup
/usr/lib/amanda/sendsize
/usr/lib/amanda/patch-system
/usr/lib/amanda/killpgrp
/usr/sbin/amrecover
/usr/man/man8/amrecover.8

%changelog
* Thu Jul  1 1999 Domingos Parra Novo <domingos@conectiva.com>
- version 2.4.1p1
- added patch to fix bug with glibc 2.1.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 16 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition
- Added spanish and portuguese translations to spec file

* Fri Apr 16 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added to Conectiva Linux Server edition

* Tue Oct 27 1998 Cristian Gafton <gafton@redhat.com>
- version 2.4.1

* Tue May 19 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to full 2.4.0 release

* Thu Feb 19 1998 Otto Hammersmith <otto@redhat.com>
- fixed group for -client and -server packages (Network->Networking)

* Wed Feb 11 1998 Otto Hammersmith <otto@redhat.com>
- updated to 2.4.0b6, fixes security hole among other things
  (as well as finally got the glibc patch in the main source.)
 
* Tue Jan 27 1998 Otto Hammersmith <otto@redhat.com>
- moved versionsuffix to client package to remove dependency of amanda on amanda-client

* Mon Jan 26 1998 Otto Hammersmith <otto@redhat.com>
- fixed libexec garbage.

* Wed Jan 21 1998 Otto Hammersmith <otto@redhat.com>
- split into three packages amanda, amanda-client, and amanda-server

* Fri Jan  9 1998 Otto Hammersmith <otto@redhat.com>
- updated to latest beta... builds much cleaner now.

* Thu Jan  8 1998 Otto Hammersmith <otto@redhat.com>
- created the package
