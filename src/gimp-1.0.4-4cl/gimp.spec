%define name gimp
%define version 1.0.4
%define release 4cl

Summary: The GNU Image Manipulation Program
Summary(pt_BR): Programa de manipulação de imagem GNU
Summary(es): Programa de manipulación de imagen GNU
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL, LGPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Url: http://www.gimp.org/
Source0: ftp://ftp.gimp.org/pub/gimp/v1.0/v%{PACKAGE_VERSION}/gimp-%{PACKAGE_VERSION}.tar.bz2
Source1: gimp.wmconfig
Source2: wilbur.xpm
Source3: mini-wilbur.xpm
Source4: Gimp.kdelnk
Source800: gimp-wmconfig.i18n.tgz
Buildroot: /var/tmp/gimp-root
Obsoletes: gimp-data-min
Requires: gtk+ >= 1.2.0
Requires: gimp-libgimp = %{PACKAGE_VERSION}
PreReq: ldconfig
BuildPreReq: aalib-devel
Summary(fr): Le programme de manipulation d'images de GNU.
Summary(de): Das GNU-Bildbearbeitungs-Programm
Summary(tr): Çizim, boyama ve görüntü iþleme programý

%description
The GIMP is an image manipulation program suitable for photo retouching,
image composition and image authoring.  Many people find it extremely useful
in creating logos and other graphics for web pages.  The GIMP has many of the
tools and filters you would expect to find in similar commercial offerings,
and some interesting extras as well.

The GIMP provides a large image manipulation toolbox, including channel
operations and layers, effects, sub-pixel imaging and anti-aliasing,
and conversions, all with multi-level undo.

This version of The GIMP includes a scripting facility, but many of the
included scripts rely on fonts that we cannot distribute.  The GIMP ftp
site has a package of fonts that you can install by yourself, which
includes all the fonts needed to run the included scripts.  Some of the
fonts have unusual licensing requirements; all the licenses are documented
in the package.  Get ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz
and ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz if you are so
inclined.  Alternatively, choose fonts which exist on your system before
running the scripts.

%description -l pt_BR
O GIMP é um programa de manipulação de imagens adequado para retoque
de fotos, composição e editoração de imagens. Muitas pessoas o acham
extremamente útil na criação de logos e outros gráficos para páginas
web. O GIMP tem muitas ferramentas e filtros normalmente encontrados
em aplicações comerciais similares, além de características extras
bem interessantes.

O GIMP fornece uma extensa caixa de ferramentas de manipulação de
imagem, incluindo camadas, efeitos, formação de imagem subpíxel e
anti-aliasing, conversões, todos com desfazimento em vários níveis
(multi-level undo).

%description -l es
GIMP es un programa de manejo de imágenes adecuado para retoque
de fotos, composición y editoración de imágenes. Muchas personas
lo encuentran extremamente útil en la creación de logos y otros
gráficos para páginas web. GIMP tiene muchas herramientas y filtros
normalmente encontrados en aplicaciones comerciales similares,
además de características extras bien interesantes.  GIMP ofrece una
extensa caja de herramientas de manejo de imagen, incluyendo camadas,
efectos, formación de imagen subpíxel y antialiasing, conversiones,
todos con deshacer en varios niveles (multi-level undo).

%package devel
Summary: GIMP plugin and extension development kit
Summary(pt_BR): Kit de desenvolvimento de "plugins" extensões para o GIMP
Summary(es): Kit de desarrollo de "plugins" extensiones para GIMP
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: gtk+-devel
Prereq: info
Summary(fr): Plugin GIMP et kit de développement d'extensions
Summary(de): GIMP-Plugin und Extension Development Kit
Summary(tr): GIMP plugin ve uzantý geliþtirme araçlarý
Requires: gimp-libgimp = %{PACKAGE_VERSION}

%description devel
Static libraries and header files for writing GIMP plugins and extensions.

%description -l pt_BR devel
Bibliotecas estáticas e arquivos de inclusão para escrever extensões
e plugins para o Gimp.

%description -l es devel
Bibliotecas estáticas y archivos de inclusión para escribir
extensiones y plugins para Gimp.

%description -l fr devel
Libraries statiques et fichiers d'en-tête pour ecrire des plugins et
des extensions pour GIMP.

%description -l de devel
Statische Libraries und Header-Dateien zum Schreiben von
GIMP-Plugins und -Erweiterungen

%description -l tr devel
GIMP plugin ve uzantý yazmak için gereken kitaplýklar ve baþlýk dosyalarý

%package libgimp
Summary: GIMP libraries
Summary(pt_BR): Bibliotecas GIMP
Summary(es): Bibliotecas GIMP
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Copyright: LGPL
Summary(fr): Librairies pour gimp.
Summary(de): GIMP-Libraries
Summary(tr): GIMP kitaplýklarý
Prereq: ldconfig

%description libgimp
Libraries used to communicate between The GIMP and other programs which
may function as "GIMP plugins".

%description -l pt_BR libgimp
Bibliotecas para comunicação entre o GIMP e outros programas que
podem funcionar como plugins.

%description -l es libgimp
Bibliotecas para comunicación entre GIMP y otros programas que
pueden funcionar como plugins.

%prep
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"

if [ ! -f configure ]; then
  ./autogen.sh --prefix=/usr
else
  ./configure --prefix=/usr
fi

make

%install

mkdir -p $RPM_BUILD_ROOT/usr/info $RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/bin \
	$RPM_BUILD_ROOT/etc/X11/wmconfig \
	$RPM_BUILD_ROOT/usr/share/icons/mini
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/gimp
install $RPM_SOURCE_DIR/wilbur.xpm $RPM_BUILD_ROOT/usr/share/icons/
install $RPM_SOURCE_DIR/mini-wilbur.xpm $RPM_BUILD_ROOT/usr/share/icons/mini/
install $RPM_SOURCE_DIR/Gimp.kdelnk $RPM_BUILD_ROOT/usr/share/gimp/

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/





tar xvfpz $RPM_SOURCE_DIR/gimp-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post 
/sbin/ldconfig
if [ -d /opt/kde/share/applnk/Graphics ] ; then
	ln -s /usr/share/gimp/Gimp.kdelnk /opt/kde/share/applnk/Graphics
fi

%postun
/sbin/ldconfig
if [ -f /opt/kde/share/applnk/Graphics/Gimp.kdelnk ] ; then
	rm -f /opt/kde/share/applnk/Graphics/Gimp.kdelnk
fi

%post libgimp -p /sbin/ldconfig

%postun libgimp -p /sbin/ldconfig

%files
%defattr(-, root, root)
%attr(644, root, root) %config /etc/X11/wmconfig/gimp
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%doc docs/*.txt docs/*.eps docs/*.ps
/usr/share/gimp
/usr/bin/gimp
/usr/lib/gimp
/usr/man/*/*
/usr/share/icons/mini/*.xpm
/usr/share/icons/*.xpm

%files devel
%defattr(-, root, root)
/usr/bin/gimptool
/usr/lib/lib*.a
/usr/lib/lib*.la
#/usr/lib/lib*.so
/usr/include/*
/usr/share/aclocal/*

%files libgimp
%defattr(-,root,root)
%attr(755,root,root) /usr/lib/lib*.so*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- BuildPreReq: aalib-devel 8)

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat May 15 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with aalib support (version 1.2)

* Mon Apr  5 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- fixes file confict
- final rebuild for 3.0 spanish edition

* Mon Apr 05 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Removed /usr/lib/*.so from package devel (Those files belong to libgimp)

* Mon Apr 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.0.4

* Wed Mar 31 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.0.3 final

* Sun Mar 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed find-requires

* Wed Mar 24 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Wed Mar 24 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 22 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated to latest CVS version
- Requires gtk+ >= 1.2.0 now

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Thu Dec 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Gimp.kdelnk: if KDE is installed the %post script will make a link
  to a Gimp.kdelnk in /opt/kde/share/applnk/Graphics

* Fri Nov 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Oct 16 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.0.2
- gimp.wmconfig translated

* Tue Sep 29 1998 Cristian Gafton <gafton@redhat.com>
- added gimp.m4 to the %files list
- updated to 1.0.1; enable again libgimp sub-package
- packaged for 5.2
- use defattr on the files list
- added the xpm files back to the srpm

* Thu Sep 10 1998 Michael Fulbright <msf@redhat.com>
- updated to version 1.0

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for fr, de, tr

* Sat May 09 1998 Erik Troan <ewt@redhat.com>
- define %ver and %rel from the Release: and Version: tags rather then the
  other way around (this way allows automated tools to increment the release
  number)
- added -q to %setup

* Mon May 04 1998 Michael K. Johnson <johnsonm@redhat.com>
- requires gtk+ >= 1.0.1 now

* Mon Apr 20 1998 Marc Ewing <marc@redhat.com>
- include *.xpm and .wmconfig in CVS source
- removed explicit glibc require

* Thu Apr 16 1998 Marc Ewing <marc@redhat.com>
- Handle builds using autogen.sh
- SMP builds
- put in CVS, and tweak for automatic CVS builds

* Sun Apr 12 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Upgraded to 0.99.26

* Sat Apr 11 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Upgraded to 0.99.25

* Wed Apr 08 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Upgraded to version 0.99.24

* Sun Apr 05 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Stop building the docs - they require emacs and
  (even worse), you must run X.

* Fri Mar 27 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- upgraded to 0.99.23

* Sat Mar 21 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- No longer requires xdelta, that was a bug on my part
- spec cleanup, changed libgimp copyright, can now be
  built by non-root users, removed some lines in the description

* Fri Mar 20 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- upgraded to 0.99.22

* Sun Mar 15 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- upgraded to 0.99.21

* Thu Mar 12 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Upgraded to 0.99.20

* Mon Mar 09 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Recompiled with gtk+ 0.99.5
- Now requires gtk+ >= 0.99.5 instead of gtk+ 0.99.4
