%define  ver     1.0.5
%define  rel     3cl
%define  prefix  /usr

Summary: The GNOME Users' Guide.
Summary(pt_BR): O Guia do Usuário do GNOME
Summary(es): El Guia del Usuario del GNOME
Name: gnome-users-guide
Version: %ver
Release: %rel
Copyright: GPL
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
# was .gz
Source0: users-guide-%{PACKAGE_VERSION}.tar.bz2
Source1: users-guide-pt_BR.sgml
BuildRoot:/var/tmp/gnome-users-guide-%{PACKAGE_VERSION}-root
BuildArchitectures: noarch

%description
This package will install the users' guide for the
GNOME Desktop Environment on your computer.

You should install this package if you are going to
use GNOME and you want a quick, handy reference.

%description -l pt_BR
Este pacote instalará o guia do usuário para o ambiente
GNOME em seu computador.

Você deve instalar este pacote se for usar o GNOME e
quiser uma referência conveniente e rápida.

%description -l es
El Guia del Usuario del GNOME

%prep
%setup -q -n users-guide-%{PACKAGE_VERSION}

%build
cp $RPM_SOURCE_DIR/users-guide-pt_BR.sgml $RPM_BUILD_DIR/users-guide-%{version}/users-guide.sgml
./configure --prefix=%{prefix}
make
cd $RPM_BUILD_DIR/users-guide-%{version}/
cp -av ./users-guide.junk/figs/* ./users-guide/figs/

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/%{prefix} install 

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jul 01 1999 Rodrigo Stulzer Lopes <rodrigo@conectiva.com>
- We are now going to use the pt_BR version of the gnome users guide

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 29 1999 Guilherme Manika
- Atualizado para a versão 1.0.5 do manual

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 22 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations

* Mon Mar 15 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.3

* Fri Mar 12 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.2

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.5rh - special version for 5.2/GNOME beta CD

* Mon Feb 08 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.5

* Thu Feb 04 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.3

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.2

* Thu Dec 17 1998 Michael Fulbright <drmike@redhat.com>
- first pass at a spec file

%files
%defattr(-, root, root)
%doc README ChangeLog 
%{prefix}/share/gnome/help/users-guide
