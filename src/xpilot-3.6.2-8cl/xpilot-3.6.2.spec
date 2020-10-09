Summary: arcade style flying game
Summary(pt_BR): Jogo de v�o no estilo arcade
Summary(es): Juego de vuelo en estilo arcade
Name: xpilot
Version: 3.6.2
Release: 8cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
# was .gz
Source: ftp://ftp.cs.uit.no/pub/games/xpilot/xpilot-3.6.2.tar.bz2
Source800: xpilot-wmconfig.i18n.tgz
Url: http://www.cs.uit.no/XPilot/
Patch: xpilot-3.6.1-config.patch
Exclusivearch: i386 sparc
BuildRoot: /var/tmp/xpilot-root
Summary(de): Ein Flieger-Game im Arkadenstil
Summary(fr): Jeu de pilotage style arcade.
Summary(tr): U�u� oyunu

%description
xpilot is a fast-paced action game with multiplayer networking
capabilities that make it full of hours of enjoyment.  The basic
object of them game is to kill and fly - need more be said?

%description -l pt_BR
xpilot � um jogo de a��o que permite diversos jogadores em rede. Isto
torna-o �timo para horas de divers�o. O objetivo b�sico do jogo �
voar e matar - precisa dizer mais?

%description -l es
xpilot es un juego de aci�n que permite diversos jugadores en
red. Esto le hace �ptimo para horas de diversi�n. El objetivo b�sico
del juego es volar y matar - �Hace falta decir algo m�s?

%description -l de
xpilot ist ein schnelles Actionspiel mit Mehrspieleroption �ber ein
Netzwerk. Die Hauptaufgabe des Fliegens ist Abschie�en und Fliegen.
Noch Fragen?

%description -l fr
xpilot est un jeu d'action un jeu d'action rapide avec la possibilit�
de jouer � plusieurs joeurs en r�seau qui garantissent des heures
de jeu passionnantes. Le but principal est de s'envoler et de tuer
besoin d'en dire plus ?.

%description -l tr
xpilot, a� �zerinden birden fazla oyuncuyu destekleyen h�zl� bir macera
oyunu. Yapman�z gereken, u�mak ve sa� kalmak.

%prep
%setup -q
%patch -p1

%build
xmkmf
make Makefiles
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpilot <<EOF
#xpilot name "xpilot (requer servidor)"
#xpilot description "Jogo Arcade de V�o/Tiro"
#xpilot group Jogos/V�deo
#xpilot exec "xterm -e xpilot -join &"
#EOF
#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpilots <<EOF
#xpilots name "xpilots (servidor)"
#xpilots description "Jogo Arcade de V�o/Tiro"
#xpilots group Jogos/V�deo
#xpilots exec "xterm -e xpilots &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xpilot-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE README.msub 
%doc doc
/usr/X11R6/bin/xpilots
/usr/X11R6/bin/xpilot
/usr/X11R6/bin/xp-replay
/usr/X11R6/lib/X11/xpilot
/usr/X11R6/man/man1/xpilot.1x
/usr/X11R6/man/man1/xpilots.1x
/usr/X11R6/man/man1/xp-replay.1x
%config /etc/X11/wmconfig/xpilot
%config /etc/X11/wmconfig/xpilots

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- add sparc
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Nov  3 1997 Otto Hammersmith <otto@redhat.com>
- made exlusivearch to i386

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
