Summary: Clients and servers for remote access commands (rsh, rlogin, rcp).
Summary(pt_BR): Cliente e servidor para o rsh, rcp e comandos rlogin
Summary(es): Cliente y servidor para el rsh, rcp y comandos rlogin
Name: rsh
Version: 0.10
Release: 25cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/netkit-rsh-0.10.tar.gz
Source1: rexec.pam
Source2: rlogin.pam
Source3: rsh.pam
Source4: rexec-1.4.tar.gz
Source700: rsh-man-pt_BR.tar
Patch0: netkit-rsh-0.10-misc.patch
Patch1: netkit-rsh-0.10-newpam.patch
Patch2: netkit-rsh-0.10-sectty.patch
Patch3: netkit-rsh-0.10-rexec.patch
Requires: inetd, pam >= 0.59
Buildroot: /var/tmp/%{name}-root

%description
The rsh package contains a set of programs which allow users to run
commmands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp).  All three of these commands
use rhosts style authentication.  This package contains the clients
and servers needed for all of these services.  It also contains a
server for rexec, an alternate method of executing remote commands.
All of these servers are run by inetd and configured using
/etc/inetd.conf and PAM.  The rexecd server is disabled by default,
but the other servers are enabled.

The rsh package should be installed to enable remote access to other
machines.

%description -l pt_BR
Rsh, rlogin e rcp são programas que permitem executar comandos em
máquinas remotas, login em outras máquinas e copiar arquivos entre
máquinas. Estes comandos usam autenticação no estilo rhost. Este
pacote inclui clientes e servidores necessários para estes serviços,
bem como um servidor rexec, que é um método alternativo para execução
de comandos remotos.

Todos estes servidores são executados pelo inetd e configurados
através de /etc/inetd.conf e PAM. O servidor rexecd está desabilitado
por default, mas o restante está habilitado.

%description -l es
Rsh, rlogin y rcp son programas que permiten ejecutar comandos
en máquinas remotas, login en otras máquinas y copiar archivos
entre máquinas. Estos comandos usan autentificación en el estilo
rhost. Este paquete incluye clientes y servidores necesarios para
estos servicios, bien como un servidor rexec, que es un método
alternativo para ejecución de comandos remotos.  Todos estos
servidores son ejecutados por el inetd y configurados a través de
/etc/inetd.conf y PAM. El servidor rexecd está inhabilitado por
defecto, pero el restante está habilitado.

%prep
%setup -q -n netkit-rsh-0.10 -a 4
%patch0 -p1 -b .misc
%patch1 -p1 -b .newpam
%patch2 -p1 -b .sectty
%patch3 -p1 -b .rexec

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

make -C rexec-1.4

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make INSTALLROOT=$RPM_BUILD_ROOT install

make INSTALLROOT=$RPM_BUILD_ROOT install -C rexec-1.4
strip $RPM_BUILD_ROOT/usr/bin/rexec

install -m 644 $RPM_SOURCE_DIR/rexec.pam $RPM_BUILD_ROOT/etc/pam.d/rexec
install -m 644 $RPM_SOURCE_DIR/rlogin.pam $RPM_BUILD_ROOT/etc/pam.d/rlogin
install -m 644 $RPM_SOURCE_DIR/rsh.pam $RPM_BUILD_ROOT/etc/pam.d/rsh


mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/rsh-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/pam.d/rsh
/etc/pam.d/rlogin
/etc/pam.d/rexec
/usr/bin/rcp
/usr/bin/rexec
/usr/bin/rlogin
/usr/bin/rsh
/usr/man/man1/rcp.1
/usr/man/man1/rexec.1
/usr/man/man1/rlogin.1
/usr/man/man1/rsh.1
/usr/man/man8/in.rexecd.8
/usr/man/man8/in.rlogind.8
/usr/man/man8/in.rshd.8
/usr/man/man8/rexecd.8
/usr/man/man8/rlogind.8
/usr/man/man8/rshd.8
/usr/sbin/in.rexecd
/usr/sbin/in.rlogind
/usr/sbin/in.rshd
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 15 1999 Michael K. Johnson <johnsonm@redhat.com>
- rlogin pam file was missing comment magic

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip rexec

* Fri Mar 26 1999 Jeff Johnson <jbj@redhat.com>
- rexec needs pam_set_item() (#60).
- clarify protocol in rexecd.8.
- add rexec client from contrib.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 14 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Sat Apr  5 1998 Marcelo F. Vianna <m-vianna@usa.net>
- Packaged for RH5.0 (Hurricane)

* Tue Oct 14 1997 Michael K. Johnson <johnsonm@redhat.com>
- new pam conventions

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
