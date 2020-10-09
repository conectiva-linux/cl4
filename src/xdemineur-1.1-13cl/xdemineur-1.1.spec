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
Summary(fr): Jeu de d�mineur
Summary(tr): May�n tarlas� oyunu

%description
This is a game of intense concentration, where you must successfully
determine the locations of mines through logic and deduction.

%description -l pt_BR
Este � um jogo de intensa concentra��o, onde voc� deve com sucesso
determinar os locais das minas atrav�s de l�gica e dedu��o. Muito
parecido com a vers�o Windows.

%description -l es
Este es un juego de intensa concentraci�n, donde debes con
�xito determinar los locales de las minas a trav�s de l�gica y
deducci�n. Muy parecido con la versi�n Windows.

%description -l de
Ein Spiel, das intensivste Konzentration erfordert, in dem Sie die 
Standorte von Minen durch logisches, deduktives Denken herausfinden m�ssen.

%description -l fr
Jeu d'une concentration extr�me, o� vous devez d�terminer les emplacements
des mines en utilisant la logique et la d�duction.

%description -l tr
Kom�u karelerde yer alan may�n say�lar�ndan yararlanarak tarlada yer alan t�m
may�nlar� bulman�z ama�lanmaktad�r.

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
#xdemineur group Jogos/Estrat�gia
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
- Jogos/Estrat�gia no wmconfig no lugar de Jogo/Estrat�gia

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- wmconfig pt_BR

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
