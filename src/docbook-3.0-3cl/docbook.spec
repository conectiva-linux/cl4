Summary: Davenport Group DocBook DTD for technical documentation
Summary(pt_BR): DTD DocBook Davenport Group para documentação técnica
Summary(es): DTD DocBook del Davenport Group para documentación técnica
Name: docbook
%define version 3.0
%define release 3cl
Version: %{version}
Release: %{release}
Copyright: Copyright 1992, 1993, 1994, 1995, 1996 HaL Computer Systems, Inc., O'Reilly & Associates, Inc., ArborText, Inc., and Fujitsu Software Corporation.
Prereq: sgml-common
Source: docbook.tgz
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
BuildRoot: /tmp/docbookroot
%define sgmlbase /usr

%description
  Davenport Group DocBook DTD for technical documentation.

%description -l pt_BR
DTD DocBook Davenport Group para documentação técnica

%description -l es
DTD DocBook del Davenport Group para documentación técnica

%prep
%setup -c

%install
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml
install docbook/* $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/

%post
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{sgmlbase}/bin/install-catalog --install docbook --version $V > /dev/null 2>&1 | :

%postun
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{sgmlbase}/bin/install-catalog --remove docbook --version $V > /dev/null 2>&1 | :

%files
%doc docbook/announce.txt
%{sgmlbase}/lib/sgml/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr  5 1999 Rodarvus <rodarvus@conectiva.com>
- fixes %post scripts
- final rebuild for 3.0 spanish edition

* Thu Apr 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Redirected output from %post and %postun to /dev/null
