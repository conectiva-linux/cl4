Summary: LDP Programmer's Guide
Summary(pt_BR): LDP Guia do Programador
Summary(es): LDP Guía del Programador
Name: lpg
Version: 0.4
Release: 5cl
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Source: http://sunsite.unc.edu/LDP/lpg-0.4.html.tar.gz
Source800: wmconfig.i18n.tgz
Copyright: distributable
Buildroot: /var/tmp/lpg
BuildArchitectures: noarch
Summary(de): LDP-Programmerierhandbuch
Summary(fr): Le guide du programmeur LDP.
Summary(tr): LDP Programcý kýlavuzu

%description
This is a generic guide to the Programming on Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l pt_BR
Este é um guia genérico de programação em sistemas Linux. Verifique
http://sunsite.unc.edu/LDP para mais informações sobre o Projeto
de Documentação do Linux, e possivelmente atualizar esta versão.

%description -l es
Este es un guía genérico de programación en sistemas Linux. Verifica
http://sunsite.unc.edu/LDP para más información sobre el Proyecto
de Documentación del Linux, y posiblemente actualizar esta versión.

%description -l de
Dies ist eine allgemeine Einführung in die Programmierung auf 
Linux-Systemen. Unter der Adresse http://sunsite.unc.edu/LDP finden 
Sie weitere Infos zum Linux-Dokumentationsprojekt und eventuelle 
Updates zu dieser Version. 

%description -l fr
Ceci est un guide générique à la programmation sur les systèmes Linux.
Allez sur http://sunsite.unc.edu/LDP pour plus d'informations sur le
Projet de Documentation Linux (LDP) et les mises à jour éventuelles
de cette version.

%description -l tr
Linux sistemleri için programlama kýlavuzu. Linux Belgeleme Projesi (Linux
Documentation Project) ile ilgili daha fazla bilgi ve yeni sürümler için
http://sunsite.unc.edu/LDP adresine bakýn.

%changelog
* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmconfig created using $BROWSER, in pt_BR

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr


* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>

- created the package

%prep
%setup -n lpg

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/doc/LDP/lpg
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
chmod 755 $RPM_BUILD_ROOT/usr/doc/LDP/lpg
cp -ar * $RPM_BUILD_ROOT/usr/doc/LDP/lpg
find $RPM_BUILD_ROOT/usr/doc/LDP -type f | xargs chmod 644
find $RPM_BUILD_ROOT/usr/doc/LDP -type d | xargs chmod 755

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/doc/LDP/lpg
/etc/X11/wmconfig/lpg
