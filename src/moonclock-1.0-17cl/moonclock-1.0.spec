Summary: traditional oclock with moon phase hacks
Summary(pt_BR): Oclock tradicional com modificações para suporte a fases da lua
Summary(es): Oclock tradicional con modificaciones para soporte a fases de la luna
Name: moonclock
Version: 1.0
Release: 17cl
Copyright: MIT
Group: Applications/Graphics
Group(pt_BR): Aplicações/Gráficos
Group(es): Aplicaciones/Gráficos
Source: ftp://ftp.x.org/contrib/applications/moonclock-1.0.tar.gz
Source800: moonclock-wmconfig.i18n.tgz
BuildRoot: /var/tmp/moonclock-root
Summary(de): herkömmliche oclock mit Mondphasen-Hacks
Summary(fr): oclock traditionnelle avec phases lunaires
Summary(tr): Ay evrelerini gösteren saat

%description
Displays the time of day and the current moon phase.  Colors change
depending on time of day (day/night) and the moon is displayed in
a neat little wedge with a star field.

%description -l pt_BR
Mostra a hora do dia e a fase atual da lua. Mudança de cores
dependendo da hora do dia (dia/noite) e a lua é mostrada pequena
e claramente em forma de cunha no espaço.

%description -l es
Enseña la hora del día y la fase actual de la luna. Cambio de
colores dependiendo de la hora del día (día/noche) y la luna se
enseña pequeña y claramente en forma de cuña en el espacio.

%description -l de
Zeigt die Uhrzeit und die aktuelle Mondphase an. Die Farben ändern
sich je nach Tageszeit (Tag/Nacht), und der Mond wird in einem
Sternenhimmel dargestellt.

%description -l fr
Affiche la date du jour et la phase lunaire courante. Les changements
de couleur dépendant de l'heure (jour/nuit) et la lune est affichée
dans un petit coin avec un champ d'étoiles.

%description -l tr
Günün saatini ve ayýn evrelerini gösterir. Renkler o anki saatin gece ya da
gündüz olmasýna göre deðiþir.

%prep
%setup -q

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man
ln -sf oclock $RPM_BUILD_ROOT/usr/X11R6/bin/moonclock
ln -sf oclock.1x $RPM_BUILD_ROOT/usr/X11R6/man/man1/moonclock.1x

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/oclock <<EOF
#oclock name "oclock"
#oclock description "Relógio com fases da Lua"
#oclock group Passatempos
#oclock exec "oclock &"
#EOF

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/



tar xvfpz $RPM_SOURCE_DIR/moonclock-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/oclock
/usr/X11R6/man/man1/oclock.1x
/usr/X11R6/bin/moonclock
/usr/X11R6/man/man1/moonclock.1x
%config /etc/X11/wmconfig/oclock

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmconfig traduzido para pt_BR

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
