Summary: A security tool which provides authentication for applications.
Summary(pt_BR): Módulos de autenticação plugáveis (PAM)
Summary(es): Módulos de autentificación plugables (PAM)
Name: pam
Version: 0.66
Release: 21cl
Copyright: GPL or BSD
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: pam-redhat-%{version}.tar.bz2
Source1: other.pamd
Buildroot: /var/tmp/pam-root
Requires: cracklib, cracklib-dicts, pwdb >= 0.54-2
Obsoletes: pamconfig
Url: http://parc.power.net/morgan/Linux-PAM/index.html

%description
PAM (Pluggable Authentication Modules) is a system security tool
which allows system administrators to set authentication policy
without having to recompile programs which do authentication.

%description -l pt_BR
PAM (Módulos de Autenticação Plugáveis) é um poderoso, flexível e
extensível sistema de autenticação, que permite o administrador
do sistema configurar serviços de autenticação individualmente
para cada aplicação pam compatível, sem necessidade de recompilar
qualquer uma das aplicações.

%description -l es
PAM (Módulos de Autenticación Plugables) es un potente, flexible y
extensible sistema de autentificación, que permite al administrador
del sistema configurar servicios de autentificación individualmente
para cada aplicación pam compatible, sin la necesidad de recompilar
cualquier una de las aplicaciones.

%prep
%setup -q

%build
touch .freezemake
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/include/security
mkdir -p $RPM_BUILD_ROOT/lib/security
make install FAKEROOT=$RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/pam.d
install -m 644 other.pamd $RPM_BUILD_ROOT/etc/pam.d/other
gzip -9 $RPM_BUILD_ROOT/usr/man/man{5,8}/*
# make sure the modules built...
[ -f $RPM_BUILD_ROOT/lib/security/pam_deny.so ] || {
  echo "You have LITTLE or NOTHING in your /lib/security directory:"
  echo $RPM_BUILD_ROOT/lib/security/*
  echo ""
  echo "Fix it before you install this package, while you still can!"
  exit 1
}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir /etc/pam.d
%config /etc/pam.d/other
%doc Copyright
%doc doc/html doc/ps doc/txts
%doc doc/specs/rfc86.0.txt
/lib/libpam.so.0.*
/lib/libpam.so
/lib/libpam_misc.so.0.*
/lib/libpam_misc.so
/lib/libpam_misc.a
/usr/include/security/*.h
/sbin/*
/lib/security
%config /etc/security/access.conf
%config /etc/security/time.conf
%config /etc/security/group.conf
%config /etc/security/limits.conf
%config /etc/security/pam_env.conf
%config /etc/security/console.perms
%dir /etc/security/console.apps
%dir /var/lock/console
/usr/man/man5/*
/usr/man/man8/*

%changelog
* Thu Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- returning libpam.so and libpam_misc.so links.

* Wed Jun 30 1999 Guilherme Manika <gwm@conectiva.com>
- Removed libpam.so and libpam_misc.so from %files (no errors during install)
- Compressed manpages

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- recompressed sources

* Thu May 20 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Apr 17 1999 Michael K. Johnson <johnsonm@redhat.com>
- added video4linux devices to /etc/security/console.perms

* Fri Apr 16 1999 Michael K. Johnson <johnsonm@redhat.com>
- added joystick lines to /etc/security/console.perms

* Thu Apr 15 1999 Michael K. Johnson <johnsonm@redhat.com>
- fixed a couple segfaults in pam_xauth uncovered by yesterday's fix...

* Wed Apr 14 1999 Cristian Gafton <gafton@redhat.com>
- use gcc -shared to link the shared libs

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- many bug fixes in pam_xauth
- pam_console can now handle broken applications that do not set
  the PAM_TTY item.

* Tue Apr 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- fixed glob/regexp confusion in pam_console, added kbd and fixed fb devices
- added pam_xauth module

* Sat Apr 10 1999 Cristian Gafton <gafton@redhat.com>
- pam_lastlog does wtmp handling now

* Thu Apr 08 1999 Michael K. Johnson <johnsonm@redhat.com>
- added option parsing to pam_console
- added framebuffer devices to default console.perms settings

* Wed Apr 07 1999 Cristian Gafton <gafton@redhat.com>
- fixed empty passwd handling in pam_pwdb

* Mon Mar 29 1999 Michael K. Johnson <johnsonm@redhat.com>
- changed /dev/cdrom default user permissions back to 0600 in console.perms
  because some cdrom players open O_RDWR.

* Fri Mar 26 1999 Michael K. Johnson <johnsonm@redhat.com>
- added /dev/jaz and /dev/zip to console.perms

* Thu Mar 25 1999 Michael K. Johnson <johnsonm@redhat.com>
- changed the default user permissions for /dev/cdrom to 0400 in console.perms

* Fri Mar 19 1999 Michael K. Johnson <johnsonm@redhat.com>
- fixed a few bugs in pam_console

* Thu Mar 18 1999 Michael K. Johnson <johnsonm@redhat.com>
- pam_console authentication working
- added /etc/security/console.apps directory

* Mon Mar 15 1999 Michael K. Johnson <johnsonm@redhat.com>
- added pam_console files to filelist

* Fri Feb 12 1999 Cristian Gafton <gafton@redhat.com>
- upgraded to 0.66, some source cleanups

* Mon Dec 28 1998 Cristian Gafton <gafton@redhat.com>
- add patch from Savochkin Andrey Vladimirovich <saw@msu.ru> for umask
  security risk

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to ver 0.65
- build the package out of internal CVS server
