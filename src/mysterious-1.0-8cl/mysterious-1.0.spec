Summary: Brian Howarth's Mysterious Adventure Series
Summary(pt_BR): Série de Adventures Mysterious do Brian Howarth
Summary(es): Serie de Adventures Mysterious del Brian Howarth
Name: mysterious
Version: 1.0
Release: 8cl
Copyright: (c) 1981,82,83, freely redistributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://ftp.gmd.de/if-archive/scott-adams/mysterious.tar.gz
Requires: scottfree
BuildArchitectures: noarch
BuildRoot: /var/tmp/mysterious-root
Summary(de): Brian Howarth's Mysterious Adventure Series
Summary(fr): Séries d'aventures mystérieuses de Brian Howarth
Summary(tr): Brian Howarth'ýn Mysterious macera oyunlarý serisi

%description
Brian Howarth's Mysterious Adventure game series.  This is a text
based adventure game.

%description -l pt_BR
Série Adventure Mistério de Brian Howarth. Este é um jogo adventure
baseado em texto.

%description -l es
Serie Adventure Misterio de Brian Howarth. Este es un juego adventure
basado en texto.

%description -l de
Brian Howarth's Mysterious Adventure-Serie. Dies sind Text-
Adventures.

%description -l fr
La série des jeux Brian Howarth's Mysterious Adventure. C'est un jeu
en mode texte.

%description -l tr
Brian Howarth'ýn Mysterious macera oyunlarý serisi. Bu oyunlar, metin
ekranda çalýþýrlar.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/games/scottfree

for i in *.dat
do
	install -m 644 $i $RPM_BUILD_ROOT/usr/lib/games/scottfree
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ReadMe.txt
/usr/lib/games/scottfree/1_baton.dat
/usr/lib/games/scottfree/2_timemachine.dat
/usr/lib/games/scottfree/3_arrow1.dat
/usr/lib/games/scottfree/4_arrow2.dat
/usr/lib/games/scottfree/5_pulsar7.dat
/usr/lib/games/scottfree/6_circus.dat
/usr/lib/games/scottfree/7_feasibility.dat
/usr/lib/games/scottfree/8_akyrz.dat
/usr/lib/games/scottfree/9_perseus.dat
/usr/lib/games/scottfree/A_tenlittleindians.dat
/usr/lib/games/scottfree/B_waxworks.dat

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
