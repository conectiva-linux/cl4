Summary: The routing daemon which maintains routing tables.
Summary(pt_BR): Servidor RIP para manutenção automática de tabela de rotas
Summary(es): Servidor RIP para manutención automática de tabla de rutas
Name: routed
Version: 0.10
Release: 16cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/netkit-routed-0.10.tar.gz
Source1: routed.init
Patch: netkit-routed-0.10-misc.patch
Patch1: netkit-routed-0.10-trace.patch
Patch2: netkit-routed-0.10-ifreq.patch
Patch3: netkit-routed-0.10-compat21.patch
Prereq: /sbin/chkconfig
Buildroot: /var/tmp/%{name}-root

%description
The routed routing daemon handles incoming RIP traffic and broadcasts
outgoing RIP traffic about network traffic routes, in order to maintain
current routing tables.  These routing tables are essential for a
networked computer, so that it knows where packets need to be sent.

The routed package should be installed on any networked machine.

%description -l pt_BR
Vários protocolos estão disponíveis para atualização automática
de tabelas de roteamento TCP/IP. O RIP é o mais simples destes, e
este pacote inclui um servidor que transmite e recebe notificações
de roteamento neste protocolo.

%description -l es
Varios protocolos están disponibles para actualización`` automática
de tablas de rutado TCP/IP. RIP es el más sencillo de estos, y este
paquete incluye un servidor que transmite y recibe notificaciones
de rutado en este protocolo.

%prep
%setup -q -n netkit-routed-0.10
%patch0 -p1 -b .misc
%patch1 -p1 -b .trace
%ifarch alpha
%patch2 -p1 -b .ifreq
%endif
%patch3 -p1 -b .compat21

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
make INSTALLROOT=$RPM_BUILD_ROOT install
install -m 755 $RPM_SOURCE_DIR/routed.init $RPM_BUILD_ROOT/etc/rc.d/init.d/routed

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#/sbin/chkconfig --add routed

%postun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del routed
fi

%files
%defattr(-,root,root)
/usr/sbin/routed
/usr/man/man8/routed.8
/etc/rc.d/init.d/routed

%changelog
* Thu Jul 01 1999 Conectiva <dist@conectiva.com.br>
- i18n initscripts

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 14)

* Tue Feb  9 1999 Jeff Johnson <jbj@redhat.com>
- check for /etc/sysconfig/routed before sourcing.

* Tue Dec 22 1998 Jeff Johnson <jbj@redhat.com>
- use stderr if no trace file specified (#423).
- use FD_ISSET not fds_bits (glibc-2.1).

* Tue Jun 16 1998 Jeff Johnson <jbj@redhat.com>
- add offset to get aligned ifreq's on alpha. This should be
  fixed in the kernel eventually.

* Tue May 19 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Sun May 10 1998 Alan Cox <alan@redhat.com>
- Fixed the trace bug. Traces must now go into /var/log/routed/*

* Mon May 04 1998 Michael K. Johnson <johnsonm@redhat.com>
- Added /etc/sysconfig/routed parsing to init script

* Sat May 02 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscripts

* Tue Oct 28 1997 Erik Troan <ewt@redhat.com>
- fixed init script (wasn't including function library)

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- added init script, chkconfig support

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
