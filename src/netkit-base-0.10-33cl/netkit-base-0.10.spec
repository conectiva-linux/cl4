Summary: The ping and inetd networking programs.
Summary(pt_BR): Inclui os programas de rede ping e inetd
Summary(es): Incluye los programas de red ping y inetd
Name: netkit-base
Version: 0.10
Release: 33cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://sunsite.unc.edu/pub/Linux/system/network/netkit-base-0.10.tar.gz
Source1: inetd.conf.default
Source2: inet.init
Source3: inetd.conf.5
Source700: netkit-base-man-pt_BR.tar
Patch0: netkit-base-0.10-misc.patch
Patch1: ping-overflow.patch
Patch2: ping-flood.patch
Patch3: inetd-fdleak.patch
Patch4: netkit-base-0.10-maint.patch
Patch5: netkit-base-0.10-cl.patch
Provides: inetd
Prereq: chkconfig
Requires: tcp_wrappers
BuildRoot: /var/tmp/%{name}-root

%description
The netkit-base package contains the basic networking tools ping and
inetd.  The ping command sends a series of ICMP protocol ECHO_REQUEST
packets to a specified network host and can tell you if that machine
is alive and receiving network traffic.  Inetd listens on certain
Internet sockets for connection requests, decides what program should
receive each request, and starts up that program.

The netkit-base package should be installed on any machine that is on
a network.

%description -l pt_BR
Este pacote provê os programas ping e inetd, que são usados para
serviços básicos em redes.

%description -l es
Este paquete provee los programas ping y inetd, que se usan para
servicios básicos en redes.

%prep
%setup -q -n netkit-base-0.10
%patch0 -p1 -b .misc

cd ping
%patch1 -p0 -b .overflow
%patch2 -p0 -b .flood
cd ..

cd inetd
%patch3 -p0 -b .leak
cd ..

%patch4 -p1 -b .maint
#%patch5 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/usr/sbin
make INSTALLROOT=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT/usr/man/man5
install -m 644 $RPM_SOURCE_DIR/inetd.conf.5 $RPM_BUILD_ROOT/usr/man/man5

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/{init,rc0,rc1,rc2,rc3,rc4,rc5,rc6}.d
install -m 644 $RPM_SOURCE_DIR/inetd.conf.default $RPM_BUILD_ROOT/etc/inetd.conf
install -m 755 $RPM_SOURCE_DIR/inet.init $RPM_BUILD_ROOT/etc/rc.d/init.d/inet

ln -fs ../init.d/inet $RPM_BUILD_ROOT/etc/rc.d/rc0.d/K50inet
ln -fs ../init.d/inet $RPM_BUILD_ROOT/etc/rc.d/rc1.d/K50inet
ln -fs ../init.d/inet $RPM_BUILD_ROOT/etc/rc.d/rc2.d/K50inet
ln -fs ../init.d/inet $RPM_BUILD_ROOT/etc/rc.d/rc3.d/S50inet
ln -fs ../init.d/inet $RPM_BUILD_ROOT/etc/rc.d/rc5.d/S50inet
ln -fs ../init.d/inet $RPM_BUILD_ROOT/etc/rc.d/rc6.d/K50inet



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/netkit-base-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add inet

%postun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del inet
fi

%files
%defattr(-,root,root)
%attr(4755,root,root)	/bin/ping
%attr(0644,root,root)	%config(noreplace) /etc/inetd.conf
%attr(0755,root,root)	%config /etc/rc.d/init.d/inet
%config(missingok) /etc/rc.d/rc0.d/K50inet
%config(missingok) /etc/rc.d/rc1.d/K50inet
%config(missingok) /etc/rc.d/rc2.d/K50inet
%config(missingok) /etc/rc.d/rc3.d/S50inet
%config(missingok) /etc/rc.d/rc5.d/S50inet
%config(missingok) /etc/rc.d/rc6.d/K50inet
/usr/man/man5/inetd.conf.5
/usr/man/man8/inetd.8
/usr/man/man8/ping.8
/usr/sbin/inetd
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- i18n initscripts (inet) (again :)

* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Injected new group into package

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- i18n initscripts
- Do not apply acme's patch right now.

* Wed Apr  7 1999 Jeff Johnson <jbj@redhat.com>
- fix inetd fd leak (#695)

* Wed Mar 31 1999 Jeff Johnson <jbj@redhat.com>
- ping flood can send faster than it can receive -- staunch the flow. (#213)

* Tue Mar 30 1999 Bill Nottingham <notting@redhat.com>
- turn off imap/pop by default
- add a buffer overflow patch

* Fri Mar 26 1999 Jeff Johnson <jbj@redhat.com>
- make inetd.conf %config(noreplace).
- fix time service config (#1725).

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- comsat service added (commented out)

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- man page added

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 23)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Wed Jun 17 1998 Jeff Johnson <jbj@redhat.com>
- man page correction (problem #727)
- add build root.

* Fri Jun 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Jun 04 1998 Mike Wangsmo <wanger@redhat.com>
- made /etc/inetd.conf a %config file.  This is a D'oh!

* Mon May 04 1998 Michael K. Johnson <johnsonm@redhat.com>
- fixed iniscript enhancement

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 23 1998 Michael K. Johnson
- enhanced initscript

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added %config(missingok) to init symlinks

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- turned off in runlevel 2
- added status, restart options to init script

* Mon Oct 13 1997 Erik Troan <ewt@redhat.com>
- added chkconfig support

* Wed Aug 27 1997 Erik Troan <ewt@redhat.com>
- fixed init.d symlinks
- fixed permissions on /etc/rc.d/inet
