Summary: Cistron RADIUS daemon (with PAM) 
Summary(pt_BR): Servidor RADIUS com muitas funções.
Summary(es): Servidor RADIUS con muchas funciones.
Name: radiusd-cistron
Version: 1.5.4.3_beta18
Release: 2cl
Source: radiusd-cistron-1.5.4.3-beta18.tar.bz2
Source1: radiusd.init
URL: http://www.miquels.cistron.nl/radius/
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
BuildRoot: /usr/tmp/radiusd

%description
RADIUS server with a lot of functions. Short overview: 

- PAM support
- Supports access based on huntgroups
- Multiple DEFAULT entries in users file
- All users file entries can optionally "fall through"
- Caches all config files in-memory
- Keeps a list of logged in users (radutmp file)
- "radwho" program can be installed as "fingerd"
- Logs both UNIX "wtmp" file format and RADIUS detail logfiles
- Supports Simultaneous-Use = X parameter. Yes, this means
  that you can now prevent double logins!

%description -l pt_BR
Servidor RADIUS com muitas funções. Visão geral:

- Suporta acesso baseado em huntgroups - Múltiplas entradas
DEFAULT no arquivo de usuários - Faz cache de todos os arquivos de
configuração em memória - Mantém uma lista dos usuários conectados
(arquivo radutmp) - O programa radwho pode ser instalado como fingerd
- Registra tanto no formato UNIX wtmp quanto no RADIUS detail -
Suporta o parâmetro Simultaneous-Use = X. Sim, isto significa
  que você pode evitar logins duplos!

%description -l es
Servidor RADIUS con muchas funciones. Visión general: - Soporta
acceso basado en huntgroups - Múltiples entradas POR DEFECTO en
el archivo de usuarios - Hace el caché de todos los archivos de
configuración en memoria - Mantienen una lista de los usuarios
conectados (archivo radutmp) - El programa radwho puede ser instalado
como fingerd - Registra tanto en el formato UNIX wtmp como en el
RADIUS detail - Soporta el parámetro Simultaneous-Use = X. ¡Sí!,
esto significa que puedes evitar logins duplos.

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed radiusd.init (me/cavassin)
- Fixed radwatch.sh (cavassin)

* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Sat Nov 21 1998 Tim Hockin <thockin@ais.net>
- Based on work by Christopher McCrory <chrismcc@netus.com>
- Build with PAM
- Included pam.d/radius
- Fixed some small errors in this spec
- Changed to build to BuildRoot
- Changed Release to "beta11" from "1"
- Included users, naslist, huntgroups, clients files, not just -dist

* Tue Oct 27 1998 Mauricio Mello de Andrade <mandrade@mma.com.br>
- Corrected the script to Start/Stop the Radius under RH5.x
- Included the script to Rotate Radius Logs under RedHat
- Checkrad Utility now works fine with Cyclades PathRas

%prep 
%setup -n radiusd-cistron-1.5.4.3
cd raddb
for f in clients users naslist huntgroups ; do cp $f $f-dist ; done
cd ..

%build
cd src
make PAM=-DPAM PAMLIB="-lpam -ldl" CFLAGS="-Wall ${RPM_OPT_FLAGS}"
cd ..

%install
# prepare $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/{,etc/{,raddb,logrotate.d,pam.d,rc.d/{,init.d,rc{0,1,2,3,4,5,6}.d}},usr/{,bin,sbin,man/{,man{1,5,8}}},var/{,log/{,radacct}}}

# make install
cd src
make install BINDIR=${RPM_BUILD_ROOT}/usr/bin SBINDIR=${RPM_BUILD_ROOT}/usr/sbin
install -m 755 radtest ${RPM_BUILD_ROOT}/usr/bin/
cd ..

# do /etc/raddb
cd raddb
install -m 640 * ${RPM_BUILD_ROOT}/etc/raddb
cd ..

# radwatch
install -m 755 scripts/radwatch ${RPM_BUILD_ROOT}/usr/sbin/

# other files
cd redhat
#install -m 555 rc.radiusd-redhat ${RPM_BUILD_ROOT}/etc/rc.d/init.d/radiusd.init
install -m 555 ${RPM_SOURCE_DIR}/radiusd.init ${RPM_BUILD_ROOT}/etc/rc.d/init.d/radiusd
install -m 644 radiusd-logrotate ${RPM_BUILD_ROOT}/etc/logrotate.d/radiusd
install -m 644 radiusd-pam ${RPM_BUILD_ROOT}/etc/pam.d/radius
cd ..

# man pages
cd doc
for i in 1 8; do
	install -m 444 *.$i ${RPM_BUILD_ROOT}/usr/man/man$i
done
install -m 444 clients.5rad ${RPM_BUILD_ROOT}/usr/man/man5/
install -m 444 naslist.5rad ${RPM_BUILD_ROOT}/usr/man/man5/
cd ..

for i in radutmp radwtmp radius.log; do
	touch ${RPM_BUILD_ROOT}/var/log/$i
	chown root.root ${RPM_BUILD_ROOT}/var/log/$i
	mkdir -p /var/log/radacct
done

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ "$1" = "0" ]; then
        /sbin/chkconfig --del radiusd
fi

%files
%doc doc/ChangeLog doc/README doc/README.pam doc/README.proxy 
%doc doc/README.usersfile doc/README.simul doc/INSTALL.OLD 
%doc doc/Makefile.README doc/README.cisco todo/ 
%doc COPYRIGHT.Cistron COPYRIGHT.Livingston

/usr/bin/*
/usr/sbin/*
/usr/man/man1/*
/usr/man/man5/*
/usr/man/man8/*
/var/log/radutmp
/var/log/radwtmp
/var/log/radius.log
%dir /var/log/radacct/
%dir /etc/raddb/
%config /etc/raddb/*
%config /etc/pam.d/radius
%config /etc/logrotate.d/radiusd
%config /etc/rc.d/init.d/radiusd
