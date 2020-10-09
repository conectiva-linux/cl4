Summary: ftp client with a nice interface
Summary(pt_BR): Cliente ftp com uma interface agrad�vel
Summary(es): Cliente ftp con una interface agradable
Name: ncftp
Version: 3.0beta19
Release: 6cl
Copyright: Distributable
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://ftp.ncftp.com/ncftp/3.0BETA/ncftp-%{version}-src.tar.gz
Source1: ncftp.desktop
Source800: ncftp-wmconfig.i18n.tgz
BuildRoot: /var/tmp/ncftp-root
Summary(de): ftp-Client mit einer attraktiven Bedineroberfl�che
Summary(fr): Client ftp avec une interface agr�able.
Summary(tr): G�zel aray�zl� bir ftp istemcisi

%description
Ncftp is a ftp client with many advantageous over the standard one. It
includes command line editing, command histories, support for recurisive
gets, automatic logins, and much more.

%description -l pt_BR
ncftp � um cliente ftp com v�rias vantagens sobre o padr�o. Ele
inclui edi��o por linha de comando, hist�rico de comandos, logins
autom�ticos, e muito mais.

%description -l es
ncftp es un cliente ftp con varias ventajas sobre el padr�n. Incluye
edici�n por l�nea de comando, hist�rico de comandos, logins
autom�ticos, y mucho m�s.

%description -l de
Ncftp ist ein ftp-Client mit vielen Verbesserungen. Er enth�lt Funktionen wie
Befehlszeilenbearbeitung, Befehlsgeschichte, Unterst�tzung f�r rekursive
Ladevorg�nge, automatische Logins, usw.

%description -l fr
Ncftp est un client ftp poss�dant de nombreux avantages sur le client
standard. Il inclue une edition de la ligne de commande, un historique
des commandes, un support pour des t�l�chargements r�cursifs, des logins
automatiques, et plus encore.

%description -l tr
Ncftp, standart ftp istemcisine oranla pek �ok avantaj� olan bir yaz�l�md�r.
Komut tarih�esi, rek�rsif dosya aktar�m�, kendili�inden sisteme giri� gibi
yetenekleri vard�r.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,man/cat1}

make prefix=$RPM_BUILD_ROOT/usr install

mkdir -p $RPM_BUILD_ROOT/usr/share/apps/Networking
install -m644 $RPM_SOURCE_DIR/ncftp.desktop $RPM_BUILD_ROOT/usr/share/apps/Networking/ncftp.desktop

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/





tar xvfpz $RPM_SOURCE_DIR/ncftp-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(missingok) /usr/share/apps/Networking/ncftp.desktop
%config(missingok) /etc/X11/wmconfig/ncftp
/usr/bin/ncftp
/usr/bin/ncftpget
/usr/bin/ncftpput
/usr/bin/ncftpbatch
/usr/bin/ncftpls
/usr/bin/ncftpbookmarks
/usr/man/man1/ncftp.1
/usr/man/man1/ncftpget.1
/usr/man/man1/ncftpput.1
/usr/man/man1/ncftpbatch.1
/usr/man/man1/ncftpls.1

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x


* Fri Jun 11 1999 Marcelo Tosatti <marcelo@conectiva.com>
- update to 3.0beta19

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Thu Dec 03 1998 Marcelo Tosatti <marcelo@conectiva.com>
- update to 3.0beta16

* Fri Nov 20 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- ncftp.wmconfig.pt_BR

* Thu Nov  5 1998 Bill Nottingham <notting@redhat.com>
- update to 3.0beta15

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- compiled for Manhattan

* Fri Mar 20 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.4.3 for security reasons

* Wed Nov 05 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the spec file

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- updated to ncftp 2.4.2

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Donnie Barnes <djb@redhat.com>
- Rebuild as Sun version didn't work.
