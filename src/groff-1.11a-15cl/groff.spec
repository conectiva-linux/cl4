Summary: GNU groff text formatting package
Summary(pt_BR): Pacote groff GNU - formatador de texto
Summary(es): Paquete groff GNU - formateador de texto
Name: groff
Version: 1.11a
Release: 15cl
Copyright: GPL
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
#Source0: ftp://prep.ai.mit.edu/pub/gnu/groff-1.11a.tar.gz
# recompactado com o bzip2
Source0: ftp://prep.ai.mit.edu/pub/gnu/groff-1.11a.tar.bz2
Source1: troff-to-ps.fpi
Source2: hyphen.pt
Patch0:  groff-1.11-make.patch
Patch1: groff-1.11-safer.patch
Patch2: groff-1.11-bash2.patch
Patch3: groff-1.11-hyphen.patch
Patch4: groff-1.11-glibc21.patch
Requires: mktemp
Buildroot: /var/tmp/groff-root
Obsoletes: groff-tools
Summary(de): GNU groff-Textformatierungspaket
Summary(fr): Paquetage de formatage de texte groff de GNU
Summary(tr): GNU groff metin biçemleme paketi

%changelog
* Fri May 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added glibc 2.1 patch for xditview

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- added hyphen.pt (and hyphen.br symlink).
  Thanks to Carlos A M dos Santos <casantos@inf.ufrgs.br>
  hyphen continues disabled...

* Tue Mar 02 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- groff-extras package: mainly perl scripts

* Tue Dec 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17

* Wed Nov 04 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 19 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- disable default us hyphenation
- added pt_BR translations

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- fix makefiles to work with bash2

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use g++ for C++ code

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- manhattan and buildroot

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- made xdefaults file a config file

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- split perl components into separate subpackage

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated to 1.11a
- added safe troff-to-ps.fpi

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- removed troff-to-ps.fpi for security reasons.

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%description
The groff text formatting system can be used to create professional
looking documents on both paper and a computer screen.  All the man
pages are processed with groff, so you'll need this package to read
man pages.

%description -l pt_BR
O pacote contém o programa gxditview, o qual pode ser usado para
formatar e visualizar documentos groff em X Window. Por exemplo,
páginas "man" podem ser lidas usando gxditview.

%description -l es
El paquete contiene el programa gxditview, que se puede usar para
formatear y visualizar documentos groff en X window. Por ejemplo,
páginas "man" se pueden leer utilizando gxditview.

%package gxditview
Summary: GNU groff X previewer
Summary(pt_BR): Groff GNU para X
Summary(es): Groff GNU para X
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Summary(de): GNU groff-X-Previewer
Summary(fr): Le visualiseur de fichier groff de GNU, sous X.
Summary(tr): GNU groff X görüntüleyici

%description gxditview
The package contains the gxditview program, which can be used to
format and view groff documents in X Windows.  For example, man
pages can be read using gxditview.

%description -l pt_BR gxditview
Este pacote contém o programa gxditview, que pode ser usado para
formatar e visualizar documentos no X Window. Por exemplo: páginas
man podem ser lidas usando o gxditview.

%description -l es gxditview
Este paquete contiene el programa gxditview, que se puede usar
para formatear y visualizar documentos en X window. Por ejemplo:
páginas man se las puede leer utilizando gxditview.

%description -l de gxditview
Das Paket enthält das gxditview-Programm, das zum Formatieren und 
Anzeigen von groff-Dokumenten in X-Windows benutzt wird. So lassen 
sich beispielsweise auch die man-Seiten mit gxditview einsehen. 

%description -l de
Das Textformatiersystem groff wird zum Erstellen professioneller
Dokumente auf Papier und Bildschirm verwendet. Alle man-Seiten
werden mit groff verarbeitet. Das Paket wird zum Lesen von man-
Seiten benötigt.

%description -l fr gxditview
Ce paquetage contient le programme gxditview, qui peut servir à
formater et viusaliser les documents groff sous X Window. Les pages
peuvent, par exemple, être lues avec gxditview.

%description -l fr
Le système de formatage de texte groff peut être utilisé pour créer
des documents d'aspect professionnel sur papier et à l'écran. Toutes
les pages man sont traitées avec groff, vous avez donc besoin de ce
paquetage pour les visualiser.

%description -l tr gxditview
Bu paket groff belgelerini görüntüleyip deðiþtirmeye yarayan gxditview
programýný içerir. Örneðin man sayfalarý gxditview kullanýlarak
okunabilir.

%description -l tr
groff metin biçemleme sistemi kaðýt veya bilgisayar ekraný üzerinde
profesyonel görünüme sahip belgeler yaratmaya yarar. Bütün kýlavuz (man)
sayfalarý groff ile hazýrlanmýþtýr. man sayfalarýný okuyabilmek için groff
paketine gereksiniminiz olacaktýr.

%package extras
Summary: Extra groff scripts
Summary(pt_BR): Scripts groff extras
Summary(es): Scripts groff extras
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Requires: perl

%description extras
The package contains some extra scripts, mainly in perl.

%description -l pt_BR extras
Este pacote contém alguns scripts extras, principalmente em perl.

%description -l es extras
Este paquete contiene scripts extras, principalmente en perl.

%prep
%setup -n groff-1.11
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
PATH=$PATH:/usr/X11R6/bin
CXX='g++' CC='gcc' CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr
make
cd xditview
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
PATH=$PATH:/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr
make install prefix=$RPM_BUILD_ROOT/usr
cd xditview
make DESTDIR=$RPM_BUILD_ROOT install install.man
strip $RPM_BUILD_ROOT/usr/bin/* || :

ln -s tmac.s	$RPM_BUILD_ROOT/usr/lib/groff/tmac/tmac.gs
ln -s tmac.mse $RPM_BUILD_ROOT/usr/lib/groff/tmac/tmac.gmse
ln -s tmac.m	$RPM_BUILD_ROOT/usr/lib/groff/tmac/tmac.gm
ln -s troff	$RPM_BUILD_ROOT/usr/bin/gtroff
ln -s tbl	$RPM_BUILD_ROOT/usr/bin/gtbl
ln -s pic	$RPM_BUILD_ROOT/usr/bin/gpic
ln -s eqn	$RPM_BUILD_ROOT/usr/bin/geqn
ln -s neqn	$RPM_BUILD_ROOT/usr/bin/gneqn
ln -s refer	$RPM_BUILD_ROOT/usr/bin/grefer
ln -s lookbib	$RPM_BUILD_ROOT/usr/bin/glookbib
ln -s indxbib	$RPM_BUILD_ROOT/usr/bin/gindxbib
ln -s soelim	$RPM_BUILD_ROOT/usr/bin/gsoelim
ln -s nroff	$RPM_BUILD_ROOT/usr/bin/gnroff
ln -s eqn.1	$RPM_BUILD_ROOT/usr/man/man1/geqn.1
ln -s indxbib.1 $RPM_BUILD_ROOT/usr/man/man1/gindxbib.1
ln -s lookbib.1 $RPM_BUILD_ROOT/usr/man/man1/glookbib.1
ln -s nroff.1 	$RPM_BUILD_ROOT/usr/man/man1/gnroff.1
ln -s pic.1 	$RPM_BUILD_ROOT/usr/man/man1/gpic.1
ln -s refer.1 	$RPM_BUILD_ROOT/usr/man/man1/grefer.1
ln -s soelim.1 $RPM_BUILD_ROOT/usr/man/man1/gsoelim.1
ln -s tbl.1 	$RPM_BUILD_ROOT/usr/man/man1/gtbl.1
ln -s troff.1 	$RPM_BUILD_ROOT/usr/man/man1/gtroff.1
mkdir -p $RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters
install -m755 $RPM_SOURCE_DIR/troff-to-ps.fpi \
	$RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters

install -m744 $RPM_SOURCE_DIR/hyphen.pt $RPM_BUILD_ROOT/usr/lib/groff/tmac/
ln -s hyphen.pt $RPM_BUILD_ROOT/usr/lib/groff/tmac/hyphen.br

cd $RPM_BUILD_ROOT
echo "%dir /usr/lib/groff" > $RPM_BUILD_DIR/file.list.groff
find . -type f | grep -v "grog\|afm\|^\.\/usr\/X11R6" | sed 's/^\.//g' >> $RPM_BUILD_DIR/file.list.groff
find . -type l | grep -v "grog\|afm\|^\.\/usr\/X11R6" | sed 's/^\.//g' >> $RPM_BUILD_DIR/file.list.groff

find . -type f | grep "grog\|afm\" | grep -v "^\.\/usr\/X11R6" | sed 's/^\.//g' > $RPM_BUILD_DIR/file.list.groff-extras
find . -type l | grep "grog\|afm\" | grep -v "^\.\/usr\/X11R6" | sed 's/^\.//g' >> $RPM_BUILD_DIR/file.list.groff-extras

%files -f ../file.list.groff

%files extras -f ../file.list.groff-extras

%files gxditview
/usr/X11R6/bin/gxditview
%config /usr/X11R6/lib/X11/app-defaults/GXditview
/usr/X11R6/man/man1/gxditview.1x

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.groff*
