Summary: backgammon game
Summary(pt_BR): Jogo de gam�o
Summary(es): Juego de gammon
Name: xgammon
Version: 0.98
Release: 16cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source:  sunsite.unc.edu:/pub/Linux/X11/games/strategy/xgammon-0.98.tar.gz
Source800: xgammon-wmconfig.i18n.tgz
Patch0: xgammon-0.98-config.patch
Patch1: xgammon-0.98-dirent.patch
Icon: xgammon.gif
BuildRoot: /var/tmp/xgammon-root
Summary(de): Backgammon-Spiel
Summary(fr): Jeu de Backgammon
Summary(tr): Tavla oyunu

%description
This version of the popular card/board game 'backgammon' allows you to
play either against the computer or another human.

%description -l pt_BR
Esta vers�o do popular jogo gam�o permite jogar contra o computador
ou contra outro humano.

%description -l es
Esta versi�n del popular juego backgammon permite jugar contra el
ordenador o contra otro humano.

%description -l de
Diese Version des beliebten Karten-/Brettspiels BACKGAMMON gestattet
es Ihnen, gegen den Computer oder einen menschlichen Partner zu spielen. 

%description -l fr
Cette version du c�l�bre jeu de carte/plateau � backgammon � vous permet
de jouer contre l'ordinateur ou un autre joueur humain.

%description -l tr
Bizde en �ok bilinen oyunlardan biri olan tavla'n�n Linux'a uyarlanm��
hali. �ster iki ki�i, ister bilgisayar ile kar��l�kl� oynayabilirsiniz.


%prep
%setup -q -c
%patch0 -p1 -b .rhconfig
%patch1 -p1

%build
export PATH=$PATH:.
xmkmf
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man6
install -m 644 xgammon.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xgammon.6

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xgammon <<EOF
#xgammon name "xgammon"
#xgammon description "Gam�o"
#xgammon group Jogos/Estrat�gia
#xgammon exec "xgammon &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xgammon-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xgammon
%config /usr/X11R6/lib/X11/app-defaults/XGammon
/usr/X11R6/lib/X11/xgammon
/usr/X11R6/man/man6/xgammon.6
%config /etc/X11/wmconfig/xgammon

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
