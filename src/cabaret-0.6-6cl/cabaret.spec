Summary: Text-mode File System Configuration Tool
Summary(pt_BR): Ferramenta de configuração de sistemas de arquivo, em modo texto.
Summary(es): Herramienta de configuración de sistemas de archivo, en modo texto.
Name: cabaret
Icon: cabaret.gif
Version: 0.6
Release: 6cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: cabaret-%{PACKAGE_VERSION}.tar.gz
Source1: cabaret.wmconfig.pt_BR
Source800: wmconfig.i18n.tgz
Requires: pythonlib >= 1.21
Requires: python snack python-intl
BuildArchitectures: noarch
BuildRoot: /var/tmp/cabaret-root

%changelog
* Tue Jun 22 1999 Guilherme Manika <gwm@conectiva.com>
- Removed ultra-ugly intl.so, now depends on python-intl

* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- wmconfig

* Wed Jun 24 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Added pt_BR translations

* Thu Nov 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed change types dialog

* Wed Nov 05 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed mounting
- fixed formatting

* Tue Nov 04 1997 Michael K. Johnson <johnsonm@redhat.com>
- adds mountpoints
- doesn't let you add existing mountpoints
- fixes grid management problems
- fixed wording

* Fri Oct 31 1997 Michael K. Johnson <johnsonm@redhat.com>
- initial version

%description
cabaret is a friendly text-mode program for manipulating /etc/fstab.
It allows you to add, delete, and modify mount points. It also lets
you mount and unmount partitions through its graphical interface.

%description -l pt_BR
Cabaret é um programa amigável em modo texto para manipular o
arquivo /etc/fstab. Ele permite adicionar, deletar e modificar mount
points. Ele também permite montar e desmontar partições através de
sua interface gráfica.

%description -l es
Cabaret es un programa amigable en modo texto para manipular el
archivo /etc/fstab. Permite adicionar, suprimir y modificar mount
points. También permite montar y desmontar particiones a través de
su interface gráfica.

%prep
%setup

%build
make

%install
make install ROOT=$RPM_BUILD_ROOT
cd po
make install ROOT=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
/usr/sbin/cabaret
/etc/X11/wmconfig/cabaret
/usr/lib/rhs/cabaret
/usr/share/locale/*/LC_MESSAGES/cabaret.mo
/usr/share/icons/cabaret.xpm
/usr/share/icons/mini/mini-cabaret.xpm
