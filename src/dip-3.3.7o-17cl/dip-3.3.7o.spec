Summary: dip modem dialer
Summary(pt_BR): Dip: Discador de modems
Summary(es): Dip: Marcador de módems
Name: dip
Version: 3.3.7o
Release: 17cl
Copyright: GPL
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/serial/dip337o-uri.tgz
Patch: dip-3.3.7o-misc.patch
Patch1: dip-3.3.7o-suffix.patch
Patch2: dip-3.3.7o-fsstnd.patch
Patch3: dip-3.3.7o-glibc.patch
Patch4: dip-3.3.7o-sparc.patch
Patch5: dip-3.3.7o-andor.patch
BuildRoot: /var/tmp/dip-root
Summary(de): dip-Modem-Wählprogramm
Summary(fr): Numéroteur modem dip.
Summary(tr): Modem çevirici

%description
dip is a program to allow for automatic scripting of modem dialing.
It's useful for setting up PPP and SLIP connections, but isn't required
for either.  It is used by netcfg for setting up SLIP connections.

%description -l pt_BR
dip é um programa que permite que scripts automáticos de discagem
de modem. É útil para configurar conexões PPP e SLIP, mas não é
necessária para nenhuma. Ele é usado por netcfg para configuração
de conexões SLIP.

%description -l es
dip es un programa que permite scripts automáticos de marcado de
módem. Es útil para configurar conexiones PPP y SLIP, pero no hace
falta a ninguna. Lo usa el netcfg para configuración de conexiones
SLIP.

%description -l de
dip ist ein Programm, das die automatische Skripterstellung zum Wählen 
über Modem ermöglicht. Es ist zum Einrichten von PPP- und SLIP-
Verbindungen nützlich, wenn auch nicht obligatorisch und wird von 
netcfg zum Einrichten von SLIP-Verbindungen benutzt. 

%description -l fr
dip est un programme permettant la mise en script automatique des
appels modems. Pratique pour configurer les connexions PPP et SLIP,
mais pas nécessaire. Il est utilisé par netcfg pour configurer les
connexions SLIP.

%description -l tr
dip, modem çevrilmesinin bir programcýk sayesinde otomatik olarak
gerçekleþtirilmesini saðlayan bir pakettir. PPP veya SLIP baðlantýlarý
kurmak için çok kullanýþlýdýr, ancak her ikisi için de gerekli deðildir.

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch4 -p0
%patch5 -p1 -b .andor
%patch3 -p1 -b .glibc

%build
make depend
(cd skey; make clean; make linux)
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}

install -c -s dip $RPM_BUILD_ROOT/usr/sbin
ln -sf dip $RPM_BUILD_ROOT/usr/sbin/diplogin
install -c -m 0444 dip.8 $RPM_BUILD_ROOT/usr/man/man8
ln -sf dip.8 $RPM_BUILD_ROOT/usr/man/man8/diplogin.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,uucp)	/usr/sbin/dip
/usr/sbin/diplogin
/usr/man/man8/dip.8
/usr/man/man8/diplogin.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- various spec file cleanups
