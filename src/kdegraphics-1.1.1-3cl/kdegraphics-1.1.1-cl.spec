%define kdeprefix /usr
%define version 1.1.1
%define kderelease 3cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source/bz2

%define conectiva versão-conectiva >= 4.0
%define qtversion  qt >= 1.42

%define kdename kdegraphics
Name: %{kdename}
Summary: K Desktop Environment - Graphics Applications
Summary(pt_BR): K Desktop Environment - Aplicações gráficas
Summary(es): K Desktop Environment - aplicaciones gráficas
Version: %{version}
Release: %{kderelease}
Source: ftp://ftp.kde.org:/pub/kde/%{sourcedir}/%{kdename}-%{version}.tar.bz2
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
BuildRoot: /var/tmp/%{kdename}-buildroot
Copyright: GPL
Requires: %{qtversion} %{conectiva}
Prefix: %{kdeprefix}
# present in parolin
Obsoletes: kde-graphics

%description
Graphics applications for the K Desktop Environment. 

Includes: kdvi (displays TeX .dvi files); kfax (displays fax 
files); kfract (a fractal generator); kghostview (displays postscript files);
kiconedit (icon editor); kpaint (a simple drawing program); ksnapshot (screen
capture utility); kview (image viewer for GIF, JPEG, TIFF, etc.).

%description -l pt_BR
Aplicações gráficas para o KDE.

Incluídos neste pacote:

kdvi: visualiza arquivos TeX's independentes de dispositivo
(.dvi) kfax: visualiza arquivos de fax kfract: gerador de fractal
kghostview: visualiza arquivos postscript (.ps) kpaint: um programa
simples de desenho kview: visualiza numerosos formatos de arquivos
gráficos

%description -l es
Aplicaciones gráficas para KDE.  Incluidos en este paquete: kdvi:
visualiza archivos TeX's independientes de dispositivo (.dvi) kfax:
visualiza archivos de fax kfract: creador de fractal kghostview:
visualiza archivos postscript (.ps) kpaint: un programa sencillo
de dibujo kview: visualiza numerosos formatos de archivos gráficos

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{kdename}-%{version}

%build
export KDEDIR=%{kdeprefix}
[ "$LINGUAS" ] && unset LINGUAS
CFLAGS="$RPM_OPT_FLAGS" \
    CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti" ./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT
make 

%install
make install-strip

# This file conflicts with kdeutils-1.1, anyone knows a better solution?
rm -f $RPM_BUILD_ROOT/usr/share/locale/es/LC_MESSAGES/kfract.mo

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

%files -f ../file.list.%{kdename}

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- requires versão-conectiva (glibc 2.1, etc)

* Sat Jun  5 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 04 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed specfile wrt rpm 3.0

* Mon May 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- updated to KDE 1.1.1
- files in KDEDIR/share/applnk no longer treated as %config files

* Sat Apr 03 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Obsoletes kde-graphics from parolin

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- removed %dir /usr/share/locale from %filelist
- removed %post script, kdestart does what it was doing

* Thu Feb 25 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Compiled with -fno-exceptions -fno-rtti
- Added postinstall script for kappfinder and wmconfig

* Tue Jan 19 1999 Conectiva <dist@conectiva.com>
- Added pt_BR translations

* Wed Jan 06 1999 Preston Brown <pbrown@redhat.com>
- re-merged in updates from Duncan Haldane
