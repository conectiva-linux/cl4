Summary: GNU libc
Summary(pt_BR): GNU libc
Summary(es): GNU libc
Name: glibc
Version: 2.1.1
%define DATE 990416
Release: 11cl
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: glibc-%{DATE}.tar.gz
Source1: http://www.ozemail.com.au/~geoffk/glibc-crypt/glibc-crypt-2.1.tar.gz
Source2: glibc-compat-2.1.0.tar.gz
Source3: glibc-2.1-nsswitch.conf
Source4: glibc-pt_BR.po
Source5: nscd.init
Patch0: glibc-2.1-rhpaths.patch
Patch1: glibc-2.1-noversion.patch
Patch2: glibc-2.1-cppfix.patch
Patch3: glibc-2.1.1-nscd.patch
Patch4: glibc-2.1.1-libio-vfork.patch
Patch5: glibc-2.1.1-libc4.patch
Patch6: glibc-2.1.1-noctty.patch
Patch7: glibc-2.1.1-fstatvfs.patch
Patch10: glibc-2.1.1-nscdhup.patch
Patch11: glibc-2.1-alpha-rx164.patch
Buildroot: /var/tmp/glibc-%{PACKAGE_VERSION}-root
Obsoletes: zoneinfo, libc-static, libc-devel, libc-profile, libc-headers,
Obsoletes:  linuxthreads, gencat, locale
Autoreq: false
%ifarch alpha
Provides: ld.so.2
%else
%endif
%ifarch sparc
Obsoletes: libc
%endif

%description
Contains the standard libraries that are used by multiple programs on
the system. In order to save disk space and memory, as well as to
ease upgrades, common system code is kept in one place and shared between
programs. This package contains the most important sets of shared libraries,
the standard C library and the standard math library. Without these, a
Linux system will not function. It also contains national language (locale)
support and timezone databases.

%description -l pt_BR
Contém as bibliotecas-padrão que são usadas por múltiplos programas
no sistema.  Para salvar espaço de disco e memória, assim como para
facilitar atualizações, o código comum do sistema é mantido em um
lugar e compartilhado entre programas.

Este pacote contém os mais importantes conjuntos de bibliotecas
compartilhadas, a biblioteca-padrão C e a biblioteca-padrão de
matemática. Sem estes, um sistema Linux não funcionará. Também
provê suporte a linguagem nacional (locale) e basede dados de
fusos horários.

%description -l es
Contiene las bibliotecas padrón que usan múltiples programas en el
sistema. El código común del sistema se mantiene en un lugar y se
comparte entre programas, para guardar espacio de disco y memoria,
y también para facilitar actualizaciones.  Este paquete contiene los
más importantes conjuntos de bibliotecas compartidas, la biblioteca
padrón C y la biblioteca padrón de matemática. Sin estos, un sistema
Linux no funcionará. También provee soporte al lenguaje nacional
(locale) y base de datos de zonas horarias.

%package devel
Summary: Additional libraries required to compile
Summary(pt_BR): Bibliotecas adicionais solicitadas para compilação
Summary(es): Bibliotecas adicionales solicitadas para compilación
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Conflicts: texinfo < 3.11
Prereq: /sbin/install-info
Obsoletes: libc-debug, libc-headers, libc-devel, linuxthreads-devel
Obsoletes: glibc-debug
Prereq: kernel-headers
Requires: kernel-headers >= 2.2.1
Autoreq: true

%description devel
To develop programs which use the standard C libraries (which nearly all
programs do), the system needs to have these standard header files and object
files available for creating the executables.

%description -l pt_BR devel
Para desenvolver programas executáveis que usam as bibliotecas-padrão
C (o que quase todos os programas fazem), o sistema precisa destes
arquivos de inclusão e bibliotecas.

%description -l es devel
El sistema necesita de estos archivos de inclusión y bibliotecas
para desarrollar programas ejecutables que usan las bibliotecas
padrón C (lo que hacen casi todos los programas).

%package profile
Summary: glibc with profiling support
Summary(pt_BR): Bibliotecas adicionais que requerem compilação 
Summary(es): Bibliotecas adicionales que requieren compilación 
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Obsoletes: libc-profile
Autoreq: true

%description profile
When programs are being profiled used gprof, they must use these libraries
instrad of the standard C libraries for gprof to be able to profile
them correctly.

%description -l pt_BR profile
Quando programas estão tendo tempos de execução de rotinas
verificados pelo gprof, eles devem utilizar estas bibliotecas
no lugar das bibliotecas C padrão para que o gprof funcione
corretamente.

%description -l es profile
Para que el gprof funcione correctamente, cuando hay programas que
están teniendo tiempos de ejecución de rutinas verificados por él,
estos deben utilizar estas bibliotecas en lugar de las bibliotecas
C padrón.

%package -n nscd
Summary: Name Service Caching Daemon
Summary(pt_BR): Servidor de cache para o Servidor de nomes
Summary(es): Name Service Caching Daemon
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Conflicts: kernel < 2.2.0
Prereq: chkconfig
Autoreq: true

%description -n nscd
nscd caches name service lookups; it can dramatically improve performance
with NIS+, and may help with DNS as well.

You cannot use nscd with 2.0 kernels, due to bugs in the kernel-side thread
support. nscd happens to hit these bugs particularly hard.

%description -l pt_BR -n nscd
O nscd faz cache de procuras de nomes, ele pode melhorar drasticamente o
desempenho com NIS+, e pode ajudar mesmo que só se utilize DNS.

%description -l es -n nscd
nscd caches name service lookups; it can dramatically improve performance
with NIS+, and may help with DNS as well.

You cannot use nscd with 2.0 kernels, due to bugs in the kernel-side thread
support. nscd happens to hit these bugs particularly hard.

%prep
%setup -n glibc -q -a 1 -a 2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch10 -p0
%patch11 -p0
 
%ifarch armv4l
rm -rf glibc-compat
%endif

find . -type f -size 0 -exec rm -f {} \;

%build
cp $RPM_SOURCE_DIR/glibc-pt_BR.po $RPM_BUILD_DIR/%{name}/po/pt_BR.po
autoconf
rm -rf build-$RPM_ARCH-linux
mkdir build-$RPM_ARCH-linux ; cd build-$RPM_ARCH-linux
%ifarch i586 i686
BuildFlags="-mpentium -D__USE_STRING_INLINES -fstrict-aliasing"
%endif
CC=egcs CFLAGS="$BuildFlags -g -O3" ../configure --prefix=/usr \
	--enable-add-ons=yes --without-cvs  \
	%{_target_cpu}-conectiva-linux
make -r CFLAGS="$BuildFlags -g -O3"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install_root=$RPM_BUILD_ROOT install -C build-$RPM_ARCH-linux
cd build-$RPM_ARCH-linux && \
    make install_root=$RPM_BUILD_ROOT install-locales -C ../localedata objdir=`pwd` && \
    cd ..

# Remove the files we don't want to distribute
rm -f $RPM_BUILD_ROOT/usr/lib/libNoVersion*

# the man pages for the linuxthreads require special attention
make -C linuxthreads/man
mkdir -p $RPM_BUILD_ROOT/usr/man/man3
install -m 0644 linuxthreads/man/*.3thr $RPM_BUILD_ROOT/usr/man/man3

gzip -9nvf $RPM_BUILD_ROOT/usr/info/libc*

ln -sf libbsd-compat.a $RPM_BUILD_ROOT/usr/lib/libbsd.a

install -m 644 $RPM_SOURCE_DIR/glibc-2.1-nsswitch.conf \
	$RPM_BUILD_ROOT/etc/nsswitch.conf

# This is for ncsd - in glibc 2.1
install -m 644 nscd/nscd.conf $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/nscd

# The database support
mkdir -p $RPM_BUILD_ROOT/var/db
install -m 644 nss/db-Makefile $RPM_BUILD_ROOT/var/db/Makefile

# Strip binaries
strip $RPM_BUILD_ROOT/sbin/* || :
strip $RPM_BUILD_ROOT/usr/bin/* || :
strip $RPM_BUILD_ROOT/usr/sbin/* || :

# BUILD THE FILE LIST
find $RPM_BUILD_ROOT -type f -or -type l | 
	sed -e 's|.*/etc|%config &|' > rpm.filelist.in
for n in /usr/share /usr/include; do 
    find ${RPM_BUILD_ROOT}${n} -type d | \
	grep -v '^/usr/share$' | \
	sed "s/^/%dir /" >> rpm.filelist.in
done

# primary filelist
sed "s|$RPM_BUILD_ROOT||" < rpm.filelist.in | 
	grep -v '/etc/localtime'  | \
	sort > rpm.filelist

grep '/usr/lib/lib.*_p\.a' < rpm.filelist > profile.filelist
egrep "(/usr/include)|(/usr/info)" < rpm.filelist | 
	grep -v /usr/info/dir > devel.filelist

mv rpm.filelist rpm.filelist.full
grep -v '/usr/lib/lib.*_p.a' rpm.filelist.full | 
	egrep -v "(/usr/include)|(/usr/info)" > rpm.filelist

grep '/usr/lib/lib.*\.a' < rpm.filelist >> devel.filelist
grep '/usr/lib/.*\.o' < rpm.filelist >> devel.filelist
grep '/usr/lib/lib.*\.so' < rpm.filelist >> devel.filelist
grep '/usr/man/man' < rpm.filelist >> devel.filelist

mv rpm.filelist rpm.filelist.full
grep -v '/usr/lib/lib.*\.a' < rpm.filelist.full |
	grep -v '/usr/lib/.*\.o' |
	grep -v '/usr/lib/lib.*\.so'|
	grep -v '/usr/man/man' | 
	grep -v 'nscd' > rpm.filelist

# /etc/localtime - we're proud of outr timezone
rm -f $RPM_BUILD_ROOT/etc/localtime
ln -sf ../usr/share/zoneinfo/US/Eastern $RPM_BUILD_ROOT/etc/localtime

# the last bit: more documentation
rm -rf documentation
mkdir documentation
cp linuxthreads/ChangeLog  documentation/ChangeLog.threads
cp linuxthreads/Changes documentation/Changes.threads
cp linuxthreads/README documentation/README.threads
cp linuxthreads/FAQ.html documentation/FAQ-threads.html
cp -r linuxthreads/Examples documentation/examples.threads
cp crypt/README documentation/README.crypt
cp db2/README documentation/README.db2
cp db2/mutex/README documentation/README.db2.mutex
cp timezone/README documentation/README.timezone
cp ChangeLog* documentation
gzip -9 documentation/ChangeLog*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/info/libc.info.gz /usr/info/dir

%preun devel
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/libc.info.gz /usr/info/dir
fi

%post -n nscd
/sbin/chkconfig --add nscd

%preun -n nscd
if [ $1 = 0 ] ; then
    /sbin/chkconfig --del nscd
fi

%clean
rm -rf "$RPM_BUILD_ROOT"
rm -f *.filelist*

%files -f rpm.filelist
%defattr(-,root,root)
%config(noreplace) /etc/localtime
%doc README NEWS INSTALL FAQ BUGS NOTES PROJECTS
%doc documentation/* README.template README.libm
%doc login/README.utmpd hesiod/README.hesiod
%dir /var/db

%files -f devel.filelist devel
%defattr(-,root,root)

%files -f profile.filelist profile
%defattr(-,root,root)

%files -n nscd
%defattr(-,root,root)
%config /etc/nscd.conf
/etc/rc.d/init.d/nscd
/usr/sbin/nscd

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- i18n initscripts (nscd)

* Tue Jun 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated pt_BR.po from the old 2.0.7 version (thx to rodrigo@conectiva)

* Wed May 19 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added to Conectiva Linux
- Recompiled with rpm 3.0.1, egcs 1.1.x and kernel 2.2.x

* Mon Apr 26 1999 Cristian Gafton <gafton@redhat.com>
- alpha patches from Jay Estabrook to support the RX164

* Wed Apr 14 1999 Cristian Gafton <gafton@redhat.com>
- new CVS update - some patches dropped out
- updated obsoletes tag lines
- patch for the ukraine support

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- add patch for libstdc++ 2.7.2 (enable __dup, __pipe and __waitpid)
- linuxthread patch from HJLu
- add patch to make nscd respond to SIGHUP by dumping the cache

* Wed Apr 07 1999 Cristian Gafton <gafton@redhat.com>
- updated from cvs tree
- add patch for fstatvfs from HJLu

* Thu Apr 01 1999 Cristian Gafton <gafton@redhat.com>
- opentty fix
- don't call lddlibc4 on sparcs

* Thu Mar 25 1999 Cristian Gafton <gafton@redhat.com>
- version 2.1.1
- make nscd run by default at init
- nscd subpackage
- let the subpackages autoreq their own thing

* Fri Mar 12 1999 Cristian Gafton <gafton@redhat.com>
- version 2.1
- strip binaries installed by default

* Thu Feb 18 1999 Cristian Gafton <gafton@redhat.com>
- updated snapshot
- glibc-crypt might have export problems (who knows?), so we are nosource
  iit for now

* Wed Feb 03 1999 Cristian Gafton <gafton@redhat.com>
- version 2.0.112
- merge glibc-debug into glibc-devel
- new compat add-on

* Wed Jan 13 1999 Cristian Gafton <gafton@redhat.com>
- new glibc-crypt add-on
- version 2.0.109
- handle /etc/localtime separately
- don't include /usr/share in the file list
- don not build glibc-compat on the arm

* Wed Dec 02 1998 Cristian Gafton <gafton@redhat.com>
- build ver 2.0.105 on all four arches
- enabled /usr/include/scsi as part of the glibc package

* Fri Oct 02 1998 Cristian Gafton <gafton@redhat.com>
- first build for 2.0.96
