Summary: Minesweeper game
Summary(pt_BR): Jogo Minesweeper
Summary(es): Juego Minesweeper
Name: xdemineur
Version: 1.1
Release: 13cl
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Copyright: MIT
Source: ftp://ftp.x.org/contrib/games/xdemineur-1.1.tar.gz
Source800: xdemineur-wmconfig.i18n.tgz
BuildRoot: /var/tmp/xdemineur-root
Summary(de): Minesweeper-Game 
Summary(fr): Jeu de démineur
Summary(tr): Mayýn tarlasý oyunu

%description
This is a game of intense concentration, where you must successfully
determine the locations of mines through logic and deduction.

%description -l pt_BR
Este é um jogo de intensa concentração, onde você deve com sucesso
determinar os locais das minas através de lógica e dedução. Muito
parecido com a versão Windows.

%description -l es
Este es un juego de intensa concentración, donde debes con
éxito determinar los locales de las minas a través de lógica y
deducción. Muy parecido con la versión Windows.

%description -l de
Ein Spiel, das intensivste Konzentration erfordert, in dem Sie die 
Standorte von Minen durch logisches, deduktives Denken herausfinden müssen.

%description -l fr
Jeu d'une concentration extrême, où vous devez déterminer les emplacements
des mines en utilisant la logique et la déduction.

%description -l tr
Komþu karelerde yer alan mayýn sayýlarýndan yararlanarak tarlada yer alan tüm
mayýnlarý bulmanýz amaçlanmaktadýr.

%prep
%setup -q -n xdemineur

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xdemineur <<EOF
#xdemineur name "xdemineur"
#xdemineur description "Minesweeper"
#xdemineur group Jogos/Estratégia
#xdemineur exec "xdemineur &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xdemineur-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xdemineur
/usr/X11R6/man/man1/xdemineur.1x
%config /etc/X11/wmconfig/xdemineur

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Fri Dec 11 1998 Conectiva <dist@conectiva.com>
- final rebuild for 3.0
- Jogos/Estratégia no wmconfig no lugar de Jogo/Estratégia

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- wmconfig pt_BR

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
