Summary: File System Configuration Tool
Summary(pt_BR): Ferramenta de Configuração de Sistemas de Arquivos
Summary(es): Herramienta de Configuración de Sistemas de Archivos
Name: fstool
Icon: fstool.gif
Version: 2.6
Release: 8cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: fstool-2.6.tar.gz
Source800: wmconfig.i18n.tgz
Requires: tcl tk perl
BuildArchitectures: noarch

%changelog
* Mon Jun 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt to remove dependencies on TkStep-replace

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations


* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>

- wmconfig only for root
- put icon in /usr/share/icons

* Tue Oct 28 1997 Otto Hammersmith <otto@redhat.com>

- fixed filename for the icon in control-panel

* Fri Oct 24 1997 Michael K. Johnson <johnsonm@redhat.com>

- updated to include Miguel's enhancements.
- include xpm, wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>

- made a noarch package

%description
The fstool is a X program for manipulating /etc/fstab. It allows you
to add, delete, and modify amount points. It also lets you mount
and unmount partitions through its graphical interface.

%description -l pt_BR
O fstool é um programa X para manipular o arquivo /etc/fstab. Ele
permite adicionar, remover e modificar pontos de montagem. Ele
também permite montar e desmontar partições através de uma interface
gráfica.

%description -l es
Fstool es un programa X para manipular el archivo /etc/fstab. Permite
adicionar, eliminar y modificar puntos de montaje. También permite
montar y desmontar particiones a través de una interface gráfica.

%prep
%setup

%build
make

%install
mkdir -p /usr/lib/rhs/control-panel
make install
mkdir -p /usr/share/icons
cp /usr/lib/rhs/control-panel/fstool.xpm /usr/share/icons

mkdir -p /etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C /etc/X11/wmconfig
chmod 600 /etc/X11/wmconfig/fstool

%files
/usr/bin/dfplus
/usr/bin/fstool
/usr/lib/rhs/control-panel/fstool-aux
/usr/lib/rhs/control-panel/fstool.init
/usr/lib/rhs/control-panel/fstool.xpm
/usr/share/icons/fstool.xpm
%config(missingok) /etc/X11/wmconfig/fstool
