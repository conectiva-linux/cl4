Summary: A collection of basic system utilities.
Summary(pt_BR): Coletânea de utilitários básicos de sistema para Linux.
Summary(es): Colectánea de utilitarios básicos de sistema para Linux.
Name: util-linux
Version: 2.9s
Release: 3cl
Copyright: distributable
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source0: ftp://sunsite.unc.edu/pub/Linux/system/Misc/util-linux-%{version}.tar.bz2
Source1: util-linux-2.7-login.pamd
Source2: util-linux-2.7-chfn.pamd
Source3: util-linux-2.7-chsh.pamd
Source4: util-linux-2.9s-pt_BR.po
Source700: util-linux-man-pt_BR.tar
Patch0: util-linux-2.9i-rhconfig.patch
Patch1: util-linux-2.9i-nochkdupexe.patch
Patch2: util-linux-2.7-gecos.patch
# XXX apply next  patch to enable mount-2.8 from util-linux (not applied)
Patch4: util-linux-2.9i-mount.patch
Patch6: util-linux-2.9i-fdiskwarning.patch
Patch8: util-linux-2.9i-nomount.patch
Patch11: util-linux-2.9o-btmp.patch
Patch13: util-linux-2.9o-openlog.patch
Patch16: util-linux-2.9o-mkswap2.patch
Patch17: util-linux-2.9s-install_po.patch

Obsoletes: fdisk
%ifarch sparc
Obsoletes: clock
%endif
BuildRoot: /var/tmp/%{name}-root
Requires: pam >= 0.66-4

%description
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function.
Among many features, Util-linux contains the fdisk configuration
tool and login program.

You should install util-linux for its essential system tools.

%description -l pt_BR
util-Linux contém uma grande variedade de utilitários de sistema
de baixo-nível necessários para um sistema Linux funcional. Isso
inclui, entre outras coisas, ferramentas de configuração como fdisk
e programas de sistema como login.

%description -l es
util-Linux contiene una gran variedad de utilitarios de sistema de
bajo nivel necesarios a un sistema Linux funcional. Esto incluye,
entre otras cosas, herramientas de configuración como fdisk y
programas de sistema como login.

%prep

%setup -q

%patch0 -p1 -b .rhconfig
%patch1 -p1 -b .nochkdupexe
%patch2 -p1 -b .gecos

# mount comes from it's own rpm (again)
#%patch4 -p1 -b .mount

%patch6 -p1 -b .fdiskwarning
%patch8 -p1 -b .nomount
%patch11 -p1 -b .btmp
%patch13 -p1 -b .openlog
%patch16 -p1 -b .mkswap2
%patch17 -p1 -b .po-install

%build
[ "$LINGUAS" ] && unset LINGUAS
cp $RPM_SOURCE_DIR/util-linux-2.9s-pt_BR.po \
	$RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
./configure
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{bin,etc/pam.d,sbin}
mkdir -p $RPM_BUILD_ROOT/usr/{bin,info,lib,man/man1,man/man6,man/man8,sbin}

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT/usr/info/ipc.info

for i in /bin/login /usr/bin/chfn /usr/bin/chsh /usr/bin/newgrp ; do
	strip $RPM_BUILD_ROOT/$i
done

strip $RPM_BUILD_ROOT/sbin/fdisk || :

install -m 644 ${RPM_SOURCE_DIR}/util-linux-2.7-login.pamd $RPM_BUILD_ROOT/etc/pam.d/login
install -m 644 ${RPM_SOURCE_DIR}/util-linux-2.7-chsh.pamd $RPM_BUILD_ROOT/etc/pam.d/chsh
install -m 644 ${RPM_SOURCE_DIR}/util-linux-2.7-chsh.pamd $RPM_BUILD_ROOT/etc/pam.d/chfn

rm -f $RPM_BUILD_ROOT/sbin/clock
ln -s hwclock $RPM_BUILD_ROOT/sbin/clock





mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/util-linux-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%ifnarch alpha
/sbin/clock
/sbin/hwclock
%endif
/usr/man/man8/hwclock.8

%config /etc/pam.d/login
%config /etc/pam.d/chfn
%config /etc/pam.d/chsh

/sbin/fdisk
%ifarch i386 alpha armv4l
/sbin/cfdisk
%endif

%ifarch i386 alpha
/sbin/fsck.minix
/sbin/mkfs.minix
%endif

/sbin/mkfs
/sbin/mkswap

/usr/bin/fdformat
/usr/bin/setfdprm
/etc/fdprm

/usr/man/man8/fdformat.8
/usr/man/man8/mkswap.8
/usr/man/man8/setfdprm.8

/usr/games/banner
/usr/man/man6/banner.6

/usr/bin/ddate
/usr/man/man1/ddate.1

%ifarch i386 alpha sparc
/bin/login
%attr(4711,root,root)	/usr/bin/chfn
%attr(4711,root,root)	/usr/bin/chsh
%attr(4711,root,root)	/usr/bin/newgrp
/usr/sbin/vipw
/usr/sbin/vigr
/usr/man/man1/chfn.1
/usr/man/man1/chsh.1
/usr/man/man1/login.1
/usr/man/man1/newgrp.1
/usr/man/man8/vipw.8
%endif

/bin/kill
/usr/bin/cal
#/usr/bin/hostid
/usr/bin/logger
/usr/bin/look
/usr/bin/mcookie
/usr/bin/namei
/usr/bin/script
/usr/bin/setterm
/usr/bin/tsort
/usr/bin/whereis
%attr(2755,root,tty)	/usr/bin/write
/usr/bin/getopt
/usr/man/man1/cal.1
#/usr/man/man1/hostid.1
/usr/man/man1/kill.1
/usr/man/man1/logger.1
/usr/man/man1/look.1
/usr/man/man1/mcookie.1
/usr/man/man1/namei.1
/usr/man/man1/script.1
/usr/man/man1/setterm.1
/usr/man/man1/tsort.1
/usr/man/man1/whereis.1
/usr/man/man1/write.1
/usr/man/man1/getopt.1

/bin/dmesg

/sbin/ctrlaltdel
/sbin/kbdrate
#/sbin/sln
/bin/arch
/usr/bin/ipcrm
/usr/bin/ipcs
/usr/bin/renice
/usr/sbin/readprofile
/usr/bin/setsid
/usr/sbin/ramsize
%ifarch i386 alpha armv4l
/usr/bin/cytune
/usr/sbin/swapdev
/usr/sbin/vidmode
%endif
/usr/sbin/rootflags

/usr/man/man1/arch.1
/usr/man/man1/readprofile.1
/usr/man/man8/cytune.8
/usr/man/man8/ctrlaltdel.8
/usr/man/man8/dmesg.8
/usr/man/man8/ipcrm.8
/usr/man/man8/ipcs.8
/usr/man/man8/kbdrate.8
/usr/man/man8/ramsize.8
/usr/man/man8/renice.8
/usr/man/man8/rootflags.8
/usr/man/man8/setsid.8
/usr/man/man8/swapdev.8
/usr/man/man8/vidmode.8

%ifarch i386
/usr/sbin/rdev
/usr/man/man8/rdev.8
%endif

/usr/info/ipc.info.gz

/usr/bin/col
/usr/bin/colcrt
/usr/bin/colrm
/usr/bin/column
/usr/bin/hexdump
/usr/bin/rev
/usr/bin/ul

/usr/man/man1/col.1
/usr/man/man1/colcrt.1
/usr/man/man1/colrm.1
/usr/man/man1/column.1
/usr/man/man1/hexdump.1
/usr/man/man1/rev.1
/usr/man/man1/ul.1
/bin/more
/usr/man/man1/more.1
/usr/lib/more.help

%ifarch i386 alpha
/usr/man/man8/fsck.minix.8
/usr/man/man8/mkfs.minix.8
/usr/man/man8/mkfs.8
%endif

/usr/man/man8/fdisk.8

%ifarch i386 alpha armv4l
/usr/man/man8/cfdisk.8
%endif

/usr/share/locale/*/LC_MESSAGES/util-linux.mo

%doc */README.*

%ifarch i386 alpha
/sbin/sfdisk
/usr/man/man8/sfdisk.8
%doc fdisk/sfdisk.examples
%endif
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Thu Jul 01 1999 Rodrigo Stulzer Lopes <rodrigo@conectiva.com>
- Updated pt_BR.po

* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to util-linux
- unset LINGUAS

* Tue Jun 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed
- included /usr/share/locale* in %files

* Fri Jun 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9s.

* Sat May 29 1999 Jeff Johnson <jbj@redhat.com>
- fix mkswap sets incorrect bits on sparc64 (#3140).

* Thu Apr 15 1999 Jeff Johnson <jbj@redhat.com>
- on sparc64 random ioctls on clock interface cause kernel messages.

* Thu Apr 15 1999 Jeff Johnson <jbj@redhat.com>
- improved raid patch (H.J. Lu).

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- added patch for smartraid controllers

* Sat Apr 10 1999 Cristian Gafton <gafton@redhat.com>
- fix logging problems caused by setproctitle and PAM interaction
  (#2045)

* Wed Mar 31 1999 Jeff Johnson <jbj@redhat.com>
- include docs and examples for sfdisk (#1164)

* Mon Mar 29 1999 Matt Wilson <msw@redhat.com>
- rtc is not working properly on alpha, we can't use hwclock yet.

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add patch to make mkswap more 64 bit friendly... Patch from
  eranian@hpl.hp.com (ahem!)

* Thu Mar 25 1999 Jeff Johnson <jbj@redhat.com>
- include sfdisk (#1164)
- fix write (#1784)
- use positive logic in spec file (%ifarch rather than %ifnarch).
- (re)-use 1st matching utmp slot if search by mypid not found.
- update to 2.9o
- lastb wants bad logins in wtmp clone /var/run/btmp (#884)

* Thu Mar 25 1999 Jakub Jelinek <jj@ultra.linux.cz>
- if hwclock is to be compiled on sparc,
  it must actually work. Also, it should obsolete
  clock, otherwise it clashes.
- limit the swap size in mkswap for 2.2.1+ kernels
  by the actual maximum size kernel can handle.
- fix kbdrate on sparc, patch by J. S. Connell
  <ankh@canuck.gen.nz>

* Wed Mar 24 1999 Matt Wilson <msw@redhat.com>
- added pam_console back into pam.d/login

* Tue Mar 23 1999 Matt Wilson <msw@redhat.com>
- updated to 2.9i
- added hwclock for sparcs and alpha

* Mon Mar 22 1999 Erik Troan <ewt@redhat.com>
- added vigr to file list

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 12)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- remove most of the ifnarch arm stuff

* Mon Mar 15 1999 Michael Johnson <johnsonm@redhat.com>
- added pam_console.so to /etc/pam.d/login

* Thu Feb  4 1999 Michael K. Johnson <johnsonm@redhat.com>
- .perms patch to login to make it retain root in parent process
  for pam_close_session to work correctly

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- strip fdisk in buildroot correctly (#718)

* Mon Jan 11 1999 Cristian Gafton <gafton@redhat.com>
- have fdisk compiled on sparc and arm

* Mon Jan 11 1999 Erik Troan <ewt@redhat.com>
- added beos partition type to fdisk

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- incorporate fdisk on all arches

* Sat Dec  5 1998 Jeff Johnson <jbj@redhat.com>
- restore PAM functionality at end of login (Bug #201)

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch top build on the arm without PAM and related utilities, for now.
- build hwclock only on intel

* Wed Nov 18 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 2.9

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide (slang-1.2.2)
- patch kbdrate wackiness so it builds with egcs

* Tue Oct 13 1998 Erik Troan <ewt@redhat.com>
- patched more to use termcap

* Mon Oct 12 1998 Erik Troan <ewt@redhat.com>
- added warning about alpha/bsd label starting cylinder

* Mon Sep 21 1998 Erik Troan <ewt@redhat.com>
- use sigsetjmp/siglongjmp in more rather then sig'less versions

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- explicit attrs for setuid/setgid programs

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- sln is now included in glibc

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- add cbm1581 floppy definitions (problem #787)

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- remove /etc/nologin at end of shutdown/halt.

* Fri Jun 19 1998 Jeff Johnson <jbj@redhat.com>
- add mount/losetup.

* Thu Jun 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.8 with 2.8b clean up. hostid now defunct?

* Mon Jun 01 1998 David S. Miller <davem@dm.cobaltmicro.com>
- "more" now works properly on sparc

* Sat May 02 1998 Jeff Johnson <jbj@redhat.com>
- Fix "fdisk -l" fault on mounted cdrom. (prob #513)

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild

* Mon Dec 29 1997 Erik Troan <ewt@redhat.com>
- more didn't suspend properly on glibc
- use proper tc*() calls rather then ioctl's

* Sun Dec 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed a security problem in chfn and chsh accepting too 
  long gecos fields

* Fri Dec 19 1997 Mike Wangsmo <wanger@redhat.com>
- removed "." from default path

* Tue Dec 02 1997 Cristian Gafton <gafton@redhat.com>
- added (again) the vipw patch

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- minor cleanups for glibc 2.1

* Fri Oct 17 1997 Michael Fulbright <msf@redhat.com>
- added vfat32 filesystem type to list recognized by fdisk

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- don't build clock on the alpha 
- don't install chkdupexe

* Thu Oct 02 1997 Michael K. Johnson <johnsonm@redhat.com>
- Update to new pam standard.
- BuildRoot.

* Thu Sep 25 1997 Cristian Gafton <gafton@redhat.com>
- added rootok and setproctitle patches
- updated pam config files for chfn and chsh

* Tue Sep 02 1997 Erik Troan <ewt@redhat.com>
- updated MCONFIG to automatically determine the architecture
- added glibc header hacks to fdisk code
- rdev is only available on the intel

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- update to util-linux 2.7, fixed login problems

* Wed Jun 25 1997 Erik Troan <ewt@redhat.com>
- Merged Red Hat changes into main util-linux source, updated package to
  development util-linux (nearly 2.7).

* Tue Apr 22 1997 Michael K. Johnson <johnsonm@redhat.com>
- LOG_AUTH --> LOG_AUTHPRIV in login and shutdown

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved to new pam and from pam.conf to pam.d

* Tue Feb 25 1997 Michael K. Johnson <johnsonm@redhat.com>
- pam.patch differentiated between different kinds of bad logins.
  In particular, "user does not exist" and "bad password" were treated
  differently.  This was a minor security hole.
