Summary: flash plugin for netscape
Summary(pt_BR): Plugin flash para o Netscape/Mozilla
Summary(es): Plugin flash para el Netscape/Mozilla
Name: flash
Version: 0.4.3
Release: 2cl
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
# was .gz
Source: http://www.geocities.com/TimesSquare/Labyrinth/5084/flash/Linux/flash-%{version}.tar.bz2
Source1: swplayer.wmconfig
URL: http://www.geocities.com/TimesSquare/Labyrinth/5084/flash.html
Provides: npflash.so
Buildroot: /tmp/flash

%description
The Flash Plugin is a Netscape plugin that allows to view Flash
files. Many commercial sites use this format to make their site
up. The Flash object also allows to navigate through a site,
therefore, without the right plugin it was impossible to go further
the "Get Shockwave" logo while running Netscape under Linux.
Since Macromedia has made the Flash file format "open", I decided
to write the plugin for Linux.

%description -l pt_BR
Este é um "plugin" para o Netscape/Mozilla que permite a visualização
de arquivos Flash.  Muitos lugares na Internet usam este formato para
construir suas páginas. Os objetos Flash também permitem a navegação
em uma grupo de páginas, desta forma a navegação era impossibilitada
sem o "plugin" correto, assim não se passava da tela "Get Shockwave"
enquanto navegando no Linux.  Como a Macromedia tornou abertas
as especificações do formato Flash, eu decidi escrever o "plugin"
para o Linux.

%description -l es
Este es un "plugin" para el Netscape/Mozilla que permite visualizar
archivos Flash.  Muchos lugares en la Internet usan este formato
para construir sus páginas. Los objetos Flash también permiten
navegar en un grupo de páginas, pero anteriormente la navegación se
veía imposibilitaba sin el "plugin" correcto, y así, no se podía
pasar de la pantalla "Get Shockwave" mientras se utilizaba Linux.
Como la Macromedia abrió las especificaciones del formato Flash,
he decidido escribir el "plugin" para Linux.

%prep
%setup

%build
make all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/netscape/plugins
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

install -m 755 -o 0 -g 0 -s Plugin/npflash.so $RPM_BUILD_ROOT/usr/lib/netscape/plugins/npflash.so
install -m 755 -o 0 -g 0 -s Player/swfplayer $RPM_BUILD_ROOT/usr/X11R6/bin/swfplayer
install -m 644 -o 0 -g 0 -s $RPM_SOURCE_DIR/swplayer.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/swfplayer

%clean
rm -rf $RPM_BUILD_ROOT

%files
/etc/X11/wmconfig/swfplayer
/usr/lib/netscape/plugins/npflash.so
/usr/X11R6/bin/swfplayer
%doc README COPYING

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun 09 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 0.4.1 to 0.4.3
- wmconfig

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 30 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- atualizado para a versão 0.4.1

* Thu Nov 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Nov 26 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- incluido no guarani

