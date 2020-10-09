%define version 1.2
%define release 5cl

Summary:	GIF manipulating library
Summary(pt_BR): Biblioteca para manipula��o de GIFs
Summary(es): Biblioteca para manipulaci�n de GIFs
Name:		libgd
Version:	%{version}
Release:	%{release}
Source:		http://www.boutell.com/gd/gd%{version}.tar.Z
Patch:		gd-shared.patch
URL:		http://www.boutell.com/gd/
Copyright:	BSD-style
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
BuildRoot:	/tmp/gd-%{version}-root

%description
This is the gd gif-manipulating library. It was created to allow graphs,
charts and the like to be generated on the fly for use on the World wide Web,
but is useful for any application in which custom .GIFs are useful. It is not
a paint program; it is a library.

%description -l pt_BR
Esta � a biblioteca gd para manipula��o de GIFs. Ela foi criada
para uso na Web, gerando gr�ficos automaticamente. Mas � �til para
qualquer programa que precise de GIFs personalizados.  N�o � um
programa de desenho; � uma biblioteca.

%description -l es
Esta es la biblioteca gd para el manejo de GIFs. Fue creada para
uso en la Web, creando gr�ficos autom�ticamente. Pero es �til para
cualquier programa que necesite de GIFs personalizados.  No es un
programa de dibujo; es una biblioteca.

%package devel
Summary:	header files and libraries needed for gd development
Summary(pt_BR): Arquivos de inclus�o e bilbiotecas para desenvolver programas usando gd.
Summary(es): Archivos de inclusi�n y bibliotecas para desarrollar programas usando gd.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires:	libgd

%description devel
This package includes the header files and libraries needed for
developing programs using gd.

%description -l pt_BR devel
Este pacote cont�m os arquivos de inclus�o e as bilbiotecas
necess�rias para desenvolver programas usando gd.

%description -l es devel
Este paquete contiene los archivos de inclusi�n y las bilbiotecas
necesarias para desarrollar programas usando gd.

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Injected new group into package

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Oct 21 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Mon Apr 20 1998 Arne Coucheron <arneco@online.no>
- released libgd-1.2-1
- cleanups to spec file
- added webgif and giftogd binaries
- added a patch to make shared libraries
- splitted the package into a main and devel package
- changed package name to libgd to avoid name collision with another package

%prep
%setup -n gd%{version}

%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" all libgd.a

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,include}
install -m 755 webgif giftogd $RPM_BUILD_ROOT/usr/bin
install -m 644 *.h $RPM_BUILD_ROOT/usr/include
install -m 644 libgd.a $RPM_BUILD_ROOT/usr/lib
install -m 644 libgd.so.%{version} $RPM_BUILD_ROOT/usr/lib
cd $RPM_BUILD_ROOT/usr/lib
ln -sf libgd.so.%{version} libgd.so

strip $RPM_BUILD_ROOT/usr/bin/* ||

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) %doc README index.html
%attr(-,root,root) /usr/bin/*
%attr(-,root,root) /usr/lib/libgd.so.%{version}

%files devel
%attr(-,root,root) /usr/lib/libgd.a
%attr(-,root,root) /usr/lib/libgd.so
%attr(-,root,root) /usr/include/*
