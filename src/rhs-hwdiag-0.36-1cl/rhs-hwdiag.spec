Summary: Red Hat utilities for probing and diagnosing system hardware.
Summary(pt_BR): Utilitário de diagnóstico e investigação de Hardware Red Hat
Summary(es): Utilitario de diagnóstico e investigación de Hardware Red Hat
Name: rhs-hwdiag
Version: 0.36
Release: 1cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: rhs-hwdiag-%{PACKAGE_VERSION}.tar.gz
Url: http://www.redhat.com/~msf/#hwdiag
Requires: newt >= 0.8
BuildRoot: /var/tmp/hwdiag-root
# I haven't tested this on Sparc or Alpha, please let me know if it works
Exclusivearch: i386 alpha armv4l

%description
The rhs-hwdiag package contains the Red Hat Hardware Discovery
Tools.  These tools probe the serial and parallel ports on your
system, and are useful for finding and reporting hardware errors
to Red Hat support if you're having problems.  These tools could
cause adverse side-effects in some situations, so you should use
them carefully.

%description -l pt_BR
Um pacote de utilitários que lista dispositivos do sistema. É
suportada a detecção de dispositivos PnP seriais e paralelos. Útil
para reportar problemas de hardware.

%description -l es
Un paquete de utilitarios que lista dispositivos del sistema. Está
soportada la detección de dispositivos PnP seriales y paralelos. Útil
para reportar problemas de hardware.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun 16 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 12 1999 Bill Nottingham <notting@redhat.com>
- add a warning about running under X

* Thu Mar 11 1999 Bill Nottingham <notting@redhat.com>
- fix PS/2 probing

* Tue Jan 19 1999 Bill Nottingham <notting@redhat.com>
- don't link against libgpm

* Sun Jan 10 1999 Matt Wilson <msw@redhat.com>
- link against libgpm now that we have mouse support

* Sun Jan 10 1999 Matt Wilson <msw@redhat.com>
- Rebuilt for newt 0.40

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- Raw Hide build (slang-1.2.2)
- buildrooted (!)

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Fri Nov  7 1997 Michael Fulbright <msf@redhat.com>

- made an official package

* Fri May 30 1997 Michael Fulbright <msf@redhat.com>

- Added /etc/printcap to output file
- Added copyright statements and GPL 'COPYING' file
- current version if 0.15beta

%prep
%setup

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin

install -m 755 -s Diagnostics/hwdiag $RPM_BUILD_ROOT/usr/bin/
install -m 755 -s Serial/pnp_serial $RPM_BUILD_ROOT/usr/bin/
install -m 755 -s ParPort/pnp_parport $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING
/usr/bin/hwdiag
/usr/bin/pnp_serial
/usr/bin/pnp_parport
