Summary: NetCat - Network test and debugging tool
Summary(pt_BR): Ferramenta de teste e depuração para serviços de rede
Summary(es): Herramienta de prueba e depuración para servicios de red
Name: nc
Version: 1.10
Release: 6cl
# was .tgz
Source: ftp://ftp.avian.org/src/hacks/nc110.tar.bz2
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
BuildRoot: /var/tmp/nc

%description
NetCat is a minimal network client. It can be used to make terminal
TCP connections to arbitrary ports and can fake connections over
UDP. It can also listen on ports.

%description -l pt_BR
O NetCat é um cliente de rede mínimo. Pode ser usado para criar
conexões TCP para portas arbitrárias e pode simular conexões sobre
UDP. Também pode receber conexões.

%description -l es
NetCat es un cliente de red mínimo. Puede ser usado para crear
conexiones TCP a puertos arbitrarios y puede simular conexiones
sobre UDP. También puede oír puertos.

%prep
%setup -c -n nc -q

%build
#Make linux is supported, but it makes a static binary. 
make CFLAGS="$RPM_OPT_FLAGS" generic

%install
mkdir $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/usr
mkdir $RPM_BUILD_ROOT/usr/bin

cp nc $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changelog
%doc scripts
/usr/bin/nc

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Nov 27 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
