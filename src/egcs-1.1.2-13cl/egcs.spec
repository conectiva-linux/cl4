# Rodrigo Parra Novo <rodarvus@conectiva.com> - 19990518
# Added a kludge to make spec file compatible with rpm 2.5.6

%ifarch i386
%define _target_cpu i386
%endif

%ifarch alpha
%define _target_cpu alpha
%endif

%ifarch sparc
%define _target_cpu sparc
%endif

%define STDC_VERSION 2.9.0
%define EGCS_VERSION 1.1.2
Summary: An experimental GNU compiler system.
Summary(pt_BR): Sistema de Compiladores Experimentais GNU
Summary(es): Sistema de Compiladores Experimentales GNU
Name: egcs
Version: %{EGCS_VERSION}
Release: 13cl
Copyright: GPL
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source0: ftp://egcs.cygnus.com/pub/egcs/releases/egcs-%{EGCS_VERSION}/egcs-%{EGCS_VERSION}.tar.bz2
Source1: egcs-libstdc++-compat.tar.gz
Patch0: ftp://ftp.varesearch.com/pub/support/hjl/egcs/egcs-1.1.2-linux.patch
Patch1: egcs-1.1.2-davem.patch
Buildroot: /var/tmp/egcs-%{EGCS_VERSION}-root
Url: http://egcs.cygnus.com/
Requires: binutils >= 2.9.1.0.21
Obsoletes: gcc
Provides: gcc
Requires: cpp = %{EGCS_VERSION}
Prereq: info

%description
EGCS is a free software project that intends to further the development
of GNU compilers using an open development environment.  The egcs package
contains the egcs compiler, a compiler aimed at integrating all the
optimizations and features necessary for a high-performance and stable
development environment.

Install egcs if you'd like to use an experimental GNU compiler.

%description -l pt_BR
Um compilador com o objetivo de integrar todas as otimizações e
características necessárias para um ambiente de desenvolvimento
estável e de alta performance.

%description -l es
Un compilador con el objetivo de integrar todas las optimizaciones
y características necesarias para un ambiente de desarrollo estable
y de alto desempeño.

%package c++
Summary: C++ support for the gcc compiler.
Summary(pt_BR): Suporte C++ para o gcc
Summary(es): Soporte C++ para gcc
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: egcs = %{EGCS_VERSION}
Obsoletes: gcc-c++
Obsoletes: libstdc++-devel
Obsoletes: libg++-devel
Requires: libstdc++ = %{STDC_VERSION}
Requires: cpp = %{EGCS_VERSION}

%description c++
This package adds C++ support to the GNU C compiler. It includes support for
most of the current C++ specification, including templates and exception
handling. It does include the static standard C++ library and C++ header
files; the library for dynamically linking programs is available separately.

%description -l pt_BR c++
Este pacote adiciona suporte C++ ao compilador C da GNU. Inclui
suporte para grande parte da especificação C++ corrente, incluindo
templates e tratamento de exceções. Não inclui a biblioteca padrão
C++, que está disponível separadamente.

%description -l es c++
Este paquete adiciona soporte C++ al compilador C de GNU. Incluye
soporte para gran parte de la especificación C++ corriente,
incluyendo templates y tratamiento de excepciones. No incluye la
biblioteca padrón C++, que está disponible separadamente.

%package objc
Summary: Objective C support for the gcc compiler.
Summary(pt_BR): Suporte Objective C para o gcc
Summary(es): Soporte Objective C para gcc
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: egcs = %{EGCS_VERSION}
Obsoletes: gcc-objc
Requires: cpp = %{EGCS_VERSION}

%description objc
Egcs-objc provides Objective C support for the GNU C compiler (gcc).
Mainly used on systems running NeXTSTEP, Objective C is an 
object-oriented derivative of the C language.

Install egcs-objc if you are going to do Objective C development and you
would like to use the gcc compiler.  You will also need to install the gcc
package.

%description -l pt_BR objc
Este pacote adiciona suporte Objective C ao compilador C da
GNU. Objective C é uma linguagem orientada a objetos derivada da
linguagem C, sendo mais utilizada em sistemas rodando NeXTSTEP. Este
pacote não inclui a biblioteca padrão de objetos do Objective C.

%description -l es objc
Este paquete adiciona soporte Objective C al compilador C de
GNU. Objective C es un lenguaje orientado a objetos derivado
del lenguaje C, siendo más utilizado en sistemas ejecutando
NeXTSTEP. Este paquete no incluye la biblioteca padrón de objetos
del Objective C.

%package g77
Summary: Fortran 77 support for the gcc compiler.
Summary(pt_BR): Suporte a Fortran 77 para o gcc
Summary(es): Soporte a Fortran 77 para gcc
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: egcs = %{EGCS_VERSION}
Prereq: info

%description g77
The egcs-g77 package provides support for compiling Fortran 77
programs with the GNU gcc compiler.

You should install egcs-g77 if you are going to do Fortran development and
you would like to use the gcc compiler.  You will also need to install the
gcc package.

%description -l pt_BR g77
Este pacote adiciona suporte para compilar programas escritos em
Fortran 77 com o compilador do GNU.

%description -l es g77
Este paquete adiciona soporte para compilar programas escritos en
Fortran 77 con el compilador del GNU.

%package -n libstdc++
Summary: GNU c++ library
Summary(pt_BR): Biblioteca c++ GNU
Summary(es): Biblioteca c++ GNU
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Obsoletes: libg++
Version: %{STDC_VERSION}

%description -n libstdc++
EGCS is a free software project that intends to further the development
of GNU compilers using an open development environment.  The egcs
package contains the egcs compiler, a compiler aimed at integrating all
the optimizations and features necessary for a high-performance and stable
development environment. EGCS includes the shared libraries necessary for
running C++ appplications, along with additional GNU tools.

Install egcs if you'd like to use an experimental GNU compiler.

%description -l pt_BR -n libstdc++
Esta é a implementação das bibliotecas padrão do C++, junto
com ferramentas GNU adicionais. O pacote inclui as bibliotecas
compartilhadas necessárias para executar aplicações C++.

%description -l es -n libstdc++
Este es el soporte de las bibliotecas padrón del C++, junto con
herramientas GNU adicionales. El paquete incluye las bibliotecas
compartidas necesarias para ejecutar aplicaciones C++.

%package -n cpp
Summary: The C Preprocessor.
Summary(pt_BR): Um preprocessador para a linguagem C
Summary(es): The C Preprocessor.
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Prereq: info

%description -n cpp
The C preprocessor is a 'macro processor' which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define 'macros,' which are abbreviations for longer
constructs.

The C preprocessor provides four separate facilities that you can use as
you see fit:

* Inclusion of header files. These are files of declarations that can be
  substituted into your program.
* Macro expansion. You can define 'macros,' which are abbreviations for 
  arbitrary fragments of C code, and then the C preprocessor will replace
  the macros with their definitions throughout the program.
* Conditional compilation. Using special preprocessing directives,
  you can include or exclude parts of the program according to various
  conditions.
* Line control. If you use a program to combine or rearrange source files
  into an intermediate file which is then compiled, you can use line
  control to inform the compiler about where each source line originated.

You should install this package if you are a programmer who is searching for
such a macro processor.

%description -l pt_BR -n cpp
O preprocessador C é um "processador de macros", que é utilizado pelo
compilador C para fazer algumas modificações no seu programa, antes da
compilação em si. Ele é chamado de "processador de macros" porque permite
a voce definir "macros", que são abreviações para construções mais
complicadas.

%description -l es -n cpp
The C preprocessor is a 'macro processor' which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define 'macros,' which are abbreviations for longer
constructs.

The C preprocessor provides four separate facilities that you can use as
you see fit:

* Inclusion of header files. These are files of declarations that can be
  substituted into your program.
* Macro expansion. You can define 'macros,' which are abbreviations for 
  arbitrary fragments of C code, and then the C preprocessor will replace
  the macros with their definitions throughout the program.
* Conditional compilation. Using special preprocessing directives,
  you can include or exclude parts of the program according to various
  conditions.
* Line control. If you use a program to combine or rearrange source files
  into an intermediate file which is then compiled, you can use line
  control to inform the compiler about where each source line originated.

You should install this package if you are a programmer who is searching for
such a macro processor.

%prep
%setup -q -n %{name}-%{EGCS_VERSION}
%patch0 -p1
%patch1 -p1
mkdir compat
tar xzf %{SOURCE1} -C compat
cd gcc ; autoconf ; cd ..

%build
rm -rf obj-$RPM_ARCH-linux
mkdir obj-$RPM_ARCH-linux
cd obj-$RPM_ARCH-linux
../configure  --prefix=/usr \
	--enable-shared --enable-threads \
	$RPM_ARCH-conectiva-linux

PATH=$PATH:/sbin:/usr/sbin
# gperf is most likely broken on alpha and sparc 
touch  ../gcc/c-gperf.h
make MAKEINFO="makeinfo --no-split"  bootstrap-lean

%install
rm -rf $RPM_BUILD_ROOT
cd obj-$RPM_ARCH-linux
PATH=$PATH:/sbin:/usr/sbin
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	mandir=$RPM_BUILD_ROOT/usr/man/man1 \
	MAKEINFO="makeinfo --no-split" 
FULLVER=$($RPM_BUILD_ROOT/usr/bin/gcc --version)
FULLPATH=$(dirname $RPM_BUILD_ROOT/usr/lib/gcc-lib/$RPM_ARCH-*/$FULLVER/cc1)

file $RPM_BUILD_ROOT/usr/bin/* | grep ELF | cut -d':' -f1 | xargs strip || :
strip $FULLPATH/{cc1,cc1obj,cc1plus,cpp,f771,collect2}

# fix some things
ln $RPM_BUILD_ROOT/usr/bin/$RPM_ARCH-conectiva-linux-gcc $RPM_BUILD_ROOT/usr/bin/egcs
ln -sf gcc $RPM_BUILD_ROOT/usr/bin/cc
ln $RPM_BUILD_ROOT/usr/man/man1/gcc.1 $RPM_BUILD_ROOT/usr/man/man1/egcs.1
#mv $RPM_BUILD_ROOT/usr/include/g++-2 $RPM_BUILD_ROOT/usr/include/g++

rm -f $RPM_BUILD_ROOT/usr/info/dir
gzip -n -9f $RPM_BUILD_ROOT/usr/info/*.info* 

ln -sf g77.1 $RPM_BUILD_ROOT/usr/man/man1/f77.1
ln -sf g77 $RPM_BUILD_ROOT/usr/bin/f77

mkdir -p $RPM_BUILD_ROOT/lib
ln -sf ../${FULLPATH##$RPM_BUILD_ROOT/}/cpp $RPM_BUILD_ROOT/lib/cpp

ln -sf cccp.1 $RPM_BUILD_ROOT/usr/man/man1/cpp.1

#install the compatibility libstdc++ library
[ -d ../compat/$RPM_ARCH ] && install -m 755 ../compat/$RPM_ARCH/* $RPM_BUILD_ROOT/usr/lib/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info --info-dir=/usr/info /usr/info/gcc.info.gz

%post -n cpp
/sbin/install-info --info-dir=/usr/info /usr/info/cpp.info.gz

%post g77
/sbin/install-info --info-dir=/usr/info /usr/info/g77.info.gz

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete --info-dir=/usr/info /usr/info/gcc.info.gz
fi

%preun -n cpp
if [ $1 = 0 ]; then
   /sbin/install-info --delete --info-dir=/usr/info /usr/info/cpp.info.gz
fi

%preun g77
if [ $1 = 0 ]; then
   /sbin/install-info --delete --info-dir=/usr/info /usr/info/g77.info.gz
fi

%post -n libstdc++ -p /sbin/ldconfig

%postun -n libstdc++ -p /sbin/ldconfig

%files
%doc README* COPYING COPYING.LIB
%dir /usr/lib/gcc-lib
%dir /usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux
%dir /usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*
%dir /usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include
/usr/bin/%{_target_cpu}-conectiva-linux-gcc
/usr/bin/egcs
/usr/bin/gcov
/usr/bin/protoize
/usr/bin/unprotoize
/usr/bin/gcc
/usr/bin/cc
/usr/info/gcc*

/usr/man/man1/gcc.1
/usr/man/man1/egcs.1

/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/SYSCALLS.c.X
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/cc1
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/collect2
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/libgcc.a
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/libgcc.map
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/specs

%ifnarch alpha
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/*.o
%endif

/usr/%{_target_cpu}-conectiva-linux

/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/README
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/float.h
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/iso646.h
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/limits.h
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/proto.h
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/stdarg.h
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/stdbool.h
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/stddef.h
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/syslimits.h
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/va-*.h
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/varargs.h
%ifarch ppc
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/*-asm.h
%endif

%files -n cpp
/lib/cpp
/usr/man/man1/cpp.1
/usr/man/man1/cccp.1
/usr/info/cpp.info*.gz
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/cpp

%files c++
/usr/man/man1/g++.1
/usr/bin/g++
/usr/bin/c++
/usr/bin/c++filt
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/cc1plus
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/libstdc*
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/exception
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/new
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/typeinfo
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/new.h
/usr/include/g+*
/usr/lib/libstdc++-2-libc*-%{STDC_VERSION}.a
/usr/lib/libstdc++-2-libc*-%{STDC_VERSION}.so
/usr/lib/libstdc++-libc*.a.2
%ifarch ppc
/usr/lib/nof
%endif

%files objc
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/cc1obj
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/libobjc.a
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/include/objc

%files g77
/usr/bin/g77
/usr/bin/f77
/usr/info/g77*
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/f771
/usr/lib/gcc-lib/%{_target_cpu}-conectiva-linux/egcs-*/libg2c.a
/usr/man/man1/g77.1
/usr/man/man1/f77.1
/usr/lib/gcc-lib/*-conectiva-linux/egcs-*/include/g2c.h

%files -n libstdc++
/usr/lib/libstdc++-2-libc*-%{STDC_VERSION}.so
%ifarch i386 sparc alpha
/usr/lib/libstdc++.so.2.8.0
%endif
%ifarch i386 alpha
/usr/lib/libstdc++.so.2.7.2.8
/usr/lib/libg++.so.2.7.2.8
%endif

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 19 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x and kernel 2.2.x

* Tue May 18 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added to Conectiva Linux

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 12)

* Wed Mar 17 1999 Cristian Gafton <gafton@redhat.com>
- version 1.1.2
- added patch from davem

* Fri Mar 12 1999 Cristian Gafton <gafton@redhat.com>
- version 1.1.2pre3
