# Note that this is NOT a relocatable package
%define ver      0.5.1
%define rel      3cl
%define prefix   /usr

Summary: gEdit is a small but powerful text editor for GNOME.
Summary(pt_BR): O gedit é um pequeno mas poderoso editor de textos para o GNOME.
Summary(es): El gedit es un pequeño pero poderoso editor de textos para el GNOME
Name:      gedit
Version:   %ver
Release:   %rel
Copyright: GPL
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
# was .gz
Source0:   gedit-%{PACKAGE_VERSION}.tar.bz2
URL:       http://gedit.pn.org/
BuildRoot: /var/tmp/gedit-%{PACKAGE_VERSION}-root

%description
gEdit is a small but powerful text editor designed expressly
for GNOME.

It includes such features as split-screen mode, a plugin
API, which allows gEdit to be extended to support many
features while remaining small at its core, multiple
document editing through the use of a 'tabbed' notebook and
many more functions.

GNOME is required to use gEdit (Gnome-Libs and Gtk+).

%description -l pt_BR
O gedit é um pequeno mas poderoso editor de textos projetado
especialmente para o GNOME.

Inclui características como modo de divisão de tela, uma API
para componentes extras que permite que o gedit receba extensões
para mais características enquanto permanece com um núcleo pequeno,
edição de vários documentos através de várias janelas e muitas
outras funções.

%description -l es
El gedit es un pequeño pero poderoso editor de textos para el GNOME

%package devel
Summary: Develop plugins for the gEdit editor.
Summary(pt_BR): Este pacote permite o desenvolvimento de componentes para o editor gedit.
Summary(es): Permite desarrollar componentes para el editor gedit.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
gEdit is a small but powerful text editor for GTK+ and/or GNOME.
This package allows you to develop plugins that work within
gEdit.  Plugins can create new documents and manipulate documents
in arbitrary ways.

%description -l pt_BR devel
Este pacote permite o desenvolvimento de componentes para o editor gedit.

%description -l es devel
Permite desarrollar componentes para el editor gedit.

%prep
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS

%ifarch alpha
  ./configure --host=alpha-conectiva-linux --prefix=%{prefix} 
%else
  ./configure --prefix=%{prefix} 
%endif

make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc README COPYING ChangeLog NEWS TODO AUTHORS INSTALL THANKS
%{prefix}/bin/gedit
%{prefix}/share/locale/*/*/*
%{prefix}/share/gnome/apps/*/*
%{prefix}/share/pixmaps/*
%{prefix}/share/mime-info/*
%{prefix}/share/geditrc
%{prefix}/man/*/*
%{prefix}/libexec/*/*/*

%files devel
%defattr(-, root, root)
%{prefix}/include/*/*
%{prefix}/lib/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 24 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- fixed LANG & /usr/share/locale

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Sat Feb 06 1999 Michael Johnson <johnsonm@redhat.com>
- Cleaned up a bit for Red Hat use

* Thu Oct 22 1998 Alex Roberts <bse@dial.pipex.com>
- First try at an RPM
