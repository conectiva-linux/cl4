Summary: Computer chess program
Summary(pt_BR): Jogo de xadrez da GNU
Summary(es): Juego de ajedrez de la GNU
Name: gnuchess
Version: 4.0.pl77
Release: 9cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Icon: xchess.gif
# was .gz
Source: prep.ai.mit.edu:/pub/gnu/gnuchess-4.0.pl77.tar.bz2
Patch0: gnuchess-4.0.pl75-fsstnd.patch
Patch1: gnuchess-4.0.pl77-ncurses.patch
Buildroot: /var/tmp/chess-root
Summary(de): Computerschachprogramm
Summary(fr): Jeu d'échecs.
Summary(tr): Bilgisayar satranç oyunu

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Nov 05 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri May 01 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>

- built against new ncurses

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>

- BuildRoot'ed

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>

- built against glibc

%description
This is the famous GNU chess program.  It is text based, but 
can be used in conjunction with xboard to play X based chess.

%description -l pt_BR
Este é o famoso programa de xadrez da GNU. É baseado em texto, mas
pode ser usado em conjunção com xboard para jogar xadrez baseado
em X.

%description -l es
Este es el famoso programa de ajedrez de GNU. Está basado en texto,
pero puede ser usado en conjunción con xboard para jugar ajedrez
basado en X.

%description -l de
Das berühmte GNU-Schachprogramm. Es ist textorientiert, kann
aber mit 'xboard' verwendet werden, um X-orientiertes Schach zu spielen.

%description -l fr
Le fameux programme de jeu d'échecs de GNU. Il est en mode texte
mais peut être utilisé avec xboard pour y jouer sous X.

%description -l tr
Bu ünlü GNU satranç programýdýr. Metin ekranda çalýþýr ama xboard programý
ile birlikte kullanýlarak X altýnda da oynanabilir.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
cd src
rm -f config.status config.cache
./configure --prefix=/usr
make "CC=gcc $RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/games/gnuchess $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man6
cd src
make prefix=$RPM_BUILD_ROOT/usr install

cd $RPM_BUILD_ROOT
strip usr/bin/gnuchess usr/bin/gnuchessr usr/bin/gnuchessn
strip usr/bin/gnuchessx usr/bin/gnuchessc usr/bin/postprint
strip usr/bin/gnuan usr/bin/game

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/gnuchess
/usr/bin/gnuchessr
/usr/bin/gnuchessn
/usr/bin/gnuchessx
/usr/bin/gnuchessc
/usr/bin/postprint
/usr/bin/gnuan
/usr/bin/game
/usr/lib/games/gnuchess/gnuchess.lang
/usr/lib/games/gnuchess/eco.pgn
/usr/lib/games/gnuchess/gnuchess.data
/usr/lib/games/gnuchess/gnuchess.eco
/usr/man/man6/game.6
/usr/man/man6/gnuan.6
/usr/man/man6/gnuchess.6
/usr/man/man6/postprint.6
