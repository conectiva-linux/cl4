Summary: Graphical tools for certain user account management tasks.
Summary(pt_BR): Ferramentas para Usuários
Summary(es): Herramientas para Usuarios
Name: usermode
Version: 1.5
Release: 3cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: usermode-%{PACKAGE_VERSION}.tar.gz
Source800: usermode-wmconfig.i18n.tgz
Requires: util-linux
BuildRoot: /var/tmp/usermode-root

%description
The usermode package contains several graphical tools for users:
userinfo, usermount and userpasswd.  Userinfo allows users to change
their finger information.  Usermount lets users mount, unmount, and
format filesystems.  Userpasswd allows users to change their passwords.

Install the usermode package if you would like to provide users with
graphical tools for certain account management tasks.

%description -l pt_BR
Várias ferramentas gráficas, incluindo uma para ajudar os usuários a
gerenciar discos flexíveis (e outras mídias removíveis) e uma para ajudar
o usuário a mudar suas informações finger.

%description -l es
Varias herramientas gráficas, incluyendo una para ayudar a los
usuarios a gestionar discos flexibles (y otras medias removibles)
y una para ayudar al usuario a cambiar su información finger.

%prep
%setup

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install
make PREFIX=$RPM_BUILD_ROOT install-man

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

tar xvfpz $RPM_SOURCE_DIR/usermode-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/usermount
/usr/man/man1/usermount.1
/usr/bin/userinfo
/usr/man/man1/userinfo.1
%attr(4755, root, root) /usr/sbin/userhelper
/usr/man/man8/userhelper.8
/usr/bin/userpasswd
/usr/man/man1/userpasswd.1
/usr/bin/consolehelper
/usr/man/man8/consolehelper.8
/etc/X11/applink/System/*
/etc/X11/wmconfig/userpasswd
/etc/X11/wmconfig/userinfo
/etc/X11/wmconfig/usermount

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Mar 27 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- added Group, Summary and %description translations

* Fri Mar 19 1999 Michael Johnson <johnsonm@redhat.com>
- updated userhelper.8 man page for consolehelper capabilities
- moved from wmconfig to desktop entries

* Thu Mar 18 1999 Michael Johnson <johnsonm@redhat.com>
- added consolehelper
- Changed conversation architecture to follow PAM spec

* Wed Mar 17 1999 Bill Nottingham <notting@redhat.com>
- remove gdk_input_remove (causing segfaults)

* Tue Jan 12 1999 Michael Johnson <johnsonm@redhat.com>
- fix missing include files

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- use defattr
- fix spec file ( rm -rf $(RPM_BUILD_ROOT) is a stupid thing to do ! )

* Tue Oct 06 1998 Preston Brown <pbrown@redhat.com>
- fixed so that the close button on window managers quits the program properly

* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- use gtk-config during build
- added make archive rule to Makefile
- uses a build root

* Fri Nov  7 1997 Otto Hammersmith <otto@redhat.com>
- new version that fixed memory leak bug.

* Mon Nov  3 1997 Otto Hammersmith <otto@redhat.com>
- updated version to fix bugs

* Fri Oct 17 1997 Otto Hammersmith <otto@redhat.com>
- Wrote man pages for userpasswd and userhelper.

* Tue Oct 14 1997 Otto Hammersmith <otto@redhat.com>
- Updated the packages... now includes userpasswd for changing passwords
  and newer versions of usermount and userinfo.  No known bugs or
  misfeatures. 
- Fixed the file list...

* Mon Oct 6 1997 Otto Hammersmith <otto@redhat.com>
- Created the spec file.
