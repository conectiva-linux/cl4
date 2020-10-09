Summary: time server for clock synchornization
Summary(pt_BR): Time server para sincroniza��o de hora
Summary(es): Time server para sincronizaci�n de hora
Name: intimed
Version: 1.10
Release: 11cl
Copyright: freeware
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/intimed/intimed-1.10.tar.gz
BuildRoot: /var/tmp/intimed-root
Summary(de): Zeit-Server zum Synchronisieren von Uhren
Summary(tr): Saat e�zamanlamas� i�in time sunucusu

%description
intimed is a server that will tell networked machines what time it
currently has.  It is useful for keeping networks of machines in
sync with the proper time.

%description -l pt_BR
intimed � um servidor que ir� informar �s m�quinas da rede que horas
ele possui no momento. Ele � �til para manter as m�quinas da rede
em sincronia.

%description -l es
intimed es un servidor que ir� informar la hora a las m�quinas de
la red. Es �til para mantener las m�quinas de la red en sincron�a.

%description -l de
intimed ist ein Server, der an vernetzte Computer die Zeit ausgibt. 
N�tzlich zur Synchronisation eines Netzwerks. 

%description -l fr
intimed est un serveur qui indique aux machines connect�es l'heure
qu'il est. Utile pour synchroniser les r�seaux de machines sur
l'heure correcte.

%description -l tr
intimed, istemci makinalara saatinin ka� oldu�unu s�yleyen bir sunucudur.
Bilgisayar a��ndaki makinalar� e� zamanl� tutmak yararl�d�r.

%prep
%setup -q -c

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin

install -s -m 755 in.timed $RPM_BUILD_ROOT/usr/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/in.timed

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
