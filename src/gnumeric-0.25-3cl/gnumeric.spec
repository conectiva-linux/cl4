%define  ver     0.25
%define  rel     3cl
%define  prefix  /usr

Summary: The full-featured GNOME spreadsheet.
Summary(pt_BR): A planilha do GNOME
Summary(es): La hoja de calculo del GNOME.
Name: gnumeric
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/Productivity
Group(pt_BR): Aplicações/Produtividade
Group(es): Aplicaciones/Productividad
# was .gz
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/gnumeric/gnumeric-%{ver}.tar.bz2
Source1: gnumeric-pt_BR.po
Patch0: gnumeric-0.25-pt_BR.patch
Patch1: gnumeric-gnome-menu.patch
Url:http://www.gnome.org/gnumeric/
BuildRoot:/var/tmp/gnumeric-%{PACKAGE_VERSION}-root

%description
GNOME is the GNU Network Object Model Environment. This powerful
environment is both easy to use and easy to configure.

This package will install Gnumeric the GNOME spreadsheet
program. This program is intended to be a replacement for
a commercial spreadsheet, so quite a bit of work has gone
into the program.

Install this package if you want to use the GNOME
spreadsheet Gnumeric.

%description -l pt_BR
Este pacote instala a planilha do GNOME, que foi feita para substituir
qualquer planilha comercial, pois uma quantidade razoável de trabalho foi
(e está sendo) colocada para torná-la a melhor possível.

%description -l es
La hoja de calculo del GNOME.

%prep
%setup -q
%patch0 -p1 -b .pt_BR 
%patch1 -p1 -b .gnome-menu

%build

cp $RPM_SOURCE_DIR/gnumeric-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po

unset LINGUAS
autoconf
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome-menu entries for gnumeric

* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 3 1999 Guilherme Manika <gwm@conectiva.com>
- atualizado para 0.25

* Wed Apr 28 1999 Guilherme Manika <gwm@conectiva.com>
- atualizado para 0.23

* Sat Apr 03 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 19990403 cvs version, which fixes the about dialog bug
- fixed little buglet in es.po

* Wed Mar 31 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 0.21

* Tue Mar 30 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 0.20

* Wed Mar 24 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 08 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations

* Sun Feb 21 1999 Michael Fulbright <drmike@redhat.com>
- fixed source line and removed libtoolize from %build

* Mon Feb 11 1999 Michael Fulbright <drmike@redhat.com>
- version 0.11

* Sun Feb 07 1999 Matt Wilson <msw@redhat.com>
- version 0.9

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- version 0.8.1

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.7

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- version 0.6

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated for GNOME freeze

* Thu Sep 24 1998 Michael Fulbright <msf@redhat.com>
- Version 0.2

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING TODO

%{prefix}/bin/*
%{prefix}/lib/gnumeric/*
%{prefix}/share/*
