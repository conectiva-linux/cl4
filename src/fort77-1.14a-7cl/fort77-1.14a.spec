Summary: driver for f2c
Summary(pt_BR): Driver para f2c
Summary(es): Driver para f2c
Name: fort77
Version: 1.14a
Release: 7cl
Copyright: public domain
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source: http://metalab.unc.edu:/pub/Linux/devel/lang/fortran/fort77-1.14a.tar.gz
Patch: fort77-nowarn.patch
Requires: f2c
Buildroot: /var/tmp/f2c-root
Summary(de): Treiber für f2c
Summary(fr): Pilote pour f2c.
Summary(tr): f2c için sürücü

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 17 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Wed Oct 21 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr


* Tue Oct 28 1997 Michael Fulbright <msf@redhat.com>

- fixed slightly so as to not split (harmless) Perl warning messages

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>

- built against glibc

%description
This is the driver for f2c, a fortran to C translator.

%description -l pt_BR
Este é o driver para f2c, um tradutor de fortran para C.

%description -l es
Este es el driver para f2c, un traductor de fortran para C.

%description -l de
Dies ist der Treiber für f2c, einen Fortran->C-Übersetzer. 

%description -l fr
Pilote pour f2c, un traducteur Fortran vers C.

%description -l tr
f2c isimli Fortran-C çeviricisinin sürücü betiði

%prep
%setup
%patch -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
install -m 755 fort77 $RPM_BUILD_ROOT/usr/bin
install -m 644 fort77.1 $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT
 

%files
/usr/bin/fort77
/usr/man/man1/fort77.1
