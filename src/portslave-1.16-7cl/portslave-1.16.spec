Summary: Portmaster "compatible" getty
Summary(pt_BR): O portslave é um programa cliente RADIUS (Serviços de Usuário para Acesso discado Remoto).
Summary(es): portslave es un programa cliente RADIUS (Servicios de Usuario para Acceso marcado Remoto).
Name: portslave
Version: 1.16
Release: 7cl
# was .gz
Source: ftp://ftp.cistron.nl/pub/people/miquels/radius/portslave-1.16.tar.bz2
Patch0: portslave-ppp-setresource.patch
Patch1: portslave-filterid.patch
Patch2: portslave-trumpet.patch
Patch3: portslave-emumodem.patch
Patch4: portslave-servercfg.patch
Patch5: portslave-1.16-conf.patch
URL: http://miquels.www.cistron.nl/radius/portslave.html
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
BuildRoot: /var/tmp/portslave

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- removed install time echoes

* Fri May 15 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- lib fixed in server.cfg

* Fri Mar 13 1998 Bruno Lopes F. Cabral <bruno@openline.com.br>
- now using BuildRoot in the spec file
- Update to Miquel van Soorenburg's <miquels@cistron.nl> final version
  (1.16). From now on is with Erik Green <erik@mnic.net> at
  http://portslave.mnic.net/

* Tue Feb 10 1998 Bruno Lopes F. Cabral <bruno@openline.com.br>
- Integrated patch from Jon Lewis <jlewis@fdt.net> that imposes limits
  on pppd. This would make pppd kill itself before eating all the CPU
  thus avoind hanging the system. Upgrading to 2.3.x could solve this and
  many others ppp 2.2.0f problems.

* Sun Oct  5 1997 Bruno Lopes F. Cabral <bruno@openline.com.br>
- Integrated patches for Framed-Filter-ID from Jens Glaser <jens@regio.net>

* Sat May 18 1997 Bruno Lopes F. Cabral <bruno@openline.com.br>
- Changed to better handling of trumpet winsock's slip client (v 1.12)

%description
Portslave is a RADIUS (Remote Access Dial-In User Services) client program
that is designed to allow a Linux computer with a multi-port serial card 
to emulate a Livingston Portmaster 2 series terminal Server. 

This version has the filter-id patch from Jens Glaser <jens@regio.net>
and the pppd resource-limit patch from Jon Lewis <jlewis@fdt.net>.
There are many portslave and cistron radiusd patches at
http://rhoen.regio.net/~jens/

Let's wait until Erik Green <erik@mnic.net>, portslave's new maintainer
decide what will be included or not in future releases. Check his
website at http://portslave.mnic.net/

%description -l pt_BR
O portslave é um programa cliente RADIUS (Serviços de Usuário para
Acesso discado Remoto) que foi projetado para permitir que uma
máquina com Linux e uma placa multi-serial emule um servidor de
terminais Livingston Portmaster2.

Esta versão tem o patch de filter-id de Jens Glaser <jens@regio.net>
e o patch de limitação de recursos do pppd de Jon Lewis
<jlewis@fdt.net>.

%description -l es
portslave es un programa cliente RADIUS (Servicios de Usuario para
Acceso marcado Remoto) que fue proyectado para permitir que una
máquina con Linux y una tarjeta multiserial emule un servidor de
terminal Livingston Portmaster2.  Esta versión tiene el patch de
filter-id de Jens Glaser <jens@regio.net> y el patch de limitación
de recursos del pppd de Jon Lewis <jlewis@fdt.net>.

%prep
%setup -n portslave-1.16
%patch -p1 -P 0
%patch -p1 -P 1
%patch -p1 -P 2
%patch -p1 -P 3
%patch -p1 -P 4
%patch -p1 -P 5
find . -name *.orig -type f -exec rm {} \;

%build
cat > src/conf.h <<EOF
/*
 * conf.h       Configuration of paths etc. for the portslave.
 *
 */

#define RAD_ID_FILE		"/var/run/radius.id"
#define PID_DIR			"/var/run"
#define RAD_SESSIONID_FILE	"/var/log/radsession.id"
#define CONFFILE		"/etc/server.cfg"
#define MAXLINES		128

#define PATH_ROUTE		"/sbin/route"
#define PATH_IFCONFIG		"/sbin/ifconfig"
#define PATH_ARP		"/sbin/arp"
EOF

cat > src/radinit.sh <<EOF
#! /bin/sh
RADINIT=/usr/local/portslave/radinit
[ -x $RADINIT ] && $RADINIT
exit 0
EOF

cd src && make
cd ../libpsr && make
cd ../rlogin-8.10 && make
cd ../ppp-2.2.0f-radius/pppd && make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/{init.d,rc3.d}
mkdir -p $RPM_BUILD_ROOT/usr/local
DIR=$RPM_BUILD_ROOT/usr/local/portslave
install -m 555 -o root -g bin -d $DIR
install -m 555 -o root -g bin -d $DIR/filters
install -m 640 -o root -g bin src/server.cfg $RPM_BUILD_ROOT/etc/server.cfg.sample
install -m 555 -o root -g bin src/radinit.sh $RPM_BUILD_ROOT/etc/rc.d/init.d/radinit
install -m 555 -o root -g bin -s src/portslave               $DIR/portslave
install -m 555 -o root -g bin -s src/ctlportslave            $DIR/ctlportslave
install -m 555 -o root -g bin -s src/radinit                 $DIR/radinit
install -m 555 -o root -g bin -s libpsr/libpsr.so            $DIR/libpsr.so
install -m 555 -o root -g bin -s rlogin-8.10/rlogin          $DIR/rlogin
install -m 555 -o root -g bin -s ppp-2.2.0f-radius/pppd/pppd $DIR/pppd

rm -f $DIR/in.fingerd $RPM_BUILD_ROOT/etc/rc.d/rc3.d/S84radinit
ln $DIR/ctlportslave $DIR/in.fingerd
ln -s ../init.d/radinit $RPM_BUILD_ROOT/etc/rc.d/rc3.d/S84radinit

#%post
#echo "autoppp -ipx-protocol -ccp-protocol and other stuff has changed on server.cfg"
#echo "Please edit yours' and avoid problems. To enable finger support use"
#echo "finger stream tcp nowait nobody daemon /usr/sbin/tcpd /usr/local/portslave/in.fingerd"
#echo "at your inetd.conf. Remember to killall -HUP inetd after changes"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CopyRight README ChangeLog MAINTAINERS README.NET README.PPPD todo/
%dir /usr/local/portslave
%dir /usr/local/portslave/filters
/etc/server.cfg.sample
/etc/rc.d/init.d/radinit
/etc/rc.d/rc3.d/S84radinit
/usr/local/portslave/portslave
/usr/local/portslave/ctlportslave
/usr/local/portslave/radinit
/usr/local/portslave/libpsr.so
/usr/local/portslave/rlogin
/usr/local/portslave/pppd
/usr/local/portslave/in.fingerd
