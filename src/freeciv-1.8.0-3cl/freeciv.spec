Summary: Civilization clone (game)
Summary(pt_BR): Clone do jogo Civilization 
Summary(es): Civilization clone (game)
Name: freeciv
Version: 1.8.0
Release: 3cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source0: ftp://ftp.freeciv.org/pub/freeciv/%{name}-%{version}.tar.bz2
Patch0:	freeciv.redhat.patch
URL: http://www.freeciv.org/
BuildRoot: /var/tmp/%{name}-%{version}-root
Prefix:	/usr

%description
FreeCiv is an implementation of Civilization II for the X Window System.

%description -l pt_BR
O FreeCiv é uma implementação do Civilization II para o Sistema X Window.

%description -l es
FreeCiv is an implementation of Civilization II for the X Window System.

%package server
Summary: Civilization Server
Summary(pt_BR): Servidor do Civilization
Summary(es): Civilization Server
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos

%description server
FreeCiv is an implementation of Civilization II for the X Window System.
This is the server part.

%description -l pt_BR server
O FreeCiv é uma implementação do Civilization II para o Sistema X Window.
Este é seu servidor.

%description -l es server
FreeCiv is an implementation of Civilization II for the X Window System.
This is the server part.

%package client
Summary: Civilization client
Summary(pt_BR): Cliente para o Civilization
Summary(es): Civilization client
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos

%description client
FreeCiv is an implementation of Civilization II the X Window System.
This is the client part.

%description -l pt_BR client
O FreeCiv é uma implementação do Civilization II para o Sistema X Window.
Este é seu cliente.

%description -l es client
FreeCiv is an implementation of Civilization II the X Window System.
This is the client part.

%prep
%setup -q
%patch -p1 -b .orig

%build
./configure  --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/games/freeciv
cp -R data/* $RPM_BUILD_ROOT%{prefix}/share/games/freeciv
mkdir -p $RPM_BUILD_ROOT%{prefix}/X11R6/lib/X11/app-defaults
cp data/Freeciv $RPM_BUILD_ROOT%{prefix}/X11R6/lib/X11/app-defaults

mkdir -p $RPM_BUILD_ROOT%{prefix}/games
install -m 755 -s client/civclient $RPM_BUILD_ROOT%{prefix}/games
install -m 755 -s server/civserver $RPM_BUILD_ROOT%{prefix}/games

install -m 755 civ $RPM_BUILD_ROOT%{prefix}/games
install -m 755 ser $RPM_BUILD_ROOT%{prefix}/games

%clean 
rm -rf $RPM_BUILD_ROOT

%files client
%defattr(-,root,root) 
%doc AUTHORS COPYING CREDITS HOWTOPLAY INSTALL README NEWS freeciv_hackers_guide.txt
%config %{prefix}/X11R6/lib/X11/app-defaults/Freeciv
%{prefix}/share/games/freeciv/*.xpm
%{prefix}/share/games/freeciv/*.txt
%{prefix}/share/games/freeciv/classic/*.xpm
%{prefix}/share/games/freeciv/default/*.xpm
%{prefix}/games/civclient
%{prefix}/games/civ

%files server
%{prefix}/share/games/freeciv/*.sav
%{prefix}/share/games/freeciv/civ1/*.ruleset
%{prefix}/share/games/freeciv/default/*.ruleset
%{prefix}/games/civserver
%{prefix}/games/ser


%changelog 
* Thu Jul 01 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed
- included in Conectiva Linux 4.0

* Thu Apr 22 1999 Preston Brown <pbrown@redhat.com>
- re-adopted package for PowerTools 6.0

* Wed Apr 21 1999 Hugo van der Kooij <hvdkooij@caiw.nl>
- Updated package to 1.8.0

* Sat Dec 26 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Updated package to 1.7.2
- Split with server and client part

* Mon Dec 14 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Fixed the place where the files are stored to be FHS 2.0 compliant.
- Made the lot RHCN complient.

* Tue Oct 6 1998 Michael Maher <mike@redhat.com>
- updated package

* Tue Aug 4 1998 Michael Maher <mike@redhat.com>
- built package                                                  

