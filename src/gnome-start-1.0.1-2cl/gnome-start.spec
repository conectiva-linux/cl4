%define Name gnome-start
%define Version 1.0.1

Summary: Startup script and gnomeinitrc for GNOME.
Summary(pt_BR): Script de inicialização do GNOME
Summary(es): Script de arranque para GNOME
Name: %{Name}
Version: %{Version}
Release: 2cl
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL
URL: http://www.gnome.org/
BuildRoot: /tmp/%{Name}-%{Version}
Source: %{Name}-%{version}.tar.bz2
Source1: gnome
Requires: gnome-core

%description
Replacement for startx and xinitrc to start GNOME in a convenient way.
You have to use the 'gnome' command instead of 'startx' to start GNOME.

%description -l pt_BR
Substituto para o startx e xinitrc para inicializar o GNOME de forma
conveniente. Você terá que usar o comando 'gnome' no lugar de 'startx'
para inicializar o GNOME.

%description -l es
Script de arranque para GNOME

%prep
%setup -q -n %{Name}-%{Version}

%install

DESTDIR=$RPM_BUILD_ROOT; export DESTDIR
[ -n "`echo $DESTDIR | sed -n 's:^/tmp/[^.].*$:OK:p'`" ] && rm -rf $DESTDIR ||
(echo "Invalid BuildRoot: '$DESTDIR'! Check this .spec ..."; exit 1) || exit 1

# install gnome and gnomeinitrc
install -d $DESTDIR/etc/X11/xinit 
install -d $DESTDIR/usr/bin
install -o root -g root -m 755 gnomeinitrc $DESTDIR/etc/X11/xinit 
#install -o root -g root -m 755 gnome $DESTDIR/usr/bin
install -o root -g root -m 755 $RPM_SOURCE_DIR/gnome $DESTDIR/usr/bin

%clean

DESTDIR=$RPM_BUILD_ROOT;export DESTDIR;[ -n "$UID" ]&&[ "$UID" -gt 0 ]&&exit 0
[ -n "`echo $DESTDIR | sed -n 's:^/tmp/[^.].*$:OK:p'`" ] && rm -rf $DESTDIR ||
(echo "Invalid BuildRoot: '$DESTDIR'! Check this .spec ..."; exit 1) || exit 1

%files 
/etc/X11/xinit/gnomeinitrc
/usr/bin/gnome

%changelog
* Mon Jun 28 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fixes call to xauth

* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Added a check to allow us to run gnome more than once at the same time

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 08 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- First version of RPM package
- Added pt_BR translations
