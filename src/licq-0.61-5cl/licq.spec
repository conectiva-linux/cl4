Name: licq
Version: 0.61
Release: 5cl
Summary: An ICQ clone and more for Unix
Summary(pt_BR): O licq é um clone do ICQ(tm) escrito em c++ usando biblioteca Qt.
Summary(es): licq es un clone del ICQ(tm) escrito en c++ usando biblioteca Qt.
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
URL: http://licq.wibble.net/
Source: ftp://ftp.wibble.net/pub/licq/srcs/licq-%{version}.tar.bz2
Source2: licq.wmconfig
Source3: licq.mini-icon.xpm
Source4: licq.sh
Source5: licq.xpm
Source800: licq-wmconfig.i18n.tgz
Patch: licq-ss.patch
Requires: qt => 1.42
BuildRoot: /tmp/%{name}-%{version}

%changelog
* Wed Jun 30 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed
- man page compressed

* Thu Jun 24 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added one more icon

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 10 1999 Conectiva <dist@conectiva.com>
- Recompiled for qt 1.44

* Sat Mar 27 1999 Conectiva <dist@conectiva.com>
- licq.sh to startup licq from wm menus

* Sat Mar 13 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 12 1999 Alexey Nogin <ayn2@cornell.edu>
[licq-0.61-1]
- Fixed Auto Away - Auto N/A problem.

* Tue Mar  9 1999 Alexey Nogin <ayn2@cornell.edu>
[licq-0.61-1]
- Incorporated numerous small changes inspired 
by Graham Roff's (Licq author) version of the spec file

* Mon Feb 22 1999 Alexey Nogin <ayn2@cornell.edu>
[licq-0.60-1]
- Added viewurl-*.sh to /usr/bin/

* Mon Dec 14 1998 Alexey Nogin <ayn2@cornell.edu>
[licq-0.50-alpha-2]
- Updated the URL

* Fri Dec 11 1998 Alexey Nogin <ayn2@cornell.edu>
[licq-0.50-alpha-1]
- Added SPEC file %defattr directive to enable non-root builds
- Changed SPEC file according to RHCN rules.

* Fri Oct 30 1998  Ian Macdonald <ianmacd@xs4all.nl>
- Upgraded to 0.44

%description
Licq is an ICQ clone written in C++ using the Qt widget set.  It
implements all major features of ICQ including messaging, urls, chat,
file transfer, and user information. In addition, Licq is highly
configurable and has support for skins and different icon packs.

%description -l pt_BR
O licq é um clone do ICQ(tm) escrito em c++ usando biblioteca Qt.
É uma tentativa de dar aos usuários do Linux uma opção não-java
para o protocolo ICQ.

%description -l es
licq es un clone del ICQ(tm) escrito en c++ usando biblioteca Qt.
Es un intento de dar a los usuarios de Linux una opción no-java
para el protocolo ICQ.

%prep
%setup
%patch -b .ss
autoheader
autoconf

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix="$RPM_BUILD_ROOT/usr" install
mkdir -p $RPM_BUILD_ROOT/{usr/share/icons/mini,etc/X11/wmconfig}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/wmconfig/licq
install %{SOURCE3} $RPM_BUILD_ROOT/usr/share/icons/mini/licq-mini.xpm
install %{SOURCE5} $RPM_BUILD_ROOT/usr/share/icons/licq.xpm
install contrib/viewurl-*.sh $RPM_BUILD_ROOT/usr/bin

install -m755 $RPM_SOURCE_DIR/licq.sh $RPM_BUILD_ROOT/usr/bin

gzip -9 $RPM_BUILD_ROOT/usr/man/man?/*


tar xvfpz $RPM_SOURCE_DIR/licq-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%attr (-,root,root) %doc doc/* contrib
%defattr (644,root,root)
%config /etc/X11/wmconfig/licq 
%attr(755,root,root) /usr/bin/licq*
/usr/share/licq-base.tar.gz
/usr/share/icons/mini/licq-mini.xpm
/usr/share/icons/licq.xpm
/usr/man/man?/*
%attr(755,root,root) /usr/bin/viewurl-*.sh
