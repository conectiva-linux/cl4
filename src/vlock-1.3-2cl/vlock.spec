Summary: A program which locks one or more virtual consoles.
Summary(pt_BR): Trava uma ou mais consoles virtuais
Summary(es): Bloquea una o más consolas virtuales
Name: vlock
Version: 1.3
Release: 2cl
Copyright: GPL

Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema

Source: ftp://tsx-11.mit.edu:/pub/linux/sources/usr.bin/vlock-1.3.tar.gz
Requires: pam >= 0.59
BuildRoot: /tmp/vlock

%description
The vlock program locks one or more sessions on the console.  Vlock
can lock the current terminal (local or remote) or the entire virtual
console system, which completely disables all console access.  The
vlock program unlocks when either the password of the user who started
vlock or the root password is typed.

Install vlock if you need to disable access to one console or to all
virtual consoles.

%description -l pt_BR
O vlock igualmente tranca o terminal corrente (que pode ser qualquer
tipo de terminal, local ou remoto), ou tranca o sistema inteiro
de console virtual, desabilitando completamente todo o acesso ao
console. O vlock é desabilitado quando a senha do usuário que o
iniciou ou a senha do root é digitada.

%description -l es
vlock igualmente cierra el terminal corriente (que puede ser
cualquier tipo de terminal, local o remoto), como cierra el sistema
entero de consola virtual, inhabilitando, por completo, todo el
acceso a consola. vlock se inhabilita cuando se teclea la contraseña
del usuario que la haya iniciado o con la contraseña del root.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Wed Jan 13 1999 Michael Johnson <johnsonm@redhat.com>
- released 1.3

* Thu Mar 12 1998 Michael K. Johnson <johnsonm@redhat.com>
- Does not create a DoS attack if pty is closed (not applicable
  to use on a VC)

* Fri Oct 10 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved to new pam conventions.
- Use pam according to spec, rather than abusing it as before.
- Updated to version 1.1.
- BuildRoot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- moved from pam.conf to pam.d

%prep 
%setup

%build
make RPM_OPT_FLAGS="${RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
install -m 755 -o 0 -g 0 -s vlock $RPM_BUILD_ROOT/usr/bin
install -m 644 -o 0 -g 0 vlock.1 $RPM_BUILD_ROOT/usr/man/man1
install -m 644 -o 0 -g 0 vlock.pamd $RPM_BUILD_ROOT/etc/pam.d/vlock

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config /etc/pam.d/vlock
/usr/bin/vlock
/usr/man/man1/vlock.1
