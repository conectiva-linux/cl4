%define mysqlver           3.21.30
%define DBIperlbin       0.93
%define mysqlDBIperlbin 1.825
%define release            5cl
%define perldir            5.005

Summary: MySQL database server
Summary(pt_BR): Servidor de banco de dados MySQL
Summary(es):        MSQL database server
Name: mysql
Version: %{mysqlver}
Release: %{release}
Source0: http://www.tcx.se/mysql-%{mysqlver}.tar.bz2
Source1: mysql-init-db
Source2: mysql.logrotate
Source3: mysql.init
Source4: mysql-faqs-1.0.tgz
Source5: manual.ps
Patch: mysql-3.21.30-glibc21.patch
URL: http://http://www.tcx.se/
Copyright: distributable
Group: Applications/Databases
Group(pt_BR): Aplicações/Banco de Dados
Group(es): Aplicaciones/Bancos de Datos
Icon: mysql.gif
PreReq: chkconfig
Requires: readline libtermcap
ExclusiveArch: i386 sparc alpha
BuildRoot: /var/tmp/mysql-%{mysqlver}-root

%description
MySQL is a SQL (Structured Query Language) database server. MySQL
was written by Michael (monty) Widenius. See the CREDITS file in the
distribution for more credits for MySQL and related things.

%description -l pt_BR
MySQL é um servidor de banco de dados SQL (linguagem estruturada de
consulta). O MySQL foi escrito por Michael (monty) Widenius. Veja
o arquivo CREDITS para mais informações.

%description -l es
MySQL is a SQL (Structured Query Language) database server. MySQL
was written by Michael (monty) Widenius. See the CREDITS file in the
distribution for more credits for MySQL and related things.


%package -n mysql-bench
Summary: MySQL - Benchmarks
Summary(pt_BR): Testes de performance do MySQL
Summary(es):   MySQL - Benchmarks
Release: %{release}
Group: Applications/Benchmarks
Group(pt_BR): Aplicações/Teste de Performance
Group(es): Aplicaciones/Teste de Performance
Requires: mysql perl >= 5.004

%description -n mysql-bench
MySQL is a SQL (Structured Query Language) database server. MySQL
was written by Michael (monty) Widenius. See the CREDITS file in the
distribution for more credits for MySQL and related things.

This package contains MySQL benchmark scripts and data.

%description -l pt_BR -n mysql-bench
Este pacote contém scripts e dados para testes de performance
do MySQL.

%description -l es -n mysql-bench
MySQL is a SQL (Structured Query Language) database server. MySQL
was written by Michael (monty) Widenius. See the CREDITS file in the
distribution for more credits for MySQL and related things.

This package contains MySQL benchmark scripts and data.


%package -n mysql-devel
Summary:  MySQL - Development header files and libraries
Summary(pt_BR): Arquivos de inclusão e bibliotecas de desenvolvimento
Summary(es):   MySQL - Development header files and libraries
Release: %{release}
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: mysql = %{mysqlver}

%description -n mysql-devel
MySQL is a SQL (Structured Query Language) database server. MySQL
was written by Michael (monty) Widenius. See the CREDITS file in the
distribution for more credits for MySQL and related things.

This package contains the development header files and libraries
necessary to develop client applications.

%description -l pt_BR -n mysql-devel
Este pacote contém os arquivos de inclusão e as bibliotecas necessárias
para desenvolver aplicações.

%description -l es -n mysql-devel
MySQL is a SQL (Structured Query Language) database server. MySQL
was written by Michael (monty) Widenius. See the CREDITS file in the
distribution for more credits for MySQL and related things.

This package contains the development header files and libraries
necessary to develop client applications.


%package -n DBI-perl-bin
Summary:  DBI-DBD - Perl Module
Summary(pt_BR): Modulo Perl DBI-DBD
Summary(es):   DBI-DBD - Perl Module
Version:  %{DBIperlbin}
Release:  %{release}
Group: Applications/Databases
Group(pt_BR): Aplicações/Banco de Dados
Group(es): Aplicaciones/Bancos de Datos
Requires: perl >= 5.004

%description -n DBI-perl-bin
DBI - The Perl Database Interface by Tim Bunce.
Copyright (c) 1994,1995,1996,1997  Tim Bunce  England

See COPYRIGHT section in DBI.pm for usage and distribution rights.

WARNING:

    THIS IS ALPHA SOFTWARE. It is *only* 'Alpha' because the
    interface (API) is not finalised. The Alpha status does
    not reflect code quality or stability.

QUICK START GUIDE:

    The DBI requires one or more 'driver' modules to talk to databases.
    Check that a DBD::* module exists for the database you wish to use.

%description -l pt_BR -n DBI-perl-bin
DBI - A Interface Perl para banco de dados, por Tim Bunce.

AVISO:

    ESTE É UM SOFTWARE ALFA. É somente considerada em estado alfa,
    porque a interface (API) não está finalizada. Este estado não
    se reflete na qualidade ou estabilidade do código.

    O DBI requer um ou mais 'drivers' para comunicar-se com o banco de
    dados. Procure por um módulo DBD::* para o banco de dados que você
    deseja usar.

%description -l es -n DBI-perl-bin
DBI - The Perl Database Interface by Tim Bunce.
Copyright (c) 1994,1995,1996,1997  Tim Bunce  England

See COPYRIGHT section in DBI.pm for usage and distribution rights.

WARNING:

    THIS IS ALPHA SOFTWARE. It is *only* 'Alpha' because the
    interface (API) is not finalised. The Alpha status does
    not reflect code quality or stability.

QUICK START GUIDE:

    The DBI requires one or more 'driver' modules to talk to databases.
    Check that a DBD::* module exists for the database you wish to use.


%package -n DBI-monitor
Summary: Interactive shell with readline for DBI
Summary(pt_BR): Shell interativa com readline para a DBI
Summary(es):   Interactive shell with readline for DBI
Release: %{release}
Group: Applications/Databases
Group(pt_BR): Aplicações/Banco de Dados
Group(es): Aplicaciones/Bancos de Datos
Requires: DBI-perl-bin >= 0.93

%description -n DBI-monitor
dbimon lets you talk to a running SQL server via the
database independent Perl interface DBI. dbimon was
inspired by Andreas Koenig's pmsql and borrows both design
ideas and code from it. Thus the look and feel is almost
identical to pmsql, in particular the following holds:

The output is formatted much in the same way as by the
msql or mysql monitor (see below), the msqlexport
command and the relshow (mysqlshow) programs, which
are coming with msql or mysql.

The additional capability is a connection to a
readline interface (if available) and a pipe to your
favorite pager.

Additionally you may switch between hosts and
databases within one session and you don't have to
type the nasty \g or ; (a trailing \g, \q, and \p will
be ignored).

%description -l pt_BR -n DBI-monitor
O dbimon é um shell que permite a intereção com um servidor SQL, via
interface Perl DBI de acessao a banco de dados.  Ele foi inspirado
no utilitário pmsql.

%description -l es -n DBI-monitor
dbimon lets you talk to a running SQL server via the
database independent Perl interface DBI. dbimon was
inspired by Andreas Koenig's pmsql and borrows both design
ideas and code from it. Thus the look and feel is almost
identical to pmsql, in particular the following holds:

The output is formatted much in the same way as by the
msql or mysql monitor (see below), the msqlexport
command and the relshow (mysqlshow) programs, which
are coming with msql or mysql.

The additional capability is a connection to a
readline interface (if available) and a pipe to your
favorite pager.

Additionally you may switch between hosts and
databases within one session and you don't have to
type the nasty \g or ; (a trailing \g, \q, and \p will
be ignored).


%package -n mysql-DBI-perl-bin
Summary: MySQL Perl Interface
Summary(pt_BR): Interface Perl para o MySQL
Summary(es):   MySQL Perl Interface
Version: %{mysqlDBIperlbin}
Release: %{release}
Group: Applications/Databases
Group(pt_BR): Aplicações/Banco de Dados
Group(es): Aplicaciones/Bancos de Datos
Requires: DBI-perl-bin >= 0.93

%description -n mysql-DBI-perl-bin
M(y)sql.pm and DBD::mSQL(mysql) implement two different approaches to
communicate with an mSQL or mysql server. DBD::mSQL(mysql) is built
upon the DBI, the generic Perl Database Interface. It brings you an
identical interface to a broad variety of databases and is in this
regard comparable to ODBC. The advantage of the DBI approach is
portability and interoperability. M(y)sql.pm are the elder species.
They were written before DBI was available but inspired by an early
draft of the DBI specification. As they have been circulating longer
they are more mature and pretty stable. They're also more complete
than DBD::mSQL and DBD::mysql.

As of Msql-Mysql-modules 1.1815, we consider DBD::mSQL and DBD::mysql
superior over MsqlPerl and MysqlPerl: They are sufficiently stable
(there´s only one known problem in DBI itself and it's announced to
be fixed in DBI 0.91) and definitely faster. Anyways, you have to decide
on your own about the trade-offs.

%description -l pt_BR -n mysql-DBI-perl-bin
Interface Perl para o MySQL, via DBI, que é a interface genérica do Perl
para banco de dados.

%description -l es -n mysql-DBI-perl-bin
M(y)sql.pm and DBD::mSQL(mysql) implement two different approaches to
communicate with an mSQL or mysql server. DBD::mSQL(mysql) is built
upon the DBI, the generic Perl Database Interface. It brings you an
identical interface to a broad variety of databases and is in this
regard comparable to ODBC. The advantage of the DBI approach is
portability and interoperability. M(y)sql.pm are the elder species.
They were written before DBI was available but inspired by an early
draft of the DBI specification. As they have been circulating longer
they are more mature and pretty stable. They're also more complete
than DBD::mSQL and DBD::mysql.

As of Msql-Mysql-modules 1.1815, we consider DBD::mSQL and DBD::mysql
superior over MsqlPerl and MysqlPerl: They are sufficiently stable
(there´s only one known problem in DBI itself and it's announced to
be fixed in DBI 0.91) and definitely faster. Anyways, you have to decide
on your own about the trade-offs.


%package -n mysql-client
Summary: MySQL - Client
Summary(pt_BR): Cliente MySQL
Summary(es):  MySQL - Client
Release: %{release}
Group: Applications/Databases
Group(pt_BR): Aplicações/Banco de Dados
Group(es): Aplicaciones/Bancos de Datos

%description -n mysql-client
MySQL is a SQL (Structured Query Language) database server. MySQL
was written by Michael (monty) Widenius. See the CREDITS file in the
distribution for more credits for MySQL and related things.

This package contains just the MySQL client.

%description -l pt_BR -n mysql-client
Este pacote contém apenas o cliente MySQL.

%description -l es -n mysql-client
MySQL is a SQL (Structured Query Language) database server. MySQL
was written by Michael (monty) Widenius. See the CREDITS file in the
distribution for more credits for MySQL and related things.

This package contains just the MySQL client.


%ifarch i386
%define runarch i386
%endif

%ifarch sparc
%define runarch sparc
%endif

%ifarch alpha
%define runarch alpha
%endif

%prep
%setup -n mysql-%{mysqlver}
mkdir FAQs
cd FAQs
tar zxvf $RPM_SOURCE_DIR/mysql-faqs-1.0.tgz
cd ..
cp $RPM_SOURCE_DIR/manual.ps Docs/

%patch -p1  
%build
CFLAGS="$RPM_OPT_FLAGS -D_LINUX_TYPES_H" CXX=g++ \
CXXFLAGS="$RPM_OPT_FLAGS -D_LINUX_TYPES_H" LDFLAGS=-s ./configure \
   --without-debug \
   --without-readline \
   --enable-shared \
   --with-unix-socket-path=/var/lib/mysql/mysql.sock \
   --prefix=/ \
   --exec-prefix=/usr \
   --libexecdir=/usr/sbin \
   --bindir=/usr/bin \
   --sbindir=/usr/sbin \
   --infodir=/usr/info \
   --sysconfdir=/etc \
   --datadir=/usr/share \
   --mandir=/usr/man \
   --localstatedir=/var/lib/mysql \
   --includedir=/usr/include \
   --libdir=/usr/lib
make

%install
rm -rf $RPM_BUILD_ROOT
for I in etc/{logrotate.d,profile.d,rc.d/init.d} var/lib/mysql \
   usr/{lib/perl5/%{runarch}-linux/%{perldir},man/man1} usr/info ; do
   mkdir -p $RPM_BUILD_ROOT/$I
done

make prefix=$RPM_BUILD_ROOT \
   exec-prefix=$RPM_BUILD_ROOT/usr \
   libexecdir=$RPM_BUILD_ROOT/usr/sbin \
   infodir=$RPM_BUILD_ROOT/usr/info \
   sysconfdir=$RPM_BUILD_ROOT/etc \
   datadir=$RPM_BUILD_ROOT/usr/share \
   mandir=$RPM_BUILD_ROOT/usr/man \
   localstatedir=$RPM_BUILD_ROOT/var/lib/mysql \
   includedir=$RPM_BUILD_ROOT/usr/include \
   bindir=$RPM_BUILD_ROOT/usr/bin \
   sbindir=$RPM_BUILD_ROOT/usr/sbin \
   libdir=$RPM_BUILD_ROOT/usr/lib \
   benchdir=$RPM_BUILD_ROOT/var/lib/sql-bench \
   PREFIX=$RPM_BUILD_ROOT/usr \
   INSTALLMAN1DIR=$RPM_BUILD_ROOT/usr/man/man1 \
   install-strip

install -m755 $RPM_SOURCE_DIR/mysql.init $RPM_BUILD_ROOT/etc/rc.d/init.d/mysql
install -m644 $RPM_SOURCE_DIR/mysql.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/mysql
install -m644 $RPM_SOURCE_DIR/mysql-init-db $RPM_BUILD_ROOT/var/lib/mysql/mysql-db.init
install -m644 Docs/mysql.info $RPM_BUILD_ROOT/usr/info
gzip -n -f9 $RPM_BUILD_ROOT/usr/info/mysql.info*

(cd $RPM_BUILD_ROOT/usr/lib; \
	ln -sf libmysqlclient.so.%{mysqlver} libmysqlclient.so.4)

(cd $RPM_BUILD_ROOT/usr/lib/perl5/site_perl; \
	ln -sf %{runarch}-linux/auto/Mysql/Mysql.so Mysql.so)

strip $RPM_BUILD_ROOT/usr/lib/* ||

# Added to make this file use /usr/bin/perl, instead of /usr/bin/perl5
TEMPFILE=`mktemp /tmp/compare-results.XXXXXX`
cd $RPM_BUILD_ROOT/var/lib/sql-bench
sed s/perl5/perl/g compare-results > $TEMPFILE
mv -f $TEMPFILE compare-results
chmod +x compare-results

%post
/sbin/ldconfig
/sbin/install-info /usr/info/mysql.info.gz /usr/info/dir
#/sbin/chkconfig --add mysql
#if [ ! -d /var/lib/mysql/mysql ]; then
#  /usr/sbin/mysqld -Sg --log=/var/log/mysql.log > /dev/null 2>&1 &
#  sleep 1
#  mysqladmin create mysql
#  mysql mysql < /var/lib/mysql/mysql-db.init
#  mysqladmin create test
#  mysqladmin shutdown
#fi
#/etc/rc.d/init.d/mysql start >/dev/null 2>&1

#%pre
#if [ -x /usr/bin/mysqladmin ]; then
#  if mysqladmin status >/dev/null 2>&1; then
#   /etc/rc.d/init.d/mysql stop;
#  fi
#fi

%preun
if [ $1 = 0 ]; then
  /sbin/install-info --delete /usr/info/mysql.info.gz /usr/info/dir
fi
#if [ -x /usr/bin/mysqladmin ]; then
#  if mysqladmin status >/dev/null 2>&1; then
#   /etc/rc.d/init.d/mysql stop;
#  fi
#fi
chkconfig --del mysql

%postun
/sbin/ldconfig

%post -n mysql-client
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) %doc PUBLIC README
%attr(-,root,root) %doc Docs/manual.html
%attr(-,root,root) %doc Docs/manual.ps
%attr(-,root,root) %doc Docs/manual.html
%attr(-,root,root) %doc Docs/manual.txt
%attr(-,root,root) %doc Docs/manual.texi
%attr(-,root,root) %doc Docs/manual_toc.html
%attr(-,root,root) %doc FAQs/mysql-faqs-1.0/mysql-faq_toc.html
%attr(-,root,root) %doc FAQs/mysql-faqs-1.0/mysql-faq.html
%attr(-,root,root) %doc FAQs/mysql-faqs-1.0/mysql-faq.info
%attr(-,root,root) %doc FAQs/mysql-faqs-1.0/mysql-faq.ps
%attr(-,root,root) %doc FAQs/mysql-faqs-1.0/mysql-faq.texi
%attr(-,root,root) %doc FAQs/mysql-faqs-1.0/mysql-faq.txt
%attr(-,root,root) %config /etc/logrotate.d/mysql
%attr(-,root,root) %config /etc/rc.d/init.d/mysql

%attr(-,root,root) /usr/bin/add_file_priv
%attr(-,root,root) /usr/bin/add_long_password
%attr(-,root,root) /usr/bin/comp_err
%attr(-,root,root) /usr/bin/isamchk
%attr(-,root,root) /usr/bin/isamlog
%attr(-,root,root) /usr/bin/msql2mysql
%attr(-,root,root) /usr/bin/mysql
%attr(-,root,root) /usr/bin/mysqlaccess
%attr(-,root,root) /usr/bin/mysqladmin
%attr(-,root,root) /usr/bin/mysqlbug
%attr(-,root,root) /usr/bin/mysqldump
%attr(-,root,root) /usr/bin/mysqlimport
%attr(-,root,root) /usr/bin/mysqlshow
%attr(-,root,root) /usr/bin/perror
%attr(-,root,root) /usr/bin/replace
%attr(-,root,root) /usr/bin/safe_mysqld
%attr(-,root,root) /usr/bin/which1
%attr(-,root,root) /usr/bin/zap

%attr(-,root,root) /usr/info/mysql.info.gz

%attr(-,root,root) /usr/lib/libmysqlclient.so
%attr(-,root,root) /usr/lib/libmysqlclient.so.4
%attr(-,root,root) /usr/lib/libmysqlclient.so.%{mysqlver}

%attr(-,root,man) /usr/man/man1/mysql.1

%attr(-,root,root) /usr/sbin/mysqld

%attr(-,root,root) %dir /usr/share/mysql
%attr(-,root,root) /usr/share/mysql/czech
%attr(-,root,root) /usr/share/mysql/dutch
%attr(-,root,root) /usr/share/mysql/english
%attr(-,root,root) /usr/share/mysql/french
%attr(-,root,root) /usr/share/mysql/german
%attr(-,root,root) /usr/share/mysql/norwegian
%attr(-,root,root) /usr/share/mysql/norwegian-ny
%attr(-,root,root) /usr/share/mysql/polish
%attr(-,root,root) /usr/share/mysql/portuguese
%attr(-,root,root) /usr/share/mysql/russian
%attr(-,root,root) /usr/share/mysql/spanish
%attr(-,root,root) /usr/share/mysql/swedish

%attr(-,root,root) %dir /var/lib/mysql
%attr(-,root,root) /var/lib/mysql/mysql-db.init

%files -n mysql-bench
%attr(644,root,root) %doc bench/README
%attr(-,root,root) /var/lib/sql-bench

%files -n mysql-client
%attr(-,root,root) /usr/bin/msql2mysql
%attr(-,root,root) /usr/bin/mysql
%attr(-,root,root) /usr/bin/mysqlaccess
%attr(-,root,root) /usr/bin/mysqladmin
%attr(-,root,root) /usr/bin/mysqlbug
%attr(-,root,root) /usr/bin/mysqldump
%attr(-,root,root) /usr/bin/mysqlimport
%attr(-,root,root) /usr/bin/mysqlshow
%attr(-,root,root) /usr/lib/libmysqlclient.so 
%attr(-,root,root) /usr/lib/libmysqlclient.so.4
%attr(-,root,root) /usr/lib/libmysqlclient.so.%{mysqlver}
%attr(-,root,man) /usr/man/man1/mysql.1

%files -n mysql-devel
%attr(-,root,root) /usr/lib/mysql
%attr(-,root,root) /usr/include/mysql

%files -n mysql-DBI-perl-bin
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBD/mysql/mysql.bs
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBD/mysql/mysql.so
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/Mysql/Mysql.bs
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/Mysql/Mysql.so
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/DBD/mysql.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/Bundle/Mysql.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/Mysql/Statement.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/Mysql.pm
%attr(-,root,man) /usr/man/man1/pmysql.1
%attr(-,root,root) /usr/bin/pmysql

%files -n DBI-monitor
%attr(-,root,man) /usr/man/man1/dbimon.1
%attr(-,root,root) /usr/bin/dbimon

%files -n DBI-perl-bin
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/DBI.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/DBD/ExampleP.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/DBD/NullP.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/DBD/Sponge.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/DBI/DBD.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/DBI/FAQ.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/DBI/W32ODBC.pm
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBI/DBI.so
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBI/DBI.bs
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBI/DBIXS.h
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBI/Driver.xst
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBI/DriverDB.xst
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBI/DriverST.xst
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBI/dbd_xsh.h
%attr(-,root,root) /usr/lib/perl5/site_perl/5.005/%{runarch}-linux/auto/DBI/dbi_sql.h

%changelog
* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start
- sources recompressed

* Wed Jun  2 1999 Marcelo Tosatti <marcelo@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- fixed problems with glibc 2.1

* Sun Apr 18 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition
- Removed serial tag
- Adjusted some files in %files section (They were using the old 5.004 Perl dir)

* Tue May 12 1998 Arne Coucheron <arneco@online.no>
- updated to 3.21.30-1
- added a serial tag
- changes to mysql.init (check that networking is up)

* Sun May 10 1998 Arne Coucheron <arneco@online.no>
- updated to 3.21.29-2
- figured out the log thingie, it was quite easy actually. :-)
- some changes to spec file to allow it be buildable with newer rpm versions

* Fri Apr 10 1998 Arne Coucheron <arneco@online.no>
- updated to 3.21.29-1

* Wed Apr 01 1998 Arne Coucheron <arneco@online.no>
- updated to 3.21.28-1

* Sun Mar 29 1998 Arne Coucheron <arneco@online.no>
- updated to 3.21.27-1

* Wed Mar 25 1998 Arne Coucheron <arneco@online.no>
- updated to 3.21.26-1
- mysql.info is in, installing it manually
- added func table to mysql-db-init
- changes to the compiler flags to avoid core dump on mysqld startup
- some cosmetic changes to mysql.init
- be aware that the log file for mysql has for some reason moved to
  /var/lib/mysql/'hostname'.log, so the logrotate has in reality no effect.
  I have not yet found any solution to this, so if anyone has any hints,
  please let me know.

* Sat Feb 28 1998 Arne Coucheron <arneco@online.no>
- updated to 3.21.25-1
- major changes to the spec file
- this distribution is now more or less the same as the one at the tcx site,
  except for some small changes and that this one uses buildroot
- can't make the info files, so leaving them out for now

* Wed Feb 04 1998 Arne Coucheron <arneco@online.no>
- updated to 3.21.23-1
- using %attr macros
- changed the mysql logrotate file so it doesn't kill off crond
- various other fixes and cleanups
