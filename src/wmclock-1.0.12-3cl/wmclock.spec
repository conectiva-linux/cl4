%define Name		wmclock
%define Version		1.0.12
%define ReleaseNum	3cl
%define linguagem   portuguese

Summary: dockable clock applet for Window Maker
Summary(pt_BR): Relógio para o "dock" do Window Maker
Summary(es): dockable clock applet for Window Maker
Name: %{Name}
Version: %{Version}
Release: %{ReleaseNum}
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
URL: http://www.asclock.org/
Source: %{Name}-%{Version}.tar.gz
Prefix: %{Prefix}
BuildRoot: /var/tmp/%{Name}_root

%description
Wmclock is an applet which displays the date and time in a dockable
tile in the same style as the clock from the NEXTSTEP(tm) operating
system.  Wmclock is specially designed for the Window Maker window
manager, by Alfredo Kojima, and features multiple language support,
twenty-four-hour and twelve-hour (am/pm) time display, and, optionally,
can run a user-specified program on a mouse click.  Wmclock is derived
from asclock, a similar clock for the AfterStep window manager.

%description -l pt_BR
O wmclock é um aplicativo que mostra a data e a hora no "dock" do
Window Maker no mesmo estilo do relógio no sistema operacional
NEXTSTEP(r). Foi projetado especialmente para o gerenciador de
janelas Window Maker, do Alfredo Kojima, e tem várias características:
suporte a várias línguas, mostra a hora em formato 24 horas e 12 horas
(am/pm) e, opcionalmente, pode executar um programa especificado pelo
usuário quando for clicado. É derivado do asclock, um relógio similar
para o gerente de janelas AfterStep.

%description -l es
Wmclock is an applet which displays the date and time in a dockable
tile in the same style as the clock from the NEXTSTEP(tm) operating
system.  Wmclock is specially designed for the Window Maker window
manager, by Alfredo Kojima, and features multiple language support,
twenty-four-hour and twelve-hour (am/pm) time display, and, optionally,
can run a user-specified program on a mouse click.  Wmclock is derived
from asclock, a similar clock for the AfterStep window manager.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --lang %{linguagem}
make

%install
for i in \
    "/usr" \
    "/usr/share" \
    "/usr/share/%{Name}" \
; do
    mkdir -p "${RPM_BUILD_ROOT}${i}"
done

make DESTDIR="${RPM_BUILD_ROOT}" install
make DESTDIR="${RPM_BUILD_ROOT}" install.man
make DESTDIR="${RPM_BUILD_ROOT}" install.share

%clean
rm -rf "${RPM_BUILD_ROOT}"

%files
%attr(-   ,root,root) %doc COPYING INSTALL README
%attr(0755,root,root) /usr/X11R6/bin/wmclock
%attr(0755,root,root) /usr/X11R6/man/man1/wmclock.1x
%attr(0755,root,root) %dir /usr/share/wmclock
%attr(-   ,root,root) /usr/share/wmclock/*

%changelog
* Wed May 26 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- added pt_BR translations
- default to compile in portuguese

* Sun Apr 18 1999 Jim Knoble <jmknoble@pobox.com>
  [wmclock-1.0.12-2]
  - Public release of RPMs.

* Sat Apr 10 1999 Jim Knoble <jmknoble@pobox.com>
  [wmclock-1.0.12-1]
  - Initial packaging.

