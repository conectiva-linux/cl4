Summary: Tacacs / Radius AAA converter
Summary(pt_BR): Este servidor fica entre um cliente TACACS+ e um servidor RADIUS, traduzindo requisições de autenticação, autorização e contabilidade.
Summary(es): Este servidor queda entre un cliente TACACS+ y un servidor RADIUS, traduciendo requisiciones de autentificación, autorización y contabilidad.
Name: tacp2rad
Version: 0.1
Release: 7cl
Source: ftp://ftp.cistron.nl/pub/people/miquels/radius/tacp2rad-0.1.tar.gz
Source1: tacp2radd.init
Patch: tacp2rad-glibc.patch
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Buildroot: /var/tmp/tacp2rad
Requires: chkconfig >= 0.9

%changelog
* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 12 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 26 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- buildroot, chkconfig, tacp2radd.init internacionalizado e traduzido para pt_BR

* Mon May 18 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- patch for glibc

* Wed Nov  5 1997 Bruno Lopes F. Cabral <bruno@openline.com.br>

Added redhat-style init script

%description
From the webpage at http://homepage.cistron.nl/~miquels/radius/

"We bought a Cisco 4000M for ISDN30 (PRI) access, and what do you 
think - it didn't support RADIUS. It does support TACACS+, though. 
So I wrote tacp2rad. This daemon sits between a TACACS+ client (a 
Cisco access server) and a RADIUS server, translating Authentication, 
Authorization and Accounting requests."

%description -l pt_BR
Descrição em http://homepage.cistron.nl/~miquels/radius/

"Compramos um Cisco 4000M para acesso ISDN30 (PRI), e vejam o
que aconteceu: Ele não suporta RADIUS. Não suporta TACACS+ também.
Então escrevi o tacp2rad. Este servidor fica entre um cliente TACACS+
(o servidor de acessos CISCO) e um servidor RADIUS, traduzindo
requisições de autenticação, autorização e contabilidade."

%description -l es
Descripción en http://homepage.cistron.nl/\~miquels/radius/
"Compramos un Cisco 4000M para acceso ISDN30 (PRI), y miren lo que ha
ocurrido: No soporta RADIUS. No soporta TACACS+ también.  Entonces,
he escrito tacp2rad. Este servidor queda entre un cliente TACACS+
(el servidor de accesos CISCO) y un servidor RADIUS, traduciendo
requisiciones de autentificación, autorización y contabilidad."

%prep
%setup
%patch -p1

%build
make clean
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 -o root -g root -s tacp2radd $RPM_BUILD_ROOT/usr/sbin
install -m 755 -o root -g root $RPM_SOURCE_DIR/tacp2radd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/tacp2radd
install -m 644 -o root -g root tacp2rad.conf $RPM_BUILD_ROOT/etc/tacp2rad.conf
install -m 644 -o root -g root tacp2rad.map  $RPM_BUILD_ROOT/etc/tacp2rad.map

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ $0 = 0 ]; then
        /sbin/chkconfig --del tacp2radd
fi

#%post
#/sbin/chkconfig --add tacp2radd

%files
%doc README rc.tacp2radd
%config /etc/tacp2rad.conf
%config /etc/tacp2rad.map
/etc/rc.d/init.d/tacp2radd
/usr/sbin/tacp2radd

