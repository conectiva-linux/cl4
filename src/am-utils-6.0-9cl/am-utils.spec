Summary: Automount utilities including an updated version of Amd.
Summary(pt_BR): Utilitários do automount - inclui o servidor automount NFS
Summary(es): Utilitarios del automount - incluye el servidor automount NFS
Name: am-utils
Version: 6.0
Serial: 1
Release: 9cl
Copyright: BSD
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://shekel.mcl.cs.columbia.edu/pub/am-utils/am-utils-%{version}.tar.bz2
Source1: am-utils.init
Source2: am-utils.conf
Source3: am-utils.sysconf
Patch0: am-utils-6.0a16-linux.patch
Patch1: am-utils-6.0a16-alpha.patch
Patch2: am-utils-6.0a16-glibc21.patch
Requires: portmap
BuildRoot: /var/tmp/am-utils-root
Prereq: chkconfig info
Obsoletes: amd

%description
Am-utils includes an updated version of Amd, the popular BSD
automounter.  An automounter is a program which maintains a cache of
mounted filesystems.  Filesystems are mounted when they are first
referenced by the user and unmounted after a certain period of inactivity.
Amd supports a variety of filesystems, including NFS, UFS, CD-ROMS and
local drives.  

You should install am-utils if you need a program for automatically
mounting and unmounting filesystems.

%description -l pt_BR
O am-utils é a "próxima geração" do popular automounter BSD amd.
Inclui muitas adições: atualizações, portes, programas, características,
correções de problemas, etc.

O AMD é o servidor automount de Berkeley. Tem a capacidade de automaticamente
montar sistemas de arquivos de todos os tipos, incluindo sistemas de
arquivos NFS, CD-ROMs e acionadores locais e de desmontá-los quando não
estiverem mais sendo usados.

A configuração default permite que seja feito um 'cd /net/[máquina]' para
obter uma lista dos diretórios exportados por aquela máquina

%description -l es
am-utils es la "próxima generación" del popular automounter
BSD amd.  Incluye muchas adiciones: actualizaciones, portes,
programas, características, correcciones de problemas, etc.
AMD es el servidor automount de Berkeley. Tiene la capacidad de
automáticamente montar sistemas de archivos de todos los tipos,
incluyendo sistemas de archivos NFS, CD-ROMs y accionadores locales
y de desmontarlos cuando no estén en uso.  La configuración por
defecto permite que se haga un 'cd /net/[máquina]' para obtener
una lista de los directorios exportados por aquella máquina

%prep
%setup -q
%patch2 -p1 -b .glibc21
%patch0 -p1 -b .lnx
%ifnarch i386
%patch1 -p1 -b .noauto
%endif

%build
cd aux ; autoconf ; mv -f configure .. ; cd ..
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--enable-shared --sysconfdir=/etc --enable-libs=-lnsl
# fun with autoconf
touch `find -name Makefile.in`
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr sysconfdir=`pwd`/etc
mkdir -p $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d}
install -m 600 $RPM_SOURCE_DIR/am-utils.conf $RPM_BUILD_ROOT/etc/amd.conf
install -m 755 $RPM_SOURCE_DIR/am-utils.sysconf $RPM_BUILD_ROOT/etc/sysconfig/amd
install -m 755 $RPM_SOURCE_DIR/am-utils.init $RPM_BUILD_ROOT/etc/rc.d/init.d/amd
strip $RPM_BUILD_ROOT/usr/sbin/* $RPM_BUILD_ROOT/usr/bin/* || :
gzip -q9f $RPM_BUILD_ROOT/usr/info/*info*
mkdir -p $RPM_BUILD_ROOT/.automount
# get rid of some lame scripts
file $RPM_BUILD_ROOT/usr/sbin/* | \
	grep -v ELF | grep -v am-eject | \
	cut -f 1 -d':' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
#/sbin/chkconfig --add amd
/sbin/install-info /usr/info/am-utils.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/am-utils.info.gz /usr/info/dir
fi

%postun
/sbin/ldconfig
if [ $1 = 0 ]; then
    /sbin/chkconfig --del amd
fi

%files
%defattr(-,root,root)
%doc doc/*.ps AUTHORS BUGS ChangeLog NEWS README* TODO
%dir /.automount
/usr/bin/pawd
/usr/sbin/*
/usr/man/man[58]/*
/usr/man/man1/pawd.1
%config /etc/amd.conf
%config /etc/sysconfig/amd
%config /etc/rc.d/init.d/amd
/usr/info/*info*.gz
/usr/lib/libamu.so
/usr/lib/libamu.so.*

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- i18n initscripts (amd)

* Sat Jun 19 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable

* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 08 1999 Preston Brown <pbrown@redhat.com>
- kill -HUP on reload, restart does a real restart.

* Fri Mar 26 1999 Bill Nottingham <notting@redhat.com>
- twiddle an echo in initscript

* Tue Mar 23 1999 Cristian Gafton <gafton@redhat.com>
- version 6.0 proper
- Serial:1 because to enforce versioning

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- rebuild for glibc 2.1
- strip all binaries

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- add missing ':' to default 'opts:=nosuid,nodev'
- install info pages

* Mon Jul 13 1998 Cristian Gafton <gafton@redhat.com>
- added the NIS support that the broken configure script failed to detect

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- disabled autofs support on alpha
- run ldconfig in postinstall

* Mon May 04 1998 Cristian Gafton <gafton@redhat.com>
- new package to replace the old and unmaintained amd
