Summary: The zlib compression and decompression library.
Summary(pt_BR): Biblioteca para compressão e descompressão
Summary(es): Biblioteca para compresión y descompresión
Name: zlib
Version: 1.1.3
Release: 6cl
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://ftp.uu.net/graphics/png/zlib-%{version}.tar.gz
PAtch0: zlib-1.1.3-glibc.patch
Url: http://www.cdrom.com/pub/infozip/zlib/
Copyright: BSD
Buildroot: /var/tmp/zlib-root

%description
The zlib compression library provides in-memory compression and
decompression functions, including integrity checks of the uncompressed
data.  This version of the library supports only one compression method
(deflation), but other algorithms may be added later, which will have
the same stream interface.  The zlib library is used by many different
system programs.

%description -l pt_BR
A biblioteca de compressão 'zlib' oferece funções de compressão
e descompressão em memória, incluindo checagem da integridade de
dados não comprimidos. Essa versão da biblioteca suporta somente um
método de compressão (deflação) mas outros algorítimos podem ser
adicionados mais tarde e terão a mesma interface. Essa biblioteca
é usada por vários programas de sistema.

%description -l es
La biblioteca de compresión 'zlib' nos ofrece funciones de compresión
y descompresión en memoria, incluyendo chequeo de la integridad
de datos no comprimidos. Esta versión de la biblioteca soporta
solamente un método de compresión (deflación) pero otros algoritmos
pueden ser añadidos más tarde y tendrán la misma interface. Esta
biblioteca se usa por varios programas de sistema.

%package devel
Summary: Header files and libraries for developing apps which will use zlib.
Summary(pt_BR): Bibliotecas e arquivos de inclusão para desenvolvimento zlib
Summary(es): Bibliotecas y archivos de inclusión para desarrollo zlib
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: zlib

%description devel
The zlib-devel package contains the header files and libraries needed
to develop programs that use the zlib compression and decompression
library.

Install the zlib-devel package if you want to develop applications that
will use the zlib library.

%description -l pt_BR devel
A biblioteca de compressão zlib provê funções de compressão e
descompressão em memória, incluindo checagens de integridade para
os dados descomprimidos.  Esta versão da biblioteca suporta somente
um método de compressão (deflation) mas outros algoritmos podem
ser adicionados no futuro e terão a mesma interface stream.

Este pacote contém os arquivos de inclusão e bibliotecas necessários
ao desenvolvimento de programas que usam zlib.

%description -l es devel
La biblioteca de compresión zlib provee funciones de compresión
y descompresión en memoria, incluye chequeos de integridad para
los datos descomprimidos.  Esta versión de la biblioteca soporta
solamente un método de compresión (deflation) pero otros algoritmos
pueden ser añadidos en el futuro y tendrán la misma interface stream.
Este paquete contiene los archivos de inclusión y bibliotecas
necesarios al desarrollo de programas que usan zlib.

%prep
%setup -q
%patch0 -p1 -b .glibc

%build
./configure --shared --prefix=/usr
make
# now build the static lib
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

./configure --shared --prefix=/usr
make install prefix=$RPM_BUILD_ROOT/usr

./configure --prefix=/usr
make install prefix=$RPM_BUILD_ROOT/usr

install -m644 zutil.h $RPM_BUILD_ROOT/usr/include/zutil.h
mkdir -p $RPM_BUILD_ROOT/usr/man/man3
install -m644 zlib.3 $RPM_BUILD_ROOT/usr/man/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/lib/libz.so.*

%files devel
%defattr(-,root,root)
%doc README ChangeLog algorithm.txt
/usr/lib/*.so
/usr/include/*
/usr/lib/*.a
/usr/man/man3/zlib.3

%changelog
* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- link against glibc

* Mon Jul 27 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 1.1.3

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.2
- buildroot

* Tue Oct 07 1997 Donnie Barnes <djb@redhat.com>
- added URL tag (down at the moment so it may not be correct)
- made zlib-devel require zlib

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
