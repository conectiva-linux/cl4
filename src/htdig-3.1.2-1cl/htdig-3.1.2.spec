Summary: A web indexing and searching system for a small domain or intranet
Summary(pt_BR): Indexador e máquina de procura para web.
Summary(es): Indexador y máquina de búsqueda para web.
Name: htdig
Version: 3.1.2
Release: 1cl
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
BuildRoot: /var/tmp/htdig-root
Source0: http://www.htdig.org/files/htdig-%{PACKAGE_VERSION}.tar.gz
Patch0: htdig-%{PACKAGE_VERSION}-conf.patch
URL: http://www.htdig.org/
Prereq: net-tools

%description
The ht://Dig system is a complete world wide web indexing and searching
system for a small domain or intranet. This system is not meant to replace
the need for powerful internet-wide search systems like Lycos, Infoseek,
Webcrawler and AltaVista. Instead it is meant to cover the search needs for
a single company, campus, or even a particular sub section of a web site.

As opposed to some WAIS-based or web-server based search engines, ht://Dig
can span several web servers at a site. The type of these different web
servers doesn't matter as long as they understand the HTTP 1.0 protocol.

%description -l pt_BR
O ht://Dig é um sistema completo para indexação e busca em um domínio pequeno
ou intranet. O sistema não foi projetado para substituir sistemas mais
poderosos para a Internet como o Lycos, Infoseek, Webcrawler ou Altavista.
Seu propósito é cobrir as necessidades para uma companhia, campus ou mesmo
uma seção particular de um site Web.

Diferentemente de sistemas de busca baseados em WAIS ou servidores web o
ht://Dig pode cobrir vários servidores web em uma localização. O tipo
destes diferentes servidores web não interessa desde que eles entendam
o protocolo HTTP 1.0.

%description -l es
El ht://Dig es un sistema completo para indexación y búsqueda
en un dominio pequeño o intranet. El sistema no fue proyectado
para substituir sistemas más potentes en Internet como el Lycos,
Infoseek, Webcrawler o Altavista.  Su propósito es cubrir las
necesidades de una compañía, campus o mismo una sección particular
de un sitio Web.  Diferentemente de sistemas de búsqueda basados en
WAIS o servidores web el ht://Dig puede cubrir varios servidores
web en una localización. El tipo de estos diferentes servidores
web no interesa desde que entiendan el protocolo HTTP 1.0.

%prep
%setup -q -n htdig-%{PACKAGE_VERSION}
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--bindir=/usr/sbin --libexec=/usr/lib --libdir=/usr/lib \
	--mandir=/usr/man --sysconfdir=/etc/htdig \
	--localstatedir=/var/lib/htdig \
	--with-image-dir=/home/httpd/html/htdig \
	--with-cgi-bin-dir=/home/httpd/cgi-bin \
	--with-search-dir=/home/httpd/html
make

%install

rm -rf $RPM_BUILD_ROOT

make INSTALL_ROOT=$RPM_BUILD_ROOT install-strip
mkdir -p $RPM_BUILD_ROOT/etc/cron.daily
ln -s ../../usr/sbin/rundig $RPM_BUILD_ROOT/etc/cron.daily/htdig-dbgen
ln -s ../../../../usr/doc/htdig-%{PACKAGE_VERSION} \
	$RPM_BUILD_ROOT/home/httpd/html/htdig/htdoc

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Only run this if installing for the first time
if [ "$1" = 1 ]; then
	SERVERNAME="`grep '^ServerName' /etc/httpd/conf/httpd.conf | awk '{print $2}'`"
	[ -z "$SERVERNAME" ] && SERVERNAME="`hostname -f`"
	[ -z "$SERVERNAME" ] && SERVERNAME="localhost"
	echo "start_url:	http://$SERVERNAME/
local_urls:	http://$SERVERNAME/=/home/httpd/html/
local_user_urls:	http://$SERVERNAME/=/home/,/public_html/" >> /etc/htdig/htdig.conf

fi

%files
%defattr(-,root,root)
%config /etc/htdig/htdig.conf
%config /usr/sbin/rundig
%config /home/httpd/html/search.html
/etc/cron.daily/htdig-dbgen
/usr/sbin/htdig
/usr/sbin/htfuzzy
/usr/sbin/htmerge
/usr/sbin/htnotify
/var/lib/htdig
/home/httpd/cgi-bin/htsearch
/home/httpd/html/htdig

%doc CONFIG README htdoc/*

%changelog
* Wed Jun 30 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- prereqs net-toos
- injected new groups

* Thu Apr 22 1999 Gilles Detillieux <grdetil@scrc.umanitoba.ca>
  - updated to version 3.1.2 final release

* Wed Feb 17 1999 Gilles Detillieux <grdetil@scrc.umanitoba.ca>
  - updated to version 3.1.1 final release
  - updated to release 1, included patch for htsearch parser bug

* Thu Feb  4 1999 Gilles Detillieux <grdetil@scrc.umanitoba.ca>
  - put web stuff back in /home/httpd/html & /home/httpd/cgi-bin, so it can
	go over a standard Apache installation on Red Hat
  - cleaned up %install to make use of new features

* Thu Feb 4 1999 Ric Klaren <klaren@telin.nl>
  - changed buildroot stuff
  - minor spec file fixes
  - install web stuff in /home/httpd/htdig
  - made rundig config file

* Tue Sep 22 1998 Gilles Detillieux <grdetil@scrc.umanitoba.ca>
  - Added local_urls stuff to generated htdig.conf file

* Fri Sep 18 1998 Gilles Detillieux <grdetil@scrc.umanitoba.ca>
  - Built the rpm from latest htdig source (3.1.0b1), using earlier
    versions of rpms by Mihai Ibanescu <misa@dntis.ro> and Elliot Lee
    <sopwith@cuc.edu> as a model, incorporating ideas from both.  I've
    made the install locations as FSSTND compliant as I can think of.

