Summary: Professional FTP daemon with apache-like configuration syntax
Summary(pt_BR): Servidor FTP profissional, com sintaxe de configuração semelhante à do apache.
Summary(es): Servidor FTP profesional, con sintaxis de configuración semejante a la del apache.
Name: proftpd
Version: 1.2.0pre3
Release: 7cl
URL: http://www.proftpd.org
# was .gz
Source0: ftp://ftp.proftpd.org/distrib/%{name}-%{version}.tar.gz
Source1: configuration.html
Source2: reference.html
Source3: proftpd.conf.conectiva

Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Provides: ftpserver
Conflicts: wu-ftpd ncftpd beroftpd
BuildRoot: /tmp/%{name}-%{version}-root

%description
ProFTPD is a highly configurable ftp daemon for unix and unix-like
operating systems.

ProFTPD is designed to be somewhat of a "drop-in" replacement for wu-ftpd.
Full online documentation is available at http://www.proftpd.org,
including a server configuration directive reference manual.

%description -l pt_BR
O ProFTPD é um servidor ftp altamente configurável para sistemas operacionais
unix.

É projetado para ser um substituto direto para o wu-ftpd.
A documentação completa está disponível em http://www.proftpd.org,
incluindo o manual de referência para as diretivas de configuração do
servidor.

%description -l es
ProFTPD es un servidor ftp altamente configurable para sistemas
operativos unix.  Está proyectado para ser un substituto directo
al wu-ftpd.  La documentación completa está disponible en
http://www.proftpd.org, incluido el manual de referencia para las
directivas de configuración del servidor.

%prep
%setup -q

#install -m644 contrib/mod_ratio.c modules/

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s \
./configure --prefix=/usr \
            --sysconfdir=/etc \
	    --localstatedir=/var/run \
            --enable-autoshadow \
            --with-modules=mod_ratio
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT/usr/{bin,sbin}
install -d $RPM_BUILD_ROOT/usr/man/{man1,man8}
#install -m600 sample-configurations/basic.conf $RPM_BUILD_ROOT/etc/proftpd.conf
install -m600 $RPM_SOURCE_DIR/proftpd.conf.conectiva $RPM_BUILD_ROOT/etc/proftpd.conf
install -m755 -s ftpcount ftpshut $RPM_BUILD_ROOT/usr/bin
install -m755 -s proftpd $RPM_BUILD_ROOT/usr/sbin
install -m644 src/proftpd.8 src/ftpshut.8 $RPM_BUILD_ROOT/usr/man/man8
install -m644 src/ftpcount.1 src/ftpwho.1 $RPM_BUILD_ROOT/usr/man/man1
install -m644 %{SOURCE1} $RPM_BUILD_DIR/%{name}-%{version}
install -m644 %{SOURCE2} $RPM_BUILD_DIR/%{name}-%{version}
ln -sf ftpcount $RPM_BUILD_ROOT/usr/bin/ftpwho
ln -sf proftpd $RPM_BUILD_ROOT/usr/sbin/in.proftpd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc changelog INSTALL README contrib/mod_ratio.c
%doc sample-configurations/virtual.conf
%doc sample-configurations/anonymous.conf
%doc *.html
%config /etc/proftpd.conf
/usr/bin/*
/usr/sbin/*
%attr(-,root,man) /usr/man/*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Updated to 1.2.0pre3

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Feb 10 1999 Marcelo Tosatti <marcelo@conectiva.com>
- fixed overflows described by Jordan Ritter

* Tue Dec 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- correções no arquivo de configuração (ortografia)
  Apontado pelo Jorge Godoy <jorge@conectiva.com>

* Mon Nov 02 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- setpath in logcount.c

* Mon Nov 02 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations, conectiva custom configuration.
- updated to 1.2.0pre1

* Wed Sep 16 1998 Arne Coucheron <arneco@online.no>
  [1.1.7pre1-1]
- added mod_ratio to compile, see the top of mod_ratio.c in the doc
  dir for usage

* Mon Aug 10 1998 Arne Coucheron <arneco@online.no>
  [1.1.6pl1-1]

* Thu Aug 06 1998 Arne Coucheron <arneco@online.no>
  [1.1.6pre4-1]

* Sat Aug 01 1998 Arne Coucheron <arneco@online.no>
  [1.1.6pre2-1]

* Thu Jul 23 1998 Arne Coucheron <arneco@online.no>
  [1.1.5pl4-1]
- making use of shadow libraries
  (Thanks to Mike McHendry <mmchen@ally.minn.net> for the hint)
- added beroftpd to Conflicts:
- added configuration and reference docs to the package

* Sun Jun 28 1998 Arne Coucheron <arneco@online.no>
  [1.0.3pl1-2]
- using $RPM_OPT_FLAGS
- using %%{name} and %%{version} macros
- using %defattr macro in filelist, ordinary users can build now 
- using install -d instead of mkdir -p
- made proftpd.conf chmod 600 for security
- added -q parameter to %setup
- added %config to /etc/proftpd.conf in filelist
- added Conflicts: wu-ftpd ncftpd
- installing util programs in /usr/bin instead of /usr/sbin
- changed name of spec file to proftpd.spec

* Wed May 6 1998 Vladimir Ivanov <vlad@elis.tasur.edu.ru>
- Fixed bug in mod_auth.c
- Initial RPM release
