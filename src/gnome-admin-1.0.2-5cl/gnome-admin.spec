# Note that this is NOT a relocatable package
%define ver      1.0.2
%define rel      5cl
%define prefix   /usr

Summary: GNOME sysadmin programs
Summary(pt_BR): Programas de administração do sistema para GNOME.
Summary(es): Programas de gestión de sistema para GNOME.
Name: gnome-admin
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
# was .gz
Source0: ftp://ftp.gnome.org/pub/gnome-admin-%{ver}.tar.bz2
Source1: gnome-admin-pt_BR.po
Patch0: gnome-admin-1.0.2-pt_BR.patch
Patch1: gnome-admin-1.0.2.diff
BuildRoot: /tmp/gnome-admin-root
Obsoletes: gnome
URL: http://www.gnome.org/

%description
GNOME system administration programs.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pt_BR
Programas de administração do sistema para GNOME.

GNOME é o Ambiente de Rede Modelado por Objetos da GNU. É um nome
fantasioso, mas o GNOME é realmente um bom ambiente gráfico. Ele
torna seu computador fácil, poderoso e fácil de configurar.

%description -l es
Programas de administración del sistema para GNOME.  GNOME es
el Ambiente de Red Modelado por Objetos de la GNU. Es un nombre
fantasioso, pero GNOME es realmente un bueno ambiente gráfico. Hace
tu ordenador sencillo, potente y fácil de configurar.

%changelog
* Thu Jul 01 1999 Rodrigo Stulzer Lopes <rodrigo@conectiva.com>
- Updated gnome-menu entries for gnome-admin

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added pt_BR.po to package
- unset LINGUAS

* Tue Mar 30 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.0.2

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Mon Mar 16 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-admin CVS source tree

%prep
%setup -q
%patch0 -p1 -b .pt_BR
%patch1 -p1 -b .gnome-menu

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-execptions"
[ "$LINGUAS" ] && unset LINGUAS
cp $RPM_SOURCE_DIR/gnome-admin-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
if [ ! -f configure ]; then
%ifarch alpha
./autogen.sh --host=alpha-conectiva-linux --prefix=%prefix --sysconfdir="/etc"
%else
./autogen.sh --prefix=%prefix --sysconfdir="/etc"
%endif
else
%ifarch alpha
autoconf
./configure --host=alpha-conectiva-linux --prefix=%prefix --sysconfdir="/etc"
%else
autoconf
./configure --prefix=%prefix --sysconfdir="/etc"
%endif
fi

make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin
%{prefix}/share/locale
%{prefix}/share/gnome/apps
%{prefix}/share/pixmaps
%{prefix}/share/logview
