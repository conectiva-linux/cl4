Summary: ASCII Tux (Linux Penguin) 
Summary(pt_BR): Tux em ASCII (Pingüim do Linux)
Summary(es): Tux en ASCII (Pingüino del Linux)
Name: linux_logo
Version: 2.05
Release: 6cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
BuildRoot: /var/tmp/linux-logo
Icon: ascii_penguin.gif
Source: linux_logo-2.05.tar.gz
Patch: linux_logo-2.05-i18n.patch
Requires: /bin/sh
BuildArchitectures: i386

%description
This package contains an ASCII Linux-Penguin.

%description -l pt_BR
Este pacote contém o tux, pingüim mascote do Linux.

%description -l es
Este paquete contiene el tux, pingüino mascota del Linux.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Oct 30 1998 Conectiva <dist@conectiva.com>
- rebuilt for Conectiva Linux 3.0

* Sat Aug 01 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- included i18n patch and pt_BR translation

* Wed Jul 29 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

%prep

%setup
%patch -p1

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/pt_BR/LC_MESSAGES
install -m 755 linux_logo $RPM_BUILD_ROOT/usr/bin/linux_logo
install -m 644 po/pt_BR.mo $RPM_BUILD_ROOT/usr/share/locale/pt_BR/LC_MESSAGES/linux_logo.mo

%clean 
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/linux_logo
/usr/share/locale/pt_BR/LC_MESSAGES/linux_logo.mo
