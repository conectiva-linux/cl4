%define kdeprefix /usr
%define version 1.1.1
%define kderelease 3cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source
%define utilsdir stable/1.1.1/apps/utils

%define conectiva versão-conectiva >= 4.0
%define qtversion qt >= 1.42

%define kdename kdeutils
%define kclock kclock-0.6
%define kdf kdf-0.5.1
Name: %{kdename}
Summary: K Desktop Environment - Utilities
Summary(pt_BR): KDE - Utilitários
Summary(es): KDE - Utilitarios
Version: %{version}
Release: %{kderelease}
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://ftp.kde.org:/pub/kde/%{sourcedir}/%{kdename}-%{version}.tar.bz2
Source1: ftp://ftp.kde.org/pub/kde/%{utilsdir}/%{kclock}.tar.bz2
Source2: ftp://ftp.kde.org/pub/kde/%{utilsdir}/%{kdf}.tar.bz2
Patch: %{kclock}-config.patch
Patch1: %{kclock}.patch
Patch2: %{kdf}.patch
Patch3: %{kdf}-install-root.patch
BuildRoot: /var/tmp/%{kdename}-buildroot
Copyright: GPL/Artistic
Requires: %{qtversion} %{conectiva} kdebase
Prefix: %{kdeprefix}
Obsoletes: kde-utils kde-pim

%description
Utilities for the K Desktop Environment.
Includes: ark (tar/gzip archive  manager); kab (address book); karm (personal
time tracker); kcalc (scientific calculator); kedit (simple text editor);
kfloppy (floppy formatting tool); khexedit (hex editor); kjots (note taker);
klipper (clipboard tool); kljettool(HP printer configuration tool); klpq
(print queue manager) knotes (post-it notes for the desktop); kpm (process
manager); kwrite (improved text editor). %{kclock} and %{kdf}
(not in the kdeutils collection yet) have also been added.

%description -l pt_BR
Utilitários para o KDE

Programas disponíveis neste pacote: karm: controle de tempo
pessoal kcalc: calculadora científica kedit: editor de textos
simples kfloppy: ferramenta de formatação de disquetes khexedit:
editor hexadecimal kjots: bloco de notas kljettool: ferramenta de
configuração de impressoras HP knotes: recados para colar no ambiente
gráfico kzip: ferramenta de manipulação de arquivos compactados

%description -l es
Utilitarios para KDE Programas disponibles en este paquete: karm:
control de tiempo personal kcalc: calculadora científica kedit:
editor de textos sencillo kfloppy: herramienta de formatear
disquetes khexedit: editor hexadecimal kjots: bloque de notas
kljettool: herramienta de configuración de impresoras HP knotes:
recados para coger en el ambiente gráfico kzip: herramienta de
manejo de archivos comprimidos

%{kclock} e %{kdf}


%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{kdename}-%{version}

%setup -q  -T  -n %{kclock} -b 1
# update kclock's config.sub, config.guess
%patch -p1
%patch1 -p1

%setup -q  -T  -n %{kdf} -b 2
%patch2 -p1
#fix install_root lack
%patch3 -p1

%build
export KDEDIR=%{kdeprefix}
[ "$LINGUAS" ] && unset LINGUAS

#compile kdeutils
cd $RPM_BUILD_DIR/%{kdename}-%{version}
CFLAGS=$RPM_OPT_FLAGS CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti" \
    ./configure --prefix=%{kdeprefix} --with-install-root=$RPM_BUILD_ROOT
make

#compile kclock
cd $RPM_BUILD_DIR/%{kclock}
CFLAGS=$RPM_OPT_FLAGS CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti" \
    ./configure \
    --prefix=%{kdeprefix} 
make 

#compile kdf
cd $RPM_BUILD_DIR/%{kdf}
CFLAGS=$RPM_OPT_FLAGS CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti" \
    ./configure \
    --prefix=%{kdeprefix} \
    --with-install-root=$RPM_BUILD_ROOT
make


%install
cd $RPM_BUILD_DIR/%{kdename}-%{version}
make install-strip

#add kdf
cd $RPM_BUILD_DIR/%{kdf}
make prefix=%{kdeprefix} install-strip

#add kclock
cd $RPM_BUILD_DIR/%{kclock}
make prefix=$RPM_BUILD_ROOT/%{kdeprefix} install-strip

#file list
cd $RPM_BUILD_ROOT
find . -type d | grep -v "\/usr\/share\/locale\|\/usr/bin" | \
	sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
	-e '/\/config\//s|^|%config|' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{kdename}

%files -f ../file.list.%{kdename}

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed specfile wrt rpm 3.0

* Thu May 06 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- fix kdf/kclock lack of install-root
- files in KDEDIR/share/applnk no longer treated as %config files
- Added kclock and kdf
- Updated to 1.1.1
- Merged with kde team's specfile

* Sat Apr 03 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Obsoletes kde-utils & kde-pim from parolin

* Thu Mar 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed dependencies
- unset LINGUAS

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- %dir /usr/share/locale removed from %filelist

* Fri Feb 26 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Compiled with -fno-exceptions -fno-rtti
- Added postinstall script for kappfinder and wmconfig

* Mon Jan 18 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added pt_BR translations

* Wed Jan 06 1999 Preston Brown <pbrown@redhat.com>
- re-merged in changes from Duncan Haldane
