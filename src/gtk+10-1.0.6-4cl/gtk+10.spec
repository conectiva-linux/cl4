# Note that this is NOT a relocatable package
%define ver      1.0.6
%define rel      4cl
%define prefix   /usr

Summary: The GIMP ToolKit (GTK+), a library for creating GUIs for X.
Summary(pt_BR): Kit de ferramentas Gimp
Summary(es): Conjunto de herramientas Gimp
Name: gtk+10
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
# was .gz
Source0: ftp://ftp.gimp.org/pub/gtk/v1.0/gtk+-%{ver}.tar.bz2
Patch0: gtk+-1.0.6-nodocs.patch
BuildRoot: /var/tmp/gtk-%{PACKAGE_VERSION}-root
Obsoletes: gtk

URL: http://www.gtk.org/
Requires: glib10 = %{PACKAGE_VERSION}

%description
The X libraries originally written for the GIMP, which are now used by
several other programs as well.

This RPM is a set of compatibility libraries needed to run applications
linked against the 1.0 series of gtk+ and glib.

%description -l pt_BR
Bibliotecas X originalmente escritas para o GIMP, que agora estão
sendo também usadas por vários outros programas.

%description -l es
Bibliotecas X originalmente escritas para GIMP, que ahora se usan
también por varios otros programas.

%package -n glib10
Summary: A library of handy utility functions.
Summary(pt_BR): Conjunto de funções gráficas utilitárias
Summary(es): Conjunto de funciones gráficas utilitarias
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas

%description -n glib10
The glib package contains a useful library of utility functions, which
are necessary for the successful operation of many different programs on
your Conectiva Linux system.

%description -l pt_BR -n glib10
Conjunto de funções utilitárias. Bibliotecas de desenvolvimento e
arquivos de inclusão estão em gtk+-devel.

%description -l es -n glib10
Conjunto de funciones utilitarias. Bibliotecas de desarrollo y
archivos de inclusión están en gtk+-devel.

%prep
%setup -q -n gtk+-%{PACKAGE_VERSION}
%patch0 -p1 -b .nodocs

%build
SHM=""
%ifarch alpha
SHM="--disable-shm"
%endif
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
autoconf
./configure --prefix=%prefix --with-xinput=xfree \
	$SHM $RPM_ARCH-conectiva-linux

make

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n glib10 -p /sbin/ldconfig

%postun -n glib10 -p /sbin/ldconfig


%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{prefix}/lib/libgtk.so.*
%{prefix}/lib/libgdk.so.*

%files -n glib10
%defattr(-, root, root)
%{prefix}/lib/libglib.so.*

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Do not try to build docs anymore (We won't be using them anyways)

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 05 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- First version of package
