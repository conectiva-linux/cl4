Summary: The most commonly-used entries in the /dev directory.
Summary(pt_BR): Arquivos de dispositivos no /dev
Summary(es): Archivos de dispositivos en el /dev
Name: dev
Version: 2.7.7
Release: 6cl
Source0: dev-%{PACKAGE_VERSION}.tar.gz
Copyright: public domain
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Buildroot: /var/tmp/dev-root
Autoreqprov: no
Prefix: /dev
Requires: shadow-utils >= 970616-7
Prereq: mktemp grep sed fileutils textutils
Prereq: shadow-utils

%description
The Red Hat Linux operating system uses file system entries to represent
devices (CD-ROMs, floppy drives, etc.) attached to the machine. All of
these entries are in the /dev tree (although they don't have to be). 
This package contains the most commonly used /dev entries.  

The dev package is a basic part of your Red Hat Linux system and it needs
to be installed.

%description -l pt_BR
Sistemas Unix (incluindo Linux) usam arquivos para representar
dispositivos conectados à máquina. Todas essas entradas estão no
diretório /dev (ainda que elas não precisem necessariamente estar
no /dev), este pacote contém as entradas /dev mais utilizadas. Esses
arquivos são essenciais para um sistema funcionar corretamente.

%description -l es
Sistemas Unix (incluso Linux) usan archivos para representar
dispositivos conectados a la máquina. Todas estas entradas están en
el directorio /dev (mismo que no necesiten estar obligatoriamente en
/dev), este paquete contiene las entradas /dev más utilizadas. Estos
archivos son esenciales para que un sistema funcione correctamente.

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- included /dev/tty13

* Wed Jun  9 1999 Matt Wilson <msw@redhat.com>
- changed %post script to mount /dev/pts with the proper permissions

* Sat Apr 17 1999 Michael K. Johnson <johnsonm@redhat.com>
- added a great many devices, mostly from the 2.2 kernel,
  regularized some permissions

* Fri Apr 16 1999 Michael K. Johnson <johnsonm@redhat.com>
- now have all the sd* devices that are mentioned in Devices.txt

* Thu Apr 15 1999 Preston Brown <pbrown@redhat.com>
- joystick entries

* Thu Apr 15 1999 Michael K. Johnson <johnsonm@redhat.com>
- changed a requires line to a prereq line for the %post
- deal properly with fstab files with multiple proc entries

* Tue Apr 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- /dev/kbd files will be managed by pam_console like /dev/fb

* Mon Apr 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- /dev/fb devices are not sparc-specific and permissions will
  change as they are managed by pam_console by default.

* Fri Apr 09 1999 Michael K. Johnson <johnsonm@redhat.com>
- make sure permissions on /etc/fstab do not change while adding
  devpts filesystem

* Mon Mar 29 1999 Michael Johnson <johnsonm@redhat.com>
- added m68k devices from puffin

* Mon Mar 29 1999 Michael Johnson <johnsonm@redhat.com>
- fixed permissions on audio devices

* Sat Mar 27 1999 Cristian Gafton <gafton@redhat.com>
- added devices for Multitech IntelligentSerialInternal (isicom)

* Thu Mar 25 1999 Michael Johnson <johnsonm@redhat.com>
- added permission check so that careless tar use will not mangle permissions
- /dev/tty set to 666
- nb devices

* Tue Mar 23 1999 Michael Johnson <johnsonm@redhat.com>
- made /dev/zero world-writable again

* Sun Mar 21 1999 Matt Wilson <msw@redhat.com>
- added entries for DAC960 and Compaq Smart/2 RAID array controllers

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Mar 19 1999 Michael Johnson <johnsonm@redhat.com>
- isdnctrl messy symlink fixed

* Tue Mar 09 1999 Michael Johnson <johnsonm@redhat.com>
- fixed logic for case when /etc/fstab does not exist

* Tue Feb 23 1999 Michael Johnson <johnsonm@redhat.com>
- added ptmx and pts, moved console to 5,1
  NB: we add devpts to /etc/fstab if it is not there; folks who
  for any reason don't want to use devpts should COMMENT OUT (not
  remove) the line and we will try not to add it again in the
  future.
- opened permissions back up on old-style ptys

* Tue Feb 23 1999 Matt Wilson <msw@redhat.com>
- yes, sparcs have IDE devices now, you *need* those devices.

* Mon Dec 14 1998 Michael K. Johnson <johnsonm@redhat.com>
- console-config is dead
- permission check limiting is still the right thing to do, though,
  for whatever replaces console-config

* Wed Dec 09 1998 Michael K. Johnson <johnsonm@redhat.com>
- moved dynamically configured to archive (changed to tar)
- added console-config.d file
- limited permission checking for files console-config manages
- permissions changed to console-config defaults

* Fri May 08 1998 Michael K. Johnson <johnsonm@redhat.com>
- added paride devices

* Tue May 05 1998 Erik Troan <ewt@redhat.com>
- uses a filelist
- ghosts /dev/log

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- fixed groupadd call in the %install

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Apr 23 1998 Prospector System <bugs@redhat.com>
- translations modified for fr, tr

* Thu Apr 23 1998 Erik Troan <ewt@redhat.com>
- fixed preinstall script

* Tue Apr 21 1998 Erik Troan <ewt@redhat.com>
- updated groupadd to work with upgrades where the floppy group already exists

* Mon Nov 10 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added more ramdisk entries

* Wed Oct 29 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added fd and ramdisk symlinks

* Fri Oct 24 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added floppy group for floppies; made them group-writable.

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- added bpcd device

* Thu Apr 10 1997 Erik Troan <ewt@redhat.com>
- Added ftape devices

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Fixed stdin, stdout devices.
- Moved rtc to cpio archive
- Added ISDN devices

%prep
%setup -c -T

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
BUILD_DIR=`pwd`

# Make sure that the floppy group exists on the build machine
/usr/sbin/groupadd -g 19 -r -f floppy > /dev/null
/usr/sbin/groupadd -g 20 -r -f console > /dev/null

# unpack in build root
cd $RPM_BUILD_ROOT
tar xpSzf $RPM_SOURCE_DIR/dev-%{PACKAGE_VERSION}.tar.gz

cd $RPM_BUILD_ROOT/dev
mknod tty13 c 4 13

# tar doesn't save some permissions unless the p option is used
# this code protects against dev package updaters forgetting to
# use the p option when unpacking the souce tarball.
for dev in zero null tty ttyp0 ; do
  if [ ! $(ls -l $dev | awk '{print $1}') = crw-rw-rw- ] ; then
    echo bad permissions on device $dev 1>&2
    exit 1
  fi
done

# do some cleanup in build root
%ifarch sparc
# SPARC specific devices
ln -s sunmouse mouse
mknod kbd c 11 0
chmod 0600 kbd
mknod openprom c 10 139

# remove devices that will *never* exist on a SPARC
rm -f aztcd mcd sbpcd1 cdu31a sbpcd2 scd3
rm -f sjcd cdu535 sbpcd3 sonycd cm206cd sbpcd
rm -f gscd sbpcd0 atibm inportbm logibm

%endif

%ifarch m68k                                                                    
# m68k specific devices                                                         
mknod amigamouse c 10 4                                                         
mknod atarimouse c 10 5                                                         
mknod apollomouse c 10 7                                                        
ln -s amigamouse mouse                                                          
mknod fdhd0 b 2 4                                                               
mknod fdhd1 b 2 5                                                               
mknod fb0current c 29 0                                                         
mknod fb1current c 29 32                                                        
mknod kbd c 11 0                                                                
chmod 0600 kbd
                                                                                
# remove devices that will *never* exist on a m68k                              
rm -f hd* aztcd mcd sbpcd1 cdu31a sbpcd2 scd3                                   
rm -f sjcd cdu535 sbpcd3 sonycd cm206cd sbpcd                                   
rm -f gscd sbpcd0 atibm inportbm logibm psaux                                   
                                                                                
%endif

# build the file list
cd $BUILD_DIR
(cd $RPM_BUILD_ROOT/dev; ls) | sed 's,^,/dev/,' | sed '{
  /\/dev\/log$/ s/^/%ghost /
  /\/dev\/fd..*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/fb.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/video.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/radio.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/winradio.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/vtx.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/vbi.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/kbd.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/audio.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/js.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/cua.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/dsp*.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/midi.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/mixer.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/sequencer/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/sndstat.*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/tty[SCDEIMR].*/ s/^/%verify(not group,mode,mtime) /
  /\/dev\/tty[a-z].$/ s/^/%verify(size) /
  /\/dev\/pty.*/ s/^/%verify(size) /
}' > filelist
# that "size" should really be "maj,min" but rpm doesn't
# follow Maximum RPM's documentation of %verify...

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -g 19 -r -f floppy
/usr/sbin/groupadd -g 20 -r -f console

%post
if [ -f /etc/fstab ] ; then
  # add /dev/pts to fstab if fstab exists (install2 does it during install)
  if grep 'devpts' /etc/fstab >/dev/null 2>&1 ; then 
      # correct permissions from broken dev packages
      TMP=$(mktemp /tmp/fstab.XXXXXX)
      sed 's/devpts.*mode=0622/devpts  gid=5,mode=620/g' < /etc/fstab > $TMP && cat $TMP > /etc/fstab || { echo "failed to correct devpts permissions in /etc/fstab" 1>&2 ; exit 1 ; }
  else
    # note that we do not disallow comments; we wish to allow people
    # to comment it out if they so desire.
    if [ $(grep '/proc' /dev/fstab 2>/dev/null | wc -l) -gt 1 ] ; then
      # ugly but robust
      echo '
none                    /dev/pts                devpts  gid=5,mode=620        0 0' \
        >> /etc/fstab || { echo "failed to add devpts filesystem to /etc/fstab" 1>&2 ; exit 1 ; }
    else
      # beautiful in the common case
      TMP=$(mktemp /tmp/fstab.XXXXXX)
      sed '/\/proc/a\
none                    /dev/pts                devpts  gid=5,mode=620        0 0
          ' < /etc/fstab > $TMP && cat $TMP > /etc/fstab || { echo "failed to add devpts filesystem to /etc/fstab" 1>&2 ; exit 1 ; }
      rm -f $TMP
    fi
  fi
fi

%files -f filelist
