Summary: GNU Tape Archiver (tar)
Summary(pt_BR): GNU Tape Archiver (tar)
Summary(es): GNU Tape Archiver (tar)
Name: tar
Version: 1.12
Release: 8cl
Copyright: GPL
Group: Applications/Archiving
Group(pt_BR): Aplicações/Arquivamento
Group(es): Aplicaciones/Almacenaje
#Source: prep.ai.mit.edu:/pub/gnu/tar-1.12.tar.gz
# recompactado com bzip2
Source: prep.ai.mit.edu:/pub/gnu/tar-1.12.tar.bz2
Source1: tar-1.12.pt_BR.po
Source2: bzip2.gnutarpatch.txt
Source700: tar-man-pt_BR.tar
Patch0: tar-1.11.8-manpage.patch
Patch1: tar-1.12.pt_BR.patch
Patch2: tar-1.12-namecache.patch
Patch3: tar-1.12-pipe.patch
Prereq: info
BuildRoot: /var/tmp/tar-root

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added two patches from Red Hat to fix tar bugs
- unset LINGUAS

* Mon Mar 22 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- fixed prereq

* Fri Feb 26 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fixed typo in pt_BR.po

* Fri Feb 19 1999 Conectiva <dist@conectiva.com>
- man pages novas/revisadas

* Sat Dec  5 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Sat Nov 28 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Wed Oct 07 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- incremented release, some machines already had release 1.2, but without bzip2 support

* Thu Sep 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR summary & descriptions
- added bzip2 support patch

* Sun Apr 19 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- added pt_BR

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- updated from 1.11.8 to 1.12
- various spec file cleanups
- /sbin/install-info support

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu May 29 1997 Michael Fulbright <msf@redhat.com>
- Fixed to include rmt

%description
GNU `tar' saves many files together into a single tape or disk
archive, and can restore individual files from the archive.  It
includes multivolume support, the ability to archive sparse files,
automatic archive compression/decompression, remote archives and
special features that allow `tar' to be used for incremental and full
backups.  If you wish to do remote backups with tar, you will need
to install the `rmt' package as well.

%description -l pt_BR
GNU "tar" guarda vários arquivos juntos em uma fita ou arquivo de
disco, e pode restaurar arquivos individuais desta armazenagem. Ele
inclui suporte para multi-volumes, habilidade de armazenar arquivos
dispersos, compressão/descompressão automática, armazenamentos
remotos e características especiais que permitem "tar" ser usado
para backups incrementais e completos. Se você deseja fazer backups
remotos com tar, você irá precisar instalar o pacote "rmt".

%description -l es
GNU "tar" guarda varios archivos juntos, en una cinta o archivo de
disco, y puede restaurar archivos individuales de este almacenaje.
Incluye soporte para multivolúmenes, habilidad de almacenar archivos
dispersos, compresión/descompresión automática, almacenajes remotos y
características especiales que permiten "tar" ser usado para backups
incrementales y completos. Si deseas hacer backups remotos con tar,
te hará falta instalar el paquete "rmt".

%prep
%setup
%patch0 -p1
%patch1
%patch2 -p1
%patch3 -p1
cp $RPM_SOURCE_DIR/tar-1.12.pt_BR.po po/pt_BR.po
cd src
patch < $RPM_SOURCE_DIR/bzip2.gnutarpatch.txt
cd ..

%build
unset LINGUAS
# add /usr/include/bsd to find sgtty.h during configuration
#CPPFLAGS=-I/usr/include/bsd ./configure --disable-nls --prefix=/usr
CPPFLAGS=-I/usr/include/bsd ./configure --prefix=/usr
make CFLAGS="$RPM_OPT_FLAGS -DHAVE_STRERROR -D_GNU_SOURCE" LDFLAGS=-s LIBS=-lbsd

%install
rm -f $RPM_BUILD_ROOT/usr/info/tar.info*
make prefix=$RPM_BUILD_ROOT/usr install
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
install -m644 tar.1 $RPM_BUILD_ROOT/usr/man/man1
gzip -9nf $RPM_BUILD_ROOT/usr/info/tar.info*
mkdir -p $RPM_BUILD_ROOT/bin -p $RPM_BUILD_ROOT/usr/sbin
rm -f $RPM_BUILD_ROOT/bin/tar
mv $RPM_BUILD_ROOT/usr/bin/tar $RPM_BUILD_ROOT/bin
mv $RPM_BUILD_ROOT/usr/libexec/rmt $RPM_BUILD_ROOT/usr/sbin/rmt
strip $RPM_BUILD_ROOT/bin/tar


cd -


mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/tar-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%post
/sbin/install-info /usr/info/tar.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/tar.info.gz /usr/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
/bin/tar
/usr/sbin/rmt
/usr/info/tar.info*
/usr/man/man1/tar.1
/usr/share/locale/*/LC_MESSAGES/tar.mo
%attr(0644,root,root) /usr/man/pt_BR/man*/*
