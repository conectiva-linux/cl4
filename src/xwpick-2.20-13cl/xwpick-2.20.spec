Summary: efficient X screen grabber
Summary(pt_BR): Capturador de Telas X
Summary(es): Capturador de Pantallas X
Name: xwpick
Version: 2.20
Release: 13cl
Copyright: MIT
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Source: ftp://ftp.x.org/contrib/applications/xwpick-2.20.tar.gz
Prefix: /usr
BuildRoot: /var/tmp/xwpick-root
Summary(de): guter X-Screen-Grabber
Summary(fr): capture d'écran X efficace
Summary(tr): X ekran kaydedicisi

%description
Xwpick lets you pick an image from an arbitrary window or
rectangular area of an X11-server and write it to a file
in a variety of formats.

%description -l pt_BR
Xwpick deixa-o capturar uma imagem de uma janela arbitrária ou uma
área retangular de um servidor X11 e gravá-la em um arquivo em uma
variedade de formatos.

%description -l es
Xwpick te deja capturar una imagen de una ventana arbitraria o un
área rectangular de un servidor X11 y la graba en un archivo en
una variedad de formatos.

%description -l de
Mit Xwpick können Sie ein Bild aus einem beliebigen Fenster
oder einer rechteckigen Fläche eines X11-Servers wählen und in
einer Datei in verschiedenen Formaten speichern.

%description -l fr
xwpick vous permet de capturer une image d'une fenêtre quelconque
ou d'une zone rectangulaire d'un serveur X11 et le sauvegarde dans
un fichier d'un des nombreux formats supportés.

%description -l tr
Xwpick ile ekranýn belirli bir bölümünü ya da bir pencereyi seçip
istediðiniz bir resim formatýnda kaydedebilirsiniz.

%prep
%setup -q

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xwpick
/usr/X11R6/man/man1/xwpick.1

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
