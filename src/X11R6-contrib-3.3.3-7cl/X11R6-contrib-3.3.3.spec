Summary: Programs for X11 from the contrib tapes
Summary(pt_BR): Programas para X11 do contrib
Summary(es): Programas para X11 del contrib
Name: X11R6-contrib
Version: 3.3.3
Release: 7cl
Copyright: MIT
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
Source0: fpt://ftp.xfree86.org/pub/XFree86/3.3.2/sources/X333contrib.tar.bz2
Source800: X11R6-contrib-wmconfig.i18n.tgz
Patch1: x11r6-contrib-3.1.2-rhs.patch
Patch2: x11r6-contrib-3.1.2-mandoc.patch
Patch3: x11r6-contrib-3.1.2-sparc.patch
Patch4: X11R6-contrib-3.3.1-pthreads.patch
BuildRoot: /var/tmp/X11R6-contrib-root
Summary(de): Programme für X11 aus den contrib-Bändern 
Summary(fr): Programmes pour X11 venant des contribs
Summary(tr): X11 daðýtýmýna dýþarýdan saðlanan programlar

%description
This is a collection of X programs from X11R6's contrib tape, which contains
programs contributed by various users. It includes listres, xbiff, xedit,
xeyes, xcalcm, xload, and xman amoung others.

%description -l pt_BR
Esta é uma coleção de programas X do contrib X11R6, que contém
programas contribuídos por vários usuários. Inclui listres, xbiff,
xedit, xeyes, xcalcm, xload e xman além de outros.

%description -l es
Esta es una colección de programas X del contrib X11R6, que contiene
programas contribuidos por varios usuarios. Incluye listres, xbiff,
xedit, xeyes, xcalc, xload y xman además de otros.

%description -l de
Dies ist eine Sammlung von X-Programmen aus dem contrib tape von X11R6,
das Programme verschiedener Benutzer enthält, u.a. listres, xbiff, xedit,
xeyes, xcalcm, xload und xman.

%description -l tr
Bu paket, çeþitli kullanýcýlarýn X11 için hazýrladýklarý bir program
koleksiyonudur. xbiff, xedit, xeyes, xcalcm, xload, ve xman gibi programlarý
içerir.

%prep
%setup -c -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cd contrib
xmkmf -a
make

%install
rm -rf $RPM_BUILD_ROOT

cd contrib
make DESTDIR=$RPM_BUILD_ROOT install install.man

( cd $RPM_BUILD_ROOT
# xload doesn't need to be setuid
  chmod u-s ./usr/X11R6/bin/xload
)

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/






tar xvfpz $RPM_SOURCE_DIR/X11R6-contrib-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/ico
/usr/X11R6/bin/listres
/usr/X11R6/bin/showfont
/usr/X11R6/bin/viewres
/usr/X11R6/bin/xbiff
/usr/X11R6/bin/xcalc
/usr/X11R6/bin/xditview
/usr/X11R6/bin/xedit
/usr/X11R6/bin/xev
/usr/X11R6/bin/xeyes
/usr/X11R6/bin/xfontsel
/usr/X11R6/bin/xgc
/usr/X11R6/bin/xload
/usr/X11R6/bin/xman
/usr/X11R6/bin/xmessage

%config /usr/X11R6/lib/X11/app-defaults/Viewres
%config /usr/X11R6/lib/X11/app-defaults/XCalc
%config /usr/X11R6/lib/X11/app-defaults/XCalc-color
%config /usr/X11R6/lib/X11/app-defaults/XFontSel
%config /usr/X11R6/lib/X11/app-defaults/XLoad
%config /usr/X11R6/lib/X11/app-defaults/Xditview
%config /usr/X11R6/lib/X11/app-defaults/Xditview-chrtr
%config /usr/X11R6/lib/X11/app-defaults/Xedit
%config /usr/X11R6/lib/X11/app-defaults/Xgc
%config /usr/X11R6/lib/X11/app-defaults/Xman
%config /usr/X11R6/lib/X11/app-defaults/Xmessage

/usr/X11R6/lib/X11/xman.help

/usr/X11R6/man/man1/ico.1x
/usr/X11R6/man/man1/listres.1x
/usr/X11R6/man/man1/showfont.1x
/usr/X11R6/man/man1/viewres.1x
/usr/X11R6/man/man1/xbiff.1x
/usr/X11R6/man/man1/xcalc.1x
/usr/X11R6/man/man1/xditview.1x
/usr/X11R6/man/man1/xedit.1x
/usr/X11R6/man/man1/xev.1x
/usr/X11R6/man/man1/xeyes.1x
/usr/X11R6/man/man1/xfontsel.1x
/usr/X11R6/man/man1/xgc.1x
/usr/X11R6/man/man1/xload.1x
/usr/X11R6/man/man1/xman.1x
/usr/X11R6/man/man1/xmessage.1x

%config /etc/X11/wmconfig/xcalc
%config /etc/X11/wmconfig/xditview
%config /etc/X11/wmconfig/xedit
%config /etc/X11/wmconfig/xeyes
%config /etc/X11/wmconfig/xfontsel
%config /etc/X11/wmconfig/xload
%config /etc/X11/wmconfig/xman

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Thu Nov 26 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- rebuild for 3.3.3

* Sat Nov 14 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- applied patch for 3.3.2Zb

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- updated to 3.3.2

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig
