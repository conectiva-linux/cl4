Summary: Talk client for one-on-one Internet chatting.
Summary(pt_BR): Conversa de cliente para um-em-um internet conversando 
Summary(es): Charla de cliente para uno-en-uno internet conversando 
Name: talk
Version: 0.11
Release: 2cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/chat/netkit-ntalk-%{version}.tar.gz
Patch0: netkit-ntalk-%{version}-misc.patch
Patch1: netkit-ntalk-%{version}-otalk.patch
Obsoletes: ntalk
Provides: ntalk
Requires: inetd
BuildRoot: /var/tmp/%{name}-root

%description
The ntalk package provides client and daemon programs for the
Internet talk protocol, which allows you to chat with other users
on different systems.  Talk is a communication program which copies
lines from one terminal to the terminal of another user.

Install ntalk if you'd like to use talk for chatting with users on
different systems.

%description -l pt_BR
Este pacote fornece um cliente e um daemon para o protocolo talk, que
permite a conversa um-para-um entre usuários em diferentes sistemas.

%description -l es
Este paquete ofrece un cliente y un daemon para el protocolo talk,
que permite la charla uno-a-uno entre usuarios en diferentes
sistemas.

%prep
%setup -q -n netkit-ntalk-%{version}
%patch0 -p1
%patch1 -p0 -b .otalk

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
/usr/bin/talk
/usr/man/man1/talk.1
/usr/sbin/in.ntalkd
/usr/sbin/in.talkd
/usr/man/man8/in.ntalkd.8
/usr/man/man8/in.talkd.8
/usr/man/man8/ntalkd.8
/usr/man/man8/talkd.8

%changelog
* Sun Jun 20 1999 Jeff Johnson <jbj@redhat.com>
- handle both talk and otalk packets (#2799).

* Fri Apr  9 1999 Jeff Johnson <jbj@redhat.com>
- update to multi-homed 0.11 version.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 14 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
