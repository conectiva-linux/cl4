%define name libPropList
%define version 0.8.3
%define release 3cl
%define prefix /usr
BuildRoot: /var/tmp/%{name}-%{version}_root

Summary: libPropList, a required library for WindowMaker
Summary(pt_BR): Biblioteca necessária para o WindowMaker
Summary(es): Biblioteca necesaria para el WindowMaker.
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp.windowmaker.org:/pub/libs/%{name}-%{version}.tar.gz
Provides: libPropList
Requires: /bin/sh

%description
Library for reading/writing GNUstep-style defaults databases.
WindowMaker requires libPropList to function.

%description -l pt_BR
Biblioteca para acessar base de dados GNUstep-style.
Necessária para o WindowMaker

%description -l es
Biblioteca para acceder a base de datos GNUstep-style.
Necesaria para el WindowMaker.

%prep
%setup
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=$RPM_BUILD_ROOT%{prefix}

%build
make

%install
make install

# files section
cd $RPM_BUILD_ROOT
rm -f $RPM_BUILD_DIR/file.list.%{name}
echo "%defattr(-,root,root)" >> $RPM_BUILD_DIR/file.list.%{name}

echo "%doc \
      AUTHORS COPYING COPYING.LIB ChangeLog INSTALL NEWS README TODO" \
      >> $RPM_BUILD_DIR/file.list.%{name}

echo "%attr(-,root,root) %{prefix}/include/proplist.h" >> $RPM_BUILD_DIR/file.list.%{name}
echo "%attr(-,root,root) %{prefix}/lib/libPropList.a" >> $RPM_BUILD_DIR/file.list.%{name}
echo "%attr(-,root,root) %{prefix}/lib/libPropList.la" >> $RPM_BUILD_DIR/file.list.%{name}
echo "%attr(-,root,root) %{prefix}/lib/libPropList.so" >> $RPM_BUILD_DIR/file.list.%{name}
echo "%attr(-,root,root) %{prefix}/lib/libPropList.so.0" >> $RPM_BUILD_DIR/file.list.%{name}
echo "%attr(-,root,root) %{prefix}/lib/libPropList.so.0.1.1" >> $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name} $RPM_BUILD_DIR/%{name}-%{version}_root

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 30 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Changed prefix from /usr/X11R6 to /usr

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Mar 18 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- First build under Conectiva Linux
