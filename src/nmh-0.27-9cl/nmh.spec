Summary: A capable mail handling system with a command line interface.
Summary(pt_BR): Novo Sistema MH de manipulação de mail
Summary(es): Nuevo Sistema MH de manipulación de mail
Name: nmh
Obsoletes: mh
Provides: mh
Version: 0.27
Release: 9cl
Requires: smtpdaemon
Copyright: freeware
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://ftp.math.gatech.edu/pub/nmh/nmh-0.27.tar.gz
Patch0: nmh-0.24-config.patch
Patch1: nmh-0.27-buildroot.patch
Patch2: nmh-0.27-security.patch
Patch3: nmh-0.27-compat21.patch
Buildroot: /var/tmp/%{name}-root

%description
Nmh is an email system based on the MH email system and is intended
to be a (mostly) compatible drop-in replacement for MH.  Nmh isn't
a single comprehensive program.  Instead, it consists of a number
of fairly simple single-purpose programs for sending, receiving,
saving, retrieving and otherwise manipulating email messages.  You
can freely intersperse nmh commands with other shell commands or
write custom scripts which utilize nmh commands.  If you want to use
nmh as a true email user agent, you'll want to also install exmh to
provide a user interface for it--nmh only has a command line interface.

If you'd like to use nmh commands in shell scripts, or if you'd like to
use nmh and exmh together as your email user agent, you should install
nmh.

%description -l pt_BR
Sistema de manipulação de mail nmh (com suporte POP). Nmh é um
popular sistema de manipulação de mail mas inclui somente uma
interface de comando de linha. Ele é uma base importante, contudo,
para programas como xmh e exmh.

%description -l es
Sistema de manejo de mail nmh (con soporte POP). Nmh es un popular
sistema de manejo de mail, pero incluye solamente una interface de
comando de línea. Es una importante base, todavía, para programas
como xmh y exmh.

%prep
%setup -q
%patch0 -p1 -b .config
%patch1 -p1 -b .buildroot
%patch2 -p1 -b .security
%patch3 -p1 -b .compat21

%build
LIBS=-lgdbm ./configure --prefix=/usr \
			--exec-prefix=/usr \
			--bindir=/usr/bin \
			--libdir=/usr/lib/nmh \
			--sysconfdir=/etc/nmh \
			--with-editor=/bin/vi

make

%install
DESTDIR=$RPM_BUILD_ROOT make install
strip `file $RPM_BUILD_ROOT/usr/bin/* | grep ELF | cut -d':' -f 1`

# XXX unnecessary because DOT_LOCKING is disabled
# chown root.mail $RPM_BUILD_ROOT/usr/bin/inc
# chmod 2755 $RPM_BUILD_ROOT/usr/bin/inc

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -d /usr/bin/mh -a ! -L /usr/bin/mh ] ; then
    ln -s . /usr/bin/mh
fi
if [ ! -d /usr/lib/mh -a ! -L /usr/lib/mh ] ; then
    ln -s nmh /usr/lib/mh
fi

%triggerpostun -- mh, nmh <= 0.27-7
if [ ! -d /usr/bin/mh -a ! -L /usr/bin/mh ] ; then
    ln -s . /usr/bin/mh
fi
if [ ! -d /usr/lib/mh -a ! -L /usr/lib/mh ] ; then
    ln -s nmh /usr/lib/mh
fi

%preun
if [ $1 = 0 ]; then
    [ ! -L /usr/bin/mh ] || rm -f /usr/bin/mh
    [ ! -L /usr/lib/mh ] || rm -f /usr/lib/mh
fi

%files
%defattr(-,root,root)
%doc COPYRIGHT DIFFERENCES FAQ MAIL.FILTERING README TODO VERSION ZSH.COMPLETION
%dir /usr/lib/nmh
%dir /etc/nmh
%config /etc/nmh/*
/usr/bin/*
/usr/lib/nmh/*
/usr/man/*/*

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Apr 18 1999 <ewt@redhat.com>
- fixed mh compatibility symlinks on removal

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Tue Jan 26 1999 Jeff Johnson <jbj@redhat.com>
- restore /usr/bin files to package.

* Wed Jan 13 1999 Jeff Johnson <jbj@redhat.com>
- fix reversed args in strncpy within security patch (#821).

* Sun Jan 10 1999 Jeff Johnson <jbj@redhat.com>
- turn off remnant setgid root.mail (which packaged as setgid root.root because
  of %defattr in %files) (bug #769).
- glibc-2.1 compatibility.

* Sat Jul 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 0.27 (security patches too)

* Sun May  3 1998 Alan Cox <alan@redhat.com>
- Fixed the obvious security holes. Im not sure I got them all, I may
  have broken a couple of things in the process. The code is such a 
  complete pile of donkey poo it is hard to be sure.
  
* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Apr 19 1998 Erik Troan <ewt@redhat.com>
- removed /usr/bin/mh and /usr/lib/mh from file list -- create them in
  scripts instead to avoid conflicts with the old mh package

* Sat Apr 11 1998 Donnie Barnes <djb@redhat.com>
- various spec file cleanups

* Wed Apr 8 1998 Bryan C. Andregg <bandregg@redhat.com>
- Fixed symlink install bug

* Tue Mar 31 1998 Bryan C. Andregg <bandregg@redhat.com>
- Added symlinks: /usr/bin/mh -> /usr/bin, /usr/lib/mh -> /usr/lib/nmh

* Wed Mar 25 1998 Bryan C. Andregg <bandregg@redhat.com>
- Initial build
