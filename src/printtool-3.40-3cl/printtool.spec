Summary: A printer configuration tool with a graphical user interface.
Summary(pt_BR): Ferramenta de configuração de impressoras
Summary(es): Herramienta de configuración de impresoras
Name: printtool
Version: 3.40
Release: 3cl
Copyright: GPL
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Source: printtool-%{PACKAGE_VERSION}.tar.gz
Source800: printtool-wmconfig.i18n.tgz
Requires: tcl
Requires: tk
Requires: control-panel
Requires: rhs-printfilters >= 1.50
Requires: lpr >= 0.16
BuildArchitectures: noarch
BuildRoot: /var/tmp/printtool-root

%description
The printtool is a printer configuration tool with a graphical user
interface.  Printtool can manage both local and remote printers,
including Windows (SMB) and NetWare (NCP) printers.

Printtool should be installed so that you can manage local and remote
printers.

%description -l pt_BR
O printtool oferece uma interface gráfica para configurar
impressora. Administra tanto impressoras locais quanto
remotas. Impressoras Windows (SMB) também podem ser configuradas.

%description -l es
printtool nos ofrece una interface gráfica para configurar
impresora. Administra tanto impresoras locales como remotas. También
pueden ser configuradas impresoras Windows (SMB).

%prep
%setup -q -n printtool

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/rhs/control-panel}

make	PREFIX=$RPM_BUILD_ROOT/usr \
	INSTALLBIN="install -m0755" INSTALLDATA="install -m0644" \
	install

install printtool.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/printtool


tar xvfpz $RPM_SOURCE_DIR/printtool-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
/usr/bin/printtool
/usr/lib/rhs/control-panel/printtool.init
/usr/lib/rhs/control-panel/printtool.xpm
%attr(0600,root,root)	%config(missingok) /etc/X11/wmconfig/printtool

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed requires wrt rpm 3.0.2

* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- returns to old Group
- added Group, Summary and %description translations

* Fri Mar 19 1999 Bill Nottingham <notting@redhat.com>
- text changes

* Mon Feb  9 1999 Bill Nottingham <notting@redhat.com>
- uniprint support, courtesy Osamu Aoki

* Mon Dec 28 1998 Bill Nottingham <notting@redhat.com>
- ditto

* Tue Dec  8 1998 Bill Nottingham <notting@redhat.com>
- oops. fix SMB printers, again

* Wed Nov 18 1998 Bill Nottingham <notting@redhat.com>
- add workgroup field for SMB printers

* Fri Oct  2 1998 Bill Nottingham <notting@redhat.com>
- fix typo

* Thu Sep  9 1998 Bill Nottingham <notting@redhat.com>
- fix description

* Thu Sep  2 1998 Bill Nottingham <notting@redhat.com>
- added NCP support

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- /etc/rc.d/init.d/lpd.init is now just lpd. (problem #768)

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Nov 26 1997 Michael Fulbright <msf@redhat.com>
- fixed to print warning if smbclient not installed

* Fri Nov  7 1997 Michael Fulbright <msf@redhat.com>
- added wmconfig

* Wed Nov  5 1997 Michael Fulbright <msf@redhat.com>
- fixed add/edit printer boxes with new packing cause old one broke bad

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- put nice new xpm icon in place
- fixed up help titles
- corrected lots of misspellings

* Tue Oct 14 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Tue Apr 22 1997 Michael Fulbright <msf@redhat.com>
- Moved to version 3.2.
- Fixed problem with EXTRA_GS_OPIONS

* Fri Mar 12 1997 Michael Fulbright <msf@redhat.com>
- Moved up to version 3.1.
- Added support for mpage - allows nup printing and adjustable margins.
- Simplified configuraion for stair-stepped text and sending EOF.
- Fixed PS filter to send a '\004' instead of a '\014' as EOF character.

* Wed Mar 12 1997 Michael Fulbright <msf@redhat.com>
- Added A4 paper test page support. 

* Fri Mar  7 1997 Michael Fulbright <msf@redhat.com>
- Split print filters off into rh-printfilters package.
- Removed some undesirable debug messages.

* Fri Feb 14 1997 Michael Fulbright <msf@redhat.com>
- Fixed a 'sh -x' left in head of smbprint script
