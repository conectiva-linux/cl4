%define name WSoundPrefs
%define version 1.0.2
%define release 2cl
%define prefix /usr/X11R6
%define windowmaker >= 0.56.0
%define wmsound >= 0.9.5
%define require WindowMaker %{windowmaker} wmsound %{wmsound}

Summary: Window Maker Sound Preferences
Summary(pt_BR): Preferências de Som do Window Maker
Summary(es): Configuración de Sonido para Window Maker
Name: %{name}
Version: %{version}
Release: %{release}
Source: ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.bz2
Source800: WSoundPrefs-wmconfig.i18n.tgz
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Icon: WSoundPrefs.gif
URL: http://shadowmere.student.utwente.nl/wmss/
Requires: %{require}
Provides: WSoundPrefs
Buildroot: /var/tmp/%{name}_root

%description
WSoundPrefs is a WINGs-based application to configure the Window Maker
Sound Server (WMSound). It is actually a replacement of the Author's older
program called WMSound Setup (aka wmss). Basically it provides the following
options: 
- Which sound to play on which sound-event 
- Which sound-device to use 
- What are the search-paths for Sounds and SoundSets 
- Loading and Saving of Soundsets 

%description -l pt_BR
WSoundPrefs é uma aplicação baseada em WINGS para configurar o servidor
de som do WindowMaker (WMSound). Provê basicamente as opções:
- qual som tocar em qual evento
- qual dispositivo de som usar
- quais são as rotas para busca de arquivos sons
- carregar e salvar grupos de som

%description -l es
Configuración de Sonido para Window Maker. Soporta básicamente:
- que sonido tocar para determinado evento
- que dispositivo de sonido usar
- cuáles directorios buscar sonidos
- cargar y guardar grupos de sonidos

%prep
%setup
xmkmf -a

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib
make install DESTDIR=$RPM_BUILD_ROOT/usr/X11R6/lib

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

tar xvfpz $RPM_SOURCE_DIR/WSoundPrefs-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

cat << EOF > $RPM_BUILD_DIR/file.list.%{name}

%defattr(-,root,root)
#%doc AUTHORS COPYING INSTALL ChangeLog
%dir /usr/X11R6/lib/GNUstep/Apps/WSoundPrefs.app
%dir /usr/X11R6/lib/GNUstep/Apps/WSoundPrefs.app/xpm
%dir /usr/X11R6/lib/GNUstep/Apps/WSoundPrefs.app/tiff
EOF

cd $RPM_BUILD_ROOT
find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' >> \
      $RPM_BUILD_DIR/file.list.%{name}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
      $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}

%clean
rm -rf $RPM_BUILD_DIR/file.list.%{name} $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%changelog
* Tue Jun 22 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 1.0.2

* Fri Jun 04 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- updated to 1.0.0
- fix for syslimits.h

* Thu Apr 01 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added wmconfig file

* Mon Mar 22 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added pt_BR translations
- Changed paths

* Sun Mar 21 1999 Thomas Ribbrock <emgaron@gmx.net>
[0.9.4-TRi-1]
- rebuild for WindowMaker-0.51.2-nls-2 rpm from contrib
- changed file layout to match
- fixed owner
- defined BuildRoot

* Thu Mar 18 1999 Nicolas Mailhot <Nicolas.Mailhot@email.enst.fr>
[0.9.3-2]
- added directories for a cleaner uninstall

* Thu Mar 18 1999 Nicolas Mailhot <Nicolas.Mailhot@email.enst.fr>
[0.9.3-1]
- Initial release for WSoundPrefs-0.9.3-1
