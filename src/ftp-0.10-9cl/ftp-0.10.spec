Summary: Standard Unix ftp (file transfer protocol) client
Summary(pt_BR): Cliente ftp padr�o Unix (protocolo de transmiss�o de arquivo)
Summary(es): Cliente ftp padr�n Unix (protocolo de transmisi�n de archivo)
Name: ftp
Version: 0.10
Release: 9cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://sunsite.unc.edu/pub/Linux/system/network/file-transfer/netkit-ftp-0.10.tar.gz
Source700: ftp-man-pt_BR.tar
Patch0: netkit-ftp-0.10-misc.patch
Patch1: netkit-ftp-0.10-overflow.patch
Patch2: netkit-ftp-0.10-i18n.patch
Requires: inetd
BuildRoot: /var/tmp/ftp-root
Summary(de): Standardm��iger Unix-ftp-Client (file transfer protocol) 
Summary(fr): Client ftp (file transfer protocol) standard d'Unix
Summary(tr): Standart UN*X ftp istemcisi

%description
This provides the standard Unix command-line ftp client. ftp is the
standard Internet file transfer protocol, which is extremely popular
for both file archives and file transfers between individuals.

%description -l pt_BR
Este pacote prov� o cliente ftp padr�o Unix para a linha de
comando. O ftp � o protocolo padr�o de transfer�ncia de arquivos
na Internet, e � extremamente popular.

%description -l es
Este paquete provee el cliente ftp padr�n Unix para la l�nea de
comando. ftp es el protocolo padr�n de transferencia de archivos
en Internet, y es extremamente popular.

%description -l de
Dadurch wird der Standard-Unix-Befehlszeilen-FTP-Client bereitgestellt. 
ftp ist das Standard-Internet-Dateitransfer-Protokoll, das sich 
sowohl f�r Dateiarchive als auch f�r Dateitransfers zwischen 
Individuen gro�er Beliebtheit erfreut. 

%description -l fr
Contient le client ftp en ligne de commande standard d'Unix. ftp est
le protocole standard de transfert de fichiers sur l'Internet. Il est
tr�s utilis� pour les archives et les transferts de fichiers entre individus.

%description -l tr
Bu pakette UN*X'in standart komut sat�r� ftp istemcisi bulunmaktad�r. Ger�i
grafik arabirimlerin egemen oldu�u bir �a�da biraz demode gibi g�z�kebilir
ancak anonim dosya ar�ivleri ve ki�iler aras� dosya iletimi i�in hala yayg�n
olarak kullan�lmaktad�r.

%prep
%setup -q -n netkit-ftp-0.10
%patch0 -p1
%patch1 -p1 -b .ovr
%patch2 -p1 -b .i18n
 
%build
./configure
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
cd ftp/po
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make INSTALLROOT=$RPM_BUILD_ROOT install
cd ftp/po
make INSTALLROOT=$RPM_BUILD_ROOT install




mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/ftp-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/ftp
/usr/bin/pftp
/usr/man/man1/ftp.1
/usr/man/man1/pftp.1
/usr/share/locale/pt_BR/LC_MESSAGES/ftp.mo
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- readline support
- added Group, Summary and %description translations

* Thu Jan 21 1999 Conectiva <dist@conectiva.com>
- added pt_BR translations
- i18n patch

* Tue Dec 15 1998 Cristian Gafton <gafton@redhat.com>
- fixed bugs 265, 304
- fixed security vulnerability

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
