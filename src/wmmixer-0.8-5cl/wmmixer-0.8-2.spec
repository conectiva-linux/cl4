%define name wmmixer
%define version 0.8
%define release 5cl

%define builddir $RPM_BUILD_DIR/%{name}

Summary: Sound mixer applet
Summary(pt_BR): Applet para controle de volume e outras opções do som.
Summary(es): Applet para control de volumen y otras opciones de sonido.
Summary(fr): Applette de volume du son

Name: %{name}
Version: %{version}
Release: %{release}
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL
Source0: %{name}.tgz
Source1: %{name}.wmconfig
Source800: wmmixer-wmconfig.i18n.tgz
Patch: %{name}-%{version}-2-c++.patch.gz
Buildroot: /tmp/%{name}-%{version}-%{release}-root
Icon: %{name}.gif

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Tue Dec  8 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations


%description 
Wmmixer is a sound mixer applet designed for the
Windowmaker dock.

%description -l pt_BR
Applet para controle de volume e outras opções do som
no dock do Window Maker

%description -l es
Applet para control de volumen y otras opciones de sonido.

%description -l fr
Wmmixer est une applette de volume du son conçue
pour le dock de WindowMaker.

%prep

%setup -n %{name}

%patch -p1

%build
xmkmf
make CFLAGS="$RPM_OPT_FLAGS"

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin $RPM_BUILD_ROOT/etc/X11/wmconfig
strip %{builddir}/wmmixer
cp %{builddir}/wmmixer $RPM_BUILD_ROOT/usr/X11R6/bin
#cp $RPM_SOURCE_DIR/%{name}.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}
mv %{builddir}/.wmmixer %{builddir}/sample.wmmixer


tar xvfpz $RPM_SOURCE_DIR/wmmixer-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc README FAQ COPYING sample.wmmixer
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/wmmixer
%attr(755,root,root) /usr/X11R6/bin/wmmixer

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}
