Summary: The PPP daemon and documentation for Linux 1.3.xx and greater.
Summary(pt_BR): Servidor ppp para linux 1.3.xx e posteriores
Summary(es): Servidor ppp para linux 1.3.xx y posteriores
Name: ppp
Version: 2.3.7
Release: 3cl
Copyright: distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://cs.anu.edu.au/pub/software/ppp/ppp-%{version}.tar.bz2
Source1: ppp-2.3.5-pamd.conf
Source700: ppp-man-pt_BR.tar
Patch0: ppp-2.3.7-make.patch
Patch1: ppp-2.3.6-sample.patch
Patch3: ppp-2.3.7-auth.patch
Patch4: ppp-2.3.7-wtmp.patch
Buildroot: /var/tmp/pppd-root
Requires: glibc >= 2.0.6

%description
The ppp package contains the PPP (Point-to-Point Protocol) daemon
and documentation for PPP support.  The PPP protocol provides a
method for transmitting datagrams over serial point-to-point links.

The ppp package should be installed if your machine need to support
the PPP protocol.

%description -l pt_BR
Este é o servidor e a documentação para suporte PPP. Ele requer um
kernel superior ao 2.0. Os kernels-padrão da Conectiva incluem suporte
PPP como módulo.

%description -l es
Este es el servidor y la documentación para soporte PPP. Requiere un
kernel superior al 2.0. Los kernels padrón de la Conectiva incluyen
soporte PPP como módulo.

%prep
%setup  -q
%patch0 -p1 -b .make
%patch1 -p1 -b .sample
%patch3 -p1 -b .auth
%patch4 -p1 -b .wtmp
find . -type f -name "*.sample" | xargs rm -f 

%build
./configure
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install TOPDIR=$RPM_BUILD_ROOT

## it shouldn't be SUID root be default
#chmod 755 $RPM_BUILD_ROOT/usr/sbin/pppd

strip $RPM_BUILD_ROOT/usr/sbin/chat $RPM_BUILD_ROOT/usr/sbin/pppstats \
	$RPM_BUILD_ROOT/usr/sbin/pppd 
chmod 644 scripts/*
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/ppp




mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/ppp-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,root)	/usr/sbin/chat
%attr(0755,root,root)	/usr/sbin/pppd
%attr(0755,root,daemon)	/usr/sbin/pppstats
%attr(0644,root,root)	/usr/man/man8/chat.8
%attr(0644,root,root)	/usr/man/man8/pppd.8
%attr(0644,root,daemon)	/usr/man/man8/pppstats.8
%attr(0755,root,root)	%dir /etc/ppp
%attr(0600,root,daemon)	%config /etc/ppp/chap-secrets
%attr(0644,root,daemon)	%config /etc/ppp/options
%attr(0600,root,daemon)	%config /etc/ppp/pap-secrets
%attr(0644,root,root)	%config /etc/pam.d/ppp
%attr(-,-,-)		%doc README README.linux scripts sample
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 06 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 2.3.5 to 2.3.7

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- force pppd use the glibc's logwtmp instead of implementing its own

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 22 1999 Michael Johnson <johnsonm@redhat.com>
- auth patch

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Jun  5 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.3.5.

* Tue May 19 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Fri May  8 1998 Jakub Jelinek <jj@ultra.linux.cz>
- make it run with kernels 2.1.100 and above.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Mar 18 1998 Cristian Gafton <gafton@redhat.com>
- requires glibc 2.0.6 or later

* Wed Mar 18 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated PAM patch to not turn off wtmp/utmp/syslog logging.

* Wed Jan  7 1998 Cristian Gafton <gafton@redhat.com>
- added the /etc/pam.d config file
- updated PAM patch to include session support

* Tue Jan  6 1998 Cristian Gafton <gafton@redhat.com>
- updated to ppp-2.3.3, build against glibc-2.0.6 - previous patches not
  required any more.
- added buildroot
- fixed the PAM support, which was really, completely broken and against any
  standards (session support is still not here... :-( )
- we build against running kernel and pray that it will work
- added a samples patch; updated glibc patch

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- added a patch to use our own route.h, rather then glibc's (which has 
  alignment problems on Alpha's) -- I only applied this patch on the Alpha,
  though it should be safe everywhere

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- turned off the execute bit for scripts in /usr/doc

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Integrated new patch from David Mosberger
- Improved description

