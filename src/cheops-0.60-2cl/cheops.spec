%define name cheops
%define version 0.60
%define release 2cl
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
# was .gz
Source: ftp://ftp.marko.net/pub/cheops/%{name}-%{version}pre1.tar.bz2
Patch: cheops-0.59a-new-ucd.patch
Summary: Cheops Network User Interface
Summary(pt_BR): Um "canivete suíço" para trabalhar em rede
Summary(es): Interface de red Cheops
Buildroot: /var/tmp/cheops-buildroot

%description
Cheops is a network "swiss army knife".  It's "network neighborhood" done right
(or gone out of control, depending on your perspective).  It's a combination
of a variety of network tools to provide system adminstrators and users with
a simple interface to managing and accessing their networks.  Cheops aims to
do for the network what the file manager did for the filesystem.

%description -l pt_BR
O Cheops é um "canivete suíço" para redes. Ele é baseado em uma variedade de
ferramentas de rede que provêm uma interface simples de configurar a rede, e
visualizá-la, ao administrador, e aos seus usuários.

%description -l es
El Cheops es una herramienta de configuración de red para el Linux.

%prep
%setup -q -n %{name}-%{version}pre1
%patch -p1
%build
./configure --prefix=/usr
make

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/X11R6/bin
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/cheops/plugins
mkdir -p ${RPM_BUILD_ROOT}/usr/share/cheops
install -s cheops ${RPM_BUILD_ROOT}/usr/X11R6/bin
install pixmaps/*.xpm cheops.conf services.conf ${RPM_BUILD_ROOT}/usr/share/cheops
install plugins/*.so ${RPM_BUILD_ROOT}/usr/lib/cheops/plugins

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(755, root, root)
%attr(644,root,root) %doc COPYING README Changelog
/usr/X11R6/bin/cheops
%dir /usr/share/cheops/
%dir /usr/lib/cheops
%attr(644,root,root) /usr/share/cheops/*
%attr(644,root,root) /usr/lib/cheops/plugins

%changelog
* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr 13 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added to Conectiva Linux 3.0 Server edition
- Updated package to version 0.60pre1
- Added Marcelo's patch to compile with new ucd-snmp

* Sat Feb 20 1999 Marcelo Tosatti <marcelo@conectiva.com>
- added pt_BR translations

* Wed Jan 6 1999 Mark A. Spencer <markster@marko.net
- Updated to cheops 0.59

* Fri Dec 12 1998 Mark A. Spencer <markster@marko.net>
- Update to new cheops with plugin support

* Wed Dec 9 1998 Mark A. Spencer <markster@marko.net>
- Remove setuid permissions from cheops

* Mon Dec 7 1998 Mark A. Spencer <markster@marko.net>
- Fix permissions problems and incorporate RPM fixes from Tom <x@4t2.com>

* Sun Dec 6 1998 Mark A. Spencer <markster@marko.net>
- Initial Release.
