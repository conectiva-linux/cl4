Summary: The NIS daemon which binds NIS clients to an NIS domain.
Summary(pt_BR): Processo de ligação NIS Summary(es): Proceso de ligación NIS
Name: ypbind
Version: 3.3
Release: 22cl
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://ftp.us.kernel.org/pub/linux/NIS/ypbind-%{PACKAGE_VERSION}.tar.bz2
Source1: ypbind.init
Source2: yp.conf
Patch0: ypbind-3.3-glibc5.diff.gz
Patch1: ypbind-3.3-am.patch
Prereq: chkconfig
Requires: portmap
Requires: yp-tools
Serial: 1
Buildroot: /var/tmp/ypbind-root

%description
The Network Information Service (NIS) is a system which provides network
information (login names, passwords, home directories, group information)
to all of the machines on a network.  NIS can enable users to login on
any machine on the network, as long as the machine has the NIS client
programs running and the user's password is recorded in the NIS passwd
database.  NIS was formerly known as Sun Yellow Pages (YP).

This package provides the ypbind daemon.  The ypbind daemon binds NIS
clients to an NIS domain.  Ypbind must be running on any machines which
are running NIS client programs.

Install the ypbind package on any machines which are running NIS client
programs (included in the yp-tools package).  If you need an NIS server,
you'll also need to install the ypserv package to a machine on your
network.

%description -l pt_BR
Este é um daemon que roda em clientes NIS/YP e os relaciona a um
domínio NIS. Ele deve estar rodando em sistemas baseados na glibc
para agirem como clientes NIS.

%description -l es
Este es un daemon que se ejecuta en clientes NIS/YP y los relaciona
a un dominio NIS. Debe ejecutarse en sistemas basados en la glibc
para funcionaren como clientes NIS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

# Rename /usr/sbin to /sbin (cheap way to move ypbind)
mv $RPM_BUILD_ROOT/usr/sbin $RPM_BUILD_ROOT/sbin
strip $RPM_BUILD_ROOT/sbin/ypbind

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ypbind
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/yp.conf
mkdir -p $RPM_BUILD_ROOT/var/yp/binding

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#/sbin/chkconfig --add ypbind

%postun
if [ $1 = 0 ] ; then
    /sbin/chkconfig --del ypbind
fi

%triggerpostun -- ypbind <= ypbind-3.3-5
/sbin/chkconfig --add ypbind

%files
%defattr(-,root,root)
/sbin/ypbind
/usr/man/*/*
%config /etc/rc.d/init.d/*
%config /etc/yp.conf
%dir /var/yp/binding
%doc README

%changelog
* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed
- chkconfig --add removed, so that the user has to enable the service start

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed Prereq

* Fri May 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- i18n initscripts

* Thu Apr 15 1999 Cristian Gafton <gafton@redhat.com>
- requires yp-tools, because ypwhcih is part of that package

* Tue Apr 13 1999 Bill Nottingham <notting@redhat.com>
- don't run ypwhich script if ypbind doesn't start

* Wed Apr 07 1999 Bill Nottingham <notting@redhat.com>
- add a 10 second timeout for initscript...

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binary

* Thu Apr 01 1999 Preston Brown <pbrown@redhat.com>
- fixed init script to wait until domain is really bound (bug #1928)

* Thu Mar 25 1999 Cristian Gafton <gafton@redhat.com>
- revert to stabdard ypbind; ypbind-mt sucks.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Sat Feb 13 1999 Cristian Gafton <gafton@redhat.com>
- build as ypbind instead of ypbind-mt

* Fri Feb 12 1999 Michael Maher <mike@redhat.com>
- addressed bug #609

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- provides ypbind
- switch to ypbind-mt instead of plain ypbind
- build for glibc 2.1
