# Note that this is NOT a relocatable package
%define ver      1.0.1
%define rel      4cl
%define prefix   /usr

Summary: GNOME Objective C libraries
Summary(pt_BR): Bibliotecas Objective C do GNOME
Summary(es): Bibliotecas Objective C del GNOME
Name: gnome-objc
Version: %ver
Release: %rel
Copyright: LGPL
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
# was .gz
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-objc/gnome-objc-%{ver}.tar.bz2
Source1: gnome-objc-pt_BR.po
Patch0: gnome-objc-1.0.1-pt_BR.patch
BuildRoot: /var/tmp/gnome-objc-%{PACKGE_VERSION}-root
Requires: gnome-libs
URL: http://www.gnome.org/

%description
Basic libraries you must have installed to use GNOME programs
that are built with Objective C.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pt_BR
Bibliotecas básicas que você deve ter instaladas para que possa
usar programas GNOME que tenham sido construídas com Objective C.

GNOME é o Ambiente de Rede Modelado por Objetos da GNU. É um nome
fantasioso, mas o GNOME é realmente um bom ambiente gráfico. Ele
torna seu computador fácil, poderoso e fácil de configurar.

%description -l es
Bibliotecas básicas que debes tener instaladas para que puedas
usar programas GNOME que hayan sido construidos con Objective C.
GNOME es el Ambiente de Red Modelado por Objetos de la GNU. Es
un nombre fantasioso, pero GNOME es realmente un buen ambiente
gráfico. Hace tu ordenador sencillo, potente y fácil de configurar.

%package devel
Summary: Libraries, includes, etc to develop Objective C GNOME applications
Summary(pt_BR): Bibliotecas, arquivos de inclusão, etc, para que você possa desenvolver aplicações GNOME em Objective C
Summary(es): Bibliotecas, archivos de inclusión, etc., para que puedas desarrollar aplicaciones GNOME en Objective C
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: gnome-objc

%description devel
Libraries, include files, etc you can use to develop Objective C
GNOME applications.

%description -l pt_BR devel
Bibliotecas, arquivos de inclusão, etc, para que você possa
desenvolver aplicações GNOME em Objective C.

%description -l es devel
Bibliotecas, archivos de inclusión, etc, para que puedas desarrollar
aplicaciones GNOME en Objective C.

%changelog
* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- LINGUAS=

* Sat Mar 06 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-objc source tree

%prep
%setup -q
%patch0 -p1 -b .pt_BR

%build

cp $RPM_SOURCE_DIR/gnome-objc-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS

if [ ! -f configure ]; then
%ifarch alpha
  ./autogen.sh --host=alpha-conectiva-linux --prefix=%prefix --sysconfdir="/etc"
%else
  ./autogen.sh --prefix=%prefix --sysconfdir="/etc"
%endif
else
%ifarch alpha
autoconf
./configure --host=alpha-conectiva-linux --prefix=%prefix --sysconfdir="/etc"
%else
autoconf
./configure --prefix=%prefix --sysconfdir="/etc"
%endif
fi

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

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/lib/lib*.so.*
%{prefix}/share/locale/*/*/*

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*.a
%{prefix}/lib/*.la
%{prefix}/lib/*.sh
%{prefix}/include/*
