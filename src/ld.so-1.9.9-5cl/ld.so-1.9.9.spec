Summary: Shared library configuration tool and old dynamic loader
Summary(pt_BR): Carregador dinâmico Linux
Summary(es): Cargador dinámico Linux
Name: ld.so
Version: 1.9.9
Release: 5cl
Copyright: BSD
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: sunsite.unc.edu:/pub/Linux/GCC/ld.so-1.9.9.tar.gz
Source700: ld.so-man-pt_BR.tar
BuildRoot: /var/tmp/ld.so-root
Prereq: filesystem
ExclusiveArch: sparc i386

%description
This package contains the shared library configuration tool, ldconfig, which
is required by many packages. It also includes the shared library loader
and dynamic loader for Linux libc 5.

%description -l pt_BR
Este pacote contém o carregador dinâmico para bibliotecas
compartilhadas. É requerido para todos os pacotes linkados
dinamicamente.

%description -l es
Este paquete contiene el cargador dinámico para bibliotecas
compartidas.  Se requiere para todos los paquetes linkados
dinámicamente.

%changelog
* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 17 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Fri Jun 26 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Added pt_BR translations
- updated to 1.9.9

* Mon Nov 17 1997 Erik Troan <ewt@redhat.com>
- Rather then searching the rpath first, search it after LD_LIBRARY_PATH
  and after the cache. While this breaks the ABI <gulp> it works significantly
  better for real-world libc 5 X apps which specify /usr/X11R6/lib as their
  rpath.

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- removed ldconfig from archive
- don't build on alpha

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- build just ldconfig on alpha

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- updated to 1.9.5
- added /etc/ld.so to filelist

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built version for coexistence w/ GNU libc

%prep
%setup -q

%build
(cd d-link; make)

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man3
mkdir -p $RPM_BUILD_ROOT/usr/man/man8

PREFIX=$RPM_BUILD_ROOT sh instldso.sh --force

# we get ldd from GNU libc
rm -f $RPM_BUILD_ROOT/usr/bin/ldd $RPM_BUILD_ROOT/sbin/ldconfig
rm -f $RPM_BUILD_ROOT/usr/info/ld.so.info

# ideally, these would come from GNU libc, but this is the best we can do
install -m 644 man/dlopen.3 $RPM_BUILD_ROOT/usr/man/man3
ln -sf dlopen.3 $RPM_BUILD_ROOT/usr/man/man3/dlsym.3
ln -sf dlopen.3 $RPM_BUILD_ROOT/usr/man/man3/dlerror.3
ln -sf dlopen.3 $RPM_BUILD_ROOT/usr/man/man3/dlclose.3


cd -


mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/ld.so-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/lib/ld.so.1.9.9
/lib/ld.so
/lib/ld-linux.so.1.9.9
/lib/ld-linux.so.1
/lib/libdl.so.1.9.9
/usr/man/man1/ldd.1
/usr/man/man3/dlopen.3
/usr/man/man3/dlsym.3
/usr/man/man3/dlerror.3
/usr/man/man3/dlclose.3
/usr/man/man8/ldconfig.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*
