Summary: Berkeley's Parallel Make
Summary(pt_BR): Make paralelo de Berkeley
Summary(es): Make paralelo de Berkeley
Name: pmake
Version: 1.0
Release: 14cl
Excludearch: alpha
Copyright: BSD
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
# was .gz
Source: ftp://sunsite.unc.edu/pub/Linux/devel/make/pmake.v1.0.tar.bz2
Patch: pmake-1.0-fsstnd.patch
Patch2: pmake-1.0-rules.patch
Patch3: pmake-tmprace.patch
BuildRoot: /var/tmp/pmake-root
Summary(de): Berkeley's Parallel Make
Summary(fr): Make parall�le de Berkeley
Summary(tr): Paralel Make program�

%description
The program make is used to coordinate the compilation and
linking of a set of sources into a program, recompiling
only what is necessary, thus saving a developer a lot of time.
In fact, make can do a lot more - read the info docs.

Pmake is a particular version of make which supports some
additional syntax not in the standard make program.  Some
berkeley programs have Makefiles written for pmake.

%description -l pt_BR
Pmake � uma vers�o particular de make que suporta algumas sintaxes
adicionais que n�o est�o no programa make padr�o. Alguns programas
berkeley possuem Makefiles escritos para pmake.

%description -l es
Pmake es una versi�n particular de make que soporta algunas sintaxis
adicionales que no est�n en el programa make padr�n. Algunos
programas berkeley poseen Makefiles escritos para pmake.

%description -l de
Das Programm make dient zum Koordinieren der Kompilierung
und Verkn�pfen einer Reihe von Quellen zu einem Programm,
wobei nur die notwendigen Teile neu kompiliert werden, was dem.
Entwickler viel Zeit spart. make kann noch viel mehr- lesen Sie die Doku.

Pmake ist eine besondere Version von make, die zus�tzliche Syntax
unterst�tzt, die im herk�mmlichen Programm nicht enthalten ist.
Einige Berkeley-Programme enthalten Makefiles f�r pmake.

%description -l fr
make sert � coordonner la compilation et l'�dition de liens
d'un ensemble de sources pour donner un programme, en ne recompilant
que ce qui est n�cessaire et en faisant donc gagner beaucoup de
temps au d�veloppeur. En fait, make peut faire beaucoup plus,
lisez les docs info.

pmake est une version particuli�re de make qui g�re une syntaxe
additionnelle qui n'est pas dans le make standard. Certains
programmes Berkeley ont des makefiles �crits pour pmake.

%description -l tr
Pmake, standart make program� i�inde yer almayan ek bir tak�m s�zdizimlerini
destekleyen bir make program s�r�m�d�r. Baz� Berkeley programlar�, pmake i�in
yaz�lm�� Makefile dosyalar�na sahiptir.

%prep
%setup -q -n pmake
%patch -p1
%patch2 -p1
%patch3 -p1

%build
make -f Makefile.dist

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,lib/pmake}

install -m 755 -s pmake $RPM_BUILD_ROOT/usr/bin/pmake
cp mk/* $RPM_BUILD_ROOT/usr/lib/pmake
install -m 644 make.1 $RPM_BUILD_ROOT/usr/man/man1/pmake.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/pmake
/usr/man/man1/pmake.1
/usr/lib/pmake
%doc README mk/bsd.README

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 30 1998 Marcelo Tosatti <marcelo@conectiva.com>
- arrumado tmp race no pmake

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Dec 16 1997 Otto Hammersmith <otto@redhat.com>
- fixed bug related to rules to build .a files.

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- updated spec file

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
