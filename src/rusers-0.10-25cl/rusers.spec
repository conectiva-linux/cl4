Summary: Displays the users logged into machines on the local network.
Summary(pt_BR): Mostra a informação do login para máquinas remotas
Summary(es): Enseña la información del login para máquinas remotas
Name: rusers
Version: 0.10
Release: 25cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/netkit-rusers-0.10.tar.gz
Source1: rusersd.init
Source2: rstatd.tar.gz
Source3: rstatd.init
Patch0: netkit-rusers-0.10-misc.patch
Patch1: rusers-0.10-maint.patch
Prereq: chkconfig
Buildroot: /var/tmp/%{name}-root

%description
The rusers program allows users to find out who is logged into
various machines on the local network.  The rusers command produces
output similar to who, but for the specified list of hosts or for
all machines on the local network.

Install rusers if you need to keep track of who is logged into your
local network.

%description -l pt_BR
O cliente e o servidor rusers, incluídos neste pacote, permitem
ver quais usuários estão logados em outras máquinas da rede.

%description -l es
El cliente y el servidor rusers, incluidos en este paquete, permiten
ver cual de los usuarios están "logados" en otras máquinas de la red.

%prep
%setup -q -n netkit-rusers-0.10 -a 2
%patch0 -p1
%patch1 -p1

%build
make
make -C rpc.rstatd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d

make INSTALLROOT=$RPM_BUILD_ROOT install
make INSTALLROOT=$RPM_BUILD_ROOT install -C rpc.rstatd

install -m 755 $RPM_SOURCE_DIR/rusersd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/rusersd
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/rstatd

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#/sbin/chkconfig --add rusersd
#/sbin/chkconfig --add rstatd

%postun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del rusersd
    /sbin/chkconfig --del rstatd
fi

%files
%defattr(-,root,root)
/usr/bin/rup
/usr/bin/rusers
/usr/man/man1/rup.1
/usr/man/man1/rusers.1
/usr/man/man8/rpc.rstatd.8
/usr/man/man8/rpc.rusersd.8
/usr/man/man8/rusersd.8
/usr/sbin/rpc.rstatd
/usr/sbin/rpc.rusersd
%config /etc/rc.d/init.d/rusersd
%config /etc/rc.d/init.d/rstatd

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- i18n initscripts (rstatd)

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed release

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- i18n initscripts

* Tue Apr  6 1999 Jeff Johnson <jbj@redhat.com>
- add rpc.rstatd (#2000)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- added /etc/rc.d/init.d/functions to the init script

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- added init script
- users %attr
- supports chkconfig

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
