%define version 3.0

Summary: Free OpenGL implementation. Runtime environment
Summary(pt_BR): Implementação free da OpenGL. Ambiente para execução
Summary(es): Implementación free de OpenGL. Ambiente para ejecución
Name: Mesa
Version: %{version}
Release: 5cl
Copyright: GPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
#Source0: ftp://iris.ssec.wisc.edu/pub/Mesa/MesaLib-%{version}.tar.gz
#Source1: ftp://iris.ssec.wisc.edu/pub/Mesa/MesaDemos-%{version}.tar.gz
# recompactados com bzip2
Source0: ftp://iris.ssec.wisc.edu/pub/Mesa/MesaLib-%{version}.tar.bz2
Source1: ftp://iris.ssec.wisc.edu/pub/Mesa/MesaDemos-%{version}.tar.bz2
Patch: Mesa-3.0-opt.patch
URL: http://www.ssec.wisc.edu/~brianp/Mesa.html
BuildRoot: /tmp/Mesa-%{version}-1-root
Prefix: /usr

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 18 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Dec 01 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com binários sem símbolos, usando strip

* Tue Dec 01 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Mesa-demos não mais gerado, muito grande... :(

* Wed Oct 21 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Wed Oct 21 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- atualização para 3.0

* Wed May  6 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>

- Correções nos tags Group (de Developments para Development)

* Thu Feb 12 1998 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- updated to final version 2.6

* Thu Feb 05 1998 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- Fixed thinko in misc patch
- build against glibc

* Sat Jan 31 1998 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- updated to version 2.6beta5
- added widget-mesa to the things to be build.

* Mon Jan 26 1998 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- updated to version 2.6beta4

* Sun Dec 14 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- updated to version 2.6beta1

* Sat Dec 13 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- Moved GLUT into a separate subpackage and added an Obsoletes tag to this
  subpackage
- Moved lib*.so to the devel package, they are only needed for development,
  not for a runtime environment.

* Sat Nov 29 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- added patches from ftp://iris.ssec.wisc.edu/pub/Mesa/patches_to_2.5
- BuildRoot'ed
- Prefix'ed
- added static versions of the libraries. (PPC version seems not to have
  support for shared versions of the library)
- moved static versions of the library and the includes to the new subpackage
  'devel'
- targets other than linux-x86 still untested.
- added Conflitcs tag
- added %postun
- added patch for RPM_OPT_FLAGS support

* Fri Nov 21 1997 Karsten Weiss <karsten@addx.au.s.shuttle.de>
- Upgraded to Mesa 2.5
- Multiarch destinations (untested).
- Included GLUT.
- Removed some of the READMEs for other platforms from the binary RPM.

%description
Mesa is a 3-D graphics library with an API which is very similar to that
of OpenGL*.  To the extent that Mesa utilizes the OpenGL command syntax
or state machine, it is being used with authorization from Silicon Graphics,
Inc.  However, the author makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with Silicon Graphics, Inc.
Those who want a licensed implementation of OpenGL should contact a licensed
vendor.  This software is distributed under the terms of the GNU Library
General Public License, see the LICENSE file for details.

* OpenGL(R) is a registered trademark of Silicon Graphics, Inc.

%description -l pt_BR
Mesa é uma biblioteca gráfica 3D com uma API muito similar à
da OpenGL*.  Até certo ponto Mesa usa a sintaxe de comandos e a
máquina de estados da própria OpenGL, com a autorização da Silicon
Graphics, Inc.  Entretanto, o autor não assume que Mesa seja uma
biblioteca que substitui a OpenGL ou seja associada com a Silicon
Graphics, Inc.  Aqueles que desejam uma implementação licenciada
da OpenGL devem contactar um vendedor licenciado. Este programa é
distribuído sob os termos da Licença Pública Geral para Bibliotecas
da GNU (LGPL). Veja o arquivo LICENSE para mais detalhes.

* OpenGL(R) é marca registrada da Silicon Graphics, Inc.

%description -l es
Mesa es una biblioteca gráfica 3D con una API muy similar a la
del OpenGL*. Hasta cierto punto Mesa usa la sintaxis de comandos y
la máquina de estados de la propia OpenGL, con la autorización de
la Silicon Graphics, Inc.  Entretanto, el autor no asume que Mesa
sea una biblioteca que substituye la OpenGL, o sea, asociada con la Silicon
Graphics, Inc.  Aquellos que deseen un soporte licenciado del
OpenGL deben contactar con un vendedor licenciado. Este programa
está distribuido bajo los términos de la Licencia Pública General
para Bibliotecas de la GNU (LGPL). Mira el archivo LICENSE para
más detalles.

* OpenGL(R) es marca registrada de la Silicon Graphics, Inc.

%package devel
Summary: Development environment for Mesa
Summary(pt_BR): Ambiente de desenvolvimento para Mesa
Summary(es): Ambiente de desarrollo para Mesa
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
The static version of the Mesa libraries and include files needed for
development.

%description -l pt_BR devel
Versão estática das bibliotecas Mesa e arquivos de inclusão
necessários para o desenvolvimento.

%description -l es devel
Versión estática de las bibliotecas Mesa y archivos de inclusión
necesarios para el desarrollo.

%package glut
Summary: GLUT library for Mesa
Summary(pt_BR): Biblioteca GLUT para Mesa
Summary(es): Biblioteca GLUT para Mesa
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Conflicts: glut

%description glut
The GLUT library.

%description -l pt_BR glut
A biblioteca GLUT - Mesa.

%description -l es glut
La biblioteca GLUT - Mesa.

%package glut-devel
Summary: GLUT Development environment for Mesa
Summary(pt_BR): Ambiente de desenvolvimento GLUT para Mesa
Summary(es): Ambiente de desarrollo GLUT para Mesa
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Conflicts: glut-devel

%description glut-devel
The static version of the GLUT library and include files needed for
development.

%description -l pt_BR glut-devel
Versão estática da biblioteca GLUT e arquivos de inclusão necessários
para o desenvolvimento.

%description -l es glut-devel
Versión estática de la biblioteca GLUT y archivos de inclusión
necesarios para el desarrollo.

%prep
%setup -q -n Mesa-3.0 -b 1
%patch -p1

%build
make linux-386
make clean
make linux-386-elf

(
cd widgets-mesa
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make 
)

%install
[ -n "$RPM_BUILD_ROOT" -a -n "`echo $RPM_BUILD_ROOT|sed -e 's#/##g'`" ] || exit 1
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib/Mesa-%{version},include,man/man3}

cp -dpr lib include $RPM_BUILD_ROOT/usr
#cp -dpr book demos xdemos samples util $RPM_BUILD_ROOT/usr/lib/Mesa-%{version}
cp -dpr util $RPM_BUILD_ROOT/usr/lib/Mesa-%{version}
cp Make-config $RPM_BUILD_ROOT/usr/lib/Mesa-%{version}

(
cd widgets-mesa
make prefix=$RPM_BUILD_ROOT/usr install
)

# acme@conectiva.com
# ter dez  1 11:03:01 EDT 1998
for a in libMesaGL.so.3.0 libMesaGLU.so.3.0 libglut.so.3.7 ; do
	strip $RPM_BUILD_ROOT/usr/lib/$a
done

%clean
[ -n "$RPM_BUILD_ROOT" -a -n "`echo $RPM_BUILD_ROOT|sed -e 's#/##g'`" ] || exit 1
rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%attr(-, root, root) %doc FUTURE IAFA-PACKAGE LICENSE README* RELNOTES VERSIONS
%attr(755, root, bin) /usr/lib/libMesa*.so.*

%files glut
%attr(755, root, bin) /usr/lib/libglut.so.*

%files glut-devel
%attr(755, root, bin) /usr/lib/libglut.so
%attr(644, root, bin) /usr/lib/libglut.a
%attr(444, root, root) /usr/include/GL/glut.h

%files devel
%attr(755, root, bin) /usr/lib/libMesa*.so
%attr(644, root, bin) /usr/lib/libMesa*.a
%attr(755, root, root) %dir /usr/lib/Mesa-%{version}
%attr(644, root, root)      /usr/lib/Mesa-%{version}/Make-config
%attr(755, root, root) %dir /usr/lib/Mesa-%{version}/util
%attr(-, root, root)        /usr/lib/Mesa-%{version}/util/*
%attr(755, root, root) %dir /usr/include/GL
%attr(444, root, root) /usr/include/GL/*
%attr(444, root, man)  /usr/man/man?/*

#%files demos
#%attr(755, root, root) %dir /usr/lib/Mesa-%{version}/book
#%attr(755, root, root) %dir /usr/lib/Mesa-%{version}/demos
#%attr(755, root, root) %dir /usr/lib/Mesa-%{version}/samples
#%attr(755, root, root) %dir /usr/lib/Mesa-%{version}/xdemos
#%attr(-, root, root) /usr/lib/Mesa-%{version}/book/*
#%attr(-, root, root) /usr/lib/Mesa-%{version}/demos/*
#%attr(-, root, root) /usr/lib/Mesa-%{version}/samples/*
#%attr(-, root, root) /usr/lib/Mesa-%{version}/xdemos/*
