Summary: LaTeX support for the jade tex backend 
Summary(pt_BR): Suporte LaTeX para o "backend" tex jade
Summary(es): Soporte LaTeX para el "backend" text jade
Name: jadetex
Version: 2.3
Release: 5cl
Requires: sgml-common, tetex >= 0.9, tetex-latex >= 0.9
Copyright: Copyright (C) 1995,1996,1997,1998 Sebastian Rahtz <s.rahtz@elsevier.co.uk>
Source0: jadetex.tar.bz2
Source1: hyperref.tar.bz2
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
BuildRoot: /tmp/jadetexroot
%define sgmlbase /usr

#%ifos solaris
## these are local hacks for a particular system; you don't want them
#%define TEXHOMEDIR /usr/unsupported/share/texmf/tex/latex
#%define TEXWEB2CDIR /usr/unsupported/share/texmf/web2c
#%define TEXBINDIR /usr/unsupported/bin
#%else
## these are real
#%define TEXHOMEDIR %{sgmlbase}/lib/texmf/texmf/tex/latex/
#%define TEXWEB2CDIR %{sgmlbase}/lib/texmf/texmf/web2c
#%define TEXBINDIR %{sgmlbase}/lib/texmf/bin/i686-linux
#%endif

%description
  jadetex is the addition support needed to crunch jade output 
as LaTeX files.  It includes jadetex 2.3 and hyperref 6.42.

%description -l pt_BR
Suporte LaTeX para o "backend" tex jade

%description -l es
Soporte LaTeX para el "backend" text jade

%prep
%setup -c -b1 -q

%build
cd hyperref
make
cd ..

cd jadetex
TEXINPUTS=.//:../hyperref//:
export TEXINPUTS
TEXMACROS=.//:../hyperref//:
export TEXMACROS
TEXFORMATS=.//:../hyperref//:
export TEXFORMATS
#latex jadetex.ins
#initex \&latex jadetex.ltx '\dump'
make -f Makefile.jadetex

%install
rm -fr $RPM_BUILD_ROOT
# install hyperref
####mkdir -p $RPM_BUILD_ROOT%{HTEX}/hyperref
####mv hyperref/*.sty hyperref/*.cfg $RPM_BUILD_ROOT%{HTEX}/hyperref/
## Let's try to not install hyperref and see if things still work.
# cd hyperref
# make install DESTDIR=$RPM_BUILD_ROOT
# cd ..

# install jadetex
cd jadetex

mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/bin
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/share/texmf/web2c
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/share/tex/jadetex

#mkdir -p $RPM_BUILD_ROOT%{WTEX}
#mv jadetex/jadetex.fmt $RPM_BUILD_ROOT%{WTEX}/jadetex.fmt
#mkdir -p $RPM_BUILD_ROOT%{BTEX}
#ln -s virtex $RPM_BUILD_ROOT%{BTEX}/jadetex
#mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/bin
###ln -s %{BTEX}/jadetex $RPM_BUILD_ROOT%{sgmlbase}/bin/jadetex
#ln -s virtex $RPM_BUILD_ROOT%{sgmlbase}/bin/jadetex
TEXINPUTS=.//:../hyperref//:
export TEXINPUTS
TEXMACROS=.//:../hyperref//:
export TEXMACROS
TEXFORMATS=.//:../hyperref//:
export TEXFORMATS
make -f Makefile.jadetex install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/bin
ln -s %{sgmlbase}/bin/virtex $RPM_BUILD_ROOT%{sgmlbase}/bin/jadetex
ln -s %{sgmlbase}/bin/pdfvirtex $RPM_BUILD_ROOT%{sgmlbase}/bin/pdfjadetex

%define TEXMFMAIN `kpsewhich -expand-var '$TEXMFMAIN'`
echo "dude texmfmain is $TEXMFMAIN"

%clean
rm -fr $RPM_BUILD_ROOT

%post
# let the system know about it!
if [ -x %{sgmlbase}/bin/texhash ]; then
   %{sgmlbase}/bin/texhash | :
fi

%files

# %attr(- root root) %{sgmlbase}/share/texmf/tex/latex/hyperref/*

%attr(- root root) %{sgmlbase}/share/texmf/web2c/jadetex.fmt
%attr(- root root) %{sgmlbase}/share/texmf/web2c/pdfjadetex.fmt
%attr(- root root) %{sgmlbase}/share/texmf/tex/jadetex/*

%attr(- root root) %{sgmlbase}/bin/jadetex
%attr(- root root) %{sgmlbase}/bin/pdfjadetex

%changelog
* Thu Jul  1 1999 Guilherme Manika <gwm@conectiva.com>
- Added %clean
- Meaningless change in %post to avoid unecessary noise

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr  5 1999 Conectiva <dist@conectiva.com>
- fixes %post script

* Mon Mar 22 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- initial packaging
