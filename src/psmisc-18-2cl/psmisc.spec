Summary: Utilities for managing processes on your system.
Summary(pt_BR): Mais ferramentas do tipo ps para o sistema de arquivos /proc
Summary(es): Más herramientas de tipo ps para el sistema de archivos /proc
Name: psmisc
Version: 18
Release: 2cl
Copyright: distributable
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/system/status/ps/psmisc-18.tar.gz
Patch: psmisc-17-buildroot.patch
Buildroot: /var/tmp/psmisc-root


%description
The psmisc package contains utilities for managing processes on
your system:  pstree, killall and fuser.  The pstree command displays
a tree structure of all of the running processes on your system.  The
killall command sends a specified signal (SIGTERM if nothing is
specified) to processes identified by name.  The fuser command
identifies the PIDs of processes that are using specified files or
filesystems.

%description -l pt_BR
Este pacote contém programas para mostrar uma árvore de processos,
saber quais usuários têm arquivo aberto e mandar sinais aos processos
por nome.

%description -l es
Este paquete contiene programas para enseñar un árbol de procesos,
saber que usuarios tienen archivo abierto y mandar señales a los
procesos por nombre.

%prep
%setup -q -n psmisc
%patch -p1 -b .br

%build
make 'LDFLAGS=-s'
strip fuser killall pstree

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
make INSTPREFIX="$RPM_BUILD_ROOT" install
mv $RPM_BUILD_ROOT/bin/fuser $RPM_BUILD_ROOT/usr/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/fuser
/usr/bin/killall
/usr/bin/pstree
/usr/man/man1/fuser.1
/usr/man/man1/killall.1
/usr/man/man1/pstree.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Sat Mar 13 1999 Michael Maher <mike@redhat.com>
- updated package

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- renamed the patch file .patch instead of .spec

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to psmisc version 17
- buildrooted

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from version 11 to version 16
- spec file cleanups

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
