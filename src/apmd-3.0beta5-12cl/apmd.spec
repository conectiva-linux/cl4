Summary: Advanced Power Management (APM) BIOS utilities for laptops.
Summary(pt_BR): Utilitários para APM (Gerenciamento Avancado de Energia)
Summary(es): Utilitarios para APM (Gestión Avanzado de Energía)
Name: apmd
Version: 3.0beta5
Release: 12cl
Source: ftp://ftp.debian.org/debian/dists/frozen/main/source/admin/%{name}_%{version}-1.tar.gz
Source1: apmd.init
Source18: apmd.init.i18n
Patch1: apmd-buildroot.patch
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires: chkconfig >= 0.9
Prereq: chkconfig
BuildRoot: /var/tmp/%{name}-root
ExclusiveArch: i386

%description
This is a Advanced Power Management daemon and utilities.
It can watch your notebook's battery and warn all users when the battery
is low.

Patches to Rik Faith's original version have been added for shutting down
the PCMCIA sockets before a suspend.

%description -l pt_BR
Utilitários e servidor para gerenciamento avançado de energia (APM).
Ele verifica a bateria de seu notebook e avisa aos usuários que
ele está com pouca carga.

Foi adicionado um patch nao oficial para parar os soquetes PCMCIA
antes de uma suspensao de energia.

%description -l es
Utilitarios y servidor para gestión avanzada de energía (APM).
Verifica la batería de tu notebook y avisa a los usuarios cuando
la carga es poca.  Fue adicionado un patch no oficial para parar
los enchufes PCMCIA antes de una suspensión de energía.

%prep
%setup -q -n apmd
%patch1 -p1 -b .buildroot

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,include,lib,sbin,man/man1,man/man8,X11R6/bin,X11R6/man/man1}
make RPM_BUILD_ROOT=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
install -m 755 $RPM_SOURCE_DIR/apmd.init.i18n $RPM_BUILD_ROOT/etc/rc.d/init.d/apmd

cat <<'EOF' >$RPM_BUILD_ROOT/etc/sysconfig/apmd
APMD_OPTIONS="-p 10 -w 5 -W"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add apmd

%preun
if [ "$1" = "0" ] ; then
	/sbin/chkconfig --del apmd
fi

%files
%defattr(-,root,root)
%doc ANNOUNCE ChangeLog README README.transfer LSM
/usr/man/man1/*
/usr/man/man8/*
#/usr/X11R6/bin/*
#/usr/X11R6/man/man1/*
/usr/bin/*
/usr/sbin/*
/usr/include/*
/usr/lib/*
%config /etc/rc.d/init.d/apmd
%config /etc/sysconfig/apmd

%changelog
* Sun Jun 20 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- apmd.init.i18n
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- add check for /proc/apm (not on SMP) (#3403)

* Mon May 31 1999 Jeff Johnson >jbj@redhat.com>
- shell script tweak (#3176).

* Fri May  7 1999 Bill Nottingham <notting@redhat.com>
- set -u flag for utc

* Sat Apr 17 1999 Matt Wilson <msw@redhat.com>
- prereqs chkconfig

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- exlusive arch i3786, as sparcs and alphas have no apm support...

* Wed Apr 14 1999 <ewt@redhat.com>
- removed X bits; gnome has a much better X interface for apm anyway

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- quoted APMD_OPTIONS variable in the init script

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- whoops, making /etc/rc.d/init.d/apmd a directory was a bad idea. fixed.

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- now owned by Avery Pennarun <apenwarr@debian.org>, upgraded to his latest.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- updated to latest patchlevel from web page.

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced init script

* Thu Apr 1 1998 Erik Troan <ewt@redhat.com>
- moved init script into a separate source file
- added restart and status options to initscript
- made it use a build root
- don't start apm when the package is installed
- don't stop apm when the package is removed

* Mon Dec  8 1997 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Compiled on RH5.0 against libc6.
- Renamed /etc/rc.d/init.d/apmd.init to /etc/rc.d/init.d/apmd
- Make /etc/rc.d/init.d/apmd to be chkconfig-compliant.

* Thu Oct  2 1997 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Fixed buggy /etc/sysconfig/apmd file generation in the spec file.
- Added a patch for apm.c's option handling.
- Both fixes were submitted by Richard D. McRobers <rdm@csn.net>
