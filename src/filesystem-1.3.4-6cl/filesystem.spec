Summary: The basic directory layout for a Linux system.
Summary(pt_BR): Layout básico do sistema de arquivos
Summary(es): Visual básico del sistema de archivos
Name: filesystem
Version: 1.3.4
Release: 6cl
Copyright: Public Domain
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source0: filesystem-1.3.4.tar.gz
Source1: filesystem-conectiva-1.3.4.tar.gz
Buildroot: /var/tmp/%{name}-root
Prereq: setup
BuildArchitectures: noarch

%description
The filesystem package is one of the basic packages that is installed on
a Red Hat Linux system.  Filesystem  contains the basic directory layout
for a Linux operating system, including the correct permissions for the
directories.

%description -l pt_BR
Este pacote contém o layout básico de diretórios para um sistema
Linux, incluindo as permissões adequadas para os diretórios. Esse
layout segue o padrão Linux Filesystem Standard (FSSTND) 1.3.

%description -l es
Este paquete contiene el visual básico de directorios para un sistema
Linux, incluso los permisos adecuados para los directorios. Este
visual sigue el padrón Linux Filesystem Standard (FSSTND) 1.3.

%prep

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
tar xzf %{SOURCE0}
tar xzf %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
/bin
/boot
/etc
/home
/lib
%dir /mnt
%attr(775,root,root) /mnt/floppy
%attr(775,root,root) /mnt/cdrom
%attr(555,root,root) /proc
%attr(750,root,root) /root
/sbin
%attr(1777,root,root) /tmp
/usr
%dir /var
/var/db
/var/lib
/var/local
%dir %attr(775,root,uucp) /var/lock
%attr(775,root,root) /var/lock/subsys
/var/log
/var/nis
/var/preserve
/var/run
%dir /var/spool
%attr(775,root,mail) /var/spool/mail
%attr(1777,root,root) /var/tmp

%changelog
* Tue Jun 29 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- /usr/man/pt_BR/* included into filesystem-conectiva

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- don't carry X11R6.1 as directory on sparc.
- /var/tmp/build root (#811)

* Wed Jan 13 1999 Preston Brown <pbrown@redhat.com>
- font directory didn't belong, which I previously misunderstood.  removed.

* Fri Nov 13 1998 Preston Brown <pbrown@redhat.com>
- /usr/share/fonts/default added.

* Fri Oct  9 1998 Bill Nottingham <notting@redhat.com>
- put /mnt/cdrom back in

* Wed Oct  7 1998 Bill Nottingham <notting@redhat.com>
- Changed /root to 0750

* Wed Aug 05 1998 Erik Troan <ewt@redhat.com>
- added /var/db
- set attributes in the spec file; don't depend on the ones in the cpio
  archive
- use a tarball instead of a cpioball

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Wed Jul 09 1997 Erik Troan <ewt@redhat.com>
- added /

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Changed /proc to 555
- Removed /var/spool/mqueue (which is owned by sendmail)
