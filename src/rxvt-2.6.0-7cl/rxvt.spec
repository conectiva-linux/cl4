Summary: A color VT102 terminal emulator for the X Window System.
Summary(pt_BR): Emulador de terminal no X window - rxvt
Summary(es): Emulador de terminal en X window - rxvt
Name: rxvt
Serial: 3
Version: 2.6.0
Release: 7cl
Copyright: distributable
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
Source: ftp://babayaga.math.fu-berlin.de/rxvt/devel/%{name}-%{version}.tar.gz
Source1: rxvt.wmconfig
Source800: rxvt-wmconfig.i18n.tgz
Patch0: rxvt-2.6.PRE2.font.patch
Patch1: rxvt-2.6.0-utmp98.patch
Buildroot: /var/tmp/%{name}-root

%description
Rxvt is a color VT102 terminal emulator for the X Window System.
Rxvt is intended to be an xterm replacement for users who don't need
the more esoteric features of xterm, like Tektronix 4014 emulation,
session logging and toolkit style configurability.  Since it doesn't
support those features, rxvt uses much less swap space than xterm
uses.  This is a significant advantage on a machine which is serving
a large number of X sessions.

The rxvt package should be installed on any machine which serves a
large number of X sessions, if you'd like to improve that machine's
performance.

%description -l pt_BR
Rxvt é um emulador de terminal VT100 para X. Ele tem o objetivo
de ser um substituto de xterm(1) para usuários que não necessitam
das características mais esotéricas de xterm. Especificamente
rxvt não implementa a emulação Tektronix 4014, registro de sessão
e configurabilidade no estilo toolkit. Como resultado, rxvt usa
muito menos swap do que xterm - uma vantagem significativa em uma
máquina servindo várias sessões X.

%description -l es
Rxvt es un emulador de terminal VT100 para X. Tiene el objetivo
de ser un substituto de xterm(1) para usuarios que no necesiten de
las características más esotéricas de xterm. Específicamente rxvt
no implementa la emulación Tektronix 4014, registro de sesión y
configurabilidad en el estilo toolkit. Como resultado, rxvt usa
mucho menos swap del que xterm - una ventaja significativa en una
máquina sirviendo varias sesiones X.

%prep
%setup -q
%patch0 -p1 -b .font
%patch1 -p1 -b .utmp

%build
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" ./configure --prefix=/usr/X11R6 \
	--enable-utmp --enable-xpm-background \
	--enable-ttygid \
	--enable-transparency --enable-menubar --enable-xim \
	--enable-next-scroll --disable-backspace-key

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man1
make prefix=$RPM_BUILD_ROOT/usr/X11R6 install
install -m 644 doc/rxvt.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 644 $RPM_SOURCE_DIR/rxvt.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/rxvt

gzip -9f $RPM_BUILD_ROOT/usr/X11R6/man/man*/*


tar xvfpz $RPM_SOURCE_DIR/rxvt-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/*
/usr/X11R6/bin/rxvt
/usr/X11R6/bin/rclock
/usr/X11R6/man/man1/*
%config(missingok) /etc/X11/wmconfig/rxvt

%changelog
* Mon Jun 21 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- turn off some stuff in configure :) So the backspace, home, end, etc
  are now working
- compressed man pages

* Thu Jun 16 1999 Bill Nottingham <notting@redhat.com>
- turn on some stuff in configure

* Tue Jun 14 1999 Bill Nottingham <notting@redhat.com>
- use --enable-ttygid

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.6.0.
- add --enable-xgetdefault (#3309).

* Thu Mar 25 1999 Erik Troan <ewt@redhat.com>
- added unix98 pty support

* Wed Mar 24 1999 Erik Troan <ewt@redhat.com>
- updated for utmpwrap

* Tue Mar 23 1999 Michael Johnson <johnsonm@redhat.com>
- added back the "old" alt-< and alt-> font change behaviour
- put the manpage in the right place

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 2.6.PRE2.  Marked as unstable, but rxvt is always unstable...

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Wed Dec 30 1998 Jeff Johnson <jbj@redhat.com>
- fix glibc-2.1 utmpx compilation problem -- add -D_GNU_SOURCE (#638).

* Mon Dec 21 1998 Preston Brown <pbrown@redhat.com>
- bumped spec # for 6.0 build

* Wed Sep 30 1998 Bill Nottingham <notting@redhat.com>
- fix to enable keypad

* Tue Sep 08 1998 Cristian Gafton <gafton@redhat.com>
- version 2.4.7
- old version used to be called 2.20, so now we are Serial: 1

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- no paths in wmconfig files.

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- added wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 31 1997 Michael K. Johnson <johnsonm@redhat.com>
- make rxvt use standard XGetDefault instead of built-in one.
