Summary: A GNU arbitrary precision library.
Summary(pt_BR): Biblioteca de precisão arbitrária da GNU
Summary(es): Biblioteca de precisión arbitraria de la GNU
Name: gmp
Version: 2.0.2
Release: 9cl
URL: http://www.gnu.org
Source: ftp://ftp.gnu.org/pub/gnu/gmp-2.0.2.tar.gz
Patch0: gmp-2.0.2-1.shared.patch
Copyright: GPL 
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
BuildRoot: /var/tmp/gmp-root

%description
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and
floating point numbers. GNU MP is designed for speed, for both
small and very large operands. GNU MP is fast for several reasons:
It uses fullwords as the basic arithmetic type, it uses fast
algorithms, it carefully optimizes assembly code for many CPUs'
most common inner loops and it generally emphasizes speed over
simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.

%description -l pt_BR
Esta é a biblioteca GNU de precisão arbitrária. Ela dá acesso a
funções para manipular arbitrariamente grandes números com interfaces
de alto ou baixo nível.

%description -l es
Esta es la biblioteca GNU de precisión arbitraria. Da acceso
a funciones para manipular arbitrariamente grandes números con
interfaces de alto o bajo nivel.

%package devel
Summary: Development tools for the GNU MP arbitrary precision library.
Summary(pt_BR): Arquivos de inclusão, bibliotecas estáticas e documentação da biblioteca gmp.
Summary(es): Archivos de inclusión, bibliotecas estáticas y documentación de la biblioteca gmp.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
PreReq: info

%description devel
The static libraries, header files and documentation for using the GNU
MP arbitrary precision library in applications.  

If you want to develop applications which will use the GNU MP library,
you'll need to install the gmp-devel package.  You'll also need to
install the gmp package.

%description -l pt_BR devel
Estas são as bibliotecas estáticas, arquivos de inclusão e
documentação para usar a biblioteca GNU de precisão arbitrária em
seus programas.

%description -l es devel
Estas son las bibliotecas estáticas, archivos de inclusión y
documentación para usar la biblioteca GNU de precisión arbitraria
en tus programas.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)

* Thu Feb 11 1999 Michael Johnson <johnsonm@redhat.com>
- include the private header file gmp-mparam.h because several
  apps seem to assume that they are building against the gmp
  source tree and require it.  Sigh.

* Tue Jan 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- libtoolize to work on arm

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- yet another touch of the spec file

* Wed Sep  2 1998 Michael Fulbright <msf@redhat.com>
- looked over before inclusion in RH 5.2

* Sat May 24 1998 Dick Porter <dick@cymru.net>
- Patch Makefile.in, not Makefile
- Don't specify i586, let configure decide the arch

* Sat Jan 24 1998 Marc Ewing <marc@redhat.com>
- started with package from Toshio Kuratomi <toshiok@cats.ucsc.edu>
- cleaned up file list
- fixed up install-info support

%prep
%setup
%patch0 -p1
%build
libtoolize --copy --force
./configure --prefix=/usr
make CFLAGS="${RPM_OPT_FLAGS}"

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/usr/lib ${RPM_BUILD_ROOT}/usr/info \
         ${RPM_BUILD_ROOT}/usr/include

make CFLAGS="${RPM_OPT_FLAGS}" prefix=${RPM_BUILD_ROOT}/usr install
gzip -9nf ${RPM_BUILD_ROOT}/usr/info/gmp.info*
install -m 644 -o root -g root mpn/gmp-mparam.h ${RPM_BUILD_ROOT}/usr/include/

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post devel
/sbin/install-info /usr/info/gmp.info.gz /usr/info/dir

%preun devel
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/gmp.info.gz /usr/info/dir
fi

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/libgmp.so.2.0.2

%files devel
%doc SPEED NEWS README
/usr/lib/libgmp.so
/usr/lib/libgmp.a
/usr/include/gmp.h
/usr/include/gmp-mparam.h
/usr/info/gmp.info*
