Summary: various geometric puzzles
Summary(pt_BR): Vários quebra-cabeças geométricos
Summary(es): Varios rompecabezas geométricos
Name: xpuzzles
Version: 5.4.1
Release: 8cl
Copyright: MIT
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
#Source: ftp://sunsite.unc.edu/pub/Linux/games/strategy/xpuzzles-5.4.1.tgz
# recompressed with bzip2
Source: ftp://sunsite.unc.edu/pub/Linux/games/strategy/xpuzzles-5.4.1.tar.bz2
Source800: xpuzzles-wmconfig.i18n.tgz
Patch: xpuzzles-5.4.1-install.patch
Patch1: xpuzzles-5.4.1-nobr.patch
BuildRoot: /var/tmp/xpuzzles-root
Summary(de): diverse geometrische Puzzles 
Summary(fr): Divers puzzles géométriques
Summary(tr): Çeþitli geometrik bulmacalar

%description
An assortment of geometric puzzles and toys, including an electronic
version of Rubik's cube, and a "dinosaur cube" program.

%description -l pt_BR
Uma seleção de quebra-cabeças geométricos e brinquedos, incluindo
uma versão eletrônica do cubo de Rubik, e um "cubo dinossauro".

%description -l es
Una selección de rompecabezas geométricos y juguetes, incluyendo
una versión electrónica del cubo de Rubik, y un "cubo dinosaurio".

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .nobr

%build
make -f xpuzzles.Makefile xmkmf
make -f xpuzzles.Makefile

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}

make -f xpuzzles.Makefile DESTDIR=$RPM_BUILD_ROOT install

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xcubes <<EOF
#xcubes name "xcubes"
#xcubes description "xcubes"
#xcubes group Jogos/Estratégia
#xcubes exec "xcubes &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xdino <<EOF
#xdino name "xdino"
#xdino description "xdino"
#xdino group Jogos/Estratégia
#xdino exec "xdino &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xhexagons <<EOF
#xhexagons name "xhexagons"
#xhexagons description "xhexagons"
#xhexagons group Jogos/Estratégia
#xhexagons exec "xhexagons &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xmball <<EOF
#xmball name "xmball"
#xmball description "xmball"
#xmball group Jogos/Estratégia
#xmball exec "xmball &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xmlink <<EOF
#xmlink name "xmlink"
#xmlink description "xmlink"
#xmlink group Jogos/Estratégia
#xmlink exec "xmlink &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xoct <<EOF
#xoct name "xoct"
#xoct description "xoct"
#xoct group Jogos/Estratégia
#xoct exec "xoct &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpanex <<EOF
#xpanex name "xpanex"
#xpanex description "xpanex"
#xpanex group Jogos/Estratégia
#xpanex exec "xpanex &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpyraminx <<EOF
#xpyraminx name "xpyraminx"
#xpyraminx description "xpyraminx"
#xpyraminx group Jogos/Estratégia
#xpyraminx exec "xpyraminx &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xrubik <<EOF
#xrubik name "xrubik"
#xrubik description "xrubik"
#xrubik group Jogos/Estratégia
#xrubik exec "xrubik &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xskewb <<EOF
#xskewb name "xskewb"
#xskewb description "xskewb"
#xskewb group Jogos/Estratégia
#xskewb exec "xskewb &"
#EOF

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xtriangles <<EOF
#xtriangles name "xtriangles"
#xtriangles description "xtriangles"
#xtriangles group Jogos/Estratégia
#xtriangles exec "xtriangles &"
#EOF




tar xvfpz $RPM_SOURCE_DIR/xpuzzles-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/X11/wmconfig/xcubes
%config /etc/X11/wmconfig/xdino
%config /etc/X11/wmconfig/xhexagons
%config /etc/X11/wmconfig/xmball
%config /etc/X11/wmconfig/xmlink
%config /etc/X11/wmconfig/xoct
%config /etc/X11/wmconfig/xpanex
%config /etc/X11/wmconfig/xpyraminx
%config /etc/X11/wmconfig/xrubik
%config /etc/X11/wmconfig/xskewb
%config /etc/X11/wmconfig/xtriangles

/usr/X11R6/bin/xpanex
/usr/X11R6/man/man1/xpanex.1
/usr/X11R6/bin/xrubik
/usr/X11R6/man/man1/xrubik.1
/usr/X11R6/bin/xskewb
/usr/X11R6/man/man1/xskewb.1
/usr/X11R6/bin/xdino
/usr/X11R6/man/man1/xdino.1
/usr/X11R6/bin/xpyraminx
/usr/X11R6/man/man1/xpyraminx.1
/usr/X11R6/bin/xoct
/usr/X11R6/man/man1/xoct.1
/usr/X11R6/bin/xmball
/usr/X11R6/man/man1/xmball.1
/usr/X11R6/bin/xcubes
/usr/X11R6/man/man1/xcubes.1
/usr/X11R6/bin/xtriangles
/usr/X11R6/man/man1/xtriangles.1
/usr/X11R6/bin/xhexagons
/usr/X11R6/man/man1/xhexagons.1
/usr/X11R6/bin/xmlink
/usr/X11R6/man/man1/xmlink.1

%changelog
* Wed Jun 16 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
