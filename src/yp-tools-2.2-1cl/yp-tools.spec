Summary: NIS (or YP) client programs.
Summary(pt_BR): Clientes NIS (YP)
Summary(es): Clientes NIS (YP)
Name: yp-tools
Version: 2.2
Release: 1cl
Copyright: GNU
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.kernel.org/pub/linux/utils/net/NIS/yp-tools-%{version}.tar.gz
Url: http://www-vt.uni-paderborn.de/~kukuk/linux/nis.html
Buildroot: /var/tmp/yp-tools-root
Obsoletes: yppasswd, yp-clients
Requires: ypbind

%description
The Network Information Service (NIS) is a system which provides network
information (login names, passwords, home directories, group information)
to all of the machines on a network.  NIS can enable users to login on
any machine on the network, as long as the machine has the NIS client
programs running and the user's password is recorded in the NIS passwd
database.  NIS was formerly known as Sun Yellow Pages (YP).

This package's NIS implementation is based on FreeBSD's YP and is a
special port for glibc 2.x and libc versions 5.4.21 and later.  This
package only provides the NIS client programs.  In order to use the
clients, you'll need to already have an NIS server running on your
network. An NIS server is provided in the ypserv package.

Install the yp-tools package if you need NIS client programs for machines
on your network.  You will also need to install the ypbind package on
every machine running NIS client programs.  If you need an NIS server,
you'll need to install the ypserv package on one machine on the network.

%description -l pt_BR
Esta implementação de NIS para Linux é baseada no YP para FreeBSD.
Ele é um porte especial para glibc 2.x e libc >=5.4.21.

Esta implementação somente provê clientes NIS. Você deve ter um
servidor NIS rodando em alguma máquina. Você pode encontrar um para
o Linux em http://www-vt.uni-paderborn.de/~kukuk/Linux/nis.html. Por
favor leia também o NIS-HOWTO.

%description -l es
Esta implementación de NIS para Linux está basada en el YP para
FreeBSD.  Es un porte especial para glibc 2.x y libc $>$=5.4.21.
Esta implementación solamente provee clientes NIS. Debes tener un
servidor NIS ejecutando en alguna máquina. Puedes encontrar uno para
Linux en http://www-vt.uni-paderborn.de/\~kukuk/Linux/nis.html. Por
Favor, lee también NIS-HOWTO.

%prep
%setup -q

%build
[ "$LINGUAS" ] && unset LINGUAS
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --disable-domainname
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
make distclean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog NEWS etc/nsswitch.conf
%doc THANKS TODO
/usr/bin/*
/usr/man/*/*
/usr/sbin/*
/usr/share/locale/*/*/*
/var/yp/nicknames

%changelog
* Fri May 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- unset LINGUAS

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- version 2.2
- make it obsolete older yp-clients package

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2/1
- version 2.1
- require ypbind

* Fri Jun 12 1998 Aron Griffis <agriffis@coat.com>
- upgraded to 2.0

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Apr 13 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.4.1

* Thu Dec 04 1997 Cristian Gafton <gafton@redhat.com>
- put yppasswd again in the package, 'cause it is the right thing to do
  (sorry djb!)
- obsoletes old, unmaintained yppasswd package

* Sat Nov 01 1997 Donnie Barnes <djb@redhat.com>
- removed yppasswd from this package.

* Fri Oct 31 1997 Donnie Barnes <djb@redhat.com>
- pulled from contrib into distribution (got fresh sources).  Thanks
  to Thorsten Kukuk <kukuk@vt.uni-paderborn.de> for the original.
- used fresh sources
