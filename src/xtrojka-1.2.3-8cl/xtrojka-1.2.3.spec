Summary: falling blocks game
Summary(pt_BR): Jogo de blocos caindo
Summary(es): Juego de bloques cayendo
Name: xtrojka
Version: 1.2.3
Release: 8cl
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/xtrojka123.tar.gz
Source800: xtrojka-wmconfig.i18n.tgz
Patch: xtrojka-1.2.3-make.patch
Icon: xtrojka.gif
BuildRoot: /var/tmp/xtrojka-root
Summary(de): Spiel mit fallenden Steinen
Summary(fr): Jeu de blocs qui tombent
Summary(tr): Düþen bloklarý yerleþtirme oyunu

%description
Similar to xjewels or tetris, this game presents you with the
challenge of keeping the playing area clear of falling blocks.

A variation on the addictive classic.

%description -l pt_BR
Similar ao xjewels ou tetris, este jogo o desafia a manter a área
de jogo livre de blocos que caem. Uma variação do clássico tetris
que vicia do mesmo jeito.

%description -l es
Similar al xjewels o tetris, este juego te desafía a mantener el
área de juego libre de bloques que caen. Una variación del clásico
tetris que vicia del mismo modo.

%description -l de
Ähnlich wie bei xjewels oder tetris, müssen Sie in diesem Spiel
die Spielfläche von fallenden Blöcken freihalten.

Eine Variation des süchtigmachenden Klassikers.

%description -l fr
Ce jeu est similaire à xjewels ou tetris, il faut supprimer les
blocs qui tombent dans la surface de jeu.

Un variation du jeu classique.

%description -l tr
xjewels ve tetris'e benzer þekilde, düþen bloklarý uygun þekilde yerleþtirmeye
yönelik bir oyun.

%prep
%setup -q -n xtrojka123
%patch -p1

%build
cp XTrojka.uk XTrojka
./resgen
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man6}
mkdir -p $RPM_BUILD_ROOT/var/lib/games

make	TARGET_DIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
	MANDIR=$RPM_BUILD_ROOT/usr/X11R6/man/man6 \
	HSFILE=$RPM_BUILD_ROOT/var/lib/games/xtrojka.score \
	install
##install -m 644 xtrojka.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xtrojka.6
##cp /dev/null $RPM_BUILD_ROOT/var/lib/games/xtrojka.score
chmod 0666 $RPM_BUILD_ROOT/var/lib/games/xtrojka.score
strip $RPM_BUILD_ROOT/usr/X11R6/bin/xtrojka

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xtrojka <<EOF
#xtrojka name "xtrojka"
#xtrojka description "xtrojka"
#xtrojka group Jogos/Vídeo
#xtrojka exec "xtrojka &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xtrojka-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xtrojka
/usr/X11R6/man/man6/xtrojka.6
%config /var/lib/games/xtrojka.score
%config /etc/X11/wmconfig/xtrojka

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
