Summary: The Red Hat Linux configuration tool for the X Window System.
Summary(pt_BR): Ferramenta Red Hat de configuração do sistema X Window
Summary(es): Herramienta Red Hat de configuración del sistema X Window
Name: Xconfigurator
%define version 4.2.3
Version: %{version}
Release: 14cl
Copyright: distributable
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware
Source: Xconfigurator-%{version}.tar.bz2
Source1: Xconfigurator-4.2.3-pt_BR.po
Source2: Xconfigurator-3.82-es.po
Source700: Xconfigurator-man-pt_BR.tar
Patch1: Xconfigurator-4.2.3-conectiva.patch
Patch2: Xconfigurator-4.2.3-acentos.patch
Patch3: Xconfigurator-4.2.3-3DImage975.patch
Patch4: Xconfigurator-4.2.3-setsysfont.patch
Requires: XFree86 >= 3.3.3.1,  kbdconfig, mouseconfig >= 2.8, console-tools
Requires: initscripts >= 3.60
BuildRoot: /var/tmp/%{name}-root

%description
Xconfigurator is a full-screen, menu-driven program which walks
you through setting up your X server. Xconfigurator is based
on the sources for xf86config, a utility from XFree86.

You should install Xconfigurator if you are installing the X Window
System.

%description -l pt_BR
Esta é a ferramenta Red Hat de configuração X. Ela é baseada nos
fontes do xf86config, um utilitário de XFree86. Adicionada uma
interface amigável para facilitar o uso pelo usuário final.

%description -l es
Esta es la herramienta Red Hat de configuración X. Está basada en
los fuentes del xf86config, un utilitario de XFree86. Adicionada
una interface amigable para facilitar el uso por el usuario final.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

cp -f ${RPM_SOURCE_DIR}/Xconfigurator-4.2.3-pt_BR.po po/pt_BR.po
cp -f ${RPM_SOURCE_DIR}/Xconfigurator-3.82-es.po po/es.po

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
strip Xconfigurator

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install

gzip -9f $RPM_BUILD_ROOT/usr/X11R6/man/man1/*




mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/Xconfigurator-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO
/usr/X11R6/bin/Xconfigurator
/usr/X11R6/bin/Xtest
/usr/X11R6/share/Xconfigurator
/usr/X11R6/man/man1/Xconfigurator.1x.gz
/usr/share/locale/*/LC_MESSAGES/Xconfigurator.mo
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Thu Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fixed place of pt_BR man
- fixed realloc in monitor list

* Wed Jun 30 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- removed duplicated Acer 33s from MonitorsDB

* Wed Jun 30 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- rebuild to fix pt_BR man (keeping into /usr/man/ instead of
  /usr/X11R6/man)
- compressed original man page

* Fri Jun 18 1999 Wanderlei Cavassin <cavassin@conectiva.com>
- Included Samsung SyncMaster 450b and 550s
- generates FontPath with xfs (default: ks_without_font_server = 0)

* Fri Jun 11 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- Updated list of IBM's monitors (info from Tonko De Rooy <tderooy@uk.ibm.com>)
- Included support to config a Spanish Xmodmap

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Fixed requires

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added Xtest to file list again

* Fri May 28 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat May 22 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- for now let's take Xtest off the rpm...

* Fri May 21 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- redid the accents patch (previously done by Cavassin)
- redid the setsysfont patch (previously done by Cavassin)
- First choose Vendor, then Model
- fontserver selectable
- support for Trident 3DImage975 boards detection

* Tue Apr 20 1999 Matt Wilson <msw@redhat.com>
- added Sun{,24} wrapper to properly set the fontpath
- allow arguments to our Xsun wrapper

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- release for Red Hat 6.0

* Thu Apr 15 1999 Matt Wilson <msw@redhat.com>
- integrated changes from DaveM to fix Ultras with PS/2 mouse and keybord
- fixed segfault
- added icelandic thingie

* Thu Apr 15 1999 Preston Brown <pbrown@redhat.com>
- sparc keyboard fix, sun monitor definition for MonitorsDB

* Wed Apr 14 1999 Matt Wilson <msw@redhat.com>
- changed mappings for some matrox cards

* Wed Apr 14 1999 Preston Brown <pbrown@redhat.com>
- if it isn't run out of the installer, start xfs when successful.

* Tue Apr 13 1999 Preston Brown <pbrown@redhat.com>
- attempt to fix Sparc64 keyboard setup (strcasecmp --> strcasestr)

* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- works with security-fixed xfs

* Wed Apr  7 1999 Matt Wilson <msw@redhat.com>
- fix for sun ps/2 keyboard mappings

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- now writes path to font server as a unix domain socket not tcp socket

* Mon Mar 29 1999 Preston Brown <pbrown@redhat.com>
- change text for 8 mb to "8 mb or more"

* Sat Mar 27 1999 Erik Troan <ewt@redhat.com>
- actually fixed kickstart

* Fri Mar 26 1999 Matt Wilson <msw@redhat.com>
- fixed kickstart

* Mon Mar 22 1999 Matt Wilson <msw@redhat.com>
- fixed bug probing I128 cards

* Mon Mar 15 1999 Matt Wilson <msw@redhat.com>
- fixed handling of unknown error conditions from Xtest
- added option to skip test
- added some custom monitor types

* Wed Mar 10 1999 Matt Wilson <msw@redhat.com>
- removed fprintf debugging
- bound to existing Xconfigurator gettext domain
- fixed %files

* Wed Mar 08 1999 Preston Brown <pbrown@redhat.com>
- don't present 1152x864 as a valid autoprobed default

* Tue Mar  2 1999 Matt Wilson <msw@redhat.com>
- reworked state flow in main to remove gotos and make flow a bit better

* Mon Mar  1 1999 Matt Wilson <msw@redhat.com>
- Xconfigurator now starts X to test the configuration
- assume failure when testing the X setup

* Wed Feb 24 1999 Matt Wilson <msw@redhat.com>
- memory probe for Mach64

* Wed Feb 24 1999 Matt Wilson <msw@redhat.com>
- fixed resolution selection segfault

* Thu Feb 18 1999 Preston Brown <pbrown@redhat.com>
- added sun support from ultrapenguin, and new resolutions 1600x1200
  and 1152x864

* Mon Feb 15 1999 Matt Wilson <msw@redhat.com>
- fixed segfaults in custom monitor setup, inittab writing.

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- fixed check for null ramdac in xf86config writing (thought I got this one)

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com
- Don't pop up windows after newt shuts down

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- Check to see if you're in --pick before presenting the initlevel screen

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- added --startxonboot

* Sun Feb  7 1999 Matt Wilson <msw@redhat.com>
- fixed check for null ramdac in xf86config writing

* Sun Feb  7 1999 Matt Wilson <msw@redhat.com>
- moved the inittab question to the proper place.

* Sun Feb  7 1999 Matt Wilson <msw@redhat.com>
- away with global variables - pass a struct around
- added a feature to rewrite the inittab to bring up the machine
  in runlevel 5 after asking the user if they want this.

* Tue Jan 19 1999 Bill Nottingham <notting@redhat.com>
- don't build on arm

* Sun Jan 10 1999 Matt Wilson <msw@redhat.com>
- Rebuilt for newt 0.40

* Wed Jan  6 1999 Matt Wilson <msw@redhat.com>
- Rebuilt for rawhide

* Wed Jan  6 1999 Matt Wilson <msw@redhat.com>
- Added probing for 3DLabs GLINT MX boards 

* Mon Dec 21 1998 Matt Wilson <msw@redhat.com>
- Rebuilt for rawhide

* Mon Dec 21 1998 Matt Wilson <msw@redhat.com>
- Fixed one more segfault

* Mon Dec 21 1998 Matt Wilson <msw@redhat.com>
- Added 3DLabs support, requires 3.3.3, fixed Cards display, fixed segfault

* Tue Dec 15 1998 Jeff Johnson <jbj@redhat.com>
- add ru.po.

* Wed Dec 02 1998 Erik Troan <ewt@redhat.com>
- added compaq monitors

* Fri Nov 13 1998 Preston Brown <pbrown@redhat.com>
- adjusted FontPath entries

* Thu Nov 12 1998 Matt Wilson <msw@redhat.com>
- Added pci probing for Riva 128 cards, made VideoRam exception (the server
can't figure out how much video ram Rive 128 cards have.)

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide (slang-1.2.2)

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- translation updates

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated pt_BR translations
- more i18n strings: ramdac_name, clockchip_name, monitortype_name

* Tue Oct 06 1998 Preston Brown <pbrown@redhat.com>
- updated pci probing to handle S3V GX2 and MX cards

* Mon Sep 28 1998 Preston Brown <pbrown@redhat.com>
- fixed autoprobing for S3V based cards, and for AGP Millennium II

* Fri Sep 25 1998 Preston Brown <pbrown@redhat.com>
- merged back in mouseconfig stuff, somehow lost!??
- merge back erik's changes, also lost!

* Fri Sep 25 1998 Cristian Gafton <gafton@redhat.com>
- turkish update

* Fri Sep 25 1998 Matthew Wilson <msw@redhat.com>
- More backbutton changes, state saving changes.  Much work left to do.

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- NeoMagic video list update

* Thu Sep 24 1998 Preston Brown <pbrown@redhat.com>
- tiny update for new mouseconfig

* Wed Sep 23 1998 Erik Troan <ewt@redhat.com>
- added support for new /etc/sysconfig/keyboard format

* Thu Sep 17 1998 Preston Brown <pbrown@redhat.com>
- fixed problem with path to keyboard map being wrong with new kbd package

* Tue Sep 15 1998 Preston Brown <pbrown@redhat.com>
- added support for new XMOUSETYPE from mouseconfig
- merged changes into cvs (whoops)

* Mon Aug 10 1998 Erik Troan <ewt@redhat.com>
- incorporated Back button mods from Matt Wilson

* Sun Aug 02 1998 Erik Troan <ewt@redhat.com>
- built against newt 0.30

* Wed Jun 10 1998 Erik Troan <ewt@redhat.com>
- was using wrong domain name for translations

* Thu May 14 1998 Cristian Gafton <gafton@redhat.com>
- fixed alpha version

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- use /sbin/setsysfont to restore the system font
- added tr, no, cz, de, no, fr translations (maybe a couple of others)

* Fri Apr 17 1998 Erik Troan <ewt@redhat.com>
- include translations in build

* Sun Apr 05 1998 Erik Troan <ewt@redhat.com>
- updated for new newt, i18n-ready
- removed tons of extraneous code
- doesn't use imake anymore
- buildrooted
- moved monitor database to /usr/X11R6/share
- requires X11R6 > 3.3.2 rather then xserver-wrapper

* Wed Jan 21 1998 Erik Troan <ewt@redhat.com>
- don't install /usr/X11R6/bin/X symlink, just require xserver-wrapper instead

* Sun Nov  9 1997 Michael Fulbright <msf@redhat.com>
- fixed --pick/--continue and --expert interaction

* Sat Nov 08 1997 Erik Troan <ewt@redhat.com>
- added checks for bad parameters

* Fri Nov  7 1997 Michael Fulbright <msf@redhat.com>
- added new video card entries from 2.0.31 kernel pci.c

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- changed /etc/X11/X symlink to be relative, not absolute

* Thu Oct 30 1997 Michael Fulbright <msf@redhat.com>
- fixed VGA16 kickstart support
- fixed version string

* Mon Oct 27 1997 Michael Fulbright <msf@redhat.com>
- Fixed Mach64 autoprobing problems
- Added more user options when selecting from autoprobed video modes

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- fixed handling of temp files to be more safe
- added option for interactive mode to autoprobe ram,color depth, etc.

* Mon Oct  6 1997 Michael Fulbright <msf@redhat.com>
- made 'Unlisted Card' work again
- added more monitors
- added a beta man page

* Thu Oct  2 1997 Michael Fulbright <msf@redhat.com>
- added generic monitor types

* Wed Oct  1 1997 Michael Fulbright <msf@redhat.com>
- made it run /etc/X11/X explicitely
- added --expert flag
- fixed memory allocation problem in SplitString()

* Tue Sep 30 1997 Michael Fulbright <msf@redhat.com>
- added kickstart support
- added PCI probing for PCI video card autodetection
- added use of --probeonly to get video card information
