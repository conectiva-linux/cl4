Summary: X windows interpreter for Infocom format text adventure games
Summary(pt_BR): Interpretador X Window para os jogos adventure no formato Infocom
Summary(es): Interpretador X Window para los juegos adventure en formato Infocom
Name: xzip
Version: 180
Release: 4cl
Copyright: Freely redistributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
#Source: ftp://ftp.gmd.de/if-archive/infocom/interpreters/zip/xzip180.tar.Z
# recompressed with bzip2
Source: ftp://ftp.gmd.de/if-archive/infocom/interpreters/zip/xzip180.tar.bz2
Source2: runzcode
Patch0: xzip-config.patch
BuildRoot: /var/tmp/xzip-root
Summary(de): X-Windows-Interpretierer für Text-Adventures im Infocom-Format 
Summary(fr): Interpréteur X pour jeux d'aventure au format texte d'Infocom
Summary(tr): Infocom biçimindeki metin ekran macera oyunlarý için X yorumlayýcýsý

%description
Now all your favorite text adventure games can take on a new dimension
with this X Windows interpreter for them.

%description -l pt_BR
Agora todos os seus jogos tipo "adventure" em texto podem adquirir
uma nova dimensão com este interpretador para X Window.

%description -l es
Ahora todos los sus juegos tipo "adventure" en texto pueden adquirir
una nueva dimensión con este interpretador para X Window.

%description -l de
Jetzt können Sie all Ihren Lieblingstextadventures eine neue Dimension
verleihen - dank dieses X-Windows-Interpretierers. 

%description -l fr
Désormais, tous vos jeux d'aventure favoris en mode texte peuvent prendre une
nouvelle dimension avec cet interpréteur X Window fait pour eux.

%description -l tr
Artýk metin kipinde çalýþan macera oyunlarýnýz bu X yorumlayýcýsý sayesinde
yeni bir boyut kazanacak.

%prep
%setup -q -n xzip
%patch -p1 -b .patch

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{games,man/man6}

install -s xzip $RPM_BUILD_ROOT/usr/games/xzip
install xzip.1 $RPM_BUILD_ROOT/usr/man/man6/xzip.6

install -d -m 755 $RPM_BUILD_ROOT/usr/lib/games/zcode
install -m 755 $RPM_SOURCE_DIR/runzcode $RPM_BUILD_ROOT/usr/games/runzcode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/man/man6/xzip.6
/usr/games/xzip
/usr/games/runzcode

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- updated package

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated to version 161

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
