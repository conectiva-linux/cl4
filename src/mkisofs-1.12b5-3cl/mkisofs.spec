Summary: Creates an image of an ISO9660 filesystem.
Summary(pt_BR): Cria uma imagem de um sistema de arquivos ISO9660
Summary(es): Crea una imagen de un sistema de archivos ISO9660
Name: mkisofs
Version: 1.12b5
Release: 3cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://ftp.fokus.gmd.de/pub/unix/cdrecord/mkisofs/mkisofs-%{version}.tar.gz
Patch0: mkisofs-1.12b4-free.patch
BuildRoot: /var/tmp/%{name}-root

%description
The mkisofs program is used as a pre-mastering program; i.e., it
generates the ISO9660 filesystem.  Mkisofs takes a snapshot of
a given directory tree and generates a binary image of the tree
which will correspond to an ISO9660 filesystem when written to
a block device.  Mkisofs is used for writing CD-ROMs, and includes
support for creating bootable El Torito CD-ROMs.

Install the mkisofs package if you need a program for writing
CD-ROMs.

%description -l pt_BR
Este é o pacote mkisofs. Ele é usado para criar imagens de sistema
de arquivos ISO 9660 para criação de CD-ROMs. Agora inclui suporte
para fazer CD-ROMs de boot "El Torito".

%description -l es
Este es el paquete mkisofs. Se le usa para crear imágenes de sistema
de archivos ISO 9660 en la creación de CD-ROMs. Ahora incluye soporte
para hacer CD-ROMs de boot "El Torito".

%prep
%setup -q
%patch0 -p1 -b .free

%build
#CC="gcc $RPM_OPT_FLAGS" ./configure --prefix=/usr

%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man8}

make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/mkisofs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README README.eltorito README.session TODO
/usr/bin/mkisofs
/usr/man/man8/mkisofs.8

%changelog
* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.12b5.

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.12b4

* Tue Sep  1 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.11.3

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- fixed segv problems on glibc systems

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 1.11.2

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- Updated to 1.11.1

* Fri May 02 1997 Michael Fulbright <msf@redhat.com>
- Updated to released version of 1.11. 
    ( Should fix problem with files ending in a '.' )

* Tue Mar 18 1997 Michael Fulbright <msf@redhat.com>
- Updated to released version of 1.10.

* Tue Feb 25 1997 Michael Fulbright <msf@redhat.com>
- Updated to 1.10b7.

* Wed Feb 12 1997 Michael Fulbright <msf@redhat.com>
- Updated to 1.10b3.

* Wed Feb 12 1997 Michael Fulbright <msf@redhat.com>
- Added %doc line to spec file (was missing all docs before).
