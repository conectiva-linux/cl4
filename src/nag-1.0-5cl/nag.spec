Summary: LDP Network Administrator's Guide
Summary(pt_BR): LDP Guia do Administrador de Rede
Summary(es): LDP Gu�a del Administrador de Red
Name: nag
Version: 1.0
Release: 5cl
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
# was .gz
Source: http://sunsite.unc.edu/LDP/nag.html.tar.bz2
Source800: wmconfig.i18n.tgz
Copyright: distributable
Buildroot: /var/tmp/nag
BuildArchitectures: noarch
Summary(de): LDP-Netzwerk-Administrator-Handbuch 
Summary(fr): Guide de l'administrateur r�seau du LDP
Summary(tr): LDP - NAG, A� y�neticisinin el kitab�

%description
This is a generic guide to the Network Administration of Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l pt_BR
Este � um guia gen�rico para Administra��o de Redes em sistemas
Linux. Veja http://sunsite.unc.edu/LDP para mais informa��es sobre
o Projeto de Documenta��o do Linux, e poss�veis atualiza��es.

%description -l es
Este es un gu�a gen�rico para Administraci�n de Redes en sistemas
Linux. Mira http://sunsite.unc.edu/LDP para m�s informaci�n sobre
el Proyecto de Documentaci�n del Linux, y posibles actualizaciones.

%description -l de
Dies ist eine allgemeine Anleitung zur Netzwerkverwaltung von Linux-Systemen.
Unter http://sunsite.unc.edu/LDP finden Sie weitere Informationen �ber das 
Linux Documentation Project und ggf. Updates zu dieser Version.

%description -l fr
Guide g�n�rique � l'administration r�seau sous Linux. 
Allez sur http://sunsite.unc.edu/LDP pour plus d'informations sur le
Projet de Documentation Linux (LDP) et les mises � jour �ventuelles
de cette version.

%description -l tr
Bu kitap, LDP (Linux belgeleme �al��mas�) sonucunda ortaya ��kan eserlerden
biri. Serinin di�er kitaplar� ile birlikte bu kitaplar�n g�ncel bir yans�s�na
http://www.linux.org.tr/LDP alt�ndan eri�ebilirsiniz. A� y�neticisinin el
kitab� Linux'da a� hizmetlerinin y�netimi �zerine genel bilgileri i�erir.

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
