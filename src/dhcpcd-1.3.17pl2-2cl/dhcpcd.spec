Summary: DHCPC Daemon
Summary(pt_BR): Servidor DHCPC
Summary(es): Servidor DHCPC
Name: dhcpcd
%define	version 1.3.17pl2
Version: %{version}
Release: 2cl
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/dhcpcd-1.3.17-pl2.tar.gz
Patch: dhcpcd-1.3.17-misc.patch
#Patch1: dhcpcd-0.65-glibc.patch
#Patch2: dhcpcd-0.65-buffer.patch
#Patch3: dhcpcd-0.65-align.patch
Patch4: dhcpcd-0.70-rtup.patch
BuildRoot: /var/tmp/%{name}-root

%description
dhcpcd is an implementation of the DHCP  client  specified in
draft-ietf-dhc-dhcp-09  (when  -r option is not speci- fied) and RFC1541
(when -r option is specified).

It gets the host information (IP address, netmask,  broad- cast  address,
etc.) from a DHCP server and configures the network interface of the
machine on which it  is  running.  It also tries to renew the lease time
according to RFC1541 or draft-ietf-dhc-dhcp-09.

%description -l pt_BR
dhcpcd é uma implementação do cliente DHCP especificado em
draft-ietf-dhc-dhcp-09 (quando a opção -r não é especificada) e
RFC1541 (quando a opção -r é especificada).  Ele captura a informação
do host (endereço IP, máscara de rede, endereço de broadcast,
etc.) de um servidor DHCP e configura a interface de rede da máquina
em que está rodando. Ele também tenta renovar o tempo de aluguel
dos endereços de acordo com RFC1541 ou draft-ietf-dhc-dhcp-09.

%description -l es
dhcpcd es una implementación del cliente DHCP especificado en
draft-ietf-dhc-dhcp-09 (cuando la opción -r no está especificada)
y RFC1541 (cuando la opción -r está especificada).  Captura la
información del host (dirección IP, máscara de red, dirección de
broadcast, etc.) de un servidor DHCP y configura la interface de
red de la máquina donde esté ejecutando. También intenta renovar
el tiempo de alquiler de los direcciones de acuerdo con RFC1541
o draft-ietf-dhc-dhcp-09.

%prep
%setup -q -n dhcpcd-1.3.17-pl2
%patch0 -p1 -b .misc
#%patch1 -p1 -b .glibc
#%patch2 -p1 -b .buffer
#%patch3 -p1 -b .align
#%patch4 -p1 -b .rtup 

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin $RPM_BUILD_ROOT/usr/man/man8

install -s -m 755 dhcpcd $RPM_BUILD_ROOT/sbin/dhcpcd
install -m 644 dhcpcd.8 $RPM_BUILD_ROOT/usr/man/man8/dhcpcd.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/sbin/dhcpcd
/usr/man/man8/dhcpcd.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Wed Dec 23 1998 Jeff Johnson <jbj@redhat.com>
- mark default route up.

* Sun Jun  7 1998 Jeff Johnson <jbj@redhat.com>
- Fix packet alignment problems on sparc.
- build root.

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed May  6 1998 Alan Cox
- fixed some potential buffer exploits reported by Chris Evans

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups 

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc, updated to 0.65

* Mon Apr 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed summary line... was a summary for tar.
