# Note that this is NOT a relocatable package
%define ver      1.0.5
%define rel      5cl
%define prefix   /usr

Summary: The core programs for the GNOME GUI desktop environment.
Summary(pt_BR): Programas principais do GNOME
Summary(es): Programas principales del GNOME
Name: gnome-core
Version: %ver
Release: %rel
Copyright: LGPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
# was .gz
Source: ftp://ftp.gnome.org/pub/gnome-core-%{ver}.tar.bz2
Source1: netscape.png
Source2: Settings.order
Source3: gnome-core-pt_BR.po
Patch1: gnome-core-1.0.4-defaults.patch
Patch3: gnome-core-1.0.0-smallpager.patch
Patch4: gnome-core-1.0.0-smallfont.patch
Patch5: gnome-core-mergerhmenus.patch
Patch6: gnome-core-1.0.3-kdemenus.patch
Patch7: gnome-core-1.0.5-pt_BR.patch
Patch8: gnome-core-gnome-menu.patch
BuildRoot: /var/tmp/gnome-core-%{PACKAGE_VERSION}-root
Obsoletes: gnome
URL: http://www.gnome.org/
Prereq: info
Requires: enlightenment >= 0.15.0
Requires: xscreensaver

%description
GNOME (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME is based completely on Open Source
software.  The gnome-core package includes the basic programs and
libraries that are needed to install GNOME.

You should install the gnome-core package if you would like to use the
GNOME desktop environment.  You'll also need to install the gnome-libs
package.  If you want to use linuxconf with a GNOME front end, you'll
also need to install the gnome-linuxconf package.

%description -l pt_BR
Programas e bibliotecas básicas que são necessárias para qualquer
instalação do GNOME.

GNOME é o Ambiente de Rede Modelado por Objetos da GNU. É um nome
fantasioso, mas o GNOME é realmente um bom ambiente gráfico. Ele
torna seu computador fácil, poderoso e fácil de configurar.

%description -l es
Programas y bibliotecas básicas que son necesarias para cualquier
instalación del GNOME.  GNOME es el Ambiente de Red Modelado por
Objetos de la GNU. Es un nombre fantasioso, pero GNOME es realmente
un bueno ambiente gráfico. Vuelve tu ordenador fácil, potente y
fácil de configurar.

%package devel
Summary: GNOME core libraries, includes and more.
Summary(pt_BR): Bibliotecas e arquivos de inclusão do painel do gnome.
Summary(es): Bibliotecas y archivos de inclusión do panel del gnome.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: gnome-core
PreReq: info

%description devel
Panel libraries and header files for creating GNOME panels.

%description -l pt_BR devel
Bibliotecas e arquivos de inclusão do painel do gnome.

%description -l es devel
Bibliotecas y archivos de inclusión del panel del gnome.

%changelog
* Thu Jul 01 1999 Rodrigo Stulzer Lopes <rodrigo@conectiva.com>
- Updated gnome-menu entries for gnome-core

* Tue Jun 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated pt_BR.po to gnome-core 1.0.5

* Wed Jun 23 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.0.5

* Sun Mar 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.0.4
- reverted the reversion of gsm
- redid some of the patches
- fixed /usr/share/locale

* Fri Mar 26 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed prereq

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 22 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Tue Mar 16 1999 Michael Fulbright <drmike@redhat.com>
- make all tiles grey by default
- reverted gsm code back to 1.0.1 code so startup properties will work
- made misc-fixed font default so we get pipe characters back
- moved /etc/X11/applink to /etc/X11/applnk

* Sun Mar 14 1999 Michael Fulbright <drmike@redhat.com>
- rebuilt against libghttp 1.0.0
- added kde menu reading code

* Thu Mar 11 1999 Michael Fulbright <drmike@redhat.com>
- added requirement for enlightenment
- added code to merge RH gnome desktop entries into panel menu

* Wed Mar 10 1999 Michael Fulbright <drmike@redhat.com>
- rebuild against gnome-libs with db1

* Sun Feb 21 1999 Michael Fulbright <drmike@redhat.com>
- removed libtoolize from %build

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- 0.99.8.1 release
- replaced bad netscape.png with acceptable one
- updated file list

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- 0.99.8 release

* Mon Feb 08 1999 Michael Fulbright <drmike@redhat.com>
- 0.99.7 release with empty dir panel menu hack

* Sat Feb 06 1999 Michael Fulbright <drmike@redhat.com>
- fixed default session to use enlightenment (again)

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.5.1

* Fri Jan 22 1999 Michael Fulbright <drmike@redhat.com>
- fixed default session to run enlightenment

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.3.2

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.2

* Thu Dec 17 1998 Michael Fulbright <drmike@redhat.com>
- hacked in new default page and logo for help-browser

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated to 0.99.0 for GNOME freeze

* Sat Nov 21 1998 Pablo Saratxaga <srtxg@chanae.alphanet.ch>
- Cleaned %files section
- added spanish and french translations for rpm

* Wed Sep 23 1998 Michael Fulbright <msf@redhat.com>
- Built 0.30 release

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-core CVS source tree

%prep
%setup -q

%patch1 -p1 -b .defaults
%patch3 -p1 -b .smallpager
%patch4 -p1 -b .smallfont
#%patch5 -p1 -b .mergerhmenus
#%patch6 -p1 -b .kdemenus
%patch7 -p1 -b .pt_BR
%patch8 -p1 -b .gnome-menu

%build

export CFLAGS="-DHAVE_CONTROL_CENTER $RPM_OPT_FLAGS"
export CXXFLAGS="-DHAVE_CONTROL_CENTER $RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS

cp $RPM_SOURCE_DIR/gnome-core-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po

autoconf
./configure --prefix=%prefix --with-window-manager=enlightenment --sysconfdir=/etc

make


%install

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

#
# this is in gnome-libs now?
#
#rm -f $RPM_BUILD_ROOT%{prefix}/share/pixmaps/gnome-default.png

cp %{SOURCE1} $RPM_BUILD_ROOT%{prefix}/share/pixmaps/
cp %{SOURCE2} $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Settings/.order

#
# clean out unneeded desktop entries
#
rm -f $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications/Netscape.desktop
rm -f $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications/Emacs.desktop

#
%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/lib/lib*.so.*
%{prefix}/share/applets
%{prefix}/share/mc/templates
%{prefix}/share/locale/*/*/*
%{prefix}/share/pixmaps/*
%{prefix}/share/xmodmap/*
%config /etc/*
%config %{prefix}/share/panelrc
%{prefix}/share/gnome/apps/*
%{prefix}/share/gnome/apps/.order
%{prefix}/share/gnome/help/*
%config %{prefix}/share/gnome/default.session
%config %{prefix}/share/gnome/default.wm

%files devel
%defattr(-, root, root)

%{prefix}/lib/*.sh
%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/include/*
%{prefix}/share/idl
