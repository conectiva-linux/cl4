Summary: An implementation of the RFC1413 identification server.
Summary(pt_BR): Internet Daemon
Summary(es): Internet Daemon
Name: pidentd
Version: 2.8.5
Release: 3cl
Copyright: Public domain
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://ftp.lysator.liu.se/pub/unix/ident/servers/pidentd-%{version}.tar.gz
Patch0: pidentd-2.8.4-rh.patch
BuildRoot: /var/tmp/%{name}-root

%description
The pidentd package contains identd, which implements the RFC1413
identification server.  Identd looks up specific TCP/IP connections
and returns either the user name or other information about the
process that owns the connection.

%description -l pt_BR
IDentd é um programa que implementa o servidor de identificação
RFC1413. Identd opera observando conexões específicas de TCP/IP e
retorna o nome do usuário do proprietário processo de conexão.

%description -l es
IDentd es un programa que introduce el servidor de identificación
RFC1413. Identd opera observando conexiones específicas de TCP/IP
y retorna el nombre del usuario del propietario proceso de conexión.

%prep
%setup -q
%patch0 -p1 -b .rh

%build
make linux

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}
mkdir -p $RPM_BUILD_ROOT/etc

make DESTROOT=$RPM_BUILD_ROOT install
install -c identconn $RPM_BUILD_ROOT/usr/sbin

perl -pi -e "s,$RPM_BUILD_ROOT,," $RPM_BUILD_ROOT/usr/man/man8/identd.8

touch $RPM_BUILD_ROOT/etc/identd.conf
touch $RPM_BUILD_ROOT/etc/identd.keys

{ cd $RPM_BUILD_ROOT
  strip ./usr/sbin/* || :
}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS INSTALL README READMEs doc TODO ChangeLog
/usr/sbin/in.identd
#/usr/sbin/idecrypt
# this shoud be g+s root.kmem but let the user set that
%attr(755,root,kmem)	/usr/sbin/itest
/usr/sbin/identconn
/usr/man/man8/*identd.8
#/usr/man/man8/idecrypt.8
#%config	/etc/identd.conf
#%config /etc/identd.keys

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.8.5.
- fix dangling BuildRoot in man page (#1458).

* Thu Nov 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.8.4.

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- updated to 2.7

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
