# Note that this is NOT a relocatable package
%define ver      0.22
%define rel      2cl
%define prefix   /usr

Summary: The GNOME front-end for linuxconf.
Summary(pt_BR): Interface GNOME para o linuxconf
Summary(es): Interface GNOME para linuxconf
Name: gnome-linuxconf
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
# was .gz
Source0: gnome-linuxconf-%{ver}.tar.bz2
Source1: linuxconf.desktop
Source800: gnome-linuxconf-wmconfig.i18n.tgz
BuildRoot: /tmp/gnome-linuxconf-root
URL: http://www.gnome.org/
Conflicts: linuxconf < 1.14

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on Open Source software. 
The gnome-linuxconf package includes GNOME's front end for the linuxconf
system configuration utility.

You should install the gnome-linuxconf package if you would like to use
GNOME's linuxconf front end. You'll also need to install the gnome-core
and gnome-libs packages.  If you would like to develop GNOME applications,
you'll also need to install gnome-libs-devel.

%description -l pt_BR
Interface gráfica para o sistema de configuração linuxconf

%description -l es
Interface gráfica para el sistema de configuración linuxconf


%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr 13 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 0.22

* Sun Mar 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 0.20

* Thu Mar 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated package to version 0.19

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Thu Feb 25 1999 Bill Nottingham <notting@redhat.com>
- new summary/description, applink entry

* Tue Feb 16 1999 Michael Fulbright <drmike@redhat.com>
- Rebuilt against gnome-libs 0.99.8

* Sun Feb 07 1999 Michael Johnson <johnsonm@redhat.com>
- New version now builds against Gtk 1.1.15 as well

* Mon Jan 25 1999 Michael Johnson <johnsonm@redhat.com>
- new improved version, should build both with GNOME 0.20/Gtk 1.0.x
  and with GNOME 0.99.x/Gtk 1.1.x

* Thu Oct 29 1998 Michael Johnson <johnsonm@redhat.com>
- imported back into official gnome tree, new version to celebrate!

* Thu Oct 01 1998 Michael K. Johnson <johnsonm@redhat.com>
- library fix

* Mon Sep 28 1998 Michael K. Johnson <johnsonm@redhat.com>
- fixed lots of bugs, now has treemenu mode

* Thu May 07 1998 Michael K. Johnson <johnsonm@redhat.com>
- linuxconf 1.11r11 handles fast connections appropriately.

* Tue May 05 1998 Michael K. Johnson <johnsonm@redhat.com>
- ignore SIGTSTP to work around suspected gtk bug
- fix use of vsnprintf()
- fix port 98 remadmin connections
- fixed resizing bug without completely changing layout

* Mon May 04 1998 Michael K. Johnson <johnsonm@redhat.com>
- fixed resizing bug
- added wmconfig entry for linuxconf

* Sat May 02 1998 Michael K. Johnson <johnsonm@redhat.com>
- fixed radio buttons, deal with "rich text"
- improved justification follows remadmin standard more closely

* Fri May 01 1998 Michael K. Johnson <johnsonm@redhat.com>
- fixes radio buttons and combo boxes
- work around small gnome problems

* Wed Apr 29 1998 Michael K. Johnson <johnsonm@redhat.com>
- takes title widths into account, so works with 0-length clists

* Thu Apr 16 1998 Michael K. Johnson <johnsonm@redhat.com>
- Now works with linuxconf 1.10r21
- Fixed a few more display problems.

* Wed Apr 15 1998 Michael K. Johnson <johnsonm@redhat.com>
- New io engine, some other improvements, make this really usable.

* Thu Apr 09 1998 Michael K. Johnson <johnsonm@redhat.com>
- Make a linuxconf-only package.  Final intent is to split gnome
  packages out more finely-grained than the current CVS tree.

* Mon Mar 16 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-admin CVS source tree

%prep
%setup -q

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS
if [ -x ./configure ] ; then
  ./configure --prefix=%{prefix}
else
  ./autogen.sh --prefix=%{prefix}
fi

%build

make

%install

mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
install -m 755 gnome-linuxconf $RPM_BUILD_ROOT%{prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/rhs/control-panel/
install -m 644 linuxconf.xpm $RPM_BUILD_ROOT%{prefix}/lib/rhs/control-panel/
install -m 755 linuxconf.init $RPM_BUILD_ROOT%{prefix}/lib/rhs/control-panel/
mkdir -p $RPM_BUILD_ROOT/etc/X11/applink/System
install -m 600 %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applink/System/linuxconf.desktop
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig




tar xvfpz $RPM_SOURCE_DIR/gnome-linuxconf-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files

%{prefix}/bin/gnome-linuxconf
%{prefix}/lib/rhs/control-panel/*
/etc/X11/applink/System/linuxconf.desktop
/etc/X11/wmconfig/linuxconf
