Summary: Creates an initial ramdisk image for preloading modules.
Summary(pt_BR): Cria um ramdisk inicial
Summary(es): Crea un ramdisk inicial
Name: mkinitrd
%define version 2.0
Version: %{version}
Release: 2cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: mkinitrd-%{version}.tar.gz
Source700: mkinitrd-man-pt_BR.tar
ExclusiveArch: i386 sparc sparc64
ExclusiveOs: Linux
Requires: ash losetup e2fsprogs bash fileutils grep mount gzip tar modutils
BuildRoot: /var/tmp/%{name}-root

%description
Mkinitrd creates filesystem images for use as initial ramdisk (initrd)
images.  These ramdisk images are often used to preload the block
device modules (SCSI or RAID) needed to access the root filesystem.

In other words, generic kernels can be built without drivers for any
SCSI adapters which load the SCSI driver as a module.  Since the kernel
needs to read those modules, but in this case it isn't able to address
the SCSI adapter, an initial ramdisk is used.  The initial ramdisk is
loaded by the operating system loader (normally LILO) and is available
to the kernel as soon as the ramdisk is loaded.  The ramdisk image
loads the proper SCSI adapter and allows the kernel to mount the root
filesystem.  The mkinitrd program creates such a ramdisk using
information found in the /etc/conf.modules file.

%description -l pt_BR
Kernels genéricos podem ser construídos sem drivers para quaisquer
placas SCSI, carregando o driver SCSI como um módulo. Para solucionar
o problema de permitir ao kernel ler o módulo sem ser capaz de
acessar a placa SCSI é usado um ramdisk inicial. Este ramdisk é
carregado pelo carregador do sistema operacional (como o lilo) e
é disponibilizado ao kernel tão logo seja carregado. Esta imagem
é responsável pela carga do módulo SCSI adequado para permitir
ao root montar o sistema de arquivos root. Este programa cria tal
imagem de ramdisk usando informação disponível em /etc/conf.modules.

%description -l es
Kernels genéricos pueden ser construidos sin drivers para cualquiera
de las tarjetas SCSI, cargando el driver SCSI como un módulo. Para
solucionar el problema de permitir al kernel leer el módulo sin ser
capaz de acceder a la tarjeta SCSI se usa un ramdisk inicial. Este
ramdisk se carga por un cargador del sistema operativo (como el lilo)
y se pone a disposición del kernel tan luego se cargue. Esta imagen
es responsable por la carga del módulo SCSI adecuado para permitir
al root montar el sistema de archivos root. Este programa crea tal
imagen de ramdisk usando información disponible en /etc/conf.modules.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
make BUILDROOT=$RPM_BUILD_ROOT install


mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/mkinitrd-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) /sbin/mkinitrd
%attr(644,root,root) /usr/man/man8/mkinitrd.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Fixed Requires

* Sat Mar 27 1999 Matt Wilson <msw@redhat.com>
- --omit-scsi-modules now omits all scsi modules
- updated documentation
- mkinitrd now grabs scsi_hostadapter modules from anywhere -
  some RAID controller modules live in block/

* Thu Feb 25 1999 Matt Wilson <msw@redhat.com>
- updated description

* Mon Jan 11 1999 Matt Wilson <msw@redhat.com>
- Ignore the absence of scsi modules, include them if they are there, but
  don't complain if they are not.
- changed --no-scsi-modules to --omit-scsi-modules (as it should have been)

* Thu Nov  5 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.

* Tue Oct 20 1998 Jakub Jelinek <jj@ultra.linux.cz>
- fix for combined sparc/sparc64 insmod, also pluto module is really
  fc4:soc:pluto and we don't look at deps, so special case it.

* Sat Aug 29 1998 Erik Troan <ewt@redhat.com>
- replaced --needs-scsi-mods (which is now the default) with
  --omit-scsi-mods

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- correct obscure regex/shell interaction (hardwires tabs on line 232)

* Mon Jan 12 1998 Erik Troan <ewt@redhat.com>
- added 'make archive' rule to Makefile
- rewrote install procedure for more robust version handling
- be smarter about grabbing options from /etc/conf.modules

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- made it use /bin/ash.static

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Only use '-s' to install binaries if /usr/bin/strip is present.
- Use an image size of 2500 if binaries can't be stripped (1500 otherwise)
- Don't use "mount -o loop" anymore -- losetup the proper devices manually
- Requires losetup, e2fsprogs

* Wed Mar 12 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fixed a bug in parsing options.
- Changed to use a build tree, then copy the finished tree into the
  image after it is built.
- Added patches derived from ones written by Christian Hechelmann which
  add an option to put the kernel version number at the end of the module
  name and use install -s to strip binaries on the fly.
