Summary: The GNU versions of common file management utilities.
Summary(pt_BR): Utilitários para manipulação de arquivos da GNU
Summary(es): Utilitarios para manejo de archivos de la GNU
Name: fileutils
Version: 4.0
Release: 3cl
Copyright: GPL
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
Source0: ftp://prep.ai.mit.edu/pub/gnu/fileutils-%{version}.tar.bz2
Source1: DIR_COLORS
Source2: fileutils-4.0-pt_BR.po
Source700: fileutils-man-pt_BR.tar
Patch0: fileutils-4.0-glibc21.patch
Buildroot: /var/tmp/fileutils-root
Prereq: /sbin/install-info
BuildPrereq: gettext

%description
The fileutils package includes a number of GNU versions of common and
popular file management utilities.  Fileutils includes the following
tools: chgrp (changes a file's group ownership), chown (changes a file's
ownership), chmod (changes a file's permissions), cp (copies files),
dd (copies and converts files), df (shows a filesystem's disk usage), dir
(gives a brief directory listing), dircolors (the setup program for the
color version of the ls command), du (shows disk usage), install (copies
files and sets permissions), ln (creates file links), ls (lists directory
contents in color), mkdir (creates directories), mkfifo (creates FIFOs,
which are named pipes), mknod (creates special files), mv (renames files),
rm (removes/deletes files), rmdir (removes empty directories), sync
(synchronizes memory and disk), touch (changes file timestamps), and vdir
(provides long directory listings).

You should install the fileutils package, because it includes many file
management utilities that you'll use frequently.

%description -l pt_BR
Estes são os utilitários GNU para gerenciamento de arquivos. Inclui
programas para copiar, mover, listar arquivos, e etc.

O programa ls neste pacote agora incorpora o ls colorido!

%description -l es
Estos son los utilitarios GNU para administración de
archivos. Incluye programas para copiar, mover, listar archivos, y
etc.  El programa ls en este paquete ahora incorpora el ls colorido!

%prep
%setup -q
%patch0 -p1

%build
[ "$LINGUAS" ] && unset LINGUAS
mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/etc
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --exec-prefix=/
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT/ install
gzip -9nf $RPM_BUILD_ROOT/usr/info/fileutils*
mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/etc
mv -f $RPM_BUILD_ROOT/bin/install $RPM_BUILD_ROOT/usr/bin/install
mv -f $RPM_BUILD_ROOT/bin/du $RPM_BUILD_ROOT/usr/bin/du
mv -f $RPM_BUILD_ROOT/bin/dir $RPM_BUILD_ROOT/usr/bin/dir
mv -f $RPM_BUILD_ROOT/bin/vdir $RPM_BUILD_ROOT/usr/bin/vdir
mv -f $RPM_BUILD_ROOT/bin/mkfifo $RPM_BUILD_ROOT/usr/bin/mkfifo
mv -f $RPM_BUILD_ROOT/bin/dircolors $RPM_BUILD_ROOT/usr/bin/dircolors

cd $RPM_BUILD_ROOT
strip usr/bin/install usr/bin/du bin/chgrp bin/chown bin/chmod bin/cp
strip bin/dd usr/bin/dir bin/ln usr/bin/vdir bin/ls bin/mkdir
strip usr/bin/mkfifo bin/mknod bin/mv bin/rm bin/rmdir bin/sync
strip bin/touch bin/df usr/bin/dircolors

install -m644 -o root -g root $RPM_SOURCE_DIR/DIR_COLORS $RPM_BUILD_ROOT/etc


mkdir -p $RPM_BUILD_ROOT/usr/share/locale/pt_BR/LC_MESSAGES
msgfmt -o $RPM_BUILD_ROOT/usr/share/locale/pt_BR/LC_MESSAGES/fileutils.mo \
	$RPM_SOURCE_DIR/fileutils-4.0-pt_BR.po


mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/fileutils-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/fileutils.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/fileutils.info.gz /usr/info/dir
fi

%files
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%config /etc/DIR_COLORS
/usr/bin/install
/usr/bin/du
/bin/chgrp
/bin/chown
/bin/chmod
/bin/cp
/bin/dd
/usr/bin/dir
/bin/ln
/usr/bin/vdir
/bin/ls
/usr/bin/dircolors
/bin/mkdir
/usr/bin/mkfifo
/bin/mknod
/bin/mv
/bin/rm
/bin/rmdir
/bin/sync
/bin/touch
/bin/df

/usr/man/man1/chgrp.1
/usr/man/man1/chown.1
/usr/man/man1/chmod.1
/usr/man/man1/cp.1
/usr/man/man1/dd.1
/usr/man/man1/df.1
/usr/man/man1/dir.1
/usr/man/man1/dircolors.1
/usr/man/man1/du.1
/usr/man/man1/install.1
/usr/man/man1/ln.1
/usr/man/man1/ls.1
/usr/man/man1/mkdir.1
/usr/man/man1/mkfifo.1
/usr/man/man1/mknod.1
/usr/man/man1/mv.1
/usr/man/man1/rm.1
/usr/man/man1/rmdir.1
/usr/man/man1/sync.1
/usr/man/man1/touch.1
/usr/man/man1/vdir.1

/usr/info/fileutils*

/usr/share/locale/*/*/*
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- included updated pt_BR translation made by
  Rodrigo Stulzer Lopes <rodrigo@conectiva.com>

* Wed May 19 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x and kernel 2.2.x
- Added pt_BR man pages
- Added pt_BR and spanish translations to spec file

* Tue Mar 23 1999 Cristian Gafton <gafton@redhat.com>
- version 4.0

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 12)

* Thu Aug 06 1998 Erik Troan <ewt@redhat.com>
- got install-info stuff working in %post/%pre

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild
- added %clean

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- minor patch for glibc 2.1

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- install-info turned off, as it creates a prereq loop

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- install-info turned on
- added BuildRoot

* Mon Sep 15 1997 Erik Troan <ewt@redhat.com>
- can't use install-info until %post -p allows argument passing

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info

* Fri May 16 1997 Erik Troan <ewt@redhat.com>
- rebuilt for glibc.

* Tue Feb 25 1997 Erik Troan <ewt@redhat.com>
- Hacked at mktime() test to work on 64 bit machines w/ broken mktime(). I
  told Ulrich Drepper and Richard Henderson about this, so hopefully glibc
  will get fixed.

* Thu Feb 20 1997 Michael Fulbright <msf@redhat.com>
- Updated to version 3.16.
