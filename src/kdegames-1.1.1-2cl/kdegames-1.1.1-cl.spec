%define kdeprefix /usr
%define version 1.1.1
%define kderelease 2cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source

%define conectiva versão-conectiva >= 3.0
%define qtversion  qt >= 1.42

%define kdename kdegames
Name: %{kdename}
Summary: K Desktop Environment - Games
Summary(pt_BR): K Desktop Environment - Jogos
Summary(es): K Desktop Environment - Juegos
Version: %{version}
Release: %{kderelease}
Source: ftp://ftp.kde.org:/pub/kde/%{sourcedir}/%{kdename}-%{version}.tar.bz2
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
BuildRoot: /var/tmp/%{kdename}-buildroot
Copyright: GPL
Requires: %{qtversion} %{conectiva} kdesupport
Prefix: %{kdeprefix}
# present in Parolin
Obsoletes: kde-games

%description
Games for the K Desktop Environment. 
Included with this package are: kabalone, kasteroids, kblackbox, kmahjongg,
kmines, konquest, kpat, kpoker, kreversi, ksame, kshisen, ksokoban, ksmiletris,
ksnake, ktetris.

%description -l pt_BR
Jogos para o KDE.

Incluídos neste pacote:

kabalone: estratégia kasteroids: arcade kmahjongg: o popular mahjongg
kmines: desarmar as minas kpat: jogos de cartas, inclusive paciência
kpoker: vídeo-poker kreversi: Reversi ksame: um jogo de tabuleiro
kshisen: Shisen-Sho - relacionado com o mahjongg ksnake: corrida
das cobras ktetris: o bem conhecido tetris

%description -l es
Juegos para KDE.  Incluidos en este paquete: kabalone: estrategia
kasteroids: arcade kmahjongg: el popular mahjongg kmines: desarmar
las minas kpat: juegos de cartas, incluso solitario kpoker: vídeo
póquer kreversi: Reversi ksame: un juego de tablero kshisen:
Shisen-Sho - relacionado con el mahjongg ksnake: corrida de las
cobras ktetris: el bien conocido tetris

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{kdename}-%{version}

%build
export KDEDIR=%{kdeprefix}
[ "$LINGUAS" ] && unset LINGUAS
    CFLAGS=$RPM_OPT_FLAGS \
    CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti" \
    ./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT
make

%install
make install-strip

cd $RPM_BUILD_ROOT
find . -type d | grep -v "\/usr\/share\/locale" | \
	sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
	-e '/\/config\//s|^|%config|' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{kdename}

%files -f ../file.list.%{kdename}

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 04 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed spefile wrt rpm 3.0

* Mon May 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- updated to KDE 1.1.1
- files in KDEDIR/share/applnk no longer treated as %config files

* Sat Apr 03 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Obsoletes kde-games

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- %dir /usr/share/locale removed from %filelist

* Thu Feb 25 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Compiled with -fno-exceptions -fno-rtti
- Added postinstall script for kappfinder and wmconfig

* Tue Jan 19 1999 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Jan 06 1999 Preston Brown <pbrown@redhat.com>
- re-merged updates from Duncan Haldane, change /opt/kde --> /usr
