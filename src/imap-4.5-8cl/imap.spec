Summary: provides support for IMAP and POP network mail protocols
Summary(pt_BR): Provê suporte para os protocolos de mail IMAP e POP
Summary(es): Provee soporte para los protocolos de mail IMAP y POP
Name: imap
Version: 4.5
Release: 8cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
# was .Z
Source: ftp://ftp.cac.washington.edu/mail/imap-%{version}.tar.bz2
Source1: imap.pamd
Patch0: imap-4.5-linux.patch
Patch1: imap-4.4-vfs.patch
Patch2: imap-4.5-redhat.patch

Buildroot: /var/tmp/imap
Requires: pam >= 0.59
Summary(de): Bietet Unterstützung für IMAP- und POP-Netz-Mail-Protokolle
Summary(fr): Fournit un support pour les protocoles de mail IMAP et POP.
Summary(tr): IMAP ve POP posta indirme protokollarý için sunucu

%description
IMAP is a server for the POP (Post Office Protocol) and IMAP mail protocols.
The POP protocol allows a "post office" machine to collect mail for users
and have that mail downloaded to the user's local machine for reading. The
IMAP protocol provides the functionality of POP, and allows a user to
read mail on a remote machine without moving it to his local mailbox.

%description -l pt_BR
IMAP é um servidor para os protocolos de mail POP (Post Office
Protocol) e IMAP.  O protocolo POP permite uma máquina de correio
coletar mail para usuários e permite o download do mail para a
máquina local do usuário para leitura. O protocolo IMAP oferece
a funcionalidade de POP, e permite um usuário ler seu mail em uma
máquina remota sem movê-lo para a sua caixa postal local.

%description -l es
IMAP es un servidor para los protocolos de mail POP (Post Office
Protocol) y IMAP.  El protocolo POP permite a una máquina de correo
colectar mail para usuarios y permite download del mail a la máquina
local del usuario para lectura. El protocolo IMAP nos ofrece la
funcionalidad de POP, y permite a un usuario leer su mail en una
máquina remota sin moverlo a su caja postal local.

%prep

%setup -q
%patch0 -p1 -b .linux
%patch1 -p1 -b .pam
%patch2 -p1 -b .noflock

%build

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DIGNORE_LOCK_EACCES_ERRORS" slx

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
install -m 644 ./src/ipopd/ipopd.8c $RPM_BUILD_ROOT/usr/man/man8/ipopd.8c
install -m 644 ./src/imapd/imapd.8c $RPM_BUILD_ROOT/usr/man/man8/imapd.8c
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -s -m 755 ./ipopd/ipop2d $RPM_BUILD_ROOT/usr/sbin
install -s -m 755 ./ipopd/ipop3d $RPM_BUILD_ROOT/usr/sbin
install -s -m 755 ./imapd/imapd $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
install -m 644 ${RPM_SOURCE_DIR}/imap.pamd $RPM_BUILD_ROOT/etc/pam.d/imap

%clean
rm -f imap
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/pam.d/imap
/usr/man/man8/ipopd.8c
/usr/man/man8/imapd.8c
%attr(0755,root,mail)	/usr/sbin/ipop2d
%attr(0755,root,mail)	/usr/sbin/ipop3d
%attr(0755,root,mail)	/usr/sbin/imapd
%doc README

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- recompressed sources with bzip2

* Sat Jun  5 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Oct 04 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- use only fcntl locking.

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.4.
- removed g+s bit to imapd.

* Wed Jul 22 1998 Jeff Johnson <jbj@redhat.com>
- updated to 4.2.
- added g+s bit to imapd so that lock files can be created.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- Updated to the latest imap as of today...

* Wed Dec 10 1997 Cristian Gafton <gafton@redhat.com>
- Updated to the latest imap as of today...
- Updated the pam patch to reflect the new directory organization

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fix patch for new PAM spec compliance.

* Thu Oct 02 1997 Michael K. Johnson <johnsonm@redhat.com>
- Comply with change in PAM spec.
- Use a buildroot.

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved from pam.conf to pam.d

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Fixed buffer overrun in server_login().
