Summary: text adventure game for use with xzip
Summary(pt_BR): Jogo adventure modo texto para uso com o xzip
Summary(es): Juego adventure modo texto para uso con xzip
Name: christminster
Version: 3
Release: 9cl
Copyright: Freely redistributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://ftp.gmd.de/if-archive/games/infocom/christminster.z5.bz2
Requires: xzip
BuildRoot: /var/tmp/christminster-root
Summary(de): Textadventure zur Benutzung mit xzip 
Summary(fr): Jeu d'aventure en mode texte à utiliser avex xzip
Summary(tr): xzip ile oynanabilen metin ekran macera oyunu

%description
This is a text adventure game for use with xzip.

%description -l pt_BR
Este é um jogo adventure de texto para usar com xzip.

%description -l es
Este es un juego "adventure" de texto para usar con xzip.

%description -l de
Ein Text-Adventure zur Verwendung mit xzip. 

%description -l fr
Jeu d'aventure en mode texte pour utiliser avec xzip.

%description -l tr
xzip ile kullanýlabilecek bir metin ekran macera oyunu

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{games,lib/games/zcode}

cp $RPM_SOURCE_DIR/christminster.z5.bz2 $RPM_BUILD_ROOT/usr/lib/games/zcode/
bunzip2 $RPM_BUILD_ROOT/usr/lib/games/zcode/christminster.z5.bz2
chmod 644 $RPM_BUILD_ROOT/usr/lib/games/zcode/christminster.z5

ln -sf runzcode $RPM_BUILD_ROOT/usr/games/christminster

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/games/zcode/christminster.z5
/usr/games/christminster

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
