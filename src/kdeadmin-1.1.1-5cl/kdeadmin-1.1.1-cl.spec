%define kdeprefix /usr
%define version 1.1.1
%define kderelease 5cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source

%define conectiva versão-conectiva >= 4.0
%define qtversion  qt >= 1.42

%define kdename kdeadmin
%define kpackage kpackage-1.3.2
Name: %{kdename}
Summary: K Desktop Environment - System Administration Tools
Summary(pt_BR): K Desktop Environment - ferramentas administrativas
Summary(es): K Desktop Environment - herramientas administrativas
Version: %{version}
Release: %{kderelease}
Source0: ftp://ftp.kde.org:/pub/kde/%{sourcedir}/%{kdename}-%{version}.tar.bz2
Source1: ftp://ftp.uwa.edu.au/pub/k/%{kpackage}.tar.bz2
Source2: kpackage-pt_BR.po
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
BuildRoot: /var/tmp/%{kdename}-buildroot
Copyright: GPL
Requires: %{qtversion}
Requires: %{conectiva}
Requires: kdesupport
Patch0: kdeadmin-1.1-uid.patch
Patch1: kpackage-1.3.2-pt_BR.patch
Prefix: %{kdeprefix}
Obsoletes: kde-admin kpackage

%description
System Administration tools for the K Desktop Environment.

Included with this package are: 
kdat (tape backup); ksysv (sysV init editor)
kpackage (manage rpms)

%description -l pt_BR
Ferramentas administrativas para o KDE.

Incluídos neste pacote:

ksysv: editor dos arquivos de iniciação sysV kuser: ferramenta de
administração de usuários

%description -l es
Herramientas administrativas para KDE.  Incluidos en este paquete:
ksysv: editor de los archivos de iniciación sysV kuser: herramienta
de gestión de usuarios

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n kdeadmin-%{version}

%patch0 -p1
%setup -q  -T  -n %{kpackage} -b 1
%patch1 -p1 -b .pt_BR

%build
[ "$LINGUAS" ] && unset LINGUAS
export KDEDIR=%{kdeprefix}
cd $RPM_BUILD_DIR/%{kdename}-%{version}
CFLAGS=$RPM_OPT_FLAGS CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti" \
    ./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--with-pam \
    --with-private-groups
make 

cd $RPM_BUILD_DIR/%{kpackage}

cp $RPM_SOURCE_DIR/kpackage-pt_BR.po $RPM_BUILD_DIR/%{kpackage}/po/pt_BR.po

autoconf
CFLAGS=$RPM_OPT_FLAGS CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti" \
    ./configure \
    --prefix=%{kdeprefix} \
    --with-install-root=$RPM_BUILD_ROOT
make 

%install
cd $RPM_BUILD_DIR/%{kdename}-%{version}
make install-strip

cd $RPM_BUILD_DIR/%{kpackage}
make install-strip

cd $RPM_BUILD_ROOT
find . -type d | grep -v "\/usr\/share\/locale" | \
	 sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
	-e '/\/config\//s|^|%config|' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{kdename}
rm -rf $RPM_BUILD_DIR/%{kdename}-%{version} $RPM_BUILD_DIR/%{kpackage}

%files -f ../file.list.%{kdename}

%changelog
* Tue Jun 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to kpackage

* Mon Jun 28 1999 Marcelo Tosatti <marcelo@conectiva.com>
- updated 

* Sat Jun 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated kpackage from 1.2.1 to 1.3.2
- requires versão-conectiva >= 4.0 (glibc 2.1, etc)
- fixed specfile wrt rpm 3.0

* Fri May 07 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- kuser omitted from package
- unset LINGUAS
- added kpackage
- files in KDEDIR/share/applnk no longer treated as %config files
- updated to 1.1.1

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- removed post, as what it did is now done in kdestart
- removed %dir /usr/share/locale from %filelist

* Thu Feb 25 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Compiled with -fno-exceptions -fno-rtti
- Added postinstall script for kappfinder and wmconfig

* Mon Jan 18 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- added pt_BR translations

* Thu Jan 07 1999 Preston Brown <pbrown@redhat.com>
- re-merged in updates from Duncan Haldane, /opt/kde --> /usr
