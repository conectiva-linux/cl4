Summary: A set of X Window System screensavers.
Summary(pt_BR): Salvadores de tela X
Summary(es): Protectores de pantalla X
Name: xscreensaver
Version: 3.14
Release: 1cl
Copyright: BSD
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
URL: http://www.jwz.org/xscreensaver/
Source: http://www.jwz.org/xscreensaver/xscreensaver-%{version}.tar.bz2
Source800: xscreensaver-wmconfig.i18n.tgz
Patch0: xscreensaver-2.34-noseguy.patch
Patch1: xscreensaver-bsod.patch
Buildroot: /var/tmp/xscreensaver-root

%description
The xscreensaver package contains a variety of screensavers for your
mind-numbing, ambition-eroding, time-wasting, hypnotized viewing
pleasure.

Install the xscreensaver package if you need screensavers for use with
the X Window System.

%description -l pt_BR
Protetores de tela de todos os tipos estão incluídos neste pacote,
garantindo horas de divertimento para o seu monitor. E se você
realmente está inclinado à proteção do seu monitor, existe aquele
velho clássico, a "tela preta".

%description -l es
En este paquete están incluidos protectores de pantalla, de todos
los tipos, garantizando horas de diversión para tu monitor. Y si
realmente estás inclinado a la protección de tu monitor, existe
aquel antiguo y clásico protector, la "pantalla negra".

%prep
%setup -q
%patch0 -p1 -b .noseguy
%patch1 -p1 -b .bsod

%build
RPMOPTS=""
%ifarch alpha
RPMOPTS="--without-xshm-ext"
%endif
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6 \
	--without-motif --without-gl --with-pam $RPMOPTS \
	--enable-subdir=../lib/xscreensaver
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man1
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/xscreensaver
make prefix=$RPM_BUILD_ROOT/usr/X11R6 \
   AD_DIR=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults \
   HACKDIR=$RPM_BUILD_ROOT/usr/X11R6/lib/xscreensaver \
   PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d \
   install-strip

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xscreensaver <<EOF
xscreensaver name "xscreensaver (1min timeout)"
xscreensaver description "xscreensaver"
xscreensaver group "Amusements/Screen Savers"
xscreensaver exec "xscreensaver -timeout 1 -cycle 1 &"
EOF



tar xvfpz $RPM_SOURCE_DIR/xscreensaver-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(missingok) /etc/pam.d/xscreensaver
%config(missingok) /etc/X11/wmconfig/xscreensaver
%attr(0755,root,root) /usr/X11R6/bin/xscreensaver
/usr/X11R6/bin/xscreensaver-command
/usr/X11R6/bin/xscreensaver-demo
%config /usr/X11R6/lib/X11/app-defaults/XScreenSaver
/usr/X11R6/man/man1/*
/usr/X11R6/lib/xscreensaver

%changelog
* Wed Jun 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 3.09 to 3.14
- sources recompressed

* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue May  4 1999 Bill Nottingham <notting@redhat.com>
- removed previously introduced security problem.

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- kill setuid the Right Way(tm)

* Mon Apr 12 1999 Bill Nottingham <notting@redhat.com>
- fix xflame on alpha

* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 3.09, fixes vmware interaction problems.

* Mon Apr  5 1999 Bill Nottingham <notting@redhat.com>
- remove setuid bit. Really. I mean it.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Bill Nottingham <notting@redhat.com>
- kill setuid, since pam works OK

* Tue Mar 16 1999 Bill Nottingham <notting@redhat.com>
- update to 3.08

* Wed Feb 24 1999 Bill Nottingham <notting@redhat.com>
- wmconfig returns, and no one is safe...

* Tue Feb 23 1999 Bill Nottingham <notting@redhat.com>
- remove bsod from random list because it's confusing people???? *sigh*

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- call libtoolize to get it to compile cleanely on the arm

* Tue Jan  5 1999 Bill Nottingham <notting@redhat.com>
- update to 3.07

* Mon Nov 23 1998 Bill Nottingham <notting@redhat.com>
- update to 3.06

* Tue Nov 17 1998 Bill Nottingham <notting@redhat.com>
- update to 3.04

* Thu Nov 12 1998 Bill Nottingham <notting@redhat.com>
- update to 3.02
- PAMify

* Tue Oct 13 1998 Cristian Gafton <gafton@redhat.com>
- take out Noseguy module b/c of possible TMv
- install modules in /usr/X11R6/lib/xscreensaver
- don't compile support for xshm on the alpha
- properly buildrooted
- updated to version 2.34

* Fri Aug  7 1998 Bill Nottingham <notting@redhat.com>
- update to 2.27

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Mon Jun 08 1998 Erik Troan <ewt@redhat.com>
- added fix for argv0 buffer overflow

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Donnie Barnes <djb@redhat.com>
- updated from 2.10 to 2.16
- added buildroot

* Wed Oct 25 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- new version, configure

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

