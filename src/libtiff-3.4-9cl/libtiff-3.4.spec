Summary: Library for handling TIFF files.
Summary(pt_BR): Biblioteca de manipulação de arquivos TIFF
Summary(es): Biblioteca de manipulación de archivos TIFF
Name: libtiff
Version: 3.4
Release: 9cl
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: ftp://ftp.sgi.com/graphics/tiff/tiff-v3.4-tar.gz
Patch0: tiff-v3.4-glibc.patch
Patch1: tiff-v3.4-shlib.patch
Url: http://www-mipl.jpl.nasa.gov/~ndr/tiff/
Buildroot: /var/tmp/libtiff-root
%define LIBVER 3.4
Summary(de): Library zum Verwalten von TIFF-Dateien
Summary(fr): Bibliothèque de gestion des fichiers TIFF
Summary(tr): TIFF dosyalarýný iþleme kitaplýðý

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Nov 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Michael Fulbright <msf@redhat.com>
- rebuilt against fixed jpeg libs (libjpeg-6b)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- new version to replace the one from libgr
- patched for glibc
- added shlib support

%description
This package is a library of functions that manipulate TIFF images.

%description -l pt_BR
Este pacote é uma biblioteca de funções para manipulação de
imagens TIFF.

%description -l es
Este paquete es una biblioteca de funciones para la manipulación
de imágenes TIFF.

%package devel
Summary: headers and static libraries for developing programs using libtiff
Summary(pt_BR): Arquivos de inclusão e bibliotecas estáticas para desenvolver programas usando libtiffs. 
Summary(es): Archivos de inclusión y bibliotecas estáticas para desarrollar programas usando libtiffs. 
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: libtiff
Summary(de): Headers und statische Libraries zur Entwicklung von Programmen  unter Verwendung von libtiff
Summary(fr): en-têtes et bibliothèques statiques pour développement avec libtiff"
Summary(tr): libtiff kitaplýðýyla geliþtirme için gerekli dosyalar

%description devel
This package is all you need to develop programs that manipulate tiff
images.

%description -l pt_BR devel
Este pacote é tudo que você precisa para desenvolver um programa
que manipula imagens TIFF.

%description -l es devel
Este paquete es todo lo que necesitas para desarrollar un programa
que manipule imágenes TIFF.

%description -l de devel
Dieses Paket enthält alles, was Sie zum Entwickeln von Programmen
zum Bearbeiten von tiff-Bildern benötigen.

%description -l de
Eine Library von Funktionen zur Manipulation von TIFFs.

%description -l fr devel
Ce package contient tout le nécessaire pour réaliser des programmes
manipulant des images au format tiff.

%description -l fr
Bibliothèque de fonctions pour manipuler des images TIFF."

%description -l tr devel
tiff resimlerini iþleyen programlar yazmak için gerekli dosyalar bu pakette
yer alýr.

%description -l tr
Bu paket TIFF resimlerini iþleyen fonksiyonlardan oluþan bir kitaplýktýr.

%prep
%setup -n tiff-v3.4
%patch0 -p1
%patch1 -p1

%build
./configure --target=linux << EOF
no
$RPM_BUILD_ROOT/usr/bin
$RPM_BUILD_ROOT/usr/lib
$RPM_BUILD_ROOT/usr/include
$RPM_BUILD_ROOT/usr/man
bsd-source-cat
yes
EOF
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/include $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/man/man1
make install
cd libtiff
install -m644 -o root -g root libtiff.so.3.4 $RPM_BUILD_ROOT/usr/lib

ln -sf libtiff.so.%{LIBVER} $RPM_BUILD_ROOT/usr/lib/libtiff.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/libtiff.so.%{LIBVER}
/usr/bin/fax2tiff
/usr/bin/fax2ps
/usr/bin/gif2tiff
/usr/bin/pal2rgb
/usr/bin/ppm2tiff
/usr/bin/rgb2ycbcr
/usr/bin/thumbnail
/usr/bin/ras2tiff
/usr/bin/tiff2bw
/usr/bin/tiff2ps
/usr/bin/tiffcmp
/usr/bin/tiffcp
/usr/bin/tiffdither
/usr/bin/tiffdump
/usr/bin/tiffinfo
/usr/bin/tiffmedian
/usr/bin/tiffsplit

%files devel
%doc COPYRIGHT README TODO VERSION html/*
/usr/lib/libtiff.so
/usr/lib/libtiff.a
/usr/include/tiff.h
/usr/include/tiffio.h
/usr/man/man1/*
/usr/man/man3/*
