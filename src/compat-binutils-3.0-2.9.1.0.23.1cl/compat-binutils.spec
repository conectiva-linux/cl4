Summary: A GNU collection of binary utilities.
Summary(pt_BR): Uma coleção de utilitários da GNU
Summary(es): A GNU collection of binary utilities.
Name: compat-binutils
Version: 3.0
%define BINver 2.9.1.0.23
Release: %{BINver}.1cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://ftp.varesearch.com/pub/support/hjl/binutils/binutils-%{BINver}.tar.gz
Patch0: binutils-2.9.1.0.16-arm.patch
Patch1: binutils-2.9.1.0.19a-arm-diff-981230.gz
Patch2: binutils-2.9.1.0.22b-xref.patch
Buildroot: /var/tmp/binutils-root
AutoProv: false
AutoReq: false

%description
This package includes the binutils required by the Conectiva Linux 3.0
backwards compatibility kit.  Binutils is a collection of binary utilities,
including ar (for creating, modifying and extracting from archives), nm (for
listing symbols from object files), objcopy (for copying and translating
object files), objdump (for displaying information from object files),
ranlib (for generating an index for the contents of an archive), size (for
listing the section sizes of an object or archive file), strings (for
listing printable strings from files), strip (for discarding symbols),
c++filt (a filter for demangling encoded C++ symbols), addr2line (for
converting addresses to file and line), and nbnconv (for converting object
code into an NLM). 

Install this package if you will be developing programs that need to run on
Conectiva Linux 3.0 or other glibc 2.0.x based systems.

%description -l pt_BR
Este pacote inclui os binutils requeridos pelo kit de compatibilidade
do Conectiva Linux 3.0.

Instale este pacote se você deseja desenvolver programas que necessitam
rodar em sistemas Conectiva Linux 3.0, ou em outras máquinas que contenham
sistemas baseados na glibc 2.0.

%description -l es
This package includes the binutils required by the Conectiva Linux 3.0
backwards compatibility kit.  Binutils is a collection of binary utilities,
including ar (for creating, modifying and extracting from archives), nm (for
listing symbols from object files), objcopy (for copying and translating
object files), objdump (for displaying information from object files),
ranlib (for generating an index for the contents of an archive), size (for
listing the section sizes of an object or archive file), strings (for
listing printable strings from files), strip (for discarding symbols),
c++filt (a filter for demangling encoded C++ symbols), addr2line (for
converting addresses to file and line), and nbnconv (for converting object
code into an NLM). 

Install this package if you will be developing programs that need to run on
Conectiva Linux 3.0 or other glibc 2.0.x based systems.

%prep 
%setup -q -n binutils-%{BINver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
ADDITIONAL_TARGETS=""
%ifarch sparc
ADDITIONAL_TARGETS="--enable-targets=sparc64-linux"
%endif
./configure \
	--prefix=/usr/$RPM_ARCH-glibc20-linux \
	--enable-shared $ADDITIONAL_TARGETS \
	$RPM_ARCH-glibc20-linux
make all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
make prefix=$RPM_BUILD_ROOT/usr install
for bin in  $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/bin/* ; do
    strip $bin
    mv $bin $bin.real
    ln -s wrapper $bin
done
cat > $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/bin/wrapper <<EOF
#!/bin/bash
LibDirectory=/usr/i386-glibc20-linux/lib
if [ -x \$0.real ] ; then
    export LD_LIBRARY_PATH=/usr/i386-glibc20/lib
    exec \$LibDirectory/ld-linux.so.2 \$0.real \$*
else
    echo "Program \$0.real missing" >&2
    exit -1
fi
EOF
chmod 755 $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/bin/wrapper

# This one comes from egcs
rm -f $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/bin/c++filt
rm -f $RPM_BUILD_ROOT/usr/lib/libiberty.a

# Fix more things
mv $RPM_BUILD_ROOT/usr/lib/lib* $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/lib
chmod +x $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/lib/lib*.so*
mv $RPM_BUILD_ROOT/usr/include $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux
install -m 644 include/libiberty.h $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/*-glibc20-linux/bin/*
/usr/*-glibc20-linux/include/*
/usr/*-glibc20-linux/lib/*

%changelog
* Wed Jun 23 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux

* Sat Apr 17 1999 Cristian Gafton <gafton@redhat.com>
- made original spec file out a recent real-life package
