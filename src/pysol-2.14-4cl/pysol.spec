Summary: PySol provides several solitaire card games
Summary(pt_BR): Vários jogos de paciência
Summary(es): PySol incluye varios juegos de cartas
Name: pysol
Version: 2.14
Release: 4cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
URL: http://wildsau.idv.uni-linz.ac.at/mfx/pysol.html
Source0: pysol-2.14.tar.gz
Source800: pysol-wmconfig.i18n.tgz
Patch0: pysol-2.10.patch
Patch1: pysol-2.14-paths.patch
BuildRoot: /var/tmp/%{name}-root
Requires: tcl >= 8.0.3
Requires: tk >= 8.0.3
Requires: python >= 1.5.1

%description
PySol has several solitaire card games, written in 100%% pure
Python. It has many features: unlimited undo and redo, load & save
games, player statistics, hint system, game plug-ins, and more!
Contains: klondike, freecel, spider, golf, etc.

%description -l pt_BR
PySol inclui vários jogos de paciência com cartas escrito 100%%
em Python.  Ele tem muitas características: desfaz e refaz jogadas
sem limites, carrega e salva jogos, estatísticas do jogador, dicas,
plug-ins e muito mais! Você poderá jogar entre outros: klondike,
freecel, spider, golf, etc.

%description -l es
PySol incluye varios juegos de cartas escrito 100%% en Python. Tiene
muchas características: "undo" y "redo" sin limitación, carga y
salva juegos, estadísticas del jugador, indirectas, "plug-ins" y
mucho más! Usted tendrá varias opciones: klondike, freecel, spider,
golf, etc.

%prep
%setup 
%patch0
%patch1 -p1 -b .pt_BR

%build

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

# Get rid of version-number dir
mv $RPM_BUILD_ROOT/usr/share/pysol/%{version}/* $RPM_BUILD_ROOT/usr/share/pysol/
rmdir $RPM_BUILD_ROOT/usr/share/pysol/%{version}/

mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/ 
mkdir -p $RPM_BUILD_ROOT/usr/bin/
install -m 644 data/pysol.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/ 
ln -s /usr/games/pysol $RPM_BUILD_ROOT/usr/bin

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

tar xvfpz $RPM_SOURCE_DIR/pysol-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root,root)
%dir /usr/share/pysol
/usr/share/pysol/*
/usr/share/pixmaps/pysol.xpm
/usr/games/pysol
/usr/bin/pysol
/usr/man/man6/pysol.6.gz
/etc/X11/wmconfig/pysol

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed a bug in the directory where the pixmap was being put

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to 2.14

* Thu Mar 18 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- added Group, Summary and %description translations

* Fri Mar 12 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- initial package
