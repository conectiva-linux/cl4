Summary: Programs for maintaining networked machines' time synchronization.
Summary(pt_BR): Servidor TCP/IP que fornece horário
Summary(es): Servidor TCP/IP que ofrece la hora
Name: timed
Version: 0.10
Release: 23cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://sunsite.unc.edu/pub/Linux/system/admin/time/netkit-timed-0.10.tar.gz
Patch0: netkit-timed-0.10-misc.patch
Patch1: timed-0.10-ifr.patch
Patch2: timed-0.10-maint.patch
Requires: inetd
Buildroot: /var/tmp/%{name}-root

%description
The timed package contains the timed daemon and the timedc program
for controlling the timed program.  Timed synchronizes its host
machine's time with the time on other local network machines.  The
timedc program is used to control and configure the operation of
timed.

Install the timed package if you need a system for keeping networked
machines' times in synchronization.

%description -l pt_BR
Este servidor permite que máquinas remotas perguntem o horário.
Ele permite uma sincronização simples de horário através da rede.

%description -l es
Este servidor permite que máquinas remotas pregunten el horario.
Permite una sincronización sencilla de horario a través de la red.

%prep
%setup -q -n netkit-timed-0.10
%patch0 -p1 -b .misc
%patch1 -p1 -b .ifr
%patch2 -p1 -b .maint

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,sbin}
mkdir -p $RPM_BUILD_ROOT/usr/man/man{1,8}
make INSTALLROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/man/man8/timed.8
/usr/man/man8/timedc.8
/usr/sbin/timed
/usr/sbin/timedc

%changelog
* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Apr 17 1999 Jeff Johnson <jbj@redhat.com>
- fix ifreq size problem.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
