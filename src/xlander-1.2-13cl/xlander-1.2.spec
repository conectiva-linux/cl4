Summary: moon landing simulation
Summary(pt_BR): Simulador de aterrissagem lunar
Summary(es): Simulador de aterrizaje lunar
Name: xlander
Version: 1.2
Release: 13cl
Copyright: MIT
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp.x.org:/R5contrib/xlander.shar.Z
Source800: xlander-wmconfig.i18n.tgz
Patch0: ftp.x.org:/R5contrib/xlander.patch01.Z
Patch1: ftp.x.org:/R5contrib/xlander.patch02.Z
BuildRoot: /var/tmp/xlander-root
Summary(de): Mondlande-Simulation
Summary(fr): Simulation d'allunissage.
Summary(tr): Aya iniþ benzeþim oyunu

%description
A very hard game, but lots of fun nonetheless. Try to manuver the lunar lander to a safe-and-nonviolent landing.

%description -l pt_BR
Um jogo difícil, mas com muita diversão. Tente manobrar sua nave
para uma aterrissagem segura e suave.

%description -l es
Un juego difícil, pero con mucha diversión. Intente maniobrar tu
nave para una poso seguro y suave.

%description -l de
Ein sehr schwieriges Spiel, macht aber trotzdem Spaß. Versuchen Sie das
Mondmodul sicher und unfallfrei zu landen.

%description -l fr
Un jeu très difficile, pas dépourvu d'intéret pour autant. Essayer de réussir un allunissage sans problème
avec votre module lunaire.

%description -l tr
Çok zor ve zevkli bir oyun. Ay aracýný güvenli ve saðlam bir þekilde yere
indirmeniz gerek.

%prep
%setup -q -T -c
uncompress < $RPM_SOURCE_DIR/xlander.shar.Z | sh
uncompress < $RPM_SOURCE_DIR/xlander.patch01.Z | patch
uncompress < $RPM_SOURCE_DIR/xlander.patch02.Z | patch

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xlander <<EOF
#xlander name "xlander"
#xlander description "Aterrissagem Linar"
#xlander group Jogos/Vídeo
#xlander exec "xlander &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xlander-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xlander
/usr/X11R6/man/man1/xlander.1x
%config /etc/X11/wmconfig/xlander

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
