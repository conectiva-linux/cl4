Summary: 3d geometry game
Summary(pt_BR): Jogo geométrico em 3d
Summary(es): Juego geométrico en 3D
Name: xbl
Version: 1.0h
Release: 7cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
# Source: ftp://ftp710.univ-lyon1.fr/pub/xbl/xbl-1.0h.tar.Z
# recompressed with bzip2
Source: ftp://ftp710.univ-lyon1.fr/pub/xbl/xbl-1.0h.tar.bz2
Source800: xbl-wmconfig.i18n.tgz
Patch: xbl-1.0f-config.patch
Url: http://www710.univ-lyon1.fr/ftp/xbl/xbl.html
BuildRoot: /var/tmp/xbl-root
Summary(de): 3D-Geometriespiel
Summary(fr): Jeu en géometrie 3D.
Summary(tr): Üç boyutlu geometri oyunu

%description
A three dimensional version of a popular arcade game.

%description -l pt_BR
Uma versão em três dimensões de um popular jogo do tipo arcade.

%description -l es
Una versión en tres dimensiones de un popular juego del tipo arcade.

%description -l de
Eine 3D-Version eines beliebten Spielhallen-Games. 

%description -l fr
Version tri-dimensionnelle d'un célèbre jeu d'arcade.

%description -l tr
Popüler oyunun üç boyutlu bir sürümü

%prep
%setup -q
%patch -p1

%build
./configure --prefix=/usr
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1,lib/X11/app-defaults}

make	RESOURCEDIR=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults \
	BINDIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
	SCOREDIR=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/xbl \
	MANPATH=$RPM_BUILD_ROOT/usr/X11R6/man \
	install

( cd $RPM_BUILD_ROOT
  strip ./usr/X11R6/bin/xbl
  mkdir -p ./etc/X11/wmconfig
#  cat > ./etc/X11/wmconfig/xbl <<EOF
#xbl name "xbl"
#xbl description "Jogo Geométrico em 3d"
#xbl group Jogos/Vídeo
#xbl exec "xbl &"
#EOF
)



tar xvfpz $RPM_SOURCE_DIR/xbl-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xbl
/usr/X11R6/lib/X11/xbl
/usr/X11R6/man/man1/xbl.1
%config /etc/X11/wmconfig/xbl

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
