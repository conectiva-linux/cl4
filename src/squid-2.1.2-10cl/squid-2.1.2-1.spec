Summary: Squid Internet Object Cache
Summary(pt_BR): proxy/cache para www/ftp/gopher
Summary(es): proxy/cache para www/ftp/gopher
Name: squid
Version: 2.1.2
Release: 10cl
Source: squid-%{PACKAGE_VERSION}.tar.bz2
Source1: squid.init
Patch: squid-2.1.2-cl.patch
Patch1: squid-2.1.PATCH2-clientHandleIMSReply-leak.patch
Copyright: distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
URL: http://squid.nlanr.net/
BuildRoot: /var/tmp/squid

%description
Squid is a caching/proxy daemon for HTTP/FTP/Gopher
This version is built on Conectiva Linux 3.0.
Make sure you run 'squid -z' manually before running normally

%description -l pt_BR
O Squid é um servidor proxy com cache de alta performance para clientes web,
suportando FTP, gopher e HTTP. Diferentemente de softwares tradicionais de
cache o squid manipula todas as requisições em um único processo sem bloqueios,
direcionado a E/S.

Mantém meta dados e objetos freqüentemente pedidos num cache em memória
RAM. Faz cache de resoluções DNS, suporta resoluções DNS sem bloqueio e implementa
um cache negativo de requisições que falharem. Se você tem pouca memória dê uma
olhada na versão NOVM deste pacote.

Também suporta SSL, controles extensivos de acesso e registro (log) completo
das requisições. Usando o leve Protocolo de Caches Internet (ICP) ele pode
ser usado em uma hierarquia de servidores para maior economia de banda de
comunicação.

Ele consiste do programa squid (servidor principal), do programa dnsserver (para
resolução DNS), do programa ftpget (para transmissões ftp) e outras ferramentas
clientes e para gerenciamento. Quando o squid é inicializado ele dispara um
número configurável de processos dnsserver, cada um podendo executar somente
uma resolução DNS bloqueante. Isto reduz o tempo que o cache espera por
resoluções DNS.

Foi derivado do projeto Harvest, financiado pela ARPA.

%description -l es
Squid es un servidor proxy con caché de alto desempeño para clientes
web, soportando FTP, gopher y HTTP. Diferentemente de softwares
tradicionales de caché squid manipula todas las requisiciones en un
único proceso sin bloqueos, direccionado a E/S.  Mantienen metadatos
y objetos frecuentemente pedidos en uno caché en memoria RAM. Hace
caché de resoluciones DNS, soporta resoluciones DNS sin bloqueo y
implementa un caché negativo de requisiciones que fallen. Si tiene
poca memoria da un vistazo en la versión NOVM de este paquete.
También soporta SSL, controles extensivos de acceso y registro
(log) completo de las requisiciones. Usando el ligero Protocolo de
Caches Internet (ICP) puede ser usado en una jerarquía de servidores
para mayor ahorro de la banda de comunicación.  Está compuesto
del programa squid (servidor principal), del programa dnsserver
(para resolución DNS), del programa ftpget (para transmisiones ftp)
y otras herramientas clientes y para administración. Cuando squid
se inicia, dispara un número configurable de procesos dnsserver,
cada uno pudiendo ejecutar solamente una resolución DNS con poder de
bloquear. Esto reduce el tiempo que el caché espera por resoluciones
DNS.  Fue derivado del proyecto Harvest, financiado por la ARPA.

%changelog
* Sun Jun 27 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- some hacking into squid.init, since squid don't forks...

* Sun Jun 27 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed (sortof) the squid.init to use action

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscripts i18n
- added Group, Summary and %description translations

* Mon Dec 14 1998 Conectiva <dist@conectiva.com>
- fixed squid.init
- applied a memory leak patch

* Sat Dec 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- --enable-snmp

* Sat Dec 12 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Dec 11 1998 Andrew Herrick <intrep@earthlink.net>

- Changed log rotation scheme to rotate weekly and store four back logs
- Fixed log rotation mechanism to use squid -k instead of kill -USR1
- Minor cosmetic fixes to the squid.init file
- Removed rhcn changes from default package

* Thu Nov 19 1998 Andrew Herrick <intrep@earthlink.net>

- Changes to make file RHCN compatible

* Mon Oct 19 1998 Andrew Herrick <intrep@earthlink.net>

- Various fixes to start file and compile fixes for RH5.0

* Thu Oct 15 1998 Andrew Herrick <intrep@earthlink.net>

- Added ncsa_auth to doc directory

* Sat Oct 3 1998 Andrew Herrick <intrep@earthlink.net>

- fixed more doc directory problems.

* Fri Oct 2 1998 Andrew Herrick <intrep@earthlink.net>

- fixed oops in rpm spec file for doc directories.

%prep
test "${RPM_BUILD_ROOT}" && rm -fr ${RPM_BUILD_ROOT}

%setup
%patch -p1
%patch1 -p0

%build
./configure \
  --prefix=/usr \
  --exec_prefix=/usr \
  --sysconfdir=/etc/squid \
  --enable-snmp
make all
make -C auth_modules/NCSA
mkdir script
cp scripts/*.pl script

%install
mkdir -p ${RPM_BUILD_ROOT}/var/log/squid
mkdir -p ${RPM_BUILD_ROOT}/etc/squid
mkdir -p ${RPM_BUILD_ROOT}/var/spool/squid

make \
  prefix=${RPM_BUILD_ROOT}/usr \
  exec_prefix=${RPM_BUILD_ROOT}/usr \
  sysconfdir=${RPM_BUILD_ROOT}/etc/squid \
  install
make \
  prefix=${RPM_BUILD_ROOT}/usr \
  exec_prefix=${RPM_BUILD_ROOT}/usr \
  sysconfdir=${RPM_BUILD_ROOT}/etc/squid \
  install-pinger

mkdir -p ${RPM_BUILD_ROOT}/etc/rc.d/init.d
cp ${RPM_SOURCE_DIR}/squid.init ${RPM_BUILD_ROOT}/etc/rc.d/init.d/squid
chmod a+x ${RPM_BUILD_ROOT}/etc/rc.d/init.d/squid

for file in squid client dnsserver cachemgr.cgi unlinkd ; do
strip ${RPM_BUILD_ROOT}/usr/bin/${file}
done

chown -R nobody:nobody ${RPM_BUILD_ROOT}/etc/squid
chown nobody:nobody ${RPM_BUILD_ROOT}/var/log/squid
chown nobody:nobody ${RPM_BUILD_ROOT}/var/spool/squid

mkdir -p ${RPM_BUILD_ROOT}/etc/cron.weekly
install -m755 squid.logrotate ${RPM_BUILD_ROOT}/etc/cron.weekly/squid.logrotate

%files
/etc/rc.d/init.d/squid
/etc/cron.weekly/squid.logrotate
/usr/bin/RunCache
/usr/bin/RunAccel
/usr/bin/squid
/usr/bin/client
/usr/bin/dnsserver
/usr/bin/cachemgr.cgi
/usr/bin/unlinkd
/usr/bin/pinger
%dir /etc/squid
%config /etc/squid/squid.conf
/etc/squid/squid.conf.default
%config /etc/squid/mime.conf
/etc/squid/mime.conf.default
/etc/squid/mib.txt
/etc/squid/errors
/etc/squid/icons
%dir /var/spool/squid
%dir /var/log/squid
%doc doc
%doc CONTRIBUTORS COPYING COPYRIGHT CREDITS ChangeLog INSTALL README
%doc QUICKSTART TODO auth_modules/NCSA/ncsa_auth script
