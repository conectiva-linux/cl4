%define LIBVER 62.0.0
Summary: Library for handling different jpeg files.
Summary(pt_BR): Biblioteca para manipulação de diferentes arquivos jpegs.
Summary(es): Biblioteca para manipulación de diferentes archivos jpegs.
Name: libjpeg
Version: 6b
Release: 12cl
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz
Buildroot: /var/tmp/libjpeg-root
Summary(de): Library zum Verarbeiten verschiedener jpeg-Dateien
Summary(fr): Bibliothèque pour gérer différents fichiers jpeg
Summary(tr): jpeg resimlerini iþleme kitaplýðý

%package devel
Summary: headers and static libraries for developing programs using libjpeg
Summary(pt_BR): Arquivos de inclusão e bibliotecas estáticas para desenvolver programas usando libjpeg 
Summary(es): Archivos de inclusión y bibliotecas estáticas para desarrollar programas usando libjpeg 
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: libjpeg
Summary(de): Header und statische Libraries zum Entwickeln von Programmen mit libjpeg
Summary(fr): Bibliothèques statiques et en-têtes pour développer avec libjpeg
Summary(tr): libjpeg için geliþtirme kitaplýklarý ve baþlýk dosyalarý

%description
This package is a library of functions that manipulate jpeg images, along
with simple clients for manipulating jpeg images.

%description -l pt_BR
Este pacote contém uma biblioteca de funções e programas simples
que manipulam imagens jpeg.

%description -l es
Este paquete contiene una biblioteca de funciones y programas
sencillos que manipulan imágenes jpeg.

%description devel
This package is all you need to develop programs that manipulate jpeg
images, including documentation.

%description -l pt_BR devel
Este pacote é tudo que você precisa para desenvolver programas que
manipulam imagens jpeg, incluindo documentação.

%description -l es devel
Este paquete es todo lo que necesitas para desarrollar programas
que manipulen imágenes jpeg, incluso  documentación.

%description -l de devel
Dieses Paket bietet alles, was Sie brauchen, um Programme zur Manipulation
von jpeg-Grafiken, einschließlich Dokumentation, zu entwickeln.

%description -l de
Dieses Paket ist eine Library mit Funktionen zur Manipulation von 
jpeg-Bildern, zusammen mit einfachen Clients zur Manipulation von jpeg-


%description -l fr devel
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images jpg, et comprend la documentation.

%description -l fr
Bibliothèque de fonctions qui manipulent des images jpeg, et clients simples
pour manipuler de telles images.

%description -l tr devel
Bu paket, jpeg resimlerini iþleyen programlar geliþtirmeniz için gereken
baþlýk dosyalarýný, kitaplýklarý ve ilgili yardým belgelerini içerir.

%description -l tr
Bu paket, jpeg þekillerini iþlemek için kitaplýklar ve basit istemciler içerir.

%prep
%setup -q -n jpeg-6b

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--enable-shared --enable-static
make
LD_LIBRARY_PATH=$PWD make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib,include,bin,man/man1}
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/* || :

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/libjpeg.so.%{LIBVER}
/usr/bin/*
/usr/man/*/*

%files devel
%defattr(-,root,root)
/usr/lib/*.a
/usr/lib/*.la
/usr/lib/*.so
/usr/include/*.h

%changelog
* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Nov 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Mon Aug  3 1998 Jeff Johnson <jbj@redhat.com>
- fix buildroot problem.

* Tue Jun 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Jun 04 1998 Marc Ewing <marc@redhat.com>
- up to release 4
- remove patch that set (improper) soname - libjpeg now does it itself

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- fixed build on manhattan

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 6b

* Wed Oct 08 1997 Donnie Barnes <djb@redhat.com>
- new package to remove jpeg stuff from libgr and put in it's own package
