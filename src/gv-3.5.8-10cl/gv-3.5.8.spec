Summary: Enhanced frontend for ghostscript
Summary(pt_BR): Frontend para ghostscript com características adicionais
Summary(es): Frontend para ghostscript con características adicionales
Name: gv
Version: 3.5.8
Release: 10cl
Copyright: GPL
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Requires: ghostscript
# was .gz
Source0: ftp://thep.physik.uni-mainz.de/pub/gv/unix/gv-3.5.8.tar.bz2
Source1: gv-3.5.8-wmconfig
Source800: gv-wmconfig.i18n.tgz
Patch0: gv-3.5.8-config.patch
Url: http://wwwthep.physik.uni-mainz.de/~plass/gv/
Obsoletes: ghostview
BuildRoot: /var/tmp/gv-root
Summary(de): Verbessertes Frontend für Ghostscript 
Summary(fr): Frontal amélioré pour ghostscript
Summary(tr): Ghostscript için grafik arayüz

%description
gv allows to view and navigate through PostScript and PDF documents on 
an X display by providing a user interface for the ghostscript interpreter. 
gv is based upon an earlier program known as ghostview.

%description -l pt_BR
Gv permite visualizar e navegar através de documentos PostScript e
PDF em um display X, oferecendo uma interface para o interpretador
ghostscript. Gv é baseado em um novo programa conhecido como
ghostview.

%description -l es
Gv permite visualizar y navegar a través de documentos PostScript y
PDF en un display X, ofreciendo una interface para el interpretador
ghostscript. Gv está basado en un nuevo programa conocido como
ghostview.

%description -l de
gv ermöglicht das Einsehen und Navigieren von PostScript- und PDF-
Dokumenten unter X, indem es eine Benutzeroberfläche für den Ghostscript-
Interpreter bereitstellt. gv basiert auf dem älteren Programm ghostview.

%description -l fr
gv permet de visualiser et de naviguer dans les documents PostScript
et PDF sur un écran X en offrant une interface pour l'interpréteur
ghostscript. gv est basé sur un ancien programme appelé ghostview.

%description -l tr
gv, PostScript ve PDF dosyalarýný bir X ekraný üzerinde gösterebilen ve
üzerlerinde dolaþmayý saðlayan bir ghostscript arayüzüdür. Ghostview adýyla
bilinen programdan yola çýkýlarak hazýrlanmýþtýr.

%prep
%setup -q
%patch0 -p1 -b .config

%build
xmkmf
make Makefiles
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man
gunzip doc/*gz
ln -sf gv $RPM_BUILD_ROOT/usr/X11R6/bin/ghostview

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/




tar xvfpz $RPM_SOURCE_DIR/gv-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES COPYING doc/*.html doc/*doc doc/*txt
/usr/X11R6/bin/gv
/usr/X11R6/lib/X11/gv
/usr/X11R6/lib/X11/app-defaults/GV
/usr/X11R6/man/man1/gv.1x
/etc/X11/wmconfig/gv
/usr/X11R6/bin/ghostview

%changelog
* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Wed Dec 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o binutils 2.9.1.0.17, gcc 2.7.2.3 e XFree86 3.3.3 gerado com o gcc

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- Manhattan build

* Thu Nov 06 1997 Cristian Gafton <gafton@redhat.com>
- we are installin a symlink to ghostview

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- updated to 3.5.8

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 15 1997 Erik Troan <ewt@redhat.com>
- added ghostscript requirement, added errlist patch for glibc.
