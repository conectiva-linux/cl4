# Note that this is NOT a relocatable package
%define ver      1.0.7
%define rel      4cl
%define prefix   /usr

Summary: The GNOME Personal Information Manager.
Summary(pt_BR): O gerenciador de informações pessoais do GNOME
Summary(es): El administrador de informaciones personales del GNOME.
Name: gnome-pim
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/Productivity
Group(pt_BR): Aplicações/Produtividade
Group(es): Aplicaciones/Productividad
# was .gz
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-pim/gnome-pim-%{ver}.tar.bz2
Source1: gnome-pim-pt_BR.po
Patch0: gnome-pim-1.0.7-pt_BR.patch
Patch1: gnome-pim-gnome-menu.patch
BuildRoot: /var/tmp/gnome-pim-%{PACKAGE_VERSION}-root
Obsoletes: gnome
URL: http://www.gnome.org

%description
The GNOME Personal Information Manager consists of applications to make
keeping up with your busy life easier.

Currently these apps are present:

 - gnomecal :  personal calendar and todo list
 - gnomecard:  contact list of friends and business associates

%description -l pt_BR
O gerente de informações pessoais do GNOME consiste de aplicações para
manter sua vida mais fácil.

Atualmente estes são os aplicativos disponíveis:

- gnomecal : calendário pessoal e lista de coisas a fazer
- gnomecard: lista de contatos: amigos e parceiros comerciais

%description -l es
El administrador de informaciones personales del GNOME consiste de
aplicaciones para hacer su vida muy mas fácil.

Actualmente estas aplicaciones están presentes:

- gnomecal:  calendario personal
- gnomecard: lista de contactos

%package devel
Summary: GNOME PIM development files
Summary(pt_BR): Arquivos para desenvolvimento do GNOME PIM
Summary(es): Archivos para desarrollo con GNOME PIM
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: gnome-pim

%description devel
Files needed to develop apps which interact with gnome-pim applications
via CORBA.

%description -l pt_BR devel
Arquivos necessários ao desenvolvimento de aplicativos que interajam com
o gnome-pim através de CORBA.

%description -l es devel
Archivos para desarrollo con GNOME PIM y CORBA

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome-menu entries for gnome-pim

* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 29 1999 Guilherme Manika <gwm@conectiva.com>
- Versão 1.0.7

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- some fixes (LINGUAS, etc)

* Mon Mar 22 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translattions
- Added optimization flags to spec file

* Sun Mar 14 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.3

* Sun Feb 21 1999 Michael Fulbright <drmike@redhat.com>
- removed libtoolize from %build and fixed source line

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.8

* Thu Feb 11 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.7

* Sat Feb 06 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.6

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.3

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- rebuild against gtk+ 1.1.12

* Mon Dec 14 1998 Michael Fulbright <drmike@redhat.com>
- first try at an RPM for the 0.99.0 release

%prep
%setup -q
%patch0 -p1 -b .pt_BR
%patch1 -p1 -b .gnome-menu

%build

cp $RPM_SOURCE_DIR/gnome-pim-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS
autoconf
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

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%config /etc/CORBA/*
%{prefix}/share/gnome/*
%{prefix}/share/locale/*
%{prefix}/share/mime-info/*

%files devel
%defattr(-, root, root)

%{prefix}/lib/*a
%{prefix}/share/idl
