Summary: interpreter for Infocom compatible text adventure games
Summary(pt_BR): Interpretador para jogos tipo adventure compatíveis com Infocom
Summary(es): Interpretador para juegos tipo adventure compatibles con Infocom
Name: pinfocom
Version: 3.0
Release: 12cl
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
# was .Z
Source0: ftp://ftp.gmd.de/if-archive/infocom/interpreters/old/pinfocom/pinfocom-3.0.tar.bz2
Source1: ftp://ftp.gmd.de/if-archive/infocom/interpreters/old/pinfocom/pinfocom-docs-3.0.tar.bz2
Patch: pinfocom-3.0-config.patch
BuildRoot: /var/tmp/pinfocom-root
Summary(de): Interpretierer für Infocom-kompatible Textadventures 
Summary(fr): Interpréteur pour les jeux d'aventure en mode texte compatibles Infocom
Summary(tr): Infocom uyumlu, metin ekran macera oyunu yorumlayýcý
%description
`pinfocom' is an interpreter for those old Infocom-compatible text adventure
games (remember those?).

%description -l pt_BR
Pinfocom é um interpretador para aqueles velhos jogos adventure
modo texto compatíveis com Infocom (lembra-se deles?).

%description -l es
Pinfocom es un interpretador para aquellos antiguos juegos adventure
modo texto compatibles con Infocom (¿acuérdate de ellos?).

%description -l de
`pinfocom' ist ein Interpreter für diese alten Infocom-kompatiblen Text-
Adventures. Erinnern Sie sich?.

%description -l fr
« pinfocom » est un interpréteur pour ces vieux jeux d'aventure en mode texte
compatibles Infocom (vous vous en rappelez ?).

%description -l tr
pinfocom, eski tarz, Infocom-uyumlu, metin ekran macera oyunlarý (hatýrlar
mýsýnýz?) için bir yorumlayýcýdýr.

%prep
%setup -q
%setup -q -T -D -a 1
%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{games,man/man1}

install -m 0755 -s pinfo $RPM_BUILD_ROOT/usr/games/pinfo
install -m 0644 pinfo.man $RPM_BUILD_ROOT/usr/man/man1/pinfo.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.ps NEWS README MANIFEST
/usr/games/pinfo
/usr/man/man1/pinfo.1

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- updated/cleaned spec file

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- built against a readline library w/ proper soname info
