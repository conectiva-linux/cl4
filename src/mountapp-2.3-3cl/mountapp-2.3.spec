%define name mountapp
%define version 2.3
%define release 3cl

Summary: A Window Maker dock app which simplifies managing mountable devices
Summary(pt_BR): Aplicação do WindowMaker para montar disquetes e CDs
Summary(es): Applet para montaje de CDs y discos flexibles
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
BuildRoot: /var/tmp/%{name}-%{version}_root
Source: http://mountapp.netpedia.net/%{name}-%{version}.tar.bz2
Source800: mountapp-wmconfig.i18n.tgz
Patch: %{name}-%{version}-PropList.patch
URL: http://mountapp.netpedia.net

%description
This is a Window Maker dock app which allows you to browse all your mount
points and to mount/unmount devices in a simple point and click manner.

%description -l pt_BR
Permite que sejam facilmente montados discos flexíveis e CDs a partir
do dock do Window Maker.

%description -l es
Applet para montaje de CDs y discos flexibles

%changelog
* Fri Jun 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Removed some %defines to cope with rpm 3.0.1

* Wed Mar 31 1999 Conectiva <dist@conectiva.com>
- added wmconfig

* Mon Mar 22 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added pt_BR translations
- Moved the root for /usr/X11R6

* Mon Jan 11 1999 Paul Johnson <pauljohn@ukans.edu>
-Added Buildroot to keep build out of /usr/X11R6 directory, allow nonroot to
rebuild.

%prep

%setup
%patch -p1

%build
export PLPATH=/usr/X11R6/lib
./configure --prefix=/usr/X11R6 --exec-prefix=/usr/X11R6 --datadir=/usr/X11R6/share
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	exec-prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	bindir=$RPM_BUILD_ROOT/usr/X11R6/bin \
	datadir=$RPM_BUILD_ROOT/usr/X11R6/share \
	install-strip

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig









tar xvfpz $RPM_SOURCE_DIR/mountapp-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root)
/usr/X11R6/bin/mount.app
/usr/X11R6/bin/mount.conf
/usr/X11R6/share/mount.app
%config(missingok) /etc/X11/wmconfig/mountapp

%doc TODO README INSTALL THANKS AUTHORS COPYING NEWS ChangeLog
