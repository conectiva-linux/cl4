Summary: colour tty yahtzee
Summary(pt_BR): Yahtzee colorido modo texto
Summary(es): Yahtzee colorido modo texto
Name: colour-yahtzee
Version: 1.0
Release: 14cl
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://sunsite.unc.edu/pub/Linux/games/strategy/colour-yahtzee.tgz
Source1: colour-yahtzee.wmconfig
Patch: colour-yahtzee-minor.patch
BuildRoot: /var/tmp/colour-yahtzee-root
Summary(de): Farb-tty-Yahtzee
Summary(fr): yahtzee pour terminal couleur.
Summary(tr): Renkli metin ekranda yahtzee

%description
This is a terminal mode version of the popular game, yahtzee.  
It is a dice and board game.

%description -l pt_BR
Esta é uma versão em modo terminal do popular jogo yahtzee. Ele é
um jogo de dado e tabuleiro.

%description -l es
Esta es una versión en modo terminal del popular juego yahtzee. Es
un juego de dados y tablero.

%description -l de
Dies ist eine Terminalmodus-Version des beliebten Yahtzee, eines Würfel- 
und Brettspiels. 

%description -l fr
Version en mode texte du célèbre jeu de dés et de plateau, yahtzee. 

%description -l tr
Sevilen yahtzee oyununun metin ekran sürümü. Zarla oynanan bir oyundur.

%prep
%setup -q -n yahtzee
%patch -p1

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/games

install -m 755 -s yahtzee $RPM_BUILD_ROOT/usr/games

install -m 644 $RPM_SOURCE_DIR/colour-yahtzee.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/colour-yahtzee

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/games/yahtzee

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- updated src url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
