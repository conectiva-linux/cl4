Name: xbanner
Summary: Spruces up the standard xdm interface
Summary(pt_BR): Altera o fundo de tela na interface X11
Summary(es): Altera el fondo de la pantalla en la interface X11
Version: 1.31
Release: 7cl
Copyright: GPL
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
#Source: ftp://physics.fullerton.edu/pub/Linux/XBanner/XBanner1.31.tar.gz
# recompressed with bzip2
Source: ftp://physics.fullerton.edu/pub/Linux/XBanner/XBanner1.31.tar.bz2
Source1: XBanner.conectiva
Patch: xbanner-1.3-rh.patch
Buildroot: /var/tmp/xbanner-root
Summary(de): Verbessert die übliche xdm-Schnittstelle
Summary(fr): Améliore l'interface xdm standard.
Summary(tr): Standart xdm arabirimi yardýmcýsý

%description
XBanner displays text, patterns, and images on the root window. This allows
users to customize both their normal X background and the background used
on xdm style login screens.

%description -l pt_BR
XBanner mostra texto, modelos e imagens na janela root. Isso permite
usuários customizarem tanto o seu fundo do servidor X normal quanto
o fundo usado nas telas estilo xdm para login.

%description -l es
XBanner enseña texto, modelos y imágenes en la ventana root. Esto
permite a  los usuarios personalizar tanto el fondo del servidor
X normal como el fondo usado en las pantallas estilo xdm para login.

%description -l de
XBanner stellt Text, Muster und Bilder im Root-Fenster dar. Damit können
Sie den normalen Hintergrund von X und den von alten xdm-Login-
Bildschirmen anpassen.

%description -l fr
XBanner affiche des textes, des textures, et des images sur la fenêtre root.
Il permet à l'utilisateur de personnaliser à la fois leur fond d'écran X
normal et le fond d'écran utilisé sur les écrans de login du style xdm.

%description -l tr
XBanner, metin ve grafik dosyalarýnýn ana pencerede gösterilmesini saðlar.
Böylece kullanýcýlar hem kendi X arkaplanlarýný hem de xdm giriþ arkaplanlarý
yapýlandýrabilirler.

%prep
%setup -q -n XBanner1.31
%patch -p1 -b .patch

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/include/X11/pixmaps
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

make ROOT="$RPM_BUILD_ROOT" install
cp $RPM_SOURCE_DIR/XBanner.conectiva \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/XBanner
%clean
rm -rf $RPM_BUILD_ROOT

%files
# I left random_effect out because the default "make install" rule doesn't
# install it

#/usr/X11R6/bin/random_effect

/usr/X11R6/bin/freetemp
/usr/X11R6/bin/xbanner
/usr/X11R6/bin/xb_check
%doc samples docs/*
%config /usr/X11R6/lib/X11/app-defaults/XBanner

%changelog
* Fri May 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 17 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Dec 04 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- correções para o Conectiva Linux

* Fri Oct 30 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- cleaned up spec, built for 5.2 

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
