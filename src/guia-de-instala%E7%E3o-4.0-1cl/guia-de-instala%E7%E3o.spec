Copyright: GPL
Source0: guia_instalacao.tar.bz2
Source800: wmconfig.i18n.tgz
Release: 1cl
Name: guia-de-instalação
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Version: 4.0
Summary: The Conectiva Linux 4.0 Installation Guide
Summary(pt_BR): O guia de instalação do Conectiva Linux 4.0
Summary(es): The Conectiva Linux 4.0 Installation Guide
BuildArchitectures: noarch
BuildRoot: /tmp/guia-install-root

%changelog
* Mon Jun 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Created package

%description
This is the HTML version of the Conectiva Linux 4.0 Installation guide,
translated to the Brazilian portuguese.

%description -l pt_BR
Esta é a versão HTML do Guia do guia de instalação do Conectiva Linux 4.0,
traduzido para o português do Brasil.

%description -l es
This is the HTML version of the Conectiva Linux 4.0 Installation guide,
translated to the Brazilian portuguese.

%prep
%setup -q -n guia_instalacao

%install
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc *
/etc/X11/wmconfig/guia-de-instalação
