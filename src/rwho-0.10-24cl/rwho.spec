Summary: Displays who is logged in to local network machines.
Summary(pt_BR): Mostra a informação do login para todas as máquinas na rede local
Summary(es): Enseña la información del login para todas las máquinas en red local
Name: rwho
Version: 0.10
Release: 24cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/netkit-rwho-0.10.tar.gz
Source1: rwhod.init
Source2: ruptime.tar.gz
Patch0: netkit-rwho-0.10-misc.patch
Patch1: rwho-0.10-maint.patch
Requires: chkconfig
Buildroot: /var/tmp/%{name}-root

%description
The rwho command displays output similar to the output of the who
command (it shows who is logged in) for all machines on the local
network running the rwho daemon.

Install the rwho command if you need to keep track of the users who
are logged in to your local network.

%description -l pt_BR
O programa rwho mostra quais usuários estão logados nas máquinas
da rede local que estejam rodando o servidor rwho. O cliente e o
servidor são fornecidos neste pacote.

%description -l es
El programa rwho enseña cual de los usuarios están logados en las
máquinas de la red local que estén ejecutando el servidor rwho. El
cliente y el servidor se ofrecen en este paquete.

%prep
%setup -q -n netkit-rwho-0.10 -a 2
%patch0 -p1
%patch1 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" -C ruptime

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/var/spool/rwho

make INSTALLROOT=$RPM_BUILD_ROOT install
make INSTALLROOT=$RPM_BUILD_ROOT install -C ruptime

install -m 755 $RPM_SOURCE_DIR/rwhod.init $RPM_BUILD_ROOT/etc/rc.d/init.d/rwhod

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#/sbin/chkconfig --add rwhod

%postun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del rwhod
fi

%files
%defattr(-,root,root)
/usr/bin/ruptime
/usr/man/man1/ruptime.1
/usr/bin/rwho
/usr/man/man1/rwho.1
/usr/sbin/rwhod
/usr/man/man8/rwhod.8
/var/spool/rwho
%config /etc/rc.d/init.d/rwhod

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed release

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- initscripts i18n

* Fri Apr  9 1999 Jeff Johnson <jbj@redhat.com>
- add ruptime (#2023)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscripts

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added /var/spool/rwho

* Fri Oct 31 1997 Donnie Barnes <djb@redhat.com>
- fixed init script

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- added an init script
- uses chkconfig
- uses %attr tags

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
