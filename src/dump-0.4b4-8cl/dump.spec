Summary: Programs for backing up and restoring filesystems.
Summary(pt_BR): Sistema de backup dump/restore
Summary(es): Sistema de copia de seguridad dump/restore
Name: dump
Version: 0.4b4
Release: 8cl
Copyright: UCB
Group: Applications/Archiving
Group(pt_BR): Aplicações/Arquivamento
Group(es): Aplicaciones/Almacenaje
Source: ftp://tsx-11.mit.edu/pub/linux/ALPHA/ext2fs/dump-%{version}.tar.gz
Patch2: dump-0.4b4-glibc.patch
Patch4: dump-0.3-kernel.patch
Patch5: dump-0.3-bread.patch
Patch6: dump-0.4b4.path.patch
Requires: rmt
BuildRoot: /var/tmp/%{name}-root

%description
The dump package contains both dump and restore.  Dump examines files in
a filesystem, determines which ones need to be backed up, and copies
those files to a specified disk, tape or other storage medium.  The
restore command performs the inverse function of dump; it can restore a
full backup of a filesystem.  Subsequent incremental backups can then be
layered on top of the full backup.  Single files and directory subtrees
may also be restored from full or partial backups.

Install dump if you need a system for both backing up filesystems and
restoring filesystems after backups.

%description -l pt_BR
o dump e o restore podem ser usados para fazer backup em partições
ext2 de várias maneiras diferentes.

%description -l es
Dump y restore pueden ser usados para hacer copias de seguridad en
particiones ext2 de varias maneras diferentes.

%package -n rmt
Summary: Provides certain programs with access to remote tape devices.
Summary(pt_BR): Acesso a dispositivo de fita remoto (em rede)
Summary(es): Acceso a dispositivo de cinta remoto (en red)
Group: Applications/Archiving
Group(pt_BR): Aplicações/Arquivamento
Group(es): Aplicaciones/Almacenaje

%description -n rmt
The rmt utility provides remote access to tape devices for programs
like dump (a filesystem backup program), restore (a program for
restoring files from a backup) and tar (an archiving program).

%description -l pt_BR -n rmt
rmt provê acesso remoto a dispositivos de fita para programas como
dump, restore e tar.

%description -l es -n rmt
rmt provee acceso remoto a dispositivos de cinta para programas como
dump, restore y tar.

%prep
%setup -q
%patch2 -p1 -b .glibc
%patch4 -p1 -b .kernel
%patch5 -p1 -b .bread
%patch6 -p1 -b .path

%build
./configure --prefix=%{_prefix} \
	--with-binmode=6755 \
	--with-manowner=root \
	--with-mangrp=root \
	--with-manmode=0644 \
	--enable-rmt
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/man/man8

make install BINDIR=$RPM_BUILD_ROOT/sbin MANDIR=${RPM_BUILD_ROOT}%{_prefix}/man/man8

{ cd $RPM_BUILD_ROOT
  strip ./sbin/* || :
  ln -sf dump ./sbin/rdump
  ln -sf restore ./sbin/rrestore
  chmod ug-s ./sbin/rmt
  mkdir -p ./etc
  > ./etc/dumpdates
  ln -sf ../sbin/rmt ./etc/rmt
}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES COPYRIGHT KNOWNBUGS README THANKS TODO dump-*.announce dump.lsm
%attr(0664,root,disk)	%config(noreplace) /etc/dumpdates
%attr(6755,root,tty)	/sbin/dump
/sbin/rdump
%attr(6755,root,tty)	/sbin/restore
/sbin/rrestore
%{_prefix}/man/man8/dump.8
%{_prefix}/man/man8/rdump.8
%{_prefix}/man/man8/restore.8
%{_prefix}/man/man8/rrestore.8

%files -n rmt
%defattr(-,root,root)
%attr(0755,root,root)	/sbin/rmt
/etc/rmt
%{_prefix}/man/man8/rmt.8 

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 25 1999 Jeff Johnson <jbj@redhat.com>
- remove setuid/setgid bits from /sbin/rmt (dump/restore are OK).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.

* Thu Mar 18 1999 Jeff Johnson <jbj@redhat.com>
- Fix dangling symlinks (#1551).

* Wed Mar 17 1999 Michael Maher <mike@redhat.com>
- Top O' the morning, build root's fixed for man pages.  

* Fri Feb 19 1999 Preston Brown <pbrown@redhat.com>
- upgraded to dump 0.4b4, massaged patches.

* Tue Feb 02 1999 Ian A Cameron <I.A.Cameron@open.ac.uk>
- added patch from Derrick J Brashear for traverse.c to stop bread errors

* Wed Jan 20 1999 Jeff Johnson <jbj@redhat.com>
- restore original 6755 root.tty to dump/restore, defattr did tty->root (#684).
- mark /etc/dumpdates as noreplace.

* Tue Jul 14 1998 Jeff Johnson <jbj@redhat.com>
- add build root.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- added a patch for resolving linux/types.h and sys/types.h conflicts

* Wed Dec 31 1997 Erik Troan <ewt@redhat.com>
- added prototype of llseek() so dump would work on large partitions

* Thu Oct 30 1997 Donnie Barnes <djb@redhat.com>
- made all symlinks relative instead of absolute

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved rmt to its own package.

* Tue Feb 11 1997 Michael Fulbright <msf@redhat.com>
- Added endian cleanups for SPARC

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com> 
- Made /etc/dumpdates writeable by group disk.
