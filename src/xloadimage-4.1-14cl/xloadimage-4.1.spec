Summary: X based image viewer
Summary(pt_BR): Visualizador de imagem baseado em X
Summary(es): Visualizador de imagen basado en X
Name: xloadimage
Version: 4.1
Release: 14cl
Copyright: MIT
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Source: ftp://ftp.x.org/R5contrib/xloadimage.4.1.tar.bz2
Patch0: xloadimage.4.1-linux.patch
Patch1: xloadimage.4.1-nobr.patch
BuildRoot: /var/tmp/xloadimage-root
Summary(de): Bildbetrachter für X
Summary(fr): Visualiseur d'images sous X.
Summary(tr): X tabanlý resim görüntüleyici

%description
Xloadimage displays images in an X11 window, loads them onto the root
window, or writes them into a file.  Many image types are recognized.

%description -l pt_BR
Xloadimage mostra imagens em uma janela X11, carrega-as como
fundo, ou grava-as em um arquivo. Vários tipos de imagem são
reconhecidos.

%description -l es
Xloadimage enseña imágenes en una ventana X11, las caarga como fondo,
o las graba en un archivo. Se reconocen varios tipos de imágenes.

%description -l de
Xloadimage stellt Bilder in einem X11-Fenster dar, lädt sie in das Root.
Fenster oder schreibt sie in eine Datei. Zahlreiche Bildformate werden unterstützt.

%description -l fr
Xloadimage permet de visualiser des images sous XWindow, de les mettre en
fond d'écrans, ou de les enregistrer dans un fichier. De nombreux formats
d'images sont reconnus par ce programme.

%description -l tr
Xloadimage, bir X penceresi içinde resimleri gösterebilir, arkaplana
yerleþtirebilir ya da bir dosyaya pek çok dosya formatýnda yazabilir.

%prep
%setup -q -n xloadimage.4.1
%patch0 -p1
%patch1 -p1 -b .nobr

cd jpeg
mv Makefile Makefile.orig
ln -s makefile.ansi Makefile

%build
xmkmf
cd jpeg
make libjpeg.a
cd ..
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

make	DESTDIR=$RPM_BUILD_ROOT \
	SYSPATHFILE=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/Xloadimage \
	install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/X11R6/lib/X11/app-defaults/Xloadimage
/usr/X11R6/bin/xloadimage
/usr/X11R6/bin/xview
/usr/X11R6/bin/xsetbg
/usr/X11R6/man/man1/xloadimage.1x

%changelog
* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Aug 25 1997 Erik Troan <ewt@redhat.com>
- built against glibc
