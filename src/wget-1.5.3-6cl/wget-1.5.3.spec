Summary: Retrieve files from the World Wide Web using HTTP and FTP
Summary(pt_BR): Cliente na linha de comando para baixar arquivos WWW/FTP com recursão opcional.
Summary(es): Cliente en línea de comando para bajar archivos WWW/FTP con recursión opcional.
Name: wget
%define version 1.5.3
Version: %{version}
Release: 6cl
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: ftp://prep.ai.mit.edu/pub/gnu/wget-%{version}.tar.gz 
Patch0: wget-1.5.0-man.patch
Patch1: wget-1.5.3-pt_BR.patch
BuildRoot: /var/tmp/wget-root
Prereq: /sbin/install-info

%description
GNU Wget is a freely available network utility to retrieve files from the
World Wide Web using HTTP and FTP, the two most widely used Internet
protocols.  It works non-interactively, thus enabling work in the background,
after having logged off. 

The recursive retrieval of HTML pages, as well as FTP sites is supported --
you can use Wget to make mirrors of archives and home pages, or traverse the
web like a WWW robot (Wget understands /robots.txt). 

Wget works exceedingly well on slow or unstable connections, keeping getting
the document until it is fully retrieved. Re-getting files from where it left
off works on servers (both HTTP and FTP) that support it. Matching of
wildcards and recursive mirroring of directories are available when retrieving
via FTP. Both HTTP and FTP retrievals can be time-stamped, thus Wget can see
if the remote file has changed since last retrieval and automatically retrieve
the new version if it has. 

By default, Wget supports proxy servers, which can lighten the network load,
speed up retrieval and provide access behind firewalls. However, if you are
behind a firewall that requires that you use a socks style gateway, you can
get the socks library and compile wget with support for socks. 

Most of the features are configurable, either through command-line options, or
via initialization file .wgetrc.  Wget allows you to install a global startup
file (/etc/wgetrc on RedHat) for site settings. 

%description -l pt_BR
O GNU wget é uma ferramenta de rede para baixar arquivos usando
HTTP e FTP. Ele funciona em modo não interativo, podendo trabalhar
em background. Funciona muito bem, mesmo em conexões lentas ou
instáveis, baixando o arquivo até que ele seja completamente
recebido.

%description -l es
GNU wget es una herramienta de red para bajar archivos usando
HTTP y FTP. Funciona en modo no interactivo, pudiendo trabajar
en background.  Funciona muy bien, incluso en conexiones lentas o
inestables, bajando el archivo hasta que sea completamente recibido.

%prep
%setup -q
%patch0 -p1 -b .man
%patch1 -p1 -b .pt_BR

%build
./configure --prefix=/usr --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc
gzip -9 $RPM_BUILD_ROOT/usr/info/*
strip $RPM_BUILD_ROOT/usr/bin/* || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/wgetrc
/usr/man/man1/wget.1
/usr/bin/wget
/usr/info/*
/usr/share/locale/*/LC_MESSAGES/*
%doc AUTHORS MAILING-LIST NEWS README INSTALL doc/ChangeLog

%post
/sbin/install-info /usr/info/wget.info.gz /usr/info/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/wget.info.gz /usr/info/dir
fi


%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 7 1999 Guilherme Manika <gwm@conectiva.com>
- Mudança irrelevante na tradução

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Nov 27 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- strip binaries

* Fri Nov 06 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 12 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- added pt_BR translations
- updated to 1.5.3

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.5.2

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- modified group to Applications/Networking

* Wed Apr 22 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5.0
- they removed the man page from the distribution (Duh!) and I added it back
  from 1.4.5. Hey, removing the man page is DUMB!

* Fri Nov 14 1997 Cristian Gafton <gafton@redhat.com>
- first build against glibc
