Summary: RPC port mapper
Summary(pt_BR): RPC port mapper
Summary(es): RPC port mapper
Name: portmap
Version: 4.0
Release: 17cl
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Copyright: BSD
Source0: ftp://coast.cs.purdue.edu/pub/tools/unix/portmap/portmap_4.tar.gz
Source1: portmap.init
Patch0: portmap-4.0-linux.patch
BuildRoot: /var/tmp/portmap-root
Prereq: chkconfig
Serial: 1

%description
The portmapper manages RPC connections, which are used by protocols
such as NFS and NIS. The portmap server must be running on machines
which act as servers for protocols which make use of the RPC mechanism.
This portmapper supports hosts.{allow,deny} type access control.

%description -l pt_BR
O portmap gerencia conexões RPC, incluindo NFS. Este mapeador de
porta pode usar hosts.{allow,deny} para controlar o acesso.

%description -l es
portmap administra conexiones RPC, que incluye NFS. Este mapeador de
puerto puede usar hosts.{allow,deny} para controlar el acceso.

%prep 
%setup -q -n portmap_4
%patch0 -p1

%build
make FACILITY=LOG_AUTH ZOMBIES='-DIGNORE_SIGCHLD -Dlint' RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d

install -m 755 -s portmap $RPM_BUILD_ROOT/sbin
install -m 755 -s pmap_set $RPM_BUILD_ROOT/usr/sbin
install -m 755 -s pmap_dump $RPM_BUILD_ROOT/usr/sbin
install -m 755 $RPM_SOURCE_DIR/portmap.init $RPM_BUILD_ROOT/etc/rc.d/init.d/portmap

# let chkconfig deal with runlevel 4
for I in 0 1 2 6; do
	mkdir $RPM_BUILD_ROOT/etc/rc.d/rc$I.d
	ln -sf ../init.d/portmap $RPM_BUILD_ROOT/etc/rc.d/rc$I.d/K89portmap
done
for I in 3 5; do
	mkdir $RPM_BUILD_ROOT/etc/rc.d/rc$I.d
	ln -sf ../init.d/portmap $RPM_BUILD_ROOT/etc/rc.d/rc$I.d/S11portmap
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add portmap

%triggerpostun -- portmap <= portmap-4.0-9
/sbin/chkconfig --add portmap

%postun
if [ $1 = 0 ] ; then
  /sbin/chkconfig --del portmap
fi

%files
%defattr(-,root,root)
%doc README CHANGES BLURB

/sbin/portmap
/usr/sbin/pmap_dump
/usr/sbin/pmap_set

%config /etc/rc.d/init.d/portmap
%config(missingok) /etc/rc.d/rc0.d/K89portmap
%config(missingok) /etc/rc.d/rc1.d/K89portmap
%config(missingok) /etc/rc.d/rc2.d/K89portmap
%config(missingok) /etc/rc.d/rc3.d/S11portmap
%config(missingok) /etc/rc.d/rc5.d/S11portmap
%config(missingok) /etc/rc.d/rc6.d/K89portmap

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- fixed prereqs

* Wed Mar 10 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- portmap.init internationalized (gprintf/functions/xgettext_sh)

* Mon Oct 26 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- Serial: 1
- portmap.init translated to pt_BR

* Tue Jul  7 1998 Jeff Johnson <jbj@redhat.com>
- start/stop portmap at levels 11/89

* Mon May 04 1998 Cristian Gafton <gafton@redhat.com>
- fixed the trigger script

* Fri May 01 1998 Jeff Johnson <jbj@redhat.com>
- added triggerpostun

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- added %trigger to fix a previously broken package

* Thu Apr 23 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscripts

* Thu Jan 08 1998 Erik Troan <ewt@redhat.com>
- rebuilt against glibc 2.0.6

* Tue Oct 28 1997 Erik Troan <ewt@redhat.com>
- fixed service name in stop section of init script

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- fixed chkconfig support

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- added restart, status commands to init script
- added chkconfig support
- uses a buildroot and %attr tags

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
