Summary: The System V system initialization program.
Summary(pt_BR): Programa de inicialização System V
Summary(es): Programa de inicialización System V
Name: SysVinit
%define version 2.74
Version: %{version}
Release: 12cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.cistron.nl/pub/people/miquels/software/sysvinit-2.74.tar.bz2
Source1: shutdown.pamd
Source700: SysVinit-man-pt_BR.tar
Patch0: sysvinit-2.74-rh.patch
Patch1: sysvinit-2.71-md5.patch
Patch2: sysvinit-2.74-nologin.patch
Patch3: sysvinit-2.74-sigpwr.patch
Patch4: sysvinit-2.74-securelevel-security.patch
Buildroot: /var/tmp/init-root
Requires: pam >= 0.66-5

%description
The SysVinit package contains a group of processes that
control the very basic functions of your system. SysVinit is
the first program started by the Linux kernel when the
system boots, controlling the startup, running and shutdown
of all other programs.

%description -l pt_BR
SysVinit é o primeiro programa executado pelo kernel Linux quando
o sistema é inicializado. Controla inicialização, funcionamento e
finalização de todos os outros programas.

%description -l es
SysVinit es el primer programa ejecutado por el kernel Linux cuando
se inicia el sistema. Controla arranque, funcionamiento y cierre
de todos los otros programas.

%prep
%setup -q -n sysvinit-%{version}
%patch0 -p1 -b .rh
%patch1 -p1 -b .md5
%patch2 -p1 -b .nologin
%patch3 -p1 -b .sigpwr
%patch4 -p1 -b .seclvl

%build
make -C src

%install
rm -rf $RPM_BUILD_ROOT
for I in sbin usr/bin usr/man/man{1,3,5,8} etc var/run dev; do
	mkdir -p $RPM_BUILD_ROOT/$I
done
make -C src ROOT=$RPM_BUILD_ROOT install
#ln -sf ../var/run/initrunlvl $RPM_BUILD_ROOT/etc

mkdir -p $RPM_BUILD_ROOT/etc/pam.d $RPM_BUILD_ROOT/etc/security/console.apps
for wrapapp in shutdown halt reboot poweroff ; do
  ln -sf consolehelper $RPM_BUILD_ROOT/usr/bin/$wrapapp
  touch $RPM_BUILD_ROOT/etc/security/console.apps/$wrapapp
  cp $RPM_SOURCE_DIR/shutdown.pamd $RPM_BUILD_ROOT/etc/pam.d/$wrapapp
done

# If this already exists, just do nothing (the ||: part)
mknod --mode=0600 $RPM_BUILD_ROOT/dev/initctl p ||:






mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/SysVinit-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%post
[ -e /var/run/initrunlvl ] && ln -s ../var/run/initrunlvl /etc/initrunlvl
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/Propaganda doc/changelog doc/Install README.RIGHT.NOW
%doc doc/sysvinit-%{version}.lsm contrib/start-stop-daemon.* 
/sbin/halt
/sbin/init
/sbin/killall5
/sbin/pidof
/sbin/poweroff
/sbin/reboot
/sbin/runlevel
/sbin/shutdown
/sbin/sulogin
/sbin/telinit

/usr/bin/last
/usr/bin/lastb
/usr/bin/mesg
/usr/bin/utmpdump
%attr(2555,root,tty)  /usr/bin/wall
/usr/man/man*/*
#/etc/initrunlvl
/dev/initctl

/usr/bin/shutdown
/usr/bin/halt
/usr/bin/reboot
/usr/bin/poweroff
%config(noreplace) /etc/pam.d/shutdown
%config(noreplace) /etc/pam.d/halt
%config(noreplace) /etc/pam.d/reboot
%config(noreplace) /etc/pam.d/poweroff
%config(missingok) /etc/security/console.apps/shutdown
%config(missingok) /etc/security/console.apps/halt
%config(missingok) /etc/security/console.apps/reboot
%config(missingok) /etc/security/console.apps/poweroff
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed
- fixed release (add cl)

* Mon Jun 14 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 20 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Apr 17 1999 Jeff Johnson <jbj@redhat.com>
- remove /etc/initlvl compatibility symlink from file list (#2236).

* Fri Mar 26 1999 Michael Johnson <johnsonm@redhat.com>
- pam.d files marked noreplace
- added poweroff as a console application

* Mon Mar 22 1999 Michael Johnson <johnsonm@redhat.com>
- marked config files as such in consolehelper part of filelist

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)

* Fri Mar 19 1999 Michael Johnson <johnsonm@redhat.com>
- consolehelper support

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- glibc 2.1

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- poweroff symlink not included (problem #762)

* Thu Jul 09 1998 Chris Evans <chris@ferret.lmh.ox.ac.uk>
- Fix a securelevel releated security hole. Go on, try and break append
  only files + securelevel now ;-)

* Wed Jul  8 1998 Jeff Johnson <jbj@redhat.com>
- remove /etc/nologin at end of shutdown.
- compile around missing SIGPWR on sparc

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.74
- fixed the package source url... (yeah, it was wrong !)

* Wed Oct 1 1997 Cristian Gafton <gafton@redhat.com>
- fixed the MD5 check in sulogin (128 hash bits encoded with base64 gives
  22 bytes, not 24...). Fix in -md5.patch

* Thu Sep 11 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- /etc/initrunlvl gets linked to /tmp/init-root/var/run/initrunlvl which is
  just plain wrong..
- /usr/bin/utmpdump was missing in the files section, although it was
  explicitly patched into PROGS.
- added attr's to the files section.
- various small fixes.

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- updated to 2.71
- built against glibc 2.0.4

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added sulogin.8 man page to file list.
