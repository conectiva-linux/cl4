# Note that this is NOT a relocatable package
%define ver      0.15.5
%define rel      34cl
%define prefix   /usr

Summary: The Enlightenment window manager.
Summary(pt_BR): Enlightenment: Gerenciador de Janelas 
Summary(es): Enlightenment: Administrador de Ventanas
Name: enlightenment
Version: %ver
Release: %rel
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source: ftp://www.rasterman.com/pub/enlightenment/enlightenment-%{ver}.tar.gz
Source1: control.cfg
Source2: menus.cfg
Source3: keybindings.cfg
Source9: shinynobuttons.cfg
Source10: CleanBig.etheme
BuildRoot: /var/tmp/e-%{ver}-root
URL: http://www.enlightenment.org/

Patch1: enlightenment-0.15.5-semisolid.patch
Patch2: enlightenment-0.15.5-dirs.patch
#Patch3: enlightenment-0.15.5-shinynobuttons.patch


Patch10: enlightenment-0.15.5-focusbug.patch
Patch11: enlightenment-0.15.5-CARD32.patch
Patch12: enlightenment-0.15.5-slidoutcheck.patch
Patch13: enlightenment-0.15.5-textbug.patch
Patch14: enlightenment-0.15.5-applix.patch
Patch15: enlightenment-0.15.5-focusswap.patch
Patch16: enlightenment-0.15.5-fixleak.patch
Patch17: enlightenment-0.15.5-resizemove.patch
Patch18: enlightenment-0.15.5-lang.patch

# post-6.0 patches
Patch20: enlightenment-0.15.5-raisewin.patch
Patch21: enlightenment-0.15.5-x11R5session.patch
Patch22: enlightenment-0.15.5-swapfocus.patch

Docdir: %{prefix}/doc

%description
Enlightenment is a window manager for the X Window System that
is designed to be powerful, extensible, configurable and
pretty darned good looking! It is one of the more graphically
intense window managers.

Enlightenment goes beyond managing windows by providing a useful
and appealing graphical shell from which to work. It is open
in design and instead of dictating a policy, allows the user to 
define their own policy, down to every last detail.

This package will install the Enlightenment window manager.

%description -l pt_BR
O Enlightenment é um gerenciador de janelas para o X Window System
que foi desenvolvido parar ser poderoso, extensível, configurável e
com um excelente visual! Ele é um dos gerenciadores de janelas com
mais características gráficas.

%description -l es
El Enlightenment es un administrador de ventanas para el X Window.
Se hizo para ser extensible, rico en características y de configuración
fácil.

%changelog
* Sat Jun 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Made "Clean" the default theme for us

* Tue May 25 1999 Michael Fulbright <drmike@redhat.com>
- added raster's patch to handle focus issues when switching desktops

* Mon May 10 1999 Michael Fulbright <drmike@redhat.com>
- added raster's patch to raise windows when gnomepager tasklist clicked
- added raster's patch to handle x11r5 sm apps more completely

* Mon Apr 19 1999 Michael Fulbright <drmike@redhat.com>
- fixed leak in enlightenment when titles change
- fixed language handling so tooltip time ok with lang change
- fixed bug where windows are corrupted if moved while resized

* Thu Apr 15 1999 Michael FUlbright <drmike@redhat.com>
- fixed bug involved click to focus and switching desktops

* Wed Apr 14 1999 Michael Fulbright <drmike@redhat.com>
- CleanBig has resize border on top now

* Mon Apr 12 1999 Michael Fulbright <drmike@redhat.com>
- fixed applix iconization bug

* Sat Apr 10 1999 Michael Fulbright <drmike@redhat.com>
- removed ShinyMetal theme - crashes when I try it.
  Raster will take a look at it later.

* Fri Apr 09 1999 Michael Fulbright <drmike@redhat.com>
- fixed focus/emacs bug

* Thu Apr 08 1999 Michael Fulbright <drmike@redhat.com>
- fixed cleanbig theme tooltips and font size

* Mon Apr 05 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15.5 plus semisolid drag fix
- made CleanBig the default theme

* Wed Mar 31 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15.5

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries

* Wed Mar 17 1999 Michael Fulbright <drmike@redhat.com>
- added patch to fix panel orientation drawing problems
- removed the CNTL-ALT-K binding, which killed a window nasty
  This conflicts with emacs and possible other app bindings

* Sun Mar 14 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15.2

* Wed Feb 24 1999 The Rasterman <raster@redhat.com>
- updated to latest source and upped release (rel 35)

* Wed Feb 24 1999 The Rasterman <raster@redhat.com>
- updated to latest source and upped release

* Tue Feb 23 1999 The Rasterman <raster@redhat.com>
- updated to latest source and upped release

* Sun Feb 21 1999 Michael Fulbright <drmike@redhat.com>
- removed libtoolize from build

* Tue Feb 11 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.15.0-19990210, rpm release 21

* Mon Feb 08 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.15.0-19990208, rpm release 20

* Mon Feb 08 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.15.0-19990207, rpm release 19

* Sat Feb 06 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.15.0-19990206

* Fri Feb 05 1999 Michael Fulbright <drmike@redhat.com>
- update to 0.15.0-19990205

* Wed Feb 04 1999 Michael Fulbright <drmike@redhat.com>
- fixed symlink for clean theme

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15.0-19990203.tar.gz

* Wed Jan 28 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15.0-19990128.tar.gz

* Tue Jan 27 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15.0-19990127.tar.gz
- new Classic theme version 0.5

* Mon Jan 25 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15.0-19990125.tar.gz
- new Classic theme version 0.4

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15-19990120

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15-990119

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.15-990115

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- incoporated version 0.3 of Classic theme
- latest snapshot of e from CVS

* Fri Dec 18 1998 Michael Fulbright <drmike@redhat.com>
- incoporated version 0.2 of Classic theme, incorporating wanger fixes

* Thu Dec 17 1998 Michael Fulbright <drmike@redhat.com>
- fixed menu button on window to not have 'Close' as first entry
- added Rasters fix for desktop areas and losing windows

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- hacked in conservative theme
- preparing for GNOME freeze

* Fri Nov 20 1998 Michael Fulbright <drmike@redhat.com>
- updated for pre-dr15

* Fri Sep 11 1998 Mandrake <mandrake@mandrake.net>
- changed rev num, also incremented imlib requirement to 1.8

* Tue Jun 2 1998 The Rasterman <raster@redhat.com>
- wrote .spec file


%prep
%setup -q

%patch1 -p0 -b .semisolid
%patch2 -p1 -b .dirs
#%patch3 -p1 -b .shinynobuttons
autoconf

%patch10 -p1 -b .focusbug
%patch11 -p1 -b .CARD32
%patch12 -p1 -b .slideoutcheck
%patch13 -p1 -b .textbug
%patch14 -p1 -b .applix
%patch15 -p1 -b .focusswap
%patch16 -p1 -b .fixleak
%patch17 -p1 -b .resizemove
%patch18 -p1 -b .lang

%patch20 -p1 -b .raisewin
%patch21 -p1 -b .x11R5sm
%patch22 -p1 -b .swapfocus

cp -f %{SOURCE10} $RPM_BUILD_DIR/enlightenment-%{PACKAGE_VERSION}/src/themes

%build

CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --enable-fsstd
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

#
# set default control
#

install -c -m 664 %{SOURCE1} $RPM_BUILD_ROOT%{prefix}/share/enlightenment/config/
install -c -m 664 %{SOURCE2} $RPM_BUILD_ROOT%{prefix}/share/enlightenment/config/
install -c -m 664 %{SOURCE3} $RPM_BUILD_ROOT%{prefix}/share/enlightenment/config/


#
# set default theme
#
rm -f $RPM_BUILD_ROOT%{prefix}/share/enlightenment/themes/DEFAULT
ln -sf Clean $RPM_BUILD_ROOT%{prefix}/share/enlightenment/themes/DEFAULT

# fix shiny metal to have no desktop buttons
install -c -m 664 %{SOURCE9} $RPM_BUILD_ROOT%{prefix}/share/enlightenment/themes/ShinyMetal/buttons.cfg


# I don't know what E's install script does, but it has issues on the alpha
# build machine because of the uid/gid of these files.
cd $RPM_BUILD_ROOT%{prefix}/share/enlightenment
chown -R 0.0 *

# strip binaries
strip `file $RPM_BUILD_ROOT/%{prefix}/bin/* | awk -F':' '/executable/ { print $1 }'`


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(-, root, root)

%{prefix}/share/enlightenment/*
%{prefix}/bin/*

%doc AUTHORS COPYING INSTALL ChangeLog NEWS README TODO
