Summary: Leading World Wide Web server
Summary(pt_BR): Servidor HTTPD para prover serviços WWW
Summary(es): Servidor HTTPD para proveer servicios WWW
Name: apache
%define version 1.3.6
%define modversion 2.3.3
Version: %{version}
Release: 15cl
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)

#Source: ftp://ftp.apache.org/apache/dist/apache_%{version}.tar.gz
# recompressed with bzip2
Source: ftp://ftp.apache.org/apache/dist/apache_%{version}.tar.bz2
Source1: index.html.tgz
#Source2: poweredby.gif
Source3: httpd-ssl.init
Source4: apache-mod_ssl.log
Source5: httpd.conf-cnc

Source8: http://www.modssl.org/source/mod_ssl-%{modversion}-%{version}.tar.bz2
Source9: make-test-certificate
Source10: thawte-create
Source11: make-hash-symlinks

Source12: mod_bandwidth.c
Source13: mod_bandwidth.txt
Source14: apacnc.sh

Patch0: apache_1.3.3-cnc.patch
Patch1: apache_1.3.6-apxs.patch
Patch2: apache_1.3.6-srvroot.patch
Patch3: apache-1.3.6-perl.patch
Patch4: apache-1.3.6-nbdm.patch

Copyright: Freely distributable and usable
BuildRoot: /var/tmp/apache-root
Requires: mailcap openssl >= 0.9.2b
Prereq: chkconfig, mktemp
Provides: webserver
Obsoletes: apache-doc apache-ssl
Summary(de): Leading World Wide Web-Server
Summary(fr): Serveur Web leader du march<E9>
Summary(tr): Lider WWW taray<FD>c<FD>

%description
Apache is a full featured web server that is freely available, and also
mappens to be the most widely used.

%description -l pt_BR
O servidor web Apache é o melhor servidor gratuito disponível
no mundo UNIX hoje. Ele usa HTTP (HyperText Transfer Protocol)
para permitir que browsers web vejam documentos e submetam dados
remotamente.  Ele pode executar várias funções diferentes, incluindo
funções de proxy e cache, e oferece características como monitor
de status, conversão dinâmica de tipo, e mais.

Este servidor Apache foi compilado com o suporte a SSL.

%description -l es
El servidor web Apache es el mejor servidor gratuito disponible en el
mundo UNIX hoy. Usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vean documentos y sometan datos remotamente.
Puede ejecutar varias funciones diferentes, incluyendo funciones de
proxy y caché, y nos ofrece características como monitor de estado,
conversión dinámica de tipo, y otras más.  Este servidor Apache
fue compilado con el soporte a SSL.

%package devel
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Summary: Header files from apache for developing/compiling 3rd party modules
Summary(pt_BR): Arquivos de inclusão do Apache para desenvolvimento de módulos.
Summary(es): Archivos de inclusión del Apache para desarrollo de módulos.
Obsoletes: secureweb-devel

%description devel
This package includes the header files for Apache, as well as the
'apxs' binary for building dynamic shared objects (DSOs).  This package needs
to be installed if you want to compile or develop additional modules for
Apache.

%description -l pt_BR devel
Este pacote contem os arquivos de inclusão para o Apache, bem como
o utilitário apxs para a construção de objetos compartilhados
dinâmicos (DSOs). Este pacote precisa ser instalado se você deseja
compilar ou desenvolver módulos adicionais para o Apache.

%description -l es devel
Este paquete contiene los archivos de inclusión para el Apache,
bien como el utilitario apxs para la construcción de objetos
compartidos dinámicos (DSOs). Ha ce falta instalar este paquete si
deseas compilar o desarrollar módulos adicionales para Apache.

%prep
# first, unpack apache.  We unpack it BELOW a toplevel directory "secureweb"
%setup -q -n apache_%{version} -a 8
%patch0 -p1 -b .redhat
%patch1 -p1 -b .apxs
%patch2 -p1 -b .srvroot
%patch3 -p1 
%patch4 -p1

%build
cd mod_ssl-%{modversion}-%{version}
./configure --with-apache=..
cd ..
cp $RPM_SOURCE_DIR/apacnc.sh .
chmod +x apacnc.sh
./apacnc.sh
#SSL_BASE=SYSTEM 
#OPTIM="$RPM_OPT_FLAGS" 

#	./configure --prefix=/usr \
#	--sbindir=/usr/sbin/ \
#	--libexecdir=/usr/lib/apache \
#	--sysconfdir=/etc/httpd/conf \
#	--serverroot=/etc/httpd \
#	--datadir=/home/httpd \
#	--includedir=/usr/include/apache \
#	--logfiledir=/var/log/httpd \
#	--localstatedir=/var \
#	--runtimedir=/var/run \
#	--proxycachedir=/var/cache/httpd \
#	--with-perl=/usr/bin/perl \
#	--enable-module=ssl \
#	--enable-module=all \
#	--enable-shared=max \
#	--disable-rule=WANTHSREGEX \
#	--disable-rule=SSL_COMPAT \
#	--add-module=%{SOURCE12}

make
	
make certificate TYPE=dummy

%install
rm -rf $RPM_BUILD_ROOT
make install root=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/sbin/httpd

# remove apachectl; we have our own SYSV init stuff
#rm $RPM_BUILD_ROOT/usr/bin/apachectl

# rename the html directory
mv $RPM_BUILD_ROOT/home/httpd/htdocs $RPM_BUILD_ROOT/home/httpd/html

# install SYSV init stuff
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m755 $RPM_SOURCE_DIR/httpd-ssl.init \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/httpd

for I in 0 1 2 6; do
	mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc$I.d
	ln -s ../init.d/httpd $RPM_BUILD_ROOT/etc/rc.d/rc$I.d/K15httpd
done
for I in 3 5; do
	mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc$I.d
	ln -s ../init.d/httpd $RPM_BUILD_ROOT/etc/rc.d/rc$I.d/S85httpd
done

# install log rotation stuff
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m644 $RPM_SOURCE_DIR/apache-mod_ssl.log \
	$RPM_BUILD_ROOT/etc/logrotate.d/apache

ln -s ../../var/log/httpd $RPM_BUILD_ROOT/etc/httpd/logs
ln -s ../../usr/lib/apache $RPM_BUILD_ROOT/etc/httpd/modules

#install -m644 $RPM_SOURCE_DIR/apache-index.html \
        #$RPM_BUILD_ROOT/home/httpd/html/index.html

tar xvfz $RPM_SOURCE_DIR/index.html.tgz -C $RPM_BUILD_ROOT/home/httpd/html

# replace Apache's default config file with our own version
install -m644 $RPM_SOURCE_DIR/httpd.conf-cnc \
	$RPM_BUILD_ROOT/etc/httpd/conf/httpd.conf

# install apache source code for devel package
#mkdir -p $RPM_BUILD_ROOT/usr/src
#tar xIf $RPM_SOURCE_DIR/apache_%{version}.tar.bz2 -C $RPM_BUILD_ROOT/usr/src
find $RPM_BUILD_ROOT -type f | \
	xargs grep -l "/usr/local/bin/perl" | \
	xargs perl -pi -e "s|/usr/local/bin/perl|/usr/bin/perl|g;"

# install more SSL stuff
install -s -m755 $RPM_SOURCE_DIR/make-test-certificate $RPM_BUILD_ROOT/usr/bin
install -s -m755 $RPM_SOURCE_DIR/make-hash-symlinks $RPM_BUILD_ROOT/usr/bin
install -s -m755 $RPM_SOURCE_DIR/thawte-create $RPM_BUILD_ROOT/usr/bin

# %doc mod_bandwidth
cp %{SOURCE13} .

%clean
rm -rf $RPM_BUILD_ROOT

%post
#/sbin/chkconfig --add httpd
[ -f /etc/mime.types ] || exit 0
# safely add .htm to mime types if it is not already there
TEMPTYPES=`/bin/mktemp /tmp/mimetypes.XXXXXX`
[ -z "$TEMPTYPES" ] && {
  echo "could not make temporary file, htm not added to /etc/mime.types" >&2
  exit 1
}
( grep -v "^text/html"  /etc/mime.types
  types=$(grep "^text/html" /etc/mime.types | cut -f2-)
  echo -en "text/html\t\t\t"
  for val in $types ; do
      if [ "$val" = "htm" ] ; then
          continue
      fi
      echo -n "$val "
  done
  echo "htm"
) > $TEMPTYPES
cat $TEMPTYPES > /etc/mime.types && rm -f $TEMPTYPES

%preun
if [ $1 = 0 ]; then
   /bin/rm -fr /var/log/httpd/*
   /sbin/chkconfig --del httpd
fi

%files
%defattr(-,root,root)
%dir /etc/httpd/conf
%config /etc/httpd/conf/access.conf
%config /etc/httpd/conf/srm.conf
%config /etc/httpd/conf/httpd.conf
%config /etc/httpd/conf/magic

/etc/httpd/logs
/etc/httpd/modules
%config /etc/logrotate.d/apache
%config /etc/rc.d/init.d/httpd
%config(missingok) /etc/rc.d/rc3.d/S85httpd
%config(missingok) /etc/rc.d/rc5.d/S85httpd
%config(missingok) /etc/rc.d/rc0.d/K15httpd
%config(missingok) /etc/rc.d/rc1.d/K15httpd
%config(missingok) /etc/rc.d/rc2.d/K15httpd
%config(missingok) /etc/rc.d/rc6.d/K15httpd

%dir /home/httpd
%dir /home/httpd/cgi-bin
%dir /home/httpd/html
%config(noreplace) /home/httpd/html/index.html
/home/httpd/html/peng.jpg
/home/httpd/html/apache_pb.gif
/home/httpd/html/mod_ssl_sb.gif
/home/httpd/html/openssl.gif
#/home/httpd/html/poweredby.gif
/home/httpd/html/manual
/home/httpd/icons

/usr/lib/apache
/usr/man/*/*
/usr/sbin/ab
/usr/sbin/httpd
/usr/sbin/logresolve
/usr/sbin/rotatelogs
/usr/bin/*

%dir /etc/httpd/conf/ssl.crt
%dir /etc/httpd/conf/ssl.csr
%dir /etc/httpd/conf/ssl.key
%config(missingok) /etc/httpd/conf/ssl.crt/server.crt
%config(missingok) /etc/httpd/conf/ssl.crt/ca-bundle.crt
%config(missingok) /etc/httpd/conf/ssl.csr/server.csr
%config(missingok) /etc/httpd/conf/ssl.key/server.key
%doc conf/ssl.crt/README.CRT conf/ssl.csr/README.CSR conf/ssl.key/README.KEY
%doc conf/ssl.crt/snakeoil-ca-rsa.crt conf/ssl.crt/snakeoil-ca-dsa.crt
%doc conf/ssl.crt/snakeoil-rsa.crt conf/ssl.crt/snakeoil-dsa.crt
%doc ABOUT_APACHE README README.SSL LICENSE LICENSE.SSL mod_bandwidth.txt

%attr(-,nobody,nobody) %dir /var/cache/httpd
%dir /var/log/httpd


%files devel
%defattr(-,root,root)
/usr/include/apache
/usr/sbin/apxs
#/usr/src/apache_%{version}

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 19 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed snakeoil files in %doc
- recompressed mod_ssl sources
- chkconfig --add removed, now the user has to explicitily enable auto
  start for the services he/she wants (most users install everything then
  complains about memory usage...)

* Sat Jun 19 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Marcelo Tosatti <marcelo@conectiva.com> 
- update to mod_ssl 2.3.3

* Sun Apr 18 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- requires mailcap instead of /etc/mime.types

* Wed Apr 14 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- added mod_bandwidth
- reincluded /usr/bin/*

* Thu Apr 14 1999 Marcelo Tosatti <marcelo@conectiva.com>
- update to 1.3.6 and mod_ssl 2.2.8

* Mon Nov 09 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- rebuild with mod_ssl-2.0.15-1.3.3

* Wed Nov 04 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- included htpasswd, htdigest and dbmmanage

* Wed Nov 03 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- rebuilded with mod_ssl-2.0.14-1.3.3
- "make certificate TYPE=dummy" is now OK

* Wed Oct 28 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Oct 13 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- changed make certificate to TYPE=test

* Sat Oct 10 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to apache-1.3.3 and mod_ssl-1.3.3-2.0.13

* Wed Sep 30 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- integrated mod_ssl
- added pt_BR translations
- added "Conectiva" to the server string and new index.html

* Fri Sep 25 1998 Cristian Gafton <gafton@redhat.com>
- change ownership of cache dir to nobody
- added "Red Hat" to the server string
- updated to version 1.3.2
- fixed all references to httpsd in config files

* Fri Sep 04 1998 Cristian Gafton <gafton@redhat.com>
- small fixes to the spec file
- patch to handle correctly the -d <newroot> option
- leave out the .usr.src.apache_%{version} for now

* Thu Sep 03 1998 Preston Brown <pbrown@redhat.com>
- patched apxs not to bomb out if it can't find httpd

* Wed Sep 02 1998 Preston Brown <pbrown@redhat.com>
- upgraded to apache 1.3.1.
- Heavy rewrite.
- changed providing a_web_server to just webserver.  Humor is not an option.

* Mon Aug 10 1998 Erik Troan <ewt@redhat.com>
- updated to build as non-root user
- added patch to defeat header dos attack

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- fixed the default config files to be more paranoid about security

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- fixed init script
- added index.htm to the list of acceptable indexes

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.2.6
- added post script to install htm extension for text/html into
  /etc/mime.types

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced sysv init script

* Tue Jan 06 1998 Erik Troan <ewt@redhat.com>
- updated to 1.2.5, which includes many security fixes

* Wed Dec 31 1997 Otto Hammersmith <otto@redhat.com>
- fixed overkill on http.init stop

* Wed Dec 31 1997 Erik Troan <ewt@redhat.com>
- added patch for backslash DOS attach

* Thu Nov 06 1997 Donnie Barnes <djb@redhat.com>
- added htdigest binary to file list

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- made the default index.html be config(noreplace) so we no longer
  blow away other folks' index.html

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added chkconfig support
- added restart|status options to initscript
- renamed httpd.init to httpd

* Tue Oct 07 1997 Elliot Lee <sopwith@redhat.com>
- Redid spec file, patches, etc. from scratch.
