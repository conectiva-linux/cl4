Summary: The kernel daemon (kerneld) and kernel module utilities.
Summary(pt_BR): Utilitários para módulos e kerneld
Summary(es): Utilitarios para módulos y kerneld
Name: modutils
Version: 2.1.121
Release: 15cl
Copyright: GPL
Group: System Environment/Kernel
Group(pt_BR): Ambiente do Sistema/Kernel
Group(es): Ambiente del Sistema/Kernel
Source: ftp://ftp.redhat.com/pub/alphabits/modutils-%{version}.tar.bz2
Source700: modutils-man-pt_BR.tar
# This is not used anymore, but we like it sitting around
Source1: kerneld.init
Source2: kmod.crond
Patch0: modutils-2.1.121-autoload.patch
Patch1: modutils-2.1.55-nowarning.patch
Patch3: modutils-2.1.121-sparckludge.patch
Patch5: modutils-2.1.85-static.patch
Patch6: modutils-2.1.121-preferred.patch
Patch7: modutils-2.1.85-rh.patch
Patch8: modutils-2.1.121-systemmap.patch
Patch9: modutils-2.1.121-pcmcia.patch
Patch10: modutils-2.1.121-loop.patch
Patch11: modutils-2.1.121-raid.patch
Patch12: modutils-2.1.121-pppcompress.patch
Exclusiveos: Linux
Buildroot: /var/tmp/modutils-root
Prereq: chkconfig
Requires: vixie-cron >= 3.0.1-31
Obsoletes: modules

%description
The modutils packages includes the kerneld program for automatic
loading of modules under 2.0 kernels and unloading of modules under
2.0 and 2.2 kernels, as well as other module management programs.

Loaded and unloaded modules are device drivers and
filesystems, as well as other things.

%description -l pt_BR
O kernel do Linux permite que novas partes do kernel sejam carregadas
e que partes não usadas sejam descarregadas enquanto o kernel
continua rodando. Estas partes carregáveis são chamadas módulos,
e podem incluir drivers de dispositivo e de sistemas de arquivos,
entre outras coisas. Este pacote inclui programas para carregar e
descarregar módulos, automaticamente ou manualmente.

%description -l es
kernel del Linux permite que nuevas partes del kernel se carguen
y que partes no utilizadas en él sean descargadas a la vez que el
kernel continua ejecutando. Estas partes cargables son llamadas
módulos, y pueden incluir drivers de dispositivo y de sistemas de
archivos, entre otras cosas. Este paquete incluye programas para
cargar y descargar módulos, automáticamente o manualmente.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%ifarch sparc sparc64
%patch3 -p1
%endif

%patch5 -p1
# %patch6 -p1 -b .preferred
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
libtoolize --copy --force
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --disable-combined-insmod
%ifarch sparc sparc64
make ARCH=sparc64
mv -f depmod/depmod depmod/depmod64
mv -f insmod/insmod insmod/insmod64
mv -f insmod/modinfo insmod/modinfo64
cd insmod
make LDFLAGS=-static ARCH=sparc64
mv -f insmod insmod64.static
cd ..
make clean
make ARCH=sparc
%else
make dep all
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/cron.d
mkdir -p $RPM_BUILD_ROOT/{usr/man/man{1,2,8},sbin}
make install prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT
%ifarch sparc
install -s -m755 -o 0 -g 0 depmod/depmod64 $RPM_BUILD_ROOT/sbin/depmod64
install -s -m755 -o 0 -g 0 insmod/insmod64.static $RPM_BUILD_ROOT/sbin/insmod64.static
install -s -m755 -o 0 -g 0 insmod/insmod64 $RPM_BUILD_ROOT/sbin/insmod64
install -s -m755 -o 0 -g 0 insmod/insmod64 $RPM_BUILD_ROOT/sbin/modinfo64
%endif

make install-scripts prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT -C kerneld

# security hole, works poorly anyway
rm -f $RPM_BUILD_ROOT/sbin/request-route
strip $RPM_BUILD_ROOT/sbin/* || :
install -m 755 $RPM_SOURCE_DIR/kerneld.init $RPM_BUILD_ROOT/etc/rc.d/init.d/kerneld
install -m 644 $RPM_SOURCE_DIR/kmod.crond $RPM_BUILD_ROOT/etc/cron.d/kmod



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/modutils-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
# get rid of the old installations on upgrade
if [ -x /etc/rc.d/init.d/kerneld ] ; then
    /sbin/chkconfig --del kerneld
fi

%files
%defattr(-,root,root)
/sbin/*
/usr/man/man*/*
%config /etc/cron.d/kmod
#%config /etc/rc.d/init.d/kerneld
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Thu May 20 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- add support for the ppp compression modules by default

* Tue Apr 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- add cron.d file to run rmmod -as

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- take out kerneld

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- add patch to make all raid personalities recognized

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- obsoletes modules
- get rid of the /lib/modules/preferred hack

* Mon Mar 15 1999 Bill Nottingham <notting@redhat.com>
- added support for /lib/modules/foo/pcmcia
- make kerneld initscript not start by default

* Tue Feb 23 1999 Matt Wilson <msw@redhat.com>
- added sparc64 support from UltraPenguin

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- call libtoolize to allow it to compile on the arm

* Wed Dec 23 1998 Jeff Johnson <jbj@redhat.com>
- search /lib/modules/preferred before defaults but after specified paths.

* Tue Nov 17 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 2.1.121

* Thu Nov 05 1998 Erik Troan <ewt@redhat.com>
- added -m, -i options

* Thu Oct 01 1998 Michael K. Johnson <johnsonm@redhat.com>
- fix syntax error I introduced when enhancing initscript

* Wed Sep 30 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhance initscript

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- pick up ultrapenguin patches (not applied for now).
- pre-generate keyword.c so gperf doesn't have to be present (not applied).
- util/sys_cm.c: fix create_module syscall (signed return on sparc too)

* Wed Jul 15 1998 Jeff Johnson <jbj@redhat.com>
- correct %postun typos

* Fri May 01 1998 Erik Troan <ewt@redhat.com>
- added /lib/modules/preferred to search path

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.1.85
- actually make use of the BuildRoot

* Fri Apr  3 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Fix sparc64, add modinfo64 on sparc.

* Wed Mar 23 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Handle EM_SPARCV9, kludge to support both 32bit and 64bit kernels
  from the same package on sparc/sparc64.

* Fri Nov  7 1997 Michael Fulbright
- removed warning message when conf.modules exists and is a empty

* Tue Oct 28 1997 Erik Troan <ewt@redhat.com>
- patched to honor -k in options
- added modprobe.1
- added init script

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- removed bogus strip of lsmod (which is a script)

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- updated to 2.1.55
- builds in a buildroot

* Mon Aug 25 1997 Erik Troan <ewt@redhat.com>
- added insmod.static

* Sun Aug 24 1997 Erik Troan <ewt@redhat.com>
- built on Intel
- combined rmmod and insmod
