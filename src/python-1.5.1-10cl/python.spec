Summary: An interpreted, interactive object-oriented programming language.
Summary(pt_BR): Linguagem script de alto nível com interface X
Summary(es): Lenguaje script de alto nivel con interface X
Name: python
Version: 1.5.1
Release: 10cl
Copyright: distributable
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source0: ftp://ftp.python.org/pub/python/src/pyth151.tgz
Source1: Python-Doc.tar.gz
Patch0: python-1.5.1-config.patch
Patch1: python-1.4-gccbug.patch
Patch2: python-1.5-localbin.patch
Patch3: Python-1.5.1-nosed.patch
Buildroot: /var/tmp/python-root

%description
Python is an interpreted, interactive, object-oriented programming
language often compared to Tcl, Perl, Scheme or Java. Python includes
modules, classes, exceptions, very high level dynamic data types and
dynamic typing. Python supports interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
Mac and MFC).

Programmers can write new built-in modules for Python in C or C++.
Python can be used as an extension language for applications that
need a programmable interface. This package contains most of the
standard Python modules, as well as modules for interfacing to the
Tix widget set for Tk and RPM.

Note that documentation for Python is provided in the python-docs
package.

%description -l pt_BR
Python é uma linguagem de scripts interpretada orientada a objetos. Contém
suporte para carga dinâmica de objetos, classes, módulos e exceções.
Adicionar interfaces para novos sistemas de biblioteca através de código C
é simples, tornando Python fácil de usar em ambientes particulares/customizados.

Este pacote Python inclui a maioria do módulos padrão Python, junto com
módulos para interfaceamento para o conjunto de componentes Tix para Tk e RPM.

%description -l es
Python es un lenguaje de scripts interpretado orientado a objetos.
Contiene soporte para carga dinámica de objetos, clases, módulos
y excepciones.

Es sencillo adicionar interfaces para nuevos sistemas de biblioteca
a través de código C, tornando Python fácil de usar en ambientes
articulares/personalizados.  Este paquete Python incluye la mayoría
de los módulos padrón Python, junto con módulos para crear interfaces
para el conjunto de componentes Tix para Tk y RPM.

%package devel
Summary: The libraries and header files needed for Python development.
Summary(pt_BR): Bibliotecas e arquivos de inclusão para construir programas em python
Summary(es): Bibliotecas y archivos de inclusión para construir programas en python
Requires: python = 1.5.1
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
The Python programming language's interpreter can be extended with
dynamically loaded extensions and can be embedded in other programs.
This package contains the header files and libraries needed to do
these types of tasks.

Install python-devel if you want to develop Python extensions.  The
python package will also need to be installed.  You'll probably also
want to install the python-docs package, which contains Python
documentation.

%description -l pt_BR devel
O interpretador Python permite incluir com facilidade extensões
carregadas dinamicamente. Python é também fácil de ser embutido
em outros programas. Este pacote contém os arquivos de inclusão e
bibliotecas necessários para estas duas tarefas.

%description -l es devel
El interpretador Python permite incluir con facilidad extensiones
cargadas dinámicamente. Python es también fácil de ser empotrado
en otros programas. Este paquete contiene los archivos de inclusión
y bibliotecas necesarios para estas dos tareas.

%package docs
Summary: Documentation for the Python programming language.
Summary(pt_BR): Documentação sobre Python
Summary(es): Documentación sobre Python
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación

%description docs
The python-docs package contains documentation on the Python
programming language and interpreter.  The documentation is provided
in ASCII text files and in LaTeX source files.

Install the python-docs package if you'd like to use the documentation
for the Python language.

%description -l pt_BR docs
Este pacote contém a documentação da linguagem Python e de seu
interpretador como um conjunto de arquivos ASCII puro e fontes
LaTeX.

%description -l es docs
Este paquete contiene la documentación del lenguaje Python y de
su interpretador como un conjunto de archivos ASCII puro y fuentes
LaTeX.

%package -n tkinter
Summary: A graphical user interface for the Python scripting language.
Summary(pt_BR): Interface GUI para Phyton
Summary(es): Interface GUI para Phyton
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: libtcl8.0.so libtk8.0.so

%description -n tkinter
The Tkinter (Tk interface) program is an graphical user interface for
the Python scripting language.

You should install the tkinter package if you'd like to use a graphical
user interface for Python programming.

%description -l pt_BR -n tkinter
Uma interface gráfica para Python, baseada em Tcl/Tk, e usada por
muitas ferramentas de configuração.

%description -l es -n tkinter
Una interface gráfica para Python, basada en Tcl/Tk, y usada por
muchas herramientas de configuración.

%prep
%setup -q -n Python-1.5.1 -a1
%patch0 -p1 -b .config
%patch2 -p1 -b .localbin

#%ifarch alpha
#%patch1 -p1
#%endif
%patch3 -p1 -b .nosed
find . -name "*.nosed" -exec rm -f {} \;

echo ': ${LDSHARED='gcc -shared'}' > config.cache
echo ': ${LINKFORSHARED='-rdynamic'}' >> config.cache
echo ': ${CCSHARED='-fPIC'}' >> config.cache

cp Lib/lib-old/rand.py Lib

%build
MACHDEP=linux-$RPM_ARCH ./configure --prefix=/usr --with-threads

LDFLAGS=-s make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib}
make install prefix=$RPM_BUILD_ROOT/usr
strip $RPM_BUILD_ROOT/usr/bin/python

rm -f modules-list.full
for n in $RPM_BUILD_ROOT/usr/lib/python1.5/*; do
  [ -d $n ] || echo $n
done >> modules-list.full

for mod in $RPM_BUILD_ROOT/usr/lib/python1.5/lib-dynload/* ; do
  [ `basename $mod` = _tkinter.so ] || echo $mod
done >> modules-list.full
sed -e "s|$RPM_BUILD_ROOT||g" < modules-list.full > modules-list

%clean
rm -rf $RPM_BUILD_ROOT
rm -f modules-list modules-list.full

%files -f modules-list
%defattr(-,root,root)
/usr/bin/*
%dir /usr/lib/python1.5
/usr/lib/python1.5/plat-linux-%{_target_cpu}
/usr/lib/python1.5/lib-stdwin
%dir /usr/lib/python1.5/lib-dynload

%files devel
%defattr(-,root,root)
/usr/lib/python*/test
/usr/lib/python*/config
/usr/include/python1.5

%files docs
%defattr(0644,root,root,0755)
%doc Misc/COPYRIGHT Misc/NEWS Misc/HYPE Misc/README Misc/cheatsheet Misc/BLURB* 
%doc Misc/HISTORY Doc

%files -n tkinter
%defattr(-,root,root)
/usr/lib/python1.5/lib-tk
/usr/lib/python1.5/lib-dynload/_tkinter.so

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 10)

* Thu Mar 18 1999 Bill Nottingham <notting@redhat.com>
- fix permissions in python-docs

* Thu Feb 11 1999 Michael Johnson <johnsonm@redhat.com>
- added mpzmodule at user request (uses gmp)
- added bsddbmodule at user request (uses db 1.85 interface)

* Mon Feb 08 1999 Michael Johnson <johnsonm@redhat.com>
- add --with-threads at user request
- clean up spec file

* Fri Jan 08 1999 Michael K. Johnson <johnsonm@redhat.com>
- New libc changes ndbm.h to db1/ndbm.h and -ldb to -ldb1

* Thu Sep  3 1998 Jeff Johnson <jbj@redhat.com>
- recompile for RH 5.2.

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- python-docs used to require /usr/bin/sed. Changed to /bin/sed instead

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- fixed the spec file for version 1.5.1
- buildroot (!)

* Mon Apr 20 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated to python 1.5.1
- created our own Python-Doc tar file from 1.5 to substitute for the
  not-yet-released Doc package.
- build _tkinter properly
- use readline again
- build crypt module again
- install rand replacement module
- added a few modules

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to python 1.5
- made /usr/lib/python1.5 file list automatically generated

* Tue Nov 04 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fixed dependencies for python and tkinter

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- pulled out tk-related stuff into tkinter package

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- bunches of scripts used /usr/local/bin/python instead of /usr/bin/python

* Tue Sep 30 1997 Erik Troan <ewt@redhat.com>
- updated for tcl/tk 8.0

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
