# Note that this is NOT a relocatable package
%define ver      1.0.0
%define rel      38cl
%define prefix   /usr

Summary: GNOME Display Manager.
Summary(pt_BR): Gerenciador de Entrada do GNOME
Summary(es): Administrador de Entrada del GNOME
Name: gdm
Version: %ver
Release: %rel
Copyright: LGPL/GPL
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
# Recompressed source with bzip2
Source0: ftp://ftp.socsci.auc.dk/pub/empl/mkp/gdm-%{PACKAGE_VERSION}.tar.bz2
Source1: gdm-pt_BR.po
Source2: Default.session
Source5: Failsafe.session

Patch0: gdm-1.0.0-rhconf.patch
Patch1: gdm-1.0.0-installdirs.patch
Patch2: gdm-groupwrite.patch
Patch3: gdm-gnomerc.patch
Patch4: gdm-1.0.0-rhgreeter.patch
Patch5: gdm-1.0.0-cnsl.patch
Patch6: gdm-1.0.0-systempath.patch
Patch7: gdm-1.0.0-nosound.patch
Patch8: gdm-1.0.0-notabcmpltion.patch
Patch9: gdm-1.0.0-signal.patch
Patch10: gdm-1.0.0-aboutbox.patch
Patch11: gdm-1.0.0-nosuspend.patch
Patch12: gdm-1.0.0-dontblastlogo.patch
Patch13: gdm-1.0.0-fixlangs2.patch
Patch14: gdm-1.0.0-noclosedspy.patch
Patch15: gdm-1.0.0-norwegian.patch
Patch16: gdm-1.0.0-photofix.patch
Patch17: gdm-1.0.0-pt_BR.patch

BuildRoot: /var/tmp/gdm-%{PACKAGE_VERSION}-root

Prereq: shadow-utils
Docdir: %{prefix}/doc

%description
GNOME Display Manager allows you to log into your system with the
X Window System running.  It is highly configurable, allowing you
to run several different X sessions at once on your local machine,
and can manage login connections from remote machines as well.

%description -l pt_BR
Gerenciador de Entrada do GNOME

%description -l es
Administrador de Entrada del GNOME

%prep
%setup -q
%patch0 -p1 -b .rhconf
%patch1 -p1 -b .installdirs
%patch2 -p1 -b .groupwrite
%patch3 -p1 -b .gnomerc
%patch4 -p1 -b .rhgreeter
%patch5 -p1 -b .cnsl
%patch6 -p1 -b .systempath
%patch7 -p1 -b .nosound
%patch8 -p1 -b .notabcmpltion
%patch9 -p1 -b .signal
%patch10 -p1 -b .aboutbox
%patch11 -p1 -b .nosuspend
%patch12 -p1 -b .dontblastlogo
%patch13 -p1 -b .fixlangs
%patch14 -p1 -b .noclosedspl
%patch15 -p1 -b .norwegian
%patch16 -p1 -b .photofix
%patch17 -p1 -b .pt_BR

%build
cp $RPM_SOURCE_DIR/gdm-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
[ "$LINGUAS" ] && unset LINGUAS
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --sysconfdir=/etc/X11 --localstatedir=/var
make
(cd config; make gdm.conf gnomerc Gnome)

%install
rm -rf $RPM_BUILD_ROOT

/usr/sbin/useradd -r gdm > /dev/null 2>&1 || /bin/true

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc/X11 localstatedir=$RPM_BUILD_ROOT/var install
# docs go elsewhere
rm -rf $RPM_BUILD_ROOT/%{prefix}/doc

# install RH specific session files
rm -f $RPM_BUILD_ROOT/etc/X11/gdm/Sessions/*

install -m 755 %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/gdm/Sessions/Default
install -m 755 %{SOURCE5} $RPM_BUILD_ROOT/etc/X11/gdm/Sessions/Failsafe
ln -sf Default $RPM_BUILD_ROOT/etc/X11/gdm/Sessions/default

# change default Init script to be Conectiva default
ln -sf ../../xdm/Xsetup_0 $RPM_BUILD_ROOT/etc/X11/gdm/Init/Default

# move pam.d stuff to right place
mv $RPM_BUILD_ROOT/etc/X11/pam.d $RPM_BUILD_ROOT/etc

# strip binaries
strip `file $RPM_BUILD_ROOT/%{prefix}/bin/* | awk -F':' '/not strip/ { print $1 }'` | :

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/useradd -u 42 -r gdm > /dev/null 2>&1
# ignore errors, as we can't disambiguate between gdm already existed
# and couldn't create account with the current adduser.
exit 0

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README docs/gdm-manual.txt
%{prefix}/bin/*
%config /etc/pam.d/gdm
%config /etc/X11/gdm/gnomerc
%config /etc/X11/gdm/gdm.conf
%config /etc/X11/gdm/Sessions/*
%config /etc/X11/gdm/Init/*
%{prefix}/share/locale/*/*/*
%{prefix}/share/pixmaps/*
%attr(750, gdm, gdm) %dir /var/gdm

%changelog
* Thu Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- Init/Default links to xdm/XSetup_0 (backspace working)

* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to gdm

* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated our gdm to RH's one (Only 16 patches ;)
- Do not make gdm's Xsetup_0 the default
- unset LINGUAS

* Mon Apr 19 1999 Michael Fulbright <drmike@redhat.com>
- fix to handling ancient gdm config files with non-standard language specs
- dont close display connection for xdmcp connections, else we die if remote
  end dies. 

* Fri Apr 16 1999 Michael Fulbright <drmike@redhat.com>
- fix language handling to set GDM_LANG variable so gnome-session 
  can pick it up

* Wed Apr 14 1999 Michael Fulbright <drmike@redhat.com>
- fix so certain dialog boxes dont overwrite background images

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- do not specify -r 42 to useradd -- it doesn't know how to fall back
  if id 42 is already taken

* Fri Apr 9 1999 Michael Fulbright <drmike@redhat.com>
- removed suspend feature

* Mon Apr 5 1999 Jonathan Blandford <jrb@redhat.com>
- added patch from otaylor to not call gtk funcs from a signal.
- added patch to tab when username not added.
- added patch to center About box (and bring up only one) and ignore "~"
  and ".rpm" files.

* Fri Mar 26 1999 Michael Fulbright <drmike@redhat.com>
- fixed handling of default session, merged all gdmgreeter patches into one

* Tue Mar 23 1999 Michael Fulbright <drmike@redhat.com>
- remove GNOME/KDE/AnotherLevel session scripts, these have been moved to
  the appropriate packages instead.
- added patch to make option menus always active (security problem otherwise)
- added jrb's patch to disable stars in passwd entry field

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- made sure /usr/bin isnt in default path twice
- strip binaries

* Wed Mar 17 1999 Michael Fulbright <drmike@redhat.com>
- fixed to use proper system path when root logs in

* Tue Mar 16 1999 Michael Fulbright <drmike@redhat.com>
- linked Init/Default to Red Hat default init script for xdm
- removed logo from login dialog box

* Mon Mar 15 1999 Michael Johnson <johnsonm@redhat.com>
- pam_console integration

* Tue Mar 09 1999 Michael Fulbright <drmike@redhat.com>
- added session files for GNOME/KDE/AnotherLevel/Default/Failsafe
- patched gdmgreeter to not complete usernames
- patched gdmgreeter to not safe selected session permanently
- patched gdmgreeter to center dialog boxes

* Mon Mar 08 1999 Michael Fulbright <drmike@redhat.com>
- removed comments from gdm.conf file, these are not parsed correctly

* Sun Mar 07 1999 Michael Fulbright <drmike@redhat.com>
- updated source line for accuracy

* Fri Feb 26 1999 Owen Taylor <otaylor@redhat.com>
- Updated patches for 1.0.0
- Fixed some problems in 1.0.0 with installation directories
- moved /usr/var/gdm /var/gdm

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- moved files from /usr/etc to /etc

* Tue Feb 16 1999 Michael Johnson <johnsonm@redhat.com>
- removed commented-out #1 definition -- put back after testing gnome-libs
  comment patch

* Sat Feb 06 1999 Michael Johnson <johnsonm@redhat.com>
- initial packaging
