Summary: interpreter for Scott Adams format text adventure games
Summary(pt_BR): Interpretador para jogos de aventura no formato Scott Adams
Summary(es): Interpretador para juegos de aventura en formato Scott Adams
Name: scottfree
Version: 1.14
Release: 9cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://ftp.gmd.de/if-archive/scott-adams/ScottFree.tar.gz
Source2: scottfree
Patch: ScottFree-curses.patch
BuildRoot: /var/tmp/scottfree-root
Summary(de): Interpretierer für Text-Adventures im Scott-Adams-Format 
Summary(fr): Interpréteur pour jeux d'aventure texte Scott Adams
Summary(tr): Scott Adams formatýnda metin ekran macera oyunlarý için yorumlayýcý

%description
`scottfree' is an interpreter for Scott-Adams-format text adventure games
(remember those?).

%description -l pt_BR
"scottfree" é um interpretador para jogos adventure de Scott Adams
de formato texto (lembra-se deles?).

%description -l es
"scottfree" es un interpretador para juegos adventure de Scott
Adams de formato texto (¿Acuérdate de ellos?).

%description -l de
`scottfree' ist ein Interpreter für Scott-Adams-ähnliche Text-Adventures
(erinnern Sie sich?).

%description -l fr
`scottfree' est un interpréteur pour les jeux d'aventure au format texte
Scott-Adams-format (vous vous souvenez de ça ?).

%description -l tr
scottfree, Scott-Adams-formatý, metin ekran macera oyunlarý için bir
yorumlayýcýdýr.

%prep
%setup -q -c
%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{games,lib/games/scottfree}

install -s -m 755 ScottCurses $RPM_BUILD_ROOT/usr/lib/games/scottfree/runtime
install -m 755 $RPM_SOURCE_DIR/scottfree $RPM_BUILD_ROOT/usr/games/scottfree

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%doc Definition
%dir /usr/lib/games/scottfree
/usr/lib/games/scottfree/runtime
/usr/games/scottfree

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
