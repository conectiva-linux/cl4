%define kdeprefix /usr
%define version 3.1b8
%define qtver qt >= 1.42

%define kdename kpilot
Name: %{kdename}
Summary: KPilot - pilot synchronization tools for KDE
Summary(pt_BR): Utilitário KDE para o Palm Pilot
Summary(es): Utilitario KDE para Palm Pilot
Version: %{version}
Release: 6cl
Source: %{kdename}-%{version}.tar.bz2
Patch: kpilot-rh.patch
Copyright: GPL
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
Buildroot: /var/tmp/%{kdename}-buildroot
Requires: %{qtver} kdesupport pilot-link
Prefix: %{kdeprefix}

%description
KPilot allows you to synchronize your PalmPilot with your desktop.  It
allows you to backup and restore the various databases (Addressbook,
ToDo List, Memos, etc.) as well as install applications to the pilot.
Two "conduits" for the third party application KOrganizer are included
which will let you sync your ToDo list and Calendar with that program.

%description -l pt_BR
Utilitário KDE para o Palm Pilot

%description -l es
Utilitario KDE para Palm Pilot

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n kpilot-3.1
%patch -p1 -b .rh

%build
export KDEDIR=%{kdeprefix}
make -f Makefile.cvs
./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check
make CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions" KDEDIR=%{kdeprefix}

%install
export KDEDIR=%{kdeprefix}
make install-strip prefix=$RPM_BUILD_ROOT%{kdeprefix}

cd $RPM_BUILD_ROOT
find . -type d | grep -v "\/usr\/share\/locale" | \
	sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
        $RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
        -e '/\/config\//s|^|%config|' \
        -e '/\/applnk\//s|^|%config|' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{kdename}

%files -f ../file.list.%{kdename}

%changelog
* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with qt 1.44

* Sat Mar 20 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Mar 11 1999 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Mar 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- adapted to Conectiva Linux

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb 08 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 3.1b8

* Tue Jan 19 1999 Preston Brown <pbrown@redhat.com>
- updated for 3.1b7, RPM 3.0.

* Fri Jan 08 1999 Preston Brown <pbrown@redhat.com>
- spec file stolen from korganizer.
