Summary: Dynamic Host Control Protocol Server and Clients.
Summary(pt_BR): Servidor DHCP (Protocolo de configuração dinâmica de hosts)
Summary(es): Servidor DHCP (Protocolo de configuración dinámica de hosts)
Name: dhcp
%define	version	2.0b1pl27
Version: %{version}
Release: 2cl
Copyright: distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
# was .gz
Source0: ftp://ftp.isc.org/isc/dhcp/dhcp-%{version}.tar.bz2
Source2: dhcpd.init
Patch: dhcp-buildroot.conectiva.patch
BuildRoot: /var/tmp/dhcpd-root
Obsoletes: dhcpd

%description
This is the second release of the dhcp package from the Internet Software
Consortium. It provides a server and a relay agent.

#%package client
#Summary: DHCP client
#Group: Networking/Daemons
#Obsoletes: dhcpcd

#%description client
#This is the second reload of the dhcppackage from the Internet Software
#Consortium. It provides a client.

%description -l pt_BR
DHCP permite que hosts numa rede TCP/IP requisitem e tenham seus
endereços IP alocados dinamicamente, permite também descobrir
informações sobre a rede em que estão conectados.  BOOTP provê
uma funcionalidade similar, com certas restrições. Este servidor
também atende aquelas requisições. Esta versão é ainda considerada
um software BETA.

%description -l es
DHCP permite que hosts en una red TCP/IP soliciten y tengan sus
direcciones IP alocadas dinámicamente, permite también descubrir
información sobre la red en que están conectados.  BOOTP provee una
funcionalidad similar, con ciertas restricciones. Este servidor
también las atiende. Esta versión aún está considerada como un
software BETA.

%prep
%setup -q
%patch -p1 -b .buildroot

%build
./configure
make CC="gcc -pipe" DEBUG="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/var/dhcpd
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/sbin

RPM_BUILD_ROOT=${RPM_BUILD_ROOT} make install

install -m 0755 $RPM_SOURCE_DIR/dhcpd.init \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/dhcpd

# the dhcp Makefiles are too stupid to even install man pages properly
rm -rf $RPM_BUILD_ROOT/usr/man
find . -name "*.[58]" | while read file; do
    ext=`echo $file | sed 's/.*\.//'`
    echo $file - $ext
    mkdir -p $RPM_BUILD_ROOT/usr/man/man$ext
    install -m 644 $file $RPM_BUILD_ROOT/usr/man/man$ext
done

#%post
#/sbin/chkconfig --add dhcpd

%postun
if [ $1 = 0 ]; then
    # execute this only if we are NOT doing an upgrade
    /sbin/chkconfig --del dhcpd 
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README RELNOTES TODO doc/*
%dir /var/dhcpd
/etc/rc.d/init.d/dhcpd
/usr/sbin/dhcpd
/usr/sbin/dhcrelay
/usr/man/man5/dhcpd.conf.5
/usr/man/man5/dhcpd.leases.5
/usr/man/man5/dhcp-options.5
/usr/man/man8/dhcpd.8
/usr/man/man8/dhcrelay.8

#%files client
#%defattr(-,root,root)
#%doc CHANGES README RELNOTES TODO doc/*
#%dir /var/dhcpd
#/etc/dhclient-script
#/sbin/dhclient
#/usr/man/man5/dhclient.conf.5
#/usr/man/man5/dhclient.leases.5
#/usr/man/man8/dhclient.8
#/usr/man/man8/dhclient-script.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start
- updated from 2.0b1pl18 to 2.0b1pl27
- fixed dhcp-buildroot.conectiva.patch

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 12 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 12 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- upgraded to 2.0b1pl18
- initscript i18n
- added es translations

* Tue Oct 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- dhcpd.init internationalized and translated to pt_BR

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- modify dhcpd.init to exit if /etc/dhcpd.conf is not present

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- Upgraded to 2.0b1pl6 (patch1 no longer needed).

* Thu Jun 11 1998 Erik Troan <ewt@redhat.com>
- applied patch from Chris Evans which makes the server a bit more paranoid
  about dhcp requests coming in from the wire

* Mon Jun 01 1998 Erik Troan <ewt@redhat.com>
- updated to dhcp 2.0b1pl1
- got proper man pages in the package

* Tue Mar 31 1998 Erik Troan <ewt@redhat.com>
- updated to build in a buildroot properly
- don't package up the client, as it doens't work very well <sigh>

* Tue Mar 17 1998 Bryan C. Andregg <bandregg@redhat.com>
- Build rooted and corrected file listing.

* Mon Mar 16 1998 Mike Wangsmo <wanger@redhat.com>
- removed the actual inet.d links (chkconfig takes care of this for us)
  and made the %postun section handle upgrades.

* Mon Mar 16 1998 Bryan C. Andregg <bandregg@redhat.com>
- First package.
