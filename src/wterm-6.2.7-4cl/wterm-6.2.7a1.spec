%define version 6.2.7
%define release 4cl
%define name wterm

Summary: A rxvt terminal with transparency and shade options
Summary(pt_BR): Terminal rxvt com opções de transparência.
Summary(es): Terminal rxvt con opciones de transparencia
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source: %{name}-%{version}a1.tar.bz2
Source800: wterm-wmconfig.i18n.tgz
BuildRoot: /var/tmp/%{name}-%{version}_root

%description
wterm is a VT100 terminal emulator for X. It's objective is to be
fast as rxvt and configurable as Eterm.

%description -l pt_BR
Wterm é um emulador de terminal VT100 para X. Seu objetivo é
ser rápido como o rxvt e configurável como o Eterm.

%description -l es
Wterm actúa como un emulador de terminal padrón VT100.
Intenta ser rápido como el rxvt y configurable así como
el Eterm.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --with-x --with-xpm --enable-next-scroll --enable-utmp --enable-xpm-background --enable-transparency --x-includes=/usr/X11R6/include/X11 --prefix=$RPM_BUILD_ROOT/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
make install

mv $RPM_BUILD_DIR/%{name}-%{version}/doc/menu/menu $RPM_BUILD_DIR/%{name}-%{version}/doc/menu/menu.wterm
mkdir -p $RPM_BUILD_ROOT/usr/share/icons
install -m 644 wterm.tiff $RPM_BUILD_ROOT/usr/share/icons
install -m 644 wtermthai.tiff $RPM_BUILD_ROOT/usr/share/icons
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig


# files section

cd $RPM_BUILD_ROOT
rm -f $RPM_BUILD_DIR/file.list.%{name}
echo "%defattr(-,root,root)" >> $RPM_BUILD_DIR/file.list.%{name}

find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
cd $RPM_BUILD_DIR/%{name}-%{version}
echo "%doc README INSTALL wterm-6.2.6.lsm doc" >> $RPM_BUILD_DIR/file.list.%{name}

# end of files section

tar xvfpz $RPM_SOURCE_DIR/wterm-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name} $RPM_BUILD_DIR/%{name}-%{version}_root

%files -f ../file.list.%{name}

%changelog
* Wed Jun 30 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Removed wtmp support (Doesn't works with glibc 2.1)

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 08 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Update to 6.2.7a1

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- added Group, Summary and %description translations

* Thu Mar 04 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Change of /usr/local to /usr/X11R6

* Wed Mar 03 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- First build...
