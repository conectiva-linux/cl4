Summary: Jade and SP -- parser and tools for SGML + DSSSL
Summary(pt_BR): Jade e SP -- "parser" e ferramentas para SGML + DSSSL
Summary(es): Jade y SP -- "parser" y herramientas para SGML + DSSSL
Name: jade
%define vermajor 1
%define verminor 2.1
%define version %{vermajor}.%{verminor}
%define release 4cl
Version: %{version}
Release: %{release}
Requires: sgml-common
Source: jade.tar.bz2
Copyright: Copyright 1997 James Clark
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
BuildRoot: /tmp/jaderoot
%define sgmlbase /usr

%description
  Jade (James' DSSSL Engine) is an implementation of the DSSSL style
language.

%description -l pt_BR
Jade e SP -- "parser" e ferramentas para SGML + DSSSL

%description -l es
Jade y SP -- "parser" y herramientas para SGML + DSSSL

%prep

%setup -c -q
%build
#cd jade; make -f Makefile.jade SGMLPATH=%{sgmlbase}/lib/sgml
#cd jade; make -f Makefile.jade DEFS=-DSGML_CATALOG_FILES_DEFAULT=\\\"%{sgmlbase}/lib/sgml/CATALOG\\\"
cd jade; ./configure --prefix=%{sgmlbase} --enable-static --enable-default-catalog=%{sgmlbase}/lib/sgml/CATALOG; make

%install
# NOTE: in installing I am also copying a bunch of .h files into
# $(prefix)/include/sp/{generic,include,lib}.  This is so that the
# library API can be used.  It's an ugly kludge, and the best way
# would be for James Clark to tell us what the appropriate list of
# files to be included is.
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/doc
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/bin
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/include
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/include/sp
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/include/sp/generic
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/include/sp/include
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/include/sp/lib
cd jade; ./configure --prefix=%{sgmlbase} --enable-static --enable-default-catalog=%{sgmlbase}/lib/sgml/CATALOG; make install prefix=$RPM_BUILD_ROOT%{sgmlbase}
mv $RPM_BUILD_ROOT%{sgmlbase}/bin/sx $RPM_BUILD_ROOT%{sgmlbase}/bin/sgml2xml
install generic/*.h $RPM_BUILD_ROOT%{sgmlbase}/include/sp/generic/
install include/*.h $RPM_BUILD_ROOT%{sgmlbase}/include/sp/include/
install lib/*.h $RPM_BUILD_ROOT%{sgmlbase}/include/sp/lib/
# install jade/jade $RPM_BUILD_ROOT%{sgmlbase}/bin/jade 
strip $RPM_BUILD_ROOT%{sgmlbase}/bin/jade 
strip $RPM_BUILD_ROOT%{sgmlbase}/bin/nsgmls   
strip $RPM_BUILD_ROOT%{sgmlbase}/bin/spam     
strip $RPM_BUILD_ROOT%{sgmlbase}/bin/sgmlnorm 
strip $RPM_BUILD_ROOT%{sgmlbase}/bin/spent    
cp dsssl/catalog $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/dsssl.cat
cp dsssl/dsssl.dtd dsssl/style-sheet.dtd dsssl/fot.dtd $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/

%post
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{sgmlbase}/bin/install-catalog --install dsssl --version $V > /dev/null 2>&1

%postun
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{sgmlbase}/bin/install-catalog --remove dsssl --version $V > /dev/null 2>&1

%files
%attr(- root root) %doc jade/doc/ jade/jadedoc/ jade/dsssl/ jade/pubtext/ jade/unicode/ jade/README jade/COPYING jade/VERSION
%attr(- root root) %{sgmlbase}/bin/*
%attr(- root root) %{sgmlbase}/lib/*
%attr(- root root) %{sgmlbase}/include/*
# %attr(- root root) %{sgmlbase}/include/sp/*
# %attr(- root root) %{sgmlbase}/include/sp/generic/*
# %attr(- root root) %{sgmlbase}/include/sp/include/*
# %attr(- root root) %{sgmlbase}/include/sp/lib/*
# %attr(- root root) %{sgmlbase}/doc/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Redirected output from %post and %postun to /dev/null
