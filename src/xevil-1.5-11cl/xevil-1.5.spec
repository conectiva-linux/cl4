Summary: A fast-action, explicitly violent game for X
Summary(pt_BR): Jogo de ação para X
Summary(es): Juego de acción para X
Name: xevil
Version: 1.5
Release: 11cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
#Source: ftp://ftp.x.org/contrib/games/xevil1.5/xevil1.5.tar.Z
# recompressed with bzip2
Source: ftp://ftp.x.org/contrib/games/xevil1.5/xevil1.5.tar.bz2
Source800: xevil-wmconfig.i18n.tgz
Patch: xevil1.5-config.patch
Buildroot: /var/tmp/xevilroot
Summary(de): Ein schnelles, extrem gewalttätiges Actionspiel für X
Summary(fr): Un jeu d'action rapide et très violent sous X
Summary(tr): Hýzlý ve þiddet yüklü bir X oyunu

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Mon Dec 07 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>

- updated to work on non Intel platforms (silly Makefile hack)
- uses a buildroot and %attr tags

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>

- built against glibc

%description
An action/adventure game for X-Windows in which you, as a Ninja warrior,
kill everything in sight, and explore if you survive. 

%description -l pt_BR
Um jogo de ação/aventura para X Window no qual você, como um
guerreiro Ninja, mata tudo a sua volta, e tenta sobreviver.

%description -l es
Un juego de ación/aventura para X Window en el que tu, como un
guerrero Ninja, mata todo a tu vuelta, y intenta sobrevivir.

%description -l de
Ein Action/Adventure-Spiel für X-Windows, in dem Sie als Ninja alles
niedermachen und dann die Gegend erkunden - wenn Sie überleben.

%description -l fr
Jeu d'action/aventure pour X Window dans lequel vous, guerrier Ninja, tuez
tout ce que vous voyez et essayez de survivre.

%description -l tr
X-Windows altýnda oynanan bir action/macera oyunu. Sizin rolünüz, bir Ninja
savaþçýsý olarak karþýnýza çýkan her þeyi öldürmek.

%prep
%setup -c
%patch -p1

%build
OS=`echo $RPM_OS | tr '[A-Z]' '[a-z]'`
make ${OS}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man6
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

install -m 755 xevil $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 644 xevil.6 $RPM_BUILD_ROOT/usr/X11R6/man/man6

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xevil <<EOF
#xevil name "xevil"
#xevil description "Jogo de Ação Rápida"
#xevil group Jogos/Vídeo
#xevil exec "xevil &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xevil-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%attr(-,root,root) /usr/X11R6/bin/xevil
%attr(-,root,root) /usr/X11R6/man/man6/xevil.6
%config %attr(-,root,root) /etc/X11/wmconfig/xevil
