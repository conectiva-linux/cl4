%define  ver     0.5
%define  rel     3cl
%define  prefix  /usr

Summary: Default GTK+ theme engines
Summary(pt_BR): Temas default para o GTK+
Summary(es): Motores por defecto de temas GTK+
Name: gtk-engines
Version: %ver
Release: %rel
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
# was .gz
Source: gtk-engines-%{PACKAGE_VERSION}.tar.bz2
Url: http://gtk.themes.org/
BuildRoot:/var/tmp/gtk-engines-%{PACKAGE_VERSION}-root

%description
These are the graphical engines for the various GTK+ toolkit themes.
Included themes are:

  - Notif
  - redmond95
  - Pixmap
  - Metal (Java swing-like)

%description -l pt_BR
Estas são máquinas gráficas para os vários temas do conjunto de ferramentas
GTK+.

Os temas incluídos são:

  - Notif
  - redmond95
  - Pixmap
  - Metal (parecido com o swing do Java)

%description -l es
Motores por defecto de temas GTK+:

  - Notif
  - redmond95
  - Pixmap
  - Metal (Java swing-like)

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rttti -fno-exceptions"
./configure --prefix=%prefix

make

%install
make exec_prefix=$RPM_BUILD_ROOT/%{prefix} prefix=$RPM_BUILD_ROOT/%{prefix} install 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING README ChangeLog
%{prefix}/lib/gtk/themes/engines/*
%{prefix}/share/themes/Pixmap/*
%{prefix}/share/themes/Metal/*
%{prefix}/share/themes/Notif/*
%{prefix}/share/themes/Redmond95/*

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 05 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- First version of package
