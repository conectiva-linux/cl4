Summary: console viewer for many graphics formats
Summary(pt_BR): Visualizador para muitos formatos de gráficos (console)
Summary(es): Visualizador para muchos formatos de gráficos (consola)
Name: zgv
Version: 4.2
Release: 7cl
Copyright: GPL
Exclusivearch: i386
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: ftp://sunsite.unc.edu/pub/Linux/apps/graphics/viewers/newzgv-4.2.tar.bz2
Patch: zgv-3.0-redhat.patch
Patch1: zgv2.7-glibc.patch
Patch2: zgv-4.2-security.patch
Patch3: zgv-4.0-yetagain.patch

Prefix: /usr
Summary(de): Konsolenbetrachter für viele Grafikformate
Summary(fr): Visualiseur d'image en mode console, pour de nombreux formats graphiques.
Summary(tr): Birçok resim formatýný görüntüleyebilen konsol aracý

%description
Zgv is a picture viewer capable of displaying GIF files as defined by
CompuServe, with the exceptions listed in the RESTRICTIONS section. It
is also capable of displaying JPEG/JFIF files using the Independant
JPEG Group's JPEG software, PBM/PGM/PPM files as used by pbmplus and
netpbm, Microsoft Windows and OS/2 BMP files, Targa (TGA) files, and
the new PNG format.

%description -l pt_BR
Zgv é um visualizador de imagens capaz de mostrar arquivos tipo
"GIF" como as definidas pela CompuServe. Ele também é capaz de
mostrar arquivos JPEG/JFIF usando o "Independent JPEG Group JPEG
software", arquivos PBM/PGM/PPM como os usados pela pbmplus e netpbm,
arquivos Microsoft Windows e OS/2 BMP, arquivos Targa (TGA), e o
novo formato PNG.

%description -l es
Zgv es un visualizador de imágenes capaz de enseñar archivos tipo
"GIF" como las definidas por la CompuServe. También es capaz de
enseñar archivos JPEG/JFIF usando "Independant JPEG Group JPEG
software", archivos PBM/PGM/PPM como los usados por la pbmplus
y netpbm, archivos Microsoft Windows y OS/2 BMP, archivos Targa
(TGA), y el nuevo formato PNG.

%description -l de
zgv ist ein Bild-Viewer, der GIF-Dateien nach der CompuServe-Definition 
anzeigen kann, abgesehen von den Ausnahmen im Teil RESTRICTIONS. Ferner 
kann er JPEG/JFIF-Dateien unter Verwendung der JPEG-Software der 
unabhängigen JPEG-Group, PBM/PGM/PPM-Dateien wie sie pbmplus und netpbm 
benutzen, sowie Microsoft Windows und OS/2 BMB-Dateien, Targa (TGA) und 
das neue PNG-Format anzeigen. 

%description -l fr
Zgv est un visualisateur de fichiers GIF tels que ceux qui sont définis
par CompuServe, avec les exceptions listées dans la section RESTRICTIONS.
Il peut aussi afficher les fichiers JPEG/JTIF utilisés par le logiciel
JPEG de l'Independant JPEG Group, les fichiers PBM/PGM/PPM utilisés par
pbmplus et netpbm, les fichiers BMP de Microsoft Windows et OS/2,
les fichiers Targa (TGA) et le nouveau format PNG.

%description -l tr
Zgv, konsol ortamýndan CompuServe'in GIF formatý (RESTRICTIONS ile
belirtilenler dýþýnda), JPEG/JFIF, PGM/PBM/PPM, Bitmap (BMP), Targa (TGA) ve
yeni PNG formatlarýndaki resimleri görüntüleyebilmektedir.

%changelog
* Fri Jun  4 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition
- Removed suid bit from /usr/bin/zgv

* Sat Mar 20 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Feb 19 1999 Marcelo Tosatti <marcelo@conectiva.com>
- aplicado patch do Chris Evans para remover opção -a

* Thu Nov 26 1998 Marcelo Tosatti <marcelo@conectiva.com>
- segurança melhorada 

* Thu Nov 26 1998 Marcelo Tosatti <marcelo@conectiva.com>
- upgrade para 4.1
 
* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Mon Jul 13 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt against svgalib 1.3.0

* Tue Jun 30 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 4.0

* Thu Jun 11 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Added pt_BR translations

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Mon Apr 20 1998 Erik Troan <ewt@redhat.com>

- updated to version 3.0

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>

- updated spec file and upgraded to version 2.8

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>

- build against new libpng

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>

- built against glibc

%prep
%setup -n zgv-4.2
%patch -p1 -b .config
%patch1 -p1 -b .glibc
%patch2 -p1 
%patch3 -p1 
%build
make


%install
make install
chmod 755 $RPM_BUILD_ROOT/usr/bin/zgv

%files
/usr/bin/zgv
/usr/man/man1/zgv.1
