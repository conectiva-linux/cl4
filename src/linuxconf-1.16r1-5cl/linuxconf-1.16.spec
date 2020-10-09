Summary: An extremely capable system configuration tool.
Summary(pt_BR): Configura��o do sistema via interfaces texto/console, X ou Web
Summary(es): Configuraci�n del sistema v�a interfaces texto/consola, X o Web
Name: linuxconf
Version: 1.16r1
Release: 5cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp.solucorp.qc.ca:/pub/linuxconf/devel/linuxconf-1.16r1.src.tar.bz2
Url: http://www.solucorp.qc.ca/linuxconf/
Source1: linuxconf-1.13r10.imagensCNC.tar.gz
Source2: lc-1.16r1-out
Patch: linuxconf-1.16-conectiva.patch
Patch1: vhosts.patch 
Patch2: linuxconf-sysv.patch
Patch3: linuxconf-pam.patch
Patch4: linuxconf-rpm-postinstall.patch

BuildRoot: /tmp/linuxconf-root
provides: LINUXCONFAPIREV13

%description
Linuxconf is an extremely capable system configuration tool.  Linuxconf
provides four different interfaces for you to choose from:  command line,
character-cell (like the installation program), an X Window System based
GUI and a web-based interface.  Linuxconf can manage a large proportion
of your system's operations, including networking, user accounts, file
systems, boot parameters, and more.

Linuxconf will simplify the process of configuring your system.  Unless
you are completely happy with configuring your system manually, you should
install the linuxconf package and use linuxconf instead.

%description -l pt_BR
Linuxconf fornece uma interface de navega��o f�cil que � acess�vel
via console/texto, web e X.

Linuxconf gerencia:

Rede:
        Informa��es da m�quina: Endere�o IP, nome da m�quina,
        etc.  Aloca��o de sub-redes IP Resolu��o DNS Roteamento
        NIS Configura��o de interface IPX PPP e SLIP Sistemas de
        arquivos NFS Bases de dados DNS Resolu��o Reversa Sendmail
        Dom�nios virtuais para e-mail UUCP IP Aliases Servidor
        DHCP/BOOTP Servidor RARP Firewall de Entrada Firewall de
        Saida Firewall para Bloqueio Mascaramento IP Contabilidade
        de pacotes Gateway de Mail para Fax
Contas de Usu�rios:
        Gerenciamento de usu�rios e grupos Contas PPP Contas SLIP
        Contas UUCP Contas somente POP Contas de email para dom�nios
        virtuais Aliases de email para dom�nios normais e virtuais
        Pol�ticas para senhas e contas de usu�rios Interpretadores
        de comandos dispon�veis para usu�rios Gerenciamento da
        crontab Gerenciamento de senhas tipo shadow
Sistemas de Arquivos:
        Gerenciamento de parti��es locais (/etc/fstab) Gerenciamento
        de volumes NFS (Gerenciamento de volumes samba est� quase
        pronto) Gerenciamento de parti��es swap Quotas de usu�rios
        e grupos Permiss�es de arquivos
Modo de Inicializa��o:
        Configura��o do Lilo Modo default de inicializa��o Defini��es
        de n�veis de execu��o (runlevels)

E mais...

%description -l es
Linuxconf ofrece una interface de navegaci�n f�cil que es accesible
v�a pantalla/texto, web y X.  Linuxconf administra: Red: Informaci�n
de la m�quina: Direcci�n IP, nombre de la m�quina, etc., alocaci�n
de subredes IP, resoluci�n DNS, rutado, NIS, configuraci�n de la
interface IPX, marcados PPP y SLIP, sistemas de archivos NFS, bases
de datos DNS, resoluci�n reversa, sendmail dominios virtuales de
e-gmail, UUCP, motes de IP, servidor DHCP/BOOTP, servidor RARP,
firewall de entrada, firewall de salida, firewall de bloqueo,
enmascaramiento de IP, contabilidad de paquetes y ruteador de email
para fax.  Cuentas de usuarios: Administraci�n de usuarios y grupos,
cuentas PPP, cuentas SLIP, cuentas UUCP, cuentas solamente POP,
cuentas de e-mail para dominios virtuales, motes de e-mail para
dominios normales y virtuales, pol�ticas para contrase�as y cuentas
de usuarios, interpretadores de comandos disponibles para usuarios,
administraci�n de la crontab y administraci�n de contrase�as tipo
shadow.  Sistemas de archivos: Administraci�n de particiones locales
(/etc/fstab), administraci�n de vol�menes NFS (el administrador de
vol�menes samba est� casi listo), administraci�n de particiones
swap, cuotas de usuarios y grupos, y permisos de archivos.
Modo de arranque: Configuraci�n del Lilo, modo de arranque padr�n
y definiciones de niveles de ejecuci�n (runlevels).  Y m�s...

%package devel
Summary: The tools needed for developing linuxconf modules.
Summary(pt_BR): Arquivos para desenvolvimento no linuxconf
Summary(es): Archivos para desarrollo en linuxconf
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
Linuxconf is an extremely capable system configuration tool.
It provides a variety of interfaces through which you can configure
your Linux system and manage a large proportion of the system's
operations.

This package provides the components necessary for developing
Linuxconf modules outside of the linuxconf source tree and/or
developing stand-alone utilities using the linuxconf interface
toolkit.

Install linuxconf-devel if you want to develop Linuxconf modules.
You must also have linuxconf installed.

%description -l pt_BR devel
Este pacote fornece os componentes necess�rios ao desenvolvimento
de m�dulos para o linuxconf. Tamb�m � necess�rio ao desenvolvimento
de utilit�rios independentes usando o conjunto de componentes
de interface com o usu�rio do linuxconf.

%description -l es devel
Este paquete ofrece los componentes necesarios al desarrollo
de m�dulos para el Configurador Linux. Tambi�n es �til para el
desarrollo de utilitarios independientes usando el conjunto de
componentes de interface con el usuario del Configurador Linux.

%prep

%setup -n linuxconf-1.16r1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%setup -T -D -a 1
%patch -p1 
%build 

# remove other languages/distributions related files - aur�lio
rm -r `cat $RPM_SOURCE_DIR/lc-1.16r1-out`

# 7:30, i'm too lazy to regenerate my patch with the correct translation 
# stuff. Remove this lines if you are building a normal tree.
#	- Marcelo
cd misc 
make 
cd ../translate
make
cd ../modules/apache
make msg 
cd ../../



make
%install

export RPM_BUILD_ROOT
make install_for_rpm

mkdir -p $RPM_BUILD_ROOT/var/log
for file in htmlaccess netconf boot ; do
        touch $RPM_BUILD_ROOT/var/log/$file.log 
        chmod 600 $RPM_BUILD_ROOT/var/log/$file.log
done

make install-devel
%clean


if [ "$RPM_BUILD_ROOT" = "/tmp/linuxconf-root" ] ; then
	rm -fr /tmp/linuxconf-root
fi

%pre

OLDINSTALL=/usr/lib/linuxconf/help.eng/notices/01-oldinstall
INITTABREPLACE=/usr/lib/linuxconf/uninstall/inittab.replace
UPGRADE="NO"



echo "#### pre install script" >>/tmp/linuxconf-rpminstall.log
date >>/tmp/linuxconf-rpminstall.log

log(){
	echo $* >>/tmp/linuxconf-rpminstall.log
	$*
}

# Check for tarball installation
if [ -f /usr/lib/linuxconf/conf.daemons ] ; then
	UPGRADE="YES"
fi

if [ -f /usr/lib/linuxconf/std/conf.daemons ] ; then
	UPGRADE="YES"
fi

# Check for old 1.9r22 RPM installation
if [ -f /usr/lib/linuxconf/install/doinst.sh ] ; then
	UPGRADE="YES"
fi

if [ $UPGRADE = "YES" ] ; then
	# Script to upgrade pre-1.9r25 Linuxconf to new SysV compliant booting.
	# Dale - Hacked in a few minutes late one night :-)

	echo Upgrading from older install strategy >>/tmp/linuxconf-rpminstall.log
	# Kill the Install directory
	if [ -f /install/doinst.sh ] ; then
		log rm -Rf /install
	fi

	# Kill the old /usr/lib/linuxconf directory, the RPM will put
	# everything we need back in later.
	log rm -Rf /usr/lib/linuxconf

	# Create the directories we will need for the upgrade
	log install -d -g users -m 755 -o root /usr/lib/linuxconf/
	log install -d -g users -m 755 -o root /usr/lib/linuxconf/help.eng/notices/
	log install -d -g users -m 755 -o root /usr/lib/linuxconf/uninstall/

	# Create a note displayed by linuxconf informing that the RPM
	# install has done some cleanup
#	echo "      Installation note" >$OLDINSTALL
#	echo >>$OLDINSTALL
#	echo "The RPM installation has detected that linuxconf was already" >>$OLDINSTALL
#	echo "installed using the tar.gz kit" >>$OLDINSTALL
#	echo >>$OLDINSTALL
#	echo "It has taken action to fix your linuxconf installation" >>$OLDINSTALL
#	echo "so it becomes more compatible with RPM based systems" >>$OLDINSTALL
#	echo >>$OLDINSTALL
#	echo "You may want to check /tmp/linuxconf-rpminstall.log" >>$OLDINSTALL

	# I put a default RedHat inittab in /usr/lib/linuxconf/install
	# When I unpack the distro, the original SHOULD be there, but hey,
	# You never can tell when someone is gonna need that 1k taken up
	# by the backup....
	if [ -f /etc/inittab.old ] ; then
		log cp /etc/inittab /usr/lib/linuxconf/uninstall/inittab.beforeupgrade
		log mv -f /etc/inittab.old /etc/inittab
	#else
		# Tell the RPM to replace this file with a stock RedHat
		# We haven't untarred anything yet, so we can't replace it
		#log cp /etc/inittab /usr/lib/linuxconf/uninstall/inittab.beforeupgrade
		#log touch $INITTABREPLACE
	fi

	if [ -f /etc/rc.d/rc.M ] ; then
		log mv -f /etc/rc.d/rc.M /usr/lib/linuxconf/uninstall/rc.M.beforeupgrade
	fi

	if [ -f /etc/rc.d/rc.sysinit.old ] ; then
		log mv -f /etc/rc.d/rc.sysinit.old /usr/lib/linuxconf/uninstall/rc.sysinit.beforelinuxconf
	fi

	if [ -f /etc/rc.d/rc.old ] ; then
		log mv -f /etc/rc.d/rc.old /usr/lib/linuxconf/uninstall/rc.beforelinuxconf
	fi

	if [ -f /usr/bin/passwd.old ] ; then
		log mv -f /usr/bin/passwd.old /usr/lib/linuxconf/uninstall/passwd.beforelinuxconf
	fi

	if [ -f /usr/sbin/syslogd.old ] ; then
		log mv -f /usr/bin/syslogd.old /usr/lib/linuxconf/uninstall/syslogd.beforelinuxconf
	fi

	if [ -f /etc/conf.linuxconf ] ; then
		log mv -f /etc/conf.linuxconf /etc/conf.linuxconf-installed
	fi
fi

%post

/usr/lib/linuxconf/install/rpm-postinst.sh $*

# Add a few group ids so that the user is not prompted for them later...
if [ -x /usr/sbin/groupadd ] ; then
	# if it is an old version of groupadd, the combined -g and -r options
	# will cause it to fail, so we fall back on just -r.  It will be less
	# consistent across systems, but that's not too horrible.
	/usr/sbin/groupadd -g 230 -r -f pppusers >/dev/null 2>&1 || \
	  /usr/sbin/groupadd -r -f pppusers >/dev/null 2>&1 || true
	/usr/sbin/groupadd -g 231 -r -f popusers >/dev/null 2>&1 || \
	  /usr/sbin/groupadd -r -f popusers >/dev/null 2>&1 || true
	/usr/sbin/groupadd -g 232 -r -f slipusers >/dev/null 2>&1 || \
	  /usr/sbin/groupadd -r -f slipusers >/dev/null 2>&1 || true
fi

# Update /etc/inetd.conf - but leaves linuxconf disabled - aur�lio
if ! grep -qs linuxconf /etc/inetd.conf
then
	echo -e '# descomente a linha seguinte para utilizar a interface web\n# linuxconf stream tcp wait root /bin/linuxconf linuxconf --http' >> /etc/inetd.conf
	# not necessary cause it's disabled - aur�lio
	#	if [ -f /var/run/inetd.pid ] ; then
	#	kill -HUP `cat /var/run/inetd.pid`
	#	fi
fi

# turning off linuxconf suid - aur�lio
chmod 0755 /bin/linuxconf

# changing the portmap path - aur�lio
if ! grep -qs 'daemons.cmdspec rpc.portmap' /etc/conf.linuxconf
then echo 'daemons.cmdspec rpc.portmap /sbin/portmap' >> /etc/conf.linuxconf
fi

# standard Conectiva HTML BODY parameters - aur�lio
if ! grep -qs 'html.bodyparm' /etc/conf.linuxconf
then echo 'html.bodyparm bgcolor=white background="/images:images/CNCfundo.jpg" text=darkblue vlink=gray link=red' >> /etc/conf.linuxconf
fi

linuxconf --unsetmod treemenu

%preun

# The script is handed a 0 if this is a uninstall
# and a 1 if it is an upgrade...
/usr/lib/linuxconf/install/rpm-preuninst.sh $1

		

%postun

# Cry a little tear, because Linuxconf is not on this machine anymore...

%files

%config(noreplace) %verify(not md5 size mtime) /etc/conf.linuxconf
%config /etc/pam.d/linuxconf
%config /etc/pam.d/linuxconf-pair
%config /etc/logrotate.d/linuxconf
/usr/lib/linuxconf/
%attr(0755,root,root)/bin/linuxconf
/bin/netconf
/bin/xconf
/bin/lpdconf
/bin/fsconf
/sbin/askrunlevel
/sbin/dnsconf
/sbin/fixperm
/sbin/mailconf
/bin/userconf
%config /bin/remadmin

%ghost /var/log/htmlaccess.log
%ghost /var/log/netconf.log
%ghost /var/log/boot.log

%doc rpmfiles/doc/COPYING
%doc rpmfiles/doc/HELPING
%doc rpmfiles/doc/RPM-CHANGES
%doc rpmfiles/doc/RPM-INSTALL
%doc rpmfiles/doc/RPM-README
%doc rpmfiles/doc/UPGRADE

%files devel

/usr/include/linuxconf
/usr/lib/liblinuxconf.a
/usr/lib/linuxconf-devel

%changelog
* Wed Jun 30 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- I'm proud to create the first entry for the changelog!
- rpm-postinstall checks if /etc/inetd.conf exists
- recompressed source
