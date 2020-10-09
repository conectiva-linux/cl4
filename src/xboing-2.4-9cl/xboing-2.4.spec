Summary: Breakout style video game
Summary(pt_BR): Jogo no estilo Breakout
Summary(es): Juego en estilo Breakout
Name: xboing
Version: 2.4
Release: 9cl
Copyright: MIT
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
#Source: ftp://ftp.x.org/pub/games/xboing2.4.tar.gz
# recompressed with bzip2
Source: ftp://ftp.x.org/pub/games/xboing2.4.tar.bz2
Source800: xboing-wmconfig.i18n.tgz
Patch0: xboing2.4.patch
Patch1: xboing-2.4.patch
Patch2: xboing-2.4-sparc.patch
Icon: xboing.gif
Url: http://www.catt.rmit.edu.au/xboing/xboing.html
BuildRoot: /var/tmp/xboing-root
Summary(de): Videogame a la Breakout
Summary(fr): Jeu vid�o du style Breakout
Summary(tr): Breakout tarz� bilgisayar oyunu

%description
xboing is an X-Windows game in the tradition of the classic 'Breakout'
arcade game. The object is to keep a ball bouncing on the bricks until
they break down. Even more fun comes in later levels when you have to
handle multiple balls and ball traps.

%description -l pt_BR
xboing � um jogo que segue a tradi��o do cl�ssico 'Breakout'. O
objetivo � manter uma bola "pulando" nos tijolos at� que eles se
quebrem. O melhor vem em n�veis mais adiantados quando voc� tem
que manipular m�ltiplas bolas e armadilhas.

%description -l es
xboing es un juego que sigue la tradici�n del cl�sico 'Breakout'. Su
objetivo es mantener una bola "saltando" en los ladrillos hasta que
se rompan. Lo mejor viene en niveles m�s adelantados cuando tienes
que manipular m�ltiples bolas y trampas.

%description -l de
xboing ist ein X-Windows-Spiel wie der Arcade-Klassiker 'Breakout'.
Sie m�ssen einen Ball auf den Steinen springen lassen, bis diese 
zerbr�ckeln. In sp�teren Levels m�ssen Sie mit mehreren B�llen
und Ballfallen rechnen.

%description -l tr
Klasik 'Breakout' oyununu hat�rlars�n�z. Xboing oynarken amac�n�z bir top
yard�m�yla t�m tu�lalar� k�rmak. �lerki d�zeylerde birden fazla top ortal�kta
dola�maya ba�lay�nca daha da �ok zevk al�yorsunuz.

%prep
%setup -q -n xboing
%patch -p1
%patch1 -p1
%patch2 -p1 -b .sparc

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{usr,var}/lib/games

make	DESTDIR=$RPM_BUILD_ROOT \
	XBOING_DIR=$RPM_BUILD_ROOT/usr/lib/games/xboing \
	HIGH_SCORE_FILE=$RPM_BUILD_ROOT/var/lib/games/xboing.score \
	install install.man

( cd $RPM_BUILD_ROOT
  mkdir -p ./etc/X11/wmconfig
#  cat > ./etc/X11/wmconfig/xboing <<EOF
#xboing name "xboing"
#xboing description "Jogo estilo Breakout"
#xboing group Jogos/V�deo
#xboing exec "xboing &"
#EOF
)



tar xvfpz $RPM_SOURCE_DIR/xboing-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/man/man1/xboing.1x
/usr/X11R6/bin/xboing
/usr/lib/games/xboing
%config /var/lib/games/xboing.score
%config /etc/X11/wmconfig/xboing

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Mon Jun 01 1998 Erik Troan <ewts@redhat.com>
- sparc architecture was trying to do a solaris build

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
