Summary: A text formatting package based on SGML.
Summary(pt_BR): Sistema de formatação de texto usado pela Documentação do Projeto Linux Summary(es): Sistema de formateado de texto usado por la Documentación del Proyecto Linux
Name: sgml-tools
Obsoletes: linuxdoc-sgml
Version: 1.0.9
Release: 6cl
Copyright: freeware
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Source: http://www.consultronics.com/~cdegroot/sgmltools/dist/%{name}-%{version}.tar.gz
Patch: sgml-tools-1.0.6-letter.patch
Patch1: sgml-tools-1.0.9-egcs.patch
Url: http://www.sgmltools.org
Buildroot: /var/tmp/%{name}-root
Requires: jade

%description
SGMLtools is a text formatting package based on SGML (Standard
Generalized Markup Language).  SGMLtools allows you to produce
LaTeX, HTML, GNU info, LyX, RTF, plain text (via groff), and other
format outputs from a single source.  SGMLtools is intended for
writing technical software documentation.

Install SGMLTools if you need a text formatting program that can
produce a variety of different formats from a single source file.
You should probably also install and try SGMLTtools if you're going
to write technical software documentation.

%description -l pt_BR
O SGML-Tools é um formatador de texto baseado em SGML, que
permite produzir uma variedade de formatos de saída. Você pode
criar PostScript e dvi (com LaTex), texto puro (com groff), HTML,
e arquivos textinfo de um único arquivo fonte SGML.

%description -l es
SGML-Tools es un formateador de texto basado en SGML, que permite
producir una variedad de formatos de salida. Puedes crear PostScript
y dvi (con LaTeX), texto puro (con groff), HTML, y archivos textinfo
de un único archivo fuente SGML.

%prep
%setup
rm -rf $RPM_BUILD_ROOT
%patch -p1
%patch1 -p1 -b .egcs

%build
CC=egcs CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/* || :

# Remove this file, as it belongs to jade
rm -f $RPM_BUILD_ROOT/usr/bin/nsgmls

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
/usr/lib/sgml-tools
/usr/lib/perl5/Text/EntityMap.pm
/usr/lib/entity-map
/usr/lib/sgml
/usr/doc/sgml-tools
/usr/bin/*
/usr/man/*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added Requires: jade
- removed /usr/bin/nsgmls, as it belongs to jade

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- we aren't going to 2.0.x for 6.0, using 1.0.9 instead (more stable)

* Thu Aug 20 1998 Bill Nottingham <notting@redhat.com>
- updated to 1.0.7

* Tue May 05 1998 Donnie Barnes <djb@redhat.com>
- changed default papersize to letter (from a4...sorry Europeans :-)
  use --papersize=a4 on any sgml2* command to change it or remove the
  patch from this spec file and rebuild.

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.0.6

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jan 12 1998 Donnie Barnes <djb@redhat.com>
- updated from 0.99 to 1.0.3
- added BuildRoot

* Sat Nov 01 1997 Donnie Barnes <djb@redhat.com>
- fixed man pages

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- new release - Obsoletes linuxdoc-sgml
