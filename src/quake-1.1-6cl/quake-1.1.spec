Name: quake
Version: 1.1 
Release: 6cl
Summary: Quake for linux
Summary(pt_BR): Quake para linux
Summary(es): Quake para linux
Source0: squake-1.1-i386-unknown-linux2.0.tar.bz2
Source1: quake
Source2: sysconfig.quake
Source3: quake.config.cfg
Source4: quake.netgame.cfg
Copyright: ID Software
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
URL: http://www.idsoftware.com
Requires: svgalib >= 1.2.11
BuildRoot: /var/tmp/quake

%description
Quake for linux!

%description -l pt_BR
Quake para Linux!

%description -l es
Quake para Linux!

%prep

%setup -c

%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/lib/quake/id1
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig

install -m755 -o 0 -g 0 squake $RPM_BUILD_ROOT/usr/bin/squake
install -m755 -o 0 -g 0 $RPM_SOURCE_DIR/quake $RPM_BUILD_ROOT/usr/bin/quake
install -m644 -o 0 -g 0 $RPM_SOURCE_DIR/sysconfig.quake $RPM_BUILD_ROOT/etc/sysconfig/quake

for i in config netgame ; do
	install -m644 -o 0 -g 0 $RPM_SOURCE_DIR/quake.$i.cfg $RPM_BUILD_ROOT/usr/lib/quake/id1/$i.cfg
done

%files
/usr/bin/squake
/usr/bin/quake
%config /usr/lib/quake/id1/config.cfg
%config /usr/lib/quake/id1/netgame.cfg
%config /etc/sysconfig/quake
%doc readme.squake

%changelog
* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Dec 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- final rebuild for 3.0
