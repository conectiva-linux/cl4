Summary: Network Configuration Tool
Summary(pt_BR): Ferramenta de Configuração de Rede
Summary(es): Herramienta de Configuración de Red
Name: netcfg
Version: 2.19
Release: 8cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: netcfg-%{PACKAGE_VERSION}.tar.gz
Source800: wmconfig.i18n.tgz
Patch0: netcfg-2.19-nobr.patch
Requires: pythonlib >= 1.20, python, tkinter, initscripts >= 3.24
BuildArchitectures: noarch
BuildRoot: /var/tmp/netcfg-root
Summary(de): Netzwerk-Konfigurations-Tool 
Summary(fr): Outil de configuration du réseau
Summary(tr): Að yapýlandýrma aracý

%description
Red Hat Linux netcfg provides a GUI interface which allows you to
easily administrate your network setup.

%description -l pt_BR
Red Hat Linux netcfg oferece uma interface GUI que permite facilmente
administrar sua configuração de rede.

%description -l es
Red Hat Linux netcfg nos ofrece una interface GUI que permite
fácilmente administrar tu configuración de red.

%description -l de
Red Hat Linux netcfg bietet eine grafische Benutzeroberfläche, über
Sie Ihre Netzwerkeinrichtung einfach verwalten können.

%description -l fr
netcfg de Red Hat offre une interface graphique permettant d'administrer
facilement la configuration de son réseau.

%description -l tr
Red Hat tarafýndan geliþtirilen, að yapýlandýrmasýný ve yönetimini
kolaylaþtýran X11 tabanlý kullanýcý arabirimi.

%prep
%setup -q
%patch0 -p1 -b .nobr

%build
unset DISPLAY || true
export PYTHONPATH=/usr/lib/rhs/python
make

%install
rm -rf $RPM_BUILD_ROOT

unset DISPLAY || true
export PYTHONPATH=/usr/lib/rhs/python

make	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLBIN="install -m755" INSTALLDATA="install -m644" \
	install

( cd $RPM_BUILD_ROOT
  mkdir -p ./usr/share/icons
  cp ./usr/lib/rhs/control-panel/netcfg.xpm ./usr/share/icons
)

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/netcfg
/usr/lib/rhs/netcfg
/usr/lib/rhs/control-panel/netcfg.init
/usr/lib/rhs/control-panel/netcfg.xpm
/usr/share/icons/netcfg.xpm
%attr(0600,root,root)	%config(missingok) /etc/X11/wmconfig/netcfg

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Bugs fixed:
 o wmconfig files take no paths
 o only root should see wmconfig

* Thu Nov 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Version 2.19 New features:
 o Debugging option for PPP devices
 o Supports active and passive PPP servers with a single configuration.

* Tue Nov 04 1997 Michael K. Johnson <johnsonm@redhat.com>
- Bugs fixed:
 o icon name corrected in netcfg.init

* Fri Oct 24 1997 Michael K. Johnson <johnsonm@redhat.com>
- Version 2.18 New features:
 o "Clone" devices allow multiple interface configurations
 o IP Forwarding option
 o Menus for modem ports and speeds.
- Bugs fixed:
 o physical/logical PPP device name translation
 o ignores backup files better.
 o removes dip scripts when removing slip devices
 o USERCTL fixed for "bus" devices like ethernet
 o Now asks for interface number for PLIP devices

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Tue Apr 15 1997 Michael K. Johnson <johnsonm@redhat.com>
- New features:
 o Allows ALL device types to be user-controllable
 o Allows DHCP configuration

* Wed Apr 02 1997 Michael K. Johnson <johnsonm@redhat.com>
- New features:
 o Silently disallows senseless lo aliasing
 o Loudly disallows non-functional SLIP aliasing
- Bugs fixed:
 o Didn't always create correct alias numbers
 o Hung if a device without an IP was aliased

* Wed Feb 26 1997 Michael K. Johnson <johnsonm@redhat.com>
- New features:
 o Supports user-controlled interfaces.
 o Includes PAP support for PPP interfaces.
 o Supports two kinds of timeouts for PPP interfaces.
 o Supports MTU as well as MRU
 o Allows giving arbitrary options to pppd
 o Sanity checking on /etc/hosts
- Bugs fixed:
 o Didn't always find the first free interface number
 o Sometimes tried to "add" an existing interface number
