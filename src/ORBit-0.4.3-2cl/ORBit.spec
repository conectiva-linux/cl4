%define ver     0.4.3
%define rel      2cl
%define prefix  /usr

Summary: High-performance CORBA Object Request Broker.
Summary(pt_BR): Corretor de requisições de objetos CORBA de alta performance.
Summary(es): Object Request Broker CORBA de alto desempeño
Name: ORBit
Version: %ver
Release: %rel
Source: ftp://ftp.labs.redhat.com/pub/ORBit/ORBit-%{PACKAGE_VERSION}.tar.bz2
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Copyright: LGPL/GPL
BuildRoot: /var/tmp/orbit-%{PACKAGE_VERSION}-root
Prefix: %{prefix}
Prereq: info

%description
ORBit is a high-performance CORBA ORB (object request
broker). It allows programs to send requests and 
receive replies from other programs, regardless of
the locations of the two programs.

You will need to install this package and the
related header files, libraries and utilities
if you want to write programs that use CORBA
technology.

%description -l pt_BR
O ORBit é um ORB (Corretor de Requisições de Objetos)
CORBA de alta performance. Permite a programas enviar e
receber respostas de outros programas, não importa a
localização destes dois programas.

Você precisará instalar este pacote e os arquivos de
inclusão relacionados se deseja desenvolver programas que
usem tecnologia CORBA.

%description -l es
Object Request Broker CORBA de alto desempeño

%package devel
Summary: Development libraries, header files and utilities for ORBit.
Summary(pt_BR): Bibliotecas, arquivos de inclusão e utilitários para desenvolvimento com o ORBit
Summary(es): Object Request Broker CORBA de alto desempeño - desarrollo
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
ORBit is a high-performance CORBA ORB (object request
broker) with support for the C language. It allows
programs to send requests and receive replies from
other programs, regardless of the locations of the
two programs.

This package contains the header files, libraries and 
utilities necessary to write programs that use CORBA
technology.

%description -l pt_BR devel
O ORBit é um ORB (Corretor de Requisições de Objetos)
CORBA de alta performance. Permite a programas enviar e
receber respostas de outros programas, não importa a
localização destes dois programas.

Este pacote contém arquivos de inclusão, bibliotecas
e utilitários necessários ao desenvolvimento de programas
que usem a tecnologia CORBA.

%description -l es devel
Object Request Broker CORBA de alto desempeño - desarrollo

%prep
%setup

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS
./configure --prefix=%prefix --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}
make prefix=$RPM_BUILD_ROOT%{prefix} install

ldconfig -n $RPM_BUILD_ROOT%{prefix}/lib

strip $RPM_BUILD_ROOT%{prefix}/bin/* || :

gzip -9 $RPM_BUILD_ROOT%{prefix}/info/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{prefix}/lib/lib*.so.*
%{prefix}/bin/orbit-event-server
%{prefix}/bin/orbit-name-server
%{prefix}/bin/old-name-server
%{prefix}/bin/name-client
%{prefix}/bin/orbit-ird

%files devel
%{prefix}/bin/orbit-idl
%{prefix}/bin/orbit-config
%{prefix}/include/*
%{prefix}/info/libIDL.info.gz
%{prefix}/lib/lib*.a
%{prefix}/lib/lib*.so

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 29 1999 Guilherme Manika <gwm@conectiva.com>
- Updated ORBit to 0.4.3

* Sun Mar 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- unset LINGUAS

* Thu Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- version 0.4.1 and 0.4.2 in one day, woohoo!

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations (kinda ;)
- Forced package to be compiled with egcs and optimization flags

* Mon Feb 22 1999 Michael Fulbright <drmike@redhat.com>
- unlibtoolize

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- updated to version 0.3.98

* Fri Feb 05 1999 Michael Fulbright <drmike@redhat.com>
- updated to version 0.3.97

* Fri Feb 05 1999 Michael Fulbright <drmike@redhat.com>
- updated to version 0.3.96

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- updated to version 0.3.91

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated for GNOME freeze, version 0.3.90

* Mon Nov 23 1998 Pablo Saratxaga <srtxg@chanae.alphanet.ch>
- improved %files section, and added use of %{prefix} and install-info
  (well,... no. The info file has not dir info inside, commented out)
