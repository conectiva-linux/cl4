%define name basic-workstation-icons
%define version 4.0
%define release 1cl
%define dockdir /etc/X11/dock
%define kdestopdir /usr/share/kdestart/Desktop

Summary: kde-desktop shortcuts and wmaker clips for a user instalation
Summary(pt_BR): Atalhos para o KDE e clips para o WindowMaker
Summary(es): kde-desktop shortcuts and wmaker clips for a user instalation
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source: personalizacao.tar.bz2
Requires: WindowMaker
Requires: XFree86
Requires: control-panel
Requires: gimp
Requires: gnome-pim
Requires: gnome-linuxconf
Requires: gnome-core
Requires: kdeadmin
Requires: kdegames
Requires: kdeutils
Requires: kdenetwork
Requires: kdestart 
Requires: killustrator
Requires: licq
Requires: mc
Requires: netscape-communicator
Requires: pysol
Requires: setuptool
Requires: x11amp
Requires: xgalaga
BuildRoot: /var/tmp/%{name}_root
BuildArch: noarch

%description
This package contains shortcuts and WindowMaker clip definitions for an
user instalation.

%description -l pt_BR
Este pacote contém atalhos para o KDE e clips para o WindowMaker.

%description -l es
This package contains shortcuts and WindowMaker clip definitions for an
user instalation.

%prep
%setup -q -n personalizacao

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
cp -a * $RPM_BUILD_ROOT

# files section

cd $RPM_BUILD_ROOT

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' > \
    $RPM_BUILD_DIR/file.list.%{name}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
    $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name} $RPM_BUILD_DIR/%{name}-%{version}

%files -f ../file.list.%{name}

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added to Conectiva Linux
- Bumped version to 4.0, as this is the version of our distribution

* Thu Jul 01 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- added requires to gnome-core (some icons)

* Thu Jun 24 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- First build
