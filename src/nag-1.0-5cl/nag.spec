Summary: LDP Network Administrator's Guide
Summary(pt_BR): LDP Guia do Administrador de Rede
Summary(es): LDP Guía del Administrador de Red
Name: nag
Version: 1.0
Release: 5cl
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
# was .gz
Source: http://sunsite.unc.edu/LDP/nag.html.tar.bz2
Source800: wmconfig.i18n.tgz
Copyright: distributable
Buildroot: /var/tmp/nag
BuildArchitectures: noarch
Summary(de): LDP-Netzwerk-Administrator-Handbuch 
Summary(fr): Guide de l'administrateur réseau du LDP
Summary(tr): LDP - NAG, Að yöneticisinin el kitabý

%description
This is a generic guide to the Network Administration of Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l pt_BR
Este é um guia genérico para Administração de Redes em sistemas
Linux. Veja http://sunsite.unc.edu/LDP para mais informações sobre
o Projeto de Documentação do Linux, e possíveis atualizações.

%description -l es
Este es un guía genérico para Administración de Redes en sistemas
Linux. Mira http://sunsite.unc.edu/LDP para más información sobre
el Proyecto de Documentación del Linux, y posibles actualizaciones.

%description -l de
Dies ist eine allgemeine Anleitung zur Netzwerkverwaltung von Linux-Systemen.
Unter http://sunsite.unc.edu/LDP finden Sie weitere Informationen über das 
Linux Documentation Project und ggf. Updates zu dieser Version.

%description -l fr
Guide générique à l'administration réseau sous Linux. 
Allez sur http://sunsite.unc.edu/LDP pour plus d'informations sur le
Projet de Documentation Linux (LDP) et les mises à jour éventuelles
de cette version.

%description -l tr
Bu kitap, LDP (Linux belgeleme çalýþmasý) sonucunda ortaya çýkan eserlerden
biri. Serinin diðer kitaplarý ile birlikte bu kitaplarýn güncel bir yansýsýna
http://www.linux.org.tr/LDP altýndan eriþebilirsiniz. Að yöneticisinin el
kitabý Linux'da að hizmetlerinin yönetimi üzerine genel bilgileri içerir.

%changelog
* Thu Jun 24 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- added pt_BR wmconfig using $BROWSER

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr


* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>

- created the package

%prep
%setup -n nag

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/doc/LDP/nag
chmod 755 $RPM_BUILD_ROOT/usr/doc/LDP/nag
cp -ar * $RPM_BUILD_ROOT/usr/doc/LDP/nag
find $RPM_BUILD_ROOT/usr/doc/LDP -type f | xargs chmod 644
find $RPM_BUILD_ROOT/usr/doc/LDP -type d | xargs chmod 755

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/doc/LDP/nag
/etc/X11/wmconfig/nag
