%define name wmsound
%define version 0.9.5
%define release 1cl

%define wmsharedir /usr/X11R6/share/WindowMaker
%define wmglobaldir /usr/X11R6/etc/WindowMaker

Summary: WindowMaker sound server
Summary(pt_BR): Servidor de som do Window Maker
Summary(es): Servidor de sonido del Window Maker
Summary(fr): Serveur de son de WindowMaker

Name: %{name}
Version: %{version}
Release: %{release}
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL
Source: %{name}-%{version}.tar.bz2
Source2: wmsdefault.tar.bz2
Source3: WMSound
Source800: wmsound-wmconfig.i18n.tgz
Buildroot: /var/tmp/%{name}_root
Requires: WindowMaker >= 0.51.0

%description
Wmsound is the sound server for WindowMaker, it 
currently supports 8 or 16 bit .wav files.

%description -l pt_BR
O wmsound é o servidor de som para o Window Maker,
atualmente suporta arquivos .wav de 8 ou 16 bits.

%description -l es
wmsound es el servidor de sonido para Window Maker, actualmente
soporta archivos .wav de 8 ó 16 bits.

%description -l fr
Wmsound est le serveur de son pour WindowMaker,
il supporte actuellement les fichiers son .wav
8 ou 16 bit.

%package data
Summary: Wmsound data
Summary(pt_BR): Dados para o wmsound
Summary(es): Datos para wmsound
Summary(fr): Données de Wmsound
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Requires: wmsound >= %{version}

%description data
The standard Wmsound data.

%description -l pt_BR data
Os dados padrão para o wmsound.

%description -l es data
Los datos predeterminados para wmsound.

%description data -l fr
Les données standard de Wmsound.

%package devel
Summary: Wmsound development libraries and headers
Summary(pt_BR): Bibliotecas e arquivos de inclusão para desenvolver aplicações wmsound
Summary(es): Bibliotecas y archivos de inclusión para desarrollar aplicaciones wmsound
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
Libraries to build applications with wmsound.

%description -l pt_BR devel
Bibliotecas para construir aplicações com wmsound.

%description -l es devel
Bibliotecas y archivos de inclusión, para que puedas desarrollar
aplicaciones que usen el servidor de sonido wmsound.

%prep

%setup
tar Ixvf $RPM_SOURCE_DIR/wmsdefault.tar.bz2

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"
xmkmf -a
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/include/X11
mkdir -p $RPM_BUILD_ROOT%{wmsharedir}/{Defaults,SoundSets,Sounds}
mkdir -p $RPM_BUILD_ROOT%{wmglobaldir}
install -m 644 lib/libwmsnd.a $RPM_BUILD_ROOT/usr/X11R6/lib
install -m 644 lib/wmsnd.h $RPM_BUILD_ROOT/usr/X11R6/include/X11
install -m 755 src/wmsound $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 755 utils/nmaker $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 755 utils/{getsounds,nmaker,setsounds} \
               $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 644 Sounds/*.wav $RPM_BUILD_ROOT%{wmsharedir}/Sounds
install -m 644 $RPM_SOURCE_DIR/WMSound $RPM_BUILD_ROOT%{wmglobaldir}
strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

mv $RPM_BUILD_ROOT%{wmsharedir}/Sounds/deiconify.wav $RPM_BUILD_ROOT%{wmsharedir}/Sounds/uniconify.wav

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig


tar xvfpz $RPM_SOURCE_DIR/wmsound-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%attr(-,root,root) %doc AUTHORS COPYING ChangeLog BUGS 
%attr(-,root,root) /usr/X11R6/bin/wmsound
%attr(-,root,root) /usr/X11R6/bin/nmaker
%attr(-,root,root) /usr/X11R6/bin/getsounds
%attr(-,root,root) /usr/X11R6/bin/setsounds
%attr(-,root,root) /etc/X11/wmconfig/wmsound

%files data
%attr(644,root,root) %config %{wmglobaldir}/WMSound
%attr(755,root,root) %dir %{wmsharedir}/Sounds
%attr(644,root,root) %{wmsharedir}/Sounds/*.wav
%attr(755,root,root) %dir %{wmsharedir}/SoundSets

%files devel
%attr(-,root,root) /usr/X11R6/lib/libwmsnd.a
%attr(-,root,root) /usr/X11R6/include/X11/wmsnd.h

%clean
rm -fr $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%changelog
* Fri Jun 04 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- removed fix to wmaker domain
- updated to 0.9.5

* Fri Apr 09 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Fixed problem with config in new wmaker domain

* Thu Apr 01 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added wmconfig file to files section
- Added path for soundsets in WMSound config file

* Tue Mar 30 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Changed a wav file from deiconify.wav to uniconify.wav (as in WMSound defaults)
- Moved wmsnd.h from include/ to include/X11

* Thu Mar 18 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 0.9.4

* Tue Mar 09 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 0.9.3
