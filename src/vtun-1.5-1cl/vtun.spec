%define name vtun
%define version 1.5
%define release 1cl
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
Source: %{name}-%{version}.tgz
Summary: VTun Virtual Tunnel over TCP/IP networks.
Summary(pt_BR): Permite a cria��o de t�neis atrav�s de redes TCP/IP
Summary(es): VTun Virtual Tunnel over TCP/IP networks.

%description
VTun provides the method for creating Virtual Tunnels over TCP/IP networks
and allows to shape, compress, encrypt traffic in that tunnels. 
Supported type of tunnels are: PPP, SLIP and most of other serial protocols
and programs, Ethernet via Linux's EtherTap device.
VTun is easily and highly configurable, it can be used for various network
task like VPN, Mobil IP, Shaped Internet access, IP address saving, etc.
It is completely user space implementation and does not require modification
to any kernel parts. 

%description -l pt_BR
O VTun fornece um m�todo para a cria��o de canais virtuais via redes TCP/IP
e permite encriptar, limitar a banda e comprimir o tr�fego nesses t�neis.
Tipos suportados de t�neis s�o: PPP, SLIP e a maioria dos protocolos seriais e
programas, Ethernet via o device EtherTap do Linux.
VTun � f�cil e altamente configur�vel, ele pode ser usado em v�rias tarefas de
rede como VPN, IP m�vel, acesso limitado a Internet, salvamento de endere�o IP, etc.
� uma implementa��o completamente feita em n�vel de usu�rio e n�o requer
modifica��es no kernel.

%description -l es
VTun provides the method for creating Virtual Tunnels over TCP/IP networks
and allows to shape, compress, encrypt traffic in that tunnels. 
Supported type of tunnels are: PPP, SLIP and most of other serial protocols
and programs, Ethernet via Linux's EtherTap device.
VTun is easily and highly configurable, it can be used for various network
task like VPN, Mobil IP, Shaped Internet access, IP address saving, etc.
It is completely user space implementation and does not require modification
to any kernel parts. 

%prep
%setup -q

%build
./configure --prefix=$RPM_BUILD_ROOT --mandir=$RPM_BUILD_ROOT/usr/man
make

%install
make install

%changelog 

* Sat Jun  5 1999 Marcelo Tosatti <marcelo@conectiva.com>
- update to 1.5

%files
%defattr(755,root,root)
%attr(644,root,root) %doc ChangeLog README README.Shaper vtund.conf 
/sbin/vtund
%attr(600,root,root) /etc/vtund.conf
%attr(644,root,root) /usr/man/man8/vtund.8
%attr(644,root,root) /usr/man/man8/vtun.8
