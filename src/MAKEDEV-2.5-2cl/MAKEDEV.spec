Summary: Creates and maintains device files in /dev.
Summary(pt_BR): Script para fazer e atualizar entradas referentes a dispositivos em /dev
Summary(es): Script para hacer y actualizar entradas referentes a dispositivos en /dev
Name: MAKEDEV
Version: 2.5
Release: 2cl
Copyright: none
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://tsx-11.mit.edu/pub/linux/sources/sbin/MAKEDEV-%{PACKAGE_VERSION}.tar.gz
Requires: /bin/sh fileutils shadow-utils >= 970616-7
Prereq: shadow-utils
# n.b. prerequires shadow-utils >= 970616-7; rpm understands that
BuildArchitectures: noarch
BuildRoot: /var/tmp/MAKEDEV-root

%description
The /dev directory contains important files which correspond to
the hardware on your system, such as sound cards, serial or 
printer ports, tape and CD-ROM drives and more. MAKEDEV is 
a script which helps you create and maintain the files in 
your /dev directory.

These are the files needed to install MAKEDEV.

%description -l pt_BR
O diretório /dev possui arquivos especiais, cada um deles
correspondendo a um tipo de dispositivo de hardware que o Linux
suporta. Este pacote contém um script que torna mais fácil a criação
e manutenção dos arquivos no diretório /dev.

%description -l es
El directorio /dev posee archivos especiales, cada uno de ellos
correspondiendo a un tipo de dispositivo de hardware que Linux
soporta. Este paquete contiene un script que hace más fácil la
creación y manutención de los archivos en el directorio /dev.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/dev
mkdir -p $RPM_BUILD_ROOT/usr/man/man8

make ROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -g 19 -o -f floppy > /dev/null

%files
%defattr(-,root,root)
/dev/MAKEDEV
/usr/man/man8/MAKEDEV.8

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x and kernel 2.2.x

* Sat Apr 17 1999 Michael K. Johnson <johnsonm@redhat.com>
- create version 2.5 with a great many devices added from the 2.2 kernel
  devices.txt

* Tue Apr 13 1999 Preston Brown <pbrown@redhat.com>
- close bug #2157

* Thu Mar 25 1999 Michael Johnson <johnsonm@redhat.com>
- sg unification
- nb devices

* Thu Mar 25 1999 Jakub Jelinek <jj@ultra.linux.cz>
- create correct /dev/console (c 5 1), support for SCSI
  disk devices sdi - sddx

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 9)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- glibc 2.1

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Apr 23 1998 Prospector System <bugs@redhat.com>
- translations modified for fr, tr

* Thu Apr 23 1998 Erik Troan <ewt@redhat.com>
- fixed group add script (had -r instead of -o)

* Fri Apr 17 1998 Erik Troan <ewt@redhat.com>
- put -o option on groupadd after -g -- I hope Christian can tell me why

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- redirect groupadd call so that we're more quiet

* Fri Oct 24 1997 Michael K. Johnson <johnsonm@redhat.com>
- 2.3.1: use /usr/sbin/groupadd from new shadow utils

* Mon Sep 29 1997 Michael K. Johnson <johnsonm@redhat.com>
- Updated to 2.3, as Nick agreed to me making an interim release while
  he figures out whether he wants to be the maintainer.

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- added dependencies
