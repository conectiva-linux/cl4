Summary: Secure Shell - encrypts network communications.
Summary(pt_BR): Secure Shell - encripta comunicações da rede.
Summary(es): Secure Shell - encripta comunicaciones de la red.
Name: ssh
Version: 1.2.27
Release: 6cl
URL: http://www.cs.hut.fi/ssh/
Source0: ftp://ftp.cs.hut.fi/pub/ssh/ssh-1.2.27.tar.gz
Source1: ftp://ftp.funet.fi/pub/crypt/mirrors/idea.sec.dsi.unimi.it/math/rsaref20.tar.Z
Source2: sshd.init.rh50
Source3: ssh.pam
Source4: ftp://ftp.cs.hut.fi/pub/ssh/ssh-1.2.27.tar.gz.sig
#Patch: ssh-1.2.20-config.patch
#Patch1: ssh-1.2.20-alpha-rsaref.patch
#Patch2: ssh-1.2.26-pam.patch
#Patch6: ssh-1.2.25-install.patch
Copyright: Non-commercially distributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
BuildRoot: /tmp/ssh-buildroot

%package clients
Summary: Clients for connecting to Secure Shell servers
Summary(pt_BR): Clientes para conexão a servidores Secure Shell
Summary(es): Clientes para conexión a servidores Secure Shell
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Requires: ssh

%package server
Summary: Secure Shell protocol server (sshd)
Summary(pt_BR): Servidor (sshd) para o protocolo Secure Shell
Summary(es): Servidor (sshd) para protocolo Secure Shell
Requires: pam ssh chkconfig >= 0.9
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)

%package extras
Summary: Extra command for the secure shell protocol suite
Summary(pt_BR): Comandos extras para o protocolo secure shell (ssh)
Summary(es): Comandos extras para protocolo secure shell (ssh)
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Requires: ssh

%description
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine.  It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network.  X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

The 'i' form of the package is compiled with internal RSAREF and is
recommended for use outside the USA, the 'us' form is compiled for
external RSAREF and should be used within the USA. The 'us' version
does not have the IDEA encryption compiled in.

This is a base package. You will need to install at least one of
ssh-clients and ssh-server to really use ssh.

%description -l pt_BR
Ssh (Secure Shell) é um programa para logar em uma máquina remota
e para executar comandos remotos. Seu objetivo é substituir rlogin
e rsh, provendo comunicação segura encriptada entre duas máquinas
confiáveis em uma rede insegura. Conexões X11 e portas TCP/IP
arbitrárias podem ser repassadas sobre o canal seguro.

A forma 'i' do pacote é compilada com a biblioteca RSAREF
internacional e é recomendada para uso fora dos EUA; A forma 'us'
é compilada com a RSAREF externa e deve ser usada dentro dos EUA.

Este é o pacote básico. Você precisa instalar pelo menos um dos
pacotes ssh-clients ou ssh-server para realmente usar o ssh.

%description -l es
Ssh (Secure Shell) es un programa para "logar" en una máquina
remota y para ejecutar comandos remotos. Su objetivo es substituir
rlogin y rsh, y proveer comunicación segura encriptada entre de
las máquinas fiables de una red insegura. Conexiones X11 y puertos
TCP/IP arbitrarias pueden ser repasadas sobre el canal seguro.
La forma 'i' del paquete está compilada con la biblioteca RSAREF
internacional y se recomienda para uso fuera de los EUA; La forma
'us' está compilada con la RSAREF externa y se debe usar dentro de
los EUA.  Este es el paquete básico. Necesitas instalar al menos uno
de los paquetes ssh-clients o ssh-server para realmente usar el ssh.

%description clients
This package includes the clients necessary to make encrypted connections
to SSH servers.

%description -l pt_BR clients
Este pacote inclui os clientes necessários para fazer conexões
encriptadas a servidores SSH.

%description -l es clients
Este paquete incluye los clientes necesarios para hacer conexiones
encriptadas a servidores SSH.

%description server
This package contains the secure shell daemon and its documentation.
The sshd is the server part of the secure shell protocol and allows
ssh clients to connect to your host.

%description -l pt_BR server
Este pacote contém o servidor secure shell (sshd) e sua documentação.
O sshd é a parte servidora do protocolo secure shell e permite que
clientes ssh façam conexões seguras com a sua máquina.

%description -l es server
Este paquete contiene el servidor secure shell (sshd) y su
documentación.  sshd es la parte servidora del protocolo secure
shell y permite que los clientes ssh hagan conexiones seguras con
su máquina.

%description extras
This package contains the make_ssh_known_hosts perl script,
the ssh-askpass command and its documentation. They were moved
to the separate package to allow clean install of ssh even
on X11-less and perl-less machines (make_ssh_known_hosts is a perl script
and ssh-askpass uses X11 libraries.

%description -l pt_BR extras
Este pacote contém o script perl make_ssh_known_hosts, o comando
ssh-askpass e sua documentação. Eles foram movidos para este pacote
separado para permitir uma instalação limpa do ssh mesmo em uma
máquina sem X11 e sem perl (make_ssh_known_hosts é um script perl
e ssh-askpass usa bibliotecas X11).

%description -l es extras
Este paquete contiene el script perl make\_ssh\_known\_hosts, el
comando ssh-askpass y su documentación. Fueron movidos para este
paquete separado para permitir una instalación  limpia del ssh
inncluso en una máquina sin X11 y sin perl (make\_ssh\_known\_hosts
es un script perl y ssh-askpass usa bibliotecas X11).

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Updated to version 1.2.27 (Marcelo)

* Mon Mar 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed find-requires

* Fri Mar 12 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Jul 11 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Updated to 1.2.26.
- Fixed the incorrect %attr for the %ghost files.
- Do not restart sshd if it has not been running already.
- When restarting or stopping sshd, redirect the stdout to stderr.
- Fixed the PAM patch (removed changelog from the top of the configure.in
  patch).
- Removed the scp-silent patch (no longer needed).
- Removed the core-sdi patch (no longer needed).

* Tue Jul 7 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Default buildroot changed to /tmp/ssh-buildroot to remove the clash with
  the root's ssh-agent socket directory (hopefully nobody has an user named
  "buildroot" :-)
- From Daniel Bergstrom <daniel@futurniture.se>:
  incorporated the core-patch from http://www.core-sdi.com/ssh/
  It seems people are really interested in ssh RPMs - I have got two mails
  about that core-sdi advisory before I could even get to read the
  freshmeat.net :-)

* Thu Jul 2 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- merged Toshio Kuratomi's changes with John A. Martin's ones,
  backported all changes to the libc5 version as well.
- modified rc script to start sshd even if there are some (non-listening)
	ssh-daemons running. This allows you to log in via the ssh and
	do /etc/rc.d/init.d/sshd stop and start.

* Wed Jul 1 1998 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
- fix symlinks (hopefully) by adding %ghost decls to file section
  and changing the test in the postinstall to test for symlink existence, not 
  file existence.
- Also have the %post section restart the sshd server.
- Change the %postun script to a %preun script.  I'm pretty sure the script
  should be run before the package is removed.

* Fri Jun 12 1998 John A. Martin <jam@jamux.com>
- added Tero Kivinen's patch posted to ssh-list today
- remade Stig Bjorlykke's non-root build patch to fit after above
- revised and renamed /etc/rc.d/init.d/sshd.init for pre-RH50 systems
	to sshd like other newer ones.

* Thu Jun 11 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- updated to 1.2.25.
- fixed truncated .pam patch.
- built on RedHat 5.1 (and tested upgrade on 5.0 too).

* Wed May 20 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Updated to 1.2.23:
- removed the -NYP patch (no longer necessary).
- removed the -tmpfile patch (no longer necessary).
- added %post scripts linking the ssh*1 binaries and manpages as ssh*
	if no such links exist. This will allow a coexistence of
	ssh1 and ssh2 RPMs on one system.

* Sat May  9 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Patch to the install part of Makefile.in allowing non-root build
	of ssh (Stig Bjorlykke <stigb@tihlde.hist.no>)

* Sat May  2 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- The ssh package needs the /etc/ssh directory to allow the host key
	to be generated. Added %dir /etc/ssh to the ssh's %files.
	(thanx to Jan Vicherek for finding this).
* Fri May  1 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Splitted into ssh, ssh-server, ssh-clients and ssh-extras RPMs
	to make installation more clean.
- No longer requires tcp_wrappers because libwrap.a is statically linked.
- The us version has defaults to the blowfish cipher because of licensing
	with the idea algorithm.
- Merged the us and international spec file. The only difference between
	them is now the Release: field.

* Wed Apr 15 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>

Change suggested by Ben Liblit <liblit@cs.berkeley.edu>:
- The /tmp/ssh-<logname> cleanup patch.

Changes suggested by Eric Backus <ericb@labejb.lsid.hp.com>:
- The /etc/rc.d/init.d/sshd marked as %config again.
- Added %attr to all the files (in the previous version a ssh_config was
	root-only readable, so that ssh did not use it at all).
- The %post script calls chkconfig as well as the %postun script
- The PGP signature of the ssh tar file added to the source RPM.

* Thu Apr  9 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>

- added redirection of ssh-keygen's output so that it does not destroy the
	screen contents when burn into and running from a RedHat-like
	installation CD.

* Sat Jan 31 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>

- make sshd.init to be chkconfig-compatible.

* Mon Jan 26 1998 Serge Droz <droz@physics.uoguelph.ca>

- Applied the NY patch to get rid of the infamous "You don't exist,
  go away" problem running yellow pages.

* Thu Jan 22 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>

- Make the %prep script to recreate configure from the PAM-patched
	configure.in using autoreconf as suggested by Simon Liddington
	<sjl96v@ecs.soton.ac.uk>

* Wed Jan 21 1998 Jan "Yenya" Kasprzak <kas@fi.muni.cz>

- Upgraded to 1.2.22.

* Fri Dec  5 1997 Jan "Yenya" Kasprzak <kas@fi.muni.cz>

- Upgraded to 1.2.21.

* Fri Jul 04 1997 Martin Ebourne <mje92@ecs.soton.ac.uk>

- Added 'echo' into sshd.init so it formats the output correctly
- Added patch for RSAREF on Alpha from Richard Bullington <rbulling@obscure.org>

* Thu Jun 26 1997 Martin Ebourne <mje92@ecs.soton.ac.uk>

- Changes from Charlie Brady <cbrady@ind.tansu.com.au> to include PAM patch
- Fixed bug with upgrading from pre-1.2.20 without a known_hosts file
- Removed /etc/shadow and /etc/login.defs fixes since now unnecessary

%prep
%setup
echo Patching to use installed zlib
#%patch -p1 -b .config
mkdir rsaref2
tar -C rsaref2 -xzf $RPM_SOURCE_DIR/rsaref20.tar.Z

if [ -e rsaref2/rsaref.tar ]; then
	cd rsaref2
	tar xf rsaref.tar
	cd ..
%ifarch alpha
	echo Patching RSAREF for 64 bitness
#%patch1 -p1 -b .alpha
%endif
fi

echo Patching to use PAM
#%patch2 -p1 -b .pam

echo Makefile.in fix for non-root builds
#%patch6 -p0 -b .nonroot

autoreconf

%build
if echo %{PACKAGE_RELEASE} | grep -q us
then
	USE_RSAREF=--with-rsaref
else
	USE_RSAREF=
fi
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --with-etcdir=/etc/ssh --with-libwrap $USE_RSAREF
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr $RPM_BUILD_ROOT/etc/rc.d/init.d $RPM_BUILD_ROOT/etc/pam.d
make install_prefix=$RPM_BUILD_ROOT install
touch $RPM_BUILD_ROOT/etc/ssh/ssh_host_key
install -m644 $RPM_SOURCE_DIR/ssh.pam $RPM_BUILD_ROOT/etc/pam.d/ssh
install -m755 $RPM_SOURCE_DIR/sshd.init.rh50 $RPM_BUILD_ROOT/etc/rc.d/init.d/sshd
install -m600 host_config.sample $RPM_BUILD_ROOT/etc/ssh/ssh_config
sed 's:_ETCDIR_:/etc/ssh:' < server_config.sample > sshd_config
install -m600 sshd_config $RPM_BUILD_ROOT/etc/ssh/sshd_config
strip $RPM_BUILD_ROOT/usr/sbin/* $RPM_BUILD_ROOT/usr/bin/* ||:
if echo %{PACKAGE_RELEASE} | grep -q us
then
	echo 'Cipher blowfish' >> $RPM_BUILD_ROOT/etc/ssh/ssh_config
fi
ln -sf ssh1 $RPM_BUILD_ROOT/usr/bin/slogin1

%clean
rm -rf $RPM_BUILD_ROOT

%post
for i in /usr/bin/ssh-keygen /usr/bin/scp
do
	if test \! -L $i
	then ln -sf `basename $i`1 $i
	fi
done
for i in /usr/man/man1/ssh-keygen.1 /usr/man/man1/scp.1
do
	if test \! -L $i
	then CHAPTER=${i#*.}; PROG=${i%.$CHAPTER}
		ln -sf `basename $PROG`1.$CHAPTER ${PROG}.$CHAPTER
	fi
done

if [ ! -f /etc/ssh/ssh_host_key -o ! -s /etc/ssh/ssh_host_key ]; then
	# Pre 1.2.20-1 RPM config was directly in /etc
	if [ -f /etc/ssh_host_key -a -s /etc/ssh_host_key ]; then
		mv /etc/ssh_host_key /etc/ssh_host_key.pub /etc/ssh/
		mv /etc/ssh_known_hosts /etc/ssh/ >/dev/null 2>&1 ||:
		mv /etc/ssh_random_seed /etc/ssh/ >/dev/null 2>&1 ||:
	else
        	/usr/bin/ssh-keygen -b 1024 -f /etc/ssh/ssh_host_key -N '' >&2
	fi
fi

%post server
for i in /usr/sbin/sshd
do
	if test \! -L $i
	then ln -sf `basename $i`1 $i
	fi
done
for i in /usr/man/man8/sshd.8
do
	if test \! -L $i
	then CHAPTER=${i#*.}; PROG=${i%.$CHAPTER}
		ln -sf `basename $PROG`1.$CHAPTER ${PROG}.$CHAPTER
	fi
done
/sbin/chkconfig --add sshd
if test -r /var/run/sshd.pid
then
	/etc/rc.d/init.d/sshd restart >&2
fi

%preun server
if [ "$1" = 0 ]
then
	/etc/rc.d/init.d/sshd stop >&2
	/sbin/chkconfig --del sshd
fi

%post clients
for i in /usr/bin/ssh /usr/bin/ssh-agent /usr/bin/ssh-add /usr/bin/slogin
do
	if test \! -L $i
	then ln -sf `basename $i`1 $i
	fi
done
for i in /usr/man/man1/ssh.1 /usr/man/man1/ssh-agent.1 /usr/man/man1/ssh-add.1 /usr/man/man1/slogin.1
do
	if test \! -L $i
	then CHAPTER=${i#*.}; PROG=${i%.$CHAPTER}
		ln -sf `basename $PROG`1.$CHAPTER ${PROG}.$CHAPTER
	fi
done

%post extras
for i in /usr/bin/ssh-askpass /usr/bin/make-ssh-known-hosts
do
	if test \! -L $i
	then ln -sf `basename $i`1 $i
	fi
done
for i in /usr/man/man1/make-ssh-known-hosts.1
do
	if test \! -L $i
	then CHAPTER=${i#*.}; PROG=${i%.$CHAPTER}
		ln -sf `basename $PROG`1.$CHAPTER ${PROG}.$CHAPTER
	fi
done


%files
%doc COPYING ChangeLog INSTALL README README.CIPHERS README.SECURERPC
%doc README.SECURID README.TIS RFC RFC.nroff TODO README.DEATTACK
%attr(0755,root,root) /usr/bin/ssh-keygen1
%attr(0644,root,root) /usr/man/man1/ssh-keygen1.1
%attr(0755,root,root) /usr/bin/scp1
%attr(0644,root,root) /usr/man/man1/scp1.1
%attr(0755,root,root) %dir /etc/ssh
%attr(-,root,root) %ghost /usr/bin/ssh-keygen
%attr(-,root,root) %ghost /usr/man/man1/ssh-keygen.1
%attr(-,root,root) %ghost /usr/bin/scp
%attr(-,root,root) %ghost /usr/man/man1/scp.1

%files server
%attr(0755,root,root) /usr/sbin/sshd1
%attr(0644,root,root) /usr/man/man8/sshd1.8
%attr(0600,root,root) %config /etc/ssh/sshd_config
%attr(0600,root,root) %config /etc/pam.d/ssh
%attr(0755,root,root) %config /etc/rc.d/init.d/sshd
%attr(-,root,root) %ghost /usr/sbin/sshd
%attr(-,root,root) %ghost /usr/man/man8/sshd.8

%files extras
%attr(0755,root,root) /usr/bin/make-ssh-known-hosts1
%attr(0644,root,root) /usr/man/man1/make-ssh-known-hosts1.1
%attr(0755,root,root) /usr/bin/ssh-askpass1
%attr(-,root,root) %ghost /usr/bin/make-ssh-known-hosts
%attr(-,root,root) %ghost /usr/man/man1/make-ssh-known-hosts.1
%attr(-,root,root) %ghost /usr/bin/ssh-askpass

%files clients
%attr(0644,root,root) %config /etc/ssh/ssh_config
%attr(4755,root,root) /usr/bin/ssh1
%attr(-,root,root) /usr/bin/slogin1
%attr(0755,root,root) /usr/bin/ssh-agent1
%attr(0755,root,root) /usr/bin/ssh-add1
%attr(0644,root,root) /usr/man/man1/ssh-agent1.1
%attr(0644,root,root) /usr/man/man1/ssh-add1.1
%attr(0644,root,root) /usr/man/man1/slogin1.1
%attr(0644,root,root) /usr/man/man1/ssh1.1
%attr(-,root,root) %ghost /usr/bin/ssh
%attr(-,root,root) %ghost /usr/bin/slogin
%attr(-,root,root) %ghost /usr/bin/ssh-agent
%attr(-,root,root) %ghost /usr/bin/ssh-add
%attr(-,root,root) %ghost /usr/man/man1/ssh-agent.1
%attr(-,root,root) %ghost /usr/man/man1/ssh-add.1
%attr(-,root,root) %ghost /usr/man/man1/slogin.1
%attr(-,root,root) %ghost /usr/man/man1/ssh.1

