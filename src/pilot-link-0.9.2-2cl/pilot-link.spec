Summary: Pilot Link - USR Pilot to Unix transfer utilities.
Summary(pt_BR): Utilitários de transferência de dados entre Unix e o Pilot
Summary(es): Utilitarios de transferencia de datos entre Unix y Pilot
Name: pilot-link
Version: 0.9.2
Release: 2cl
Copyright: GPL/LGPL
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
Source:	ftp://ryeham.ee.ryerson.ca/pub/PalmOS/%{name}.%{version}.tar.bz2
Patch0:	pilot-link-perl-install.patch
Patch1:	pilot-link.perl.patch
Patch2:	pilot-link-pixdir.patch
Patch3:	ftp://ryeham.ee.ryerson.ca/pub/PalmOS/pilot-link.sync-ldif.patch
BuildPrereq: libstdc++
BuildPrereq: ncurses-devel
BuildPrereq: readline-devel
BuildPrereq: tcl
BuildPrereq: tk
BuildPrereq: XFree86-devel
BuildRoot: /tmp/%{name}-%{version}-root

%description
This suite of tools allows you to upload and download programs
and data files between a *nix machine and the USR Pilot.  It has
a few extra utils that will allow for things like syncing the
Pilot's calendar app with Ical.  Note that you might still need
to consult the sources for pilot-link if you would like the
Python, Tcl, or Perl bindings.

%description -l pt_BR
Este conjunto de ferramentas permite transferir programas e 
dados entre máquinas *nix e o Palm Pilot. Alguns utilitários
extras permitem coisas como sincronizar dados entre o calendário
do Pilot e o Ical. 

%description -l es
Este conjunto de herramientas permite transferir programas y datos
entre máquinas *nix y el Palm Pilot. Algunos utilitarios extras
permiten cosas como sincronizar datos entre el calendario del Pilot
y el Ical.

%package devel
Summary: Pilot development header files
Summary(pt_BR): Arquivos de inclusão para o desenvolvimento de programas
Summary(es): Archivos de inclusión para el desarrollo de programas
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: %{name} = %{version}

%description devel
This package contains the development headers that are used
to build the pilot-link package.

%description -l pt_BR devel
Este pacote contém os arquivos de inclusão necessários
para gerar aplicações Pilot.

%description -l es devel
Este paquete contiene los archivos de inclusión necesarios
para crear aplicaciones Pilot.

%package static
Summary: Pilot link static libraries
Summary(pt_BR): Bibliotecas estáticas necessárias para gerar aplicações Pilot.
Summary(es): Bibliotecas estáticas necesarias para crear aplicaciones Pilot.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: %{name}-devel = %{version}

%description static
Pilot link static libraries.

%description -l pt_BR static
Este pacote contém as bibliotecas estáticas necessárias
para gerar aplicações Pilot.

%description -l es static
Este paquete contiene las bibliotecas estáticas necesarias
para crear aplicaciones Pilot.

%prep 
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf
%ifarch armv4l
libtoolize --copy --force
%endif

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates" \
./configure %{_target} --prefix=/usr

make LIBDIR="/usr/share"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/share

make install \
	prefix=$RPM_BUILD_ROOT/usr

mv $RPM_BUILD_ROOT/usr/lib/pilot-link $RPM_BUILD_ROOT/usr/share

strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/* ChangeLog README*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/lib/lib*.so.*.*
%attr(755,root,root) /usr/bin/*
/usr/share/pilot-link
/usr/man/man[17]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so
/usr/include/*

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed vendor

* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun May  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.2-2]
- now package is FHS 2.0 compiliat.

* Mon Apr 26 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.2-1]
- added "-fno-rtti -fno-exceptions -fno-implicit-templates" c++ optimization
  options,
- added patch with sync-ldif (application which sync the PalmPilot address
  book with a Netscape Communicator address book LDIF file,
- addded gzipping man pages and %doc,
- /sbin/ldconfig now is runed as -p parameter in %post, %postun,
- added Group(pl),
- added "BuildPrereq: glibc-devel".

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- added missing files from devel subpackage

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- move /usr/lib/pix to /usr/lib/pilot-link (dumb, BAD name)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Thu Jan 21 1999 Bill Nottingham <notting@redhat.com>
- arm fix

* Fri Sep 24 1998 Michael Maher <mike@redhat.com>
- cleaned up spec file, updated package

* Tue May 19 1998 Michael Maher <mike@redhat.com>
- updated rpm

* Thu Jan 29 1998 Otto Hammersmith <otto@redhat.com>
- added changelog
- updated to 0.8.9
- removed explicit requires for /usr/bin/perl
