Summary: A fast, compact editor based on the slang screen library.
Summary(pt_BR): Um pequeno e rápido editor
Summary(es): Un pequeño y rápido editor
Name: jed
Version: 0.98.7
Release: 3cl
Copyright: GPL
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Source0: ftp://space.mit.edu/pub/davis/jed/jed0.98-7.tar.gz
Source1: xjed.wmconfig
Source800: jed-wmconfig.i18n.tgz
Patch0: BUGS
Patch1: jed-0.98.6-make.patch
Patch2: jed-0.97.14-XFree86-3.2-keys.patch
Patch3: jed-0.98.6-dfa.patch
Requires: jed-common = %{version}
BuildRoot: /var/tmp/jed-root

%description
Jed is a fast, compact editor based on the slang screen library.  Jed
features include emulation of the Emacs, EDT, WordStar and Brief editors;
support for extensive customization with slang macros, colors,
keybindings, etc.; and a variety of programming modes with syntax
highlighting.

You should install jed if you've used it before and you like it, or if you
haven't used any text editors before and you're still deciding what you'd
like to use.  You'll also need to have slang installed.

%description -l pt_BR
Jed é um editor compacto e rápido baseado na biblioteca slang. Ele
tem modos de edição especiais para C, C++ e outras linguagens. Pode
emular Emacs, Wordstar e outros editores, podendo ser configurado
com macros slang, cores, mapeamento de teclas, etc.

%description -l es
Jed es un editor compacto y rápido basado en la biblioteca
slang. Tiene modos de edición especiales para C, C++ y otros
lenguajes. Puede emular Emacs, Wordstar y otros editores, y se lo
puede configurar con macros slang, color, mapas de teclas, etc.

%package common
Summary: Files needed by any Jed editor.
Summary(pt_BR): Arquivos necessários pelo editor jed
Summary(es): Files needed by any Jed editor.
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
%description common
The jed-common package contains files (such as .sl files) that are
needed by any jed binary in order to run.

%description -l pt_BR common
O pacote jed-common contém arquivos (como arquivos .sl) que são
necessários por qualquer binário do jed para rodar.

%description -l es common
The jed-common package contains files (such as .sl files) that are
needed by any jed binary in order to run.

%package xjed
Requires: jed-common = %{version}
Summary: The X Window System version of the Jed text editor.
Summary(pt_BR): Editor Jed - versão X
Summary(es): Editor Jed - versión X
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores

%description xjed
Xjed is a version of the Jed text editor that will work with the X Window
System.
  
You should install xjed if you like Jed and you'd like to use it with X.
You'll also need to have the X Window System installed.

%description -l pt_BR xjed
Xjed é o editor jed para X Window.

%description -l es xjed
Xjed es el editor jed para X Window.

%package -n rgrep
Summary: A grep utility which can recursively descend through directories.
Summary(pt_BR): Utilitário grep recursivo
Summary(es): Utilitario grep recursivo
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto

%description -n rgrep
The rgrep utility can recursively descend through directories as
it greps for the specified pattern.  Note that this ability does
take a toll on rgrep's performance, which is somewhat slow.  Rgrep
will also highlight the matching expression.

Install the rgrep package if you need a recursive grep which can
highlight the matching expression.

%description -l pt_BR -n rgrep
Utilitário grep recursivo que pode destacar a expressão encontrada,
escrito pelo autor do editor Jed.

%description -l es -n rgrep
Utilitario grep recursivo que puede destacar la expresión encontrada,
escrito por el autor del editor Jed.

%prep
%setup -q -n jed
cd src
%patch0 -p0
cd ..
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
CFLAGS="-DMEMCPY=SLmemcpy -DMEMSET=SLmemset -DMEMCHR=SLmemchr $RPM_OPT_FLAGS" ./configure --prefix=/usr
make all
make xjed

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib/jed
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin

cp -r lib $RPM_BUILD_ROOT/usr/lib/jed
cp -r info $RPM_BUILD_ROOT/usr/lib/jed

cd src/objs
install -m 0755 -s jed $RPM_BUILD_ROOT/usr/bin
install -m 0755 -s xjed $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 0755 -s rgrep $RPM_BUILD_ROOT/usr/bin
JED_ROOT=$RPM_BUILD_ROOT/usr/lib/jed $RPM_BUILD_ROOT/usr/bin/jed -batch -n -l preparse.sl

cd ../../doc
install -m 644 jed.1 $RPM_BUILD_ROOT/usr/man/man1
install -m 644 rgrep.1 $RPM_BUILD_ROOT/usr/man/man1

install -m 0644 $RPM_SOURCE_DIR/xjed.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/xjed





tar xvfpz $RPM_SOURCE_DIR/jed-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/jed

%files common
%defattr(-,root,root)
%doc COPYING COPYRIGHT doc INSTALL INSTALL.unx README changes.txt
%docdir /usr/lib/jed/info
/usr/man/man1/jed.1
/usr/lib/jed

%files xjed
%defattr(-,root,root)
/usr/X11R6/bin/xjed
%config(missingok) /etc/X11/wmconfig/xjed

%files -n rgrep
%defattr(-,root,root)
/usr/bin/rgrep
/usr/man/man1/rgrep.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- i18n wmconfig

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- update to 0.98.7 for Raw Hide
- split off lib stuff into jed-common

* Mon Oct  5 1998 Jeff Johnson <jbj@redhat.com>
- change rgep group tag, same as grep.

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- added wmconfig entry for xjed

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated to 0.98.4
- included man pages in file lists

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
