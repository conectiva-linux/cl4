Summary: Translations for all initscritps in /etc/rc.d/init.d
Summary(pt_BR): Traduções para todos os initscripts em /etc/rc.d/init.d
Summary(es): Traducciones de todos los initscripts en /etc/rc.d/init.d
Name: initscripts-translations
Version: 4.19
Release: 3cl
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: initscripts-translations-%{version}-%{release}.tar.gz
Copyright: GPL
BuildRoot: /var/tmp/initscripts-translations
BuildArch: noarch

%description
Translations for all initscritps in /etc/rc.d/init.d

%description -l pt_BR
Traduções para todos os initscripts em /etc/rc.d/init.d

%description -l es
Traducciones de todos los initscripts en /etc/rc.d/init.d

%prep
%setup -n initscripts-translations-%{version}-%{release}

%build
make

%install
make PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/share/locale/*/LC_MESSAGES/initscripts.mo

%changelog
* Sat Jun 26 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- new translations
- using release number in tgz name

* Mon May 31 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- new translations for initscripts 4.19

* Mon Mar 29 1999 Conectiva <dist@conectiva.com>
- changed po

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 17 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- spanish translations added

* Mon Mar 15 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- ispell...

* Mon Mar 15 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- /etc/rc.d/rc.* included

* Sun Mar 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- network-scripts included

* Sat Mar 13 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initial version
