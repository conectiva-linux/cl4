# Note that this is NOT a relocatable package
%define ver      0.4
%define rel      9cl
%define prefix   /usr

Summary: Color font rendering library for X11R6.
Summary(pt_BR): Biblioteca para renderização colorida de fontes para o X11R6.
Summary(es): Biblioteca de render de fuentes coloridas para el X11R6.
Name: fnlib
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
# was .gz
Source: ftp://www.rasterman.com/pub/enlightenment/libs/fnlib/fnlib-%{ver}.tar.bz2
Obsoletes: Fnlib
BuildRoot: /var/tmp/fnlib-%{ver}-root
URL: http://www.rasterman.com/
Requires: imlib

%description
Fnlib is a library that provides full, scalable 24-bit color font 
rendering abilities for X.

%description -l pt_BR
A fnlib é uma biblioteca que fornece renderização completa e escalável
de 24 bits de cores para fontes no X.

%description -l es
Biblioteca de render de fuentes coloridas para el X11R6.

%package devel
Summary: Headers, static libraries and documentation for Fnlib.
Summary(pt_BR): Arquivos de inclusão, bibliotecas estáticas e documentação para a fnlib.
Summary(es): Archivos de inclusión, bibliotecas estáticas y documentación para fnlib.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: fnlib
Obsoletes: Fnlib

%description devel
Headers, static libraries and documentation for Fnlib.

%description -l pt_BR devel
Arquivos de inclusão, bibliotecas estáticas e documentação para a fnlib.

%description -l es devel
Archivos de inclusión, bibliotecas estáticas y documentación para fnlib.

%prep
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
./configure --prefix=%prefix --sysconfdir=/etc
make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc README

%config /etc/fnrc
%{prefix}/lib/lib*.so.*
%{prefix}/share/fnlib_fonts/*

%files devel
%defattr(-, root, root)

%doc doc/index.html
%doc doc/fontinfo.README

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/include/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Uses optimization flags now

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- built against imlib 1.9.3
