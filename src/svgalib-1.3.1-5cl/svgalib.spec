Summary: library for full screen [S]VGA graphics
Summary(pt_BR): Biblioteca para gráficos em tela cheia [S]VGA
Summary(es): Biblioteca para gráficos en pantalla llena [S]VGA
Name: svgalib
Version: 1.3.1
Exclusivearch: i386
Exclusiveos: Linux
Release: 5cl
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://sunsite.unc.edu/pub/Linux/libs/graphics/svgalib-1.3.1.tar.bz2
Patch: svgalib-1.3.1-config.patch
Patch1: svgalib-1.3.1-devmem.patch
Patch2: svgalib-1.3.0-secu.patch
Patch4: svgalib-1.3.0-buildroot.patch
Patch5: svgalib-1.3.0-closebug.patch

Buildroot: /var/tmp/svgalib-root
Summary(de): Library für Vollbildschirm-[S]VGA-Grafiken
Summary(fr): Bibliothèque pour les graphiques plein écran [S]VGA
Summary(tr): Tam-ekran [S]VGA çizimleri kitaplýðý

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 31 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.3.1 final
- redid conf patch

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Nov 05 1998 Marcelo Tosatti <marcelo@conectiva.com>
- corrigidos problemas de segurança ao não fechar /dev/mem
- corrigido tmp race 
- rebuild for 3.0

* Wed Oct 21 1998 Conectiva <bugs@conectiva.com>
- updated to 1.3.1.19981020

* Wed Oct 21 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Tue Sep 01 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.3.1.19980903

* Mon Jul 13 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.3.0

* Thu Jun 11 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Added pt_BR translations

* Thu May 07 1998 Prospector System <bugs@redhat.com>
updated to 1.3.0
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Mon Apr 06 1998 Erik Troan <ewt@redhat.com>
- updated to svgalib 1.2.13
- uses a build root

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- removed Mach64 from configuration, as the driver does not work

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

%description
SVGAlib is a library which allows applications to use full screen
graphics on a variety of hardware platforms. Many games and utilities
are avaiable which take advantage of SVGAlib for graphics access, as
it is more suitable for machines with little memory then X Windows is.

%description -l pt_BR
SVGAlib é uma biblioteca que permite a aplicações usar gráficos
de tela cheia em uma variedade de plataformas de hardware. Muitos
jogos e utilitários são disponibilizados para usar a SVGAlib para
acesso a gráficos, pois ele é mais indicado em máquinas com pouca
memória para rodar um sistema X Window.

%description -l es
SVGAlib es una biblioteca que permite a las aplicaciones usar
gráficos de pantalla llena en una variedad de plataformas de
hardware. Muchos juegos y utilitarios son puestos a disposición
para usar la SVGAlib para acceso a gráficos, pues es más indicado
en máquinas con poca memoria para ejecutar un sistema X Window.

%package devel
Summary: development libraries and include files for [S]VGA graphics
Summary(pt_BR): Bibliotecas de desenvolvimento e arquivos de inclusão para gráficos [S]VGA
Summary(es): Bibliotecas de desarrollo y archivos de inclusión para gráficos [S]VGA
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: svgalib
Summary(de): Entwicklungs-Libraries und INCLUDE-Dateien für (S)VGA-Grafik. 
Summary(fr): Bibliothèques et en-têtes de développement pour graphiques [S]VGA.
Summary(tr): [S]VGA grafikleri için geliþtirme kitaplýklarý ve baþlýk dosyalarý

%description devel
These are the libraries and header files that are needed to build programs
which use SVGAlib. SVGAlib allows programs to use full screen graphics
on a variety of hardware platforms and without the overhead X requires.

%description -l pt_BR devel
Estas são as bibliotecas e arquivos de inclusão que são necessários
para construir programas que usam SVGAlib. SVGAlib permite que
programas usem gráficos de tela cheia em uma variedade de plataformas
de hardware sem o overhead do X.

%description -l es devel
Estas son las bibliotecas y archivos de inclusión que son necesarios
para construir programas que usan SVGAlib. Permite que los programas
usen gráficos de pantalla llena en una variedad de plataformas de
hardware sin el overhead del X.

%description -l de devel
Dies sind die Libraries und Header-Dateien, die zum Erstellen von Programmen
erforderlich sind, die SVGAlib verwenden. Mit SVGAlib können Programme
Vollbildgrafiken auf einer Reihe von Plattformen verwenden, ohne den von X
erforderlichen Overhead.

%description -l de
SVGAlib ist eine Library, die es Applikationen gestattet, auf einer
Reihe von Plattformen Vollbild-Grafiken  zu benutzen. Viele Games
und Utilities nutzen diese Library für den Grafikzugriff, da sie 
für Maschinen mit wenig Speicher besser geeignet ist als X-Windows.

%description -l fr devel
Bibliothèques et en-têtes pour construire des programmes utilisant SVGAlib.
SVGAlib permet au programmes d'utiliser des graphiques plein écran sur une
grande variété de plates-formes matérielles et sans le surcoût qu'entraîne X.

%description -l tr devel
Bu paket, SVGAlib kitaplýðýný kullanan programlar geliþtirmek için gereken
baþlýk dosyalarýný ve statik kitaplýklarý içerir.

%description -l tr
SVGAlib, deðiþik donaným platformlarý üzerinde, uygulamalarýn tam ekran
çizim kullanmalarýný saðlayan bir kitaplýktýr. Az bellekli makinalar için
X Windows'tan daha uygun olmasýnýn yanýsýra, pek çok oyun ve yardýmcý
programlar çizim eriþimi için bu kitaplýðý kullanýr.

%description -l tr
SVGAlib é uma biblioteca que permite a aplicações usar gráficos de
tela cheia em uma variedade de plataformas de hardware. Muitos
jogos e utilitários são disponibilizados para usar a SVGAlib para
acesso a gráficos, pois ele é mais indicado em máquinas com
pouca memória para rodar um sistema X Window.

%description -l tr devel
Estas são as bibliotecas e arquivos de inclusão que são necessários para
construir programas que usam SVGAlib. SVGAlib permite que programas usem
gráficos de tela cheia em uma variedade de plataformas de hardware sem
o overhead do X.

%prep
%setup -q
%patch -p1 -b .config
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%build
make static shared

#%clean
#rm -fr $RPM_BUILD_ROOT

%install
export PATH=/sbin:$PATH
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/vga
mkdir -p $RPM_BUILD_ROOT/usr/include
mkdir -p $RPM_BUILD_ROOT/usr/man
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man3
mkdir -p $RPM_BUILD_ROOT/usr/man/man6
mkdir -p $RPM_BUILD_ROOT/usr/man/man7
make INSTALL_PREFIX="$RPM_BUILD_ROOT" install installsharedlib

strip $RPM_BUILD_ROOT/usr/bin/restorefont
strip $RPM_BUILD_ROOT/usr/bin/restorepalette
strip $RPM_BUILD_ROOT/usr/bin/dumpreg
strip $RPM_BUILD_ROOT/usr/bin/restoretextmode

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%config /etc/vga/libvga.config
%config /etc/vga/libvga.et4000
%config /etc/vga/libvga.et6000

/usr/bin/restorefont
/usr/bin/restorepalette
/usr/bin/dumpreg
/usr/bin/restoretextmode
/usr/bin/textmode
/usr/bin/savetextmode

%doc doc/*

/usr/lib/libvga.so.%{PACKAGE_VERSION}
/usr/lib/libvgagl.so.%{PACKAGE_VERSION}

%files devel
/usr/include/vga.h
/usr/include/vgakeyboard.h
/usr/include/vgamouse.h
/usr/include/vgagl.h
/usr/lib/libvga.a
/usr/lib/libvgagl.a
/usr/lib/libvga.so
/usr/lib/libvgagl.so
