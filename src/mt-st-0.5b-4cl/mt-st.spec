Summary: Programs to control tape device operations.
Summary(pt_BR): Controla a operação de drivers de fita magnética (mt)
Summary(es): Controla la operación de drivers de cinta magnética (mt)
Name: mt-st
Version: 0.5b
Release: 4cl
Copyright: BSD
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://metalab.unc.edu/pub/Linux/system/backup/mt-st-0.5b.tar.gz
Patch: mt-st-buildroot.patch
BuildRoot: /var/tmp/%{name}-root

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape
devices) can control rewinding, ejecting, skipping files and
blocks and more.

This package can help you manage tape drives.

%description -l pt_BR
O programa mt pode ser usado para desenvolver várias operações em
fitas, incluindo retroceder, ejetar, pular arquivos e blocos, etc.

%description -l es
El programa mt puede ser usado para desarrollar varias operaciones
en cintas, incluyendo retroceder, expulsar, saltar archivos y
bloques, etc.

%prep
%setup -q
%patch -p1 -b .buildroot

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{bin,sbin,usr/man/man1,usr/man/man8}
make install

%files
%defattr(-,root,root)
%doc COPYING README README.stinit mt-st-0.5b.lsm stinit.def.examples
/bin/mt
/sbin/stinit
/usr/man/man1/mt.1
/usr/man/man8/stinit.8

%changelog
* Mon Jun 14 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Feb 10 1999 Preston Brown <pbrown@redhat.com>
- upgrade to .5b, which fixes some cmd. line arg issues (bugzilla #18)

* Thu Jul 23 1998 Jeff Johnson <jbj@redhat.com>
- package for 5.2.

* Sun Jul 19 1998 Andrea Borgia <borgia@cs.unibo.it>
- updated to version 0.5
- removed the touch to force the build: no binaries are included!
- added to the docs: README.stinit, stinit.def.examples
- made buildroot capable

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
