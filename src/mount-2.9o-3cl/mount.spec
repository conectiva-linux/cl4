Summary: Programs for mounting and unmounting filesystems.
Summary(pt_BR): Programas para montagem e desmontagem de sistemas de arquivos
Summary(es): Programas para montaje y desmontaje de sistemas de archivos
Name: mount
Exclusiveos: Linux
Version: 2.9o
Release: 3cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.win.tue.nl/pub/linux/util/mount-%{version}.tar.bz2
Source700: mount-man-pt_BR.tar
Patch0: mount-2.9o-standalone.patch
Patch1: mount-2.9i-loop.patch
Patch2: mount-2.9o-sparc.patch
Patch3: mount-2.9o-fs.patch
Patch4: mount-2.9o-fix.patch

BuildRoot: /var/tmp/%{name}-root

%description
The mount package contains the mount, umount, swapon and swapoff
programs.  Accessible files on your system are arranged in one big
tree or hierarchy.  These files can be spread out over several
devices. The mount command attaches a filesystem on some device to
your system's file tree.  The umount command detaches a filesystem
from the tree.  Swapon and swapoff, respectively, specify and disable
devices and files for paging and swapping.

%description -l pt_BR
Mount é usado para adicionar novos sistemas de arquivos , tanto
local como em rede, para a estrutura do seu diretório corrente. Os
sistema de arquivos devem já existir para isso funcionar. Ele pode
também ser usado para mudar os tipos de acesso que o kernel usa
para os sistemas de arquivos já montados.

Este pacote é crítico para o funcionamento do seu sistema.

%description -l es
Mount se usa para adicionar nuevos sistemas de archivos, tanto local
como en red, para la estructura de su directorio corriente. Los
sistemas de archivos deben ya existir para que esto funcione. Puede
también ser usado para cambiar los tipos de acceso que el kernel
utiliza para los sistemas de archivos ya montados.  Este paquete
es crítico para el funcionamiento de tu sistema.

%package -n losetup
Summary: Programs for setting up and configuring loopback devices.
Summary(pt_BR): Programas para configurar dispositivos loopback
Summary(es): Programas para configurar dispositivos loopback
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base

%description -n losetup
Linux supports a special block device called the loop device, which
maps a normal file onto a virtual block device.  This allows for the
file to be used as a "virtual file system" inside another file.  Losetup
is used to associate loop devices with regular files or block devices,
to detach loop devices and to query the status of a loop device.

%description -l pt_BR -n losetup
Linux suporta um dispositivo de bloco especial chamado dispositivo
loopback, que mapeia um arquivo normal em um dispositivo de bloco
virtual. Este pacote contém programas para o estabelecimento e
remoção do mapeamento entre arquivos e dispositivos de loopback.

Dispositivos de bloco loopback não devem ser confundidos com o
dispositivo de rede loopback, que é configurado com o comando
ifconfig.

%description -l es -n losetup
Linux soporta un dispositivo de bloque especial llamado
dispositivo loopback, hace el mapa de un archivo normal en un
dispositivo de bloque virtual. Este paquete contiene programas
para el establecimiento y remoción de los mapas entre archivos y
dispositivos de loopback.  Los dispositivos de bloque loopback no
deben ser confundidos con el dispositivo de red loopback, que está
configurado con el comando ifconfig.

%prep
%setup -q
%patch0 -p1 -b .standalone
%patch1 -p2 -b .loop
%patch2 -p2 -b .sparc
%patch3 -p2 -b .fstypes
%patch4 -p2 -b .fix

cat << EOF > defines.h
#define HAVE_locale_h	1
EOF

cat << EOF  > version.h
#define	UTIL_LINUX_VERSION "%{version}"
const char * const util_linux_version = "mount " UTIL_LINUX_VERSION;
EOF

%build

( cd lib; cc $RPM_OPT_FLAGS -c setproctitle.c )

make	LIB=./lib \
	BINDIR=/bin \
	SBINDIR=/sbin \
	MANDIR=/usr/man \
	all

%install
rm -rf $RPM_BUILD_ROOT

make	LIB=./lib \
	BINDIR=$RPM_BUILD_ROOT/bin \
	SBINDIR=$RPM_BUILD_ROOT/sbin \
	MAN5DIR=$RPM_BUILD_ROOT/usr/man/man5 \
	MAN8DIR=$RPM_BUILD_ROOT/usr/man/man8 \
	INSTALLDIR="install -d -m 755" \
	INSTALLSUID="install -s -m 755" \
	INSTALLBIN="install -s -m 755" \
	INSTALLMAN="install -m 644" \
	install




mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/mount-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(4755,root,root)	/bin/mount
%attr(4755,root,root)	/bin/umount
/sbin/swapon
/sbin/swapoff
/usr/man/man5/fstab.5
/usr/man/man5/nfs.5
/usr/man/man8/mount.8
/usr/man/man8/swapoff.8
/usr/man/man8/swapon.8
/usr/man/man8/umount.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%files -n losetup
%defattr(-,root,root)
/usr/man/man8/losetup.8
/sbin/losetup

%changelog
* Tue Jun 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Tue May 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added pt_BR man pages

* Thu Apr 15 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9o.

* Fri Mar 26 1999 Bill Nottingham <notting@redhat.com>
- accept ncpfs/smbfs as valid types, not just ncp/smb

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Sun Mar 14 1999 Jeff Johnson <jbj@redhat.com>
- rebuild to try and get setuid bits in binary package  -- they're in the
  spec file %attr (#1507).

* Mon Jan 18 1999 Jeff Johnson <jbj@redhat.com>
- rebuild for Raw Hide.
- update to mount-2.9 (from util-linux-2.9)

* Tue Oct 06 1998 Cristian Gafton <gafton@redhat.com>
- accept the fact that sometimes the last line in fstab does not have a \n

* Wed Aug  5 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.8a (from util-linux)

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixed to compile on manhattan

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to mount-2.7l

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- updated for glibc 2.1

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- updated to 2.7f
- added glibc hacks for the Alpha (I don't know why Intel doesn't need them)

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- updated to 2.6h
- built against glibc
