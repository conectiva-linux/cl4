Summary: X11 drawing tool
Summary(pt_BR): Ferramenta para desenho X11
Summary(es): Herramienta para diseño X11
Name: xfig
Version: 3.2.2
Release: 5cl
Copyright: Freeware
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: ftp://ftp.x.org/contrib/applications/drawing_tools/xfig/xfig.%{PACKAGE_VERSION}.tar.bz2
Source800: xfig-wmconfig.i18n.tgz
Patch0: xfig-%{PACKAGE_VERSION}-config.patch
Patch1:  xfig.3.2.2-vararg.patch
Requires: transfig >= 3.2.1
Buildroot: /var/tmp/xfig-root
Summary(de): X11-Zeichen-Tool
Summary(fr): Outil de dessin sous X11
Summary(tr): X11 çizim aracý

%description
This program gives you all the features you need to create basic- to
intermediate-level vector graphics, including bezier curves, lines,
rulers, and more. 

%description -l pt_BR
Este programa oferece tudo o que você precisa para criar gráficos
com vetores, incluindo curvas, linhas, réguas, e mais.

%description -l es
Este programa ofrece todo lo que necesitas para crear gráficos con
vectores, incluyendo curvas, líneas, reglas, y más.

%description -l de
Dieses Programm bietet sämtliche Funktionen, die Sie zum Erstellen von
elementaren und fortgeschrittenen Vektorgrafiken benötigen, einschließlich
Bezier-Kurven, Linien, Lineale und anderes.

%description -l fr
Ce programme vous offre tout ce dont vous avez besoin pour créer des graphiques
vectoriels, de base à moyennement complexes. Il comprend les courbes de Bézier,
les lignes, les règles etc.

%description -l tr
Bu program, en temel olanlarýndan ileri düzeydekilere kadar tüm belli baþlý
vektör grafikleri (doðrular, bezier eðrisi vs) çizebilmenize olanak verir.

%prep
%setup -q -n xfig.%{PACKAGE_VERSION}
%patch0 -p1 -b .config
%patch1 -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
make DESTDIR=$RPM_BUILD_ROOT install install.man

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xfig <<EOF
#xfig name "xfig"
#xfig description "Ferramenta de Desenho"
#xfig group Gráficos
#xfig exec "xfig &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xfig-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/*
/usr/X11R6/lib/X11/xfig
/usr/X11R6/man/*/*
%config /usr/X11R6/lib/X11/app-defaults/*
%config /etc/X11/wmconfig/xfig

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Jul  7 1998 Jeff Johnson <jbj@redhat.com>
- updated to 3.2.2.

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- updated for manhattan
- buildroot

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- new version
- messed with config for 5.0
- updated Requires and Copyright
- added wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
