Summary: A library for manipulating JPEG image format files.
Summary(pt_BR): Biblioteca para manipulação de diferentes arquivos jpegs.
Summary(es): Biblioteca para manipulación de diferentes archivos jpegs.
Name: libjpeg6a
Version: 6a
Release: 5cl
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6a.tar.gz
Buildroot: /var/tmp/libjpeg-root
ExcludeArch: armv4l
Patch: jpeg-shlib.patch
%define LIBVER 6.0.1

%description
This package is a library of functions that manipulate jpeg images, along
with simple clients for manipulating jpeg images.

This version of the package includes only a library that is needed for
preserving the backwards compatibility with previous releases of Red Hat
Linux.

%description -l pt_BR
Este pacote contém uma biblioteca de funções e programas simples
que manipulam imagens jpeg.

%description -l es
Este paquete contiene una biblioteca de funciones y programas
sencillos que manipulan imágenes jpeg.

%prep
%setup -n jpeg-6a
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=$RPM_BUILD_ROOT/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib #$RPM_BUILD_ROOT/usr/include $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/man/man1

install -m 755 -o 0 -g 0 libjpeg.so.%{LIBVER} $RPM_BUILD_ROOT/usr/lib

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/libjpeg.so.%{LIBVER}

%changelog
* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Feb 03 1999 Cristian Gafton <gafton@redhat.com>
- rebuild for glibc 2.1

* Tue Jun 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jun 04 1998 Marc Ewing <marc@redhat.com>
- renamed to libjpeg6a
- shared lib *only* package
- this package was made for use on RH 5.1 to support apps from 5.0

* Wed Oct 08 1997 Donnie Barnes <djb@redhat.com>
- new package to remove jpeg stuff from libgr and put in it's own package
