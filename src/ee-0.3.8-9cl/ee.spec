# Note that this is NOT a relocatable package
%define ver      0.3.8
%define rel      9cl
%define prefix   /usr

Summary: The Electric Eyes image viewer application.
Summary(pt_BR): Electric Eyes - Visualizador de Imagens
Summary(es): Electric Eyes - Visualizador de Imágenes
Name: ee
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
# was .gz
Source0: ftp://ftp.gnome.org/pub/ee-%{ver}.tar.bz2
Source1: ee-pt_BR.po
Source800: ee-wmconfig.i18n.tgz
Patch0: ee-desktop.patch
Patch1: ee-0.3.8-pt_BR.patch
Patch2: ee-gnome-menu.patch
BuildRoot: /var/tmp/ee-%{PACKAGE_VERSION}-root
URL: http://www.gnome.org/
Requires: imlib >= 1.9.2

%description
The ee package contains the Electric Eyes image viewer for the GNOME
desktop environment.  Electric Eyes is primary an image viewer, but it
also allows many types of image manipulations.  Electric Eyes can handle
almost any type of image.

Install the ee package if you need an image viewer.

%description -l pt_BR
O visualizador de imagens Electric Eyes permite a visualização
e manipulação de uma variedade de formatos de imagens.

%description -l es
El visor de imágenes Electric Eyes permite visualizar y manejar
una variedad de formatos de imágenes.

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome menu entries for ee

* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 24 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 24 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- unset LINGUAS

* Wed Mar 24 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Wed Mar 24 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 08 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations

* Mon Feb 22 1999 Michael Fulbright <drmike@redhat.com>
- unlibtoolize

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- version 0.3.8

* Mon Feb 08 1999 Michael Fulbright <drmike@redhat.com>
- version 0.3.7

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- rebuilt for gtk+ 1.1.12

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated for GNOME freeze

* Tue Sep 22 1998 Carsten Haitzler <raster@redhat.com>
- requires imlib 1.8.1
- more minor bug fixes.

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- stuff

* Thu Aug 13 1998 Marc Ewing <marc@redhat.com>
- Initial spec file copied from gnome-graphics

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .pt_BR
%patch2 -p1 -b .gnome-menu

%build

cp $RPM_SOURCE_DIR/ee-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
[ "$LINGUAS" ] && unset LINGUAS
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make prefix=$RPM_BUILD_ROOT%{prefix} install





tar xvfpz $RPM_SOURCE_DIR/ee-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/share/gnome/help/ee
%{prefix}/share/locale/*/*/*
%{prefix}/share/gnome/apps/*
%{prefix}/share/mime-info/ee.keys
