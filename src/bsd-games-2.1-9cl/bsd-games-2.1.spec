Summary: miscellaneous BSD games package
Summary(pt_BR): Pacote com vários jogos BSD
Summary(es): Paquete con varios juegos BSD
Name: bsd-games
Version: 2.1
Release: 9cl
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
#Source0: ftp://sunsite.unc.edu/pub/Linux/games/bsd-games-2.1.tar.gz
Source0: ftp://sunsite.unc.edu/pub/Linux/games/bsd-games-2.1.tar.bz2
Patch0: bsd-games-2.1-config.patch.bz2
Patch1: bsd-games-2.1-nonlist.patch
Patch2: bsd-games-2.1-hole.patch
Patch3: bsd-games-2.1-sailbug.patch
Patch4: bsd-games-compat21.patch
Buildroot: /var/tmp/bsd-games
Summary(de): Diverse BSD-Games  
Summary(fr): paquetage de jeux BSD divers
Summary(tr): Metin ekranda oyunlar paketi

%description
This is a bunch of games.  Highlights include backgammon, cribbage,
hangman, monop, primes, trek, and battlestar.

%description -l pt_BR
Isto é um conjunto de jogos. Os destaques incluem gamão, jogo de
cartas, forca, monopólio e guerra nas estrelas.

%description -l es
Esto es un conjunto de juegos. Los destaques incluyen gammon,
barajas, ahorcado, monopolio y guerra en las estrellas.

%description -l de
Dies ist eine Sammlung von Games. Zu den bekanntesten gehören Backgammon,
Cribbage, Monop, Primes, Trek und Battlestar.

%description -l fr
Lot de jeux. Contient backgammon, cribbage, le pendu, monop, primes, trek
et battlestar.

%description -l tr
Tavla, cribbage, adam asmaca, monop, primes, trek ve battlestar gibi oyunlar
içeren bir paket.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations


* Thu Jun 18 1998 Alan Cox <alan@redhat.com>

- Chris Evans pointed out a hole in sail I missed.

* Wed Jun 17 1998 Alan Cox <alan@redhat.com>

- Stopped people using cribbage to be able to cheat game score files.

* Tue May 05 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixed the config patch so that it will build on non /usr/src/redhat build
  trees

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- updated to bsd-games 2.1
- started over on package

%prep
%setup -q
%patch -p1 -b .config
%patch1 -p1 -b .nonlist
%patch2 -p1 -b .nocheat
%patch3 -p1 -b .reallynocheat
%patch4 -p1
chmod +x install-man
chmod +x install-score

%build
rm -rf $RPM_BUILD_ROOT
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 

%install
make RPM_BUILD_ROOT="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
/var/lib/games
/usr/share/games
/usr/man/man5/*
/usr/man/man6/*
/usr/man/man8/*
%attr(755,root,games) /usr/games/*
/usr/sbin/*
