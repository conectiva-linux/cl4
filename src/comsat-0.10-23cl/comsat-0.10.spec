Summary: A mail checker client and comsat mail checking server.
Summary(pt_BR): Um programa para checar e-mail e um servidor comsat
Summary(es): A mail checker client and comsat mail checking server.
Name: comsat
Version: 0.10
Release: 23cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://sunsite.unc.edu/pub/Linux/system/network/finger/biff+comsat-0.10.tar.gz
Patch0: biff+comsat-0.10-misc.patch
Patch1: biff+comsat-0.10-nobr.patch
Obsoletes: biff
Provides: biff
Requires: inetd
BuildRoot: /var/tmp/%{name}-root

%description
The biff client and comsat server are an antiquated method of
asynchronous mail notification.  Although they are still supported, most
users use their shell's MAIL variable (or csh shell's mail variable) to
check for mail, or a dedicated application like xbiff or xmailbox.  If
the comsat service is not enabled, biff won't work and you'll need to use
either the MAIL or mail variable.   

You may want to install biff if you'd like to be notified when mail
arrives. However, you should probably check out the more modern
methodologies of mail notification (xbiff or xmailbox) instead.

%description -l pt_BR
Um Servidor comsat (Para checagem de e-mails)

%description -l es
The biff client and comsat server are an antiquated method of
asynchronous mail notification.  Although they are still supported, most
users use their shell's MAIL variable (or csh shell's mail variable) to
check for mail, or a dedicated application like xbiff or xmailbox.  If
the comsat service is not enabled, biff won't work and you'll need to use
either the MAIL or mail variable.   

You may want to install biff if you'd like to be notified when mail
arrives. However, you should probably check out the more modern
methodologies of mail notification (xbiff or xmailbox) instead.


%prep
%setup -q -n biff+comsat-0.10
%patch0 -p1
%patch1 -p1

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
/usr/bin/biff
/usr/man/man1/biff.1
/usr/sbin/in.comsat
/usr/man/man8/in.comsat.8
/usr/man/man8/comsat.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
