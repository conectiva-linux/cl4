Summary: A file compression and packaging utility compatible with PKZIP.
Summary(pt_BR): Cria arquivos .zip compatíveis com PKZIP(tm)
Summary(es): Crea archivos .zip compatibles con PKZIP(tm)
Name: zip
Version: 2.1
Release: 8cl
Copyright: distributable
Group: Applications/Archiving
Group(pt_BR): Aplicações/Arquivamento
Group(es): Aplicaciones/Almacenaje
Source: ftp.uu.net:/pub/archiving/zip/zip21.zip
Source700: zip-man-pt_BR.tar
Patch0: zip21.patch
Patch1: zip-2.1-arm.patch
Prefix: /usr
BuildRoot: /var/tmp/zip-root

%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and is
compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%description -l pt_BR
zip é um utilitário de compressão e empacotamento de arquivo para
Unix, VMS, MSDOS, OS/2, Windows NT, Minix, Atari e Machintosh. Ele
é equivalente ao uso de programas UNIX como tar(1) e compress(1)
combinados e é compatível com o PKZIP (ZIP de Phil Katz para
sistemas MSDOS).

%description -l es
zip es un utilitario de compresión y empaquetado de archivo para
Unix, VMS, MSDOS, OS/2, Windows NT, Minix, Atari y Machintosh. Y
equivale al uso de programas UNIX como tar(1) y compress(1)
combinados y es compatible con PKZIP (ZIP de Phil Katz para sistemas
MSDOS).

%prep
%setup -T -c -q 
unzip $RPM_SOURCE_DIR/zip21.zip
%patch0 -p1
%patch1 -p1

%build
make -f unix/Makefile prefix=/usr "RPM_OPT_FLAGS=$RPM_OPT_FLAGS" generic_gcc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make -f unix/Makefile prefix=$RPM_BUILD_ROOT/usr install

pushd $RPM_BUILD_ROOT
for n in zipnote zipsplit zip zipcloak ; do
    strip ./usr/bin/$n
done
popd


mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/zip-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Where algorith.doc install.doc zip.doc TODO infozip.who
/usr/bin/zipgrep
/usr/bin/zipnote
/usr/bin/zipsplit
/usr/bin/zip
/usr/bin/zipcloak
/usr/man/man1/zip.1
/usr/man/man1/zipgrep.1
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added pt_BR man pages

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- updated text in the spec file

* Fri Jan 15 1999 Cristian Gafton <gafton@redhat.com>
- patch top build on the arm

* Mon Dec 21 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
