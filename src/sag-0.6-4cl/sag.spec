Summary: LDP System Administrator's Guide
Summary(pt_BR): Guia do Administrador de Sistemas - do LDP
Summary(es): Guía del Administrador de Sistemas - del LDP
Name: sag
Version: 0.6
Release: 4cl
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
#Source: http://sunsite.unc.edu/LDP/sag-0.6-html.tar.gz
# recompressed with bzip2
Source: http://sunsite.unc.edu/LDP/sag-0.6-html.tar.bz2
Source800: wmconfig.i18n.tgz
Copyright: distributable
Buildroot: /var/tmp/sag-root
BuildArchitectures: noarch
Summary(de): LDP-System-Administrator-Handbuch 
Summary(fr): Guide de l'administrateur système du LDP
Summary(tr): LDP Sistem Yöneticisi Kýlavuzu

%description
This is a generic guide to the System Administration of Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l pt_BR
Este é um guia genérico para Administração de Sistemas Linux. Veja
http://sunsite.unc.edu/LDP para mais informações sobre o Projeto
de Documentação do Linux e possíveis atualizações.

%description -l es
Este es un guía genérico para Administración de Sistemas Linux. Mira
http://sunsite.unc.edu/LDP para más información sobre el Proyecto
de Documentación del Linux y posibles actualizaciones.

%description -l de
Eine allgemeine Führung durch die Systemadministration von Linux-
Systemen. Für weitere Infos zum Linux Dokumentationsprojekt und für 
mögliche Updates zu dieser Version besuchen Sie http://sunsite.unc.edu/LDP.

%description -l fr
Guide générique pour l'administration système sous Linux. Consultez
http://sunsite.unc.edu/LDP pour plus d'informations sur le Projet de
Documentation Linux, et les éventuelles mises à jour de cette version.

%description -l tr
Bu paket, Linux'da sistem yöneticiliðini anlatan rehberi içerir. LDP (Linux
Documentation Project) hakkýnda daha fazla bilgi ve olasý sürüm deðiþiklikleri
için http://sunsite.unc.edu/LDP sayfasýna bakýnýz.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmconfig created using $BROWSER, in pt_BR

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- version 0.6

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- created the package

%prep
%setup -n sag-0.6-html

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/doc/LDP/sag
chmod 755 $RPM_BUILD_ROOT/usr/doc/LDP/sag
cp -ar * $RPM_BUILD_ROOT/usr/doc/LDP/sag
find $RPM_BUILD_ROOT/usr/doc/LDP -type f | xargs chmod 644
find $RPM_BUILD_ROOT/usr/doc/LDP -type d | xargs chmod 755

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/doc/LDP/sag
/etc/X11/wmconfig/sag
