# Note that this is NOT a relocatable package
%define ver      1.9.5
%define rel      2cl
%define prefix   /usr

Summary: An image loading and rendering library for X11R6.
Summary(pt_BR): Biblioteca de carga e renderização para X11R6
Summary(es): Biblioteca de carga y render 3D para X11R6
Name: imlib
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
# era .gz
Source: ftp://ftp.labs.redhat.com/pub/imlib/imlib-%{ver}.tar.bz2
Obsoletes: Imlib
BuildRoot: /var/tmp/imlib-%{PACKAGE_VERSION}-root

URL: http://www.labs.redhat.com/imlib/
Requires: libpng 
Requires: libtiff 
Requires: libjpeg
Requires: zlib 
Requires: libgr-progs 
Requires: gtk+ >= 1.2
Requires: libungif
Docdir: %{prefix}/doc

%description
Imlib is a display depth independent image loading and rendering library.
Imlib is designed to simplify and speed up the process of loading images
and obtaining X Window System drawables.  Imlib provides many simple
manipulation routines which can be used for common operations.  

Install imlib if you need an image loading and rendering library for X11R6.
You may also want to install the imlib-cfgeditor package, which will help
you configure Imlib.

%description -l pt_BR
A Imlib é uma biblioteca avançada que substitui as bibliotecas libXpm
que fornece muito mais opções/características com uma flexibilidade
e velocidade muito maiores.

%description -l es
Imlib es una biblioteca avanzada que sustituye las bibliotecas libXpm
que ofrece mucho más opciones/características con una flexibilidad
y velocidad mucho mayores.

%package devel
Summary: Development tools for Imlib applications.
Summary(pt_BR): Arquivos de inclusão, bibliotecas estáticas e documentação para a Imlib.
Summary(es): Archivos de inclusión, bibliotecas estáticas y documentación para Imlib.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: imlib = %{PACKAGE_VERSION}
Obsoletes: Imlib

%description devel
The header files, static libraries and documentation needed for
developing Imlib applications.  Imlib is an image loading and rendering
library for X11R6.

Install the imlib-devel package if you want to develop Imlib applications.
You'll also need to install the imlib and imlib_cfgeditor packages.

%description -l pt_BR devel
Arquivos de inclusão, bibliotecas estáticas e documentação para
a Imlib.

%description -l es devel
Archivos de inclusión, bibliotecas estáticas y documentación
para Imlib.

%package cfgeditor
Summary: A configuration editor for the Imlib library.
Summary(pt_BR): Editor da configuração da imlib
Summary(es): Editor de configuración de imlib
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Requires: imlib = %{PACKAGE_VERSION}

%description cfgeditor
The imlib-cfgeditor package contains the imlib_config program, which you
can use to configure the Imlib image loading and rendering library.
Imlib_config can be used to control how Imlib uses color and handles
gamma corrections, etc.

If you're installing the imlib package, you should also install
imlib_cfgeditor.

%description -l pt_BR cfgeditor
O programa imlib_config lhe permite controlar como a imlib usa
as cores e trata correção gamma, etc.

%description -l es cfgeditor
El programa imlib\_config te permite controlar como  imlib usa los
colores y manipula la corrección gamma, etc.

%prep
%setup -q

%build
export CFLAGS="${RPM_OPT_FLAGS}"
export CXXFLAGS="${RPM_OPT_FLAGS} -fno-rtti -fno-exceptions"
./configure --prefix=%prefix --sysconfdir=/etc
make

%install
make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%attr(755,root,root) %{prefix}/lib/lib*.so.*
/etc/*
%{prefix}/lib/libimlib-*.so

%files cfgeditor
%defattr(-,root,root)
%{prefix}/bin/imlib_config

%files devel
%defattr(-,root,root)
%doc doc/*.gif doc/*.html
%{prefix}/bin/imlib-config
%{prefix}/lib/libImlib.so
%{prefix}/lib/libgdk_imlib.so
%{prefix}/lib/*a
%{prefix}/include/*
%{prefix}/share/aclocal/*

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 29 1999 Guilherme Manika <gwm@conectiva.com>
- Para 1.9.5

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 05 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Remade package from and old version of spec file
