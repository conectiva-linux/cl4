Summary: An FTP daemon provided by Washington University.
Summary(pt_BR): Deamon FTP da Universidade de Washington
Summary(es): Deamon FTP de la Universidad de Washington
Name: wu-ftpd
Version: 2.5.0
Release: 6cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://ftp.vr.net/pub/wu-ftpd/wu-ftpd-%{version}.tar.bz2
Source1: ftpd.log
Source2: ftp.pamd
Patch0: wu-ftpd-2.4.2-vr17-redhat.patch
Patch1: wu-ftpd-2.5.0-glob.patch
# pathname patch already part of 2.5.0
Patch2: wu-ftpd-2.5.0-ftpwho.patch
Requires: pam >= 0.59
Provides: ftpserver
Prereq: fileutils
Buildroot: /var/tmp/%{name}-root

%description
The wu-ftpd package contains the wu-ftpd FTP (File Transfer Protocol)
server daemon.  The FTP protocol is a method of transferring files
between machines on a network and/or over the Internet.  Wu-ftpd's
features include logging of transfers, logging of commands, on the fly
compression and archiving, classification of users' type and location,
per class limits, per directory upload permissions, restricted guest
accounts, system wide and per directory messages, directory alias,
cdpath, filename filter and virtual host support.

Install the wu-ftpd package if you need to provide FTP service to remote
users.

%description -l pt_BR
wu-ftpd é o daemon que serve arquivos FTP para clientes ftp. Ele
é útil se você deseja transferir programas entre computadores sem
rodar um sistema de arquivos de rede como NFS; ou se você deseja
ter um site de FTP anônimo (neste caso, você necessita instalar o
pacote anonftp).

%description -l es
wu-ftpd es el daemon que ccc archivos FTP para clientes ftp. Es
útil si deseas transferir programas entre ordenadores sin ejecutar
un sistema de archivos de red como NFS; o si deseas tener un sitio
de FTP anónimo (en este caso, necesitas instalar el paquete anonftp).

%prep
%setup -q
mkdir rhsconfig
%patch0 -p1
#%patch1 -p1 -b .glob
%patch2 -p1 -b .ftpwho

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS" ./build lnx USE_PAM=1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
make install DESTDIR=$RPM_BUILD_ROOT
install -m755 util/xferstats $RPM_BUILD_ROOT/usr/sbin
cd rhsconfig
install -m 600 ftpaccess ftpusers  ftphosts ftpgroups ftpconversions $RPM_BUILD_ROOT/etc
strip $RPM_BUILD_ROOT/usr/sbin/* || :
mkdir -p $RPM_BUILD_ROOT/etc/{pam,logrotate}.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/logrotate.d/ftpd
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/ftp
ln -sf in.ftpd $RPM_BUILD_ROOT/usr/sbin/wu.ftpd
ln -sf in.ftpd $RPM_BUILD_ROOT/usr/sbin/in.wuftpd

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /var/log/xferlog ]; then
    touch /var/log/xferlog
    chmod 600 /var/log/xferlog
fi

%files
%defattr(-,root,root)
%doc README ANNOUNCE-RELEASE ERRATA VIRTUAL.FTP.SUPPORT
%doc doc/FIXES doc/examples
/usr/sbin/*
/usr/bin/*
/usr/man/*/*
%config /etc/ftp*
%config /etc/pam.d/ftp
%config /etc/logrotate.d/ftpd

%changelog
* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun  7 1999 <jbj@redhat.com>
- update to 2.5.0 (pathname patch no longer needed).
- use "/bin/ps -f -p #" to get correct ftpwho info (#2455).
- revert glob patch in order to fix "cd ~user" (#2798) and "ls foo*" (#2944).

* Mon Apr 19 1999 <ewt@redhat.com>
- fixed pathname overflow patch

* Sat Apr 17 1999 <ewt@redhat.com>
- use libc glob function
- patched up some overflows - ick.

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- version 2.4.2-vr17. Thank GOD! - important patches are already in. Joy an
  happyness will reign the world now.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Mon Feb 15 1999 Cristian Gafton <gafton@redhat.com>
- update to 2.4.2-beta18-vr14 from ftp.vr.net

* Mon Aug  3 1998 Jeff Johnson <jbj@redhat.com>
- fix busted symlinks.

* Thu Jul 16 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.4.2-beta18

* Tue Jun 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Tue Jun  9 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.4.2-beta17 (fix problems #679/#680)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun May 03 1998 Cristian Gafton <gafton@redhat.com>
- fixed the ps patch for the new ps convention (use ps www instead of ps -www)

* Sun Apr 12 1998 Cristian Gafton <gafton@redhat.com>
- added %clean section

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.4.2b16
- BuildRoot

* Fri Dec 12 1997 Cristian Gafton <gafton@redhat.com>
- added a patch to prevent a possible PORT command exploit
- cleaned up the .linux patch to get a clean compile on glibc

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- fixed copyright field

* Mon Oct 13 1997 Michael K. Johnson <johnsonm@redhat.com>
- Updated to new pam conventions.

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- Updated to beta 15, which fixes a number of security holes. Release 1
  if for RH 4.2, release 2 is glibc based.

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved from pam.conf to pam.d

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- xferstats should look for perl in /usr/bin, not /usr/local/bin
- provides the "ftpserver" virtual package

* Thu Feb 13 1997 Michael K. Johnson <johnsonm@redhat.com>
- Updated to beta-12, and created a new PAM patch from scratch, since
  the old one made massive changes to ftpd and caused some problems.
