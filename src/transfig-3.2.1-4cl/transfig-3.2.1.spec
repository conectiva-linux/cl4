Summary: Converts .fig files (such as those from xfig) to other formats
Summary(pt_BR): Converte arquivos .fig (como os do xfig) para outros formatos
Summary(es): Convierte archivos .fig (como los del xfig) para otros formatos
Name: transfig
Version: 3.2.1
Release: 4cl
Copyright: distributable
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
# was .gz
Source: ftp://ftp.x.org/contrib/applications/drawing_tools/transfig/transfig.%{PACKAGE_VERSION}.tar.bz2
Patch0: transfig-3.2.1-imake.patch
Buildroot: /var/tmp/transfig-root
Summary(de): Konvertiert .fig-Dateien (z.B. aus xfig) in andere Formate
Summary(fr): Convertit les fichiers .fig (comme ceux d'xfig) en d'autres formats."
Summary(tr): fig dosyalarýný baþka biçimlere dönüþtürür

%description
TransFig is a set of tools for creating TeX documents with graphics
which are portable, in the sense that they can be printed in a wide
variety of environments.

%description -l pt_BR
TransFig é um conjunto de ferramentas para criação de documentos
TeX com gráficos que são portáveis, no sentido de que eles podem
ser impressos em uma grande variedade de ambientes.

%description -l es
TransFig es un conjunto de herramientas para creación de documentos
TeX con gráficos que son portables, en el sentido de que pueden
ser impresos en una gran variedad de ambientes.

%description -l de
TransFig ist ein Satz von Tools zum Erstellen von TeX-Dokumenten mit
Grafiken, die portabel sind, das heißt, sie können in einer großen Auswahl
von Umgebungen gedruckt werden.

%description -l fr
Transfig est un ensemble d'outils pour créer des documents textes avec
des graphiques portables, en ce sens qu'ils peuvent être imprimés dans
des nombreux environnements.

%description -l tr
TransFig, çizimler içeren TeX belgeleri üretebilmek için kullanýlan bir araç
kümesidir ve çeþitli ortamlarda çýktýsý alýnabilecek dosyalar yaratýr.

%prep
%setup -q -n transfig.%{PACKAGE_VERSION}
#%patch0 -p1

%build
xmkmf
make Makefiles

%ifarch alpha
make EXTRA_DEFINES="-Dcfree=free"
%else
make
%endif

%install
rm -rf $RPM_BUILD_ROOT
make BINDIR=$RPM_BUILD_ROOT/usr/X11R6/bin install
make MANSOURCEPATH=$RPM_BUILD_ROOT/usr/X11R6/man/man install.man

# Dunno why these are not installed
for i in fig2ps2tex fig2ps2tex.sh pic2tpic
do
	install -c -m 755 fig2dev/$i.script $RPM_BUILD_ROOT/usr/X11R6/bin/$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES NOTES README
/usr/X11R6/bin/transfig
/usr/X11R6/bin/fig2dev
/usr/X11R6/bin/fig2ps2tex
/usr/X11R6/bin/fig2ps2tex.sh
/usr/X11R6/bin/pic2tpic
/usr/X11R6/man/man1/fig2dev.1x
/usr/X11R6/man/man1/fig2ps2tex.1x
/usr/X11R6/man/man1/pic2tpic.1x
/usr/X11R6/man/man1/transfig.1x

%changelog
* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Jul  7 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.2.1.

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- add %clean.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Nov 13 1997 Otto Hammersmith <otto@redhat.com>
- fixed problem with Imakefile for fig2dev not including $(XLIB)
- build rooted.

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- recreated the glibc patch that is needed for an alpha build, missed it
  building on the intel.

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- updated version
- fixed source url

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
