Summary: A login program for SLIP connections.
Summary(pt_BR): Programa de login para SLIP
Summary(es): Programa de login para SLIP
Name: sliplogin
Version: 2.1.1
Release: 7cl
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
Copyright: BSD
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/serial/sliplogin-2.1.1.tar.gz
Patch0: sliplogin-2.1.0-misc.patch
Patch1: sliplogin-2.1.1-modes.patch
Patch2: sliplogin-2.1.0-path.patch
Patch4: sliplogin-2.1.0-glibc.patch
Patch5: sliplogin-2.1.1-includes.patch
Patch6: sliplogin-2.1.1-netdev.patch
BuildRoot: /var/tmp/sliplogin-root

%description
The sliplogin utility turns the terminal line on standard input into
a SLIP (Serial Line Internet Protocol) link to a remote host. Sliplogin
is usually used to allow dial-in SLIP connections.

Install the sliplogin package if you need to support dial-in SLIP
connections.

%description -l pt_BR
Vincula uma interface SLIP a uma entrada padrão. Isso é geralmente
utilizado para permitir conexões SLIP discadas.

%description -l es
Vincula una interface SLIP a una entrada padrón. Esto es generalmente
utilizado para permitir conexiones SLIP marcadas.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1 -b .modes
%patch2 -p1 -b .path
%patch4 -p1 -b .glibc
%patch5 -p1 -b .includes
%patch6 -p1 -b .netdev

%build
make clean
rm -f sliplogin
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS" access
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc/slip,usr/sbin,usr/man/man8}

make	SLIP=$RPM_BUILD_ROOT/etc/slip \
	SBIN=$RPM_BUILD_ROOT/usr/sbin \
	MAN=$RPM_BUILD_ROOT/usr/man \
	install

install -m644 slip.tty $RPM_BUILD_ROOT/etc/slip
install -m644 slip.hosts $RPM_BUILD_ROOT/etc/slip
install -m644 slip.route $RPM_BUILD_ROOT/etc/slip
install -m644 slip.passwd $RPM_BUILD_ROOT/etc/slip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.dynamic README.nis CHANGES TROUBLE_SHOOTING TODO
%config /etc/slip/slip.tty
%config /etc/slip/slip.login
%config /etc/slip/slip.logout
%config /etc/slip/slip.hosts
%config /etc/slip/slip.passwd
%config /etc/slip/slip.route
/usr/sbin/sliplogin
/usr/man/man8/sliplogin.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- upgraded to 2.1.1
- struct password needs <pwd.h>

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>
- removed excludearch for alpha

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
