Summary: programs to access SMB network servers
Summary(pt_BR): Programas para acessar servidores SMB
Summary(es): Programas para acceder servidores SMB
Name: smbfs
Version: 2.0.1
Release: 8cl
Copyright: GPL
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
Source: http://metalab.unc.edu/pub/Linux/system/Filesystems/smbfs/smbfs-2.0.1.tgz
Patch: smbfs-2.0.1-glibchacks.patch
Patch1: smbfs-2.0.1-smbumount.patch
Exclusivearch: i386
Buildroot: /tmp/ksmbfs-root
Summary(de): Programme für den Zugriff auf SMG-Netzwerk-Server
Summary(fr): Programme pour accéder aux serveurs des réseaux SMB.
Summary(tr): SMB sunucularýna eriþmek için gerekli programlar

%description
This package includes the tools necessary to mount filesystems from SMB
servers.

%description -l pt_BR
Este pacote inclui as ferramentas necessárias para montar sistemas
de arquivos em servidores SMB.

%description -l es
Este paquete incluye las herramientas necesarias para montar sistemas
de archivos en servidores SMB.

%description -l de
Beinhaltet die erforderlichen Werkzeuge zum Montieren (mounting) von
"  "Dateisystemen auf
SMB-Server  

%description -l fr
Ce paquetage contient les outils nécessaires pour monter les systèmes de
fichiers des serveurs SMB.

%description -l tr
Bu paket, SMB sunucularýndan dosya sistemi baðlamak için gereken araçlarý
içerir.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 16 1998 Donnie Barnes <djb@redhat.com>
- added patch to fix smbumount bug

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- fixes for uid_t/gid_t/mode_t differences between glibc and the 2.0.x kernel

%prep
%setup 
%patch -p1
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin $RPM_BUILD_ROOT/usr/man/man8
install -s util/smbmount $RPM_BUILD_ROOT/usr/sbin/
install -s util/smbumount $RPM_BUILD_ROOT/usr/sbin/
install -m644 man/smbmount.8 $RPM_BUILD_ROOT/usr/man/man8/
install -m644 man/smbumount.8 $RPM_BUILD_ROOT/usr/man/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/sbin/smbmount
/usr/sbin/smbumount
/usr/man/man8/smbmount.8
/usr/man/man8/smbumount.8
%doc README COPYING Changes FAQ smbfs-2.0.1.lsm
