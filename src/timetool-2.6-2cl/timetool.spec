Summary: A utility for setting the system's date and time.
Summary(pt_BR): Ferramenta de configuração de horário e data
Summary(es): Herramienta de configuración de fecha y hora
Name: timetool
Version: 2.6
Release: 2cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: timetool-%{version}.tar.gz
Requires: control-panel
BuildArchitectures: noarch
BuildRoot: /var/tmp/timetool-root

%description
The timetool utility provides a graphical user interface for setting
the current date and time on your system.

%description -l pt_BR
Timetool é uma interface gráfica para ajustar a data e hora corrente
para o seu sistema.

%description -l es
Timetool es una interface gráfica para ajustar la fecha y hora
corriente de tu sistema.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/rhs/control-panel}

make PREFIX=$RPM_BUILD_ROOT/usr install

{ pushd $RPM_BUILD_ROOT
  mkdir -p ./etc/X11/applnk/System
  cat > ./etc/X11/applnk/System/timetool.desktop <<EOF
[Desktop Entry]
Name=Time Tool
Comment=Set Time and Date
Exec=timetool
Terminal=0
Type=Application
EOF
popd
}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/timetool
/usr/lib/rhs/control-panel/timetool.init
/usr/lib/rhs/control-panel/timetool.xpm
%attr(0600,root,root)	%config(missingok) /etc/X11/applnk/System/timetool.desktop

%changelog
* Sat Jun 12 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 11 1999 Preston Brown <pbrown@redhat.com>
- better leapyear fix from  jrs@math.lsa.umich.edu

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- fixed Y2K leapyear bug

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- wmconfig only for root

* Thu Oct 30 1997 Otto Hammersmith <otto@redhat.com>
- fixed control-panel icon

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- requires control-panel (doesn't start properly from the command line)
- didn't switch to 24 hour time properly
