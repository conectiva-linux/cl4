Summary: installs the config files to start your own caching namserver
Summary(pt_BR): Instala arquivos de configuração para usar seu próprio servidor de nomes com cache
Summary(es): Instala archivos de configuración para usar su propio servidor de nombres con caché
Name: caching-nameserver
Version: 5.2
Release: 4cl
Copyright: freeware
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://FTP.RS.INTERNIC.NET/domain/named.root
Source1: named.boot
Source2: named.local
Source3: named.conf
Requires: bind
BuildRoot: /var/tmp/caching-nameserver-root
BuildArchitectures: noarch

%description
Includes configuration files for bind (the DNS nameserver) which make it
behave as a simple caching nameserver. Many users on dialup connections
use this package (along with bind) and make the it's own nameserver to
speed up name resoultions.

%description -l pt_BR
Inclui arquivos de configuração para o bind (servidor de nomes DNS)
que faz com que ele se comporte como um cache simples do servidor
de nomes. Vários usuários usam este pacote em conexões discadas
(junto com bind) e fazem o seu próprio servidor de nomes para
acelerar as resoluções.

%description -l es
Incluye archivos de configuración para el bind (servidor de nombres
DNS) que hace con que se comporte como un caché sencillo del servidor
de nombres. Varios usuarios usan este paquete en conexiones marcadas
(junto con bind) y hacen su propio servidor de nombres para acelerar
las resoluciones.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc,var/named}

install -m 644 $RPM_SOURCE_DIR/named.root $RPM_BUILD_ROOT/var/named/named.ca
install -m 644 $RPM_SOURCE_DIR/named.local $RPM_BUILD_ROOT/var/named/named.local
install -m 644 $RPM_SOURCE_DIR/named.boot $RPM_BUILD_ROOT/etc/named.boot
install -m 644 $RPM_SOURCE_DIR/named.conf $RPM_BUILD_ROOT/etc/named.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/named.boot
%config /etc/named.conf
%config /var/named/named.ca
%config /var/named/named.local

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- install bind-8.1.2 named.conf

* Mon May 04 1998 Donnie Barnes <djb@redhat.com>
- upgraded from 1.1 to 5.1 to make caching-nameserver version the same
  as the version of Red Hat that it runs on.  
- updated named.root

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- updated named.root to latest
- updated copyright

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
