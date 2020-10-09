Summary: dumps packets that are sent or received over a network interface
Summary(pt_BR): Mostra os pacotes que s�o enviados ou recebidos atrav�s de uma interface de rede
Summary(es): Ense�a los paquetes que son enviados o recibidos a trav�s de una interface de red
Name: tcpdump
Version: 3.4
%define	tcpdump_dir	tcpdump-3.4
Release: 10cl
# XXX serial number is necessary to obsolete tcpdump-3.4a5
Serial: 1
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
#Source0: ftp://ftp.ee.lbl.gov/tcpdump-3.4.tar.Z
#Source1: ftp://ftp.ee.lbl.gov/libpcap-0.4.tar.Z
#Source2: ftp://ftp.ee.lbl.gov/arpwatch-2.1a4.tar.Z
# recompressed with bzip2
Source0: ftp://ftp.ee.lbl.gov/tcpdump-3.4.tar.bz2
Source1: ftp://ftp.ee.lbl.gov/libpcap-0.4.tar.bz2
Source2: ftp://ftp.ee.lbl.gov/arpwatch-2.1a4.tar.bz2
Source3: arpwatch.init
Patch0: tcpdump-3.4a5-man.patch
Patch1: tcpdump-3.4a5-sack.patch
Buildroot: /var/tmp/tcpdump-root
Summary(de): deponiert Pakete, die �ber eine Netzwerkschnittstelle gesandt oder empfangen werden  
Summary(fr): vide les paquets �mis ou re�us sur une interface r�seau
Summary(tr): Bir a� arabirimi �zerinden gelen ya da giden paketleri listeler

%description
Tcpdump prints out the headers of packets on a network interface.  It
is very useful for debugging network problems and security operations.

%description -l pt_BR
Tcpdump imprime os cabe�alhos dos pacotes em uma interface de rede. Ele
� muito pr�tico para resolver problemas na rede e para opera��es
de seguran�a.

%description -l es
Tcpdump imprime los encabezamientos de los paquetes en una interface
de red. Es muy pr�ctico para solucionar problemas en la red y para
operaciones de seguridad.

%description -l de
Tcpdump druckt die Headers von Paketen auf einer Netzschnittstelle. 
Es ist �beraus n�tzlich zum Debuggen von Netzwerkproblemen und von
Sicherheitsoperationen.

%description -l fr
tcpdump affiche les en-t�tes des paquets d'une interface r�seau. Il est
tr�s utile pour d�tecter les probl�mes de r�seau et de s�curit�.

%description -l tr
Tcpdump, bir a� arabirimi �zerinden ge�en paketlerin ba�l�klar�n� d�ker.
G�venlik i�lemleri ve a� problemlerinin irdelenmesi konular�nda son derece
yararl�d�r.

%package -n libpcap
Version: 0.4
%define	libpcap_dir	libpcap-0.4
Summary: Libpcap provides promiscuous mode access to network interfaces.
Summary(pt_BR): A libpcap fornece acesso ao modo prom�scuo em interfaces de rede.
Summary(es): libpcap ofrece acceso a modo promiscuo en interfaces de red.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description -n libpcap
Libpcap is a system-independent interface for user-level packet capture.
Libpcap provides a portable framework for low-level network monitoring.
Applications include network statistics collection, security monitoring,
network debugging, etc. Libpcap has system-independent API that is used
by several applications, including tcpdump and arpwatch.

%description -l pt_BR -n libpcap
A libpcap � uma interface independente de sistema para captura de pacotes
em modo usu�rio. Fornece um esquema port�til para monitora��o da rede
em baixo n�vel. � utilizada para coleta de estat�sticas de rede,
monitoramento de seguran�a, depura��o da rede, etc. Tem uma API independente
de sistema que � usada por v�rias aplica��es, entre elas tcpdump e arpwatch.

%description -l es -n libpcap
libpcap es una interface independiente de sistema para captura de
paquetes en modo usuario. Ofrece un esquema port�til para el control
de la red en bajo nivel. Se utiliza para colecta de estad�sticas de
red, Control de seguridad, depuraci�n de la red, etc. Tiene una
API independiente de sistema que se usa por varias aplicaciones,
entre ellas tcpdump y arpwatch.

%package -n arpwatch
Version: 2.1a4
%define	arpwatch_dir	arpwatch-2.1a4
Summary: Arpwatch monitors changes in ethernet/ip address pairings.
Summary(pt_BR): O arpwatch monitora mudan�as em pares de endere�os ethernet/ip.
Summary(es): El arpwatch monitora cambios en pares de direcciones ethernet/ip.
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema

%description -n arpwatch
Arpwatch and arpsnmp are tools that monitors ethernet or fddi activity and
maintain a database of ethernet/ip address pairings.

%description -l pt_BR -n arpwatch
O arpwatch e o arpsnmp s�o ferramentas que monitoram atividade ethernet e
fddi e mant�m um banco de dados de pares de endere�os ethernet/ip.

%description -l es -n arpwatch
arpwatch y arpsnmp son herramientas que controlan actividad ethernet
y fddi, y mantiene un banco de datos de pares de direcciones
ethernet/ip.

%prep
%setup -q -c -a 1 -a 2

cd %tcpdump_dir
%patch0 -p2
%patch1 -p2
cd ..

%build
cd %libpcap_dir
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make
cd ..

cd %tcpdump_dir
CFLAGS="$RPM_OPT_FLAGS -DIP_MAX_MEMBERSHIPS=20" ./configure --prefix=/usr
make
cd ..

cd %arpwatch_dir
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make ARPDIR=/var/arpwatch
cd ..

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{include/pcap/net,lib,man/man3,man/man8,sbin}

cd %libpcap_dir
make DESTDIR=$RPM_BUILD_ROOT INCLDEST=/usr/include/pcap install install-incl install-man
cd ..

cd %tcpdump_dir
install -m755 -s tcpdump $RPM_BUILD_ROOT/usr/sbin
install -m644 tcpdump.1 $RPM_BUILD_ROOT/usr/man/man8/tcpdump.8
cd ..

cd %arpwatch_dir
make DESTDIR=$RPM_BUILD_ROOT install install-man
mkdir -p $RPM_BUILD_ROOT/var/arpwatch
for n in arp2ethers massagevendor; do
	install -m755 $n $RPM_BUILD_ROOT/var/arpwatch
done
for n in *.awk *.dat; do
	install -m644 $n $RPM_BUILD_ROOT/var/arpwatch
done
( cd $RPM_BUILD_ROOT
  mkdir -p ./etc/rc.d/init.d
  install -m755 $RPM_SOURCE_DIR/arpwatch.init ./etc/rc.d/init.d/arpwatch
)
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc	%tcpdump_dir/README %tcpdump_dir/CHANGES
/usr/sbin/tcpdump
/usr/man/man8/tcpdump.8

%files -n libpcap
%defattr(-,root,root)
%doc	%libpcap_dir/README %libpcap_dir/CHANGES
/usr/include/pcap
/usr/lib/libpcap.a
/usr/man/man3/pcap.3

%files -n arpwatch
%doc	%arpwatch_dir/README %arpwatch_dir/CHANGES
/usr/sbin/arpwatch
#/usr/sbin/arpsnmp
/usr/man/man8/arpwatch.8
#/usr/man/man8/arpsnmp.8
/etc/rc.d/init.d/arpwatch
%dir	/var/arpwatch
%config	/var/arpwatch/arp.dat
%config	/var/arpwatch/ethercodes.dat
/var/arpwatch/*.awk
/var/arpwatch/arp2ethers
/var/arpwatch/massagevendor

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 12 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Sep 29 1998 Jeff Johnson <jbj@redhat.com>
- libpcap description typo.

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- fix arpwatch summary line.

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- enable arpwatch

* Mon Aug  3 1998 Jeff Johnson <jbj@redhat.com>
- separate package for libpcap.
- update tcpdump to 3.4, libpcap to 0.4.
- added arpwatch (but disabled for now)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May  2 1998 Alan Cox <alan@rehat.com>
- Added the SACK printing fix so you can dump Linux 2.1+.

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- updated to release 3.4a5
- uses a buildroot and %attr 

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
