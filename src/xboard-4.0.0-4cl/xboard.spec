Summary: An X Window System graphical chessboard.
Summary(pt_BR): Interface X11 para o xadrez da GNU
Summary(es): Interface X11 para el ajedrez de la GNU
Name: xboard
Version: 4.0.0 
Release: 4cl
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://ftp.gnu.org/pub/gnu/xboard-4.0.0.tar.gz
Source800: xboard-wmconfig.i18n.tgz
Patch0: xboard-header.patch
Patch1: xboard-4.0.0-xref.patch
Copyright: GPL
BuildRoot: /var/tmp/xboard-root

%description
Xboard is an X Window System based graphical chessboard  which can be
used with the GNUchess and Crafty chess programs, with Internet Chess
Servers (ICSs), with chess via email, or with your own saved games.

Install the xboard package if you need a graphical chessboard.

%description -l pt_BR
xboard oferece a você uma interface gráfica fácil de usar para o
programa de xadrez da GNU, permitindo você aproveitar horas da ação
intelectual sem ter que aprender comandos complicados.

%description -l es
xboard te ofrece una interface gráfica fácil de usar para el programa
de ajedrez de GNU, permitiendo que aproveches horas de la ación
intelectual sin tener que aprender comandos complicados.

%prep
%setup -q 
%patch0 -p1 -b .orig
%patch1 -p1

%build
./configure --prefix=/usr
make

%install
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/xboard

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xboard <<EOF
xboard name "xboard"
xboard description "Chess"
xboard group Games/Strategy
xboard exec "xboard &"
EOF


tar xvfpz $RPM_SOURCE_DIR/xboard-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/xboard
/usr/bin/zic2xpm
/usr/bin/cmail
/usr/bin/pxboard
/usr/man/man6/xboard.6
/usr/man/man6/zic2xpm.6
/usr/man/man6/cmail.6
/usr/info/xboard.info
%config /etc/X11/wmconfig/xboard

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- cleaned up spec file
- built package for 6.0

* Sat Jul 11 1998 Mike Wangsmo <wanger@redhat.com>
- updated to a new version
- buildrooted the package too

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
