Summary: Creates an initial ramdisk image for preloading modules.
Summary(pt_BR): Cria um disco de inicialização
Summary(es): Crea un disquete de arranque
Name: mkbootdisk
%define version 1.2
Version: %{version}
Release: 3cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: mkbootdisk-%{version}.tar.gz
Source700: mkbootdisk-man-pt_BR.tar
Patch0: mkbootdisk-1.1-conectiva.patch
ExclusiveArch: i386 sparc sparc64
ExclusiveOs: Linux
Requires: mkinitrd
%ifarch sparc sparc64
Requires: silo genromfs
%endif
BuildRoot: /var/tmp/%{name}-root

%description
The mkbootdisk program creates a standalone boot floppy disk for booting
the running system.  The created boot disk will look for the root
filesystem on the device mentioned in /etc/fstab and includes an
initial ramdisk image which will load any necessary SCSI modules for
the system.

%description -l pt_BR
Este pacote cria um disco de inicialização auto-contido. Assume que o
disco de inicialização deve usar a partição raiz configurada no arquivo
/etc/fstab. O disco de inicialização resultando inclui todos os módulos
SCSI necessários ao sistema.

%description -l es
Este paquete crea un disco de arranque autocontenido. Asume que
el disco de arranque debe usar la partición raíz configurada en
el archivo /etc/fstab. El disco de arranque obtenido incluye todos
los módulos SCSI necesarios al sistema.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
make BUILDROOT=$RPM_BUILD_ROOT install


mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/mkbootdisk-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) /sbin/mkbootdisk
%attr(644,root,root) /usr/man/man8/mkbootdisk.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Apr  7 1999 Matt Wilson <msw@redhat.com>
- pass load_ramdisk=2 as alan had to port his ramdisk hack from 2.0.x 

* Mon Apr  5 1999 Matt Wilson <msw@redhat.com>
- pass load_ramdisk=1 for rescue image, as 2.2 kernels get this right

* Thu Mar 18 1999 Matt Wilson <msw@redhat.com>
- fixed misspelling in man page

* Thu Feb 25 1999 Matt Wilson <msw@redhat.com>
- updated the description

* Thu Nov  5 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.

* Fri Oct 30 1998 Jakub Jelinek <jj@ultra.linux.cz>
- support for SPARC

* Sat Aug 29 1998 Erik Troan <ewt@redhat.com>
- wasn't including nfs, isofs, or fat modules properly
- mkinitrd args weren't passed right due to a typo
