# Note that this is NOT a relocatable package
%define ver      1.0.0
%define rel      3cl
%define prefix   /usr

Summary: libXML library
Summary(pt_BR): Biblioteca libXML
Summary(es): Biblioteca libXML
Name: libxml
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://ftp.gnome.org/pub/GNOME/sources/libxml/libxml-%{ver}.tar.gz
BuildRoot: /var/tmp/libxml-%{PACKAGE_VERSION}-root

URL: http://www.gnome.org/
Prereq: info

%description
This library allows you to manipulate XML files.

%description -l pt_BR
Esta biblioteca permite a manipulação de arquivos XML.

%description -l es
Esta biblioteca permite manipulación de archivos XML.

%package devel
Summary: Libraries, includes, etc to develop libxml applications
Summary(pt_BR): Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações que usem a biblioteca libxml
Summary(es): Biblioteca y archivos de inclusión para desarrollo de aplicaciones libXML.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: libxml

%description devel
Libraries, include files, etc you can use to develop libxml applications.

%description -l pt_BR devel
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
que usem a biblioteca libxml.

%description -l es devel
Biblioteca y archivos de inclusión para desarrollo de aplicaciones libXML.

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Sun Oct  4 1998 Daniel Veillard <Daniel.Veillard@w3.org>
- Added xml-config to the package

* Thu Sep 24 1998 Michael Fulbright <msf@redhat.com>
- Built release 0.30

%prep
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
%ifarch alpha
./configure --host=alpha-conectiva-linux --prefix=%prefix 
%else
./configure --prefix=%prefix 
%endif

make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} install


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING COPYING.LIB TODO
%{prefix}/lib/lib*.so.*
%{prefix}/bin/xml-config

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/lib/*.sh
%{prefix}/include/*
