Summary: A development library for text mode user interfaces.
Summary(pt_BR): Not Erik's Windowing Toolkit - janelamento em modo texto com slang
Summary(es): Not Erik's Windowing Toolkit - hechura de ventanas en modo texto con slang
Name: newt
%define version 0.40
Version: %{version}
Release: 11cl
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://ftp.redhat.com/pub/redhat/code/newt/newt-%{version}.tar.bz2
Requires: slang
Provides: snack

%package devel
Summary: Newt windowing toolkit development files.
Summary(pt_BR): Toolkit do desenvolvedor para a biblioteca de janelas newt
Summary(es): Toolkit del desarrollador para la biblioteca de ventanas newt
Requires: slang-devel
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
BuildRoot: /var/tmp/newtroot

%description
Newt is a programming library for color text mode, widget based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
checkboxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces.  This package also contains the
shared library needed by programs built with newt, as well as a
/usr/bin/dialog replacement called whiptail.  Newt is based on the
slang library.

%description -l pt_BR
Estes são os arquivos principais e bibliotecas para aplicações
de desenvolvimento que usem newt. Newt é um kit de ferramentas
de janelas para modo texto, que oferece vários widgets e pilhas
de janelas.

%description -l es
Estos son los archivos principales y bibliotecas para aplicaciones de
desarrollo que usen newt. Newt es un kit de herramientas de ventanas
para modo texto, que nos ofrece varios widgets y montes de ventanas.

%description devel
The newt-devel package contains the header files and libraries
necessary for developing applications which use newt.  Newt is
a development library for text mode user interfaces.  Newt is
based on the slang library.

Install newt-devel if you want to develop applications which will
use newt.

%description -l pt_BR devel
Estes são os arquivos de inclusão e bibliotecas para o
desenvolvimento de aplicações que usam newt. Newt é um toolkit de
janelamento para modo texto, que provê muitos widgets e janelas
sobrepostas.

%description -l es devel
Estos son los archivos de inclusión y bibliotecas para el desarrollo
de aplicaciones que usan newt. Newt es un toolkit de ventanas para
modo texto, que provee muchos widgets y ventanas sobrepuestas.

%prep
%setup

%build
./configure --enable-gpm-support
make
make shared

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make instroot=$RPM_BUILD_ROOT install
make instroot=$RPM_BUILD_ROOT install-sh

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 17 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Fri Apr  9 1999 Matt Wilson <msw@redhat.com>
- fixed a glibc related bug in reflow that was truncating all text to 1000
chars

* Fri Apr 09 1999 Matt Wilson <msw@redhat.com>
- fixed bug that made newt apps crash when you hit <insert> followed by lots
of keys

* Mon Mar 15 1999 Matt Wilson <msw@redhat.com>
- fix from Jakub Jelinek for listbox keypresses

* Fri Feb 27 1999 Matt Wilson <msw@redhat.com>
- fixed support for navigating listboxes with alphabetical keypresses

* Thu Feb 25 1999 Matt Wilson <msw@redhat.com>
- updated descriptions
- added support for navigating listboxes with alphabetical keypresses

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- made grid wrapped windows at least the size of their title bars

* Fri Feb  5 1999 Matt Wilson <msw@redhat.com>
- Function to set checkbox flags.  This will go away later when I have
  a generic flag setting function and signals to comps to go insensitive.

* Tue Jan 19 1999 Matt Wilson <msw@redhat.com>
- Stopped using libgpm, internalized all gpm calls.  Still need some cleanups.

* Thu Jan  7 1999 Matt Wilson <msw@redhat.com>
- Added GPM mouse support
- Moved to autoconf to allow compiling without GPM support
- Changed revision to 0.40

* Wed Oct 21 1998 Bill Nottingham <notting@redhat.com>
- built against slang-1.2.2

* Wed Aug 19 1998 Bill Nottingham <notting@redhat.com>
- bugfixes for text reflow
- added docs

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Thu Apr 30 1998 Erik Troan <ewt@redhat.com>
- removed whiptcl.so -- it should be in a separate package

* Mon Feb 16 1998 Erik Troan <ewt@redhat.com>
- added newtWinMenu()
- many bug fixes in grid code

* Wed Jan 21 1998 Erik Troan <ewt@redhat.com>
- removed newtWinTernary()
- made newtWinChoice() return codes consistent with newtWinTernary()

* Fri Jan 16 1998 Erik Troan <ewt@redhat.com>
- added changes from Bruce Perens
    - small cleanups
    - lets whiptail automatically resize windows
- the order of placing a grid and adding components to a form no longer
  matters
- added newtGridAddComponentsToForm()

* Wed Oct 08 1997 Erik Troan <ewt@redhat.com>
- added newtWinTernary()

* Tue Oct 07 1997 Erik Troan <ewt@redhat.com>
- made Make/spec files use a buildroot
- added grid support (for newt 0.11 actually)

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- Added patched from Clarence Smith for setting the size of a listbox
- Version 0.9

* Tue May 28 1997 Elliot Lee <sopwith@redhat.com> 0.8-2
- Touchups on Makefile
- Cleaned up NEWT_FLAGS_*

* Tue Mar 18 1997 Erik Troan <ewt@redhat.com>
- Cleaned up listbox
- Added whiptail
- Added newtButtonCompact button type and associated colors
- Added newtTextboxGetNumLines() and newtTextboxSetHeight()

* Tue Feb 25 1997 Erik Troan <ewt@redhat.com>
- Added changes from sopwith for C++ cleanliness and some listbox fixes.

%files
%defattr (-,root,root)
%doc CHANGES COPYING
/usr/lib/libnewt.so.*
/usr/bin/whiptail
/usr/lib/python1.5/snack.py
/usr/lib/python1.5/lib-dynload/_snackmodule.so

%files devel
%defattr (-,root,root)
%doc tutorial.sgml
/usr/include/newt.h
/usr/lib/libnewt.a
/usr/lib/libnewt.so
