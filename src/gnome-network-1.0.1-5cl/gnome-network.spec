# Note that this is NOT a relocatable package
%define ver      1.0.1
%define rel      5cl
%define prefix   /usr

Summary: GNOME network programs
Summary(pt_BR): Programas de rede do GNOME
Summary(es): Programas de red del GNOME
Name: gnome-network
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
# was .gz
Source0: ftp://ftp.gnome.org/pub/gnome-network-%{ver}.tar.bz2
Source1: gnome-network-pt_BR.po
Patch0: gnome-network-1.0.1-pt_BR.patch
Patch1: gnome-network-1.0.1-desktop.patch
BuildRoot: /tmp/gnome-network-root
Obsoletes: gnome
URL: http://www.gnome.org/

%description
GNOME network programs.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pt_BR
Programas de rede do GNOME

GNOME é o Ambiente de Rede Modelado por Objetos da GNU. É um nome
fantasioso, mas o GNOME é realmente um bom ambiente gráfico. Ele
torna seu computador fácil, poderoso e fácil de configurar.

%description -l es
Programas de red del GNOME GNOME es el Ambiente de Red Modelado
por Objetos de la GNU. Es un nombre fantasioso, pero GNOME es
realmente un buen ambiente gráfico. Hace tu ordenador sencillo,
potente y fácil de configurar.

%changelog
* Thu Jul 01 1999 Rodrigo Stulzer Lopes <rodrigo@conectiva.com>
- new desktop translations to pt_BR

* Fri Jun 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- some fixes (LINGUAS, etc)

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Mon Mar 16 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-network CVS source tree

%prep
%setup -q
%patch0 -p1 -b .pt_BR
%patch1 -p1 -b .desktop

%build

cp $RPM_SOURCE_DIR/gnome-network-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po

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
%{prefix}/share/locale/*/*/*
%{prefix}/share/gnome/apps/*
