Summary: A utility that manages print jobs.
Summary(pt_BR): Servidor e cliente para impressão local e remota.
Summary(es): Servidor y cliente para impresión local y remota.
Name: lpr
Version: 0.35
Release: 4cl
Copyright: distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: lpr-%{PACKAGE_VERSION}.tar.bz2
Source1: lpd.init
Source700: lpr-man-pt_BR.tar
Prereq: chkconfig
BuildRoot: /var/tmp/lpr-root

%description
The lpr package provides the basic system utility for managing printing
services.  Lpr manages print queues, sends print jobs to local and remote
printers and accepts print jobs from remote clients.

If you will be printing from your system, you'll need to install the lpr
package.

%description -l pt_BR
Este pacote gerencia os serviços de impressão. Gerencia filas de
impressão, envia jobs para impressoras locais e remotas e aceita
jobs de clientes remotos.

%description -l es
Este paquete administra los servicios de impresión. Administra
colas de impresión, envía jobs para impresoras locales y remotas
y acepta jobs de clientes remotos.


%prep
%setup -q

%build

%ifarch alpha
# we shouldn't need this with more recent glibc's, but lpq kills remote
# lpd w/o it
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Dgetline=get_line"
%else
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,sbin,man/man1,man/man5,man/man8}

%ifarch alpha
# we shouldn't need this with more recent glibc's, but lpq kills remote
# lpd w/o it and there seems to be a mistake in lpr's makefiles somewhere
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Dgetline=get_line" DESTDIR=$RPM_BUILD_ROOT install
%else
make DESTDIR=$RPM_BUILD_ROOT install
%endif

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m755 %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/lpd
( cd $RPM_BUILD_ROOT
mkdir -p ./etc/rc.d/{rc0.d,rc1.d,rc2.d,rc3.d,rc4.d,rc5.d,rc6.d}
  ln -sf ../init.d/lpd ./etc/rc.d/rc0.d/K60lpd
  ln -sf ../init.d/lpd ./etc/rc.d/rc1.d/K60lpd
  ln -sf ../init.d/lpd ./etc/rc.d/rc2.d/S60lpd
  ln -sf ../init.d/lpd ./etc/rc.d/rc3.d/S60lpd
  ln -sf ../init.d/lpd ./etc/rc.d/rc5.d/S60lpd
  ln -sf ../init.d/lpd ./etc/rc.d/rc6.d/K60lpd
  mkdir -p ./var/spool/lpd
)



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/lpr-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#/sbin/chkconfig --add lpd

%postun
if [ $1 = 0 ]; then
   /sbin/chkconfig --del lpd
fi

%files
%defattr(-,root,root)
%attr(6555,root,lp) /usr/bin/lpq
%attr(6555,root,lp) /usr/bin/lpr
%attr(6555,root,lp) /usr/bin/lprm
/usr/bin/lptest
/usr/man/man1/lpq.1
/usr/man/man1/lpr.1
/usr/man/man1/lprm.1
/usr/man/man1/lptest.1
/usr/man/man5/printcap.5
/usr/man/man8/lpc.8
/usr/man/man8/lpd.8
/usr/man/man8/pac.8
%attr(2755,root,lp) /usr/sbin/lpc
/usr/sbin/lpd
/usr/sbin/lpf
/usr/sbin/pac
%attr(0775,root,daemon)	%dir /var/spool/lpd
%config /etc/rc.d/init.d/lpd
%config(missingok) /etc/rc.d/rc0.d/K60lpd
%config(missingok) /etc/rc.d/rc1.d/K60lpd
%config(missingok) /etc/rc.d/rc2.d/S60lpd
%config(missingok) /etc/rc.d/rc3.d/S60lpd
%config(missingok) /etc/rc.d/rc5.d/S60lpd
%config(missingok) /etc/rc.d/rc6.d/K60lpd
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- i18n initscripts (lpd)

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start
- recompressed source

* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Bill Nottingham <notting@redhat.com>
- increase buffer length for filenames (bug #1676)

* Fri Mar 19 1999 Bill Nottingham <notting@redhat.com>
- change man page to show that -r -s is not supported (bug #717)

* Mon Feb 15 1999 Bill Nottingham <notting@redhat.com>
- security patch from Chris Evans
- fix for remote but not local users (originally from Kevin Sochacki)

* Mon Feb  8 1999 Bill Nottingham <notting@redhat.com>
- build for 6.0 tree

* Thu Oct  1 1998 Bill Nottingham <notting@redhat.com>
- don't ignore SIGCHLD in filters

* Mon Aug  3 1998 Jeff Johnson <jbj@redhat.com>
- build root.

* Fri Jun 26 1998 Jeff Johnson <jbj@redhat.com>
- bring printjob up-to-date (fix problem #564)

* Thu Apr 23 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscript

* Thu Apr 23 1998 Erik Troan <ewt@redhat.com>
- included new rmjob security fix from BSD

* Sat Apr 18 1998 Erik Troan <ewt@redhat.com>
- included rmjob patches from BSD

* Fri Feb 27 1998 Otto Hammersmith <otto@redhat.com>
- increased buffer for hostname from 32 to 1024, plenty big enough now.

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added chkconfig support
- changed the initscript name from lpd.init to lpd (all links, too)

* Mon Oct 27 1997 Michael Fulbright <msf@redhat.com>
- Fixed print filters to change to printer's UID so root-squashing wont bite us

* Wed Oct  8 1997 Michael Fulbright <msf@redhat.com>
- Fixed nasty error in getprent() and forked lpd's in startup() which
  caused the printcap file to be read incorrectly.
- added #include <string.h> as needed to make compile cleaner.  

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- changes for glibc 2.0.4

* Tue Apr 22 1997 Michael Fulbright <msf@redhat.com>
- moved to v. 0.17, then 0.18 (!)
- Fixed bug on Alpha/glibc when printing to a remote queue via a filter

* Fri Mar 28 1997 Michael Fulbright <msf@redhat.com>
- Moved version up to 0.16
- Added input filter support for remote queues

* Wed Mar 05 1997 Erik Troan <ewt@redhat.com>
- Incorporated filter patch into main sources
- Removed RCS logs from source tar file
- Added patched from David Mosberger to fix __ivaliduser on Alpha's
- added -Dgetline=get_line for old glibcs (this means alpha)
