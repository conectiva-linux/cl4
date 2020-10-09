Summary: Various mind games for Linux SVGAlib
Summary(pt_BR): V�rios jogos de quebra-cabe�a para Linux SVGAlib
Summary(es): Varios juegos de rompecabezas para Linux SVGAlib
Name: vga_gamespack
Version: 1.3
Release: 13cl
Copyright: Distributable
Exclusivearch: i386
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://sunsite.unc.edu/pub/Linux/games/strategy/vga_gamespack-1.3.tgz
Patch0: vga_gamespack-1.3-misc.patch
Patch1: vga_gamespack-br.patch
Summary(de): Verschiedene Denkspiele f�r Linux SVGAlib
Summary(tr): SVGAlib ile �al��an �e�itli zeka oyunlar�
Buildroot: /var/tmp/vga_gamespack-root

%description
A number of various mind games for the Linux console using SVGAlib. The
selection includes such favorites as Othello, Minesweeper, and Connect 4.

%description -l pt_BR
V�rios jogos "mentais" para o Linux usando SVGAlib. A sele��o inclui
alguns best-sellers como Othello, Minesweeper, e Connect 4.

%description -l es
Varios juegos "mentales" para Linux usando SVGAlib. La selecci�n
incluye algunos best-sellers como Othello, Minesweeper, y Connect 4.

%description -l de
Eine Auswahl verschiedener Denkspiele f�r die Linux-Konsole unter 
Verwendung der SVGAlib, unter anderem solche Favoriten wie Othello, 
Minesweeper und Connect 4. 

%description -l fr
Jeux de r�flexion pour la console Linux, utilisant SVGAlib. Inclus Othello
D�mineur et Connect 4.

%description -l tr
SVGAlib kullanan konsol oyunlar�. Othello, may�n tarlas� ve hedef 4 gibi
sevilen oyunlar� i�erir.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Wed Oct 14 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- added pt_BR translations

* Tue Aug 18 1998 Cristian Gafton <gafton@redhat.com>
- buildroot

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Michael Fulbright
- cleaned up spec file

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%prep
%setup -n vga_gamespack
%patch0 -p1
%patch1 -p1

%build
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install INSTROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/games/vga_connectN
/usr/games/vga_mines
/usr/games/vga_othello
/usr/lib/games/Vga16font8x16
