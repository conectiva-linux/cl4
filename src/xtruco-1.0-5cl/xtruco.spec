Name: xtruco
Release: 5cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Version: 1.0
Summary: A nice brazilian card game
Summary(pt_BR): Jogo de cartas brasileiro
Summary(es): Juego de cartas brasileño
Source0: xtruco.tar.gz
Source800: xtruco-wmconfig.i18n.tgz
Patch: xtruco.makefile.patch
BuildRoot: /tmp/%{name}-%{version}

%description
A popular card game in Brazil.

%description -l pt_BR
Truco! Jogue truco com o seu Linux!

%description -l es
Juego de cartas brasileño

%prep
%setup -n xtruco
%patch

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin $RPM_BUILD_ROOT/etc/X11/wmconfig/
install -m0755 xtruco $RPM_BUILD_ROOT/usr/X11R6/bin/xtruco


tar xvfpz $RPM_SOURCE_DIR/xtruco-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
/usr/X11R6/bin/xtruco
%config /etc/X11/wmconfig/xtruco

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

