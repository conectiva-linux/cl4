Summary: falling blocks game similar to xjewels or t*tris for curses
Summary(pt_BR): Jogo de blocos que caem similar ao xjewels ou tetris para curses
Summary(es): Juego de bloques que caen, similar al xjewels o tetris para curses
Name: trojka
Version: 1.1
Release: 15cl
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: sunsite.unc.edu:/pub/Linux/games/arcade/tetris/trojka.tgz
Patch0: trojka-fsstnd.patch
Patch1: trojka-misc.patch
Patch2: trojka-glibc.patch
BuildRoot: /var/tmp/trojka-root
Icon: trojka.gif
Summary(de): Spiel mit fallenden Steinen, ähnlich xjewels oder t*tris für curses
Summary(fr): Jeu de blocs similaire à xjewels ou t*tris pour curse
Summary(tr): xjewels ve t*tris'e benzer, metin ekranlý, düþen blok oyunu

%description
The aim of this game is to control and to place the falling blocks, so
that at least three blocks horizontally or diagonally, or both, have
matching patterns. This sequence is then removed, and the above blocks
will coll you reach the top of the screen, the game is finished.

%description -l pt_BR
O objetivo deste jogo é controlar e arrumar os blocos que caem, para
que ao menos três blocos de mesmo modelo se encaixem horizontalmente
ou diagonalmente, separadamente ou juntos. Esta seqüência é então
removida, e quando os blocos acima alcançarem o topo da tela,
o jogo termina.

%description -l es
El objetivo de este juego es controlar y arreglar los bloques que
caen, para que por lo menos tres bloques del mismo modelo se encajen
horizontalmente o diagonalmente, separados o juntos. Entonces,
esta secuencia se elimina, y cuando los bloques arriba alcancen lo
alto de la pantalla, el juego se termina.

%description -l de
Ziel dieses Spiels ist es, die herunterfallenden Blöcke zu steuern 
und so zu plazieren, daß mindestens drei Blöcke in waagrechter Richtung 
oder diagonal (oder in beiden Richtungen) passende Muster aufweisen. 
Diese Folge wird dann entfernt. Wenn der obere Bildschirmrand erreicht 
ist, ist das Spiel zu Ende. 

%description -l fr
Le but de ce jeu est de contrôler et de placer les blocs qui tombent
de façon à ce qu'au moins trois blocs aient le même motif en horizontal,
en vertical ou les deux. Cette suite est alors ôtée et les blocs du dessus
tombent. Le jeu est fini lorsque le haut de l'écran est atteint.

%description -l tr
Bu oyunun amacý, düþen bloklarý desenlerine göre üçlü sýralar oluþturacak
þekilde yerleþtirmektir.

%prep
%setup -q -n trojka
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS" linux

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{games,man/man6}
mkdir -p $RPM_BUILD_ROOT/var/lib/games

install -m755 -s trojka $RPM_BUILD_ROOT/usr/games
install -m644 trojka.6 $RPM_BUILD_ROOT/usr/man/man6/trojka.6
cp /dev/null $RPM_BUILD_ROOT/var/lib/games/trojka.scores
chmod 666 $RPM_BUILD_ROOT/var/lib/games/trojka.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/games/trojka
/usr/man/man6/trojka.6
/var/lib/games/trojka.scores

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Nov 04 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- fixed path to source

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
