Summary: Game like Sega's columns
Summary(pt_BR): Jogo semelhante ao Colunas do Sega
Summary(es): Juego semejante al Columnas del Sega
Name: xjewel
Version: 1.6
Release: 13cl
Copyright: MIT
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp.x.org:/R5contrib/xjewel-1.6.tar.z
Source800: xjewel-wmconfig.i18n.tgz
Patch0: xjewel-1.6-imake.patch
Patch1: xjewel-1.6-enhance.patch
Patch2: xjewel-1.6-nobr.patch
Icon: xjewel.gif
BuildRoot: /var/tmp/xjewel-root
Summary(de): Game von der Art von Segas COLUMNS 
Summary(fr): Jeu du style Columns de Sega
Summary(tr): Sega'nýn columns'una benzer oyun

%description
Jewel is a game much like Domain/Jewelbox which is a puzzle game like
Tetris.

It is played by controling the motion of blocks which continue to fall from
the top of the screen.  One can move them left and right, as well as
rotate the jewel segements.  The object is to get the most points before
the grim reaper ends the fun.

%description -l pt_BR
Jewel é um jogo muito mais parecido com Domain/Jewelbox do que um
jogo de quebra-cabeça como Tetris.
Ele é jogado controlando a movimentação de blocos que continuam a
cair do topo da sua tela. Pode-se movê-los para esquerda e direita,
assim como alterar sua rotação. O objetivo é conseguir mais pontos
até o "ceifeiro cruel" acabar com a diversão.

%description -l es
Jewel es un juego mucho más parecido con Domain/Jewelbox de que
un juego de rompecabezas, como el Tetris.  Se juega controlando
el movimiento de bloques que continúan a caer de lo más alto de
tu pantalla. Se puede moverlos para izquierda y derecha, así como
alterar su rotación. El objetivo es conseguir más puntos hasta que el
"segador cruel" acabe con la diversión.

%description -l de
Jewel hat große Ähnlichkeit mit Domain/Jewelbox, einem Puzzle-Game in 
der Tetris-Manier.
Die Aufgabe besteht darin, die Bewegung der Blöcke zu steuern, die vom 
oberen Bildschirmrand nach unten fallen. Man kann sie nach links und 
nach rechts bewegen und die Segmente drehen. Der Spieler versucht, 
möglichst viele Punkte einzuheimsen, bevor sein Lebensfaden 
abgezwackt wird.

%description -l fr
jewel est un jeu comme Domain/Jewelbox qui est un jeu de puzzle de style
Tetris.

On y joue en contrôlant le déplacement des blocs qui tombent du haut de
l'écran. On peut les déplacer à droite et à gauche et les faire tourner.
Le but est d'avoir le plus de points possible avant que la Faucheuse
n'y mette un terme.

%description -l tr
Jewel, Domain/Jewelbox ya da Tetris benzeri bir bulmaca oyunudur. Amaç düþen
bloklarý saða/sola çevirerek ya da döndürerek uygun biçimde yerleþtirmektir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/var/lib/games

make DESTDIR=$RPM_BUILD_ROOT install install.man

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xjewel <<EOF
#xjewel name "xjewel"
#xjewel description "Jogo Colunas"
#xjewel group Jogos/Vídeo
#xjewel exec "xjewel &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xjewel-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xjewel
%config /var/lib/games/xjewel.scores
/usr/X11R6/man/man1/xjewel.1x
%config /etc/X11/wmconfig/xjewel

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
