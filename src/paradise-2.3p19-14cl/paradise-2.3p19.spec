Summary: Enhanced Netrek client with sound and color
Summary(pt_BR): Cliente Netrek Paradise melhorado, com som e cor
Summary(es): Cliente Netrek Paradise mejorado, con sonido y color
Name: paradise
Version: 2.3p19
Release: 14cl
Copyright: BSD
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://ftp.cs.umn.edu/users/glamm/paradise/client/client.2.3p19.tar.bz2
Patch: paradise-2.3p19-config.patch-2
Patch1: paradise-compat21.patch
BuildRoot: /var/tmp/paradise-root
Summary(de): Verbesserter Netrek-Client mit Sound und Farbe 
Summary(fr): Client Netrek amélioré avec son et couleur
Summary(tr): Ses ve renk desteði olan Netrek istemcisi

%description
Netrek is a very popular Internet based arcade game.  You fly around
with a team of players shooting at and capturing planets from the
enemy (another team).  A good way to drop out of college.

%description -l pt_BR
Netrek paradise é um jogo muito popular para a Internet do tipo
arcade. Você voa com um time de jogadores atirando e capturando
planetas do inimigo (outro time). Uma boa maneira de abandonar
a universidade.

%description -l es
Netrek paradise es un juego muy popular para la Internet del tipo
arcade. Vuelas con un time de jugadores disparando y capturando
planetas del enemigo (otro time). Una buena manera de abandonar
la universidad.


%description -l de
Netrek ist ein äußerst beliebtes Internet-Arkaden-Game. Man fliegt mit 
einer Crew von Players im All umher und schnappt dem Feind (einem 
anderen Team) Planeten weg. Kann süchtig machen! 

%description -l fr
netrek est un jeu d'arcade Internet très populaire. Vous volez avec
une équipe de joueurs capturant et tirant sur les planètes de l'ennemi
(l'autre équipe). Une bonne façon d'abandonner ses études.

%description -l tr
Netrek, Internet tabanlý, popüler bir oyundur. Kendi takýmýnýzdaki oyuncularla
birlikte uçarak düþman takýmýn gezegenlerini vurur ve ele geçirirsiniz.

%prep
%setup -q -n client.2.3p19
%patch -p1 -b .tmp
%patch1 -p1

mv data.c data.c.orig
tr -d \\000 < data.c.orig > data.c

%build
make generic
make paradise.sndsrv.linux 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/games

install -m 755 -s netrek.paradise $RPM_BUILD_ROOT/usr/games
install -m 755 -s paradise.sndsrv.linux $RPM_BUILD_ROOT/usr/games
cp sample.xtrekrc $RPM_BUILD_ROOT/usr/games/sample.xtrekrc
chmod 644 $RPM_BUILD_ROOT/usr/games/sample.xtrekrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/games/netrek.paradise
/usr/games/paradise.sndsrv.linux
/usr/games/sample.xtrekrc

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Marcelo Tosatti <marcelo@conectiva.com>
- Fixed glibc 2.1 problems

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations


* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the spec file

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
