Summary: A library for manipulating GIF format image files.
Summary(pt_BR): Biblioteca de manipulação de arquivos GIF
Summary(es): Biblioteca de manipulación de archivos GIF
Name: libungif
Version: 4.1.0
Release: 5cl
Copyright: X Consortium-like
URL:	http://prtr-13.ucsc.edu/~badger/software/libungif.shtml
# was .gz
Source0: ftp://prtr-13.ucsc.edu/pub/libungif/%{name}-%{version}.tar.bz2
# was .gz
Source1: ftp://prtr-13.ucsc.edu/pub/libungif/%{name}-3.1.0.tar.bz2
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
BuildRoot: /var/tmp/libungif-root
# The following libgif.so handles packages built against the
# previous broken giflib package
Provides: libgif.so.3 libgif.so giflib
Obsoletes: giflib
Prefix: /usr

%description
The libungif package contains a shared library of functions for loading
and saving GIF format image files.  The libungif library can load any
GIF file, but it will save GIFs only in uncompressed format (i.e., it
won't use the patented LZW compression used to save "normal" compressed
GIF files).

Install the libungif package if you need to manipulate GIF files.  You
should also install the libungif-progs package.

%description -l pt_BR
Biblioteca compartilhada para carga e gravação de arquivos GIF. A
gravação não usa um algoritmo que não usa a compressão LZW.

%description -l es
Es una biblioteca compartida para carga y grabación de archivos
GIF. La grabación no usa un algoritmo que no usa la compresión LZW.

%package devel
Summary: Development tools for programs which will use the libungif library.
Summary(pt_BR): Arquivos de inclusão, bibliotecas estáticas e documentação para biblioteca de manipulação de GIF
Summary(es): Archivos de inclusión, bibliotecas estáticas y documentación para biblioteca de manipulación de GIF
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
This package contains the static libraries, header files and documentation
necessary for development of programs that will use the libungif library
to load and save GIF format image files.

You should install this package if you need to develop programs which
will use the libungif library functions for loading and saving GIF format
image files.  You'll also need to install the libungif package.

%description -l pt_BR devel
Arquivos de inclusão, bibliotecas estáticas e documentação para
biblioteca de manipulação de GIF

%description -l es devel
Archivos de inclusión, bibliotecas estáticas y documentación para
biblioteca de manipulación de GIF

%package progs
Summary: Programs for manipulating GIF format image files.
Summary(pt_BR): Programas para converter e transfomar imagens gif.
Summary(es): Programas para convertir y transformar imágenes gif.
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia

%description progs
The libungif-progs package contains various programs for manipulating
GIF format image files.

Install this package if you need to manipulate GIF format image files.
You'll also need to install the libungif package.

%description -l pt_BR progs
Este pacote contem vários programas para manipuar arquivos de
imagens gif.

%description -l es progs
Este paquete contiene varios programas para manipular archivos de
imágenes gif.

%prep
%setup -q -a 1

%build
export CC=egcs
libtoolize --copy --force
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make all
cd %{name}-3.1.0
libtoolize --copy --force
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make all

%install
rm -rf ${RPM_BUILD_ROOT}
cd $RPM_BUILD_DIR/%{name}-%{version}/%{name}-3.1.0/lib
make DESTDIR="${RPM_BUILD_ROOT}" install-strip
{
  cd ${RPM_BUILD_ROOT}/usr/lib
  chmod +x libungif.so.3.1.0
  ln -sf libungif.so.3.1.0 ./libgif.so.3.1.0
  ln -sf libgif.so.3.1.0 ./libgif.so.3
  rm *.a
}

cd $RPM_BUILD_DIR/%{name}-%{version}
make DESTDIR="${RPM_BUILD_ROOT}" install-strip
{
  cd ${RPM_BUILD_ROOT}/usr/lib
  chmod +x libungif.so.%{version}
  ln -sf libungif.so.%{version} ./libgif.so.%{version}
  ln -sf libgif.so.%{version} ./libgif.so.4
  ln -sf libgif.so.4 ./libgif.so
  ln -sf libungif.a ./libgif.a
}

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%doc COPYING README UNCOMPRESSED_GIF NEWS ONEWS
/usr/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%doc doc/*
%doc util/giffiltr.c
%doc util/gifspnge.c
/usr/lib/lib*.a
/usr/lib/lib*.so
/usr/lib/lib*.la
/usr/include/*.h

%files progs
%defattr(-,root,root)
/usr/bin/*

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 29 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Sun Mar 14 1999 Preston Brown <pbrown@redhat.com>
- include libungif 4.1.0 as standard library, with 3.1.0 backwards compat.

* Mon Jan 11 1999 Cristian Gafton <gafton@redhat.com>
- build for 6.0
- call libtoolize to make sure it will build on the arm

* Sat Oct 31 1998 Jeff Johnson <jbj@redhat.com>
- package for RH 5.2.

* Mon Sep 14 1998 Arne Coucheron <arneco@online.no>
  [3.1.0-3]
- major cleanups and changes to the spec file

* Mon Sep 7 1998 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
- Upgrade to version 3.1.0 (which incorporates the patches in 3.0-4)
- Updated Source: and URL: to reflect change in directories/pages.

* Tue May 26 1998 Dick Porter <dick@cymru.net>
- Fixed some "warning: cast to pointer from integer of different size" on Alpha

* Tue May 5 1998 Marc Ewing <marc@redhat.com>
- Made it obsolete giflib and provide libgif.so and giflib (previous
  giflib packages were built incorrectly and packages built against
  it require libgif.so but work fine with this package)
- cleaned buildroot
- Removed Toshio as packager so he doesn't get yelled at when Red Hat
  breaks it :-)

* Fri Apr 24 1998 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
- Initial revision of libungif, a giflib derivative modified to not use LZW
  compression.
