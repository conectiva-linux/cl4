Summary: Programs for accessing MS-DOS disks without mounting the disks.
Summary(pt_BR): Programas para acessar discos DOS sem montá-los
Summary(es): Programas para acceder discos DOS sin montarlos
Name: mtools
Version: 3.9.1
Release: 8cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: http://www.tux.org/pub/tux/knaff/mtools/mtools-3.9.1.tar.gz 
Source700: mtools-man-pt_BR.tar
Url: http://www.tux.org/pub/tux/knaff/mtools/index.html
Buildroot: /var/tmp/mtools-root
Patch0: mtools-3.9.1-linux.patch
Patch1: mtools-3.9.1-newkernel.patch
Patch2: mtools-3.9.1-ref.patch
Prereq: info


%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 Xdf disks, and 2m disks.

Mtools should be installed if you need to use MS-DOS disks.

%description -l pt_BR
Mtools é uma coleção de utilitários para acessar discos MS-DOS no
Unix sem montá-los. Ele suporta nomes longos de arquivos estilo
Win'95, discos OS/2 Xdf, discos ZIP/JAZ e discos 2m (armazena até
1992k em um disco 3 1/2 de alta densidade).

%description -l es
Mtools es una colección de utilitarios para acceder a discos MS-DOS
en Unix sin montarlos. Soporta nombres largos de archivos estilo
Win'95, discos OS/2 Xdf, discos ZIP/JAZ y discos 2m (almacena hasta
1992k en un disco 3 1/2 de alta densidad).

%prep
%setup -q
%patch0 -p1 -b .linux
%patch1 -p1 -b .newkern
%patch2 -p1 -b .ref

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --sysconfdir=/etc
make
strip mtools mkmanifest

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr $RPM_BUILD_ROOT/etc
make prefix=$RPM_BUILD_ROOT/usr install
/usr/bin/install -c -m 644 mtools.conf $RPM_BUILD_ROOT/etc
gzip -9f $RPM_BUILD_ROOT/usr/info/*



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/mtools-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/mtools.info.gz /usr/info/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/mtools.info.gz /usr/info/dir
fi

%files
%config /etc/mtools.conf
%doc COPYING Changelog README Release.notes mtools.texi
/usr/bin/*
/usr/man/man*/*.[0-9]
/usr/info/*
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- patch to make the texi sources compile
- fix the spec file group and description
- fixed floppy drive sizes

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0
- fixed invalid SAMPLE_FILE configuration file

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- Built package for 5.2.
- Updated Source to 3.9.1.
- Cleaned up spec file.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 3.8

* Tue Oct 21 1997 Otto Hammersmith
- changed buildroot to /var/tmp, rather than /tmp
- use install-info

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Apr 17 1997 Erik Troan <ewt@redhat.com>
- Changed sysconfdir to be /etc

* Mon Apr 14 1997 Michael Fulbright <msf@redhat.com>
- Updated to 3.6
