Name: quake2
Version: 3.20
%define version %{PACKAGE_VERSION}
Release: 5cl
Summary: Quake2 for linux
Summary(pt_BR): Quake2 para Linux
Summary(es): Quake2 para Linux
Source0: ftp://ftp.cdrom.com/pub/idgames/idstuff/quake2/unix/quake2-%{version}-glibc-i386-unknown-linux2.0.tar.gz
Source1: quake2
Source2: sysconfig.quake2
Source3: quake2.conf
Source4: quake2-server.conf
Source5: quake2-server
Copyright: distributable
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
URL: http://www.idsoftware.com
Requires: svgalib >= 1.2.13
BuildRoot: /var/tmp/quake2
Autoreqprov: no

%description
Quake2 for linux!

%description -l pt_BR
Quake2 para Linux!

%description -l es
Quake2 para Linux!

%package server
Summary: Quake2 server
Summary(pt_BR): Servidor Quake2
Summary(es): Servidor Quake2
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Requires: quake2 = %{version} chkconfig >= 0.9

%description server
Quake2 server

%description -l pt_BR server
Servidor Quake2

%description -l es server
Quake2 para Linux!

%prep

%setup -c
%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/lib/quake2
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig

tar cf - * | (cd $RPM_BUILD_ROOT/usr/lib/quake2 ; tar xf -)
rm -f $RPM_BUILD_ROOT/usr/lib/quake2/quake2
rm -rf $RPM_BUILD_ROOT/usr/lib/quake2/baseq2/{players,save}
install -m755 -o 0 -g 0 quake2 $RPM_BUILD_ROOT/usr/bin/quake2id
install -m755 -o 0 -g 0 $RPM_SOURCE_DIR/quake2.conf $RPM_BUILD_ROOT/etc
install -m755 -o 0 -g 0 $RPM_SOURCE_DIR/quake2-server.conf $RPM_BUILD_ROOT/usr/lib/quake2/baseq2/server.cfg
install -m755 -o 0 -g 0 $RPM_SOURCE_DIR/quake2-server $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m755 -o 0 -g 0 $RPM_SOURCE_DIR/quake2 $RPM_BUILD_ROOT/usr/bin/quake2
install -m644 -o 0 -g 0 $RPM_SOURCE_DIR/sysconfig.quake2 $RPM_BUILD_ROOT/etc/sysconfig/quake2

#%post server
#/sbin/chkconfig --add quake2-server

%preun server
if [ "$1" = 0 ]
then /sbin/chkconfig --del quake2-server
fi

%files
/usr/bin/quake2id
/usr/bin/quake2
/usr/lib/quake2
%config /etc/sysconfig/quake2
%config /etc/quake2.conf
%doc README readme.txt %{version}_Changes.txt

%files server
/etc/rc.d/init.d/quake2-server
%config /usr/lib/quake2/baseq2/server.cfg

%changelog
* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- upgraded to 3.20

* Fri Mar 12 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- initscript i18n

* Fri Nov 20 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- correções do aurélio para convivência com o linuxconf

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Sep 11 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to 3.19a glibc!

* Wed Sep 02 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- quake2-server not started by default

* Sat Aug 22 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- updated to 3.17
