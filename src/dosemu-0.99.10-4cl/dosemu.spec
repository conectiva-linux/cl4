Summary: A DOS emulator.
Summary(pt_BR): Emulador DOS
Summary(es): Emulador DOS
Name: dosemu
Version: 0.99.10
Release: 4cl
Exclusivearch: i386
Copyright: distributable
Group: Applications/Emulators
Group(pt_BR): Aplicações/Emuladores
Group(es): Aplicaciones/Emuladores
Source0: ftp://dtp.dosemu.org/dosemu/dosemu-%{PACKAGE_VERSION}.tgz
Source1: http://www.freedos.org/files/fdbeta1.zip
Source800: dosemu-wmconfig.i18n.tgz
# this kernel is generated from the freedos.144 floppy image coming with the
# above. Why they ship the kernel on the floppy image only ?!
Source2: dosemu-freedos-kernel.tar.gz
Patch0: dosemu-0.66.7-config.patch
Patch1: dosemu-0.66.7-glibc.patch
Patch2: dosemu-0.66.7-pushal.patch
Patch3: dosemu-0.98.1-security.patch
Patch4: dosemu-0.98.1-justroot.patch
Requires: kernel >= 2.0.28, mtools >= 3.6
Url: http://www.dosemu.org
Buildroot: /var/tmp/dosemu-root

%package -n xdosemu
Requires: dosemu = %{PACKAGE_VERSION}
Summary: A DOS emulator for the X Window System.
Summary(pt_BR): Emulador DOS que roda no X
Summary(es): Emulador DOS que se ejecuta en X
Group: Applications/Emulators
Group(pt_BR): Aplicações/Emuladores
Group(es): Aplicaciones/Emuladores

%package freedos
Requires: dosemu = %{PACKAGE_VERSION}
Summary: A FreeDOS hdimage for dosemu, a DOS emulator, to use.
Summary(pt_BR): Uma imagem de disco rígido do FreeDOS para o dosemu, substituindo outras versões do DOS
Summary(es): Una imagen de disco duro del FreeDOS para dosemu, substituyendo otras versiones del DOS
Group: Applications/Emulators
Group(pt_BR): Aplicações/Emuladores
Group(es): Aplicaciones/Emuladores

%description
Dosemu is a DOS emulator.  Once you've installed dosemu, start the DOS
emulator by typing in the dos command.

You need to install dosemu if you use DOS programs and you want to be able
to run them on your Red Hat Linux system.  You may also need to install
the dosemu-freedos package.

%description -l pt_BR
Essa é uma versão do emulador DOS que foi projetada para rodar em
sessões X Window. Oferece suporte para gráficos VGA bem como suporte
para mouse.

%description -l es
Esta es una versión del emulador DOS que fue proyectada para
ejecutarse en secciones X Window. Ofrece soporte a gráficos VGA
como también soporte a ratón.

%description -n xdosemu
Xdosemu is a version of the dosemu DOS emulator that runs with the X
]Window System.  Xdosemu provides VGA graphics and mouse support.

Install xdosemu if you need to run DOS programs on your system, and you'd
like to do so with the convenience of graphics support and mouse
capabilities.

%description -l pt_BR -n xdosemu
Esta é a versão do emulador DOS desenhada para rodar em uma janela
do X Window. Possui suporte a gráficos VGA e mouse.

%description -l es -n xdosemu
Esta es la versión del emulador DOS dibujada para ejecutarse en
una ventana del X Window. Posee soporte para gráficos VGA y ratón.

%description freedos
Generally, the dosemu DOS emulator requires either that your system
have some version of DOS available or that your system's partitions
were formatted and installed with DOS. If your system does not meet
either of the previous requirements, you can instead use the dosemu-
freedos package, which contains an hdimage file which will be
installed in teh /var/lib/dosemu directory. The hdimage file is
already bootable with FreeDOS.

You will need to edit your /etc/dosemu.conf file to add the
image to the list of disk 'drives' used by dosemu.

Install dosemu-freedos if you are installing the dosemu package
and you don't have a version of DOS available on your system,
and your system's partitions were not formatted and installed
with DOS.

%description -l pt_BR freedos
Este pacote inclui uma imagem de disco rígido que será instalada no
diretório /var/lib/dosemu se for necessário uma versão do DOS para
o uso do dosemu.

Geralmente o dosemu requer uma versão qualquer do DOS para inicializar
seu arquivo hdimage antes do primeiro uso ou que você tenha alguma
partição formatada e com o DOS instalado. Se nenhuma destas duas opções
estiver disponível use esta imagem que já é inicializável com o FreeDOS.

Será necessário editar o arquivo /etc/dosemu.conf para adicionar esta
imagem na lista de "drives" usados pelo dosemu.

%description -l es freedos
Este paquete incluye una imagen de disco duro que será instalada
en el directorio /var/lib/dosemu, si es necesaria una versión
del DOS para el uso del dosemu.  Generalmente dosemu requiere una
versión cualquiera del DOS para arrancar su archivo hdimage antes
del primer uso, o que tengas alguna partición formateada y con el
DOS instalado. Si ninguna de estas dos opciones está disponible usa
esta imagen que ya arranca con el FreeDOs.  Será necesario editar
el archivo /etc/dosemu.conf para añadir esta imagen en la lista de
"drives" usados por el dosemu.

%prep
%setup -q
%patch0 -p1 -b .lock
#%patch2 -p1 -b .pushal
%patch3 -p1 -b .security
%patch4 -p1 -b .justroot
unzip -L $RPM_SOURCE_DIR/fdbeta1.zip
rm -rf freedos
mkdir freedos
for i in orlando/{base,sys,util}/?/*.zip ; do
    unzip -d freedos -q $i
done
tar xzf $RPM_SOURCE_DIR/dosemu-freedos-kernel.tar.gz -C freedos

%build
PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/X11R6/bin
./default-configure
echo | make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
make install INSTROOT=$RPM_BUILD_ROOT
install -m 755 src/tools/periph/{hdinfo,mkhdimage,mkfatimage16} $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/icons
install -m 644 etc/dosemu.xpm $RPM_BUILD_ROOT/usr/share/icons
install -m 644 etc/dosemu.users.secure $RPM_BUILD_ROOT/etc/dosemu.users
src/tools/periph/mkfatimage16 -p -k 8192 -l FreeDos \
	-b freedos/kernel/boot.bin \
	-f $RPM_BUILD_ROOT/var/lib/dosemu/hdimage.freedos \
	freedos/kernel/* 
FREEDOS=`/bin/mktemp /tmp/freedos.XXXXXX`
echo "drive n: file=\"$RPM_BUILD_ROOT/var/lib/dosemu/hdimage.freedos\" offset=8832" > $FREEDOS
MTOOLSRC=$FREEDOS
export MTOOLSRC
mcopy -o/ freedos/BIN freedos/DOC freedos/HELP n:
mmd n:/DOSEMU
mcopy -/ commands/* n:/DOSEMU
mcopy commands/exitemu* n:/
mdir -w n:
rm -f $FREEDOS
unset MTOOLSRC

install -m 644 etc/hdimage.dist $RPM_BUILD_ROOT/var/lib/dosemu/hdimage
# install dexe utils
#install -m 755 dexe/{do_mtools,extract-dos,mkdexe,myxcopy} $RPM_BUILD_ROOT/usr/bin

cat <<EOF >$RPM_BUILD_ROOT/usr/bin/rundos
#!/bin/sh
BINDIR=/bin
export BINDIR 
# ignore errors if user does not have module installed
/usr/bin/dos
EOF
chmod 0755 $RPM_BUILD_ROOT/usr/bin/rundos

# Strip things
strip $RPM_BUILD_ROOT/usr/bin/* || :

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig





tar xvfpz $RPM_SOURCE_DIR/dosemu-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%post -n xdosemu
if [ -x /usr/X11R6/bin/mkfontdir ]; then
	(cd /usr/X11R6/lib/X11/fonts/misc; /usr/X11R6/bin/mkfontdir)
fi
killall -USR1 xfs > /dev/null 2>&1 || :

%postun -n xdosemu
if [ -x /usr/X11R6/bin/mkfontdir ]; then
	(cd /usr/X11R6/lib/X11/fonts/misc; /usr/X11R6/bin/mkfontdir)
fi
killall -USR1 xfs > /dev/null 2>&1 || :

%post freedos
[ -e /var/lib/dosemu/hdimage.first ] || \
    ln -s hdimage.freedos /var/lib/dosemu/hdimage.first

%postun freedos
if [ $1 = 0 ]; then
  if [ -e /var/lib/dosemu/hdimage.first ]; then
    rm -f /var/lib/dosemu/hdimage.first
  fi
fi
    
%files
%defattr(-,root,root)
%doc QuickStart doc/*
%dir /var/lib/dosemu
%config /etc/dosemu.conf
%config /etc/dosemu.users
%config /var/lib/dosemu/hdimage
%config /var/lib/dosemu/global.conf
/usr/bin/dos
/usr/bin/dosdebug
/usr/bin/dosexec
/usr/bin/hdinfo
/usr/bin/mkhdimage
/usr/bin/mkfatimage16
/usr/bin/rundos
/usr/man/man1/dos.1
/usr/man/man1/dosdebug.1
/usr/man/man1/mkfatimage16.1
/usr/share/icons/dosemu.xpm

%files -n xdosemu
%defattr(-,root,root)
/usr/bin/xdos
/usr/bin/xtermdos
/usr/man/man1/xdos.1
/usr/man/man1/xtermdos.1
/usr/X11R6/lib/X11/fonts/misc/vga.pcf

%files freedos
%config /var/lib/dosemu/hdimage.freedos

%clean
rm -rf $RPM_BUILD_ROOT
rm -f dosemu.files

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 28 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- added Group, Summary and %description translations

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- remove hdimage.first link on deinstallation of freedos.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Wed Mar 17 1999 Matt Wilson <msw@redhat.com>
- fixed %post and %postun scripts
- version 0.99.10

* Tue Jan 12 1999 Matt Wilson <msw@redhat.com>
- version 0.99.6

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- version 0.98.1
- freedos has its own subpackage

* Wed Jun 24 1998 Alan Cox <alan@redhat.com>
- Wrote additional fixes for dexe overflow problem in parser.y

* Tue Jun 23 1998 Alan Cox <alan@redhat.com>
- Applied the security fixes from Hans Lerman

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- added DOS-C kernel and FreeDos utilities

* Thu Jan 29 1998 Cristian Gafton <gafton@redhat.com>
- updated spec file to include all the available commands
- uses a buildroot
- ship mkfatimage16, which is the only binary that can create a real hdimage
  file

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Updated to 0.66.7
- Ported to glibc

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Updated to 0.66.2.
- Removed /usr/bin/load-dosmods as we don't need emumod.o anymore

* Tue Mar 11 1997 Michael K. Johnson <johnsonm@redhat.com>
- Modify the default configuration file to use /var/lock in
  ascii format for lock files, as specified in the FSSTD/FHS.

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Assume vm86plus system call does not exist.
- N.B. This should be changed in a future version with a later kernel
  that supports that system call by default.
- Install the mkhdimage program.
