Summary: Bootp and dhcp client for automatic IP configuration
Summary(pt_BR): Cliente para dhcp e bootp para configuração automática de IP
Summary(es): Bootp and dhcp client for automatic IP configuration
%define version 0.6.7
Name: pump
Version: %{version}
Release: 1cl
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Copyright: MIT
BuildRoot: /var/tmp/pump-root
Source: pump-%{version}.tar.gz
Obsoletes: bootpc
Requires: initscripts >= 3.92

%description
DHCP (Dynamic Host Configuration Protocol) and BOOTP (Boot Protocol)
are protocols which allow individual devices on an IP network to get
their own network configuration information (IP address, subnetmask,
broadcast address, etc.) from network servers.  The overall purpose of
DHCP and BOOTP is to make it easier to administer a large network.

Pump is a combined BOOTP and DHCP client daemon, which allows your machine
to retrieve configuration information from a server.  You should install
this package if you are on a network which uses BOOTP or DHCP.

%description -l pt_BR
O pump é um cliente DHCP e BOOTP, que permite que sua máquina busque
informações de configuração de um servidor.

Instale este pacote se você deseja utilizar BOOTP ou DHCP.

%description -l es
DHCP (Dynamic Host Configuration Protocol) and BOOTP (Boot Protocol)
are protocols which allow individual devices on an IP network to get
their own network configuration information (IP address, subnetmask,
broadcast address, etc.) from network servers.  The overall purpose of
DHCP and BOOTP is to make it easier to administer a large network.

Pump is a combined BOOTP and DHCP client daemon, which allows your machine
to retrieve configuration information from a server.  You should install
this package if you are on a network which uses BOOTP or DHCP.

%prep
%setup -q

%build
make

%install
make RPM_BUILD_ROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
/sbin/pump
/usr/man/man8/pump.8

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added to Conectiva Linux

* Thu May 06 1999 Erik Troan <ewt@redhat.com>
- set option list so we'll work with NT
- tried to add a -h option, but I have no way of testing it :-(

* Wed Apr 28 1999 Erik Troan <ewt@redhat.com>
- closing fd 1 is important

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- don't obsolete dhcpcd

* Tue Apr 06 1999 Erik Troan <ewt@redhat.com>
- retry code didn't handle failure terribly gracefully

* Tue Mar 30 1999 Erik Troan <ewt@redhat.com>
- added --lookup-hostname
- generate a DNS search path based on full domain set
- use raw socket for revieving reply; this lets us work properly on 2.2
  kernels when we recieve unicast replies from the bootp server

* Mon Mar 22 1999 Erik Troan <ewt@redhat.com>
- it was always requesting a 20 second lease

* Mon Mar 22 1999 Michael K. Johnson <johnsonm@redhat.com>
- added minimal man page /usr/man/man8/pump.8
