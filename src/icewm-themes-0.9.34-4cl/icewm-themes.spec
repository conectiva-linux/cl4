%define ver 0.9.34
%define prefix /usr/X11R6

Summary: X11 Window Manager Themes
Summary(pt_BR): Temas para o gerenciador de janelas icewm.
Summary(es): Temas para el administrador de ventanas icewm
Name: icewm-themes
Prefix: %prefix
Version: %ver
BuildArch: noarch
Release: 4cl
Copyright: LGPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
# was .gz
Source: icewm-themes-%ver.tar.bz2
URL: http://www.kiss.uni-lj.si/~k4fr0235/icewm/
BuildRoot: /tmp/build-icewm-themes-%ver

%description
Themes for icewm window manager.

%description -l pt_BR
Temas para o gerenciador de janelas icewm.

%description -l es
Temas para el administrador de ventanas icewm.

%prep
%setup

%build

%install
make PREFIX=$RPM_BUILD_ROOT%{prefix} install

%files
%defattr(-,root,root)
%{prefix}/lib/X11/icewm/themes/

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initial packaging
