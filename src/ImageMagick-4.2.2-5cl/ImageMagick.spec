Summary: An X application for displaying and manipulating images.
Summary(pt_BR): Exibidor, conversor e manipulador de imagens sob X
Summary(es): Exhibidor, convertidor y manipulador de imágenes bajo X
Name: ImageMagick
Version: 4.2.2
Release: 5cl
Copyright: freeware
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: ftp://ftp.wizards.dupont.com/pub/ImageMagick/ImageMagick-%{version}.tar.gz
Patch0: ImageMagick-4.1.0-libpath.patch
Patch1: ImageMagick-4.2-pgm.patch
Url: http://www.wizards.dupont.com/cristy/ImageMagick.html
Buildroot: /var/tmp/ImageMagick-root

%description
ImageMagick is a powerful image display, coversion and
manipulation tool. It runs in an X session. With this
tool, you can view, edit and display a variety of
image formats.

This package installs the necessary files to run ImageMagick.

%description -l pt_BR
ImageMagick é uma ferramenta para manipular, converter e exibir
imagens, que funciona sob o X Window. É uma ferramenta poderosa que
permite editar imagens, podendo tratar vários formatos diferentes.

%description -l es
ImageMagick es una herramienta para manipular, convertir y exhibir
imágenes, que funciona bajo X Window. Es una herramienta potente
que permite editar imágenes, pudiendo manipular varios formatos
diferentes.

%package devel
Summary: Static libraries and header files for ImageMagick app development.
Summary(pt_BR): Biblioteca estática e arquivos de inclusão para desenvolvimento com ImageMagick
Summary(es): Biblioteca estática y archivos de inclusión para desarrollo con ImageMagick
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: ImageMagick = %{PACKAGE_VERSION}

%description devel
If you want to create applications that will use ImageMagick code
or APIs, you'll need to install these packages as well as ImageMagick.
These additional packages aren't necessary if you simply want to
use ImageMagick, however.

ImageMagick-devel is an addition to ImageMagick which includes 
static libraries and header files necessary to develop 
applications. 

%description -l pt_BR devel
Este é o pacote de desenvolvimento ImageMagick. Inclui as bibliotecas
estáticas e os arquivos de inclusão para o desenvolvimento de suas
próprias aplicações que fazem uso do código ImageMagick e/ou APIs.

%description -l es devel
Este es el paquete de desarrollo ImageMagick. Incluye las bibliotecas
estáticas y los archivos de inclusión para el desarrollo de sus
propias aplicaciones que hacen uso del código ImageMagick y/el APIs.

%prep
%setup -q
%patch0 -p1 -b .libpath
%patch1 -p1 -b .pgm

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6 \
	--enable-shared \
	--with-perl --with-x $RPM_ARCH-conectiva-linux
make

%install
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make install \
	prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	PREFIX=$RPM_BUILD_ROOT/usr \
	libdir=$RPM_BUILD_ROOT/usr/X11R6/lib
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/include/X11
mv $RPM_BUILD_ROOT/usr/X11R6/include/magick $RPM_BUILD_ROOT/usr/X11R6/include/X11
# find the perl files
find $RPM_BUILD_ROOT/usr/lib/perl5 -type f -o -type l | \
	sed -e "s|$RPM_BUILD_ROOT||g" | \
	grep -v "perllocal.pod" > files-perl.list
strip $RPM_BUILD_ROOT/usr/X11R6/bin/* || :

%clean
rm -rf $RPM_BUILD_ROOT
rm -fv files-perl.list

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc www
%doc README.txt ImageMagick.html
%attr(755,root,root) /usr/X11R6/lib/*.so.*
/usr/X11R6/bin/*
/usr/X11R6/man/*/*
/usr/X11R6/share/*

%files devel -f files-perl.list
%defattr(-,root,root)
/usr/X11R6/lib/*.a
/usr/X11R6/lib/*.la
/usr/X11R6/include/X11/magick
/usr/X11R6/lib/*.so

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- include the perl man pages as well

* Tue Apr 06 1999 Michael K. Johnson <johnsonm@redhat.com>
- remove --enable-16bit because it damages interoperability

* Mon Apr  5 1999 Bill Nottingham <notting@redhat.com>
- update to 4.2.2
- change ChangeLog to refer to actual dates. 
- strip binaries

* Thu Apr  1 1999 Bill Nottingham <notting@redhat.com>
- add more files. Oops.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Wed Mar 10 1999 Bill Nottingham <notting@redhat.com>
- version 4.2.1

* Tue Jan 19 1999 Michael K. Johnson <johnsonm@redhat.com>
- changed group

* Tue Jan 19 1999 Cristian Gafton <gafton@redhat.com>
- hacks to make it work with the new perl
- version 4.1.0 (actually installs the sonames as 4.0.10... doh!)
- make sure the libraries have the x bit on

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.0.5

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.0.4
- added BuildRoot

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 3.8.3 to 3.9.1
- removed PNG patch (appears to be fixed)

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- build against new libpng

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
- updated to version 3.8.3.
- updated source and url tags.
