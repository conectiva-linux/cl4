%define name SVGATextMode
%define version 1.9
%define release 1cl

Name: %{name}
Version: %{version}
Release: %{release}
Summary: SVGATextMode enhanced text mode switching
Summary(pt_BR): Utilitário para configuração avançada dos modos de vídeo da console
Summary(es): Utilitario para configuración avanzada de los modos de vídeo da consola
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
#Source: ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}-src.tar.gz
Source: %{name}-%{version}-src.tar.bz2
Patch0: SVGATextMode-1.9-src-make.patch
Patch1: SVGATextMode-1.8-src-agp.patch
Patch2: SVGATextMode-1.9-src-cnc.patch
Requires: kbd
BuildRoot: /var/tmp/%{name}-%{version}-root
ExclusiveArch: i386

%description
SVGATextMode allows the screen mode of the Linux console to be
controlled in detail.  This allows more characters on screen, more
stable text, less characters on screen, less stable text, etc. also, on
badly designed hardware, you could sometimes achieve a melted monitor.

Extra fonts are required to work fully, though without them useful effects
can still be achieved.

%description -l pt_BR
O SVGATextMode permite que o modo da tela do console do Linux seja
controlado detalhadamente. Isto permite que mais caracteres sejam
mostrados na tela, mais textos estáveis, menos caracteres na tela,
menos textos estáveis, etc.  Em hardware com projeto ruim voce
podera obter um monitor derretido.

Fontes extras são necessárias para que o mesmo funcione corretamente,
mas mesmo sem elas efeitos úteis podem ser obtidos.

%description -l es
SVGATextMode permite que el modo de la pantalla de la consola
del Linux sea controlada detalladamente. Esto permite que más
caracteres sean mostrados en la pantalla, más textos estables,
menos caracteres en la pantalla, menos textos estables, etc.  En un
hardware con proyecto malo podrás acabar con un monitor derretido.
Son necesarias fuentes extras para que funcione correctamente,
pero mismo sin ellas se pueden obtener efectos útiles.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 05 1999 Domingos Parra Novo <domingos@conectiva.com>
- upgraded to 1.9
- Some minor changes to specfile

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Sep 03 1998 Cristian Gafton <gafton@redhat.com>
- added patch for Matrox Millenium AGP

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- ExclusiveArch: i386

* Sun Jan 11 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.8
- built against glibc; spec file cleanup

* Wed Jul 2 1997 Timo Karjalainen <timok@iki.fi>
- Upgraded to version 1.6

* Fri Jun 13 1997 Timo Karjalainen <timok@iki.fi>
- Config file moved from /usr/etc to /etc
- Some minor changes to specfile

* Wed Jun 4 1997 Ximenes Zalteca <ximenes@null.net>
- Re-Group:'d

* Sun Apr 27 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- added %changelog
- added %clean
- added BuildRoot

%prep
%setup -q -n SVGATextMode-%{version}-src
%patch0 -p1 -b .make
%patch1 -p1 -b .agp
%patch2 -p1 -b .cnc

%build
make dep
make all RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc,usr/man/man5,usr/man/man8,usr/sbin}
make DESTDIR=$RPM_BUILD_ROOT newinstall man-install
install -m 0755 STMmenu $RPM_BUILD_ROOT/usr/sbin/stm-menu

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%config /etc/TextConfig
%doc README README.FIRST CREDITS COPYING HISTORY TODO Changelog
%doc doc/*
/usr/sbin/*
/usr/man/*/*
