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
Summary(de): Client und D�mon f�r das 'trivial file transfer protocol (tftp)'
Summary(fr): Client et d�mon pour le � trivial file transfer protocol � (tftp)
Summary(tr): �lkel dosya aktar�m protokolu (TFTP) i�in sunucu ve istemci

%description
The trivial file transfer protocol (tftp) is normally used only for 
booting diskless workstations. It provides very little security, and
should not be enabled unless it is needed. The tftp server is run from
/etc/inetd.conf, and is disabled by default on Red Hat systems.

%description -l pt_BR
O protocolo trivial de transfer�ncia de arquivos (tftp) � normalmente
usado apenas em esta��es de trabalho sem disquete de inicializa��o. Ele
proporciona pouca seguran�a e n�o deve ser habilitado a menos
que seja necess�rio. O servidor tftp � executado atrav�s do inetd
(etc/inetd.conf), e � desabilitado por default no sistema Conectiva.

%description -l es
El protocolo trivial de transferencia de archivos (tftp)
normalmente se usa s�lo en estaciones de trabajo sin disquete de
arranque. Proporciona poca seguridad y no debe ser habilitado a
menos que sea necesario. El servidor tftp se ejecuta a trav�s del
inetd (etc/inetd.conf), y se inhabilita por defecto en el sistema
Conectiva.

%description -l de
Das trivial file transfer protocol (tftp) wird in der Regel nur zum 
Booten von disklosen Workstations benutzt. Es bietet nur geringe 
Sicherheit und sollte nur im Bedarfsfall aktiviert werden. 
Der tftp-Server wird von /etc/inetd.conf aus betrieben 
und ist auf Red-Hat-Systemen standardm��ig ausgeschaltet. 

%description -l fr
Le � trivial file transfer protocol � (tftp) est normalement utilis�
uniquement pour d�marrer les stations de travail sans disque. Il offre
tr�s peu de s�curit� et ne devrait pas �tre activ� sauf si c'est
n�cessaire. Le serveur tftp est lanc� � partir de /etc/inetd.conf et
d�sactiv� par d�faut sur les syst�mes Red Hat. 

%description -l tr
�lkel dosya aktar�m protokolu genelde disksiz i� istasyonlar�n�n a� �zerinden
a��lmalar�nda kullan�l�r. G�venlik denetimleri �ok az oldu�undan zorunlu
kalmad�k�a �al��t�r�lmamal�d�r.

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
