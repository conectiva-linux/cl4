%define version 2.0.14
Summary: GNU Octave - A numerical matrix mathematics program
Summary(pt_BR): GNU Octave - Um programa para cálculo numérico e matricial
Summary(es): GNU Octave - Un programa para cálculo numérico y matricial
Name: octave
Version: %version
Release: 2cl
Copyright: GNU
Group: Applications/Mathmatics
Group(pt_BR): Aplicações/Matemática
Group(es): Aplicaciones/Matemática
Source: ftp://ftp.che.wisc.edu/pub/octave/octave-%{version}.tar.bz2
Patch: octave-2.0.13-tmprace.patch
URL: http://www.che.wisc.edu/octave/
BuildRoot: /var/tmp/octave-tmp/

%description
GNU Octave - A numerical matrix mathematics program.  Matlab-like
high-level language and interactive environment for numerical
computation.

%description -l pt_BR
GNU Octave - Um programa de cálculo numérico e matricial. Possui
linguagem de alto nível e ambiente interativo para computação
numérica semelhantes ao do Matlab.

%description -l es
GNU Octave - Un programa de cálculo numérico y matricial. Posee
lenguaje de altonivel y ambiente interactivo para computación
numérica, semejantes a los del Matlab.

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 27 1999 Guilherme Manika <gwm@conectiva.com>
- Atualizado para 2.0.14
- spec fixes

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 30 1998 Conectiva <dist@conectiva.com>
- fixed tmp race and strip binaries

* Thu Nov 05 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Thu Jul 02 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild against ncurses 4

%prep
%setup
%patch -p1

%build
OS=`echo $RPM_OS | tr '[A-Z]' '[a-z]'`
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS"   ./configure --prefix=/usr --with-g77 --enable-dl --enable-shared --enable-rpath --enable-lite-kernel --host ${RPM_ARCH}-conectiva-${OS}-gnu
make -j3


%install
rm -fr $RPM_BUILD_ROOT
strip src/octave
make prefix=$RPM_BUILD_ROOT/usr install
gzip -9 $RPM_BUILD_ROOT/usr/info/octave.*
gzip -9 $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -fr $RPM_BUILD_ROOT

%pre
ldconfig

%post
ldconfig

%files
%doc BUGS COPYING NEWS NEWS.1 PROJECTS  README README.Linux 
%doc ChangeLog ChangeLog.1 ROADMAP SENDING-PATCHES THANKS
%doc doc emacs examples
/usr/include/octave*
/usr/share/octave
/usr/libexec/octave
/usr/bin/mkoctfile
/usr/bin/octave*
/usr/lib/octave*
/usr/man/man1/octave.1.gz
/usr/info/octave*
