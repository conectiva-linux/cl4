Summary: A C library for parsing command line parameters.
Summary(pt_BR): Biblioteca C para analisar gramaticalmente os parâmetros da linha de comando
Summary(es): Biblioteca C para analizar gramaticalmente los parámetros de la línea de comando
Name: popt
Version: 1.3
Release: 2cl
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://ftp.redhat.com/pub/redhat/code/popt/popt-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}root

%description
Popt is a C library for parsing command line parameters.  Popt
was heavily influenced by the getopt() and getopt_long() functions,
but it improves on them by allowing more powerful argument expansion.
Popt can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments.  Popt allows command
line arguments to be aliased via configuration files and includes
utility functions for parsing arbitrary strings into argv[] arrays
using shell-like rules.

Install popt if you're a C programmer and you'd like to use its
capabilities.

%description -l pt_BR
O Popt é uma biblioteca C para interpretar parâmetros da linha
de comando.  Fortemente influenciada pelas funções getopt()
e getopt_long(), permitindo uma expansão de argumentos mais
poderosa. Ela pode analisar um vetor arbitrário no estilo argv[]
e configurar automaticamente variáveis baseada nos argumentos da
linha de comando.

Também permite que argumentos da linha de comando tenham aliases via
arquivos de configuração, e inclui funções utilitárias para análise
de strings em vetores argv[] usando regras parecidas com as de shell.

%description -l es
Popt es una biblioteca C para interpretar parámetros de la línea
de comando.  Bastante influenciada por las funciones getopt()
y getopt\_long(), permitiendo una expansión de argumentos más
eficaz. Puede analizar un vector arbitrario en el estilo argv[]
y configurar automáticamente variables basadas en los argumentos
de la línea de comando.  También permite que argumentos de la línea
de comando tengan aliases vía archivos de configuración, y incluye
funciones utilitarias para análisis de strings en vectores argv[]
usando reglas parecidas con las de shell.

%prep
%setup -q
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --disable-shared

%build
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/libpopt.a
/usr/include/popt.h
/usr/man/man3/popt.3

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Injected new group into package

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Dec 10 1998 Michael Johnson <johnsonm@redhat.com>
- released 1.2.2; see CHANGES

* Tue Nov 17 1998 Michael K. Johnson <johnsonm@redhat.com>
- added man page to default install

* Thu Oct 22 1998 Erik Troan <ewt@redhat.com>
- see CHANGES file for 1.2

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- added ./configure step to spec file
