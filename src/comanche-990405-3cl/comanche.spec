Summary: A front-end for configuring the Apache Web server.
Summary(pt_BR): Configurador do Apache
Summary(es): Configurador del Apache
Name: comanche
Serial: 1
Version: 990405
Release: 3cl
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source0: http://comanche.com.dtu.dk/comanche/download/com%{version}.tar.gz
Source1: comanche.wmconfig
Source2: comanche.xpm
Source3: comanche-mini.xpm

Copyright: GPL
BuildRoot: /var/tmp/comanche-root
BuildArchitectures: noarch
Obsoletes: apachecfg
Requires: itcl, tk, rcs

%description
Comanche (COnfiguration MANager for apaCHE) is a front-end for the
Apache Web server, the most popular Web server used on the Internet.
Comanche aims to to make it easier to manage and configure Apache.

%description -l pt_BR
Comanche significa COnfiguration MANager for apaCHE. É um front-end
popular para o Projeto de Configuração do Servidor Apache, que é
o servidor web mais popular, rápido e confiável da Internet.

Este pacote trabalha com RCS para fornecer um histórico preciso
das alterações nos arquivos de configuração do apache.

%description -l es
Comanche significa COnfiguration MANager sea apaCHE. Es un front-end
popular para el Proyecto de Configuración del Servidor Apache,
que es el servidor web más popular, rápido y fiable de la Internet.
Este paquete trabaja con RCS para ofrecer un histórico preciso de
las alteraciones en los archivos de configuración del apache.

%prep
%setup -q -n com%{version}

%build
cat > comanche <<EOF
#!/bin/bash
#

cd /usr/lib/comanche
exec /usr/bin/itkwish3.0 main.tcl /etc/httpd/conf
EOF

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/comanche}
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 755 comanche $RPM_BUILD_ROOT/usr/bin
rm apachectl INSTALL changes.txt comanche 
cp -a * $RPM_BUILD_ROOT/usr/lib/comanche
install -m 644 $RPM_SOURCE_DIR/comanche.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/comanche
chmod 600 $RPM_BUILD_ROOT/etc/X11/wmconfig/comanche
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/mini
install -m 644 $RPM_SOURCE_DIR/comanche.xpm $RPM_BUILD_ROOT/usr/share/icons
install -m 644 $RPM_SOURCE_DIR/comanche-mini.xpm \
	$RPM_BUILD_ROOT/usr/share/icons/mini/mini-comanche.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/*
/usr/lib/comanche
%config(missingok) /etc/X11/wmconfig/comanche
/usr/share/icons/comanche.xpm
/usr/share/icons/mini/mini-comanche.xpm

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Injected new group into package

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- upgrade to Daniel's latest fix release (990405)

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- defattr for files section
- upgrade to Daniel's latest fix release

* Fri Mar 26 1999 Daniel Lopez <ridruejo@comanche.com.dtu.dk>
- upgrade to 19990325, added missing documentation

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 19981207, fixed wmconfig stuff.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.6a
- patched to work with apache 1.3.2

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- install comanche.xpm in the control-panel directory

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- first packaging
- added patch from MkJ to get rid og non-working menus
- obsoletes apachecfg
