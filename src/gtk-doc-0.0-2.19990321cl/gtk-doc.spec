# Note that this is NOT a relocatable package
%define build_date 19990321
%define ver        0.0
%define rel        2.%{build_date}cl
%define prefix     /usr

Summary: The GTK doc generator
Summary(pt_BR): O gerador de documentação do GTK
Summary(es): El generador de documentación del GTK
Name: gtk-doc
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Source: %{name}-%{build_date}.tar.bz2
BuildRoot: /var/tmp/gtk-doc-%{PACKAGE_VERSION}-root

%description
This package generates HTML documentation for GTK+ programs

%description -l pt_BR
O gerador de documentação do GTK

%description -l es
El generador de documentación del GTK

%prep
%setup -q -n %{name}-%{build_date}

%build
./configure --prefix=%prefix

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%{prefix}/bin/*
%{prefix}/share/gtk-doc

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Injected new group into package

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 22 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Created package from 19990312 snapshot
