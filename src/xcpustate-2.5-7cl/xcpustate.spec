Summary: An X Window System based CPU state monitor.
Summary(pt_BR): Monitor de performance da CPU
Summary(es): Monitor de desempeño de la CPU
Name: xcpustate
%define version	2.5
Version: %{version}
Release: 7cl
Copyright: Freely redistributable
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema

Source: ftp://ftp.cs.toronto.edu/pub/jdd/xcpustate/xcpustate-%{version}.tar.gz
Source800: xcpustate-wmconfig.i18n.tgz
Patch0: xcpustate-%{version}-nlist.patch
Patch1: xcpustate-%{version}-alpha.patch
Patch2: xcpustate-%{version}-6.0.patch
BuildRoot: /var/tmp/xcpustate-root

%description
The xcpustate utility is an X Window System based monitor which shows
the amount of time that the CPU is spending in different states.  On a
Linux system, xcpustate displays a bar that indicates the amounts of idle,
user, nice and system time (from left to right) used by the CPU.

Install the xcpustate package if you'd like to use a horizontal bar style
CPU state monitor.

%description -l pt_BR
XCPUSTATE é um monitor de performance instantânea. Foi originalmente
escrito por Mark Morae para monitorar a distribuição de carga nas CPUs
de uma Silicon Graphics Iris 4D/240. Desde então já foi portado para
uma variedade de máquinas uniprocessadas e multiprocessadas.

%description -l es
XCPUSTATE es un monitor de desempeño instantáneo. Fue originalmente
escrito por Mark Morae para monitorar la distribución de carga
en las CPUs de una Silicon Graphics Iris 4D/240. Desde entonces
ya fue transportado para una variedad de máquinas uniprocesadas
y multiprocesadas.

%prep
%setup -q
%patch0 -p1 -b .nlist
%patch2 -p1 -b .glibc
%ifarch alpha
%patch1 -p1 -b .alpha
%endif

%build
xmkmf
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install install.man
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig


tar xvfpz $RPM_SOURCE_DIR/xcpustate-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,root) /usr/X11R6/bin/xcpustate
%attr(0644,root,root) /usr/X11R6/man/man1/xcpustate.1x

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0
- added patch to build

* Wed Jun 03 1998 Jeff Johnson <jbj@redhat.com>
- Created.

