Summary: An X Window System tool for creating morphed images.
Summary(pt_BR): Programa de "morphing" com interface X
Summary(es): Programa de "morphing" con interface X
Name: xmorph
Version: 1996.07.12
Release: 11cl
Copyright: GPL
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Source: ftp://ftp.x.org/contrib/graphics/xmorph-11sep97.tar.bz2
Source800: xmorph-wmconfig.i18n.tgz
Patch: xmorph-11sep97-make.patch
Patch1: xmorph-11sep97-glibc.patch
Prefix: /usr
BuildRoot: /var/tmp/xmorph-root

%description
Xmorph is a digital image warping (aka morphing) program.  Xmorph
provides the tools needed and comprehensible instructions for you to
create morphs:  changing one image into another.  Xmorph runs under the
X Window System.

Install the xmorph package if you need a program that will create morphed
images.

%description -l pt_BR
xmorph permite a você criar "morphs" fascinantes - mudanças animadas
entre duas imagens diferentes - e oferece as ferramentas para você
fazê-lo de uma maneira intuitiva e de fácil compreensão.

%description -l es
xmorph te permite crear "morphs" fascinantes - cambios animados
entre imágenes diferentes - y nos ofrece las herramientas para
hacerlo de una manera intuitiva y de fácil entendimiento.

%prep
%setup -q -n xmorph-11sep97
%patch0 -p0 -b .make
%patch1 -p1 -b .glibc

%build
make depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

install -s xmorph $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 644 xmorph.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/xmorph.1
gzip -9f $RPM_BUILD_ROOT/usr/X11R6/man/man1/xmorph.1

tar xvfpz $RPM_SOURCE_DIR/xmorph-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README HISTORY
/usr/X11R6/bin/xmorph
%attr(644,root,root) /usr/X11R6/man/man1/xmorph.1.gz

%changelog
* Thu Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fixed mode for man page (now compressed)

* Fri Jun 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed specfile

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
