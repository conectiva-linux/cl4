%define name wmakerconf
%define prefixpath /usr/X11R6
%define ver     2.1
%define release 1cl

Name: %{name}
Version: %{ver}
Release: %{release}
Summary: This is a GTK-based configuration tool for Window Maker
Summary(pt_BR): Ferramenta de configuração baseada no GTK para o WindowMaker
Summary(es): Herramienta de configuración basada en GTK para WindowMaker
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL
Source: ftp://sunshine.informatik.uni-wuerzburg.de/pub/wmaker/%{name}-%{ver}.tar.bz2
Source800: wmakerconf-wmconfig.i18n.tgz
Icon: wmakerconf.xpm
Requires: libPropList, perl, gzip, lynx
BuildRoot: /var/tmp/%{name}-%{version}_root

%description
wmakerconf is a GTK+ based configuration tool for the window manager
Window Maker.

Support of all Window Maker attributes: Font selection browser, pixmap
preview browser, color selection dialog, shortcut dialog, file selection
dialog, ... 

Tooltips with short description of every attribute. 

New attributes can be simply integrated by changing the wmakerconf proplist

%description -l pt_BR
Ferramenta de configuração baseada em GTK+ para o gerenciador de janelas
Window Maker.

Suporta todos os atributos do Window Maker: navegador para seleção de fontes,
navegador para visualização de pixmaps, caixa de diálogo para seleção de
cores, caixa de diálogo para atalhos, caixa de diálogo para seleção de
arquivos, ...

Dicas em todos os atributos.

Novos atributos podem ser integrados de forma simples, mudando a lista de
propriedades do wmakerconf.

%description -l es
Herramienta de configuración basada en GTK+ para el administrador
de ventanas Window Maker.  Soporta todos los atributos del Window
Maker: navegador para selección de fuentes, navegador para visualizar
pixmaps, caja de diálogo para selección de colores, caja de diálogo
para accesos directos, caja de diálogo para selección de archivos,...
Trucos en todos los atributos. Nuevos atributos se pueden integrar
de forma sencilla, cambiando la lista de propiedades del wmakerconf.

%prep
%setup -q 

%build
unset LINGUAS
CFLAGS="$RPM_OPT_FLAGS" ./configure \
    --prefix=%{prefixpath} \
	--with-wmakerprefix=%{prefixpath}
make

%install
rm -rf $RPM_BUILD_ROOT
make install-strip prefix=$RPM_BUILD_ROOT%{prefixpath}

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

mkdir -p $RPM_BUILD_ROOT/usr/X11R6/share/WindowMaker/Pixmaps
cp $RPM_SOURCE_DIR/wmakerconf.xpm $RPM_BUILD_ROOT/usr/X11R6/share/WindowMaker/Pixmaps

mv data/README data/README.data




tar xvfpz $RPM_SOURCE_DIR/wmakerconf-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{ver}

%files
%defattr(-,root,root)

%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL MANUAL NEWS NLS-TEAM1 README TODO data/NLS-TEAM2
%{prefixpath}/bin/*
%{prefixpath}/share/wmakerconf
%{prefixpath}/share/locale/*/LC_MESSAGES/*
%{prefixpath}/share/WindowMaker/Pixmaps/wmakerconf.xpm
%config(missingok) /etc/X11/wmconfig/wmakerconf

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue May 11 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 2.1

* Thu Apr 29 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 2.0

* Wed Apr 14 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 1.99.1

* Tue Apr 13 1999 Conectiva <dist@conectiva.com>
- Unset LINGUAS in spec file

* Sat Apr 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Upgraded to 1.99.0

* Wed Mar 31 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added icon in wmaker path
- moved file data/README to data/README.data

* Sat Mar 27 1999 Conectiva <dist@conectiva.com>
- rebuild against new gtk

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 19 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added pt_BR translations
- Removed libPropList from package, link dinamically ?

* Sun Mar 14 1999 Ullrich Hafner <hafner@bigfoot.de>
- upgraded to wmakerconf 1.8
- removed data package
- new NLS structure

* Fri Feb 12 1999 Ullrich Hafner <hafner@bigfoot.de>
- upgraded to wmakerconf 1.7

* Wed Jan 20 1999 Ullrich Hafner <hafner@bigfoot.de>
- upgraded to wmakerconf 1.6

* Tue Dec 22 1998 Ullrich Hafner <hafner@bigfoot.de>
- upgraded to wmakerconf 1.5
- added prefix

* Thu Nov 19 1998 Ullrich Hafner <hafner@bigfoot.de>
- upgraded to wmakerconf 1.3
- updated data files for windowmaker 0.20.2 and above
- split into wmakerconf and wmakerconf-data package

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- updated data files for windowmaker 0.20 and above

* Fri Sep 18 1998 Cristian Gafton <gafton@redhat.com>
- packaged for 5.2 to be used with WindowMaker
