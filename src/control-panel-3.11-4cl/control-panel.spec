Summary: A Red Hat program launcher for the X Window System.
Summary(pt_BR): Painel de Controle Red Hat
Summary(es): Panel de Control Red Hat
Name: control-panel
Version: 3.11
Release: 4cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: control-panel-%{PACKAGE_VERSION}.tar.gz
Source800: control-panel-wmconfig.i18n.tgz
BuildRoot: /var/tmp/control-panel-root

%description
The Red Hat control panel is a configuration program launcher 
for the X Window System. Both convenient and pleasing, the 
Red Hat control panel allows you easy access to numerous X-based
system administration tools included in your Red Hat Linux
system.

Eventually, you'll want to work with many of your system
administration tools; this package helps you locate and launch
many of them.

%description -l pt_BR
O control-panel (painel de controle) Red Hat é um programa X que
executa várias ferramentas de configuração. Outros pacotes oferecem
informação que permitem a visualização das ferramentas disponíveis
no menu do control-panel.

%description -l es
Control-panel (panel de control) Red Hat es un programa X que
ejecuta varias herramientas de configuración. Otros paquetes ofrecen
información que permiten la visualización de las herramientas
disponibles en el menú del panel de control.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT

#rm -rf /usr/lib/rhs/control-panel/loopy
mkdir -p /usr/lib/rhs/control-panel
make DESTDIR=$RPM_BUILD_ROOT OWNER= install install-man

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig






tar xvfpz $RPM_SOURCE_DIR/control-panel-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/control-panel
/usr/man/man8/control-panel.8
/usr/lib/rhs/control-panel/loopy
/usr/lib/rhs/control-panel/dialog.tcl
/usr/lib/rhs/control-panel/bindings.tcl
%config /etc/X11/applnk/System/control-panel.desktop

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Mar 27 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- added Group, Summary and %description translations

* Wed Mar 17 1999 Michael Fulbright <drmike@redhat.com>
- quick hack so orientation change will work

* Tue Mar 09 1999 Michael Fulbright <drmike@redhat.com>
- fixed problem due to switching to gtk+ 1.2

* Tue Feb 23 1999 Michael Johnson <johnsonm@redhat.com>
- updated text
- moved to desktop files from wmconfig files

* Mon Dec 14 1998 Michael Johnson <johnsonm@redhat.com>
- fixed missing include files, updated to use gtk-config

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Erik Troan <ewt@redhat.com>
- included changes from rhad labs to update things for new gtk

* Sun Nov 09 1997 Michael K. Johnson <johnsonm@redhat.com>
- removed improper geometry handling

* Tue Nov  4 1997 Otto Hammersmith <otto@redhat.com>
- control panel now obeys the -geometry option

* Mon Nov  3 1997 Otto Hammersmith <otto@redhat.com>
- updated version... added bindings.tcl

* Thu Oct 30 1997 Otto Hammersmith <otto@redhat.com>
- added loopy files
- updated version

* Fri Oct 17 1997 Otto Hammersmith <otto@redhat.com>
- Replaced the tcl/tk version with a gtk+ version in C.  No longer
  noarch... gee, what a loss.

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
