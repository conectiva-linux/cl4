Summary: Text-mode Configuration Tool
Summary(pt_BR): Ferramenta de configuração em modo texto
Summary(es): Herramienta de configuración en modo texto
# the name is "setuptool" because we already have a package
# named "setup".  Oh, well.
Name: setuptool
Version: 1.0
Release: 4cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: setup-%{PACKAGE_VERSION}.tar.gz
Source800: wmconfig.i18n.tgz
Requires: python pythonlib >= 1.21 snack python-intl
BuildArchitectures: noarch
BuildRoot: /var/tmp/setup-root
Patch: setup-intl+pt_BR.patch

%description
setup is a friendly text-mode menu program that gives you easy,
instant access to all the text-mode configuration programs in
Conectiva Linux.

%description -l pt_BR
Setup é um programa amigável, em modo texto, que dá acesso a todas
as ferramentas de configuração do Red Hat Linux, que sejam também
em modo texto.

%description -l es
Setup es un programa amigable, en modo texto, que da acceso a todas
las herramientas de configuración del Red Hat Linux, que también
sean en modo texto.

%changelog
* Tue Jun 22 1999 Guilherme Manika <gwm@conectiva.com>
- i18n

* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations


* Wed Nov 05 1997 Michael K. Johnson <johnsonm@redhat.com>

- initial version

%prep
%setup -n setup-%{PACKAGE_VERSION}
%patch -p1

%build
make
cd po
make

%install
make install ROOT=$RPM_BUILD_ROOT
cd po
make install ROOT=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
/usr/sbin/setup
/etc/X11/wmconfig/setup
/usr/lib/rhs/setup
/usr/share/locale/pt_BR/LC_MESSAGES/setuptool.mo
