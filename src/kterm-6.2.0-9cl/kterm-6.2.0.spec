Summary: A Kanji (Japanese character set) terminal emulator for X.
Summary(pt_BR): Kterm (Emulador de Terminal Kanji)
Summary(es): Kterm (Emulador de Terminal Kanji)
Name: kterm
Version: 6.2.0
Release: 9cl
Source: ftp://ftp.sunet.se/pub/X11/R6contrib/applications/kterm-6.2.0.tar.gz
Source1: kterm.wmconfig
Source800: kterm-wmconfig.i18n.tgz
Patch0: kterm-6.2.0-kbd.patch
Patch1: kterm-6.2.0-glibc.patch
Patch2: kterm-6.2.0-utmp98.patch
Copyright: distributable
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
Buildroot: /var/tmp/kterm-root
Requires: /usr/sbin/utempter

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 26 1999 Erik Troan <ewt@redhat.com>
- added unix98 pty support

* Wed Mar 24 1999 Erik Troan <ewt@redhat.com>
- added utemper support
- turn off setuid bit

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Thu Jan  7 1999 Bill Nottingham <notting@redhat.com>
- built for glibc2.1
- this package doesn't change much, does it?

* Fri May 01 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixed build problems for manhattan

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- updated source
- added wmconfig entries
- fixed source url

* Tue Oct 07 1997 Erik Troan <ewt@redhat.com>
- needed patch for glibc on the alpha as TIOCSLTC is defined for OSF 
  compatibility

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%description
The kterm package provides a terminal emulator for the Kanji Japanese
character set.

Install kterm if you need a Kanji character set terminal emulator.
You'll also need to have the X Window System installed.

%description -l pt_BR
kterm é o Emulador de Terminal Kanji. Ele usa o conjunto de
caracteres Kanji ao invés do conjunto normal de inglês para aqueles
que preferem Kanji.

%description -l es
kterm es el Emulador de Terminal Kanji. Usa el conjunto de caracteres
Kanji en lugar del conjunto normal de inglés para aquellos que
prefieran Kanji.

%prep
%setup
%patch0 -p1 -b .kbd
%patch1 -p1 -b .glibc
%patch2 -p1 -b .utempter

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 644 -o root -g root $RPM_SOURCE_DIR/kterm.wmconfig \
	$RPM_BUILD_ROOT/etc/X11/wmconfig/kterm
chmod 755 $RPM_BUILD_ROOT/usr/X11R6/bin/kterm



tar xvfpz $RPM_SOURCE_DIR/kterm-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
/usr/X11R6/bin/kterm
/usr/X11R6/lib/X11/app-defaults/KTerm
/usr/X11R6/man/man1/kterm.1x
/etc/X11/wmconfig/kterm

%clean
rm -rf $RPM_BUILD_ROOT
