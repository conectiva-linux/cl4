Summary: A small utility for safely making /tmp files.
Summary(pt_BR): Programa de segurança feito para arquivos tmp
Summary(es): Programa de seguridad hecho para archivos tmp
Name: mktemp
%define version 1.5
Version: %{version}
Release: 2cl
Copyright: BSD
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.openbsd.org/pub/OpenBSD/src/usr.bin/mktemp-%{version}.tar.gz
Patch: mktemp-1.4-linux.patch
Patch1: mktemp-1.5-man.patch
Url: http://www.openbsd.org
Buildroot: /var/tmp/mktemp

%description
The mktemp utility takes a given file name template and overwrites
a portion of it to create a unique file name.  This allows shell
scripts and other programs to safely create and use /tmp files.

Install the mktemp package if you need to use shell scripts or other
programs which will create and use unique /tmp files.

%description -l pt_BR
O mktemp é um pequeno utilitário que faz interface para a função do
sistema mktemp() para permitir que scripts shell e outros programas
usem arquivos no /tmp com segurança.

%description -l es
mktemp es un pequeño utilitario que hace de interface para la
función del sistema mktemp() para permitir que scripts shell y
otros programas usen archivos en /tmp con seguridad.

%prep
%setup
%patch -p1
%patch1 -p1

%build
make

%install
mkdir -p /var/tmp/mktemp/usr/bin /var/tmp/mktemp/usr/man/man1
make ROOT="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
/bin/mktemp
/usr/man/man1/mktemp.1

%changelog
* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Erik Troan <ewt@redhat.com>
- sync'd man page with openbsd latest, and updated it for some Linux-specific
  changes

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 01 1997 Erik Troan <ewt@redhat.com>
- moved to /bin

