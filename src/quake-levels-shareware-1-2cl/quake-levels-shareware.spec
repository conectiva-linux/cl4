Name: quake-levels-shareware
Version: 1
Release: 2cl
Summary: Niveis Shareware do Quake
Summary(pt_BR): Níveis Shareware do Quake
Summary(es): Niveles Shareware del Quake
Source: pak0.pak.bz2
Copyright: Shareware
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
URL: http://www.idsoftware.com/
BuildRoot: /var/tmp/quake-levels-shareware
BuildArchitectures: noarch
Autoreqprov: no

%description
Shareware quake levels

%description -l pt_BR
Níveis Shareware do Quake

%description -l es
Niveles Shareware del Quake

%install

mkdir -p $RPM_BUILD_ROOT/usr/lib/quake/id1
cp $RPM_SOURCE_DIR/pak0.pak.bz2 $RPM_BUILD_ROOT/usr/lib/quake/id1
cd $RPM_BUILD_ROOT/usr/lib/quake/id1
bunzip2 pak0.pak.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir /usr/lib/quake
/usr/lib/quake/id1/pak0.pak
