%define name fortune-pt_BR
%define version 1.0
%define release 1cl

Summary: Portuguese fortunes
Summary(pt_BR): Ditados portugueses
Summary(es): Portuguese fortunes
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
#Source: http://www.terravista.pt/Ancora/1790/arquivos/fortunes.tar.gz
Source: %{name}.tar.bz2
BuildRoot: /var/tmp/%{name}_root
Requires: fortune-mod
Buildarch: noarch

%description
Portuguese fortunes. This is an addiction to the fortune program.
use with: fortune fortunes-pt_BR

%description -l pt_BR
Ditados em português, use assim: fortune fortunes-pt_BR

%description -l es
Portuguese fortunes. This is an addiction to the fortune program.
use with: fortune fortunes-pt_BR

%prep
%setup -q -n fortune-pt_BR

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/games/fortunes
install -m 644 fortunes-pt_BR $RPM_BUILD_ROOT/usr/share/games/fortunes/
install -m 644 fortunes-pt_BR.dat $RPM_BUILD_ROOT/usr/share/games/fortunes/

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/fortune-pt_BR

%files
%defattr(-,root,root)
/usr/share/games/fortunes/fortunes-pt_BR
/usr/share/games/fortunes/fortunes-pt_BR.dat

%changelog
* Mon Jun 07 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- first build for conectiva linux
