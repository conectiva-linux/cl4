Summary: turns your X root into an aquarium
Summary(pt_BR): Transforma seu X em um aquário
Summary(es): Transforma tu X en un acuario
Name: xfishtank
Version: 2.0
Release: 14cl
Copyright: MIT
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Source: ftp://ftp.x.org/R5contrib/xfishtank.tar.bz2
Source800: xfishtank-wmconfig.i18n.tgz
Patch: xfishtank-bugs.patch
BuildRoot: /var/tmp/xfishtank-root
Summary(de): verwandelt Ihre X-Root in ein Aquarium 
Summary(fr): transforme votre fond X en aquarium
Summary(tr): X ekranýnýnýzý akvaryuma çevirir

%description
Enjoy an animated aquarium background on your screen, with a variety of
tropical fish swimming in it.

%description -l pt_BR
Divirta-se com um aquário animado no fundo da sua tela, com uma
variedade de peixes tropicais nadando nele.

%description -l es
Diviértate con un acuario animado en el fondo de tu pantalla,
con una variedad de peces tropicales nadando en él.

%description -l de
Ein animiertes Aquarium als Bildschirmhintergrund mit einer Vielzahl
tropischer Fische.

%description -l fr
Profitez d'un aquarium animé comme fond d'écran, avec des poissons
tropicaux qui s'y proménent.

%description -l tr
Bu program X oturumunuzun arkaplanýný, içinde tropikal balýklarýn yüzdüðü
bir akvaryuma çevirecektir.

%prep
%setup -q -n xfishtank
%patch -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xfish <<EOF
#xfish name "xfishtank"
#xfish description "Peixes em seu monitor"
#xfish group Passatempos
#xfish exec "xfishtank &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xfishtank-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xfishtank
%config /etc/X11/wmconfig/xfish

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- wmconfig traduzido

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
