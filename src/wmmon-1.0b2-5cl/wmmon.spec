%define name wmmon
%define version 1.0b2
%define release 5cl

%define builddir $RPM_BUILD_DIR/%{name}.app

Summary: CPU/Memory/Swap/Disk usage applet
Summary(pt_BR): Applet para monitorar o uso de CPU/Mem�ria/Disco/Swap  
Summary(es): Applet para monitorar el uso de CPU/Mem�ria/Disco/Swap
Summary(fr): Applette d'utilisation du processeur/m�moire/swap/disque

Name: %{name}
Version: %{version}
Release: %{release}
Group: User Interface/Desktops
Group(pt_BR): Interface do Usu�rio/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL
Url: http://windowmaker.mezaway.org
Source0: %{name}-%{version}.tar.bz2
Source800: wmmon-wmconfig.i18n.tgz
Patch: %{name}-%{version}-makefile.patch.bz2
Buildroot: /var/tmp/%{name}_root
Icon: %{name}.gif

%description
Wmmon is the swiss army knife of monitoring. It can
display CPU,Memory,Swap,Disk usage. But also the
uptime and other information that are useful to
system administrators. Wmmon is designed to work
with the WindowMaker dock.

%description -l pt_BR
Wmmon � o canivete su��o da monitora��o. Ele pode mostrar o uso
de CPU, mem�ria, swap, disco e outras informa��es �teis para o
administrador do sistema. Wmmon � projetado para funcionar com o
dock do WindowMaker.

%description -l es
Wmmon es el cuchillo suizo de la monitoraci�n. Puede visualizar el
uso de CPU, memoria, swap, disco y otras informaciones para los
administradores de sistema. Wmmon se dise�a para trabajar con el
dock de WindowMaker.

%description -l fr
Wmmon est le couteau suisse de la surveillance. Il
peut afficher l'utilisation du processeur, de la
m�moire, du swap et du disque. Mais aussi le temps
�coul� entre chaque red�marrage de la machine et
d'autres information utiles a l'administrateur
syst�me. Wmmon est con�u pour fonctionner avec le
dock de WindowMaker.

%prep

%setup -n %{name}.app

%patch -p1

%build
cd wmmon
make CFLAGS="$RPM_OPT_FLAGS"

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/bin}
cp %{builddir}/wmmon/wmmon $RPM_BUILD_ROOT/usr/X11R6/bin
strip $RPM_BUILD_ROOT/usr/X11R6/bin/wmmon



tar xvfpz $RPM_SOURCE_DIR/wmmon-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/wmmon
%attr(755,root,root) /usr/X11R6/bin/wmmon

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Thu Mar 04 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added pt_BR translations
