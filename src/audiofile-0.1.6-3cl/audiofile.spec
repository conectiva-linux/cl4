%define  ver     0.1.6
%define  rel     3cl
%define  prefix  /usr

Summary: Library to handle various audio file formats.
Summary(pt_BR): Biblioteca para manipular vários formatos de arquivos de áudio.
Summary(es): Biblioteca para manipulación de varios archivos de sonido.
Name: audiofile
Version: %ver
Release: %rel
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
# was .gz
Source: ftp://ftp.gnome.org/pub/GNOME/audiofile/audiofile-%{PACKAGE_VERSION}.tar.bz2
BuildRoot:/var/tmp/audiofile-%{PACKAGE_VERSION}-root
Docdir: %{prefix}/doc

%description
Library to handle various audio file formats.
Used by the esound daemon.

%description -l pt_BR
Biblioteca para manipular vários formatos de arquivos de áudio.

%description -l es
Biblioteca para manipulación de varios archivos de sonido.

%package devel
Summary: Libraries, includes and other files to develop audiofile applications.
Summary(pt_BR): Bibliotecas, arquivos de inclusão e outros arquivos para desenvolver aplicativos audiofile
Summary(es): Bibliotecas, archivos de inclusión y otros archivos para el desarrollo de aplicaciones audiofile.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
Libraries, include files and other resources you can use
to develop audiofile applications.

%description -l pt_BR devel
Bibliotecas, arquivos de inclusão e outros arquivos para desenvolver
aplicativos audiofile.

%description -l es devel
Bibliotecas, archivos de inclusión y otros archivos para el desarrollo
de aplicaciones audiofile.

%prep
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
./configure --prefix=%prefix
make

%install

mkdir -p $RPM_BUILD_ROOT

#
# makefile is broken, sets exec_prefix explicitely.
#
make exec_prefix=$RPM_BUILD_ROOT/%{prefix} prefix=$RPM_BUILD_ROOT/%{prefix} install 

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- added optimization flags to spec file

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- Version 0.1.6

* Sun Feb 21 1999 Michael Fulbright <drmike@redhat.com>
- Removed libtoolize from %build

* Wed Feb 3 1999 Jonathan Blandfor <jrb@redhat.com>
- Newer version with bug fix.  Upped release.

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- integrating into rawhide release at GNOME freeze

* Fri Nov 20 1998 Michael Fulbright <drmike@redhat.com>
- First try at a spec file

%files
%defattr(-, root, root)
%doc COPYING TODO README ChangeLog LICENSE docs
%{prefix}/bin/*
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-, root, root)
%{prefix}/lib/lib*.so
%{prefix}/lib/*.a
%{prefix}/include/*
