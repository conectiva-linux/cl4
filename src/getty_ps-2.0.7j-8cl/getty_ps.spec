Summary: The getty and uugetty programs.
Summary(pt_BR): Getty e uugetty
Summary(es): Getty y uugetty
Name: getty_ps
Version: 2.0.7j
Copyright: Distributable - Copyright 1989,1990 by Paul Sutcliffe Jr.
Release: 8cl
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
Source: ftp://tsx-11.mit.edu/pub/linux/sources/sbin/getty_ps-2.0.7j.tar.gz
Source700: getty_ps-man-pt_BR.tar
Patch0: getty_ps-2.0.7j-make.patch
Patch1: getty_ps-2.0.7h-jpm.patch
Patch2: getty_ps-2.0.7h-pipe.patch
Patch3: getty_ps-2.0.7j-glibc.patch
Patch4: getty_ps-2.0.7j-signal.patch
Patch5: getty_ps-2.0.7j-6.0.patch
Buildroot: /var/tmp/getty_ps-root

%description
The getty_ps package contains the getty and uugetty programs, basic
programs for accomplishing the login process on a Red Hat Linux system.
Getty and uugetty are used to accept logins on the console or a terminal.
Getty is invoked by the init process to open tty lines and set their modes,
to print the login prompt and get the user's name, and to initiate a login
process for the user.  Uugetty works just like getty, except that uugetty
creates and uses lock files to prevent two or more processes from
conflicting in their use of a tty line.  Getty and uugetty can also handle
answer a modem for dialup connections, but mgetty is recommended for that
purpose.

%description -l pt_BR
Getty e uugetty são usados para aceitar logins na console ou em
terminal. Eles podem tratar respostas de modem em conexões discadas
(embora mgetty seja o recomendado para este propósito).

%description -l es
Getty y uugetty se usan para aceptar logins en la pantalla o en
terminal. Pueden manejar respuestas de módem en conexiones marcadas
(no obstante mgetty es lo más recomendado para este propósito).

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin \
	$RPM_BUILD_ROOT/usr/man/man1 $RPM_BUILD_ROOT/usr/man/man5 \
	$RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/var/log

%setup -q
%patch0 -p1 -b .make
%patch1 -p1 -b .jpm
%patch2 -p1 -b .pipe
%patch3 -p1 -b .noglibc
%patch4 -p1 -b .signal
%patch5 -p1 -b .6.0

%build
make clean
RPM_OPT_FLAGS="$RPM_OPT_FLAGS" make

%install
TOPDIR=$RPM_BUILD_ROOT make install

install -m 644 Examples/gettydefs.high-speed $RPM_BUILD_ROOT/etc/gettydefs

( cd $RPM_BUILD_ROOT
  chmod 755 ./sbin/getty ./sbin/uugetty
  ln -sf getty.1 ./usr/man/man1/uugetty.1
#  touch ./var/log/getty.log
)





mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/getty_ps-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%postun
if [ $1 = 0 ]; then
  rm -f /var/log/getty.log
fi

%files
%defattr(-,root,root)
%doc Examples ANNOUNCE README.linux README.2.0.7j README.hi-speed
%config /etc/gettydefs
/sbin/getty
/sbin/uugetty
/usr/man/man1/*
/usr/man/man5/gettydefs.5
#%ghost /var/log/getty.log
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- explicitly remove log file on package removal.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Mon Jan 23 1999 Michael Maher <mike@redhat.com>
- changed group name, ran thru system

* Thu Dec 17 1998 Michael Maher <mike@redhat.com> 
- rebuilt for 6.0 
- added patch to remove STRDUP

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- rebuilt to include doco.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Mar 26 1997 Erik Troan <ewt@redhat.com>
- Ported to glibc (I don't know where the last glibc package came from)
- Rebuilt because it was last built against some broken SPARC headers. 
