Name: rgXnetchess
Release: 7cl
Copyright: Free Software
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Version: 1.0
Summary: A network chess program
Summary(pt_BR): Xadrez para jogar em rede
Summary(es): Ajedrez para jugar en red
Source0: http://www.uni-jena.de/allgpsy/rg/rgXnetchess-1.0.tgz
Source1: rgXnetchess.wmconfig
Source800: rgXnetchess-wmconfig.i18n.tgz
URL: http://www.uni-jena.de/allgpsy/rg/chess.html
Patch: rgXnetchess-1.0.i18n.patch.gz
Patch1: rgXnetchess-makefile.patch
Patch2: rgXnetchess-egcs.patch
BuildRoot: /var/tmp/chess

%description
This is a network chess program. (You wouldn't have guessed it.) It is
designed to take away the burden of connecting to a chess server and
figuring out where and who the person is you want to play with. If you
regu- larly play chess against the same person over the net you will love
this program. It has a self explaining design with buttons for resigning,
offering draw and quitting and allows chatting.
The program knows all the rules of chess and detects mate and stalemate
and it has time control.

%description -l pt_BR
Este é um programa para jogar xadrez em rede local ou pela Internet.
Se você costuma jogar xadrez em rede freqüentemente com a mesma pessoa,
você vai adorar este programa, que não necessita de um servidor de
xadrez.
O programa conhece todas as regras do xadrez e detecta cheque-mate,
mate perpétuo e tem controle de tempo.

%description -l es
Este es un programa para jugar ajedrez en red local o por Internet.
Si tienes la costumbre de jugar ajedrez en red, frecuentemente con
la misma persona, vas adorar este programa, que no necesita de un
servidor de ajedrez.  El programa conoce todas las reglas del ajedrez
y detecta jeque mate, mate perpetuo y tiene control de tiempo.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with qt 1.44

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- added Group, Summary and %description translations

* Fri Nov 27 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Sep 14 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- first release with i18n patch

%prep
%setup -n rgXnetchess
%patch -p1
%patch1 -p0
%patch2 -p1

%build
CC=egcs FLAGS="-O3 -I/usr/include/qt -DENABLE_NLS" make

%install
ROOT=$RPM_BUILD_ROOT make install

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
install -m644 $RPM_SOURCE_DIR/rgXnetchess.wmconfig \
        $RPM_BUILD_ROOT/etc/X11/wmconfig/rgXnetchess




tar xvfpz $RPM_SOURCE_DIR/rgXnetchess-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%defattr(-,root,root)
%doc README
%dir /usr/X11R6/bin/chess
/usr/share/locale/pt_BR/LC_MESSAGES/chess.mo
%config /etc/X11/wmconfig/rgXnetchess
