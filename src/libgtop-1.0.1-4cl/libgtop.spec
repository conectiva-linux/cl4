# Note that this is NOT a relocatable package
%define ver      1.0.1
%define rel      4cl
%define prefix   /usr

Summary: LibGTop library
Summary(pt_BR): Biblioteca libgtop
Summary(es): Biblioteca libgtop
Name: libgtop
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
# was .gz
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/libgtop/libgtop-%{ver}.tar.bz2
Source1: libgtop-pt_BR.po
Patch0: libgtop-1.0.1-pt_BR.patch
BuildRoot: /tmp/libgtop-root
URL: http://www.home-of-linux.org/gnome/libgtop/
Prereq: info

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc.

On Linux systems, these information are taken directly from the /proc
filesystem while on other systems a server is used to read those
information from /dev/kmem or whatever. 

%description -l pt_BR
Uma biblioteca que obtém informações sobre o sistema como cpu e
uso da memória, processos ativos, etc. Em sistemas Linux estas
informações são obtidas diretamente do sistema de arquivos /proc.

%description -l es
Una biblioteca que obtiene información sobre el sistema como cpu
y uso de la memoria, procesos activos, etc. En sistemas Linux esta
información se obtiene directamente del sistema de archivos /proc.

%package devel
Summary: Libraries, includes, etc to develop LibGTop applications
Summary(pt_BR): Bibliotecas e arquivos de inclusão para desenvolver aplicações com a libgtop
Summary(es): Bibliotecas e archivos de inclusión para desarrollar aplicaciones libgtop.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: libgtop

%description devel
Libraries, include files, etc you can use to develop GNOME applications.

%description -l pt_BR devel
Bibliotecas e arquivos de inclusão para desenvolver aplicações com a libgtop

%description -l es devel
Bibliotecas e archivos de inclusión para desarrollar aplicaciones libgtop.

%package examples
Summary: Examples for LibGTop
Summary(pt_BR): Exemplos para a libgtop
Summary(es): Ejemplos para libgtop
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Requires: libgtop

%description examples
Examples for LibGTop.

%description -l pt_BR examples
Exemplos para a libgtop.

%description -l es examples
Ejemplos para libgtop

%changelog
* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package
- unset LINGUAS

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file.

* Tue Aug 19 1998 Martin Baulig <martin@home-of-linux.org>
- released LibGTop 0.25.0

* Sun Aug 16 1998 Martin Baulig <martin@home-of-linux.org>
- first version of the RPM

%prep
%setup -q
%patch0 -p1 -b .pt_BR

%build

cp $RPM_SOURCE_DIR/libgtop-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
unset LINGUAS
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
if [ ! -f configure ]; then
./autogen.sh --prefix=%prefix --without-linux-table --with-libgtop-inodedb --with-libgtop-examples --with-libgtop-guile --with-libgtop-smp
else
%ifarch alpha
autoconf
./configure --host=alpha-conectiva-linux --prefix=%prefix --without-linux-table --with-libgtop-inodedb --with-libgtop-examples --with-libgtop-guile --with-libgtop-smp
%else
autoconf
./configure --prefix=%prefix --without-linux-table --with-libgtop-inodedb --with-libgtop-examples --with-libgtop-guile --with-libgtop-smp
%endif
fi

make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} install

rm -fr $RPM_BUILD_ROOT/%{prefix}/include/libgtop

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc RELNOTES-0.25 RELNOTES-1.0 AUTHORS ChangeLog NEWS README
%doc TODO NEWS.old copyright.txt
%doc src/inodedb/README.inodedb

%{prefix}/lib/lib*.so.*
%{prefix}/share/*
%{prefix}/bin/*

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/lib/*.sh
%{prefix}/lib/*.def
%{prefix}/include/*

%files examples
%defattr(-,root,root)

%{prefix}/libexec/libgtop/*
