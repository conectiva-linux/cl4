Summary: converts and manipulates GIFs
Summary(pt_BR): Converte e manipula GIFs
Summary(es): Convierte y manipula GIFs
Name: giftrans
Version: 1.12.2
Release: 5cl
Copyright: BSD
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: ftp://ftp.rz.uni-karlsruhe.de/pub/net/www/tools/giftrans-1.12.2.tar.gz
Buildroot: /var/tmp/giftrans-root
Summary(de): konvertiert und manipuliert GIFs 
Summary(fr): converti et manipule des GIFs
Summary(tr): GIF dosyalarýný baþka biçimlere çevirir

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr


* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>

- udpated version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>

- built against glibc

%description
This program can convert and manipulate GIF images from the 
command line.  It is most useful for making a color transparent
for web sites.

%description -l pt_BR
Este programa na linha de comando pode converter e manipular
imagens GIF. Ele é bastante usado para fazer GIF transparentes para
web sites.

%description -l es
Este programa en la línea de comando puede convertir y manipular
imágenes GIF. Se usa bastante para hacer GIF transparentes para
sitios web.

%description -l de
Dieses Programm kann GIF-Bilder aus der Befehlszeile konvertieren und 
manipulieren. Besonders praktisch ist es, um eine Farbe für Web-Seiten
transparent zu machen. 

%description -l fr
Ce programme convertit et manipule des images GIF à partir de
la ligne de commande. Il est surtout utilisé pour créer une
couleur transparente pour les sites web.

%description -l tr
Bu program, GIF biçimindeki resim dosyalarýný baþka biçimlere çevirir. En
yaygýn kullaným alanlarýndan biri, web siteleri için resimleri saydam hale
getirmektir.

%prep
%setup

%build
gcc -Dvoidd=void $RPM_OPT_FLAGS -s -o giftrans giftrans.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
install -s -m 755 giftrans $RPM_BUILD_ROOT/usr/bin
install giftrans.1 $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT
 

%files
/usr/bin/giftrans
/usr/man/man1/giftrans.1
