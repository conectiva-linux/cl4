Summary: Utilities for the ncpfs filesystem, a NetWare client for Linux.
Summary(pt_BR): Utilitários de suporte para ncpfs, que é o cliente Linux free para netware
Summary(es): Utilitarios de soporte para ncpfs, que es el cliente Linux free para netware
Name: ncpfs
Version: 2.2.0.12
Release: 6cl
Copyright:  GPL
Source: ftp://ftp.platan.vc.cvut.cz/pub/linux/ncpfs/ncpfs-%{version}/ncpfs-%{version}.tgz
Source1: mount.ncp
Source700: ncpfs-man-pt_BR.tar
Patch: ncpfs-paths.patch
Patch1: ncpfs-2.2.0.11-glibc21.patch
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Requires: ipxutils
ExcludeArch: alpha
Buildroot: /var/tmp/ncpfs-root

%description
Ncpfs is a filesystem which understands the Novell NetWare(TM)
NCP protocol.  Functionally, NCP is used for NetWare the way NFS
is used in the TCP/IP world.  For a Linux system to mount a NetWare
filesystem, it needs a special mount program.  The ncpfs package
contains such a mount program plus other tools for configuring and
using the ncpfs filesystem.

Install the ncpfs package if you need to use the ncpfs filesystem
to use Novell NetWare files or services.

%description -l pt_BR
Este pacote contém ferramentas para ajudar a configurar e usar o
sistema de arquivos ncpfs, que é um sistema de arquivos Linux que
entende o protocolo NCP. Esse é o protocolo que os clientes Novell
NetWare usam para "conversar" com servidores NetWare.

%description -l es
Este paquete contiene herramientas para ayudar a configurar y usar
el sistema de archivos ncpfs, que es un sistema de archivos Linux
capaz de entender el protocolo NCP. Este es el protocolo que los
clientes Novell NetWare usan para "conversar" con servidores NetWare.

%package -n ipxutils
Summary: Tools for configuring and debugging IPX interfaces and networks.
Summary(pt_BR): Utilitários para configuração IPX
Summary(es): Utilitarios para configuración IPX
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema

%description -n ipxutils
The ipxutils package includes utilities (ipx_configure, ipx_internal_net,
ipx_interface, ipx_route) necessary for configuring and debugging IPX
interfaces and networks under Linux. IPX is the low-level protocol used
by Novell's NetWare file server system to transfer data.

Install ipxutils if you need to configure IPX networking on your network.

%description -l pt_BR -n ipxutils
Este pacote inclui os utilitários necessários à configuração e
depuração de interfaces e redes IPX no Linux. IPX é o protocolo de
baixo nível usado pelo NetWare para transferir dados.

%description -l es -n ipxutils
Este paquete incluye los utilitarios necesarios a  configuración y
depuración de interfaces y redes IPX en Linux. IPX es el protocolo
de bajo nivel usado por el NetWare para transferir datos.

%prep
%setup -q
%patch0 -p1 -b .paths
%patch1 -p1 -b .glibc21

%build
make
make -C ipxdump

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Move ipx_configure/ipx_internal_net to permit /usr from NFS
for i in ipx_configure ipx_internal_net
do
	mv $RPM_BUILD_ROOT/usr/bin/$i $RPM_BUILD_ROOT/sbin/$i
done

ln -sf libncp.so.2.2.0 $RPM_BUILD_ROOT/lib/libncp.so
install -m755 ipxdump/ipxdump ipxdump/ipxparse $RPM_BUILD_ROOT/usr/bin/
strip $RPM_BUILD_ROOT/sbin/* $RPM_BUILD_ROOT/usr/bin/* || :

# these could be SUID root, but it's a security hole
chmod 755 $RPM_BUILD_ROOT/usr/bin/ncpmount $RPM_BUILD_ROOT/usr/bin/ncpumount 
mkdir -p $RPM_BUILD_ROOT/sbin
install -m755 $RPM_SOURCE_DIR/mount.ncp $RPM_BUILD_ROOT/sbin
ln -s mount.ncp $RPM_BUILD_ROOT/sbin/mount.ncpfs

# file list
find $RPM_BUILD_ROOT -type f -or -type l | \
	grep -v ipx | grep -v mount.ncp.8| \
	sed -e "s|$RPM_BUILD_ROOT||g" | \
	sed -e "s|/usr/bin/nwsfind|%attr(0755,root,root) /usr/bin/nwsfind|g" > rpm.files




mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/ncpfs-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
rm -f rpm.files

%files -f rpm.files
%defattr(-,root,root)
%doc BUGS COPYING Changes FAQ README 
%doc ipxdump/README

%files -n ipxutils
%defattr(-,root,root)
%doc ipx-1.0/COPYING ipx-1.0/README
/sbin/ipx_configure
/sbin/ipx_internal_net
/usr/bin/ipx*
/usr/man/man8/ipx*
%attr(0644,root,root) /usr/man/pt_BR/man8/*

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr  6 1999 Bill Nottingham <notting@redhat.com>
- turn off setuid on nwsfind
- move ipxutils to using ncpfs versioning for sanity reasons

* Fri Mar 26 1999 Bill Nottingham <notting@redhat.com>
- doesn't work on alpha, apparently
- add a mount.ncp mount helper

* Mon Mar 22 1999 Bill Nottingham <notting@redhat.com>
- remove dangling symlink

* Tue Feb 23 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.0.12

* Fri Jan 22 1999 Bill Nottingham <notting@redhat.com>
- build for arm. Yuk.

* Wed Dec  9 1998 Bill Nottingham <notting@redhat.com>
- update to 2.2.0.11

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.2.0.

* Fri Jul 10 1998 Jeff Johnson <jbj@redhat.com>
- exclusively i386 for now.

* Tue Jul  7 1998 Jeff Johnson <jbj@redhat.com>
- move ipx_configure/ipx_internal_net to /sbin to permit /usr from NFS.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Apr 13 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild
- there is a new version out, 2.0.12, but it contains RSA crypto code, so
  it's of no use for us. :-(
- buildroot and spec file cleanup

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- uid_t, gid_t, mode_t fixes for glibc 2.0.5 and linux 2.0.x

* Wed Oct 23 1997 Michael Fulbright <msf@redhat.com>
- added a few file which were missing from the file list

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to 2.0.11
- massive hacking for glibc

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- nwrights program now included in package.
