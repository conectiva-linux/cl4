# Note that this is NOT a relocatable package
%define ver      1.0.5
%define rel      25cl
%define prefix   /usr

Summary: The GNOME control center.
Summary(pt_BR): O Centro de Controle do GNOME
Summary(es): El centro de controle del GNOME.
Name: control-center
Version: %ver
Release: %rel
Copyright: LGPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/control-center/control-center-1.0.5.tar.bz2
Source1: control-center.png
Source2: gnomecc.desktop
Source3: control-center-pt_BR.po
BuildRoot: /var/tmp/control-center-%{PACKAGE_VERSION}-root
Obsoletes: gnome
URL: http://www.gnome.org
Docdir: %{prefix}/doc
Patch0: control-center-nosound.patch
Patch1: control-center-esdrelease.patch
Patch2: control-center-bgcolor1.patch
Patch3: control-center-fsbgpath.patch
Patch4: control-center-1.0.5-dontstartesd.patch
Patch5: control-center-1.0.5-newsession.patch
Patch6: control-center-1.0.5-fixclosedlg.patch 
Patch7: control-center-1.0.5-limitedbgs.patch
Patch8: control-center-1.0.5-smfixtry.patch
Patch9: control-center-1.0.5-quietdebug.patch
Patch10: control-center-1.0.5-geditfixtry.patch
Patch11: control-center-1.0.5-addmime.patch
Patch20: control-center-1.0.5-noscreensaver.patch
Patch21: control-center-1.0.5-numwallpapers.patch
Patch22: control-center-1.0.5-warning.patch
Patch24: control-center-1.0.5-newfocus.patch
Patch25: control-center-1.0.5-pt_BR.patch
Patch26: control-center-1.0.5-gnome-menu.patch
Patch27: control-center-1.0.5.desktop.diff
Requires: xscreensaver >= 3.08

%description
Control-center is a configuration tool for easily
setting up your GNOME environment.

GNOME is the GNU Network Object Model Environment. That's
a fancy name, but really GNOME is a nice GUI desktop 
environment. 

It's a powerful, easy to configure environment which
helps to make your computer easy to use.

%description -l pt_BR
O control-center é uma ferramenta para facilmente
configurar seu ambiente GNOME.

%description -l es
El control-center es una herramienta para una configuración
facilitada el entorno GNOME.

%package devel
Summary: GNOME control-center development files.
Summary(pt_BR): Arquivos para desenvolvimento com o control-center do GNOME.
Summary(es): Archivos para desarrollo con el control-center del GNOME
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: control-center = %{PACKAGE_VERSION}
Requires: gnome-libs-devel

%description devel
If you're interested in developing panels for the GNOME
control center, you'll want to install this package.

Control-center-devel helps you create the 'capplets'
which are used in the control center.

%description -l pt_BR devel
Se você estiver interessado em desenvolver painéis para o
centro de controle do GNOME este pacote será necessário.

O control-center-devel lhe a ajuda na criação de 'capplets',
que são usados no centro de controle.

%description -l es devel
Archivos para desarrollo con el control-center del GNOME

%changelog
* Thu Jul 01 1999 Rodrigo Stulzer Lopes <rodrigo@conectiva.com>
- Updated pt_BR.po
- Added more gnome-menu entries for control-center

* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome menu entries for control-center

* Wed Jun 23 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Mon Jun 14 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Apr 07 1999 Michael Fulbright <drmike@redhat.com>
- fixed sound-properties to only disable sound when run with --init-settings-..
- removed debugging output from several capplets, fixed try behaviour of sm and
  gnome-edit capplets
- fixed bug in screensaver and background props
- added new icons

* Mon Apr 05 1999 Jonathan Blandford <jrb@redhat.com>
- added a patch to fix the close dialog
- added a patch to limit the number of bg's in the history.

* Fri Apr 02 1999 Jonathan Blandford <jrb@redhat.com>
- vesion 1.0.5
- removed all patches >10 other then dontstartesd.

* Thu Apr 01 1999 Michael Fulbright <drmike@redhat.com>
- removed UI props till it works better

* Wed Mar 31 1999 Michael Fulbright <drmike@redhat.com>
- make sure we DONT inadvertantly start esd by calling esd_open_...

* Tue Mar 30 1999 Michael Fulbright <drmike@redhat.com>
- changed default bg color to '#356390'

* Thu Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- prime file selector path for browse in background-props if 
  "/usr/share/pixmaps/backgrounds/" exists.
- fix behavior of file selector when you delete/cancel/ok it

* Wed Mar 24 1999 Michael Fulbright <drmike@redhat.com>
- added patch to fix trying in theme selector 
- disabled crystal screensaver, it does evil things to preview in capplet

* Mon Mar 22 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.4, fixes problems with sndprops and theme props among
  other things.

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- fix sound-properties capplet so Try/Revert doesnt come on unless user
  changes something
- fixed theme-selector to not leave processes behind on Linux 2.2 kernels
- strip binaries

* Sun Mar 14 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.3
- added patch to make esd release after 30 sec of inactivity

* Wed Mar 10 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.2
- turned off sound by default

* Thu Mar 04 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.1

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.8.1
- added etc/CORBA/servers/* to file list

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.99.8
- added /usr/lib/cappletConf.sh

* Mon Feb 08 1999 The Rasterman <raster@redhat.com>
- update to 0.99.5.1

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.99.5

* Mon Jan 20 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.99.3.1

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.99.3
- seems like patch for non-standard xscreensaver placement was already in
  prestine sources(?)

* Wed Jan 06 1999 Jonathan Blandford <jrb@redhat.com>
- updated to 0.99.1
- temporary hack patch to get path to work to non-standard placement
  of xscreensaver binaries in RH 5.2

* Wed Dec 16 1998 Jonathan Blandford <jrb@redhat.com>
- Created for the new control-center branch


%prep
%setup -q
%patch0 -p1 -b .nosound
%patch1 -p1 -b .esdrelease
%patch2 -p1 -b .bgcolor1
%patch3 -p1 -b .fsbgpath
%patch4 -p1 -b .dontstartesd
%patch5 -p1 -b .newsession
%patch6 -p1 -b .fixclosedlg
%patch7 -p1 -b .limitedbgs
%patch8 -p1 -b .smfixtry
%patch9 -p1 -b .quietdebug
%patch10 -p1 -b .gedittry
%patch11 -p1 -b .addmime

%patch20 -p1 -b .noscreensaver
%patch21 -p1 -b .numwallpapers
%patch22 -p1 -b .warning

%patch24 -p1 -b .newfocus

%patch25 -p1 -b .pt_BR
%patch26 -p1 -b .gnome-menu
%patch27 -p1 -b .gnome-menu

# install new desktop entry and icon
cp %{SOURCE1} $RPM_BUILD_DIR/control-center-%{PACKAGE_VERSION}/control-center
cp %{SOURCE2} $RPM_BUILD_DIR/control-center-%{PACKAGE_VERSION}/control-center

%build

cp $RPM_SOURCE_DIR/control-center-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po

unset LINGUAS
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

# clear out ui props for now
rm -f $RPM_BUILD_ROOT%{prefix}/bin/ui-properties
rm -rf $RPM_BUILD_ROOT%{prefix}/share/control-center/UIOptions
rm -rf $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Settings/UIOptions

# strip binaries
strip `file $RPM_BUILD_ROOT/%{prefix}/bin/* | awk -F':' '/executable/ { print $1 }'`

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/lib/lib*.so.*
%config /etc/CORBA/servers/*
%{prefix}/share/control-center
%{prefix}/share/pixmaps/*
%{prefix}/share/locale/*/*/*
%{prefix}/share/gnome/wm-properties/*
%{prefix}/share/gnome/apps/Settings/*

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/lib/*Conf.sh
%{prefix}/share/idl
%{prefix}/include/*
