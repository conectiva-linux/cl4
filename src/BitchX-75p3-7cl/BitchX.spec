%define	name BitchX
%define	BXvers	75p3
%define	release	7cl

Summary: Improved color IRC client with built-in scripts
Summary(pt_BR): Cliente IRC para o console do Linux
Summary(es): Improved color IRC client with built-in scripts
Name: %{name}
Version: %{BXvers}
Release: %{release}
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Copyright: GPL
URL: http://www.bitchx.org
Source0: ircii-pana-%{version}.tar.bz2
Source1: .config.h
Source2: ircII-4.4B-translation.tar.gz
Patch0:	BitchX.install_script.patch
Patch1:	BitchX.makefile.patch
Patch2:	BitchX.translation_path.patch
BuildRoot: /tmp/%{name}-%{version}
Requires: wserv
 
%description 
BitchX is a popular ANSI color ircII client by panasync. It
incorporates various features that would normally require a
script. It's interface is more colorful and cleaner than ircII.

%description -l pt_BR
O BitchX é um cliente de IRC com suporte a cores para o console
do Linux. Ele incorpora várias características que normalmente
requereriam um script, e a sua interface é mais colorida, e simples
de trabalhar que a do ircII :)

%description -l es
BitchX is a popular ANSI color ircII client by panasync. It
incorporates various features that would normally require a
script. It's interface is more colorful and cleaner than ircII.

%package -n wserv
Summary: Support program to IRC clients
Summary(pt_BR): Programa de suporte a clientes IRC
Summary(es): Support program to IRC clients
Version: 1.13
Release: 1cl
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Copyright: GPL
 
%description -n wserv
This is an support program to some IRC clients.

%description -l pt_BR -n wserv
Programa de suporte a clientes IRC

%description -l es -n wserv
This is an support program to some IRC clients.

%prep
%setup -q -n BitchX -a 2
%patch0 -p1
%patch1 -p1 -b .makefile
%patch2 -p1 -b .translation_path

cp -p $RPM_SOURCE_DIR/.config.h .

%ifarch i386
	EXTRA_CONFIG_FLAGS=--with-tcl
%endif

CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=/usr $EXTRA_CONFIG_FLAGS

%build
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ;fi
install -d -m 755 $RPM_BUILD_ROOT/usr/bin
install -d -m 755 $RPM_BUILD_ROOT/usr/man/man1
install -d -m 755 $RPM_BUILD_ROOT/usr/lib/bx/translation

install -m 644 translation/* $RPM_BUILD_ROOT/usr/lib/bx/translation

( cd source; strip BitchX wserv scr-bx; cd ..)

make prefix=$RPM_BUILD_ROOT/usr installbin

(cd $RPM_BUILD_ROOT/usr/bin;ln -sf BitchX-%{BXvers} BitchX;cd $RPM_BUILD_DIR)

install -m755 install-bitchx $RPM_BUILD_ROOT/usr/bin

install -m644 BitchX.ircnames $RPM_BUILD_ROOT/usr/lib/bx
install -m644 BitchX.quit $RPM_BUILD_ROOT/usr/lib/bx
install -m644 BitchX.reasons $RPM_BUILD_ROOT/usr/lib/bx

rm -r bitchx-docs/CVS
cp -r bitchx-docs/* $RPM_BUILD_ROOT/usr/lib/bx/help
install -m644 BitchX.help $RPM_BUILD_ROOT/usr/lib/bx/help

install -m644 BitchX.1.gz $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
%doc doc/* BitchX.1.gz BitchX.help BitchX.ircnames BitchX.quit BitchX.reasons Changes
/usr/bin/BitchX-%{BXvers}
/usr/bin/BitchX
/usr/bin/scr-bx
/usr/bin/install-bitchx
/usr/man/man1/BitchX.1.gz
/usr/lib/bx

%files -n wserv
/usr/bin/wserv

%changelog
* Tue Jun 29 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- moved wserv to a separate package

* Mon Jun 07 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- latin1 (for diacriticals)

* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Removed %post message

* Fri May 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added to Conectiva Linux
- Removed Serial tag

* Thu Apr  1 1999 Ryan Weaver <ryanw@infohwy.com>
  [BitchX-75p3-4]
- Mow including translation file from ircII-4.4B.

* Wed Mar 31 1999 Ryan Weaver <ryanw@infohwy.com>
  [BitchX-75p3-3]
- Added ifarch statment to build with the included tcl.o
  only if building on an i386.
- Made the sed script to build with cdrom support into a
  patch for Makefile.in
- Added patch to put ~/.BitchX before default script dir in Makefile.in
- Added patch to fix TRANSLATION_PATH in include/config.h, translation
  files not included. Get from ircII.
- Removed some old changlog entries in specfile.

* Wed Mar  3 1999 Jorge Godoy <jorge@bestway.com.br>
  [BitchX-75p3]
- Added pt_BR translation and support to specfile.

* Mon Mar  1 1999 Ryan Weaver <ryanw@infohwy.com>
  [BitchX-75p3]
- Updated to version 75p3 final.
- No listings in ChangeLog

