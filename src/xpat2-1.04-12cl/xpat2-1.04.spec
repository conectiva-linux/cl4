Summary: X Patience - various solitaire card games
Summary(pt_BR): X Patience - vários jogos de cartas
Summary(es): X Patience - varios juegos de cartas
Name: xpat2
Version: 1.04
Release: 12cl
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: http://metalab.unc.edu/pub/Linux/games/x11/strategy/xpat2-1.04-src.tar.bz2
Source800: xpat2-wmconfig.i18n.tgz
Patch: xpat2-1.03-fsstnd.patch
Patch1: xpat2-1.04-xpm.patch
Patch2: xpat2-1.04-nobr.patch
BuildRoot: /var/tmp/xpat2-root
Summary(de): X-Patience - diverse Solitaire-Kartenspiele 
Summary(fr): X Patience - divers jeux de solitaires
Summary(tr): X Patience - fal oyunu

%description
In 1989, Dave Lemke, Heather Rose, Donald R. Woods and Sun
Microsystems, Inc., created the xsol solitaire game (also known as
klondike under DOS) and the rules of some other patience games.  Its
main features are variable rule sets and different card sets for
different resolution monitors.

xpat2 (X Patience) is a collection of these assorted solitaire card games
that will truly "try your patience".

%description -l pt_BR
Em 1989, Dave Lemke, Heather Rose, Donald R. Woods e a Sun
Microsystems, Inc., criaram o jogo de paciência xsol (também
conhecido como klondike no DOS) e as regras de alguns outros jogos de
paciência. As características principais são variáveis com conjuntos
de regras e diferentes conjuntos de cartas para diferentes resoluções
de monitores. xpat2 (X Patience) é uma coleção destes variados
jogos de paciência que irão realmente "testar a sua paciência".

%description -l es
En 1989, Dave Lemke, Heather Rose, Donald R. Woods y la Sun
Microsystems, Inc., crearon el juego del solitario xsol (también
conocido como klondike en DOS) y las reglas de algunos otros juegos
del solitario. Las características principales son variables
con conjuntos de reglas y diferentes conjuntos de cartas para
diferentes resoluciones de monitores. xpat2 (X Patience) es una
colección de estos variados juegos de solitario que irán realmente
"probar tu solitario".

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1 -b .nobr

%build
export PATH=/usr/bin/X11:$PATH
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/{lib/games/xpat,man/man6}
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/{italian,german,russian,french}/app-defaults

make DESTDIR=$RPM_BUILD_ROOT install

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpat2 <<EOF
#xpat2 name "xpat2"
#xpat2 description "Paciência"
#xpat2 group Jogos/Estratégia
#xpat2 exec "xpat2 &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xpat2-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/games/xpat
/usr/man/man6/xpat2.6x
/usr/X11R6/bin/xpat2
%config /usr/X11R6/lib/X11/app-defaults/XPat
%config /etc/X11/wmconfig/xpat2

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Sep 17 1998 Jeff Johnson <jbj@redhat.com>
- use "mkdir -p" rather than mkdirhier to avoid IFS problem with bash-2.02.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
