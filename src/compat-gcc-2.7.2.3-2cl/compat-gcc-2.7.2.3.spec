Summary: GNU C Compiler
Summary(pt_BR): Compilador C GNU
Summary(es): Compilador C GNU
Name: compat-gcc
%define version 2.7.2.3
Version: %{version}
Release: 2cl
Copyright: GPL
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
# Source: ftp://prep.ai.mit.edu/pub/gnu/gcc-%{version}.tar.gz
# repacked with bzip2
Source: ftp://prep.ai.mit.edu/pub/gnu/gcc-%{version}.tar.bz2
Patch1: gcc-2.7.2-make.patch
Requires: binutils
Buildroot: /var/tmp/gcc-root
Exclusivearch: i386

%description
The GNU C compiler -- a full featured ANSI C compiler, with support
for K&R C as well. GCC provides many levels of source code error
checking tradionaly provided by other tools (such as lint), produces
debugging information, and can perform many different optimizations to
the resulting object code.

Install this package if you want to compile the Linux kernel.

%description -l pt_BR
Compilador C GNU, que possui todas as características de um
compilador C ANSI, e também suporta K&R. GCC fornece vários
níveis de verificação de erro de código fonte, tradicionalmente
fornecida por outras ferramentas (como lint), gera informação para
depuração, e pode produzir códigos objeto com diferentes níveis
de otimização.

Instale este pacote se você deseja compilar o cerne (kernel) do
Linux.

%description -l es
Compilador C GNU, que posee todas las características de un
compilador C ANSI, y también soporta K\&R. GCC ofrece varios
niveles de verificación de error de código fuente, tradicionalmente
ofrecida por otras herramientas (como lint), crea información para
depuración, y puede producir códigos objeto con diferentes niveles
de optimización.

Instale este paquete se deseas compilar el Linux kernel.

%prep
%setup -q -n gcc-%{version}
%patch1 -p1 -b .cnc

%build
 ./configure --prefix=/usr \
	--local-prefix=/usr/local --gxx-include-dir=/usr/include/g++ \
	${RPM_ARCH}-conectiva-linux 

make LANGUAGES=c CFLAGS="-O2"
make stage1
make CC="stage1/xgcc -Bstage1/" CFLAGS="-O2" LDFLAGS="-s"
make stage2
make CC="stage2/xgcc -Bstage2/" CFLAGS="-O2" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,info,man}
make CC="stage2/xgcc -Bstage2/" CFLAGS="-O2" LDFLAGS="-s" install \
	prefix=$RPM_BUILD_ROOT/usr

rm -rf $RPM_BUILD_ROOT/usr/lib/gcc-lib/${RPM_ARCH}-conectiva-linux/*/include/objc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/lib/gcc-lib/*-conectiva-linux/*
%dir /usr/lib/gcc-lib/*-conectiva-linux/*/include
/usr/lib/gcc-lib/*-conectiva-linux/*/SYSCALLS.c.X
/usr/lib/gcc-lib/*-conectiva-linux/*/cc1
/usr/lib/gcc-lib/*-conectiva-linux/*/cpp
/usr/lib/gcc-lib/*-conectiva-linux/*/libgcc.a
/usr/lib/gcc-lib/*-conectiva-linux/*/specs
/usr/lib/gcc-lib/*-conectiva-linux/*/include/*
/usr/lib/gcc-lib/*-conectiva-linux/*/*.o

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Made this package from the old gcc 2.7.2.3
- All architectures get cc/gcc from egcs. The old gcc 2.7.2.3 will only
  be disponible as a switch (-V 2.7.2.3) in egcs. (To compile the Linux
  kernel)
