Summary: X based flight combat
Summary(pt_BR): Combate aéreo para X-Window
Summary(es): Combate aéreo para X-Window
Name: acm
Version: 4.7
Release: 9
Copyright: MIT
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://ftp.x.org/contrib/games/multiplayer/acm-4.7.tar.bz2
Patch: acm-4.7-linux.patch
Patch1: acm-4.7.patch
BuildRoot: /var/tmp/acm-root
Summary(de): Flugkampfspiel unter X
Summary(fr): Combat aérien sous X.
Summary(tr): X tabanlý uçuþ ve savaþ

%description
ACM is an X based flight simulator.  It also have network cabailities
for multiple player games.

%description -l pt_BR
ACM é um simulador de vôo para X. Ele também permite jogar em rede
com vários jogadores.

%description -l es
ACM es un simulador de vuelo para X. También permite jugar en red
con varios jugadores.

%description -l de
ACM ist ein Flugsimulator auf X-Basis, der netzwerkfähig ist 
und die Teilnahme mehrerer Spieler gestattet. 

%description -l fr
ACM est un simulateur de vol sous X. Il permet de jouer en réseau à plusieurs
joueurs.

%description -l tr
ACM, X tabanlý bir uçuþ simulatörüdür. Çok oyunculu oynayabilmek için
gerekli að yeteneklerine sahiptir.

%prep
%setup -q
%patch -p1 -b .linux
%patch1 -p1 -b .orig

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/games,man/man1}

make prefix=$RPM_BUILD_ROOT/usr install
gzip -9 $RPM_BUILD_ROOT/usr/man/man1/acm.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/acm
/usr/bin/acms
/usr/bin/kill-acms
/usr/man/man1/acm.1.gz
/usr/lib/games/acm

%changelog
* Wed Jun 30 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Mon Jan 25 1999 Michael Maher <mike@redhat.com>
- changed the group heading

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- rebuilt package for 6.0

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
