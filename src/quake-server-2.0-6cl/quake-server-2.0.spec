Name: quake-server
Version: 2.0 
Release: 6cl
Summary: Quake server for linux
Summary(pt_BR): Servidor quake para linux
Summary(es): Servidor quake para linux
Source0: unixded-1.0-i386-unknown-linux2.0.tar.gz
Source1: quake-server
Copyright: Distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
URL: http://www.idsoftware.com
Requires: quake-levels-shareware chkconfig >= 0.9
BuildRoot: /var/tmp/quake-server

%description
Quake Server

%description -l pt_BR
Servidor quake para Linux

%description -l es
Servidor Quake para Linux

%prep

%setup -c

%build

%install

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/usr/sbin

for i in 3 0 6 ; do
	mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc$i.d
done

install -m 755 -o 0 -g 0 $RPM_SOURCE_DIR/quake-server $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 -o 0 -g 0 unixded $RPM_BUILD_ROOT/usr/sbin

#%post
#/sbin/chkconfig --add quake-server

%postun
if [ "$1" = 0 ]
then /sbin/chkconfig --del quake-server
fi

%files
/etc/rc.d/init.d/quake-server
/usr/sbin/unixded
%doc readme.unixded

%changelog
* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Mar 13 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscript i18n

