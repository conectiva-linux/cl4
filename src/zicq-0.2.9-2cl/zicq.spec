Name: zicq
Version: 0.2.9
Release: 2cl
Summary: zicq is an ncurses based ICQ client for text mode unix
Summary(pt_BR): O zicq é um cliente ICQ baseado em ncurses para o modo texto do Unix
Summary(es): zicq is an ncurses based ICQ client for text mode unix
Copyright: redistributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: zicq-.2.9.tar.bz2
BuildRoot: /tmp/zicq-root

%description
This program is designed as a text mode unix ICQ since the only
ICQ client that will run on a unix box is the java version which is
slow and resource intensive.

%description -l pt_BR
O zicq é um cliente ICQ baseado em ncurses para o modo texto do Unix

%description -l es
This program is designed as a text mode unix ICQ since the only
ICQ client that will run on a unix box is the java version which is
slow and resource intensive.

%prep
%setup -q -n zicq-.2.9

%build
make
strip zicq

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 zicq $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
install -m 644 zicq.1 $RPM_BUILD_ROOT/usr/man/man1/zicq.1
%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc README commands.txt icq091.txt
/usr/bin/zicq
/usr/man/man1/zicq.1

%changelog
* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr 6 1999  Brian Bruns <bruns@Magenet.com>
- Update to .2.9
- Included man page

* Sat Mar 20 1999  Brian Bruns <bruns@Magenet.com>
- First build
