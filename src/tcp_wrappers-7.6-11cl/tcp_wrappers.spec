Summary: A security tool which acts as a wrapper for TCP daemons.
Summary(pt_BR): Programa de segurança para daemons tcp
Summary(es): Programa de seguridad para daemons tcp
Name: tcp_wrappers
Version: 7.6
Release: 11cl
Copyright: Distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://coast.cs.purdue.edu/pub/tools/unix/tcp_wrappers/tcp_wrappers_7.6.tar.bz2
Patch: tcpw7.2-config.patch
Patch1: tcpw7.2-setenv.patch
BuildRoot: /var/tmp/%{name}-root

%description
The tcp_wrappers package provides small daemon programs which can
monitor and filter incoming requests for systat, finger, ftp, telnet,
rlogin, rsh, exec, tftp, talk and other network services.

Install the tcp_wrappers program if you need a security tool for
filtering incoming network services requests.

%description -l pt_BR
Com este pacote você pode monitorar e filtrar chamadas de SYSTAT,
FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, e outros serviços
de rede.

%description -l es
Con este paquete puedes monitorar y filtrar llamadas de SYSTAT,
FINGER, FTP, TElNET, RLOGIN, RSH, EXEC, TFTP, TALK, y otros servicios
de red.

%prep
%setup -q -n tcp_wrappers_7.6
%patch0 -p1 -b .config
%patch1 -p1 -b .setenv

%build
%ifarch sparc sparc64
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fPIC"
export RPM_OPT_FLAGS
%endif
make linux

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{include,lib,man/man3,man/man5,man/man8,sbin}

cp hosts_access.3 $RPM_BUILD_ROOT/usr/man/man3
cp hosts_access.5 hosts_options.5 $RPM_BUILD_ROOT/usr/man/man5
cp tcpd.8 tcpdchk.8 tcpdmatch.8 $RPM_BUILD_ROOT/usr/man/man8
ln -sf hosts_access.5 $RPM_BUILD_ROOT/usr/man/man5/hosts.allow.5
ln -sf hosts_access.5 $RPM_BUILD_ROOT/usr/man/man5/hosts.deny.5
cp libwrap.a $RPM_BUILD_ROOT/usr/lib
cp tcpd.h $RPM_BUILD_ROOT/usr/include
install -m755 safe_finger $RPM_BUILD_ROOT/usr/sbin
install -m755 tcpd $RPM_BUILD_ROOT/usr/sbin
install -m755 tcpdchk $RPM_BUILD_ROOT/usr/sbin
install -m755 tcpdmatch $RPM_BUILD_ROOT/usr/sbin
install -m755 try-from $RPM_BUILD_ROOT/usr/sbin

strip $RPM_BUILD_ROOT/usr/sbin/tcpd $RPM_BUILD_ROOT/usr/sbin/tcpdchk 
strip $RPM_BUILD_ROOT/usr/sbin/tcpdmatch $RPM_BUILD_ROOT/usr/sbin/safe_finger
strip $RPM_BUILD_ROOT/usr/sbin/try-from

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BLURB CHANGES README* DISCLAIMER Banners.Makefile
/usr/man/man3/hosts_access.3
/usr/man/man5/hosts_access.5
/usr/man/man5/hosts.allow.5
/usr/man/man5/hosts.deny.5
/usr/man/man5/hosts_options.5
/usr/man/man8/tcpd.8
/usr/man/man8/tcpdchk.8
/usr/man/man8/tcpdmatch.8
/usr/include/tcpd.h
/usr/lib/libwrap.a
/usr/sbin/safe_finger
/usr/sbin/tcpd
/usr/sbin/tcpdchk
/usr/sbin/tcpdmatch
/usr/sbin/try-from

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 12 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Jeff Johnson <jbj@redhat.com>
- compile on sparc with -fPIC.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Sat Aug 22 1998 Jeff Johnson <jbj@redhat.com>
- close setenv bug (problem #690)
- spec file cleanup

* Thu Jun 25 1998 Alan Cox <alan@redhat.com>
- Erp where did the Dec 05 patch escape to

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- don't build setenv.o module -- it just breaks things

* Wed Oct 29 1997 Marc Ewing <marc@redhat.com>
- upgrade to 7.6

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Upgraded to version 7.5
- Uses a build root
