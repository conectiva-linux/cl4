# Note that this is NOT a relocatable package
%define ver      1.0.10
%define rel      2cl
%define prefix   /usr

Summary: The libraries needed by the GNOME GUI desktop environment.
Summary(pt_BR): Bibliotecas básicas do GNOME.
Summary(es): Bibliotecas básicas del GNOME.
Name: gnome-libs
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
# Recompressed source with bzip2
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-libs/gnome-libs-%{ver}.tar.bz2
Source1: gnome.mime
Source2: gnome-libs-pt_BR.po
BuildRoot: /var/tmp/gnome-libs-%{ver}-root
Obsoletes: gnome
URL: http://www.gnome.org/
Requires: gtk+ >= 1.2.1
Requires: gnome-audio
Prereq: utempter
Patch0: gnome-libs-db1.patch
Patch1: gnome-libs-rhsnddefs.patch
Patch2: gnome-libs-1.0.5-newsession.patch
Patch3: gnome-libs-1.0.5-sndon.patch
Patch4: gnome-libs-1.0.8-nullfont.patch
Patch5: gnome-libs-1.0.10-pt_BR.patch

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on Open Source software.
The gnome-libs package includes libraries that are needed by GNOME.

You should install the gnome-libs package if you would like to use the
GNOME desktop environment.  You'll also need to install the gnome-core
package.  If you would like to develop GNOME applications, you'll also
need to install gnome-libs-devel.  If you want to use linuxconf with a
GNOME front end, you'll also need to install the gnome-linuxconf
package.

%description -l pt_BR
Bibliotecas básicas que devem ser instaladas para usar o GNOME.

GNOME é o Ambiente de Rede Modelado por Objetos da GNU. É um nome
fantasioso, mas o GNOME é realmente um bom ambiente gráfico. Ele
torna seu computador fácil, poderoso e fácil de configurar.

%description -l es
Bibliotecas básicas que deben ser instaladas para usar GNOME.
GNOME es el Ambiente de Red Modelado por Objetos de GNU. Es un nombre
fantasioso, pero GNOME es realmente un bueno ambiente gráfico. Vuelve
tu ordenador fácil, potente y fácil de configurar.

%package devel
Summary: Libraries and include files for developing GNOME applications.
Summary(pt_BR): Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações GNOME
Summary(es): Bibliotecas, archivos de inclusión, e etc. para desarrollar aplicaciones GNOME
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: gnome-libs = %{PACKAGE_VERSION}
Requires: gtk+-devel
Requires: imlib-devel
Requires: esound-devel
Requires: ORBit-devel
Obsoletes: gnome

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on Open Source software. 
The gnome-libs-devel package includes the libraries and include files that
you will need to develop GNOME applications.  

You should install the gnome-libs-devel package if you would like to
develop GNOME applications.  You don't need to install gnome-libs-devel
if you just want to use the GNOME desktop environment.  If you are going
to develop GNOME applications and/or you're going to use the GNOME desktop
environment, you'll also need to install the gnome-core and gnome-libs
packages.  If you want to use linuxconf with a GNOME front end, you'll
also need to install the gnome-linuxconf package.

%description -l pt_BR devel
Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações
GNOME

%description -l es devel
Bibliotecas, archivos de inclusión, y etc para desarrollar
aplicaciones GNOME

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated pt_BR.po

* Sun Jun 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR po to package
- Updated to version 1.0.10

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Michael Fulbright <drmike@redhat.com>
- quick patch to handle gnome-font-picker crashing when gdk_font_load()
  returns NULL

* Mon Apr 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.0.8

* Sun Mar 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 1.0.4 to 1.0.5
- fixed some patchs to fit in 1.0.5

* Fri Mar 26 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed find-requires

* Thu Mar 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt against glib/gtk+ 1.2.1 to get rid of the "accelleration"
  messages...

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- unset LINGUAS, to include all the available translations

* Mon Mar 22 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 20 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated package to gnome-libs 1.0.3 + KDE integration patches

* Sat Mar 06 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file
  
* Thu Mar 04 1999 Michael Fulbright <drmike@redhat.com>
- GNOME 1.0 woohoo

%prep
%setup -q
%patch0 -p1 -b .db1
%patch1 -p1 -b .rhsnddefs
autoconf
%patch2 -p1 -b .newsession
%patch3 -p1 -b .sndon
%patch4 -p1 -b .nullfont
%patch5 -p1 -b .pt_BR

%build

cp $RPM_SOURCE_DIR/gnome-libs-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po

[ "$LINGUAS" ] && unset LINGUAS
export CFLAGS="$RPM_OPT_FLAGS"
autoconf
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
./configure --prefix=%prefix --sysconfdir=/etc --localstatedir=/var/lib
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

# strip binaries
strip `file $RPM_BUILD_ROOT/%{prefix}/bin/* | awk -F':' '/executable/ { print $1 }'`
strip `file $RPM_BUILD_ROOT/%{prefix}/sbin/* | awk -F':' '/executable/ { print $1 }'`

# add new gnome.mimes
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{prefix}/share/mime-info/

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{prefix}/lib/lib*.so.*
%{prefix}/bin/dns-helper
%{prefix}/bin/gconfigger
%{prefix}/bin/gnome-bug
%{prefix}/bin/gnome-dump-metadata
%{prefix}/bin/gnome-gen-mimedb
%{prefix}/bin/gnome-moz-remote
%{prefix}/bin/gnome-name-service
%{prefix}/bin/gnome_segv
%{prefix}/bin/goad-browser
%{prefix}/bin/loadshlib
%{prefix}/bin/new-object
%attr(2755, root, utmp) %{prefix}/sbin/gnome-pty-helper
%{prefix}/share/locale/*/*/*
%{prefix}/share/idl/*
%{prefix}/share/pixmaps/*
%{prefix}/share/mime-info/gnome.mime
%{prefix}/share/type-convert/type.convert
%config %{prefix}/share/gtkrc*
%config /etc/*

%files devel
%defattr(-, root, root)

%doc devel-docs

%{prefix}/bin/gnome-config
%{prefix}/bin/libart-config
%{prefix}/lib/lib*.so
%{prefix}/lib/*.a
%{prefix}/lib/*.sh
%{prefix}/lib/gnome-libs
%{prefix}/include/*
%{prefix}/share/aclocal/*
%{prefix}/share/doc/*
