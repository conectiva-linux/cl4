Summary: graphics file browser utility
Summary(pt_BR): Utilitário para navegação em arquivos gráficos
Summary(es): Aplicación para navegación en archivos gráficos
Name: gqview
Version: 0.6.0
Release: 5cl
Copyright: GPL
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
# was .tgz
Source0: http://www.geocities.com/SiliconValley/Haven/5235/gqview-0.6.0.src.tar.bz2
Patch0: gqview-gnome-menu.patch
BuildRoot: /tmp/%{name}-%{version}-root
URL: http://www.geocities.com/SiliconValley/Haven/5235/index.html

%description
GQview is a browser for graphics files.
Offering single click viewing of your graphics files.
Includes thumbnail view, zoom and filtering features.
And external editor support.

%description -l pt_BR
Utilitário para navegação em arquivos gráficos.
Inclui visualização de diretório com pequenas imagens (thumbnails),
ampliação e filtros.

%description -l es
Aplicación para navegación en archivos gráficos

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome-menu entries for gqview

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 24 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- redid most of the spec file

* Wed Oct 7 1998 John Ellis <gqview@geocities.com>
- updated for version 0.4.2

* Fri Sep 11 1998 John Ellis <gqview@geocities.com>
- updated for version 0.4.1

* Sat Aug 15 1998 John Ellis <gqview@geocities.com>
- updated for version 0.4.0

* Wed Aug 5 1998 Joel Young <jyoung@erols.com>
- enhanced rpm .spec file

%prep
%setup
%patch0 -p1 -b .gnome-menu

%build
make PREFIX=/usr

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
mkdir -p $RPM_BUILD_ROOT/usr/share/gnome/apps/Graphics

cp gqview $RPM_BUILD_ROOT/usr/bin/gqview
cp gqview.png $RPM_BUILD_ROOT/usr/share/pixmaps
cp gqview.desktop $RPM_BUILD_ROOT/usr/share/gnome/apps/Graphics

%files
%defattr(-,root,root)
%doc README COPYING TODO
/usr/bin/gqview
/usr/share/pixmaps/gqview.png
/usr/share/gnome/apps/Graphics/gqview.desktop
