Summary: A GNU collection of binary utilities.
Summary(pt_BR): Utilitários para desenvolvimento de binários da GNU
Summary(es): Utilitarios para desarrollo de binarios de la GNU
Name: binutils
Version: 2.9.1.0.23
Release: 5cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://ftp.varesearch.com/pub/support/hjl/binutils/binutils-%{version}.tar.gz
Patch1: binutils-2.9.1.0.19a-arm-diff-981230.gz
Patch2: binutils-2.9.1.0.22b-xref.patch
Patch3: binutils-2.9.1.0.23-2.9.1.0.24-nosparc.diff.gz
Patch4: alpha-relax-patch.gz
Buildroot: /var/tmp/binutils-root

%description
Binutils is a collection of binary utilities, including ar (for creating,
modifying and extracting from archives), nm (for listing symbols from
object files), objcopy (for copying and translating object files),
objdump (for displaying information from object files), ranlib (for
generating an index for the contents of an archive), size (for listing
the section sizes of an object or archive file), strings (for listing
printable strings from files), strip (for discarding symbols), c++filt
(a filter for demangling encoded C++ symbols), addr2line (for converting
addresses to file and line), and nbnconv (for converting object code into
an NLM). 

Install binutils if you need to perform any of these types of actions on
binary files.  Most programmers will want to install binutils.

%description -l pt_BR
binutils é uma coletânea de utilitários necessários para compilar
programas. Inclui assembler e linker, assim como vários outros
programas para trabalhar com formatos executáveis.

%description -l es
binutils es una colectánea de utilitarios necesarios para compilar
programas. Incluye assembler y linker, así como varios otros
programas para trabajar con formatos que se puedan ejecutar.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
ADDITIONAL_TARGETS=""
%ifarch sparc
ADDITIONAL_TARGETS="--enable-targets=sparc64-linux"
%endif
./configure --prefix=/usr --enable-shared $ADDITIONAL_TARGETS \
	$RPM_ARCH-conectiva-linux
make tooldir=/usr all info

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
make prefix=$RPM_BUILD_ROOT/usr tooldir=$RPM_BUILD_ROOT/usr/ install install-info
strip $RPM_BUILD_ROOT/usr/bin/*
gzip -q9f $RPM_BUILD_ROOT/usr/info/*.info*

#install -m 644 libiberty/libiberty.a $RPM_BUILD_ROOT/usr/lib
install -m 644 include/libiberty.h $RPM_BUILD_ROOT/usr/include

chmod +x $RPM_BUILD_ROOT/usr/lib/lib*.so*

# This one comes from egcs
rm -f $RPM_BUILD_ROOT/usr/bin/c++filt

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/install-info --info-dir=/usr/info /usr/info/as.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/bfd.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/binutils.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/gasp.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/gprof.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/ld.info.gz
/sbin/install-info --info-dir=/usr/info /usr/info/standards.info.gz

%preun
if [ $1 = 0 ] ;then
  /sbin/install-info --delete --info-dir=/usr/info /usr/info/as.info.gz
  /sbin/install-info --delete --info-dir=/usr/info /usr/info/bfd.info.gz
  /sbin/install-info --delete --info-dir=/usr/info /usr/info/binutils.info.gz
  /sbin/install-info --delete --info-dir=/usr/info /usr/info/gasp.info.gz
  /sbin/install-info --delete --info-dir=/usr/info /usr/info/gprof.info.gz
  /sbin/install-info --delete --info-dir=/usr/info /usr/info/ld.info.gz
  /sbin/install-info --delete --info-dir=/usr/info /usr/info/standards.info.gz
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README
/usr/bin/*
/usr/man/man1/*
/usr/include/*
/usr/lib/*
/usr/info/*info*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 19 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x and kernel 2.2.x

* Tue May 18 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- traduções para pt_BR incluídas para Summary, %description e Group

* Mon Apr 26 1999 Cristian Gafton <gafton@redhat.com>
- back out very *stupid* sparc patch done by HJLu. People, keep out of
  things you don't understand.
- add alpha relax patch from rth

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- version  2.9.1.0.23
- patch to make texinfo documentation compile
- auto rebuild in the new build environment (release 2)

* Tue Feb 23 1999 Cristian Gafton <gafton@redhat.com>
- updated to 2.9.1.0.21
- merged with UltraPenguin

* Mon Jan 04 1999 Cristian Gafton <gafton@redhat.com>
- added ARM patch from philb
- version 2.9.1.0.19a
- added a patch to allow arm* arch to be identified as an ARM

* Thu Oct 01 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.9.1.0.14.

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.13.

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.9.1.0.12

* Thu Jul  2 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.7.

* Wed Jun 03 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.6.

* Tue Jun 02 1998 Erik Troan <ewt@redhat.com>
- added patch from rth to get right offsets for sections in relocateable
  objects on sparc32

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- version 2.9.1.0.4 is out; even more, it is public !

* Tue May 05 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.3.

* Mon Apr 20 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.9.0.3

* Tue Apr 14 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.9.0.2

* Sun Apr 05 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.8.1.0.29 (HJ warned me that this thing is a moving target...
  :-)
- "fixed" the damn make install command so that all tools get installed

* Thu Apr 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded again to 2.8.1.0.28 (at least on alpha now egcs will compile)
- added info packages handling

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.8.1.0.23

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.8.1.0.15 (required to compile the newer glibc)
- all patches are obsoleted now

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added 2.8.1.0.1 patch from hj
- added patch for alpha palcode form rth
