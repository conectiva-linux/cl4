Name: quakeworld
Version: 2.30
Release: 5cl
Summary: QuakeWorld for linux
Summary(pt_BR): Cliente QuakeWorld para linux
Summary(es): Cliente QuakeWorld para linux
Source: ftp://ftp.idsoftware.com/idstuff/quakeworld/qwcl-2.30-glibc-i386-unknown-linux2.0.tar.gz
Source1: quakew
Source2: xquakew
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
URL: http://www.idsoftware.com/
Requires: svgalib >= 1.3.0
Requires: quake-levels-shareware
BuildRoot: /tmp/quakeworld

%description
QuakeWorld Client

%description -l pt_BR
Cliente QuakeWorld para Linux.

%description -l es
Cliente QuakeWorld para Linux.

%package X11
Summary: QuakeWorld for Linux/X11
Summary(pt_BR): Cliente QuakeWorld para linux/X11
Summary(es): Cliente QuakeWorld para linux/X11
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
%description X11
QuakeWorld Client

%description -l pt_BR X11
Cliente QuakeWorld para Linux/X11.

%description -l es X11
Cliente QuakeWorld para Linux/X11.

%prep

%setup -c

%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin

strip qwcl
strip glqwcl
strip qwcl.x11
install -m 755 -o 0 -g 0 qwcl $RPM_BUILD_ROOT/usr/bin
install -m 755 -o 0 -g 0 qwcl.x11 $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 755 -o 0 -g 0 $RPM_SOURCE_DIR/quakew $RPM_BUILD_ROOT/usr/bin
install -m 755 -o 0 -g 0 $RPM_SOURCE_DIR/xquakew $RPM_BUILD_ROOT/usr/X11R6/bin

%files
/usr/bin/qwcl
/usr/bin/quakew
%doc README.qwcl

%files X11
/usr/X11R6/bin/xquakew
/usr/X11R6/bin/qwcl.x11

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed spec file wrt rpm 3.0.2

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Nov 27 1998 Conectiva <dist@conectiva.com>
- acertado o Grupo

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Aug 31 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 2.30
