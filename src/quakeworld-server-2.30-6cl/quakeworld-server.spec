Name: quakeworld-server
Version: 2.30
Release: 6cl
Summary: QuakeWorld Server
Summary(pt_BR): Servidor quakeworld para Linux
Summary(es): Servidor quakeworld para Linux
Source: ftp://ftp.idsoftware.com/idstuff/quakeworld/qwsv-2.30-glibc-i386-unknown-linux2.0.tar.gz
Source1: quakeworld-server
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
URL: http://www.idsoftware.com/
Requires: svgalib >= 1.3.0
Requires: quake-levels-shareware
Requires: chkconfig >= 0.9
BuildRoot: /tmp/quakeworld-server

%description
QuakeWorld Server

%description -l pt_BR
Servidor quakeworld para Linux

%description -l es
Servidor quakeworld para Linux

%prep

%setup -c

%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/usr/lib/quake/qw

strip qwsv
install -m 755 -o 0 -g 0 qwsv $RPM_BUILD_ROOT/usr/sbin
install -m 755 -o 0 -g 0 qw/qwprogs.dat $RPM_BUILD_ROOT/usr/lib/quake/qw
install -m 755 -o 0 -g 0 $RPM_SOURCE_DIR/quakeworld-server $RPM_BUILD_ROOT/etc/rc.d/init.d

#%post
#/sbin/chkconfig --add quakeworld-server

%preun
if [ "$1" = "0" ]
then /sbin/chkconfig --del quakeworld-server
fi

%files
/usr/sbin/qwsv
/etc/rc.d/init.d/quakeworld-server
/usr/lib/quake/qw
%doc README.qwsv

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed spec file wrt rpm 3.0.2

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Fri Mar 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscripts i18n
- added Group, Summary and %description translations

* Fri Nov 20 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- correções do aurélio para convivência com o linuxconf
