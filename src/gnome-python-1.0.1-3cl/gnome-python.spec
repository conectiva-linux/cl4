%define py_prefix   /usr
%define py_ver      1.5
%define pygtk_ver   0.5.12
%define pygnome_ver 1.0.1

Summary: pygtk and pygnome
Summary(pt_BR): pygtk & pygnome
Summary(es): pygtk y pygnome
Name: gnome-python
Version: %{pygnome_ver}
Release: 3cl
Source: gnome-python-%{pygnome_ver}.tar.bz2
Copyright: LGPL
Group: Applications/Libraries
Group(pt_BR): Aplicações/Bibliotecas
Group(es): Aplicaciones/Bibliotecas
BuildRoot: /var/tmp/gnome-python-root

%description
Source package for python bindings for GTK+ and GNOME.  The binary packages
give better descriptions of what they do.

%description -l pt_BR
Suporte a desenvolvimento de aplicações GTK+ e GNOME usando a linguagem
python.

%description -l es
pygtk y pygnome

%package -n pygtk
Version: %{pygtk_ver}
Summary: Python bindings for the GTK+ widget set
Summary(pt_BR): Suporte a desenvolvimento de aplicações GTK+ usando a linguagem python.
Summary(es): Soporte para desarrollo de aplicaciones que usen el GTK+ con python
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: glib, gtk+, imlib, python

%description -n pygtk
PyGTK is an extension module for python that gives you access to the GTK+
widget set.  Just about anything you can write in C with GTK+ you can write
in python with PyGTK (within reason), but with all of python's benefits.

%description -l pt_BR -n pygtk
PyGTK é uma extensão para o python que lhe permite acessar o conjunto de
componentes GTK+. Quase tudo o que pode ser escrito em C com o GTK+ pode
ser escrito em python usando o PyGTK (dentro do possível), mas com todos
os benefícios da linguagem python.

%description -l es -n pygtk
Soporte para desarrollo de aplicaciones que usen el GTK+ con python

%package -n pygnome
Version: %{pygnome_ver}
Summary: Python bindings for the GNOME libraries
Summary(pt_BR): Suporte a desenvolvimento de aplicações GNOME usando a linguagem python
Summary(es): Soporte para desarrollo de aplicaciones que usen el GNOME con python
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: pygtk = %{pygtk_ver}
Requires: gnome-libs >= 1.0.1

%description -n pygnome
PyGNOME is an extension module for python that gives you access to the
base GNOME libraries.  This means you have access to more widgets, simple
configuration interface, metadata support and many other features.

%description -l pt_BR -n pygnome
PyGNOME é uma extensão para o python que lhe permite acessar as bibliotecas
do GNOME. Isto significa que você terá acesso a mais componentes, uma
interface de configuração mais simples, suporte a metadados e muitas outras
coisas.

%description -l es -n pygnome
Soporte para desarrollo de aplicaciones que usen el GNOME con python

%prep
%setup -q

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
./configure

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files -n pygtk
%{py_prefix}/lib/python%{py_ver}/site-packages/gtk.py*
%{py_prefix}/lib/python%{py_ver}/site-packages/Gtkinter.py*
%{py_prefix}/lib/python%{py_ver}/site-packages/GtkExtra.py*
%{py_prefix}/lib/python%{py_ver}/site-packages/GTK.py*
%{py_prefix}/lib/python%{py_ver}/site-packages/GDK.py*
%{py_prefix}/lib/python%{py_ver}/site-packages/GdkImlib.py*
%{py_prefix}/lib/python%{py_ver}/site-packages/pyglade/*.py*

%{py_prefix}/lib/python%{py_ver}/site-packages/_gtkmodule.so
%{py_prefix}/lib/python%{py_ver}/site-packages/_gdkimlibmodule.so

%doc pygtk/AUTHORS pygtk/NEWS pygtk/README pygtk/MAPPING pygtk/ChangeLog
%doc pygtk/description.py pygtk/examples

%files -n pygnome
%{py_prefix}/lib/python%{py_ver}/site-packages/gettext.py*
%{py_prefix}/lib/python%{py_ver}/site-packages/gnome/*.py*

%{py_prefix}/lib/python%{py_ver}/site-packages/_gnomemodule.so
%{py_prefix}/lib/python%{py_ver}/site-packages/_gnomeuimodule.so
%{py_prefix}/lib/python%{py_ver}/site-packages/_zvtmodule.so
%{py_prefix}/lib/python%{py_ver}/site-packages/_gtkxmhtmlmodule.so

%doc AUTHORS NEWS README ChangeLog
%doc pygnome/examples

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 30 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.0.1

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file
