Summary: GNU libc for Red Hat Linux 5.2 backwards compatibility
Summary(pt_BR): Libc 6.0 para o compatibilidade com sistemas Conectiva Linux 3.0
Summary(es): GNU libc for Red Hat Linux 5.2 backwards compatibility
Name: compat-glibc
Version: 3.0
%define kheaders 2.1.76
%define version 990211
Release: 2.0.7.1cl
Copyright: LGPL
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Source0: glibc-2.0.7-%{version}.tar.gz
Source1: ftp://prep.ai.mit.edu/pub/gnu/glibc-localedata-2.0.7pre3.tar.gz
Source2: ftp://alpha.gnu.org/gnu/glibc-linuxthreads-2.0.7-19981118.tar.gz
Source3: ftp://prep.ai.mit.edu/pub/gnu/glibc-crypt-2.0.6.tar.gz 
Source4: glibc-2.0.7-nsswitch.conf
Source5: linux-include-%{kheaders}.tar.gz
Source6: glibc-2.0.7-db-mans.tar.gz
Patch0: glibc-2.0.7-preload.patch
Patch1: glibc-2.0.7-nonmt.patch
Patch2: glibc-2.0.7-localedata.patch
Patch3: glibc-2.0.7-misc.patch
Patch4: glibc-2.0.7-sparc.patch
Patch5: glibc-2.0.7-sparc2.patch
Patch6: glibc-2.0.7-sparc3.patch
Patch7: glibc-2.0.7-tz.patch

Patch9: glibc-2.0.7-sparc4.patch
Patch11: glibc-2.0.7-pagesize.patch
Patch12: glibc-2.0.7-getpagesize.patch

Patch14: glibc-2.0.7-slovak.patch
Patch15: glibc-2.0.7-serbian.patch
Patch17: glibc-2.0.7-shaper.patch
Patch18: glibc-2.0.7-sparclongjmp2.patch
Patch19: glibc-2.0.7-dlopen.patch
Patch100: glibc-2.0.7-kfd.patch

Buildroot: /var/tmp/glibc-%{PACKAGE_VERSION}-root
Autoreq: false
Autoprov: false

%description
This package contains the version 2.0.7 of the GNU C library for compiling
binaries that will run on Red Hat Linux 2.0 and other glibc 2.0.x Linux
based systems. This package includes the runtime libraries.

%description -l pt_BR
Este pacote contém a versão 2.0.7 da GNU glibc para compilar programas que
rodarão no Conectiva Linux 3.0 e em outros sistemas Linux baseados na libc
6.0. Este pacote inclui as bibliotecas dinâmicas.

%description -l es
This package contains the version 2.0.7 of the GNU C library for compiling
binaries that will run on Red Hat Linux 2.0 and other glibc 2.0.x Linux
based systems. This package includes the runtime libraries.

%prep
%setup -q -a 1 -a 2 -a 3 -a 5 -a 6 -n glibc-2.0.7
%patch0 -p1
%patch2 -p1
%patch3 -p1
%ifarch sparc
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch9 -p1
%patch12 -p1
%patch18 -p1
%endif
%patch7 -p1
%patch11 -p1
%patch14 -p1
%patch15 -p1
%patch17 -p1
%patch19 -p1

# this is the 3000 file descriptors patch...
#patch100 -p1 -b .kfd

ln -s asm-${RPM_ARCH} linux/include/asm
ln -s ../../../../linux/include/linux sysdeps/unix/sysv/linux/linux
ln -s ../../../../linux/include/asm sysdeps/unix/sysv/linux/asm

find . -type f -size 0 -exec rm -f {} \;

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS -DNDEBUG=1" ./configure \
	--enable-add-ons=yes --with-profile=no \
	--prefix=/usr/$RPM_ARCH-glibc20-linux
make -r

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install_root=$RPM_BUILD_ROOT install

# remove stuff that we have no use for
rm -rf $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/{bin,etc,info,sbin,share}
rm -f $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/lib/lib*_p.a
for lib in  $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/lib/lib*.a ; do 
    [ -f ${lib%%.a}.so ] && rm -f $lib
done

# we know we want to use *this* one
cat > $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/lib/libc.so << EOF
/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
GROUP ( 
   /usr/i386-glibc20-linux/lib/libc.so.6 
   /usr/i386-glibc20-linux/lib/ld-linux.so.2 
   /usr/i386-glibc20-linux/lib/libc_nonshared.a 
      )
EOF

# Just drop in the kernel include headers...
cd linux/include
tar chf - asm linux | tar xf - -C $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/include
cd ../..

find $RPM_BUILD_ROOT -type f -or -type l | 
	sed 's|.*/etc|%config &|' > rpm.filelist.in
find ${RPM_BUILD_ROOT}/usr/$RPM_ARCH-glibc20-linux/include -type d | \
	sed "s/^/%dir /" >> rpm.filelist.in

sed "s|$RPM_BUILD_ROOT||" < rpm.filelist.in | sort > rpm.filelist

%clean
rm -rf $RPM_BUILD_ROOT
rm -f *.filelist*

%files -f rpm.filelist
%defattr(-,root,root)

%changelog
* Wed Jun 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Apr 17 1999 Cristian Gafton <gafton@redhat.com>
- crafted first version from the original Red Hat Linux 5.2 spec file
