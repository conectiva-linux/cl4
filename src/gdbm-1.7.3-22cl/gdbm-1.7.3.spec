Summary: A GNU set of database routines which use extensible hashing.
Summary(pt_BR): Biblioteca de banco de dados GNU para C
Summary(es): Biblioteca de banco de datos GNU para C
Name: gdbm
Version: 1.7.3
Release: 22cl
Source: ftp://prep.ai.mit.edu/pub/gnu/gdbm-1.7.3.tar.gz
Patch: gdbm-1.7.3-shlib.patch
Copyright: GPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Buildroot: /var/tmp/gdbm-root

%description
Gdbm is a GNU database indexing library, including routines
which use extensible hashing.  Gdbm works in a similar way to standard UNIX
dbm routines.  Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

If you're a C developer and your programs need access to simple database
routines, you should install gdbm.  You'll also need to install gdbm-devel.

%description -l pt_BR
Esta é uma biblioteca para banco de dados indexados. É útil para
aqueles que desenvolvem aplicações em C que tenham que fazer acesso
a banco de dados de forma simples e eficiente.

%description -l es
Esta es una biblioteca para banco de datos indexados. Es útil para
aquellos que desarrollan aplicaciones en C, que tienen de hacer
acceso a banco de datos de forma simple y eficiente.

%package devel
Summary: Development libraries and header files for the gdbm library.
Summary(pt_BR): Bibliotecas e arquivos de inclusão para desenvolvimento utilizando gdbm
Summary(es): Bibliotecas y archivos de inclusión para desarrollo utilizando gdbm
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: gdbm
Prereq: info

%description devel
Gdbm-devel contains the development libraries and header files
for gdbm, the GNU database system.  These libraries and header files are
necessary if you plan to do development using the gdbm database.

Install gdbm-devel if you are developing C programs which will use the
gdbm database library.  You'll also need to install the gdbm package.

%description -l pt_BR devel
Estas são as bibliotecas e arquivos de inclusão para desenvolvimento
gdbm, que é o sistema de banco de dados GNU. São necessárias se
você pretende desenvolver usando o banco de dados gdbm.

%description -l es devel
Estas son las bibliotecas y archivos de inclusión para desarrollo
gdbm, que es el sistema de banco de datos GNU. Son necesarias si
pretendes desarrollar usando el banco de datos gdbm.

%prep
%setup
%patch -p1 -b .shared
mkdir shared

%build
./configure --prefix=/usr
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" shared

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib,include,info,man/man3}
make install prefix=$RPM_BUILD_ROOT/usr
gzip -fn9 $RPM_BUILD_ROOT/usr/info/gdbm*info*
ln -sf libgdbm.so.2.0.0 $RPM_BUILD_ROOT/usr/lib/libgdbm.so

%post -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/info/gdbm.info.gz /usr/info/dir --entry="* gdbm: (gdbm).                   The GNU Database."

%postun -p /sbin/ldconfig

%preun devel
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/gdbm.info.gz /usr/info/dir --entry="* gdbm: (gdbm).                   The GNU Database."
fi

%files
/usr/lib/libgdbm.so.2.*

%files devel
/usr/lib/libgdbm.so
/usr/man/*/*
/usr/lib/libgdbm.a
/usr/include/*
/usr/info/gdbm*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 19)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- gdbm-devel moved to Development/Libraries

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- buildroot and built for Manhattan

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc
