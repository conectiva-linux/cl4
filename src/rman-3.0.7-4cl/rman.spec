Summary: Converts man pages in *roff format to other formats.
Summary(pt_BR): Converte páginas de manual do formato *roff para outros formatos
Summary(es): Convierte páginas de manual de formato *roff a otros formatos
Name: rman
Version: 3.0.7
Release: 4cl
Copyright: BSD
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
#Source: ftp://ftp.cs.berkeley.edu/ucb/people/phelps/tcltk/%{name}-%{version}.tar.Z
# recompressed with bzip2
Source: ftp://ftp.cs.berkeley.edu/ucb/people/phelps/tcltk/%{name}-%{version}.tar.bz2
Patch: %{name}-%{version}-conectiva.patch
BuildRoot: /tmp/%{name}-%{version}

%description
PolyglotMan (nee RosettaMan) is a filter for UNIX manual pages. It takes
as input man pages for a variety of UNIX flavors and produces as output
a variety of file formats.

%description -l pt_BR
PolyglotMan (antes RosettaMan) é um filtro para páginas de manual. Ele
converte dos formatos *roff para outros formatos, como html e tex.

%description -l es
PolyglotMan (antes RosettaMan) es un filtro para páginas de manual.
Convierte los formatos *roff a otros formatos, como html y tex.

%prep
%setup -q
%patch

%build
make CFLAGS=$RPM_OPT_FLAGS

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}
make	BINDIR=$RPM_BUILD_ROOT/usr/bin \
	MANDIR=$RPM_BUILD_ROOT/usr/man/man1 install

strip $RPM_BUILD_ROOT/usr/bin/rman

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644, root, root, 755)
%doc ANNOUNCE-rman CHANGES README-rman
%attr(755,root,root) /usr/bin/rman
/usr/man/man1/rman.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Dec 11 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 3.0.7

* Fri Dec  4 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- added setlocale()

* Sat Nov 28 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [3.0.6-1]
- New version.
- Many fixes of spec-file
