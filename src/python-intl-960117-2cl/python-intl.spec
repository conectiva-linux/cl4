Summary: Special Python internationalization modules
Summary(pt_BR): Esse pacote contém um módulo para internacionalizar Programas em Python
Summary(es): Special Python internationalization modules
Name: python-intl
Version: 960117
Release: 2cl
Copyright: GPL
Group: Applications/Libraries
Group(pt_BR): Aplicações/Bibliotecas
Group(es): Aplicaciones/Bibliotecas
Source: intl-%{PACKAGE_VERSION}.tgz
Requires: python >= 1.5 python <= 1.6
# Cabaret used to provide this like this, so it will stay here
# for compatibility for a while
Provides: intl.so
BuildRoot: /var/tmp/intl-root
Patch: intl-makefile.patch

%description
This package contains a Python module for internationalization.

%description -l pt_BR
Esse pacote contém um módulo para internacionalizar Programas em Python.

%description -l es
This package contains a Python module for internationalization.

%prep
%setup -n intl
%patch -p1

%build
make

%install
mkdir -p $RPM_BUILD_ROOT//usr/lib/python1.5/lib-dynload/
install -s -o root -m 555 intl.so $RPM_BUILD_ROOT/usr/lib/python1.5/lib-dynload/
install -s -o root -m 555 wstrop.so $RPM_BUILD_ROOT/usr/lib/python1.5/lib-dynload/

%files
/usr/lib/python1.5/lib-dynload/intl.so
/usr/lib/python1.5/lib-dynload/wstrop.so
%doc README

%changelog
* Wed Jun 22 1999 Guilherme Manika <gwm@conectiva.com>
- Added README to documentation

* Tue Jun 22 1999 Guilherme Manika <gwm@conectiva.com>
- Initial rpm
