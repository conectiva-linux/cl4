%define prefix /usr
%define ver 1.0.2
%define rel 3cl

Summary: GNOME http client library.
Summary(pt_BR): Biblioteca cliente para http do GNOME.
Summary(es): Biblioteca cliente http del GNOME.
Name: libghttp
Version: %{ver}
Release: %{rel}
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://ftp.gnome.org/pub/GNOME/sources/libghttp/libghttp-%{PACKAGE_VERSION}.tar.gz
BuildRoot: /var/tmp/ghttp-%{PACKAGE-VERSION}-root
URL: http://www.gnome.org/

%description
Library for making HTTP 1.1 requests.

%description -l pt_BR
Biblioteca cliente para http 1.1 do GNOME.

%description -l es
Biblioteca cliente http 1.1 del GNOME.

%package devel
Summary: GNOME http client development
Summary(pt_BR): Componentes para desenvolvimento com o cliente http do GNOME.
Summary(es): Biblioteca cliente http 1.1 del GNOME - desarrollo
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: libghttp

%description devel
Libraries and includes files you can use for libghttp development

%description -l pt_BR devel
Componentes para desenvolvimento com o cliente http do GNOME.

%description -l es devel
Biblioteca cliente http 1.1 del GNOME - desarrollo

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 22 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated package to version 1.0.0

* Sat Mar 06 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.2

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- built with gnome-libs 0.99.2 

%prep
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
./configure --prefix=%{prefix}
make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post 
if ! grep %{prefix}/lib /etc/ld.so.conf > /dev/null ; then
  echo "%{prefix}/lib" >> /etc/ld.so.conf
fi

/sbin/ldconfig

%postun -p /sbin/ldconfig
%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README doc/ghttp.html
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/include/*
