Summary: A graphical utility for controlling network interfaces.
Summary(pt_BR): Aplicativo gráfico para o controle de dispositivo de rede por usuários.
Summary(es): Aplicativo gráfico para el control de dispositivo de red por usuarios.
Name: usernet
Version: 1.0.9
Release: 2cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
BuildRoot: /var/tmp/usernet-root
Source: usernet-%{PACKAGE_VERSION}.tar.gz
Source800: usernet-wmconfig.i18n.tgz
Requires: initscripts >= 3.20

%description
The usernet utility provides a graphical interface for manipulating
network interfaces (bringing them up or down and viewing their status).
Users can only manipulate interfaces that are user-controllable.  The
superuser can control all interfaces.

Install the usernet package if you'd like to provide a graphical utility
for manipulating network interfaces.

%description -l pt_BR
Um programa feito para facilitar aos usuários o gerenciamento de
dispositivos de rede, que podem ser controlados por usuário não-root,
e a verificação do status desses dispositivos.

%description -l es
Un programa hecho para facilitar a los usuarios la gestión de
dispositivos de red, que pueden ser controlados por usuario no root,
y la verificación del estado de estos dispositivos.

%prep
%setup

%build
make VERSION=%{PACKAGE_VERSION}

%install
make install BR=$RPM_BUILD_ROOT VERSION=%{PACKAGE_VERSION}


tar xvfpz $RPM_SOURCE_DIR/usernet-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/usernet
/usr/share/usernet/%{PACKAGE_VERSION}
/usr/man/man1/usernet.1
/etc/X11/wmconfig/usernet

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Mar 27 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 17 1999 Bill Nottingham <notting@redhat.com>
- fix it so that it reverts to 'bad' color if ifup fails

* Thu Feb 25 1999 Bill Nottingham <notting@redhat.com>
- new summary/description

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries on install
- use the "proper" build root dir
- defattr

* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- updated to use gtk-config
- Makefile gets version number from .spec file

* Tue Dec 16 1997 Michael K. Johnson <johnsonm@redhat.com>
- usernet hanging on PPP devices fixed

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- no paths in wmconfig files

* Fri Oct 24 1997 Michael K. Johnson <johnsonm@redhat.com>
- Change in Gtk behaviour for closing windows.
- wmconfig

* Tue Oct 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Change to a fork-fork-exec for running if{up,down} so that the
  status button responds instantly, and init cleans up after our
  poor orphaned processes.

* Fri Oct 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Resize window to fit up to three interface buttons without a scrollbar.
- When changing versions, need to update version in usernetrc as well.
  Do that automatically now.
- Everything takes the version from the spec file.

* Fri Oct 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Call if{up,down} directly and let them call usernetctl if necessary,
  so that root can also use the tool.
