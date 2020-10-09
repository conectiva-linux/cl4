Copyright: GPL
Source: manual-conectiva-linux-3.0.tar.bz2
Source800: wmconfig.i18n.tgz
Release: 9cl
Name: manual-conectiva-linux
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Version: 3.0
Summary: The Conectiva Linux User's Guide
Summary(pt_BR): O manual do usu�rio do Conectiva Linux
Summary(es): El manual de usuario del Conectiva Linux
BuildArchitectures: noarch
BuildRoot: /tmp/marumbi-manual
Obsoletes: crhl-marumbi-manual
Serial: 1

%changelog
* Tue May 25 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Modified the wmconfig file so now it works with windowmaker

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Tue Dec 08 1998 aur�lio marinho jargas <aurelio@conectiva.com> 
- revis�o inicial de todo o manual

* Sun Dec 06 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Atualizado para a vers�o 3.0 (3.0)
- Serial: 1, pois a vers�o anterior era 5.0 :(

%description
This is a local copy of the HTML version of the
Conectiva Linux User's Manual. The online copy can be
found at http://www.conectiva.com/manual.

%description -l pt_BR
Esta � uma c�pia local da vers�o HTML do Manual do Usu�rio
do Conectiva Linux. A c�pia on-line pode ser encontrada em
http://www.conectiva.com.br/manual.

%description -l es
Esta es una copia local de la versi�n HTML del Manual del Usuario
de Conectiva Linux. La copia on-line puede ser encontrada en
http://www.conectiva.com.br/manual.

%prep
%setup -n manual-conectiva-linux

%build
 
%install
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc *
/etc/X11/wmconfig/manual-conectiva-linux
