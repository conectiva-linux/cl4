Summary: Card games for the linux console
Summary(pt_BR): Jogo de carta de baralho para console.
Summary(es): Juego de carta de baraja para consola.
Name: vga_cardgames
Version: 1.3.1
Release: 13cl
Exclusivearch: i386
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://sunsite.unc.edu/pub/Linux/games/strategy/vga_cardgames-1.3.1.tgz
Patch0: vga_cardgames-1.3.1-fsstnd.patch
Patch1: vga_cardgames-1.3.1-br.patch
Summary(fr): Jeux de cartes pour la console Linux
Summary(tr): Konsolda oynanan kaðýt oyunlarý
BuildRoot: /var/tmp/vga_cardgames-root

%description
A number of various card games for the Linux console, including Klondike,
'Oh Hell', Solitaire, and Spider, as well as some other popular
time-wasters :) 

%description -l pt_BR
Vários jogos de carta para o Linux, incluindo Klondike, "Oh Hell",
Solitaire, e Spider, assim como outros populares passatempos :)

%description -l es
Varios juegos de baraja para Linux, incluye Klondike, "Oh Hell",
Solitaire, y Spider, así como otros populares pasatiempos :)

%description -l de
Eine Reihe verschiedener Kartenspiele für die Linux-Konsole, u.a. 
Klondike, Oh Hell, Solitaire und Spider, plus andere beliebte Zeit-
vergeuder ...

%description -l fr
Divers jeux de cartes en mode console pour Linux, dont Klondike,'Oh Hell',
Solitaire, et Spider, ainsi que d'autres passe-temps populaires :).

%description -l tr
Metin ekranda oynanan çeþitli kaðýt oyunlarý. Klondike, Solitaire, Spider
gibi fal oyunlarý bu pakette yer alýr.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Wed Oct 14 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- added pt_BR translations

* Tue Aug 18 1998 Cristian Gafton <gafton@redhat.com>
- buildroot

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%prep
%setup -n vga_cardgames
%patch0 -p1
%patch1 -p1

%build
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make install INSTROOT=$RPM_BUILD_ROOT

%files
/usr/games/vga_klondike
/usr/games/vga_ohhell
/usr/games/vga_solitaire
/usr/games/vga_spider
/usr/lib/games/Vga16font8x16.cards
/usr/lib/games/Cards56x80
