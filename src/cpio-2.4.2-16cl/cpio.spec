Summary: A GNU archiving program.
Summary(pt_BR): Programa de empacotamento cpio da GNU (usado pelo utilitário rpm)
Summary(es): Programa de empaquetado cpio de la GNU (usado por el utilitario rpm)
Name: cpio
Version: 2.4.2
Release: 16cl
Copyright: GPL
Group: Applications/Archiving
Group(pt_BR): Aplicações/Arquivamento
Group(es): Aplicaciones/Almacenaje
Source: ftp://prep.ai.mit.edu/pub/gnu/cpio-2.4.2.tar.gz
Source700: cpio-man-pt_BR.tar
Patch0: cpio-2.3-lstat.patch
Patch1: cpio-2.4.2-glibc.patch
Patch2: cpio-2.4.2-mtime.patch
Patch3: cpio-2.4.2-svr4compat.patch
Patch4: cpio-2.4.2-glibc21.patch
Patch5: cpio-2.4.2-longlongdev.patch
Prereq: info rmt
Buildroot: /var/tmp/cpio-root

%description
GNU cpio copies files into or out of a cpio or tar archive.  Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions.  The archive can be another file on the disk, a magnetic
tape, or a pipe.  GNU cpio supports the following archive formats:  binary,
old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar and POSIX.1
tar.  By default, cpio creates binary format archives, so that they are
compatible with older cpio programs.  When it is extracting files from
archives, cpio automatically recognizes which kind of archive it is reading
and can read archives created on machines with a different byte-order.

Install cpio if you need a program to manage file archives.

%description -l pt_BR
cpio copia arquivos para dentro ou para fora ou de um "archive"
cpio ou tar, que é um arquivo que contém outros arquivos mais
informações sobre eles, como o seu nome de arquivo, dono e permissões
de acesso. O "archive" pode ser outro arquivo no disco, uma fita
magnética ou um pipe. cpio possui três modos de operação.

%description -l es
cpio copia archivos para dentro o para fuera, o de un "archive"
cpio o tar, que es un archivo que contiene otros archivos,
más información sobre ellos, como su nombre de archivo, dueño y
permisos de acceso. "archive" puede ser otro archivo en el disco,
una cinta magnética o un pipe. cpio posee tres modos de operación.

%prep
%setup -q
# patch 0 not applied
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .svr4compat
%patch4 -p1 -b .glibc21
%patch5 -p1 -b .longlongdev

%build
./configure --prefix=/usr --bindir=/bin --libexecdir=/sbin
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr bindir=$RPM_BUILD_ROOT/bin libexecdir=$RPM_BUILD_ROOT/sbin install

gzip -9nf $RPM_BUILD_ROOT/usr/info/cpio.*





mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/cpio-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/cpio.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/cpio.info.gz /usr/info/dir
fi

%files
%doc README NEWS
/bin/cpio
#/bin/mt
/usr/info/cpio.*
/usr/man/man1/cpio.1
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed prereq

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added pt_BR man pages
- Added pt_BR and es translations to spec file

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 12)

* Sat Dec  5 1998 Jeff Johnson <jbj@redhat.com>
- longlong dev wrong with "-o -H odc" headers (formerly "-oc").

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch to compile on glibc 2.1, where strdup is a macro

* Tue Jul 14 1998 Jeff Johnson <jbj@redhat.com>
- Fiddle bindir/libexecdir to get RH install correct.
- Don't include /sbin/rmt -- use the rmt from dump package.
- Don't include /bin/mt -- use the mt from mt-st package.
- Add prereq's

* Tue Jun 30 1998 Jeff Johnson <jbj@redhat.com>
- fix '-c' to duplicate svr4 behavior (problem #438)
- install support programs & info pages

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot
- removed "(used by RPM)" comment in Summary

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- no longer statically linked as RPM doesn't use cpio for unpacking packages
