# Note that this is NOT a relocatable package
%define ver      1.0.1
%define rel      6cl
%define prefix   /usr

Summary: GNOME media programs
Summary(pt_BR): Programas multim�dia do GNOME.
Summary(es): Programas multimedia del GNOME.
Name: gnome-media
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/Multimedia
Group(pt_BR): Aplica��es/Multim�dia
Group(es): Aplicaciones/Multimedia
# was .gz
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-media-%{ver}.tar.bz2
Source1: gnome-media-pt_BR.po
Patch0: gnome-media-1.0.1-pt_BR.patch
Patch1: gnome-media-gnome-menu.patch
BuildRoot: /var/tmp/gnome-media-%{PACKAGE_VERSION}-root
Obsoletes: gnome
URL: http://www.gnome.org/
Requires: gnome-libs >= 1.0.1
Summary(fr): Programmes multim�dia de GNOME

%description
GNOME media programs.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pt_BR
Programas multim�dia do GNOME.

GNOME � o Ambiente de Rede Modelado por Objetos da GNU. � um nome
fantasioso, mas o GNOME � realmente um bom ambiente gr�fico. Ele
torna seu computador f�cil, poderoso e f�cil de configurar.

%description -l es
Programas multimedia del GNOME.  GNOME es el Ambiente de Red
Modelado por Objetos de la GNU. Es un nombre fantasioso, pero GNOME
es realmente un buen ambiente gr�fico. Hace tu ordenador sencillo,
potente y f�cil de configurar.

%description -l fr
Programmes multim�dia GNOME.

GNOME (GNU Network Object Model Environment) est un environnement graphique
de type bureau. Il rends l'utilisation de votre ordinateur plus facile,
agr�able et eficace, et est facile � configurer.

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated gnome-menu entries for gnome-media

* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome-menu entries for gnome-media

* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- some fixes (LINGUAS, etc)

* Sun Mar 07 1999 Rodrigo Parra Novo <rodavus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Sat Nov 21 1998 Pablo Saratxaga <srtxg@chanae.alphanet.ch>
- added spanish and french translations for rpm

* Wed Sep 23 1998 Michael Fulbright <msf@redhat.com>
- Updated to 0.30 release

* Mon Mar 16 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-media CVS source tree

%prep
%setup -q
%patch0 -p1 -b .pt_BR
%patch1 -p1 -b .gnome-menu

%build

cp $RPM_SOURCE_DIR/gnome-media-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS

if [ ! -f configure ]; then
%ifarch alpha
  ./autogen.sh --host=alpha-conectiva-linux --prefix=%prefix 
%else
  ./autogen.sh --prefix=%prefix 
%endif
else
%ifarch alpha
autoconf
./configure --host=alpha-conectiva-linux --prefix=%prefix
%else
autoconf
./configure --prefix=%prefix 
%endif
fi

make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/share/locale/*/*/*
%{prefix}/share/gnome/apps/*
%{prefix}/share/pixmaps/*
