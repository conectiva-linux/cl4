Name:		pciutils
Version:	1.99.5
Release: 1cl
Source:		ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Patch: 		pciutils-werror.patch
Patch2:		pciutils-%{version}.sparc.patch
Copyright:	GNU GPL
Buildroot: 	/tmp/%{name}-%{version}-root
ExclusiveOS: 	Linux
ExcludeArch:	armv4l
Summary: Linux PCI utilities.
Summary(pt_BR): Utilitários para PCI do Linux
Summary(es): Linux PCI utilities.
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Requires: kernel >= 2.1.85

%description
This package contains various utilities for inspecting
and setting devices connected to the PCI bus.

It requires kernel version 2.1.82 or newer (supporting
the /proc/bus/pci interface).

%description -l pt_BR
Este pacote contém vários utilitários para inspeção e
configuração de dispositivos conectados ao barramento
PCI do seu computador.

O pciutils requer o kernel versão 2.1.82 ou superior.

%description -l es
This package contains various utilities for inspecting
and setting devices connected to the PCI bus.

It requires kernel version 2.1.82 or newer (supporting
the /proc/bus/pci interface).

%prep
%setup -q
%patch -p1
%patch2 -p1

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,/usr/man/man8,/usr/share}

install -s lspci setpci $RPM_BUILD_ROOT/sbin
install lspci.8 setpci.8 $RPM_BUILD_ROOT/usr/man/man8
install pci.ids $RPM_BUILD_ROOT/usr/share

%files
%defattr(0644, root, root, 0755)
%attr(0644, root, man) /usr/man/man8/*
%attr(0711, root, root) /sbin/*
%config /usr/share/pci.ids
%doc README ChangeLog pciutils.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Jakub Jelinek  <jj@ultra.linux.cz>
- update to 1.99.5
- fix sparc64 operation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Thu Feb  4 1999 Bill Nottingham <notting@redhat.com>
- initial build
