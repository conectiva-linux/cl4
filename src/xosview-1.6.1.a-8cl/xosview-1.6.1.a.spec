Summary: X11 util for viewing system resources
Summary(pt_BR): Utilitário X11 para visualizar os recursos do sistema
Summary(es): Utilitario X11 para visualizar los recursos del sistema
Name: xosview
%define version 1.6.1.a
Version: %{version}
Release: 8cl
Exclusiveos: Linux
Exclusivearch: i386 sparc alpha
#
# Source: http://lore.ece.utexas.edu/~bgrayson/xosview/xosview-%{version}.tar.gz
Source: ftp://sunsite.unc.edu/pub/Linux/utils/status/xosview-%{version}.tar.gz
Source800: xosview-wmconfig.i18n.tgz
Patch0: xosview-1.6.1.a-sparc.patch
Copyright: distributable GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Buildroot: /var/tmp/xosview-root
Summary(de): X11-Util zur Anzeige von Systemressourcen
Summary(fr): Utilitaire X11 pour visualiser les ressources système
Summary(tr): Sistem kaynaklarýný denetleyen X11 yardýmcý programý

%description
xosview provides a convenient bar graph of the current system state -
memory usage, CPU load, and network usage. Very useful for monitoring status.

%description -l pt_BR
O xosview oferece um conveniente gráfico de barras do estado atual
do sistema - uso de memória, carga da CPU e uso de rede. Muito útil
para monitoração do status do seu sistema.

%description -l es
xosview nos ofrece un conveniente gráfico de barras del estado
actual del sistema - uso de memoria, carga de la CPU y uso de
red. Muy útil para monitoración del estado de tu sistema.

%description -l de
xosview stellt den aktuellen Systemzustand mit Balkengrafiken dar -
Speichernutzung, CPU- und Netzwerkauslastung. Sehr nützlich.

%description -l fr

xosview offre un histogramme représentant l'état courant du système -
l'utilisation mémoire, la charge CPU et l'utilisation du réseau. Très
utile pour surveiller ces états.

%description -l tr
xosview sistemin o anki durumunu (iþlemci yükü, bellek ve að kullanýmý)
küçük bir pencerede grafik ortamda sunar.

%prep
%setup -q
%ifarch sparc alpha
%patch0 -p1 -b .sparc
%endif

# --- XXX Cruft Alert!
rm linux/*.o

%build
%ifarch alpha
./configure --prefix=/usr --disable-linux-memstat alpha-conectiva-linux-gnu
%else
./configure --prefix=/usr
%endif
make all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1,lib/X11/app-defaults}
make PREFIX=$RPM_BUILD_ROOT/usr/X11R6 install
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xosview <<EOF
#xosview name "Estatísticas do SO"
#xosview description "Visualizador das Estatísticas do SO"
#xosview group Administração
#xosview exec "xosview &"
#EOF

chmod u-s $RPM_BUILD_ROOT/usr/X11R6/bin/*



tar xvfpz $RPM_SOURCE_DIR/xosview-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
/usr/X11R6/bin/*
/usr/X11R6/man/man1/*
%config /usr/X11R6/lib/X11/app-defaults/*
%config /etc/X11/wmconfig/*

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Jun 16 1998 Jeff Johnson <jbj@redhat.com>
- add sparc/alpha functionality.
- add %clean

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Mon Jun 01 1998 Erik Troan <ewt@redhat.com>
- how the hell did this get setuid root?

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5.1 (so that it compiles with egcs)
- buildroot

* Tue Nov  4 1997 Erik Troan <ewt@redhat.com>
- commented out line causing core dumps when exiting

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
