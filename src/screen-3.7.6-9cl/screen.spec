Summary: A screen manager that supports multiple logins on one terminal.
Summary(pt_BR): Screen - Gerencia múltiplas sessões em um tty
Summary(es): Screen - Administra múltiples sesiones en un tty
Name: screen
Version: 3.7.6
Release: 9cl
Copyright: distributable
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://prep.ai.mit.edu/pub/gnu/screen-%{version}.tar.gz
Patch2: screen-3.7.6-compat21.patch
Patch3: screen-3.7.6-unix98.patch
Patch4: screen-3.7.6-utempter.patch
Patch5: screen-nowarn.patch
Prereq: /sbin/install-info
BuildRoot: /var/tmp/%{name}-root

%description
The screen utility allows you to have multiple logins on just one
terminal.  Screen is useful for users who telnet into a machine or
are connected via a dumb terminal, but want to use more than just
one login.

Install the screen package if you need a screen manager that can
support multiple logins on one terminal.

%description -l pt_BR
Screen é um programa que permite que você tenha múltiplos logins em
um terminal. Ele é útil em situações onde você está usando telnet
em uma máquina ou conectado via um terminal dumb e quer mais do
que apenas um login.

%description -l es
Screen es un programa que permite que tengas múltiples logins en un
terminal. Es útil en situaciones donde estás usando telnet en una
máquina o conectado vía un terminal dumb y quiera más que apenas
un login.

%prep
%setup -q

%patch2 -p1 -b .compat21
%patch3 -p1 -b .unix98
%patch4 -p1 -b .utempter
%patch5 -p1 -b .nowarn

%build
./configure --prefix=/usr
sed -e "s|.*#.*def.*PTYMODE .*|#define PTYMODE 0620|g" config.h > config.foo
sed -e "s|.*#.*def.*PTYGROUP .*|#define PTYGROUP 5|g" config.foo > config.h
rm -f config.foo
make CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -DETCSCREENRC=\\\"/etc/screenrc\\\""

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/skel

perl -pi -e 's,/usr/local/etc/screenrc,/etc/screenrc,' etc/etcscreenrc

make prefix=$RPM_BUILD_ROOT/usr install

( cd $RPM_BUILD_ROOT
  gzip -9nf ./usr/info/screen.info*
  strip ./usr/bin/screen

  rm -f ./usr/bin/screen.old ./usr/bin/screen
  mv ./usr/bin/screen-%{version} ./usr/bin/screen
)

install -c -m 0444 etc/etcscreenrc $RPM_BUILD_ROOT/etc/screenrc
install -c -m 0644 etc/screenrc $RPM_BUILD_ROOT/etc/skel/.screenrc

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/screen.info.gz /usr/info/dir --entry="* screen: (screen).             Terminal multiplexer."

if [ -d /tmp/screens ]; then
    # we're not setuid root anymore
    chmod 777 /tmp/screens
fi

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/screen.info.gz /usr/info/dir --entry="* screen: (screen).             Terminal multiplexer."
fi

%files
%defattr(-,root,root)
%doc NEWS README FAQ

%attr(755,root,root) /usr/bin/screen
/usr/man/man1/screen.1
/usr/info/screen.info*

%config /etc/screenrc
%config /etc/skel/.screenrc

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun 16 1999 Bill Nottingham <notting@redhat.com>
- force tty permissions/group

* Wed Jun 5 1999 Dale Lovelace <dale@redhat.com>
- permissions on /etc/skel/.screenrc to 644

* Mon Apr 26 1999 Bill Nottingham <notting@redhat.com>
- take out warning of directory permissions so root can still use screen

* Wed Apr 07 1999 Bill Nottingham <notting@redhat.com>
- take out warning of directory ownership so root can still use screen

* Wed Apr 07 1999 Erik Troan <ewt@redhat.com>
- patched in utempter support, turned off setuid bit

* Fri Mar 26 1999 Erik Troan <ewt@redhat.com>
- fixed unix98 pty support

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Mar 11 1999 Bill Nottingham <notting@redhat.com>
- add patch for Unix98 pty support

* Mon Dec 28 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.7.6.

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- upgraded to 3.7.4

* Wed Oct 08 1997 Erik Troan <ewt@redhat.com>
- removed glibc 1.99 specific patch

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- added install-info support

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
