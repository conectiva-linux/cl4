Summary: X11 Pixmap Library
Summary(pt_BR): Biblioteca Pixmap X11
Summary(es): Biblioteca Pixmap X11
Name: xpm
Version: 3.4j
Release: 8cl
Copyright: MIT
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: ftp://ftp.x.org/contrib/libraries/xpm-3.4j.tar.gz
Source1: ftp://ftp.x.org/contrib/libraries/xpm-doc-A4.PS.gz 
Source2: ftp://ftp.x.org/contrib/libraries/xpm-tutorial.PS.gz 
Source3: ftp://ftp.x.org/contrib/libraries/xpm.FAQ 
Source4: ftp://ftp.x.org/contrib/libraries/xpm.README 
Source5: ftp://ftp.x.org/contrib/libraries/xpm_examples.tar.gz
%define LIBVER 4.10
%define NAME xpm
%define VERSION 3.4j
BuildRoot: /var/tmp/xpm-root
Summary(de): X11 Pixmap-Library
Summary(fr): Librairie Pixmap pour X11.
Summary(tr): X11 Pixmap kitaplýðý

%description
Allows applications to display color, bitmapped pictures. Used by a large
number of popular X Windows programs to enhance the user interface.

%description -l pt_BR
Permite que aplicações mostrem imagens bitmap com cores. Usado por
um grande número de programas populares do X Window para melhorar
a interface do usuário.

%description -l es
Permite que aplicaciones muestren imágenes bitmap con colores. Usado
por un gran número de programas populares del X Window para mejorar
la interface del usuario.


%package devel
Requires: xpm
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Summary: Development libraries and header files for X Pixmap library
Summary(pt_BR): Bibliotecas de desenvolvimento e arquivos de inclusão para a biblioteca X Pixmap
Summary(es): Bibliotecas de desarrollo y archivos de inclusión para la biblioteca X Pixmap
Summary(de): Entwicklungs-Libraries und Header-Dateien für die X-Pixmap-Library 
Summary(fr): Bibliothèques et en-têtes de développement pour la bibliothèque Pixmap X
Summary(tr): X Pixmap kitaplýðýný kullanan programlar geliþtirmek için gerekli dosyalar

%description devel
Allows you to develop applications that display bitmaps in X-Windows.

%description -l pt_BR devel
Bibliotecas e arquivos de cabeçalho para a biblioteca "X
Pixmap". Possibilita o desenvolvimento de aplicações que mostram
bitmaps no X Window.

%description -l es devel
Bibliotecas y archivos de encabezamiento para la biblioteca "X
Pixmap". Posibilita el desarrollo de aplicaciones que enseñan
bitmaps en el X Window.

%description -l de devel
Ermöglicht die Entwicklung von Anwendungen zum Darstellen von Bitmaps in X-Windows.

%description -l de
Ermöglicht Anwendungen, farbige Bitmap-Bilder darzustellen. Wird von
vielen beliebten X-Windows-Programmen zum Verbessern der
Benutzeroberfläche verwendet.

%description -l fr devel
Permet de développer des applications affichant des bitmaps sous X11"

%description -l fr
Permet aux applications d'afficher des images bitmap en couleur. Utilisé
par un grand nombre de programmes X Windows pour améliorer l'interface
utilisateur.

%description -l tr devel
xpm kitaplýðýný kullanan programlar geliþtirmek için gerekli dosyalar

%description -l tr
Uyugulamalarýn renkli ve bitmap resim göstermelerini saðlayan kitaplýklarý
içerir. Kullanýcý arabirimini geliþtiren çok sayýda X Window programý
tarafýndan kullanýlýr.

%prep
%setup -q
cd $RPM_SOURCE_DIR
cp xpm-doc-A4.PS.gz xpm-tutorial.PS.gz xpm.FAQ xpm.README xpm_examples.tar.gz $RPM_BUILD_DIR/%{NAME}-%{VERSION}

%build
xmkmf
make Makefiles
##install -m644 lib/xpm.h /usr/X11R6/include/X11/xpm.h
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
ln -sf libXpm.so.%{LIBVER} $RPM_BUILD_ROOT/usr/X11R6/lib/libXpm.so

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/X11R6/lib/libXpm.so.%{LIBVER}

%files devel
%defattr(-,root,root)
%doc xpm-doc-A4.PS.gz xpm-tutorial.PS.gz xpm.FAQ xpm.README xpm_examples.tar.gz
/usr/X11R6/lib/libXpm.a
/usr/X11R6/include/X11/xpm.h
/usr/X11R6/bin/sxpm
/usr/X11R6/lib/libXpm.so

%changelog
* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- upgraded to 3.4j
- spec file cleanups
- added docs to the devel package

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc
