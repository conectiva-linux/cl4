# Note that this is NOT a relocatable package
%define ver      1.0.1
%define rel      5cl
%define prefix   /usr

Summary: GNOME System Monitor
Summary(pt_BR): Monitor do Sistema do GNOME
Summary(es): Monitor del Sistema del GNOME
Name: gtop
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
# was .gz
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/gtop/gtop-%{ver}.tar.bz2
Source1: gtop-pt_BR.po
Patch0: gtop-1.0.1-pt_BR.patch
Patch1: gtop-gnome-menu.patch
BuildRoot: /tmp/gtop-root
Obsoletes: gnome
URL: http://www.gnome.org/

%description
GNOME System Monitor.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pt_BR
Monitor do Sistema do GNOME

%description -l es
Monitor del Sistema del GNOME

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome-menu entries for gtop

* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 24 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 24 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Sun Aug 23 1998 Martin Baulig <martin@home-of-linux.org>
- Make GTop its own top-level module.

%prep
%setup -q
%patch0 -p1 -b .pt_BR
%patch1 -p1 -b .gnome-menu

%build

cp $RPM_SOURCE_DIR/gtop-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS
if [ ! -f configure ]; then
%ifarch alpha
  ./autogen.sh --host=alpha-conectiva-linux --prefix=%prefix 
%else
  ./autogen.sh --prefix=%prefix 
%endif
else
%ifarch alpha
autoconf
./configure --host=alpha-conectiva-linux --prefix=%prefix
%else
autoconf
./configure --prefix=%prefix 
%endif
fi

make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/share/*
