%define version 0.9.9
%define name klyx
Name: %{name}
Summary: KLyX - a document processor for the K Desktop Environment
Summary(pt_BR): Processador de textos para o KDE
Summary(es): Procesador de textos para KDE
Version: %{version}
Release: 6cl
Source0: ftp.kde.org:/pub/kde/unstable/apps/%{name}-%{version}.tar.bz2
Source1: klyx.kdelnk
Source2: klyx-pt_BR.po
Patch0: klyx-cedilha.patch
Patch1: klyx-0.9.9-pt_BR.patch
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
BuildRoot: /tmp/rpmbuild_%{name}
Copyright: GPL
Requires: qt >= 1.33 

%description
A document processor for the K Desktop Environment that is based
on LyX and uses LaTeX as its background formatting engine.

%description -l pt_BR
Processador de textos para o KDE baseado no LyX, usa LaTeX
como base.

%description -l es
Procesador de textos para KDE basado en LyX, usa LaTeX como base.

%description -l it
KLyX è un word processor per il KDE basato su LyX; utilizza LaTeX
come motore di formattazione.

%description -l de
Ein Dokumentenverarbeitungssystem für den KDE Dsktop basierend auf LyX.
Verwendet LaTeX als Hintergrundsatzsystem.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n klyx-%{version}
%patch0
%patch1 -p1 -b .pt_BR

%build
cp $RPM_SOURCE_DIR/klyx-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
export KDEDIR=/usr
autoconf
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti" ./configure --prefix=/usr --with-install-root=$RPM_BUILD_ROOT
make

%install
make install-strip

install -d $RPM_BUILD_ROOT/usr/share/applnk/Applications
install $RPM_SOURCE_DIR/klyx.kdelnk \
	$RPM_BUILD_ROOT/usr/share/applnk/Applications

install -d $RPM_BUILD_ROOT/usr/share/icons/
install $RPM_BUILD_DIR/klyx-%{version}/pics/lyx.xpm \
	$RPM_BUILD_ROOT/usr/share/icons/

ln -s portuges.kmap $RPM_BUILD_ROOT/usr/share/apps/klyx/kbd/brazil.kmap

cd $RPM_BUILD_ROOT
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}

%dir %attr(-,root,root) /usr/share/apps/klyx/bind 
%dir %attr(-,root,root) /usr/share/apps/klyx/clipart
%dir %attr(-,root,root) /usr/share/apps/klyx/doc
%dir %attr(-,root,root) /usr/share/apps/klyx/examples
%dir %attr(-,root,root) /usr/share/apps/klyx/kbd
%dir %attr(-,root,root) /usr/share/apps/klyx/layouts
%dir %attr(-,root,root) /usr/share/apps/klyx/pics
%dir %attr(-,root,root) /usr/share/apps/klyx/templates
%dir %attr(-,root,root) /usr/share/apps/klyx/tex
%dir %attr(-,root,root) /usr/share/apps/klyx

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
rm -f $RPM_BUILD_DIR/file.list.%{name}

%changelog
* Tue Jun 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 10 1999 Conectiva <dist@conectiva.com>
- Recompiled against qt 1.44 and KDE 1.1.1

* Fri Mar 12 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 12 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- cedilla patch
- Added klyx entry to the KDE desktop (kdelnk + icon)
