Summary: paint program for X
Summary(pt_BR): Programa de desenho para X
Summary(es): Programa de dise�o para X
Name: xpaint
Version: 2.4.9
Release: 10cl 
Copyright: MIT
Icon: xpaint.gif
Group: Applications/Multimedia
Group(pt_BR): Aplica��es/Multim�dia
Group(es): Aplicaciones/Multimedia
Source: ftp://sunsite.unc.edu/pub/Linux/apps/graphics/draw/xpaint-2.4.9.tar.bz2
Source800: xpaint-wmconfig.i18n.tgz
Patch: xpaint-2.4.7-config.patch
Patch1: xpaint-2.4.7-glibc.patch
BuildRoot: /var/tmp/xpaint-root
Summary(de): Malprogramm f�r X
Summary(fr): Programme de dessin sous X
Summary(tr): X alt�nda boyama program�

%description
XPaint is a color image editing tool which features most standard
paint program options, as well as advanced features such as image
processing algorithms.  It allows for the editing of multiple images
simultaneously and supp

%description -l pt_BR
XPaint � uma ferramenta de edi��o de imagens coloridas que apresenta
a maioria das op��es-padr�o de programas de pintura, assim como
caracter�sticas avan�adas como processamento de imagens atrav�s
de algoritmos. Ele tamb�m permite a edi��o de m�ltiplas imagens
simultaneamente.

%description -l es
XPaint es una herramienta de edici�n de im�genes coloridas que
presenta la mayor�a de las opciones padr�n de programas de pintura,
as� como caracter�sticas avanzadas como procesamiento de im�genes
a trav�s de algoritmos. Tambi�n permite la edici�n de m�ltiples
im�genes simult�neamente.

%description -l de
XPaint ist ein Farbbildbearbeitungs-Tool mit den meisten �blichen,
aber auch erweiterten Funktionen wie Bildverarbeitungsalgorithmen.
Sie k�nnen mehrere Bilder gleichzeitig bearbeiten.

%description -l fr
xpaint est un outil d'�dition d'images en couleur offrant la plupart
des options du programme paint, ainsi que des caract�ristiques avanc�es
comme des algorithmes de traitement d'image. Il permet l'�dition
simultan�e de plusieurs images et plus.

%description -l tr
Xpaint, X ortam�nda en temel resimleme yeteneklerini bar�nd�ran basit bir
programd�r.

%prep
%setup -q -n xpaint
%patch -p1 -b .config
%patch1 -p1 -b .glibc

%build
xmkmf
make Makefiles
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT MANDIR=/usr/X11R6/man/man1 install install.man

( cd $RPM_BUILD_ROOT
  mkdir -p ./etc/X11/wmconfig
#  cat > ./etc/X11/wmconfig/xpaint <<EOF
#xpaint name "xpaint"
#xpaint description "Programa de Desenho"
#xpaint group Gr�ficos
#xpaint exec "xpaint &"
#EOF
)



tar xvfpz $RPM_SOURCE_DIR/xpaint-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README README.PNG TODO Doc
%config /etc/X11/wmconfig/xpaint

/usr/X11R6/bin/xpaint
/usr/X11R6/lib/X11/app-defaults/XPaint
/usr/X11R6/man/man1/xpaint.1x

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations and wmconfig

* Mon Aug  3 1998 Jeff Johnson <jbj@redhat.com>
- build root.

* Tue Jun 09 1998 Mike Wangsmo <wanger@redhat.com>
- changed the docs from being %config files.

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- built against libpng 1.0

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new release
- wmconfig

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- build against new libpng

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- "make install.man" places man page in wrong location
