# Note that this is NOT a relocatable package
%define ver      1.0.1
%define rel      6cl
%define prefix   /usr

Summary: GNOME utility programs
Summary(pt_BR): Programas utilitários do GNOME
Summary(es): Programas utilitarios del GNOME
Name: gnome-utils
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
# was .gz
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-utils-%{ver}.tar.bz2
Source1: gnome-utils-pt_BR.po
Patch0: gnome-utils-1.0.1-pt_BR.patch
Patch1: gnome-utils-gnome-menu.patch
Patch2: gnome-utils-detectar-conectiva.patch
BuildRoot: /var/tmp/gnome-utils-%{PACKAGE_VERSION}-root
Obsoletes: gnome

URL: http://www.gnome.org/
Requires: gnome-libs >= 1.0.1

%description
GNOME utility programs.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pt_BR
Programas utilitários do GNOME

GNOME é o Ambiente de Rede Modelado por Objetos da GNU. É um nome
fantasioso, mas o GNOME é realmente um bom ambiente gráfico. Ele
torna seu computador fácil, poderoso e fácil de configurar.

%description -l es
Programas utilitarios del GNOME GNOME es el Ambiente de Red Modelado
por Objetos de la GNU. Es un nombre fantasioso, pero GNOME es
realmente un buen ambiente gráfico. Hace tu ordenador sencillo,
poderoso y fácil de configurar.

%changelog
* Thu Jul 01 1999 Guilherme Wunsch Manika <gwm@conectiva.com>
- included patch to detect Conectiva Linux

* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome-menu entries for gnome-utils

* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Wed Sep 23 1998 Michael Fulbright <msf@redhat.com>
- Upgraded to 0.30

* Mon Apr  6 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-utils CVS source tree

%prep
%setup -q
%patch0 -p1 -b .pt_BR
%patch1 -p1 -b .gnome-menu
%patch2 -p1 -b .ConectivaLinux

%build

cp $RPM_SOURCE_DIR/gnome-utils-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS
if [ ! -f configure ]; then
./autogen.sh --prefix=%prefix
else
autoconf
./configure --prefix=%prefix
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
%{prefix}/man/*/*
%{prefix}/share/locale/*/*/*
%{prefix}/share/pixmaps/*
%{prefix}/share/gnome/apps/*
%{prefix}/share/gnome/help/*
%{prefix}/share/gstripchart/*
