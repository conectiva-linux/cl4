Summary: A Pascal to C translator.
Summary(pt_BR): Biblioteca compartilhada para programas feitos com o conversor p2c de pascal para C
Summary(es): Biblioteca compartida para programas hechos con el convertidor p2c de pascal a C
Name: p2c
Version: 1.22
Release: 3cl
Copyright: distributable
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source: ftp://csvax.cs.caltech.edu/pub/p2c-1.22.tar.bz2
Patch0: p2c-1.20-misc.patch
Patch1: p2c-1.20-br.patch
Patch2: p2c-newpatch.patch
BuildRoot: /var/tmp/p2c-root
Obsoletes: basic

%description
P2c is a system for translating Pascal programs into the C language.
P2c accepts input source files in certain Pascal dialects:  HP
Pascal, Turbo/UCSD Pascal, DEC VAX Pascal, Oregon Software Pascal/2,
Macintosh Programmer's Workshop Pascal and Sun/Berkeley Pascal.  P2c
outputs a set of .c and .h files which make up a C program equivalent
to the original Pascal program.  The C program can then be compiled
using a standard C compiler, such as gcc.

Install the p2c package if you need a program for translating Pascal
code into C code.

%description -l pt_BR
O p2c é um tradutor de Pascal para C. Ele é usado para converter o
código fonte Pascal em código fonte C, então este pode ser compilado
usando-se um compilador C padrão (como gcc).

%description -l es
p2c es un traductor de Pascal para C. Se usa para convertir el
código fuente Pascal en código fuente C, éste puede ser compilado
usándose un compilador C padrón (como gcc).

%package devel
Summary: Files for p2c Pascal to C translator development.
Summary(pt_BR): Programas e arquivos de inclusão para o tradutor de Pascal para C
Summary(es): Programas y archivos de inclusión para el traductor de Pascal a C
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes

%description devel
The p2c-devel package contains the files necessary for development
of the p2c Pascal to C translation system.

Install the p2c-devel package if you want to do p2c development.

%description -l pt_BR devel
Este é o kit de desenvolvimento para o tradutor de Pascal para
C. Contém os arquivos de inclusão e alguns programas que podem ser
úteis para quem usa o tradutor.

%description -l es devel
Este es el kit de desarrollo para el traductor de Pascal para C.
Contiene los archivos de inclusión y algunos programas que pueden
ser útiles para quien usa el traductor.

%prep
%setup  -q
#%patch0 -p1 -b .misc
#%patch1 -p1 -b .br
%patch2 -p1 -b .new
mkdir src/shlib
mkdir include
ln -s ../src include/p2c

%build
cp src/sys.p2crc src/p2crc
make RPM_OPTS="$RPM_OPT_FLAGS"
make RPM_OPTS="$RPM_OPT_FLAGS" shlib -C src

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,man/man1,include}
make install RPM_INSTALL=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/bin/p2c
 
%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc examples/*
%defattr(-,root,root)
/usr/bin/p2c
/usr/lib/libp2c.so.1.2.0
/usr/lib/p2c
/usr/man/man1/p2c.1

%files devel
%defattr(-,root,root)
/usr/lib/libp2c.a
/usr/include/p2c


%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun 15 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- fixed group.

* Sun Mar 21 1999 Michael Maher <mike@redhat.com>
- Merged patched tar ball on gribble with original 
  installation.  Was missing important parts of 
  make files.  
- Fixed many errors in Makefiles. 
- moved 'basic' stuff into doc

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1
- buildroot
- binary files and man page should really be in the main package, 
  not -devel

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

