Summary: The Red Hat Linux mouse configuration tool.
Summary(pt_BR): Ferramenta de configuração do mouse da Red Hat
Summary(es): Herramienta de configuración de ratón de la Red Hat
Name: mouseconfig
Version: 3.9
Release: 2cl
Copyright: distributable
Group: Utilities/System
Group(pt_BR): Utilitários/Sistema
Group(es): Utilitarios/Sistema
Source: mouseconfig-%{PACKAGE_VERSION}.tar.gz
Source1: mouseconfig-%{PACKAGE_VERSION}-pt_BR.po
Patch: mouseconfig-%{PACKAGE_VERSION}-i18n-mousename.patch
Patch1: PNP-probe-conectiva.patch
Patch2: mouseconfig-%{PACKAGE_VERSION}-probe.patch
Prereq: findutils, textutils
Buildroot: /var/tmp/mouseconfig-root

%description
Mouseconfig is a text-based mouse configuration tool.  Mouseconfig
sets up the files and links needed for configuring and using a mouse
on a Red Hat Linux system.  The mouseconfig tool can be used to set
the correct mouse type for programs like gpm, and can be used with
Xconfigurator to set up the mouse for the X Window System.

%description -l pt_BR
Essa é uma ferramenta modo texto de configuração do mouse. Você pode
usá-la para configurar o tipo de mouse apropriado para programas
como "gpm". Ele também pode ser usado em conjunto com o Red Hat
Xconfigurator para "ajustar" o mouse para o Sistema X Window.

%description -l es
Esta es una herramienta modo texto de configuración del ratón. Puedes
usarla para configurar el tipo de ratón apropiado para programas
como "gpm". También puede ser usada en conjunto con el Red Hat
Xconfigurator para "ajustar" el ratón al Sistema X Window.

%prep
%setup
%patch  -p1
%patch1 -p1
%patch2 -p1
cp $RPM_SOURCE_DIR/mouseconfig-%{PACKAGE_VERSION}-pt_BR.po po/pt_BR.po

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
strip mouseconfig

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/sbin/mouseconfig
/usr/man/man8/mouseconfig.8
#/usr/man/*/man8/mouseconfig.8
/usr/share/locale/*/LC_MESSAGES/mouseconfig.mo

%post
if [ -L /dev/mouse ]; then
     OLDDEV=`find /dev -name mouse -printf "%l" | grep cua`
     if [ "x$OLDDEV" != "x" ]; then
          DEVICE=`basename $OLDDEV`
          PORT=`echo $DEVICE | cut -b4`
	  rm -f /dev/mouse
          ln -s ttyS$PORT /dev/mouse
     fi
fi     


%changelog
* Sat Jun 19 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated pt_BR.po
- correct PNP-probing for serial mouse
- included Genius EasyMouse 3 Buttons and fixed one Logitech to 2 buttons

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- release for Red Hat Linux 6.0

* Tue Apr 13 1999 Preston Brown <pbrown@redhat.com>
- netscroll sets gpm mouse type to netmouse now, not plain ps/2.

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- updated man page to reflect that mouseconfig can fix XF86Config.

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- fixed gpm mouse types to match gpm 1.17

* Thu Mar 18 1999 Matt Wilson <msw@redhat.com>
- updated man page

* Mon Mar 15 1999 Matt Wilson <msw@redhat.com>
- added new feature that rewrites the /etc/X11/XF86Config file to
  reflect new changes in mouse settings.

* Thu Mar 10 1999 Matt Wilson <msw@redhat.com>
- changed handling of the "No mouse" option
- made /dev/mouse symlink relative
- changed sun probing to default to serial mice for sun4[cm]

* Tue Mar  9 1999 Jeff Johnson <jbj@redhat.com>
- add in_ID.po.

* Wed Mar  3 1999 Matt Wilson <msw@redhat.com>
- mouseconfig now exits when enter is pressed
- fixed sparc support

* Sat Feb 27 1999 Matt Wilson <msw@redhat.com>
- added workarounds for 2.2 kernel serial and psaux changes

* Thu Feb 25 1999 Matt Wilson <msw@redhat.com>
- updated descriptions

* Fri Feb 19 1999 Preston Brown <pbrown@redhat.com>
- added sparc support.

* Mon Feb 15 1999 Matt Wilson <msw@redaht.com>
- Fixed typo in %post script

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- Fixed %post script to handle absolute symlinks

* Fri Feb  5 1999 Matt Wilson <msw@redhat.com>
- Finished %post script

* Wed Jan 27 1999 Matt Wilson <msw@redhat.com>
- s/cua/ttyS/g so we don't use the depreciated /dev/cua interface to
  serial devices

* Tue Jan 19 1999 Bill Nottingham <notting@redhat.com>
- alpha & arm fixes

* Sun Jan 10 1999 Matt Wilson <msw@redhat.com>
- rebuilt for newt 0.40

* Fri Nov 13 1998 Preston Brown <pbrown@redhat.com>
- somehow the "No Mouse" option was lost, re-added.

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide (slang-1.2.2)

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- translation updates

* Mon Oct 12 1998 Preston Brown <pbrown@redhat.com>
- if serial mouse detected that is non-pnp, default on generic not msnew.

* Thu Oct 08 1998 Preston Brown <pbrown@redhat.com>
- F12 functionality fixed
- fixed 0-based array bug in reading config file that has been there always?!

* Wed Oct 07 1998 Preston Brown <pbrown@redhat.com>
- merged in some more of the brazilian translation stuff.

* Mon Oct 05 1998 Preston Brown <pbrown@redhat.com>
- fixed some random problems, esp. autodetecting serial port but then asking
- what port to use anyway.  Tested in lab in install and "afterwards" modes,
- checks out OK. Removed %patch -p1; why was it back again!?

* Sat Sep 26 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- more translatable strings (i18n)
- the mouse full names, etc
- po/pt_BR (brazilian portuguese) translation - new file
- fixes to the --back section in the english man page
- man hierarchy for the man page translations, pt_BR is the first translation
- make clean goes to the po directory
- make install goes to the man directory

* Fri Sep 25 1998 Preston Brown <pbrown@redhat.com>
- more fixes to autodetection, help button

* Fri Sep 25 1998 Cristian Gafton <gafton@redhat.com>
- slovak patches in
- turkish translation update

* Thu Sep 24 1998 Preston Brown <pbrown@redhat.com>
- pnp updates for logitech, microsoft serial mice
- little update to kickstart stuff, changed a || to a &&

* Wed Sep 23 1998 Cristian Gafton <gafton@redhat.com>
- added Serbian (sr) language support

* Wed Sep 23 1998 Preston Brown <pbrown@redhat.com>
- fixed problem when reading config file but not selecting configured mouse
- default focus of window is on the mouse list, not the OK button

* Thu Sep 17 1998 Preston Brown <pbrown@redhat.com>
- pasted in a block of code to readConfigFile that I missed.

* Tue Sep 15 1998 Preston Brown <pbrown@redhat.com>
- updated so that new ms mice are recognized in pnp mode.
- merged into CVS (whoops. sorry bout that)

* Thu Sep 10 1998 Preston Brown <pbrown@redhat.com>
- added some new mouse types, X mousetype config line; alphabetized list

* Sun Aug 02 1998 Erik Troan <ewt@redhat.com>
- use NEWT_FLAG_SCROLL now for newt 0.30
- added --test

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for fr, de, tr

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- uadded/updated translations

* Mon Apr 20 1998 Erik Troan <ewt@redhat.com>
- build rooted
- added de and en_RN translations

* Fri Mar 27 1998 Erik Troan <ewt@redhat.com>
- reworked much of the code to be somewhat readable -- this came from
  poor XFree86 code to begin with, and it never seemed to get any better

* Sun Nov  9 1997 Michael Fulbright <msf@redhat.com>
- fixed --expert mode

* Fri Nov  7 1997 Michael Fulbright <msf@redhat.com>
- fixes some problems with busmice probing

* Wed Nov  5 1997 Michael Fulbright <msf@redhat.com>
- changed SERIAL to serial when reporting probe results
- added a dist to Makefile, so 'make dist' makes a tarball

* Sat Nov  1 1997 Michael Fulbright <msf@redhat.com>
- added man page to file list

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- added query if ps/2 mouse found if they want to emulate 3 buttons

* Mon Oct  6 1997 Michael Fulbright <msf@redhat.com>
- fixed creation of /dev/mouse link for cua devices in interactice mode.
- added man page and --help information

* Thu Oct  2 1997 Michael Fulbright <msf@redhat.com>
- added --expert and probing in interactive mode.

* Tue Sep 30 1997 Michael Fulbright <msf@redhat.com>
- enchanced kickstart behavior, tries to autoprobe devices in this mode.

* Thu Sep 18 1997 Erik Troan <ewt@redhat.com>
- added command line options

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc
