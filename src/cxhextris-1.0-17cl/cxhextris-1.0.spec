Summary: color X11 version of hextris 
Summary(pt_BR): Versão colorida X11 do jogo hextris
Summary(es): Versión colorida X11 del juego hextris
Name: cxhextris
Version: 1.0
Release: 17cl
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/cxhextris.tar.z
Source800: cxhextris-wmconfig.i18n.tgz
Patch0: cxhextris-config.patch
Patch1: cxhextris-axp.patch
Patch2: cxhextris-security.patch
Prereq: XFree86
BuildRoot: /var/tmp/cxhextris-root
Summary(de): Farbige X11-Version von Hextris
Summary(fr): Version X11 en couleurs d'hextris
Summary(tr): Düþen bloklarý yerleþtirme oyunu

%description
cxhextrix is a color version of the popular hextris.  Both are
a close of the popular T*tris video game, a game where one must
try to stack odd shaped blocks together perfectly.  This game
requires X Windows to work properly.

%description -l pt_BR
cxhextrix é uma versão colorida do popular hextris. Ambos são
semelhantes ao popular jogo de vídeo Tetris, um jogo onde deve-se
tentar encaixar perfeitamente blocos que caem. Este jogo requer X
Window para funcionar apropriadamente.

%description -l es
cxhextrix es una versión colorida del popular hextris. Ambos son
semejantes al popular juego de vídeo Tetris, un juego donde se
debe intentar encajar perfectamente bloques que caen. Este juego
requiere X Window para funcionar apropiadamente.

%description -l de
cxhextrix ist eine Farbversion des populären hextris, beides nahe 
Verwandte des klassischen T*tris Video-Games, bei dem unregelmäßig 
geformte Blöcke perfekt aufeinander gestapelt werden müssen. 
Voraussetzung ist, daß X-Windows korrekt funktioniert.

%description -l fr
cxhextrix est une version en couleurs du célèbre hextris. Tous deux
sont des clones du célèbre jeu vidéo T*tris, où l'on doit essayer
d'empiler parfaitement des blocs avec des formes curieuses. Ce jeu
nécessite X Window pour fonctionner correctement.

%description -l tr
cxhextrix, hextris'in renkli sürümüdür. Her ikisi de, garip þekilli bloklarýn
- arada boþluk býrakýlmadan - bir yýðýn haline getirilmeye çalýþýldýðý Tetris
oyununa benzer.

%prep
%setup -q -n cxhextris
%patch -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc
make FONTDIR=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts install.font

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/






tar xvfpz $RPM_SOURCE_DIR/cxhextris-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd /usr/X11R6/lib/X11/fonts/misc; /usr/X11R6/bin/mkfontdir)

%postun
(cd /usr/X11R6/lib/X11/fonts/misc; /usr/X11R6/bin/mkfontdir)

%files
%defattr(-,root,root)
%doc README README.Linux
%attr(755,games,games)	/usr/X11R6/bin/xhextris
/usr/X11R6/lib/X11/fonts/misc/hex20.pcf
%attr(-,games,games)	/var/lib/games/xhextris-scores
/etc/X11/wmconfig/cxhextris

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Mon Nov 30 1998 Marcelo Tossati <marcelo@conectiva.com>
- retirado suid bit do /usr/X11R6/bin/xhextris

* Sat Oct 24 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmconfig traduzido

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Tue Jun 09 1998 Mike Wangsmo <wanger@redhat.com>
- fixed the wmconfig entry

* Sat May  2 1998 Alan Cox <alan@redhat.com>
- buffer overrun fixed. General restructure to avoid running setuid except
  during the first moments of initialisation.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url
- added wmconfig entries

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
