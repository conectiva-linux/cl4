Summary: The shared library for the S-Lang extension language.
Summary(pt_BR): Biblioteca compartilhada para linguagem de extens�o semelhante a C
Summary(es): Biblioteca compartida para leguaje de extensi�n semejante a C
Name: slang
%define version 1.2.2
Version: %{version}
Release: 4cl
Copyright: GPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://space.mit.edu/pub/davis/slang/slang%{version}.tar.gz
Url: ftp://space.mit.edu/pub/davis/slang/
Buildroot: /var/tmp/slang-root

%description
S-Lang is an interpreted language and a programming library.  The
S-Lang language was designed so that it can be easily embedded into
a program to provide the program with a powerful extension language.
The S-Lang library, provided in this package, provides the S-Lang
extension language.  S-Lang's syntax resembles C, which makes it easy
to recode S-Lang procedures in C if you need to.

%description -l pt_BR
Slang (pronunc�a-se "sssslang") � um poderoso interpretador que
suporta C-como sintaxe. Ele foi escrito no in�cio para ser facilmente
embutido em um programa para torn�-lo mais extens�vel. Slang
tamb�m oferece uma maneira de rapidamente desenvolver e debugar
aplica��es, embutindo-o de maneira segura e eficiente. Desde
que slang assemelhou-se com C, tornou-se f�cil re-codificar os
procedimentos slang em C se necess�rio.

%description -l es
Slang (se pronuncia "sssslang") es un potente interpretador que
soporta C-como sintaxis. Fue escrito en el inicio para ser f�cilmente
embutido en un programa para volverlo m�s extensible. Slang
tambi�n nos ofrece una manera de r�pidamente desarrollar y depurar
aplicaciones, empotr�ndolo de manera segura y eficiente. Desde que
slang se parece a C, se hizo f�cil recodificar los procedimientos
slang en C, si hace falta.

%package devel
Summary: The static library and header files for development using S-Lang.
Summary(pt_BR): Biblioteca est�tica e arquivos de inclus�o para slang
Summary(es): Biblioteca est�tica y archivos de inclusi�n para slang
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: slang

%description devel
This package contains the S-Lang extension language static libraries
and header files which you'll need if you want to develop S-Lang based
applications.  Documentation which may help you write S-Lang based
applications is also included.

Install the slang-devel package if you want to develop applications
based on the S-Lang extension language.

%description -l pt_BR devel
Este pacote cont�m as bibliotecas est�ticas e arquivos de inclus�o
slang, necess�rias ao desenvolvimento de aplica��es baseadas em
slang. Tamb�m inclui documenta��o para lhe ajudar na escrita de
aplica��es baseadas em slang.

%description -l es devel
Este paquete contiene las bibliotecas est�ticas y archivos de
inclusi�n slang, necesarios al desarrollo de aplicaciones basadas
en slang.  Tambi�n incluye documentaci�n para ayudarte en la
escritura de aplicaciones basadas en slang.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Oct 21 1998 Bill Nottingham <notting@redhat.com>
- libslang.so goes in -devel

* Sun Jun 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de

* Sat Jun  6 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.2.2 with buildroot.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 18 1998 Erik Troan <ewt@redhat.com>
- rebuilt to find terminfo in /usr/share

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- upgraded to 0.99.38 (will it EVER go 1.0???)
- all patches removed (all appear to be in this version)

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%prep
%setup -n slang -q

%build
CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr --includedir=/usr/include/slang
make elf all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/include/slang

make prefix=$RPM_BUILD_ROOT/usr install_include_dir=$RPM_BUILD_ROOT/usr/include/slang install-elf install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/lib/libslang.so.*

%files devel
%doc doc
/usr/lib/libslang.a
/usr/lib/libslang.so
/usr/include/slang
