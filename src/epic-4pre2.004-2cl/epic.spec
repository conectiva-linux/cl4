Summary: Enhanced console IRC client
Summary(pt_BR): Cliente IRC para a console
Summary(es): Enhanced console IRC client
Name: epic
Version: 4pre2.004
Release: 2cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: ftp://ftp.epicsol.org/pub/ircii/EPIC4-ALPHA/epic4pre2.004-19990507.tar.bz2
BuildRoot: /var/tmp/epic-tmp/
Requires: wserv

%description
EPIC is a enhanced console IRC client almost fully backwards-compatible
with the irc][ client.

%description -l pt_BR
O EPIC é um cliente IRC avançado para console, quase completamente compatível
com o cliente irc][.

%description -l es
EPIC is a enhanced console IRC client almost fully backwards-compatible
with the irc][ client.

%prep
%setup -n ircii-EPIC4pre2.004

%build
CFLAGS=-O2 ./configure --prefix=/usr
make

%install
rm -fr $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/epic-EPIC4pre2.004-19990507
mv -f $RPM_BUILD_ROOT/usr/bin/epic-EPIC4pre2.004-19990507 $RPM_BUILD_ROOT/usr/bin/epic
strip $RPM_BUILD_ROOT/usr/libexec/wserv
gzip -9 $RPM_BUILD_ROOT/usr/man/man1/epic.1

%clean
rm -fr $RPM_BUILD_ROOT

%files
/usr/bin/epic
/usr/man/man1/epic.1.gz
/usr/share/epic/
%doc doc/*

%changelog
* Tue Jun 15 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Removed wserv, which is now on a separate package

* Fri May 28 1999 Guilherme Manika <gwm@conectiva.com>
- Versão inicial

