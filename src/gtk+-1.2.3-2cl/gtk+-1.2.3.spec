# Note that this is NOT a relocatable package
%define ver      1.2.3
%define rel      2cl
%define prefix   /usr

Summary: The Gimp Toolkit
Summary(pt_BR): Kit de ferramentas Gimp
Summary(es): Conjunto de herramientas Gimp
Name: gtk+
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
# was .gz
Source0: ftp://ftp.gimp.org/pub/gtk/v1.2/gtk+-%{ver}.tar.bz2
Source1: gtk+-pt_BR.po
Patch0: gtk+-1.2.3-pt_BR.patch
BuildRoot: /var/tmp/gtk-%{PACKAGE_VERSION}-root
Obsoletes: gtk
URL: http://www.gtk.org/
Prereq: info
Requires: glib
Docdir: %{prefix}/doc
Serial: 1

%description
The X libraries originally written for the GIMP, which are now used by
several other programs as well.

%description -l pt_BR
Bibliotecas X originalmente escritas para o GIMP, que agora estão
sendo também usadas por vários outros programas.

%description -l es
Bibliotecas X originalmente escritas para GIMP, que ahora se usan
también por varios otros programas.

%package devel
Summary: GIMP Toolkit and GIMP Drawing Kit - Development libraries
Summary(pt_BR): Kit de ferramenta e kit de desenho GIMP
Summary(es): Conjunto de herramienta y conjunto de diseño GIMP
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: gtk+
Obsoletes: gtk-devel
PreReq: info

%description devel
Static libraries and header files for the GIMP's X libraries, which are
available as public libraries.  GLIB includes generally useful data
structures, GDK is a drawing toolkit which provides a thin layer over
Xlib to help automate things like dealing with different color depths,
and GTK is a widget set for creating user interfaces.

%description -l pt_BR devel
Bibliotecas estáticas e arquivos de inclusão do GIMP, que estão
disponíveis como bibliotecas públicas. A GLIB inclui estruturas de
dados úteis; o GDK é um kit de ferramentas que provê uma camada sobre
a Xlib para ajudar a automatizar coisas como o uso de diferentes
profundidades de cor; e GTK é um conjunto de widgets para criar
interfaces de usuário.

%description -l es devel
Bibliotecas estáticas y archivos de inclusión del GIMP, que están
disponibles como bibliotecas públicas. GLIB incluye estructuras de
datos útiles; eGDK es un kit de herramientas que provee una camada
sobre Xlib para ayudar a automatizar cosas como el uso de diferentes
profundidades de color; y GTK es un conjunto de widgets para crear
interfaces de usuario.

%prep
%setup -q
%patch0 -p1 -b .pt_BR

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
[ "$LINGUAS" ] && unset LINGUAS
cp $RPM_SOURCE_DIR/gtk+-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
%ifarch alpha
autoconf
./configure --prefix=%prefix --host=alpha-conectiva-linux
%else
autoconf
./configure --prefix=%prefix
%endif

make

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install

gzip -9n $RPM_BUILD_ROOT%{prefix}/info/*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{prefix}/info/gdk.info.gz %{prefix}/info/dir
/sbin/install-info %{prefix}/info/gtk.info.gz %{prefix}/info/dir

%preun devel
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{prefix}/info/gdk.info.gz %{prefix}/info/dir
    /sbin/install-info --delete %{prefix}/info/gtk.info.gz %{prefix}/info/dir
fi

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{prefix}/lib/libgtk-1.2.so.*
%{prefix}/lib/libgdk-1.2.so.*
%{prefix}/share/themes/Default

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/include/*
%{prefix}/info/*
%{prefix}/man/man1/*
%{prefix}/share/aclocal/*
%{prefix}/bin/*

%changelog
* Wed Jun 16 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added .po translations for pt_BR

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated to gtk+ 1.2.3

* Mon Mar 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed find-requires

* Thu Mar 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated package to version 1.2.1

* Fri Mar 05 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recreated package from gtk+ 1.0.6 spec file
