%define	name	gftp
%define	version	1.13
%define	release	2cl

Summary: gFTP is a multithreaded FTP client for X Windows written using Gtk.
Summary(pt_BR): Cliente FTP multithreaded para o X Window
Summary(es): Cliente FTP multithreaded para el X Windows
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
URL: http://www.newwave.net/~masneyb/
# was .gz
Source:	http://www.newwave.net/~masneyb/%{name}-%{version}.tar.bz2
Requires: gtk+ >= 1.1.12
BuildRoot: /tmp/%{name}-%{version}
Patch: gftp-config-patch

%description
gFTP is a multithreaded FTP client for X Windows written using Gtk.
It allows to have simultaneous downloads, resuming of interrupted
file transfers, file transfer queues, a very nice connection manager
and many more features.

%description -l pt_BR
O gftp é um cliente FTP multithreaded para o X Window escrito usando a
biblioteca gtk. Permite transferir arquivos simultâneamente, continuar
transferências interrompidas, filas para transferências de arquivos e um
gerenciador de conexões muito bom e muitas outras características.

%description -l es
Cliente FTP multithreaded para el X Windows.

%prep
%setup -q
%patch -p1

%build
CFLAGS=$RPM_OPT_FLAGS \
	./configure --prefix=/usr/X11R6
make

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,/share/gftp}
make PREFIX=$RPM_BUILD_ROOT/usr/X11R6 install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING COPYING.LIB Makefile.in README TODO eplf.txt rfc959.txt
/usr/X11R6/bin/gftp
/usr/X11R6/share/gftp

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 3 1999 Guilherme Manika <gwm@conectiva.com>
- gftprc mais novo, conserta o problema de não achar http.xpm

* Wed Mar 31 1999 Ryan Weaver <ryanw@infohwy.com>
  [gftp-1.13-1]
- Added graphical configuration
- Uses a lot less memory
- Separated all ftp code into gnome-ftp library
- Now prompts the user to reconnect on connect error
- Added much more efficient transfer dialog for when the files exist
- Added local and remote chmod support
- Added support for HTTP proxies
- Added another FTP proxy type
- Added support for EPLF directory listings
- Now uses a configure script to generate the makefile
- Added Save Password feature in the connection manager
- Added more keyboard shortcuts
- Various bug fixes
- Improved internal design

* Tue Feb 16 1999 Ryan Weaver <ryanw@infohwy.com>
  [gftp-1.12-1]
- Added the ability to edit local and remote files
- Added the ability to associate with a file extension a file viewer
  and the default download type (ASCII or BINARY).
- Added anti-idle tool. Please do not abuse this feature
- Better remote symlink handling
- Removed some icons from the distribution
- Added another FTP proxy type
- Several small enhancements
