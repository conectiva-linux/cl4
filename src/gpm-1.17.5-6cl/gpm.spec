Summary: A mouse server for the Linux console.
Summary(pt_BR): Suporte para mouse em terminais modo texto
Summary(es): Soporte para ratón en terminales modo texto
Name: gpm
Version: 1.17.5
Release: 6cl
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://animal.unipv.it/pub/gpm/gpm-%{version}.tar.bz2
Source1: gpm.init
Patch0: gpm-nops.patch
Patch1: gpm-1.17.2-makedev.patch
Patch2: gpm-1.17.5-docfix.patch
Patch3: gpm-1.17.5-fixso.patch
Prereq: chkconfig ldconfig info
# this defines the library version that this package builds.
%define LIBVER 1.17.5
BuildRoot: /var/tmp/gpm-root

%description
Gpm provides mouse support to text-based Linux applications like the emacs
editor, the Midnight Commander file management system, and other programs.
Gpm also provides console cut-and-paste operations using the mouse and
includes a program to allow pop-up menus to appear at the click of a mouse
button.

Gpm should be installed if you intend to use a mouse with your Red Hat
Linux system.

%description -l pt_BR
Gpm acrescenta suporte a mouse para aplicações Linux baseadas em
modo texto, como emacs, Midnight Commander, e outros. Fornece ainda,
para a console, operações de cortar e colar usando o mouse.

%description -l es
Gpm acrecienta soporte a ratón para aplicaciones Linux basadas en
modo texto, como emacs, Midnight Commander, y otros. Ofrece aún,
soporte a pantalla y operaciones de cortar-pegar usando el ratón.

%package devel
Requires: gpm
Summary: Libraries and header files for developing mouse driven programs.
Summary(pt_BR): Bibliotecas e arquivos de inclusão para desenvolver programas que utilizam mouse
Summary(es): Bibliotecas y archivos de inclusión para desarrollar programas que utilicen ratón
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
The gpm-devel program contains the libraries and header files needed
for development of mouse driven programs.  This package allows you to
develop text-mode programs which use the mouse.

Install gpm-devel if you need to develop text-mode programs which will use
the mouse.  You'll also need to install the gpm package.

%description -l pt_BR devel
Este pacote permite o desenvolvimento de programas em modo texto
que usam mouse.

%description -l es devel
Este paquete permite el desarrollo de programas en modo texto que
usan ratón.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1 -b .docfix
%patch3 -p1 -b .fixso

%build
autoconf
CFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS" ./configure \
	--prefix=/usr \
	--sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc

# As of Red Hat Linux 6.0, mouseconfig handles SPARC mice
#%ifarch sparc
#mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
#(echo MOUSETYPE=\"sun\"; echo XEMU3=no) > $RPM_BUILD_ROOT/etc/sysconfig/mouse
#%endif

PATH=/sbin:$PATH:/usr/sbin:$PATH

make prefix=$RPM_BUILD_ROOT/usr install-strip

install -m644 doc/gpm-root.1 $RPM_BUILD_ROOT/usr/man/man1
install -m644 gpm-root.conf $RPM_BUILD_ROOT/etc
install -s -m755 mouse-test $RPM_BUILD_ROOT/usr/bin
install -s -m755 hltest $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/emacs/site-lisp
install -m644 t-mouse.el t-mouse.elc $RPM_BUILD_ROOT/usr/share/emacs/site-lisp

{
  pushd $RPM_BUILD_ROOT
  ln -sf libgpm.so.%{LIBVER} ./usr/lib/libgpm.so
  gzip -9nf ./usr/info/gpm.info*
  popd
}

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d  
install -m 755 $RPM_SOURCE_DIR/gpm.init $RPM_BUILD_ROOT/etc/rc.d/init.d/gpm

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add gpm
/sbin/ldconfig
/sbin/install-info /usr/info/gpm.info.gz /usr/info/dir --entry="* gpm: (gpm).                   Text-mode mouse library."

%preun
if [ $1 = 0 ]; then
    /sbin/install-info /usr/info/gpm.info.gz --delete /usr/info/dir --entry="* gpm: (gpm).                   Text-mode mouse library."
fi

%postun
/sbin/ldconfig
if [ $1 = 0 ]; then
    /sbin/chkconfig --del gpm
fi

%files
%defattr(-,root,root)
%config /etc/gpm-root.conf

#%ifarch sparc
#%config /etc/sysconfig/mouse
#%endif

/usr/bin/disable-paste
/usr/bin/mouse-test
/usr/bin/mev
/usr/bin/gpm-root
/usr/bin/hltest
/usr/sbin/gpm
/usr/share/emacs/site-lisp/t-mouse.el
/usr/share/emacs/site-lisp/t-mouse.elc
/usr/info/gpm.info*
/usr/man/man1/mev.1
/usr/man/man1/gpm-root.1
/usr/man/man8/gpm.8
/usr/lib/libgpm.so.%{LIBVER}
%config /etc/rc.d/init.d/gpm

%files devel
%defattr(-,root,root)
/usr/lib/libgpm.a
/usr/include/gpm.h
/usr/lib/libgpm.so

%changelog
* Fri Jun 04 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed pidfile name. this was confusing linuxconf. fix reported by aurelio

* Fri Jun  4 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- make sure all binaries are stripped, make init stuff more chkconfig style
- removed sparc-specific mouse stuff
- bumped libver to 1.17.5
- fixed texinfo source

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Thu Mar  4 1999 Matt Wilson <msw@redhat.com>
- updated to 1.75.5

* Tue Feb 16 1999 Cristian Gafton <gafton@redhat.com>
- avoid using makedev for internal functions (it is a #define in the system
  headers)

* Wed Jan 13 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 1.17.2.

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- enforce the use of -D_GNU_SOURCE so that it will compile on the ARM
- build against glibc 2.1

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscript

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- recompiled for manhattan

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 1.13

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added patch from Richard to get things to build on the SPARC

* Tue Oct 28 1997 Donnie Barnes <djb@redhat.com>
- fixed the emacs patch to install the emacs files in the right
  place (hopefully).

* Mon Oct 13 1997 Erik Troan <ewt@redhat.com>
- added chkconfig support
- added install-info

* Thu Sep 11 1997 Donald Barnes <djb@redhat.com>
- upgraded from 1.10 to 1.12
- added status/restart functionality to init script
- added define LIBVER 1.11

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
