Summary: PacMan type game for X
Summary(pt_BR): Jogo tipo PacMan para X
Summary(es): Juego tipo PacMan para X
Name: xchomp
Version: 1.0
Release: 13cl
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://sunsite.unc.edu:/pub/Linux/games/x11/video/xchomp-linux.tar.z
Source2: xchomp.wmconfig
Source800: xchomp-wmconfig.i18n.tgz
Patch: xchomp-delay.patch
Patch1: xchomp-make.patch
Icon: xchomp.gif
Buildroot: /var/tmp/xchomp-root
Summary(de): Spiel im PacMan-Stil für X 
Summary(fr): Jeu de type PacMan pour X
Summary(tr): PacMan tarzý bilgisayar oyunu


%description
The classic arcade action game comes to your screen with xchomp, the
PacMan-like game. Not as extensive as the original game, but still lots of
fun!

%description -l pt_BR
O clássico PacMan chega a sua tela com xchomp. Não tão extenso
quanto o jogo original, mas ainda muito legal!

%description -l es
El clásico PacMan llega a su pantalla con xchomp. No tan extenso
como el juego original, pero aún ¡muy genial!

%description -l de
Mit xchomp kommt ein Arcade-Klassiker auf Ihren Bildschirm, hat
Ähnlichkeiten mit PacMan. Nicht so umfangreich wie das Original, 
macht aber trotzdem noch viel Spaß!

%description -l fr
Le classique du jeu d'action sur arcade arrive sur votre ecran avec xchomp,
le clone du jeu PacMan.Il n'est certes pas aussi complet que l'original, mais
vous promet tout de meme de bon moments.

%description -l tr
xchomp, PacMan'in (dobiþko) Linux'a uyarlanmýþ hali.

%prep
%setup -q -n xchomp
%patch -p1
%patch1 -p1 -b .makepatch

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 755 -s xchomp $RPM_BUILD_ROOT/usr/X11R6/bin/xchomp



tar xvfpz $RPM_SOURCE_DIR/xchomp-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) %doc README README.linux
%attr(-,root,root) /usr/X11R6/bin/xchomp
%attr(-,root,root) /etc/X11/wmconfig/xchomp

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- wmconfig.pt_BR

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- built for 5.2

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Nov 06 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- buildroot'd and %attr'd
- added wmconfig entry
- uses RPM_OPT_FLAGS
