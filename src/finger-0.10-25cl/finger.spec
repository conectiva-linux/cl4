Summary: The finger client and server.
Summary(pt_BR): Cliente e servidor finger 
Summary(es): Cliente y servidor finger 
Name: finger
Version: 0.10
Release: 25cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://sunsite.unc.edu/pub/Linux/system/network/finger/bsd-finger-0.10.tar.gz
Patch0: bsd-finger-0.10-misc.patch
Patch1: bsd-finger-0.10-security.patch
Patch2: bsd-finger-0.10-nobr.patch
Patch3: bsd-finger-0.10-typo.patch
Patch4: bsd-finger-0.10-timeout.patch
Patch5: bsd-finger-0.10-pts.patch
Patch6: bsd-finger-0.10-maint.patch
Requires: inetd
BuildRoot: /var/tmp/%{name}-root

%description
Finger is a utility which allows users to see information about system
users (login name, home directory, name, how long they've been logged
in to the system, etc.).  The finger package includes a standard finger
client and server. The server daemon (fingerd) runs from /etc/inetd.conf,
which must be modified to disable finger requests.

You should install finger if your system is used by multiple users and
you'd like finger information to be available.

%description -l pt_BR
Finger é um protocolo simples que permite buscar informações
sobre usuários em outras máquinas. Este pacote inclui um cliente
padrão finger e o servidor. O servidor roda através do inetd
e configurado no /etc/inetd.conf, que deve ser modificado para
desativar solicitações de finger.

%description -l es
Finger es un protocolo sencillo que permite buscar información
sobre usuarios en otras máquinas. Este paquete incluye un cliente
padrón finger y el servidor. El servidor se ejecuta a través del
inetd y configurado en /etc/inetd.conf, que debe ser modificado
para desactivar solicitaciones de finger.

%prep
%setup -q -n bsd-finger-0.10
%patch0 -p1 -b .misc
%patch1 -p1 -b .security
%patch2 -p1 -b .nobr
%patch3 -p1 -b .typo
%patch4 -p1 -b .timeout
%patch5 -p1 -b .maint

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,man/man8,sbin}

make INSTALLROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/finger
/usr/man/man1/finger.1
/usr/sbin/in.fingerd
/usr/man/man8/in.fingerd.8
/usr/man/man8/fingerd.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Injected new group into package

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr  8 1999 Jeff Johnson <jbj@redhat.com>
- fix process table filled DOS attack (#1271)
- fix pts display problems (#1987 partially)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- fix error message typo.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added check for getpwnam() failure
