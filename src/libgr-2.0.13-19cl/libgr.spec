Summary: A library for handling different graphics file formats.
Summary(pt_BR): Biblioteca para manipulação de diferentes arquivos gráficos.
Summary(es): Biblioteca para manipulación de diferentes archivos gráficos.
Name: libgr
Version: 2.0.13
Release: 19cl
Copyright: freeware
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: ftp://ftp.ctd.comsat.com/pub/linux/ELF/libgr-2.0.13.tar.gz
Source1: jpeg-to-pnm.fpi
Source2: pnm-to-ps.fpi 
Source3: libgr-scripts.tar.gz
Patch0: libgr-config.patch
Patch1: libgr-2.0.13-incl.patch
Patch2: libgr-2.0.13-glibc.patch
Patch3: libgr-2.0.13-pktopbm.patch
Patch4: libgr-2.0.13-glibc21.patch
Patch5: libgr-2.0.13-bmp.no24.patch
Patch6: libgr-2.0.13-bmptoppm.no24.patch
Buildroot: /var/tmp/libgr-root

%description
The libgr package contains a library of functions which support programs
for handling various graphics file formats, including .pbm (portable
pitmaps), .pgm (portable graymaps), .pnm (portable anymaps), .ppm
(portable pixmaps) and others.

%description -l pt_BR
Este pacote é uma biblioteca para manipulação de vários formatos
de arquivos gráficos, incluindo FBM, JPEG, PBM, PGM, PNM, PPM,
REL e TIFF.

%description -l es
Este paquete es una biblioteca para el manejo de varios formatos
de archivos gráficos, que incluye FBM, JPEG, PBM, PGM, PNM, PPM,
REL y TIFF.

%package devel
Summary: Development tools for programs which will use the libgr library.
Summary(pt_BR): Arquivos de inclusão e bibliotecas estáticas para desenvolvimento utilizando libgr
Summary(es): Archivos de inclusión y bibliotecas estáticas para desarrollo utilizando libgr
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: libgr

%description devel
The libgr-devel package contains the header files and static libraries,
etc., for developing programs which can handle the various graphics file
formats supported by the libgr library.

Install libgr-devel if you want to develop programs for handling the
graphics file formats supported by the libgr library.  You'll also need
to have the libgr package installed.

%description -l pt_BR devel
Este pacote é tudo que você precisa para desenvolver programas que
manipulam vários formatos de arquivos gráficos suportados pela libgr.

%description -l es devel
Este paquete es todo lo que necesitas para desarrollar programas que
manipulan varios formatos de archivos gráficos soportados por libgr.

%package progs
Summary: Tools for manipulating graphics files in libgr supported formats.
Summary(pt_BR): Programas utilitários libgr
Summary(es): Programas utilitarios libgr
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Obsoletes: netpbm

%description progs
The libgr-progs package contains a group of scripts for manipulating the
graphics files in formats which are supported by the libgr library.  For
example, libgr-progs includes the rasttopnm script, which will convert a
Sun rasterfile into a portable anymap.  Libgr-progs contains many other
scripts for converting from one graphics file format to another.

If you need to use these conversion scripts, you should install
libgr-progs.  You'll also need to install the libgr package.

%description -l pt_BR progs
Este pacote inclui vários utilitários para manipulação de arquivos
JPEG para uso pelos programas que usam a libgr.

%description -l es progs
Este paquete incluye varios utilitarios para el manejo de archivos
JPEG para ser usado por los programas que usan la libgr.

%prep
%setup -q
%patch0 -p1
tar xvfz $RPM_SOURCE_DIR/libgr-scripts.tar.gz
%patch1 -p1 -b .incl
%patch2 -p1 -b .glibc
%patch3 -p1 -b .pktopbm
%patch4 -p1 -b .glibc21
%patch5 -p1 -b .bmp
%patch6 -p1 -b .bmptoppm

# only necessary if you build tiff and jpeg support (we don't)
# (cd tiff; ln -s ../jpeg/ .)

%build
SHARED=shared
make SHARED=$SHARED everything
make -f Makefile.tiff -C pnm progs
# old png/png.h disagrees with /usr/include/png.h
rm png/png.h
make -C png progs

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib,include,bin}
make prefix=$RPM_BUILD_ROOT/usr install_everything
make -f Makefile.tiff -C pnm prefix=$RPM_BUILD_ROOT/usr install_p install_m
make -C png prefix=$RPM_BUILD_ROOT/usr install_p install_m

# (cd jpeg ; make SHARED=$SHARED install ; make install-headers )
# (cd tiff; install -m 644 -o 0 -g 0 tiff.h /usr/include)
# (cd tiff; install -m 644 -o 0 -g 0 tiffio.h /usr/include)
for i in $RPM_BUILD_ROOT/usr/bin/* ; do
    strip $i || :
done
unset i

cd libgr-scripts
./install.sh $RPM_BUILD_ROOT
cd -

# removed from this package; get from home site(s) or libjpeg/libtiff packages
# ln -sf libjpeg.so.6.0.1 $RPM_BUILD_ROOT/usr/lib/libjpeg.so
# ln -sf libtiff.so.3.4.28 $RPM_BUILD_ROOT/usr/lib/libtiff.so

ln -sf libfbm.so.1.0.0 $RPM_BUILD_ROOT/usr/lib/libfbm.so
ln -sf libpbm.so.1.0.0 $RPM_BUILD_ROOT/usr/lib/libpbm.so
ln -sf libpgm.so.1.0.0 $RPM_BUILD_ROOT/usr/lib/libpgm.so
ln -sf libpnm.so.1.0.0 $RPM_BUILD_ROOT/usr/lib/libpnm.so
ln -sf libppm.so.1.0.0 $RPM_BUILD_ROOT/usr/lib/libppm.so
ln -sf librle.so.1.0.0 $RPM_BUILD_ROOT/usr/lib/librle.so

mkdir -p $RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters
install -m755 $RPM_SOURCE_DIR/jpeg-to-pnm.fpi \
	$RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters
install -m755 $RPM_SOURCE_DIR/pnm-to-ps.fpi \
	$RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters
#/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/lib/lib*.so.*

%files devel
/usr/include/*.h
/usr/lib/lib*.a
/usr/lib/lib*.so
/usr/man/man3/*.3

%files progs
/usr/lib/rhs/rhs-printfilters/jpeg-to-pnm.fpi
/usr/lib/rhs/rhs-printfilters/pnm-to-ps.fpi
/usr/man/man1/*.1
/usr/bin/*

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 23 1999 Michael Johnson <johnsonm@redhat.com>
- removed old png.h header file that was causing png utils to die
- build png in build instead of install section...

* Mon Mar 22 1999 Bill Nottingham <notting@redhat.com>
- patch for 24-bit .BMP files (from sam@campbellsci.co.uk)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 15)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- clean up the spec file
- build for glibc 2.1
- patch to fix pktopbm

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- glibc2 defines random in <stdlib.h> (pbm/pbmplus.h problem #693)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- cleaned up the spec file a little bit
- validated mike's changes :-)

* Wed May 6 1998 Michael Maher <mike@redhat.com>
- added pnm-to-ps.fpi that was missing from previous packages

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- altered %install so that the package installs now even if a previous
  version was not installed on the system 

* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- built against libpng 1.0

* Thu Nov 06 1997 Donnie Barnes <djb@redhat.com>
- changed copyright from "distributable" to "freeware"
- added some missing scripts that existed in netpbm
- added some binaries that weren't getting built
- added patch to build tiff manipulation progs (requires libtiff)

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- obsoletes netpbm now

* Tue Oct 14 1997 Erik Troan <ewt@redhat.com>
- mucked config.guess and Make.Rules to build on Alpha/Linux

* Tue Oct 07 1997 Donnie Barnes <djb@redhat.com>
- updated to 2.0.13
- dropped libjpeg and libtiff (those should come from home sources)
- removed glibc patch (new version appears to have it!)
- added i686 as a valid arch type to config.guess

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
