# Note that this is NOT a relocatable package
%define ver      1.2.3
%define rel      1cl
%define prefix   /usr

Summary: Handy library of utility functions
Summary(pt_BR): Conjunto de funções gráficas utilitárias
Summary(es): Conjunto de funciones gráficas utilitarias
Name: glib
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
# was .gz
Source: ftp://ftp.gimp.org/pub/gtk/v1.2/glib-%{ver}.tar.bz2
BuildRoot: /var/tmp/glib-%{PACKAGE_VERSION}-root
URL: http://www.gtk.org/
Docdir: %{prefix}/doc
Serial: 1

%description
Handy library of utility functions. Development libs and headers
are in glib-devel.

%description -l pt_BR
Conjunto de funções utilitárias. Bibliotecas de desenvolvimento e
arquivos de inclusão estão em glib-devel.

%description -l es
Conjunto de funciones utilitarias. Bibliotecas de desarrollo y
archivos de inclusión están en glib-devel.

%package devel
Summary: GIMP Toolkit and GIMP Drawing Kit support library
Summary(pt_BR): Conjunto de ferramentas e biblioteca do kit de desenho do GIMP
Summary(es): Conjunto de funciones gráficas utilitarias para desarrollo
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
Static libraries and header files for the support library for the GIMP's X
libraries, which are available as public libraries.  GLIB includes generally
useful data structures.

%description -l pt_BR devel
Bibliotecas estáticas e arquivos de inclusão para a biblioteca de suporte para
as bibliotecas X do GIMP, que são disponíveis como bibliotecas públicas. A GLIB
inclui estruturas de dados genéricas úteis.

%description -l es devel
Conjunto de funciones gráficas utilitarias para desarrollo

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated to version 1.2.3

* Fri Mar 26 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Serial = 1 ...

* Thu Mar 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated package to version 1.2.1

* Fri Mar 05 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Adapted from old gtk+ 1.0.6 spec file

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS
%ifarch alpha
./configure --prefix=%prefix --host=alpha-conectiva-linux
%else
./configure --prefix=%prefix
%endif

make

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/lib/libglib-1.2.so.*
%{prefix}/lib/libgthread-1.2.so.*
%{prefix}/lib/libgmodule-1.2.so.*

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/lib/glib
%{prefix}/include/*
%{prefix}/man/man1/
%{prefix}/share/aclocal/*
%{prefix}/bin/*
