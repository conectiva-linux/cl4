Name: doom
Version: 1.8
Release: 14cl
ExclusiveArch: i386
Url:http://www.idsoftware.com
Source: linux-doom-1.8.tar.bz2
Patch: rundoom.patch
Copyright: shareware
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Requires: aout-libs
Autoreqprov: no
Summary: DOOM for Linux Consoles & X-Windows
Summary(pt_BR): DOOM para consoles Linux e para X-Window
Summary(es): DOOM para consolas Linux y para X-Window

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 18 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- added patch to rundoom 

* Tue Sep 16 1997 Erik Troan <ewt@redhat.com>
- repackaged for 5.0

%description
DOOM is the original awesome game from ID software.  It is a first person
graphical (and very graphic!) game that runs under SVGA lib or X Windows,
and allows multiple players to play simultaneously. 

%description -l pt_BR
DOOM é o incrível jogo original da ID software. É um jogo gráfico
em primeira pessoa, rodando em svgalib ou X Window. Também pode
ser jogado em rede.

%description -l es
DOOM es el increíble juego original de la ID software. Es un juego
gráfico en primera persona, ejecutando en svgalib o X Window. También
se puede jugar en red.

%prep
%setup
%patch

%install
mkdir -p /usr/lib/games/doom
install -m 755 -o 0 -g 0 xdoom /usr/X11R6/bin/xdoom
install -m 755 -o 0 -g 0 sdoom /usr/games/sdoom
install -m 755 -o 0 -g 0 sndserver /usr/lib/games/doom/sndserver
install -m 755 -o 0 -g 0 musserver /usr/lib/games/doom/musserver
install -m 755 -o 0 -g 0 doom1.wad /usr/lib/games/doom/doom1.wad
install -m 755 -o 0 -g 0 rundoom /usr/games/rundoom

%files
%doc README README.config README.linuxs README.linuxx mus.doc
/usr/X11R6/bin/xdoom
/usr/lib/games/doom/doom1.wad
/usr/lib/games/doom/sndserver
/usr/games/sdoom
/usr/lib/games/doom/musserver
/usr/games/rundoom
