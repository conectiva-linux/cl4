Summary: bootp/DHCP server and test programs
Summary(pt_BR): Servidor bootp/DHCP e programas de teste
Summary(es): Servidor bootp/DHCP y programas de prueba
Name: bootp
Version: 2.4.3
Release: 13cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
#Source: ftp://ftp.mc.com/pub/bootp-2.4.3.tar.Z
Source: ftp://ftp.mc.com/pub/bootp-2.4.3.tar.bz2
Patch: bootp-2.4.3-linux.patch
Patch1: http://www.sghms.ac.uk/~mpreston/tools.htm/dhcp.patch
Patch2: bootp-2.4.3-glibc.patch
Patch3: bootp-2.4.3-pathfix.patch
Patch4: bootp-2.4.3-miscsecure.patch
Buildroot: /var/tmp/bootp-root
Requires: inetd
Summary(de): bootp/DHCP-Server und Testprogramme
Summary(fr): Serveur bootp/DHCP et programmes test
Summary(tr): bootp/DHCP sunucusu ve test programlarý

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun 16 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Feb 19 1999 Marcelo Tosatti <marcelo@conectiva.com>
- removed my patch from OpenBSD and added a more complete version from
  Chris Evans

* Fri Dec 04 1998 Marcelo Tosatti <marcelo@conectiva.com>
- added patch from OpenBSD to stop possible remote code execution

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed May 13 1998 Alan Cox <alan@redhat.com>
- Fixed a potential problem with the bootfile buffer being non terminated
  allowing a theoretical exploit. We now check the buffer as we walk it. Bug
  noted and reported by Chris Evans.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- minor spec file cleanups
- now uses a build root and %attr
- requires inetd server

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%description
This is a server for the bootp protocol; which allows network
administrators to setup networking information for clients via an
/etc/bootptab on a server so that the clients can automatically get
their networking information. While this server includes rudimentary
DHCP support as well, we suggest using the dhcpd package if you need
DHCP support, as it is much more complete.

%description -l pt_BR
Este servidor pode atender tanto requisições bootp quanto DHCP. Ele
é projetado para o administrador da rede configurar informações para
clientes via um /etc/bootptab em um servidor. Assim, os clientes
podem pegar automaticamente as suas informações de rede.

%description -l es
Este servidor puede atender tanto requisiciones bootp como DHCP. Está
proyectado para que el administrador de red configure información
para clientes vía un /etc/bootptab en un servidor. Así, los clientes
pueden coger automáticamente información de la red.

%description -l de
Dies ist ein Server für das bootp-Protokoll, der Netzwerkadministratoren
das Einrichten von Netzinfos für Clients über ein /etc/bootptab auf einem
Server gestattet, so daß die Clients ihre Infos automatisch bekommen. 
Obwohl dieser Server rudimentären DHCP-Support beinhaltet, 
empfehlen wir den Einsatz des dhcpd-Pakets, wenn Sie DHCP-Unterstützung
wünschen, weil sie damit umfassenderen Support erhalten.

%description -l fr
C'est un serveur pour le protocole bootp, qui permet aux administrateurs
réseau de configurer les informations pour les clients réseau via
le fichier /etc/bootptab sur un serveur de telle manière que les clients
puissent automatiquement obtenir les informations. Bien que le serveur
comprenne aussi un support rudimentaire pour dhcp, nous recommandons
d'utiliser le package dhcp si vous désirez un support dhcp, car
il est beaucoup plus complet.

%description -l tr
bootp sunucusu, istemcilerin að bilgilerini sunucu üzerindeki bir dosyadan
almalarýna olanak verir. Bu sunucu temel DHCP desteðini içermekle birlikte,
DHCP desteðine gerek duyulan durumlarda dhcpd paketinin kullanýmý önerilir

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make linux

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) /usr/man/man5/bootptab.5
%attr(-,root,root) /usr/man/man8/bootpd.8
%attr(-,root,root) /usr/man/man8/bootpef.8
%attr(-,root,root) /usr/man/man8/bootptest.8
%attr(-,root,root) /usr/sbin/bootpd
%attr(-,root,root) /usr/sbin/bootpef
%attr(-,root,root) /usr/sbin/bootpgw
%attr(-,root,root) /usr/sbin/bootptest
