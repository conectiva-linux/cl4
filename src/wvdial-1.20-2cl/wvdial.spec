Summary: Automatic dialer for pppd
Summary(pt_BR): Discador automático para Internet (pppd)
Summary(es): Marcador automático para Internet (pppd)
Name: wvdial
%define version 1.20
Version: %{version}
Release: 2cl
Requires: ppp
# Source: http://www.worldvisions.ca/wvdial/wvdial-%{version}.tar.gz
# Repackaged with bzip2
Source: http://www.worldvisions.ca/wvdial/wvdial-%{version}.tar.bz2
URL: http://www.worldvisions.ca/wvdial/
Copyright: LGPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Buildroot: /var/tmp/wvdial

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr  1 1999 Conectiva <dist@conectiva.com>
- buildroot

* Sat Nov 28 1998 Dave Baker <dsb3@earthlink.net>
- Updated for v1.20
- Now compiled with egcs, not gcc

* Fri Sep 25 1998 Dave Baker <dsb3@earthlink.net>
- Updated for v1.10

* Fri Sep 11 1998 Dave Baker <dsb3@earthlink.net>
- Updated for v1.01

* Mon Sep 06 1998 Dave Baker <dsb3@earthlink.net>
- Initial RPM (v1.00) created

%description
Wvdial is a pseudo-intelligent dialer that will attempt to automatically
guess username and password prompts, and start pppd automatically.
Use the associated program wvdialconf to probe for modems and create a
default configuration file.

%description -l pt_BR
Wvdial é um discador pseudo-inteligente que tenta se conectar
automaticamente, fornecendo o nome do usuário, senha e disparando
o pppd. Use o programa wvdialconf para detectar o modems e criar
uma configuração padrão.

%description -l es
Wvdial es un marcador pseudo-inteligente que procurará conjeturar
automáticamente el username y la contraseña, arrancando el pppd.
Utilice el wvdialconf para detectar el modem y para crear un archivo
de configuración por defecto.

%prep
%setup

%build
make PREFIX=/usr

%install
make install PREFIX=$RPM_BUILD_ROOT/usr PPPDIR=$RPM_BUILD_ROOT/etc/ppp/peers
cat << EOF >> $RPM_BUILD_ROOT/etc/wvdial.conf
# Use 
#
#   wvdialconf /etc/wvdial.conf
#
# to generate this configuration file
EOF

%files
%defattr(-,root,root)
%doc ANNOUNCE CHANGES README COPYING.LIB
/usr/bin/wvdial
/usr/bin/wvdialconf
/etc/ppp/peers/wvdial
/usr/man/man1/wvdial.1
/usr/man/man1/wvdialconf.1
%config(missingok) /etc/wvdial.conf

%clean
cd ..
rm -rf wvdial-%{version} 
