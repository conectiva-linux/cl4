Summary: Sets the system to use either a local terminal or a serial console.
Summary(pt_BR): Alterna um sistema entre vídeo local consoles seriais
Summary(es): Alterna un sistema entre vídeo local consolas seriales
Name: setconsole
Version: 1.0
Release: 9cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: setconsole-1.0.tar.gz
Patch: setconsole-1.0.patch
Exclusiveos: Linux
Requires: /bin/sh
Requires: textutils
Requires: grep
Requires: sed
BuildArchitectures: noarch
BuildRoot: /var/tmp/setconsole-root

%description
Setconsole is a basic system utility for setting up the /etc/inittab,
/dev/systty and /dev/console files to handle a new console.  The
console can be either the local terminal (i.e., directly attached to
the system via a video card) or a serial console.

%description -l pt_BR
setconsole configura /etc/inittab, /dev/systty e /dev/console para um
novo console. O console pode ser tanto o terminal local (diretamente
ligado no sistema via uma placa de vídeo) ou um console serial.

%description -l es
setconsole configura /etc/inittab, /dev/systty y /dev/pantalla para
una nueva consola. Tanto puede ser el terminal local (directamente
encendido en el sistema vía una tarjeta de vídeo) o una consola
serial.

%prep
%setup -q
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}

install -m755 setconsole $RPM_BUILD_ROOT/usr/sbin/setconsole
install -m644 setconsole.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/setconsole
/usr/man/man8/setconsole.8

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed spec file wrt rpm 3.0.2

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)

* Thu Feb 11 1999 Michael Maher <mike@redhat.com>
- merged Jakub's changes into the regular 6.0 stuff.

* Wed Nov 04 1998 Jakub Jelinek <jj@ultra.linux.cz>
- with 2.1 /dev/console, a lot of things are not needed any more.

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
