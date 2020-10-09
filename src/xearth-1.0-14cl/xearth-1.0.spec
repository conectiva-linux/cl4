Summary: Displays a lit globe in the background of your X screen
Summary(pt_BR): Mostra um globo terrestre em pano de fundo de seu tela X
Summary(es): Ense�a un globo terrestre, como tapiz de fondo, de tu pantalla X
Name: xearth
Version: 1.0
Release: 14cl
Copyright: MIT
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gr�ficos
Group(es): Pasatiempos/Gr�ficos
Source: ftp://cag.lcs.mit.edu/pub/tuna/xearth-1.0.tar.bz2
Source800: xearth-wmconfig.i18n.tgz
Patch: xearth-1.0-redhat.patch
Patch1: xearth-1.0-cnc.patch
BuildRoot: /var/tmp/xearth-root
Summary(de): Anzeige eines erleuchteten Globus im Hintergrund Ihres X-Bildschirms 
Summary(fr): Affiche un globe terrestre illumin� dans le fond de votre �cran X
Summary(tr): X ekran�n�z�n arkaplan�nda bir d�nya g�r�nt�s�

%description
Xearth displays a pseudo-3D globe that rotates to show the earth as it
actually is, including markers for major cities and Red Hat Software :-).

%description -l pt_BR
Xearth mostra um globo pseudo-3D que rotaciona para mostrar a terra
como ela realmente �, mostrando marcas para cidades principais,
RedHat Software e a Conectiva tamb�m :-))

%description -l es
Xearth ense�a un globo pseudo 3D que cumple un movimiento de rotaci�n
para ense�ar la tierra como realmente es, mostrando marcas en
ciudades principales, y en RedHat Software y Conectiva tambi�n :-))

%description -l de
Xearth stellt einen rotierenden pseudo-3D-Globus dar, auf dem
die wichtigsten St�dte und Red Hat Software eingezeichnet sind:-).

%description -l fr
Xearth affiche un globe en pseudo-3D qui tourne et montre la terre telle
qu'elle est sur le moment, avec les principales villes et...
Red Hat Software :-).

%description -l tr
xearth, d�nyan�n o saatte g�ne�e g�re durumunu ve �zerindeki belli ba�l�
�ehirleri grafik olarak g�sterir. �zellikle X ortam�nda arka plan olarak
kullan�lmas� tavsiye edilir. Bu durumda her be� dakikada bir arka plan resmi
kendisini g�ncelleyecektir.

%prep
%setup -q
%patch -p0
%patch1 -p0

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xearth <<EOF
#xearth name "xearth"
#xearth description "xearth"
#xearth group Passatempos
#xearth exec "xearth -fork"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xearth-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xearth
/usr/X11R6/man/man1/xearth.1x
%config /etc/X11/wmconfig/xearth

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- wmconfig
- conectiva's coordinates

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 29 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
