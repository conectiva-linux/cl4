Summary: Generates function prototypes and variable declarations from C code.
Summary(pt_BR): Utilitário de prototipação C
Summary(es): Utilitario de prototipos C
Name: cproto
Version: 4.6
Release: 3cl
Copyright: Public Domain
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://ftp.oce.com/pub/cproto/cproto-%{version}.tar.gz
#Patch: cproto-4.4-gcc.patch
Patch1: cproto-4.6.1-patch
Prefix: %{_prefix}
BuildRoot: /var/tmp/%{name}-root

%description
Cproto generates function prototypes and variable declarations from
C source code.  Cproto can also convert function definitions between the
old style and the ANSI C style.  This conversion will overwrite the
original files, however, so be sure to make a backup copy of your original
files in case something goes wrong.  Since cproto uses a Yacc generated
parser, it shouldn't be confused by complex function definitions as much
as other prototype generators) because it uses a Yacc generated parser.  

Cproto will be useful for C programmers, so install cproto if you are going
to do any C programming.

%description -l pt_BR
O cproto gera protótipos de função para funções definidas nos
arquivos fonte C para saída padrão. As definições das funções podem
ser no velho estilo ou no estilo ANSI C. Opcionalmente, cproto
também produz declarações para variáveis definidas nos arquivos. Se
não é fornecido argumento de arquivo, cproto lê da entrada padrão.

%description -l es
cproto crea prototipos de función para funciones definidas en
los archivos fuente C para salida padrón. Las definiciones de
las funciones pueden ser en el antiguo estilo o en el estilo ANSI
C. Opcionalmente, cproto también produce declaraciones para variables
definidas en los archivos. Si no se ofrece argumento de archivo,
cproto lee de la entrada padrón.

%prep
%setup -q

%build
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --exec-prefix=/usr

%configure --exec-prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=${RPM_BUILD_ROOT}%{_prefix} bindir=${RPM_BUILD_ROOT}%{_prefix}/bin install

( cd $RPM_BUILD_ROOT
  strip .%{_prefix}/bin/cproto
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README
%{_prefix}/bin/cproto
%{_prefix}/man/man1/cproto.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- update to 4.6.1 (#1516).
- use %configure

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
