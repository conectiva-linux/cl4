Summary: stylesheets for use at Cygnus, in particular with docbook.
Summary(pt_BR): "stylesheets" usados na Cygnus, em particular com o docbook.
Summary(es): "stylesheets" usados en Cygnus, en particular con docbook.
Name: stylesheets
%define version 0.8
%define release 3cl
Version: %{version}
Release: %{release}
Requires: sgml-common docbook
Source: stylesheets.tar.bz2
Copyright: Mark Eichin, Cygnus Solutions; Mark Burton (markb@ordern.com); Mark Galassi (Cygnus Solutions) for dbtohtml.dsl; Jon Bosak, Sun Microsystems for bosak-db3 and docbook.dsl, norm@berkshire.net for the nwalsh-modular/ hierarchy; Mark Galassi (Cygnus Solutions) for cygnus-both.dsl: contains Cygnus customizations for the DocBook modular stylesheets.
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
BuildRoot: /tmp/stylesheetsroot
%define sgmlbase /usr

%description
  stylesheets is a collection of stylesheets used at Cygnus for SGML 
  conversion.  The stylesheets themselves are in /usr/lib/sgml/stylesheets.
  experimental entries are added to the catalog.  Some simple scripts are
  included to facilitate using the stylesheets.  These stylesheets are
  almost entirely the work of Norm Walsh (norm@nwalsh.com).  Version
  0.8 tracks Norm's 1.33 stylesheets.

%description -l pt_BR
"stylesheets" usados na Cygnus, em particular com o docbook.

%description -l es
"stylesheets" usados en Cygnus, en particular con docbook.

%prep
%setup -c

%install
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/dtds
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/dtds/decls
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/common
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/html
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/lib
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/print
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/test
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/images
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/bin
install stylesheets/*.cat $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/
install stylesheets/nwalsh-modular/VERSION $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/VERSION
install stylesheets/nwalsh-modular/catalog $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/nwalsh-modular.cat
install stylesheets/nwalsh-modular/dtds/decls/docbook.dcl $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/dtds/decls/
install stylesheets/*.dsl $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/
install stylesheets/nwalsh-modular/catalog $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/
install stylesheets/nwalsh-modular/common/*.dsl $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/common/
install stylesheets/nwalsh-modular/common/*.ent $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/common/
install stylesheets/nwalsh-modular/html/*.dsl $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/html/
install stylesheets/nwalsh-modular/lib/*.dsl $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/lib/
install stylesheets/nwalsh-modular/print/*.dsl $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/print/
install stylesheets/nwalsh-modular/test/*.sgm $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/test/
install stylesheets/nwalsh-modular/test/*.dsl $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/test/
install stylesheets/nwalsh-modular/test/*.css $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/test/
install stylesheets/nwalsh-modular/images/*.gif $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/stylesheets/nwalsh-modular/images/
for i in stylesheets/*.sh; do
  j=`basename $i .sh`
  install $i $RPM_BUILD_ROOT%{sgmlbase}/bin/$j
done

%post
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{sgmlbase}/bin/install-catalog --install stylesheets --version $V > /dev/null 2>&1
%{sgmlbase}/bin/install-catalog --install nwalsh-modular --version $V > /dev/null 2>&1

%postun
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{sgmlbase}/bin/install-catalog --remove stylesheets --version $V > /dev/null 2>&1
%{sgmlbase}/bin/install-catalog --remove nwalsh-modular --version $V > /dev/null 2>&1

%files
%attr(- root root) %{sgmlbase}/lib/sgml/dtds/*
%attr(- root root) %{sgmlbase}/lib/sgml/stylesheets/*
%attr(- root root) %{sgmlbase}/lib/sgml/stylesheets.cat
%attr(- root root) %{sgmlbase}/lib/sgml/nwalsh-modular.cat
%attr(- root root) %{sgmlbase}/bin/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Redirected output from %post and %postun to /dev/null

* Mon Mar 22 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- First version of package
