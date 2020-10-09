Summary: Translator of English <--> C/C++ declarations
Summary(pt_BR): Tradutor ingl�s <--> declara��es C/C++
Summary(es): Traductor ingl�s <--> declaraciones C/C++
Name: cdecl
Version: 2.5
Release: 11cl
Copyright: distributable
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/cdecl-2.5.tar.gz
Patch: cdecl-2.5.misc.patch
BuildRoot: /var/tmp/cdecl-root
Summary(de): �bersetzer von Deklarationen zwischen Englisch und C/C++
Summary(fr): Traducteur anglais <--> d�clarations C/C++.
Summary(tr): �ngilizceden C/C++ bildirimlerine �evirici

%description
This is a package to translate English to C/C++ function declarations
and vice versa.  It is useful for programmers.

%description -l pt_BR
Este � um pacote para traduzir ingl�s para declara��es de fun��es
C/C++ e vicer-versa. �til para programadores.

%description -l es
Este es un paquete para traducir ingl�s para declaraciones de
funciones C/C++ y viceversa. �til para programadores.

%description -l de
Dies ist ein Paket zum �bersetzen von Englisch in C/C++ Funktionsanweisungen
und umgekehrt. N�tzlich f�r Programmierer.

%description -l fr
C'est un package pour traduire de l'anglais en d�clarations de fonctions
C/C++ et vice-versa. Utile pour les programmeurs.

%description -l tr
�ngilizceden C/C++ bildirimlerine �eviri i�lemini ve tersini ger�ekle�tirmek
i�in kullan�lan bir pakettir. Programc�lar i�in kullan��l�d�r.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make BINDIR=$RPM_BUILD_ROOT/usr/bin MANDIR=$RPM_BUILD_ROOT/usr/man/man1 \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/cdecl
/usr/bin/c++decl
/usr/man/man1/cdecl.1
/usr/man/man1/c++decl.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- built against readline lib w/ proper soname

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
