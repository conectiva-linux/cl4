%define version 1.1.1
%define name kdehelp-pt_BR
Name: kdehelp-pt_BR
Summary: K Desktop Environment - Documentation (Brazilian Portuguese)
Summary(pt_BR): Documentação em Português (Brasil) para o KDE.
Summary(es): Documentación en Portugués (de Brasil) para KDE.
Version: %{version}
Release: 3cl
Source: %{name}-%{version}.tar.bz2
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
BuildRoot: /var/tmp/realhot_%{name}
Copyright: GPL
BuildArchitectures: noarch

%description
Brasilian portuguese translation of the documentation for the K Desktop
Enviroment.

%description -l pt_BR
Tradução para português (variante Brasil) da documentação do KDE.

%description -l es
Traducción de la documentación del K Desktop Enviroment para el
portugués de Brasil.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{name}-%{version}

%install
export KDEDIR=/usr
mkdir -p $RPM_BUILD_ROOT/$KDEDIR/share/doc/HTML/pt_BR
cp -Rf * $RPM_BUILD_ROOT/$KDEDIR/share/doc/HTML/pt_BR

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- turned this a noarch package

* Mon May 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- updated to 1.1.1

* Sat Mar 27 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to latest tarball from epx

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 03 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled package for KDE 1.1
- Changed default path to /usr, instead of /opt/kde

* Sat Oct 31 1998 Rodrigo Parra Novo <rodarvus@conectiva.com>
- First version of package
- added pt_BR translations
