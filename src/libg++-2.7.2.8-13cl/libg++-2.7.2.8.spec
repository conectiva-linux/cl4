Summary: GNU g++ library
Summary(pt_BR): Biblioteca g++ GNU
Summary(es): Biblioteca g++ GNU
Name: libg++
Version: 2.7.2.8
Release: 13cl
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: ftp://prep.ai.mit.edu/pub/gnu/libg++-2.7.2.tar.gz
Source1: libg++-2.7.2-binaries.tar.gz
Patch0: ftp://tsx-11.mit.edu/pub/linux/packages/GCC/libg++-2.7.2-2.7.2.7.diff.gz
Patch1: ftp://tsx-11.mit.edu/pub/linux/packages/GCC/libg++-2.7.2.7-2.7.2.8.diff.gz
Patch2: libg++-2.7.2-strcpsn.patch
Buildroot: /var/tmp/libgpp-root
Exclusivearch: i386
Summary(de):  GNU g++-Library 
Summary(fr): Bibiothèque g++ GNU.
Summary(tr): GNU g++ kitaplýðý

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Mon Apr 20 1998 Cristian Gafton <gafton@redhat.com>
- ExclusiveArch: i386
- added the precompile binaries for i386. egcs C++ compiler can not compile
  this anymore, and this package is a compatibility package anyway, so...

* Wed Apr 15 1998 Cristian Gafton <gafton@redhat.com>
- build only the runtime package. For C++ development one should use the
  libstdc++ that comes with egcs instead.
- added a buildroot

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- hacked to build w/ -fPIC 
- fixed info file inclusion

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

%description
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools.
This package includes the shared libraries necessary to run C++
applications.

%description -l pt_BR
Esta é a implementação GNU das bibliotecas-padrão C++, acompanhada
de ferramentas GNU adicionais. Este pacote inclui as bibliotecas
compartilhadas necessárias para rodar aplicações C++.

%description -l es
Esta es el soporte GNU de las bibliotecas padrón C++, acompañada de
herramientas GNU adicionales. Este paquete incluye las bibliotecas
compartidas necesarias para que se ejecuten aplicaciones C++.

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
tar xzvf $RPM_SOURCE_DIR/libg++-2.7.2-binaries.tar.gz -C $RPM_BUILD_ROOT
#make install install-info prefix=$RPM_BUILD_ROOT/usr
#gzip -9fn $RPM_BUILD_ROOT/usr/info/*info*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/lib/libstdc++.so.2.7.2.8
/usr/lib/libg++.so.2.7.2.8
