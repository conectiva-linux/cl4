Summary: A server process which provides boot information to diskless clients.
Summary(pt_BR): Servidor de rcp que fornece informação de boot a clientes sem disco 
Summary(es): Servidor de rcp que ofrece información de boot a clientes sin disco 
Name: bootparamd
Version: 0.10
Release: 14cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: bootparamd-0.10.tar.gz
Patch: bootparamd.acme.patch
Prereq: chkconfig
Requires: portmap
BuildRoot: /var/tmp/%{name}-root

%description
The bootparamd process provides bootparamd, a server process which
provides the information needed by diskless clients in order for them
to successfully boot.  Bootparamd looks first in /etc/bootparams for an
entry for that particular client; if a local bootparams file doesn't
exist, it looks at the appropriate Network Information Service (NIS)
map.  Some network boot loaders (notably Sun's) rely on special boot
server code on the server, in addition to the rarp and tftp servers.
This bootparamd server process is compatible with SunOS bootparam clients
and servers which need that boot server code.

You should install bootparamd if you need to provide boot information to
diskless clients on your network.

%description -l pt_BR
Alguns carregadores de boot de rede (notavelmente Sun) contam com
um código especial de servidor de boot, além de rarp e servidores
tftp. Este servidor é compatível com os clientes e servidores
bootparam do SunOS.

%description -l es
Algunos cargadores de boot de red (notablemente Sun) cuetan con un
código especial de servidor de boot, además de rarp y servidores
tftp. Este servidor es compatible con los clientes y servidores
bootparam del SunOS.

%prep
%setup -q -n bootparamd
%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
make INSTALLROOT=$RPM_BUILD_ROOT install
install -m 755 bootparamd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/bootparamd

%clean
rm -rf $RPM_BUILD_ROOT

%post
#/sbin/chkconfig --add bootparamd

%postun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del bootparamd
fi

%files
%defattr(-,root,root)
/usr/sbin/rpc.bootparamd
/usr/bin/callbootd
/usr/man/man8/rpc.bootparamd.8
/usr/man/man8/bootparamd.8
%config /etc/rc.d/init.d/bootparamd

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed prereq

* Fri Mar 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscripts i18n
- added Group, Summary and %description translations

* Mon Feb  8 1999 Jeff Johnson <jbj@redhat.com>
- port OpenBSD version.

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- rebuild for Raw Hide.

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- removed triggerpostun.

* Fri May 01 1998 Jeff Johnson <jbj@redhat.com>
- added triggerpostun

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscript

* Thu Jan 08 1998 Erik Troan <ewt@redhat.com>
- updated initscript to include functions
- fixed 'stop' action of initscript
- added requirement for portmap

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- added an initscript

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
