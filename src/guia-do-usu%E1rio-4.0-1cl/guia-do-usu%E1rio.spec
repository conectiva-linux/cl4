Copyright: GPL
Source0: guia_usuario.tar.bz2
Source800: wmconfig.i18n.tgz
Release: 1cl
Name: guia-do-usu�rio
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Version: 4.0
Summary: The Conectiva Linux 4.0 Users Guide
Summary(pt_BR): O guia do Usu�rio do Conectiva Linux 4.0
Summary(es): The Conectiva Linux 4.0 Users Guide
BuildArchitectures: noarch
BuildRoot: /tmp/guia-do-usuario-install-root

%changelog
* Mon Jun 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Created package

%description
This is the HTML version of the Conectiva Linux 4.0 Users guide,
translated to the Brazilian portuguese.

%description -l pt_BR
Esta � a vers�o HTML do Guia do guia do Usu�rio do Conectiva Linux 4.0,
traduzido para o portugu�s do Brasil.

%description -l es
This is the HTML version of the Conectiva Linux 4.0 Users guide,
translated to the Brazilian portuguese.

%prep
%setup -q -n guia_usuario

%install
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc *
/etc/X11/wmconfig/guia-do-usu�rio
