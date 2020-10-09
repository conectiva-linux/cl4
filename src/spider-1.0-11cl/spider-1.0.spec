Summary: X11 implementation of Spider card game
Summary(pt_BR): Implementa��o X11 do jogo de cartas Spider
Summary(es): Implementaci�n X11 del juego de cartas Spider
Name: spider
Version: 1.0
Release: 11cl
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
# was .Z
Source: ftp://sunsite.unc.edu/pub/Linux/games/solitaires/spider.tar.bz2
Source1: spider.wmconfig
Source800: spider-wmconfig.i18n.tgz
BuildRoot: /var/tmp/spider-root
Summary(de): X11-Implementierung des Kartenspiels \"Spider\"
Summary(fr): Implantation X11 du jeu de cartes Spider
Summary(tr): Spider ka��t oyununun X11 ger�ekle�tirmesi

%description
spider is a particularly challenging double-deck solitaire.  Unlike
most solitaires, it provides extraordinary opportunities for the
skillful player to overcome bad luck in the deal by means of careful
analysis and complex manipulations.

%description -l pt_BR
spider � particularmente um derivado de paci�ncia com duplo baralho.
Diferentemente da maioria dos "paci�ncias", ele oferece oportunidades
extraordin�rias para a habilidade do jogador para cobrir o azar nas
apostas por meio de uma cuidadosa an�lise e manipula��es complexas.

%description -l es
spider es particularmente un derivado del solitario con doble
baraja.  Diferentemente de la mayor�a de los "solitarios", nos
ofrece oportunidades extraordinarias para la habilidad del jugador
para cubrir el azar en las apuestas, por medio de una cuidadosa
an�lisis y a trav�s de manipulaciones complejas.

%description -l de
spider ist ein ganz besonders anspruchsvolles Solitaire mit doppelten 
Karten. Anders als andere Solitaires bietet es dem geschickten Spieler
hervorragende M�glichkeiten, durch sorgf�ltige Analyse und komplexe 
Manipulationen auch ung�nstige Situationen zu meistern. 

%description -l fr
spider est un jeu de solitaire qui, � la diff�rence de la plupart des
autres solitaires, offre la possibilit� au joueur exp�riment� de surmonter
une mauvaise donne par une analyse pouss�e et des manipulations complexes.

%description -l tr
spider iki desteli fal oyunudur. Di�er fal oyunlar�n�n aksine, dikkatli
��z�mleme ve karma��k kullan�mlarla iyi bir oyuncunun ka��tlar�n
da��t�m�ndaki k�t� �ans� yenmesini sa�layacak olanaklar sunar.

%prep
%setup -q -n spider

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
cp $RPM_SOURCE_DIR/spider.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/spider


tar xvfpz $RPM_SOURCE_DIR/spider-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/spider
/usr/X11R6/man/man1/spider.1x
/etc/X11/wmconfig/spider

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- included spider.wmconfig in portuguese

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
