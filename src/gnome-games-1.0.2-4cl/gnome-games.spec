# Note that this is NOT a relocatable package
%define ver      1.0.2
%define rel      4cl
%define prefix   /usr

Summary: GNOME games.
Summary(pt_BR): Jogos para o GNOME.
Summary(es): Juegos para GNOME.
Name: gnome-games
Version: %ver
Release: %rel
Copyright: LGPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
# was .gz
Source0: ftp://ftp.gnome.org/pub/gnome-games-%{PACKAGE_VERSION}.tar.bz2
Source1: gnome-games-pt_BR.po
Patch0: gnome-games-1.0.2-pt_BR.patch
Patch1: gnome-games-gnome-menu.patch
BuildRoot: /var/tmp/gnome-games-%{PACKAGE_VERSION}-root
Obsoletes: gnome
URL: http://www.gnome.org/
Docdir: %{prefix}/doc

%description
GNOME is the GNU Network Object Model Environment. That's a fancy
name, but really GNOME is a nice GUI desktop environment.
Its powerful, friendly and easy-to-configure interface makes
using your computer easy.

This package installs some GNOME games on your system,
such as gnothello, solitaire, tetris and others.

%description -l pt_BR
Jogos para o GNOME.

GNOME é o Ambiente de Rede Modelado por Objetos da GNU. É um nome
fantasioso, mas o GNOME é realmente um bom ambiente gráfico. Ele
torna seu computador fácil, poderoso e fácil de configurar.

%description -l es
Juegos para GNOME.  GNOME es el Ambiente de Red Modelado por Objetos
de la GNU. Es un nombre fantasioso, pero GNOME es realmente un
bueno ambiente gráfico. Hace tu ordenador sencillo, potente y fácil
de configurar.

%package devel
Summary: GNOME games development libraries.
Summary(pt_BR): Bibliotecas para o desenvolvimento de jogos para o GNOME.
Summary(es): Bibliotecas para el desarrollo de juegos para GNOME.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: gnome-games

%description devel
This packages installs the libraries and files needed
to develop some GNOME games.

%description -l pt_BR devel
Bibliotecas para o desenvolvimento de jogos para o GNOME.

%description -l es devel
Bibliotecas para el desarrollo de juegos para GNOME.

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome-menu entries for gnome-games

* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 30 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.0.2

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- some fixes

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Sat Nov 21 1998 Michael Fulbright <drmike@redhat.com>
- updated for 0.30 tree

* Fri Nov 20 1998 Pablo Saratxaga <srtxg@chanae.alphanet.ch>
- use --localstatedir=/var/lib in config state (score files for games
  for exemple will go there).

* Mon Mar 16 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-games CVS source tree

%prep
%setup -q
%patch0 -p1 -b .pt_BR
%patch1 -p1 -b .gnome-menu

%build

cp $RPM_SOURCE_DIR/gnome-games-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS
%ifarch alpha
autoconf
./configure --host=alpha-conectiva-linux --prefix=%prefix --localstatedir=/var/lib
%else
autoconf
./configure --prefix=%prefix --localstatedir=/var/lib
%endif

make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%attr(-, root, games) %{prefix}/bin/*
%{prefix}/etc/sound/events
%{prefix}/share/gnome/apps/Games/*
%{prefix}/share/gnibbles/*
%{prefix}/share/gnobots2/*
%{prefix}/share/gnome/help/*
%{prefix}/share/gnome-stones/*
%{prefix}/share/gturing/*
%{prefix}/share/locale/*/*/*
%{prefix}/share/metatris/*
%{prefix}/share/pixmaps/*
%{prefix}/share/sol-games/*
%{prefix}/share/sounds/*

%{prefix}/lib/lib*.so.*
%{prefix}/lib/gnome-stones/objects/lib*.so.*
#%ghost /var/lib/games/*

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/lib/gnome-stones/objects/lib*.so
%{prefix}/lib/gnome-stones/objects/lib*a
%{prefix}/include/*
