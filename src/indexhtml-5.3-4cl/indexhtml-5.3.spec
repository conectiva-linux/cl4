Name: indexhtml
Summary: Conectiva html index page
Summary(pt_BR): Página índice html da Conectiva
Summary(es): Página índice html de la Conectiva
Version: 5.3
Release: 4cl
Source: indexhtml-5.3.tar.bz2
Copyright: distributable
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
BuildArchitectures: noarch
BuildRoot: /var/tmp/index-html

%description
Conectiva html index page

%description -l pt_BR
Página índice html da Conectiva

%description -l es
Página índice html de la Conectiva

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 30 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- included index-es.html. Renamed index.html to index-pt.html.
- BuildRoot and %post script

* Mon Nov 30 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- 5.2 com alterações na página

* Wed May  6 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- início

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/doc/HTML
cp -p * $RPM_BUILD_ROOT/usr/doc/HTML/
ln -sf index-pt.html $RPM_BUILD_ROOT/usr/doc/HTML/index.html

%post
i=${LANG%%_*}
[ -n "$i" ] && ln -sf index-$i.html $RPM_BUILD_ROOT/usr/doc/HTML/index.html
exit 0

%files
/usr/doc/HTML/index-pt.html
/usr/doc/HTML/index-es.html
%verify(not md5 size mtime link) %config(missingok) /usr/doc/HTML/index.html
/usr/doc/HTML/logo.jpg
