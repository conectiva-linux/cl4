Summary: X based image viewer for darned near all images
Summary(pt_BR): Visualizador de imagens para X para quase todos os formatos de imagens
Summary(es): Visualizador de imágenes para X para cuasi todos los formatos de imágenes
Name: xv
Version: 3.10a
Release: 17cl
Copyright: Shareware
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
#Source0: ftp://ftp.cis.upenn.edu/pub/xv/xv-3.10a.tar.gz
# recompressed with bzip2
Source0: ftp://ftp.cis.upenn.edu/pub/xv/xv-3.10a.tar.bz2
Source1: ftp://swrinde.nde.swri.edu/pub/png/applications/xv-3.10a-png-1.2d.tar.gz
Source2: xv.wmconfig
Source800: xv-wmconfig.i18n.tgz
Patch0: xv-3.10a-linux.patch
Patch1: xv-3.10a.JPEG-patch
Patch2: xv-3.10a-glibc.patch
Url: http://www.trilon.com/xv/xv.html
BuildRoot: /var/tmp/xv-root
Summary(de): X-basierender Bild-Viewer für praktische sämtliche Grafiken
Summary(fr): Visualisateur sous X pour quasiment tous les types d'images
Summary(tr): X tabanlý resim görüntüleyici

%description
This is the famous 'xv' by John Bradley.  It is shareware, but
we ship it with the permission of the authors.  It is a graphics
viewer for many file types, including gif, jpg, tiff, xwd, etc.
It also have manipulation features such as cropping, expanding,
etc.

%description -l pt_BR
Este é o famoso 'xv' de John Bradley. Ele é shareware, mas nós
o distribuimos com a permissão dos autores. É um visualizador
gráfico para vários tipos de arquivos, incluindo gif, jpg, tiff,
xwd, etc. Também possui características de manipulação como corte,
expansão, etc.

%description -l es
Este es el famoso 'xv' de John Bradley. Es shareware, pero
nosotros lo distribuimos con la permisión de los autores. Es un
visor gráfico para varios tipos de archivos, incluyendo gif, jpg,
tiff, xwd, etc. También posee características de manejo como corte,
expansión, etc.

%description -l de
Dies ist das berühmte 'xv' von John Bradley, ein Shareware-
Programm, das wir mit Erlaubnis des Autors liefern. Es ist
ein Grafik-Viewer für diverse Dateitypen, einschließlich gif, 
funktionen wie Trimmen, Strecken u.ä.

%description -l fr
Le célébre xv de John Bradley. C'est shareware, mais nous le distribuons
avec la permission de l'auteur. C'est un visualiseur graphique pour
de nombreux formats de fichier dont gif, jpg, tiff, xwd, etc.
Il offre aussi des fonctionnalités comme la capture, l'extension,la retouche de palette, etc.

%description -l tr
xv baþta PNG, GIF, JPG, BMP, XBM, XPM olmak üzere birçok resim dosyasýný
görüntüleyebilir, deðiþik formatlarda kaydedebilir ve üzerinde boyutlandýrma,
renk deðiþtirme gibi bazý temel iþlemleri yapabilir. Çok detaylý iþlemler
yapamamasýna raðmen temel resim iþlemlerinde öncellikle kullanýlabilecek,
kullanýþlý arayüzüne sahip bir programdýr.

%prep
%setup -q
cd $RPM_BUILD_DIR/xv-3.10a
tar xvfz $RPM_SOURCE_DIR/xv-3.10a-png-1.2d.tar.gz
patch -p1 --quiet < xvpng.diff
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{X11R6/bin,X11R6/man/man1,usr/lib}

make	BINDIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
	MANDIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
	LIBDIR=$RPM_BUILD_ROOT/usr/lib \
	install

( cd $RPM_BUILD_ROOT
  strip ./usr/X11R6/bin/{xv,bggen,vdcomp,xcmap,xvpictoppm}
  mkdir -p ./etc/X11/wmconfig
  #install -m644 $RPM_SOURCE_DIR/xv.wmconfig ./etc/X11/wmconfig/xv
)



tar xvfpz $RPM_SOURCE_DIR/xv-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README docs/xvdocs.ps BUGS CHANGELOG IDEAS 
%config /etc/X11/wmconfig/xv
/usr/X11R6/bin/xv
/usr/X11R6/bin/bggen
/usr/X11R6/bin/vdcomp
/usr/X11R6/bin/xcmap
/usr/X11R6/bin/xvpictoppm
/usr/X11R6/man/man1/xv.1
/usr/X11R6/man/man1/bggen.1
/usr/X11R6/man/man1/xcmap.1
/usr/X11R6/man/man1/xvpictoppm.1
/usr/X11R6/man/man1/vdcomp.1

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0, use new libjpeg (reported by rodrigo@conectiva.com)

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry 

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- various spec file cleanups
- added patch to manipulate PNG files

* Mon Aug 25 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- incorporated new jpegv6 patch from the author's web site
