Summary: A GNU implementation of Scheme for application extensibility.
Summary(pt_BR): Linguagem de extensão da GNU
Summary(es): Lenguaje de extensión de la GNU
Name: guile
Version: 1.3
Release: 4cl
# was .gz
Source: ftp://ftp.gnu.org/pub/gnu/guile-%{PACKAGE_VERSION}.tar.bz2
Patch0: guile-1.3-scm.patch
Patch1: guile-1.3-ansi.patch
Copyright: GPL
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Buildroot: /var/tmp/%{name}-root
Prereq: info
Requires: umb-scheme

%description
GUILE (GNU's Ubiquitous Intelligent Language for Extension) is a library
implementation of the Scheme programming language, written in C.  GUILE
provides a machine-independent execution platform that can be linked in
as a library during the building of extensible programs.

Install the guile package if you'd like to add extensibility to programs
that you are developing.  You'll also need to install the guile-devel
package.

%description -l pt_BR
Guile é um implementação de Scheme portável e embutível escrita em
C. Guile provê uma máquina de execução independente de plataforma,
que pode ser linkada como uma biblioteca construindo programas
extensíveis.

%description -l es
Guile es una implementación de Scheme, que puede ser portátil y
empotrada, escrita en C. Guile provee una máquina de ejecución
independiente de plataforma, que puede ser linkada como una
biblioteca construyendo programas extensibles.

%package devel
Summary: The libraries and header files for the GUILE extensibility library.
Summary(pt_BR): Bibliotecas da Guile, arquivos de inclusão, etc.
Summary(es): Bibliotecas de Guile, archivos de inclusión, etc.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: guile

%description devel
The guile-devel package includes the libraries, header files, etc., that
you'll need to develop applications that are linked with the GUILE
extensibility library.

You need to install the guile-devel package if you want to develop
applications that will be linked to GUILE.  You'll also need to install
the guile package.

%description -l pt_BR devel
Este pacote contém o que é necessário para desenvolver aplicações
usando a Guile.

%description -l es devel
Este paquete contiene todo lo necesario para desarrollar aplicaciones
usando Guile.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .ansi

%build
libtoolize --force --copy
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --enable-dynamic-linking
make

%install
rm -rf $RPM_BUILD_ROOT

make install prefix=$RPM_BUILD_ROOT/usr/

pushd $RPM_BUILD_ROOT
strip ./usr/bin/guile
chmod +x ./usr/lib/libguile.so.*.0.0
gzip -9nf ./usr/info/data-rep*
mkdir -p ./usr/share/guile/site
ln -s ../../lib/umb-scheme/slib ./usr/share/guile/slib
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog GUILE-VERSION HACKING NEWS README TODO
%doc SNAPSHOTS ANON-CVS THANKS
/usr/bin/guile
/usr/lib/libguile.so.*.*
%dir /usr/share/guile
%dir /usr/share/guile/site
%dir /usr/share/guile/%{PACKAGE_VERSION}
/usr/share/guile/%{PACKAGE_VERSION}/ice-9
/usr/share/aclocal/*
/usr/share/guile/slib

%files devel
%defattr(-,root,root)
/usr/bin/guile-config
/usr/bin/guile-snarf
/usr/lib/lib*so
/usr/lib/lib*a
/usr/include/guile
/usr/include/libguile
/usr/include/libguile.h
/usr/info/data-rep*

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Removed %post and %postun for package devel

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 17 1999 Michael Johnson <johnsonm@redhat.com>
- added .ansi patch to fix #endif

* Wed Feb 10 1999 Cristian Gafton <gafton@redhat.com>
- add patch for the scm stuff

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- integrate changes from rhcn version (#640)

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- call libtoolize first to get it to compile on the arm

* Sat Jan  9 1999 Todd Larason <jtl@molehill.org>
- Added "Requires: guile" at suggestion of Manu Rouat <emmanuel.rouat@wanadoo.fr>

* Fri Jan  1 1999 Todd Larason <jtl@molehill.org>
- guile-devel does depend on guile
- remove devel dependancy on m4
- move guile-snarf from guile to guile-devel
- Converted to rhcn

* Wed Oct 21 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.3.
- don't strip libguile.so.*.0.0. (but set the execute bits).

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- spec file fixups

* Wed Sep  2 1998 Michael Fulbright <msf@redhat.com>
- Updated for RH 5.2

* Mon Jan 26 1998 Marc Ewing <marc@redhat.com>
- Started with spec from Tomasz Koczko <kloczek@idk.com.pl>
- added slib link

* Thu Sep 18 1997 Tomasz Koczko <kloczek@idk.com.pl>          (1.2-3)
- added %attr(-, root, root) for %doc, 
- in %post, %postun ldconfig runed as parameter "-p",
- removed /bin/sh from requires,
- added %description,
- changes in %files.

* Fri Jul 11 1997 Tomasz Koczko <kloczek@rudy.mif.pg.gda.pl>  (1.2-2)
- all rewrited for using Buildroot,
- added %postun,
- removed making buid logs,
- removed "--inclededir", added "--enable-dynamic-linking" to configure
  parameters,
- added striping shared libs and /usr/bin/guile,
- added "Requires: /bin/sh" (for guile-snarf) in guile package and
  "Requires: m4" for guile-devel,
- added macro %{PACKAGE_VERSION} in "Source:" and %files,
- added %attr macros in %files.
