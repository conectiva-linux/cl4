Summary: Conectiva Linux release file
Summary(pt_BR): Arquivo contendo a versão da distribuição Conectiva Linux
Summary(es): Archivo conteniendo la versión de la distribución Conectiva Linux
Name: versão-conectiva
Version: 4.0
Release: 2cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
BuildArchitectures: noarch
BuildRoot: /var/tmp/versão-conectiva-root
Obsoletes: redhat-release

%description
Conectiva Linux release file

%description -l pt_BR
Arquivo contendo a versão da distribuição Conectiva Linux

%description -l es
Archivo que contiene la versión de la distribución Conectiva Linux

%changelog
* Wed Jun 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Obsoletes redhat-release

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Conectiva Linux 4.0

* Fri Apr 16 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Conectiva Linux 3.0 server edition

* Wed Mar 31 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Conectiva Linux 3.0 spanish edition

* Wed Dec 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Conectiva Linux 3.0

%install
mkdir -p $RPM_BUILD_ROOT/etc
echo "Conectiva Linux 4.0" > $RPM_BUILD_ROOT/etc/versão-conectiva

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0644,root,root) /etc/versão-conectiva
