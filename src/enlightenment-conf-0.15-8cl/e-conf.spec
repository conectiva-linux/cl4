# Note that this is NOT a relocatable package
%define ver      0.15
%define rel      8cl
%define prefix   /usr

Summary: Enlightenment Configuration applet.
Summary(pt_BR): Aplicativo para configuração do Enlightenment
Summary(es): Aplicación para configurar el Enlightenment.
Name: enlightenment-conf
Version: %ver
Release: %rel
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source0: ftp://www.rasterman.com/pub/enlightenment/enlightenment-conf-%{ver}.tar.bz2
Source1: enlightenment-conf-pt_BR.po
BuildRoot: /var/tmp/e-conf-%{PACKAGE_VERSION}-root

URL: http://www.rasterman.com
Requires: control-center >= 1.0.0

Patch0: enlightenment-conf-0.15-keybind.patch
Patch1: enlightenment-conf-0.15-pt_BR.patch

%description
A Configuration tool for easily setting up Enlightenment

%description -l pt_BR
Aplicativo para configuração do Enlightenment

%description -l es
Aplicación para configurar el Enlightenment.

%prep
%setup -q
%patch0 -p1 -b .noscrollbar
%patch1 -p1 -b .pt_BR

%build

cp $RPM_SOURCE_DIR/enlightenment-conf-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
unset LINGUAS
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

# strip binaries
strip `file $RPM_BUILD_ROOT/%{prefix}/bin/* | awk -F':' '/executable/ { print $1 }'`

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/share/locale/*/*/*


%changelog
* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- unset LINGUAS

* Sat Jun 12 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries

* Tue Feb 23 1999 The Rasterman <raster@redhat.com>
- Updated to 0.14

* Wed Feb 3 1999 The Rasterman <raster@redhat.com>
- Created for new E-conf standalone module
