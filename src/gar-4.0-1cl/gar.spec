Copyright: GPL
Source0: gar.tar.bz2
Source800: wmconfig.i18n.tgz
Release: 1cl
Name: gar
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Version: 4.0
Summary: The network administrators guide (Brazilian portuguese version)
Summary(pt_BR): O guia do administrador de redes (Versão em português do Brasil)
Summary(es): The network administrators guide (Brazilian portuguese version)
BuildArchitectures: noarch
BuildRoot: /tmp/gar-install-root

%changelog
* Mon Jun 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Created package

%description
This is the HTML version of the Network Administrators Guide,
translated to the Brazilian portuguese.

%description -l pt_BR
Esta é a versão HTML do Guia do administrador de redes,
traduzido para o português do Brasil.

%description -l es
This is the HTML version of the Network Administrators Guide,
translated to the Brazilian portuguese.

%prep
%setup -q -n gar

%install
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc *
/etc/X11/wmconfig/gar
