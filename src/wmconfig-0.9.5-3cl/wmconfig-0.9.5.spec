Summary: A configuration tool for X window managers.
Summary(pt_BR): Configurador de gerenciadores de janelas
Summary(es): Configurador de Administradores de ventanas
Name: wmconfig
%define version 0.9.5
Version: %{version}
Release: 3cl
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source: ftp://ftp.redhat.com/home/gafton/wmconfig/wmconfig-%{version}.tar.gz
Patch0: wmconfig-0.9.5-cnc.patch
Patch1: wmconfig-kdedir.patch
Patch2: wmconfig-nameless.patch
Patch3: wmconfig-0.7-i18n.patch
Patch4: wmconfig-0.9.5-dot-directory.patch
BuildRoot: /var/tmp/wmconfig-root

%description
The wmconfig program is a helper program which provides output for use
in configuring window managers.  Wmconfig will produce a list of menu
definitions for a specified X window manager (currently, FVWM2, FVWM95,
AfterStep, MWM, IceWM and KDE are supported).  Wmconfig's output can
be placed into your .rc file or you can use the output for other
configuration purposes.

%description -l pt_BR
Este é um programa que gera configurações de menu para diferentes
gerenciadores de janela disponíveis para o sistema X11. É uma
tentativa de abstrair uma configuração única entre esses diferentes
gerenciadores. Atualmente suporta: FVWM2, FVWM95, Afterstep, MWM,
IceWM e KDE.

%description -l es
Este es un programa que crea configuraciones de menú para diferentes
administradores de ventana disponibles para el sistema X11. Es un
intento de abstraer una configuración única entre estos diferentes
administradores. Actualmente soporta: FVWM2, FVWM95, Afterstep,
MWM, IceWM y KDE.

%prep
%setup -q
%patch0 -p0
#patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
automake
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6 \
	--enable-gnome
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/X11R6/bin/wmconfig
%dir /etc/X11/wmconfig
/usr/X11R6/man/man1/wmconfig.1
%doc COPYING

%changelog
* Fri Jun 25 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- patch to read gnome's .directory files (i18n info)

* Fri Jun 04 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated to wmconfig 0.9.5

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 08 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- i18n
- removed kdedir patch

* Mon Mar 01 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Modified kde permissions 0700 -> 0755

* Fri Feb 26 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fix core dump with name less wmconfig file

* Thu Feb 25 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Update for version 0.7
- Patch for write kde applnks in other directories (--kdedir)

* Thu Dec 03 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- --rootmenu defaults to "Conectiva Linux"
