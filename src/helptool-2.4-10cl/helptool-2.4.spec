Summary: Simple Help File Searching Tool
Summary(pt_BR): Ferramenta para pesquisar arquivos de ajuda
Summary(es): Herramienta para pesquisar archivos de ayuda
Name: helptool
Version: 2.4
Release: 10cl
Copyright: GPL
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Source: helptool-2.4.tar.gz
Source800: wmconfig.i18n.tgz
Patch0: helptool-2.4-nobr.patch
Requires: tcl tk perl
BuildArchitectures: noarch
BuildRoot: /var/tmp/helptool-root

%description
The help tool provides a unified graphical interface for searching through
many of the help sources available, including man pages and GNU texinfo 
documents.

%description -l pt_BR
Esta ferramenta oferece uma interface gráfica única para procurar
ajuda através de várias fontes disponíveis, incluindo páginas de
manuais e documentos texinfo GNU.

%description -l es
Esta herramienta nos ofrece una interface gráfica única para buscar
ayuda a través de varias fuentes disponibles, incluyendo páginas
de manuales y documentos texinfo GNU.

%prep
%setup -q
%patch0 -p1 -b .nobr

%build
make

%install
rm -rf $RPM_BUILD_ROOT

make	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLBIN="install -m755" INSTALLDATA="install -m644" \
	install

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/helpme
/usr/bin/helptool
/usr/lib/rhs/control-panel/helptool.init
/usr/lib/rhs/control-panel/helptool.xpm
/etc/X11/wmconfig/helptool

%changelog
* Mon Jun 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt to remove TkStep-replace dependencies

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- can't have paths in wmconfig files

* Tue Oct 28 1997 Otto Hammersmith <otto@redhat.com>
- fixed icon filename in fstool.init

* Fri Oct 24 1997 Michael K. Johnson <johnsonm@redhat.com>
- xpm icon and wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Fri Apr 18 1997 Michael K. Johnson <johnsonm@redhat.com>
- helptool 2.3:
-   Fixed broken catch statement
-   Added perl requirement for helpme
