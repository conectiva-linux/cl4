Summary: The client and server programs for the telnet remote login protocol.
Summary(pt_BR): Cliente e servidor para o protocolo telnet de login remoto 
Summary(es): Cliente y servidor para el protocolo telnet de login remoto 
Name: telnet
Version: 0.10
Release: 27cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/netkit-telnet-0.10.tar.gz
Source1: telnet.wmconfig
Source2: telnet-client.tar.gz
Source700: telnet-man-pt_BR.tar
Source800: telnet-wmconfig.i18n.tgz
Patch0: netkit-telnet-0.10-misc.patch
Patch1: netkit-telnet-0.10-openpty.patch
Patch2: telnet-0.10-maint.patch
Patch3: telnet-0.10-utmp.patch
Requires: inetd
Buildroot: /var/tmp/%{name}-root

%description
Telnet is a popular protocol for logging into remote systems over
the Internet.  The telnet package provides a command line telnet client
as well as a telnet daemon, which will support remote logins into the
host machine.  The telnet daemon is enabled by default.  You may
disable the telnet daemon by editing /etc/inetd.conf.

Install the telnet package if you want to telnet to remote machines
and/or support remote logins to your own machine.

%description -l pt_BR
O telnet é um protocolo popular para logins remotos através da
Internet. Este pacote fornece um cliente telnet na linha de comando
e um servidor telnet que permite login remoto dentro da máquina em
que ele está rodando. O servidor telnet é habilitado por default,
e pode ser desabilitado editando-se o /etc/inetd.conf.

%description -l es
telnet es un protocolo popular para logins remotos a través de
la Internet. Este paquete ofrece un cliente telnet en la línea de
comando y un servidor telnet que permite login remoto dentro de la
máquina en que se está ejecutando. El servidor telnet se habilita
por defecto, y puede ser inhabilitado editándose /etc/inetd.conf.

%prep
%setup -q -n netkit-telnet-0.10
%patch0 -p1 -b .misc
%patch1 -p1 -b .openpty
%patch2 -p1 -b .maint
%patch3 -p1 -b .utmp

mv telnet telnet-NETKIT
tar xzf %SOURCE2

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make INSTALLROOT=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m644 $RPM_SOURCE_DIR/telnet.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/telnet




mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/telnet-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

tar xvfpz $RPM_SOURCE_DIR/telnet-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(missingok) /etc/X11/wmconfig/telnet
/usr/bin/telnet
/usr/man/man1/telnet.1
/usr/sbin/in.telnetd
/usr/man/man5/issue.net.5
/usr/man/man8/in.telnetd.8
/usr/man/man8/telnetd.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- i18n wmconfig

* Thu Apr 15 1999 Jeff Johnson <jbj@redhat.com>
- use glibc utmp routines.

* Thu Apr  8 1999 Jeff Johnson <jbj@redhat.com>
- fix the fix (wrong way memcpy).

* Wed Apr  7 1999 Jeff Johnson <jbj@redhat.com>
- fix "telnet localhost" bus error on sparc64 (alpha?).

* Tue Apr  6 1999 Jeff Johnson <jbj@redhat.com>
- use OpenBSD telnet client (and fix minor core dump with .telnetrc #247)

* Thu Mar 25 1999 Erik Troan <ewt@redhat.com>
- use openpty in telnetd

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 24 1998 Cristian Gafton <gafton@redhat.com>
- compile C++ code using egcs

* Tue Apr 14 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
