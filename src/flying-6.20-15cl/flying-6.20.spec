Summary: pool, snooker, air hockey, and other table games
Summary(pt_BR): Pool, snooker, air hockey, e outros jogos de tabuleiro
Summary(es): Pool, snooker, air hockey, y otros juegos de tablero
Name: flying
Version: 6.20
Release: 15cl
Copyright: MIT
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
# was .tgz
Source: ftp://ftp.x.org/contrib/games/multiplayer/flying-6.20.tar.bz2
Source1: cannon.wmconfig
Source2: carrom.wmconfig
Source3: curling.wmconfig
Source4: hockey.wmconfig
Source5: pool.wmconfig
Source6: pool9.wmconfig
Source7: snooker.wmconfig
Source800: flying-wmconfig.i18n.tgz
Patch: flying-6.20-glibc.patch
Buildroot: /var/tmp/flying-root
Summary(de): Billiard, Snooker, Air-Hockey und andere Tischsportarten 
Summary(fr): billard, snooker, hockey et autres jeux de table
Summary(tr): Çeþitli bilardo oyunlarý

%description
This is a package of games that run under X Windows.  It contains
pool, snooker, air hockey, and other table games.  WARNING:  This
software could become addictive and could cause serious levels of
sleep deprivation or loss of mobility in the legs if used at 
extreme levels.

%description -l pt_BR
Este é um pacote de jogos que rodam em X Window. Ele contém pool,
snooker, air hockey e outros jogos de tabuleiro. ADVERTÊNCIA: Esse
software pode viciar e pode causar sérios níveis de privação do sono
ou perda da mobilidade nas pernas se usado em condições extremas.

%description -l es
Este es un paquete de juegos que ejecutan en X Window. Contiene pool,
snooker, air hockey y otros juegos de tablero. ADVERTENCIA: Este
software puede viciar y puede causar serios niveles de privación
del sueño o pérdida de la movilidad en las piernas se usado en
condiciones extremas.

%description -l de
Dieses Games-Paketläuft unter X-Windows. Es enthält
Pool, Snooker, Air Hockey und andere Tischspiele. WARNUNG:
Der übermäßige Einsatz dieser Software kann süchtig machen 
und Schlafentzug oder Verlust der Beweglichkeit der Beine 
zur Folge haben.

%description -l tr
Bu pakette X11 için bilardo tarzý bir dizi oyun yer almaktadýr.

%prep
cd /usr/src/rpm/BUILD
rm -rf flying-%{PACKAGE_VERSION}
tar xvfI /usr/src/rpm/SOURCES/flying-%{PACKAGE_VERSION}.tar.bz2
cd flying-%{PACKAGE_VERSION}
%patch -p1 -b .patch

%build
cd flying-%{PACKAGE_VERSION}
make -f Makefile.Linux CXX="g++ $RPM_OPT_FLAGS"

%install
cd flying-%{PACKAGE_VERSION}
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man6}
install -s -m 755 flying $RPM_BUILD_ROOT/usr/X11R6/bin/flying
ln -sf flying $RPM_BUILD_ROOT/usr/X11R6/bin/xsnooker
ln -sf flying $RPM_BUILD_ROOT/usr/X11R6/bin/xpool
ln -sf flying $RPM_BUILD_ROOT/usr/X11R6/bin/xcannon
ln -sf flying $RPM_BUILD_ROOT/usr/X11R6/bin/xcarrom
ln -sf flying $RPM_BUILD_ROOT/usr/X11R6/bin/xhockey
ln -sf flying $RPM_BUILD_ROOT/usr/X11R6/bin/xcurling
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man6
install -m 644 flying.man $RPM_BUILD_ROOT/usr/X11R6/man/man6/flying.6
ln -sf flying.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xsnooker.6
ln -sf flying.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xpool.6
ln -sf flying.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xcannon.6
ln -sf flying.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xcarrom.6
ln -sf flying.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xhockey.6
ln -sf flying.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6/xcurling.6

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/






tar xvfpz $RPM_SOURCE_DIR/flying-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc README
/usr/X11R6/bin/*
/usr/X11R6/man/*/*
%config /etc/X11/wmconfig/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Sep 01 1998 Michael Maher <mike@redhat.com>
- built for 5.2 
- edited SOURCE path.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- force use of egcs for compiling it

* Sun Apr 12 1998 Cristian Gafton <gafton@redhat.com>
- added %clean

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan build
- buildroot

* Thu Oct 16 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

