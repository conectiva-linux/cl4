Summary: A server-side, HTML-embedded scripting language
Summary(pt_BR): PHP3 - uma poderosa linguagem de script para HTML
Summary(es): PHP3 - un potente lenguaje de script para HTML
Name: mod_php3
%define version 3.0.9
Version: %{version}
Release: 5cl
URL: http://www.php.net
Source: ftp://www.php.net/pub/distributions/php-%{version}.tar.bz2
Source1: http://www.php.net/distributions/manual.tar.bz2
Source2: http://www.php.net/distributions/manual-3.0.6.pdf.bz2
Source3: http://www.php.net/distributions/manual.rtf.bz2
Source4: http://www.php.net/distributions/bigmanual.html
Source5: http://www.php.net/distributions/copyright.html
Source6: http://www.php.net/logos/big-logo1t.gif
Source7: FAQ.php3
Source8: changes.php3
Source9: php-add
Source10: php-del
Source11: php-add-doc
Source12: php-del-doc
Source13: logo1t.gif
Source14: indexphp3.html
Source15: imap-devel.tgz
Patch: php3.patch
Patch1: php-3.0.8-inc.patch
Patch2: php-imap.patch
Patch3: php-make.patch
Icon: php3.gif
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires: apache >= 1.3.6 
Obsoletes: php, mod_php
BuildRoot: /tmp/%{name}-%{version}-root
BuildPrereq: apache-devel

%description
PHP3 is a powerful apache module that adds scripting and database connection
capabilities to the apache server.

%description -l pt_BR
PHP3 é um poderoso módulo para o apache, adicionando uma linguagem de
script embutido em HTML, com características avançadas como o acesso
a banco de dados.

%description -l es
PHP3 es un fuerte módulo para apache, que adiciona un lenguaje
de script incluso en HTML, con características avanzadas como el
acceso a banco de datos.

%package doc
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Requires: webserver
Summary: Online manual for PHP3
Summary(pt_BR): Manual para o PHP3
Summary(es): Manual de PHP3

%description doc
Documentation for PHP3

%description -l pt_BR doc
Documentação para o PHP3

%description -l es doc
Documentacion del PHP3

%package gd
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires: mod_php3 >= %{version}
Requires: freetype >= 1.2-6
Summary: GD (graphic creation) module for PHP3 (apache)
Summary(pt_BR): Modulo GD (criação de gráficos) para o PHP3
Summary(es): GD (graphic creation) module for PHP3 (apache)
%description gd 
 This package provides a PHP3 module (apache version) to use the GD
 graphics library calls directly from PHP3 scripts.

%description -l pt_BR gd
Este pacote fornece um módulo PHP3 (versão apache) para usar a biblioteca
gráfica GD diretamente a partir de scripts PHP3.

%description -l es gd
This package provides a PHP3 module (apache version) to use the GD
graphics library calls directly from PHP3 scripts.

%package imap
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires: mod_php3 >= %{version}
Summary: IMAP module for PHP3 (apache) 
Summary(pt_BR): Módulo IMAP para o PHP3
Summary(es): IMAP module for PHP3 (apache) 

%description imap
 This package provides a PHP3 module (apache version) for using IMAP
 functions directly from PHP3 scripts.

%description -l pt_BR imap
Este pacote fornece um módulo PHP3 (versão apache) para usar funções
IMAP diretamente a partir de scripts PHP3.

%description -l es imap
This package provides a PHP3 module (apache version) for using IMAP
functions directly from PHP3 scripts.

%package mysql
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires:  mod_php3 >= %{version}
Provides: php3-database
Summary: Mysql module for PHP3 (Apache)
Summary(pt_BR): Módulo mysql para o PHP3
Summary(es): Mysql module for PHP3 (Apache)

%description mysql
 This package provides a PHP3 module (apache version) for mysql connectivity
 directly from PHP3 scripts.

%description -l pt_BR mysql
Este pacote fornece um módulo PHP3 (versão apache) para conectar-se ao
mysql diretamente a partir de scripts PHP3.

%description -l es mysql
This package provides a PHP3 module (apache version) for mysql connectivity
directly from PHP3 scripts.

%package pgsql
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires: mod_php3 >= %{version}
Provides: php3-database
Summary: PostgreSQL module for PHP3 (apache)
Summary(pt_BR): Módulo PostgreSQL para o PHP3
Summary(es): PostgreSQL module for PHP3 (apache)
%description pgsql 
 
 This package provides a PHP3 module (apache version) for PostgreSQL
 connectivity directly from PHP3 scripts.

%description -l pt_BR pgsql
Este pacote fornece um módulo PHP3 (versão apache) para conectar-se ao
PostgreSQL diretamente a partir de scripts PHP3.

%description -l es pgsql
This package provides a PHP3 module (apache version) for PostgreSQL
connectivity directly from PHP3 scripts.

%package cgi
Summary:   A server-side, HTML-embedded scripting language
Summary(pt_BR): Uma linguagem de script, processada no servidor e embutida em HTML
Summary(es): A server-side, HTML-embedded scripting language
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
%description cgi
 This package provides a standalone cgi binary (usable as a standalone
 interpreter) and some modules providing extra functions
 
 With additional modules it supports direct communication with postgresql,
 mysql, msql databases, dbf files, and it has an interface to the libgd
 graphics library.

%description -l pt_BR cgi
PHP3 é um poderoso CGI que adiciona uma linguagem de script embutido em HTML,
com características avançadas como o acesso a banco de dados.

%description -l es cgi
This package provides a standalone cgi binary (usable as a standalone
interpreter) and some modules providing extra functions
 
With additional modules it supports direct communication with postgresql,
mysql, msql databases, dbf files, and it has an interface to the libgd
graphics library.

%package cgi-gd
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires: mod_php3-cgi >= %{version}
Requires: freetype >= 1.2-6
Summary: GD (graphic creation) module for PHP3 (cgi)
Summary(pt_BR): Módulo GD (criação de gráficos) para o PHP3 (cgi)
Summary(es): GD (graphic creation) module for PHP3 (cgi)
%description cgi-gd 
 This package provides a PHP3 module (cgi version) to use the GD graphics
 library calls directly from PHP3 scripts.

%description -l pt_BR cgi-gd
Este pacote fornece um módulo PHP3 (versão CGI) para usar a biblioteca
gráfica GD diretamente a partir de scripts PHP3.

%description -l es cgi-gd
This package provides a PHP3 module (cgi version) to use the GD graphics
library calls directly from PHP3 scripts.

%package  cgi-imap
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires: mod_php3-cgi >= %{version}
Summary: IMAP module for PHP3 (cgi) 
Summary(pt_BR): Módulo IMAP para o PHP3 (cgi)
Summary(es): IMAP module for PHP3 (cgi) 
%description  cgi-imap
 
 This package provides a PHP3 module (cgi version) for using IMAP
 functions directly from PHP3 scripts.

%description -l pt_BR cgi-imap
Este pacote fornece um módulo PHP3 (versão CGI) para usar funções
IMAP diretamente a partir de scripts PHP3.

%description -l es cgi-imap
This package provides a PHP3 module (cgi version) for using IMAP
functions directly from PHP3 scripts.

%package  cgi-mysql
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires:  mod_php3-cgi >= %{version}
Provides: php3-database
Summary: Mysql module for PHP3 (cgi)
Summary(pt_BR): Módulo mysql para o PHP3 (cgi)
Summary(es): Mysql module for PHP3 (cgi)
%description  cgi-mysql
 
 This package provides a PHP3 module (cgi version) for mysql connectivity
 directly from PHP3 scripts.

%description -l pt_BR cgi-mysql
Este pacote fornece um módulo PHP3 (versão CGI) para conectar-se a bancos de
dados mysql diretamente a partir de scripts PHP3.

%description -l es cgi-mysql
This package provides a PHP3 module (cgi version) for mysql connectivity
directly from PHP3 scripts.

%package  cgi-pgsql
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires: mod_php3-cgi >= %{version}
Provides: php3-database
Summary: PostgreSQL module for PHP3 (cgi)
Summary(pt_BR): Módulo PostgreSQL para o PHP3 (cgi)
Summary(es): PostgreSQL module for PHP3 (cgi)
%description  cgi-pgsql 
 
 This package provides a PHP3 module (cgi version) for PostgreSQL
 connectivity directly from PHP3 scripts.

%description -l pt_BR cgi-pgsql
Este pacote fornece um módulo PHP3 (versão CGI) para conectar-se a bancos de
dados PostgreSQL diretamente a partir de scripts PHP3.

%description -l es cgi-pgsql
This package provides a PHP3 module (cgi version) for PostgreSQL
connectivity directly from PHP3 scripts.

%prep
%setup -q -n php-%{version} -a 15
%patch -p1
%patch1 -p1
%patch2 -p1

install -m644 %{SOURCE2} doc
install -m644 %{SOURCE3} doc
install -m644 %{SOURCE4} doc
install -m644 %{SOURCE5} doc
chmod a-x doc/*.awk

%build

# Apache modules
./configure \
	--with-apxs \
	--prefix=/usr \
	--enable-safe-mode \
	--with-exec-dir=/usr/bin \
	--with-zlib \
	--with-dbase \
	--with-filepro \
	--with-config-file-path=/etc/php3/apache \
	--disable-debug \
	--enable-magic-quotes \
	--enable-debugger \
	--enable-bcmath \
	--enable-track-vars \
	--with-system-regex \
	--with-yp \
	--without-gd \
	--without-xml \
	--with-imap=./imap
	

make
make -C convertor
gcc -shared -fPIC -DCOMPILE_DL=1  -I. -I/usr/include/apache -I/usr/include/mysql -o mysql.so ./functions/mysql.c -L/usr/lib/mysql -lmysqlclient -lc
gcc -shared -fPIC -DCOMPILE_DL=1  -I. -I/usr/include/apache -I/usr/include/pgsql -o pgsql.so ./functions/pgsql.c -lpq -lc

cd dl && ./setup
cd ..
patch -p1 < $RPM_SOURCE_DIR/php-make.patch
cd dl
make clean; make CFLAGS="-I/usr/include/apache -I." calendar.so crypt.so

sed -e "s/HAVE_IMAP 0/HAVE_IMAP 1/g" \
-e "s/HAVE_LDAP 0/HAVE_LDAP 1/g" \
-e "s/HAVE_LIBEXPAT 0/HAVE_LIBEXPAT 1/g" \
-e "s/HAVE_LIBGD13 0/HAVE_LIBGD13 1/g" \
-e "s/HAVE_LIBGD 0/HAVE_LIBGD 1/g" \
-e "s/\/\* #undef HAVE_LIBGD \*\//#define HAVE_LIBGD 1/g" \
-e "s/\/\* #undef HAVE_LIBTTF \*\//#define HAVE_LIBTTF 1/g" < config.h > config.h- && mv -f config.h- config.h
cd ..
gcc -shared -fPIC -DCOMPILE_DL=1  -I. -I/usr/include/apache -o gd.so ./functions/gd.c ./functions/gdcache.c ./functions/gdttf.c -lgd -lttf -lc
gcc -shared -fPIC -DCOMPILE_DL=1  -I. -I/usr/include/apache -I/usr/include/imap -o imap.so ./functions/imap.c imap/lib/c-client.a -lc
#gcc -shared -fPIC -DCOMPILE_DL=1  -I. -I/usr/include/apache -o ldap.so ./functions/ldap.c -lldap -llber -lc

mkdir apache && mv *.so dl/*.so apache   

make clean


# CGI
./configure \
	--enable-force-cgi-redirect \
        --prefix=/usr \
        --enable-safe-mode \
        --with-exec-dir=/usr/bin \
        --with-zlib \
        --with-dbase \
        --with-filepro \
        --with-config-file-path=/etc/php3/cgi \
        --disable-debug \
        --enable-magic-quotes \
        --enable-debugger \
        --enable-bcmath \
        --enable-track-vars \
        --with-system-regex \
	--with-yp \
        --without-gd \
	--without-xml 
	

make LDFLAGS="-rdynamic"

gcc -shared -fPIC -DCOMPILE_DL=1  -I. -I/usr/include/mysql -o mysql.so ./functions/mysql.c  -L/usr/lib/mysql -lmysqlclient -lc
gcc -shared -fPIC -DCOMPILE_DL=1  -I. -I/usr/include/pgsql -o pgsql.so ./functions/pgsql.c -lpq -lc
(cd ./dl && ./setup ; make clean; make CFLAGS="-I." calendar.so crypt.so)


sed -e "s/HAVE_IMAP 0/HAVE_IMAP 1/g" \
-e "s/HAVE_LDAP 0/HAVE_LDAP 1/g" \
-e "s/HAVE_LIBEXPAT 0/HAVE_LIBEXPAT 1/g" \
-e "s/HAVE_LIBGD13 0/HAVE_LIBGD13 1/g" \
-e "s/HAVE_LIBGD 0/HAVE_LIBGD 1/g" \
-e "s/\/\* #undef HAVE_LIBGD \*\//#define HAVE_LIBGD 1/g" \
-e "s/\/\* #undef HAVE_LIBTTF \*\//#define HAVE_LIBTTF 1/g" < config.h > config.h- && mv -f config.h- config.h


gcc -shared -fPIC -DCOMPILE_DL=1  -I. -o gd.so ./functions/gd.c ./functions/gdcache.c ./functions/gdttf.c -lgd -lttf -lc
gcc -shared -fPIC -DCOMPILE_DL=1  -I. -I/usr/include/imap -o imap.so ./functions/imap.c imap/lib/c-client.a -lc
#gcc -shared -fPIC -DCOMPILE_DL=1  -I. -o ldap.so ./functions/ldap.c -lldap -llber -lc
mkdir cgi && mv *.so dl/*.so php cgi   


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/php3/apache
install -d $RPM_BUILD_ROOT/etc/php3/cgi
install -d $RPM_BUILD_ROOT/home/httpd/icons
install -d $RPM_BUILD_ROOT/home/httpd/cgi-bin
install -d $RPM_BUILD_ROOT/home/httpd/html/manual/mod/mod_php3
install -d $RPM_BUILD_ROOT/usr/lib/apache
install -d $RPM_BUILD_ROOT/usr/lib/php3
install -d $RPM_BUILD_ROOT/usr/lib/php3/apache
install -d $RPM_BUILD_ROOT/usr/lib/php3/cgi
install -d $RPM_BUILD_ROOT/usr/bin

cd apache
install -m755 libphp3.so $RPM_BUILD_ROOT/usr/lib/apache/mod_php3.so
install -m755 crypt.so $RPM_BUILD_ROOT/usr/lib/php3/apache
install -m755 calendar.so $RPM_BUILD_ROOT/usr/lib/php3/apache
install -m755 gd.so $RPM_BUILD_ROOT/usr/lib/php3/apache
install -m755 imap.so $RPM_BUILD_ROOT/usr/lib/php3/apache
#install -m755 ldap.so $RPM_BUILD_ROOT/usr/lib/php3/apache
install -m755 mysql.so $RPM_BUILD_ROOT/usr/lib/php3/apache
install -m755 pgsql.so $RPM_BUILD_ROOT/usr/lib/php3/apache

cd ../cgi
install -m755 php $RPM_BUILD_ROOT/home/httpd/cgi-bin
install -m755 crypt.so $RPM_BUILD_ROOT/usr/lib/php3/cgi
install -m755 calendar.so $RPM_BUILD_ROOT/usr/lib/php3/cgi
install -m755 gd.so $RPM_BUILD_ROOT/usr/lib/php3/cgi
install -m755 imap.so $RPM_BUILD_ROOT/usr/lib/php3/cgi
#install -m755 ldap.so $RPM_BUILD_ROOT/usr/lib/php3/cgi
install -m755 mysql.so $RPM_BUILD_ROOT/usr/lib/php3/cgi
install -m755 pgsql.so $RPM_BUILD_ROOT/usr/lib/php3/cgi

cd ../
install -m755 convertor/convertor $RPM_BUILD_ROOT/usr/bin
install -m644 php3.ini-apache $RPM_BUILD_ROOT/etc/php3/apache/php3.ini
install -m644 php3.ini-cgi $RPM_BUILD_ROOT/etc/php3/cgi/php3.ini
install -m644 extra/icons/*.gif $RPM_BUILD_ROOT/home/httpd/icons
install -m644 %{SOURCE13} $RPM_BUILD_ROOT/home/httpd/icons
install -m644 %{SOURCE6} $RPM_BUILD_ROOT/home/httpd/icons
install -m755 %{SOURCE9} $RPM_BUILD_ROOT/usr/bin
install -m755 %{SOURCE10} $RPM_BUILD_ROOT/usr/bin
install -m755 %{SOURCE11} $RPM_BUILD_ROOT/usr/bin
install -m755 %{SOURCE12} $RPM_BUILD_ROOT/usr/bin
mv -f convertor/README convertor/README.convertor
cp -f %{SOURCE7} .
cp -f %{SOURCE8} .
mkdir -p $RPM_BUILD_ROOT/home/httpd/php/bin
ln -sf /bin/uname $RPM_BUILD_ROOT/home/httpd/php/bin/uname
mkdir -p $RPM_BUILD_ROOT/home/httpd/html/manual/mod/mod_php3
cd $RPM_BUILD_ROOT/home/httpd/html/manual/mod/mod_php3
tar xIpf %{SOURCE1}
ln -sf manual.html index.html

# install modified index.html
install -m644 %{SOURCE14} $RPM_BUILD_ROOT/home/httpd/html

strip $RPM_BUILD_ROOT/usr/{bin/convertor,lib/apache/*.so,lib/php3/*.so,lib/php3/cgi/*.so} ||

%post
#/usr/bin/php-add

%preun
#if [ $1 = 0 ]; then
#  /usr/bin/php-del
#fi

%post doc
/usr/bin/php-add-doc

%preun doc
if [ $1 = 0 ]; then
/usr/bin/php-del-doc
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BUGS CHANGES COPYING CREDITS ChangeLog EXTENSION_STATUS FUNCTION_LIST.txt INSTALL* LICENSE TODO WISHLIST*
%doc convertor/README.convertor examples FAQ.php3 changes.php3
%config /etc/php3/apache/php3.ini
%dir /home/httpd/php
/home/httpd/html/indexphp3.html
/home/httpd/php/bin
/home/httpd/icons/*
/usr/bin/convertor
/usr/lib/apache/*.so
/usr/bin/php-add
/usr/bin/php-del
/usr/lib/php3/apache/calendar.so
/usr/lib/php3/apache/crypt.so


%files doc
%defattr(-,root,root)
%doc doc/*
%dir /home/httpd/php
/home/httpd/html/manual/mod/mod_php3
/usr/bin/php-add-doc
/usr/bin/php-del-doc

%files gd
/usr/lib/php3/apache/gd.so

%files imap
/usr/lib/php3/apache/imap.so

#%files ldap
#/usr/lib/php3/apache/ldap.so

%files mysql
/usr/lib/php3/apache/mysql.so

%files pgsql
/usr/lib/php3/apache/pgsql.so


%files cgi
%defattr(-,root,root)
/home/httpd/cgi-bin/php
/usr/lib/php3/cgi/calendar.so
/usr/lib/php3/cgi/crypt.so
%config /etc/php3/cgi/php3.ini

%files cgi-gd
/usr/lib/php3/cgi/gd.so

%files  cgi-imap
/usr/lib/php3/cgi/imap.so

#%files  cgi-ldap
#/usr/lib/php3/cgi/ldap.so

%files  cgi-mysql
/usr/lib/php3/cgi/mysql.so

%files  cgi-pgsql
/usr/lib/php3/cgi/pgsql.so

%changelog
* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- some BuildPreReqs...

* Sat Jun 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed
- fixed releases
- fixed requires: was requiring mod-php3 instead of mod_php3

* Tue May 25 1999 Pablo Costa <pablo@ib.usp.br>
- Compile with apache 1.3.6 and glibc 2.1
- Compile without ssl 
- Add nis(YP) support
- Add package cgi. Now php can work without apache
- Add packages with apache modules:  gd, imap, ldap, mysql, pgsql and xml
- Add packages with cgi modules:  gd, imap, ldap, mysql, pgsql and xml
- Rename add-php, del-php to php-add and php-del
- Change config path to /etc/php3/apache (apache version)
- Change config path to /etc/php3/cgi (cgi version)
- Change config path to /etc/php3/cgi (cgi version)
- Suppressed post and preun scripts (Wait for next release :-)

* Mon Feb  2 1999 Henri Gomez <gomez@slib.fr>
- Adapted apache-php SRPMS from Khimenko Victor SRPMS to standard RH5.2
- moved /usr/libexec/apache to /usr/lib/apache to follow latest apache rpm
- added requires SSLeay
- added -L/usr/lib/mysql to apxs
- mod_ssl 2.2.0 upgraded
- now exec bin in /usr/bin instead of /home/httpd/bin
- modified index.html to reflect PHP3 installation.

* Fri Jan 22 1999 Khimenko Victor <khim@sch57.msk.ru>
- mod_ssl 2.1.8 is out => EAPI changes

* Wed Jan 13 1999 Khimenko Victor <khim@sch57.msk.ru>
- Apache 1.3.4 => recompilation of all DSO modules

* Sun Jan 10 1999 Khimenko Victor <khim@sch57.msk.ru>
- error in add-php-doc script fixed

* Wed Dec 30 1998 Khimenko Victor <khim@sch57.msk.ru>
- now this rpm could be even really used (i.e. mod_php.so could be loaded :-)

* Fri Dec 25 1998 Khimenko Victor <khim@sch57.msk.ru>
- update to 3.0.6
# this changes are commented because a got a "not in chronological order" from 
# the cute rpm 3.0
#* Mon Feb  2 1999 Henri Gomez <gomez@slib.fr>
#- Adapted apache-php SRPMS from Khimenko Victor SRPMS to standard RH5.2
#- moved /usr/libexec/apache to /usr/lib/apache to follow latest apache rpm
#- added requires SSLeay
#- added -L/usr/lib/mysql to apxs
#- mod_ssl 2.2.0 upgraded
#- now exec bin in /usr/bin instead of /home/httpd/bin
#- modified index.html to reflect PHP3 installation.
#
#* Fri Jan 22 1999 Khimenko Victor <khim@sch57.msk.ru>
#- mod_ssl 2.1.8 is out => EAPI changes

#* Wed Jan 13 1999 Khimenko Victor <khim@sch57.msk.ru>
#- Apache 1.3.4 => recompilation of all DSO modules

#* Sun Jan 10 1999 Khimenko Victor <khim@sch57.msk.ru>
#- error in add-php-doc script fixed

#* Wed Dec 30 1998 Khimenko Victor <khim@sch57.msk.ru>
#- now this rpm could be even really used (i.e. mod_php.so could be loaded :-)

* Fri Dec 25 1998 Khimenko Victor <khim@sch57.msk.ru>
- update to 3.0.6

* Wed Dec 23 1998 Khimenko Victor <khim@sch57.msk.ru>
- EAPI hack

* Mon Nov 23 1998 Khimenko Victor <khim@sch57.msk.ru>
- added imap support

* Sun Oct 11 1998 Khimenko Victor <khim@sch57.msk.ru>
- recompiled with apache 1.3.3

* Wed Oct  7 1998 Khimenko Victor <khim@sch57.msk.ru>
- update to 3.0.5

* Sun Sep 27 1998 Khimenko Victor <khim@sch57.msk.ru>
- changes for compatibility with threads library

* Thu Sep 24 1998 Khimenko Victor <khim@sch57.msk.ru>
- update to 3.0.4, changes for KSI-Linux

* Mon Aug 17 1998 Arne Coucheron <arneco@online.no>
  [3.0.3-1]
- module moved to /usr/libexec/apache to comply with latest apache rpm

* Fri Aug 07 1998 Andrea Borgia <borgia@cs.unibo.it>
  [3.0.2a]
- removed unnecessary "requires freetype" and "requires gd"
	(they're autodetected by rpm and do not force the builder
	to have them installed at compile-time)
- fixed sed substitutions (extra or missing escapes)
- added to %doc: COPYING, EXTENSION_STATUS, INSTALL, LICENSE, TODO, WISHLIST*
- added online manual as a subpackage and made it viewable through web server
	(think of a cluster of machines to see the reason why)

* Mon Jul 06 1998 Arne Coucheron <arneco@online.no>
  [3.0.1-1]

* Sun Jun 21 1998 Arne Coucheron <arneco@online.no>
  [3.0-1]
- added --with-zlib and --enable-debugger to configure
- changed name of package to mod_php

* Fri Jun 05 1998 Arne Coucheron <arneco@online.no>
  [3.0RC5-2]
- recompiled against Apache 1.3.0
- corrected source and url tags

* Tue Jun 02 1998 Arne Coucheron <arneco@online.no>
  [3.0RC5]
- this is now a standalone package thanks to the DSO capabilities of
  Apache 1.3 which make it possible to build modules outside the Apache
  source tree
