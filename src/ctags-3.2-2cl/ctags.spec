Summary: A C programming language indexing and/or cross-reference tool.
Summary(pt_BR): Ctags exuberantes! Ferramenta de referência cruzada para C
Summary(es): Ctags ¡exuberantes! Herramienta de referencia cruzada para C
Name: ctags
Version: 3.2
Release: 2cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/ctags-%{version}.tar.gz
Patch0: ctags-3.2-glibc.patch
Buildroot: /var/tmp/ctags-root

%description
Ctags generates an index (or tag) file of C language objects found in
C source and header files.  The index makes it easy for text editors or
other utilities to locate the indexed items.  Ctags can also generate a
cross reference file which lists information about the various objects
found in a set of C language files in human readable form.  Exuberant
Ctags improves on ctags because it can find all types of C language tags,
including macro definitions, enumerated values (values inside enum{...}),
function and method definitions, enum/struct/union tags, external
function prototypes, typedef names and variable declarations.  Exuberant
Ctags is far less likely to be fooled by code containing #if preprocessor
conditional constructs than ctags.  Exuberant ctags supports output of
emacs style TAGS files and can be used to print out a list of selected
objects found in source files.

Install ctags if you are going to use your system for C programming.

%description -l pt_BR
Um ctags melhor que gera tags para todos os tipos possíveis de tag:
definições de macro, valores enumerados, definições de função
e método, tags enum/struct/union, protótipos de função externa
(opcional), typedefs e declarações variáveis. É mais difícil de ser
enganado em códigos que contenha a diretiva condicional #if para o
pré-processador, pois utiliza um algoritmo condicional de caminho
para resolver decisões complicadas, e um algoritmo de resgate quando
este falha. Também pode ser usado para mostrar uma lista de objetos
selecionados que estejam nos arquivos fonte.

%description -l es
Un ctags mejor que crea tags para todos los tipos posibles de tag:
definiciones de macro, valores enumerados, definiciones de función
y método, tags enum/struct/union, prototipos de función externa
(opcional), typedefs y declaraciones variables. Es más difícil de
ser engañado en códigos que contenga la directiva condicional #if
para el preprocesador, pues utiliza un algoritmo condicional de
camino para solucionar decisiones complicadas, y un algoritmo de
rescate cuando este falla. También puede ser usado para enseñar
una lista de objetos seleccionados que esté en los archivos fuente.

%prep
%setup -q
%patch0 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install-strip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc FAQ INSTALL NEWS QUOTES README
/usr/bin/ctags
/usr/man/man1/ctags.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)
- version 3.2

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.0.3

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- removed etags.  Emacs provides its own; and needs to support
  more than just C.

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 1.5 to 1.6

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
