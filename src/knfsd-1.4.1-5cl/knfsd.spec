Name: knfsd
Version: 1.4.1
Release: 5cl
Summary: Kernel NFS server.
Summary(pt_BR): Servidor NFS para o Linux
Summary(es): Kernel NFS server.
# Source0: ftp://ftp.kernel.org/pub/linux/devel/gcc/knfsd-%{version}.tar.gz
# Repacked with bzip2
Source0: ftp://ftp.kernel.org/pub/linux/devel/gcc/knfsd-%{version}.tar.bz2
Source1: knfsd.init
Source2: exports.5
Requires: kernel , portmap
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Obsoletes: nfs-server
Provides: nfs-server
Copyright: GPL
Buildroot: /var/tmp/knfsd-root
ExcludeArch: armv4l

%description
This is the *new* kernel NFS server and related tools.  It provides a much
higher level of performance than the traditional Linux user-land NFS server.

%description -l pt_BR
Este é o novo servidor NFS "kernel level" e ferramentas de trabalho. Ele
provê uma performance muito superior que o servidor NFS "user level" que
o Linux utilizava anteriormente.

%description -l es
This is the *new* kernel NFS server and related tools.  It provides a much
higher level of performance than the traditional Linux user-land NFS server.

%package clients
Obsoletes: nfs-server-clients
Provides: nfs-server-clients
Summary: Clients for connecting to a remote NFS server.
Summary(pt_BR): Clientes para conexão à um servidor NFS remoto
Summary(es): Clients for connecting to a remote NFS server.
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema

%description clients
The nfs-server-clients package contains the showmount program.
Showmount queries the mount daemon on a remote host for information
about the NFS (Network File System) server on the remote host.  For
example, showmount can display the clients which are mounted on that
host.  This package is not needed to mount NFS volumes.

Install nfs-server-clients if you'd like to use the showmount tool
for querying NFS servers.

%description -l pt_BR clients
Este pacote contém o programa showmount. O showmount consulta o
servidor "mount" em uma máquina remota para pegar informações
sobre o servidor NFS.

%description -l es clients
The nfs-server-clients package contains the showmount program.
Showmount queries the mount daemon on a remote host for information
about the NFS (Network File System) server on the remote host.  For
example, showmount can display the clients which are mounted on that
host.  This package is not needed to mount NFS volumes.

Install nfs-server-clients if you'd like to use the showmount tool
for querying NFS servers.

%prep
%setup -q

%build
./configure --prefix=$RPM_BUILD_ROOT --sbindir=$RPM_BUILD_ROOT/usr/sbin/ \
	--mandir=$RPM_BUILD_ROOT/usr/man/
	
make all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{/sbin,/usr/{sbin,man/man8}}
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/var/lib/nfs/
make install prefix=$RPM_BUILD_ROOT
install -m 755 tools/rpcdebug/rpcdebug $RPM_BUILD_ROOT/sbin
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfs
touch $RPM_BUILD_ROOT/var/lib/nfs/rmtab
touch $RPM_BUILD_ROOT/var/lib/nfs/xtab
mkdir -p $RPM_BUILD_ROOT/usr/man/man5
install -m 644 $RPM_SOURCE_DIR/exports.5 $RPM_BUILD_ROOT/usr/man/man5/exports.5

## fix up all file names
#cd $RPM_BUILD_ROOT/usr/sbin
#mv -f kexportfs exportfs
#mv -f rpc.kmountd rpc.mountd
#mv -f rpc.knfsd rpc.nfsd
#mv -f rpc.kstatd rpc.statd
#mv -f knfsstat nfsstat
#mv -f rpc.krquotad rpc.rquotad
#mv -f knhfsstone nhfsstone
#mv -f kshowmount showmount

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#/sbin/chkconfig --add nfs

%preun
if [ "$1" = "0" ]; then
    /sbin/chkconfig --del nfs
fi

%files
%defattr(-,root,root)
/sbin/rpcdebug
/usr/sbin/exportfs
/usr/sbin/rpc.mountd
/usr/sbin/rpc.nfsd
/usr/sbin/rpc.statd
/usr/sbin/nfsstat
/usr/sbin/rpc.rquotad
/usr/sbin/nhfsstone
/usr/man/man8/exportfs.8
/usr/man/man8/nfsstat.8
/usr/man/man8/rquotad.8
%config /etc/rc.d/init.d/nfs
/var/lib/nfs/xtab
/var/lib/nfs/rmtab
%dir /var/lib/nfs
/usr/man/man5/exports.5

%files clients
/usr/sbin/showmount
/usr/man/man8/showmount.8

%changelog
* Sun Jun 27 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fixes i18n stuff of knfsd.init

* Sun Jun 27 1999 Marcelo Tosatti <marcelo@conectiva.com>
- updated knfsd from 1.3.3b to 1.4.1

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Mon Jun 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Updated to version 1.3.3b

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- make the init script deal more gracefully with the restart) part

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- block devices check for the RAID systems (patch from John Ireland
  <jireland@jesus.ox.ac.uk>)
- version 1.2.2
- start more nfsd daemons by default to improve performance

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- the main package shouldn't obsolete the nfs-server-clients package. fixed.

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- explicitly require portmap (bug #1902)

* Mon Mar 29 1999 Michael Johnson <johnsonm@redhat.com>
- fixed init script probe function to not respond "restart" all the time

* Mon Mar 29 1999 Preston Brown <pbrown@redhat.com>
- fixed exports man page

* Fri Mar 26 1999 Bill Nottingham <notting@redhat.com>
- rewrite initscript so we don't have 6 [OK|FAILED] on the same line. :)

* Wed Mar 24 1999 Erik Troan <ewt@redhat.com>
- added exports.5 man page from old user space nfs server

* Tue Mar 23 1999 Cristian Gafton <gafton@redhat.com>
- version 1.2
- auto rebuild in the new build environment (release 4)

* Mon Feb 08 1999 Matt Wilson <msw@redhat.com>
- fixed typo in initscripts

* Wed Feb 03 1999 Cristian Gafton <gafton@redhat.com>
- put showmount in the knfsd-clients

* Mon Dec 28 1998 Cristian Gafton <gafton@redhat.com>
- added %post and %preun scripts
- build as a separate package
- buildroot
