%define kdeprefix /usr
%define version 1.1.1
%define kderelease 6cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source

%define conectiva versão-conectiva >= 4.0
%define qtversion qt >= 1.42

%define kdename korganizer
Name: %{kdename}
Summary: KOrganizer - Calendar and Scheduling Program for KDE
Summary(pt_BR): Calendário e agenda para o KDE
Summary(es): Calendario y agenda para KDE
Version: %{version}
Release: %{kderelease}
URL: http://www.kde.org
# was .gz
Source: ftp://ftp.kde.org:/pub/kde/%{sourcedir}/%{kdename}-%{version}.tar.bz2
Patch: korganizer-1.1.1-makefilepo.patch
Copyright: GPL
Group: Applications/Productivity
Group(pt_BR): Aplicações/Produtividade
Group(es): Aplicaciones/Productividad
Buildroot: /var/tmp/korganizer-buildroot
Requires: %{qtversion}
Requires: %{conectiva}
Requires: kdebase
Prefix: %{kdeprefix}

%description
KOrganizer is a complete calendar and scheduling program for KDE.  It allows 
interchange with other calendar applications through the industry-standard 
vCalendar file format.

%description -l pt_BR
O KOrganizer é um programa completo de calendário e agendamento para o KDE.
Permite intercâmbio de informações entre aplicações de calendário através
do formato de arquivo vCalendar, padrão da indústria.

%description -l es
KOrganizer es un programa completo de calendario y agenda para KDE.
Permite intercambio de información entre aplicaciones de calendario
a través del formato de archivo vCalendar, padrón de la industria.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{kdename}-%{version}
%patch -p1

%build
export KDEDIR=%{kdeprefix}
[ "$LINGUAS" ] && unset LINGUAS
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions" \
	./configure --prefix=%{kdeprefix} --with-install-root=$RPM_BUILD_ROOT
make KDEDIR=%{kdeprefix}

%install
export KDEDIR=%{kdeprefix}
make prefix=$RPM_BUILD_ROOT%{kdeprefix} install-strip

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
* Tue Jun 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- fixed spec file wrt to rpm 3.0.2 (sigh)

* Sun Jun 06 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed pot files install, patch sent to Preston Brown

* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 06 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed specfile wrt rpm 3.0

* Mon May 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- updated for KDE 1.1.1

* Thu Mar 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- unset LINGUAS

* Mon Mar 08 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- adapted to Conectiva Linux 3.0
- added pt_BR translations

* Sat Feb 13 1999 <duncan@kde.org>
- files in KDEDIR/share/applnk no longer treated as %config files

* Mon Feb 8 1999 <duncan@kde.org>
- new rpm packaging for KDE-1.1
- relocatable rpms

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- updated file specification to pick up config files as such.
