Summary: Text tool for setting and loading a keyboard map
Summary(pt_BR): Ferramenta modo texto para ajustar e carregar um mapa de teclado
Summary(es): Herramienta modo texto para ajustar y cargar un mapa de teclado
Name: kbdconfig
%define version	1.9.2
Version: %{version}
Release: 3cl
Copyright: GPL
ExclusiveOS: Linux
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
BuildRoot: /var/tmp/kbdconfig-root
Source: kbdconfig-%{version}.tar.bz2
Source1: kbdconfig-es.po
Patch0: kbdconfig-%{version}-conectiva.patch

%description
This is a terminal mode program for setting the keyboard map for your system.
Keyboard maps are necessary for using non US default keyboards. Kbdconfig
loads the selected keymap before exiting and configures your machine to
use that keymap automatically after rebooting.

%description -l pt_BR
Este é um programa modo terminal para ajustar o mapa de teclado
para o seu sistema. Mapas de teclado são necessários para usar
teclados que não sejam padrão US. Kbdconfig carrega o mapa de
teclado selecionado antes de sair e configura a sua máquina para
utilizá-lo após o boot.

%description -l es
Este es un programa modo terminal para ajustar el mapa de teclado
para tu sistema. Los mapas de teclado son necesarios para la
utilización de teclados que no sean padrón US. Kbdconfig carga el
mapa de teclado seleccionado antes de salir y configura su máquina
para utilizarlo después del arranque.

%prep
%setup -q
%patch -p1
cp $RPM_SOURCE_DIR/kbdconfig-es.po po/es.po

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make INSTROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root)/usr/sbin/kbdconfig
%attr(-,root,root)/usr/man/man8/kbdconfig.8
%attr(-,root,root)/usr/man/*/man8/kbdconfig.8
%attr(-,root,root)/usr/share/locale/*/LC_MESSAGES/kbdconfig.mo

%changelog 
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 31 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.9.2

* Wed Mar 31 1999 Conectiva <dist@conectiva.com>
- added spanish .po

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Nov 22 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- patch to symlink .Xmodmap in /etc/X11/xinit

* Mon Nov  9 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- included pt_BR translated man page in %files

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- translation updates

* Fri Sep 25 1998 Cristian Gafton <gafton@redhat.com>
- turkish message catalog

* Wed Sep 23 1998 Erik Troan <ewt@redhat.com>
- look in qwertz directory as well

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- remove path checks from keyboard map processing.
- add sparc support.

* Sun Aug 02 1998 Erik Troan <ewt@redhat.com>
- added --back
- built against newt 0.30

* Sun Mar 22 1998 Erik Troan <ewt@redhat.com>
- added i18n support
- added --back option
- added man page
- buildrooted spec file

* Mon Jan 12 1998 Erik Troan <ewt@redhat.com>
- added patch to replace alloca() with malloc()

* Tue Nov  4 1997 Michael Fulbrght <msf@redhat.com>
- changed to handle .map and .map.gz files properly
