%define name fte
%define version 0.49.13
%define release 1cl

Summary: Text editor for console and X Window System.
Summary(pt_BR): Editor de textos para o X e console
Summary(es): Text editor for console and X Window System.
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: Artistic
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
URL: http://kiss.uni-lj.si/~k4fr0235/fte/
# Repacked source with bzip2
Source: %{name}-%{version}.src.tar.bz2
Patch0: %{name}-%{version}-conectiva.patch
Patch1: %{name}-%{version}-erwin.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-install-root

%description
Multiple file/window editing, Column blocks,  configurable
menus and  keyboard  bindings,  mouse support,  undo/redo,
regular expression search and replace, folding, background
compiler execution, Color syntax highlighting  for  C/C++,
HTML, PERL, TEX, and many more.

%description -l pt_BR
Edição de múltiplos arquivos,  janelas,  configurações  de
menu e janela modificáveis, undo/redo, procura e substituição
de expressões regulares, execução do compilador em background,
reconhecimento de sintaxe para C/C++, HTML, PERL, TEX, e varias
outras.

%description -l es
Multiple file/window editing, Column blocks,  configurable
menus and  keyboard  bindings,  mouse support,  undo/redo,
regular expression search and replace, folding, background
compiler execution, Color syntax highlighting  for  C/C++,
HTML, PERL, TEX, and many more.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated fte to 0.49.13
- Updated the two patches to work with the new version

* Tue Jun  8 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat May 15 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added to Conectiva Linux

* Wed Dec 30 1998 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated to version 0.49.7

* Mon Dec 28 1998 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated to version 0.49.4
- Added pt_BR translations
- Added Erwin Andreasen's patch for vfte
- Added BuildRoot
- Changed URL to reflect Marko's new homepage
- Updated fte script to load sfte, instead of vfte
  (Which works better at non-english speaking countries)

* Wed Aug 19 1998 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated to version 0.46.4

* Wed Aug 05 1998 Rodrigo Parra Novo <rodarvus@conectiva.com>
- First build with rpm (version 0.45)

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make -C src unix OPTIMIZE="$RPM_OPT_FLAGS"
src/cfte config/main.fte system.fterc

%install
mkdir -p $RPM_BUILD_ROOT/etc/fte $RPM_BUILD_ROOT/usr/man/man1 \
	$RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 644 -o 0 -g 0 system.fterc $RPM_BUILD_ROOT/etc/fte
cp -a config $RPM_BUILD_ROOT/etc/fte
install -m 644 -o 0 -g 0 man/cfte.1 $RPM_BUILD_ROOT/usr/man/man1
install -m 644 -o 0 -g 0 man/fte.1 $RPM_BUILD_ROOT/usr/man/man1
install -m 755 -o 0 -g 0 scripts/fte $RPM_BUILD_ROOT/usr/bin
install -m 755 -o 0 -g 0 src/vfte $RPM_BUILD_ROOT/usr/bin
install -m 755 -o 0 -g 0 src/cfte $RPM_BUILD_ROOT/usr/bin
install -m 755 -o 0 -g 0 src/sfte $RPM_BUILD_ROOT/usr/bin
install -m 755 -o 0 -g 0 src/xfte $RPM_BUILD_ROOT/usr/X11R6/bin

%files
%doc Artistic BUGS COPYING doc/ HISTORY README TODO
%config /etc/fte
/usr/man/man1/cfte.1
/usr/man/man1/fte.1
/usr/bin/fte
/usr/bin/vfte
/usr/bin/cfte
/usr/bin/sfte
/usr/X11R6/bin/xfte
