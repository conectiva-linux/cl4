Summary: Writes a kickstart description of the current machine.
Summary(pt_BR): Cria um kickstart apartir da máquina em que for rodado
Summary(es): Writes a kickstart description of the current machine.
Name: mkkickstart
%define version 1.2
Version: %{version}
Release: 2cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: mkkickstart-%{version}.tar.gz
Exclusiveos: Linux
Requires: sed fileutils textutils grep
BuildArch: noarch
Buildroot: /var/tmp/mkkickstart-root

%description
The mkkickstart program writes a kickstart description from the host
machine.  The kickstart description can then be used, during a CD-ROM
or NFS installation, to automatically build that machine's
configuration of Conectiva Linux on one or more other machines.

Install mkkickstart if you want to use the kickstart method to
automatically install Conectiva Linux.

%description -l pt_BR
O programa mkkickstart escreve um kickstart apartir da máquina em que
ele foi rodado. Este kickstart pode então ser usado durante uma
instalação via CDROM ou NFS, para criar automaticamente a configuração
desta máquina do Conectiva Linux em uma ou mais máquinas.

Instale o mkkickstart se você deseja utilizar o método "kickstart"
para instalar automaticamente o Conectiva Linux.

%description -l es
The mkkickstart program writes a kickstart description from the host
machine.  The kickstart description can then be used, during a CD-ROM
or NFS installation, to automatically build that machine's
configuration of Red Hat Linux on one or more other machines.

Install mkkickstart if you want to use the kickstart method to
automatically install Red Hat Linux.

%changelog
* Mon Jun 14 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added to Conectiva Linux

* Sun Apr 11 1999 Erik Troan <ewt@redhat.com>
- partition sizes could come out wrong
- dig password out of /etc/shadow
- create auth line

* Sat Mar 27 1999 Erik Troan <ewt@redhat.com>
- small partitions were being set as 0 MB

* Sat Mar 27 1999 Erik Troan <ewt@redhat.com>
- integrated alan's rel 4 fixes

* Thu Feb 25 1999 Matt Wilson <msw@redhat.com>
- updated spec file

* Wed Feb  3 1999 Bill Nottingham <notting@redhat.com>
- make noarch

* Thu Sep 10 1998 Alan Cox <alan@redhat.com>
- Fix nox

* Thu Aug 27 1998 Alan Cox <alan@redhat.com>
- Made the program output files to the correct format, rather than the 
  original (and buggy) specification

%prep
%setup

%install
make BUILDROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) /usr/sbin/mkkickstart
%attr(644,root,root) /usr/man/man8/mkkickstart.8
