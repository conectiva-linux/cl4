%define name wminet
%define version 1.0b2
%define release 3cl

%define builddir $RPM_BUILD_DIR/%{name}.app

Summary: Network services monitoring applet
Summary(pt_BR): Applet para monitorar serviços de rede
Summary(es): Applet para monitorar servicios de red
Summary(fr): Applette d'utilisation des services réseau

Name: %{name}
Version: %{version}
Release: %{release}
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL
Url: http://windowmaker.mezaway.org
Source0: %{name}-%{version}.tar.gz
Source800: wminet-wmconfig.i18n.tgz
Buildroot: /var/tmp/%{name}_root
Icon: %{name}.gif

%description
Wminet monitors network services such as
FTP, HTTP and NFS as well as the number of
users and processes on your system.

%description -l pt_BR
Wminet monitora serviços de rede tais como FTP, HTTP e NFS bem como
o número de usuários e processos no sistema.

%description -l es
Wminet monitora servicios de red (FTP, HTTP y NFS) bien como
el número de usuarios y procesos en el sistema.

%description -l fr
Wminet surveille les services réseau comme
FTP, HTTP et NFS ainsi que le nombre d'utilisateurs
et de processus sur votre système.

%prep

%setup -n %{name}.app

%build
cd wminet
make FLAGS="$RPM_OPT_FLAGS"

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/bin}
cp %{builddir}/wminet/wminet $RPM_BUILD_ROOT/usr/X11R6/bin
strip $RPM_BUILD_ROOT/usr/X11R6/bin/wminet


tar xvfpz $RPM_SOURCE_DIR/wminet-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO wminet/wminetrc
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/wminet
%attr(755,root,root) /usr/X11R6/bin/wminet

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- added Group, Summary and %description translations
