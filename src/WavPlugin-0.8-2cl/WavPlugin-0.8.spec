%define name WavPlugin
%define version 0.8
%define release 2cl

Summary: wave plugin for netscape
Summary(pt_BR): Plugin wave para o Netscape
Summary(es): Plugin wave para el Netscape
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: %{name}-%{version}.tar.bz2
Patch: %{name}-Makefile.patch
Provides: npwav.so
Requires: netscape-common
Buildroot: /var/tmp/%{name}-%{version}_root

%description
The Wave Plugin for netscape, that allows to hear wave/voc/snd files.

%description -l pt_BR
Plugin Wave para o Netscape. Permite ouvir arquivos wave/voc/snd.

%description -l es
El Plugin wave para netscape, permite oír archivos wave/voc/snd.

%changelog
* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- First build.
- Patch in Makefile for search libXaw3d

%prep
%setup -q -n WavPlugin

%patch -p1

%build
make clean
CFLAGS=$RPM_OPT_FLAGS make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/netscape/plugins
install -m 755 -s npwav.so $RPM_BUILD_ROOT/usr/lib/netscape/plugins/

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%files
/usr/lib/netscape/plugins/npwav.so
%doc README
