Summary: Galaga clone
Summary(pt_BR): Clone do galaga
Summary(es): Clone del galaga
%define version 2.0.34
Name: xgalaga
Version: %{version}
Release: 5cl
Copyright: Shareware
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://ftp.x.org/contrib/games/xgalaga-%{version}.tar.bz2
Source800: xgalaga-wmconfig.i18n.tgz
Patch: xgalaga-%{version}.buildroot.patch
Patch1: xgalaga-glibc21.patch

Url: http://www.aa.net/~ogre/xgal.html
BuildRoot: /tmp/build-xgalaga

%changelog

* Tue Jun  8 1999 Marcelo Tosatti <marcelo@conectiva.com>
- fixed problems with glibc 2.1

* Mon Nov 30 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- strip binaries

* Tue Oct 27 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Sep 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- updated to 2.0.34

%description
A clone of the old space arcade game 'Galaga'.  (It's Galaga, you know
how to play Galaga!  Ship follows the mouse, button fires.  Auto-fire by
holding it down, so no-one accuses us of breaking their mouse!)

%description -l pt_BR
Um clone do velho jogo arcade espacial 'Galaga'. (É Galaga,
você sabe como jogar Galaga! A nave segue o mouse e o botão
atira. Tiro-automático segurando o botão, então ninguém me acusar
de quebrar o seu mouse!)

%description -l es
Un clone del viejo juego arcade espacial 'Galaga'. (Es Galaga, ¡sabes
cómo jugar Galaga! La nave sigue el ratón y el botón dispara. Disparo
automático sujetando el botón, ¿pero, que nadie me acuse
de romper el ratón!)

%prep
%setup -n xgalaga-%{version}
%patch -p1
%patch1 -p1

%build
./configure --exec-prefix=/usr/X11R6/bin --prefix=/usr/lib/xgalaga --with-sound=native $RPM_ARCH-conectiva-linux-gnu
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib/xgalaga
mkdir -p $RPM_BUILD_ROOT/var/lib/games
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
make DESTDIR="$RPM_BUILD_ROOT" install

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xgalaga <<EOF
#xgalaga name "xgalaga"
#xgalaga description "Galaga"
#xgalaga group Jogos/Vídeo
#xgalaga exec "xgalaga -keyboard &"
#EOF

touch $RPM_BUILD_ROOT/var/lib/games/xgalscores
strip $RPM_BUILD_ROOT/usr/X11R6/bin/*



tar xvfpz $RPM_SOURCE_DIR/xgalaga-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
/usr/X11R6/bin/xgalaga
/usr/lib/xgalaga
%ghost /var/lib/games/xgalscores
%config /etc/X11/wmconfig/xgalaga
