Summary: Client and daemon for the trivial file transfer protocol (tftp)
Summary(pt_BR): Cliente e servidor para o protocolo ftp trivial (tftp)
Summary(es): Cliente y servidor para el protocolo ftp trivial (tftp)
Name: tftp
Version: 0.10
Release: 8cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: http://metalab.unc.edu/pub/Linux/system/network/file-transfer/netkit-tftp-0.10.tar.gz
Patch: netkit-tftp-0.10-misc.patch
Patch1: netkit-tftp-0.10-security.patch
Requires: inetd
BuildRoot: /var/tmp/tftp-root
Summary(de): Client und Dämon für das 'trivial file transfer protocol (tftp)'
Summary(fr): Client et démon pour le « trivial file transfer protocol » (tftp)
Summary(tr): Ýlkel dosya aktarým protokolu (TFTP) için sunucu ve istemci

%description
The trivial file transfer protocol (tftp) is normally used only for 
booting diskless workstations. It provides very little security, and
should not be enabled unless it is needed. The tftp server is run from
/etc/inetd.conf, and is disabled by default on Red Hat systems.

%description -l pt_BR
O protocolo trivial de transferência de arquivos (tftp) é normalmente
usado apenas em estações de trabalho sem disquete de inicialização. Ele
proporciona pouca segurança e não deve ser habilitado a menos
que seja necessário. O servidor tftp é executado através do inetd
(etc/inetd.conf), e é desabilitado por default no sistema Conectiva.

%description -l es
El protocolo trivial de transferencia de archivos (tftp)
normalmente se usa sólo en estaciones de trabajo sin disquete de
arranque. Proporciona poca seguridad y no debe ser habilitado a
menos que sea necesario. El servidor tftp se ejecuta a través del
inetd (etc/inetd.conf), y se inhabilita por defecto en el sistema
Conectiva.

%description -l de
Das trivial file transfer protocol (tftp) wird in der Regel nur zum 
Booten von disklosen Workstations benutzt. Es bietet nur geringe 
Sicherheit und sollte nur im Bedarfsfall aktiviert werden. 
Der tftp-Server wird von /etc/inetd.conf aus betrieben 
und ist auf Red-Hat-Systemen standardmäßig ausgeschaltet. 

%description -l fr
Le « trivial file transfer protocol » (tftp) est normalement utilisé
uniquement pour démarrer les stations de travail sans disque. Il offre
très peu de sécurité et ne devrait pas être activé sauf si c'est
nécessaire. Le serveur tftp est lancé à partir de /etc/inetd.conf et
désactivé par défaut sur les systèmes Red Hat. 

%description -l tr
Ýlkel dosya aktarým protokolu genelde disksiz iþ istasyonlarýnýn að üzerinden
açýlmalarýnda kullanýlýr. Güvenlik denetimleri çok az olduðundan zorunlu
kalmadýkça çalýþtýrýlmamalýdýr.

%prep
%setup -q -n netkit-tftp-0.10
%patch -p1 -b .misc
%patch1 -p1 -b .security

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,sbin,man/man1,man/man8}

make INSTALLROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/tftp
/usr/man/man1/tftp.1
/usr/sbin/in.tftpd
/usr/man/man8/in.tftpd.8
/usr/man/man8/tftpd.8

%changelog
* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added check for getpwnam() failure

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
