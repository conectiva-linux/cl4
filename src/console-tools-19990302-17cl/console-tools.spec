Summary: Linux console tools
Summary(pt_BR): Ferramentas de console para o Linux
Summary(es): Linux console tools
Name: console-tools
%define	CTVER	1999.03.02
Version: 19990302
Release: 17cl
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Exclusiveos: Linux
Copyright: GPL
URL: http://www.multimania.com/ydirson/en/lct/
Source0: ftp://metalab.unc.edu/pub/Linux/system/keyboards/console-tools-%{CTVER}.tar.gz
Source1: keytable.init
Source2: ftp://ftp.dementia.org/pub/linux/pc2sun.pl
Source3: console-tools-1998.08.11.add-ons-nosk.tar.gz
Source4: console-tools-1998.08.11.sunfonts.tar.gz
Source5: kbd-0.96-turkish.tar.gz
Source6: kbd-ro.map.gz
Source7: kbd-sr.map.gz
Source8: ucw-fonts-1.1.1.tar.gz
Source9: kbd-0.96-latin0.tar.gz
Source10: kbd-0.96-amiga.tar.gz
Source11: sunt4-no-latin1.map.gz
Source12: lat2u-font.tar.gz
Source13: data-addon.tar.gz
Source14: br-abnt.kmap.gz
Source15: br-abnt2.kmap.gz
Source16: us-acentos.kmap.gz
Source17: us.kmap.gz
Patch0: console-tools-1998.08.11.resizecons.patch
Patch1: console-tools-1998.08.11.sparc.patch
Patch2: console-tools-1998.08.11.sparc2.patch
Patch3: console-tools-1999.03.02.sparc3.patch
Patch4: console-tools-1998.08.11.kmaps.patch
Patch5: console-tools.fonts.patch
# Allow consolechars & loadkeys to run from the root partition
Patch6: console-tools-rootpart.patch
# Add /etc/sysconfig/console (without subdirs) to the search path
Patch7: console-tools-searchpath.patch
Patch8: console-tools.fonts2.patch
Patch9: console-tools.fonts3.patch

Prereq: chkconfig fileutils sed
Obsoletes: kbd
Provides: kbd
Buildroot: /var/tmp/%{name}-root

%description
This package contains utilities to load console fonts and
keyboard maps.  It also includes a number of different fonts
and keyboard maps.

%description -l pt_BR
Este pacote contém utilitários para fontes do console e
mapas de teclado. Ele também inclui várias fontes e teclados
diferentes.

%description -l es
This package contains utilities to load console fonts and
keyboard maps.  It also includes a number of different fonts
and keyboard maps.

%prep

%ifarch m68k
%setup -q -n console-tools-%{CTVER} -a 3 -a 4 -a 5 -a 8 -a 9 -a 10 -a 12 -a 13
%else
%setup -q -n console-tools-%{CTVER} -a 3 -a 4 -a 5 -a 8 -a 9 -a 12 -a 13
%endif

%ifarch sparc sparc64
%patch1 -p1
%patch2 -p1
%patch3 -p1
%endif

%patch5 -p0
%patch6 -p1 -b .rootpart
%patch7 -p1 -b .searchpath
%patch8 -p1 -b .fonts2
%patch9 -p1 -b .fonts3

cp -p consolefonts/latin5-16.psf data/consolefonts # kbd-0.96-turkish.tar.gz
cp -p consoletrans/latin5 data/consoletrans
cp -p keymaps/i386/qwerty/trf.map data/keymaps/i386/qwerty/trf.kmap

%build
[ "$LINGUAS" ] && unset LINGUAS
%ifarch i386
DISABLE_RESIZECONS=
%else
DISABLE_RESIZECONS=--disable-resizecons
%endif

CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" ./configure --prefix=/usr \
  --datadir='${prefix}/lib/kbd' --enable-localdatadir=/etc/sysconfig/console \
  $DISABLE_RESIZECONS
make CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" LDFLAGS=-s prefix=/usr

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

make install prefix=$RPM_BUILD_ROOT/usr

# XXX hotwire some fonts on sun
%ifarch sparc sparc64
XXXFONTS="
    RUSCII_8x14.psf.gz RUSCII_8x16.psf.gz RUSCII_8x8.psf.gz
    koi8u-8x14.psf.gz koi8u-8x16.psf.gz koi8u-8x8.psf.gz
    lat2u-16.psf.gz latin5-16.psf.gz 
    ucw08.psf.gz  ucw11m.psf.gz ucw11z.psf.gz ucw16.psf.gz
"
make -C data/consolefonts $XXXFONTS
for F in $XXXFONTS
do
  install -c -m 0644 data/consolefonts/$F $RPM_BUILD_ROOT/usr/lib/kbd/consolefonts/$F
done
%endif

file $RPM_BUILD_ROOT/usr/bin/* | grep ELF | cut -f 1 -d ':' | xargs strip

# don't give loadkeys SUID perms
chmod 755 $RPM_BUILD_ROOT/usr/bin/loadkeys

# other keymaps
for map in ro sr ; do
   install -m 644 $RPM_SOURCE_DIR/kbd-$map.map.gz \
      $RPM_BUILD_ROOT/usr/lib/kbd/keymaps/i386/qwerty/$map.map.gz
done

install -m 644 $RPM_SOURCE_DIR/sunt4-no-latin1.map.gz \
	$RPM_BUILD_ROOT/usr/lib/kbd/keymaps/sun/sunt4-no-latin1.map.gz

install -d -m 755 $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d -m 755 $RPM_BUILD_ROOT/etc/rc.d/rc{2,3,5}.d

install -m 755 $RPM_SOURCE_DIR/keytable.init $RPM_BUILD_ROOT/etc/rc.d/init.d/keytable
ln -sf ../init.d/keytable $RPM_BUILD_ROOT/etc/rc.d/rc2.d/S75keytable
ln -sf ../init.d/keytable $RPM_BUILD_ROOT/etc/rc.d/rc3.d/S75keytable
ln -sf ../init.d/keytable $RPM_BUILD_ROOT/etc/rc.d/rc5.d/S75keytable

mkdir -p $RPM_BUILD_ROOT/bin
for foo in loadkeys consolechars ; do
  mv $RPM_BUILD_ROOT/usr/bin/$foo $RPM_BUILD_ROOT/bin
  ln -s ../../bin/$foo $RPM_BUILD_ROOT/usr/bin/$foo
done

%ifarch sparc
install -m 755 $RPM_SOURCE_DIR/pc2sun.pl $RPM_BUILD_ROOT/usr/lib/kbd/keytables
%endif

%ifnarch i386
rm -f $RPM_BUILD_ROOT/usr/man/man8/resizecons.8
%endif

chmod +x $RPM_BUILD_ROOT/usr/lib/*.so*

# Using the maps from casantos with some modifications
for MAP in br-abnt.kmap.gz br-abnt2.kmap.gz us-acentos.kmap.gz us.kmap.gz
do
	install -m644 -o root -g root $RPM_SOURCE_DIR/$MAP \
		$RPM_BUILD_ROOT/usr/lib/kbd/keymaps/i386/qwerty/
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add keytable
if [ -f /etc/sysconfig/keyboard ] ; then
    . /etc/sysconfig/keyboard
    if [ -n "$KEYTABLE" ] ; then
        KT=`echo $KEYTABLE | sed -e "s/.*\///g" | sed -e "s/\..*//g"`
        echo "KEYTABLE=$KT" > /etc/sysconfig/keyboard
    fi
fi
if [ -f /etc/sysconfig/i18n ] ; then
   . /etc/sysconfig/i18n
   if [ -d /etc/sysconfig/console ] ; then
      if [ -n "$SYSFONT" ]; then
         cp -f /usr/lib/kbd/consolefonts/$SYSFONT* /etc/sysconfig/console
      fi
      if [ -n "$UNIMAP" ]; then
         cp -f /usr/lib/kbd/consoletrans/$UNIMAP* /etc/sysconfig/console
      fi
      if [ -n "$SYSFONTACM" ]; then 
         cp -f /usr/lib/kbd/consoletrans/$SYSFONTACM* /etc/sysconfig/console
      fi
   fi
fi

%preun
if [ $1 = 0 ]; then
   /sbin/chkconfig --del keytable
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)

%doc README NEWS RELEASE BUGS TODO
%doc doc/[cdf]* doc/keymaps doc/README* doc/*.txt

%config /etc/rc.d/init.d/keytable
%config(missingok) /etc/rc.d/rc2.d/S75keytable
%config(missingok) /etc/rc.d/rc3.d/S75keytable
%config(missingok) /etc/rc.d/rc5.d/S75keytable

/usr/lib/*
/bin/consolechars
/bin/loadkeys
/usr/bin/charset
/usr/bin/chvt
/usr/bin/codepage
/usr/bin/consolechars
/usr/bin/deallocvt
/usr/bin/dumpkeys
/usr/bin/fgconsole
%ifarch i386
/usr/bin/fix_bs_and_del
%endif
/usr/bin/getkeycodes
/usr/bin/kbd_mode
/usr/bin/loadkeys
/usr/bin/loadunimap
/usr/bin/mk_modmap
/usr/bin/mapscrn
/usr/bin/psfaddtable
/usr/bin/psfgettable
/usr/bin/psfstriptable
%ifarch i386
/usr/bin/resizecons
%endif
/usr/bin/saveunimap
/usr/bin/screendump
/usr/bin/setfont
/usr/bin/setkeycodes
/usr/bin/setleds
/usr/bin/setmetamode
/usr/bin/setvesablank
/usr/bin/showcfont
/usr/bin/showkey
/usr/bin/unicode_start
/usr/bin/unicode_stop
/usr/bin/vcstime
/usr/bin/vt-is-UTF8
/usr/bin/writevt

/usr/man/man1/*
/usr/man/man4/*
/usr/man/man5/*
/usr/man/man8/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- rename our maps from .map.gz to .kmap.gz

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 04 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- included CTRL-arrow bindings to us, us-acentos, br-abnt and br-abnt2

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- unset LINGUAS

* Mon May 31 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- included our console maps

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- make keytable %post handle us.map better

* Thu Apr 15 1999 Jeff Johnson <jbj@redhat.com>
- hotwire sun fonts.

* Wed Apr 14 1999 Bill Nottingham <notting@redhat.com>
- %post changes; just copy the user's configured font/map/etc.

* Wed Apr 14 1999 Matt Wilson <msw@redhat.com>
- added fonts RUSCII_*, koi8u_*, and acm koi8u2ruscii from
  Leon Kanter <leon@geon.donetsk.ua>

* Mon Apr 12 1999 Bill Nottingham <notting@redhat.com>
- removed sh-utils from prereq.
- added sed to prereq

* Fri Apr  9 1999 Jeff Johnson <jbj@redhat.com>
- more latin2 fonts (Peter Ivanyi).

* Thu Apr  8 1999 Bill Nottingham <notting@redhat.com>
- added sh-utils to prereq.

* Mon Apr  5 1999 Bill Nottingham <notting@redhat.com>
- /etc/sysconfig/console support
- add setsysfont to init script

* Mon Mar 29 1999 Peter Ivanyi <ivanyi@internet.sk>
- more fixes.

* Thu Mar 25 1999 Peter Ivanyi <ivanyi@internet.sk>
- add ucw-fonts-1.1.tar.gz
- delete obsolete sk keymaps from console-tools-1998.08.11.add-ons.

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- added norwegian sun4 keymap support

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 1999.03.02.

* Tue Feb 16 1999 Jeff Johnson <jbj@redhat.com>
- repackage for Red Hat 6.0

* Wed Jan 30 1999 Alex deVries <puffin@redhat.com>
- added amiga support for Jes Sorensen

* Mon Dec 07 1998 Jakub Jelinek <jj@ultra.linux.cz>
- some keymaps were including "*.map", which has to be
  replaced by "*.kmap"

* Fri Dec 04 1998 Jakub Jelinek <jj@ultra.linux.cz>
- upgrade to console-tools, added new sun keymaps,
  new sun fonts for latin0/1 and latin2, iso15.acm
  and iso02+euro.acm.
- Print the verbose messages only if verbose was 
  specified on command line.

* Thu Oct 01 1998 Cristian Gafton <gafton@redhat.com>
- added Euro (latin0) support from Guylhem Aznar

* Sun Sep 27 1998 Cristian Gafton <gafton@redhat.com>
- fix the name the ro and sr maps are installed under
- slovak keymaps
- ro.map and sr.map are welcomed to the club
- enable turkish again

* Mon Aug 24 1998 Cristian Gafton <gafton@redhat.com>
- KEYTABLE should not have the full patch name (%post hack)

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- install keymaps on tty0 w/o using (non-installed) open(1).

* Tue Jul 14 1998 Jeff Johnson <jbj@redhat.com>
- updated to 0.96a.

* Thu Jun 11 1998 Mikael Hedin <micce@irf.se>
- specify VT0 in case we use a serial console

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- quotes permit multiple keytables in keytable.init (problem #675)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Donnie Barnes <djb@redhat.com>
- added some extra turkish support

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixes for building on alpha
- completed buildroot usage

* Thu Apr 23 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscript

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 0.95

* Wed Mar 25 1998 Erik Troan <ewt@redhat.com>
- fixed /tmp exploit

* Wed Nov 05 1997 Donnie Barnes <djb@redhat.com>
- added SPARC stuff (finally!), Thanks to eduardo@medusa.es for most of it.
- added buildroot
- cleaned up the file list
- moved to rev 5 because the contrib ver rel was 4

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- updated from 0.91 to 0.94
- added chkconfig support
- spec file cleanups

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
