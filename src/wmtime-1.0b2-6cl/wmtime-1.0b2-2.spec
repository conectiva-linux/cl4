%define name wmtime
%define version 1.0b2
%define release 6cl

%define builddir $RPM_BUILD_DIR/%{name}.app

Summary: Time applet
Summary(pt_BR): Applet para mostrar data e hora no dock do Window Maker.
Summary(es): Applet para muestrar la fecha y hora en el dock del Window Maker.
Summary(fr): Applette horloge

Name: %{name}
Version: %{version}
Release: %{release}
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL
Url: http://windowmaker.mezaway.org/
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.wmconfig
Source800: wmtime-wmconfig.i18n.tgz
Patch: %{name}-%{version}-2-makefile.patch.gz
Buildroot: /tmp/%{name}-%{version}-%{release}-root
Icon: %{name}.gif

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Tue Dec  8 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

%description
Wmtime is a WindowMaker dock applet that can
display time in analog and digital forms. It
displays the date too.

%description -l pt_BR
Applet para mostrar data e hora no dock do Window Maker.
Mostra de forma analógica ou digital.

%description -l es
Applet para muestrar la fecha y hora en el dock del Window Maker.

%description -l fr
Wmtime est une applette pour le dock de 
WindowMaker qui peut afficher l'heure dans
une forme analogique ou digitale. Elle peut
afficher la date aussi.

%prep

%setup -n %{name}.app

%patch -p1

%build
cd wmtime
make CFLAGS="$RPM_OPT_FLAGS"

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/bin}
cp %{builddir}/wmtime/wmtime $RPM_BUILD_ROOT/usr/X11R6/bin
strip $RPM_BUILD_ROOT/usr/X11R6/bin/wmtime
cp $RPM_SOURCE_DIR/%{name}.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}



tar xvfpz $RPM_SOURCE_DIR/wmtime-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/wmtime
%attr(755,root,root) /usr/X11R6/bin/wmtime

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}
