Summary: An X terminal locking program.
Summary(pt_BR): Programa para bloquear o terminal X com vários salvadores de tela
Summary(es): Programa para bloquear el terminal X con varios protectores de pantalla
Name: xlockmore
Version: 4.14
Release: 1cl
Copyright: MIT
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
# was .gz
Source0: ftp://ftp.tux.org/pub/tux/bagleyd/xlockmore/xlockmore-%{version}.tar.bz2
Source1: m-redhat.xpm
Source2: m-redhat.xbm
Source3: s-redhat.xpm
Source4: s-redhat.xbm
Source5: xlock.pamd
Source800: xlockmore-wmconfig.i18n.tgz
Patch2: xlockmore-4.14-fortune.patch
Patch3: xlockmore-4.14-conectiva.patch
Patch4: xlockmore-4.14-noship.patch
Patch5: xlockmore-4.14-useMesa.patch
Requires: pam >= 0.59
Requires: fortune-mod
Buildroot: /var/tmp/xlockmore-buildroot

%description
The xlockmore utility is an enhanced version of the standard xlock
program, which allows you to lock an X session so that other users
can't access it.  Xlockmore runs a provided screensaver until you type
in your password.

Install the xlockmore package if you need a locking program to secure
X sessions.

%description -l pt_BR
Uma versão melhorada do xlock que permite a você manter outros usuários
longe de sua sessão X enquanto você está afastado da máquina. Ele
roda um dos vários protetores de tela enquanto aguarda você entrar
com a sua senha, desbloqueando a sessão e voltando ao X.

%description -l es
Una versión mejorada del xlock que te permite mantener otros usuarios
lejos de tu sesión X mientras estás alejado de la máquina. Se ejecuta
en uno de los varios protectores de pantalla mientras aguarda que
entres con tu contraseña, desbloqueando la sesión y volviendo al X.

%prep
%setup -q
%patch2 -p1 -b .fortune
#%patch3 -p1 -b .redhat
%patch4 -p1 -b .noship
%patch5 -p1 -b .mesaGL

cp $RPM_SOURCE_DIR/m-redhat.xpm pixmaps/m-redhat.xpm
cp $RPM_SOURCE_DIR/m-redhat.xbm bitmaps/m-redhat.xbm
cp $RPM_SOURCE_DIR/m-redhat.xpm pixmaps/l-redhat.xpm
cp $RPM_SOURCE_DIR/m-redhat.xbm bitmaps/l-redhat.xbm
cp $RPM_SOURCE_DIR/s-redhat.xpm pixmaps/s-redhat.xpm
cp $RPM_SOURCE_DIR/s-redhat.xbm bitmaps/s-redhat.xbm

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6 \
	--without-motif --without-gtk --enable-pam
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
make install prefix=$RPM_BUILD_ROOT/usr/X11R6 xapploaddir=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/
install -m 644 ${RPM_SOURCE_DIR}/xlock.pamd $RPM_BUILD_ROOT/etc/pam.d/xlock

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig


tar xvfpz $RPM_SOURCE_DIR/xlockmore-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/pam.d/xlock
/usr/X11R6/bin/xlock
/usr/X11R6/man/man1/xlock.1
%config /usr/X11R6/lib/X11/app-defaults/XLock
%config /etc/X11/wmconfig/xlock

%changelog
* Sat Jun 26 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 4.14

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 17 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 17 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- upgraded from 4.11 to 4.13 for Conectiva Linux
- i18n wmconfig

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- update to 4.12

* Tue Oct 13 1998 Cristian Gafton <gafton@redhat.com>
- take out some modules to avoid TMv

* Fri Sep 18 1998 Bill Nottingham <notting@redhat.com>
- turned PAM support on in ./configure 

* Fri Sep 11 1998 Preston Brown <pbrown@redhat.com>
- Upgraded to 4.11

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Donnie Barnes <djb@redhat.com>
- upgraded to 4.09
- removed Michael's PAM patch (it's now available in the sources)

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- upgrade to 4.05
- add wmconfig

* Mon Oct 13 1997 Michael K. Johnson <johnsonm@redhat.com>
- Upgraded to 4.04
- Changed pam to new conventions
- Use configure instead of imake
- buildroot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- moved from pam.conf to pam.d

