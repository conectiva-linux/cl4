Summary: A library of functions for manipulating PNG image format files.
Summary(pt_BR): Biblioteca PNG
Summary(es): Biblioteca PNG
Name: libpng
Version: 1.0.3
Release: 6cl
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://ftp.uu.net/graphics/png/src/libpng-1.0.3.tar.gz
Patch0: libpng-1.0.3-rhconf.patch
Buildroot: /var/tmp/libpng-root
%define LIBVER 2.1.0.3
Serial: 1

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG is
a bit-mapped graphics format similar to the GIF format.  PNG was created to
replace the GIF format, since GIF uses a patented data compression
algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.

%description -l pt_BR
Esta biblioteca é uma coleção de rotinas para criar e manipular
arquivos gráficos no formato PNG. Este formato foi projetado para
substituir o formato GIF, com extensões e melhorias.

%description -l es
Esta biblioteca es una colección de rutinas para crear y manipular
archivos gráficos en el formato PNG. Este formato fue proyectado
para substituir el formato GIF, con extensiones y mejorías.

%package devel
Summary: Development tools for programs to manipulate PNG image format files.
Summary(pt_BR): Arquivos de inclusão e bibliotecas estáticas
Summary(es): Archivos de inclusión y bibliotecas estáticas
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: libpng = %{PACKAGE_VERSION}
Serial: 1

%description devel
The libpng-devel package contains the header files and static libraries
necessary for developing programs using the PNG (Portable Network
Graphics) library.

If you want to develop programs which will manipulate PNG image format
files, you should install libpng-devel.  You'll also need to install the
libpng package.

%description -l pt_BR devel
Arquivos de inclusão e bibliotecas estáticas que são necessários
somente para o desenvolvimento de programas que usam a biblioteca
PNG.

%description -l es devel
Archivos de inclusión y bibliotecas estáticas que son necesarios
solamente para el desarrollo de programas que usan la biblioteca PNG.

%prep
%setup
ln -s scripts/makefile.lnx ./Makefile
%patch0 -p1 -b .rhconf

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
mkdir -p $RPM_BUILD_ROOT/usr/man/man{3,5}
install -m 644 *.3 $RPM_BUILD_ROOT/usr/man/man3
install -m 644 *.5 $RPM_BUILD_ROOT/usr/man/man5
gzip -9 $RPM_BUILD_ROOT/usr/man/man3/*.3
gzip -9 $RPM_BUILD_ROOT/usr/man/man5/*.5

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc *.txt example.c README TODO CHANGES
/usr/lib/libpng.so.%{LIBVER}
/usr/lib/libpng.so
/usr/man/man5/*

%files devel
%defattr(-,root,root)
/usr/include/*
/usr/lib/libpng.a
/usr/man/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- returning .so link

* Wed Jun 30 1999 Guilherme Manika <gwm@conectiva.com>
- Removed libpng.so from filelist to provide user with a cleaner,
  softer install experience (no ldconfig error messages, that is)
- Compressed manpages

* Mon Jun 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed a little bug in the file list, which made many packages
  require libpng-devel

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Sun Feb 07 1999 Michael Johnson <johnsonm@redhat.com>
- rev to 1.0.3

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Wed Sep 23 1998 Cristian Gafton <gafton@redhat.com>
- we are Serial: 1 now because we are reverting the 1.0.2 version from 5.2
  beta to this prior one
- install man pages; set defattr defaults

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel subpackage moved to Development/Libraries

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.0.1
- added buildroot

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- updated to new version
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
