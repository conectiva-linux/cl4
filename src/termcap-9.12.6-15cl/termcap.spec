Summary: The terminal feature database used by certain applications.
Summary(pt_BR): Arquivo termcap
Summary(es): Archivo termcap
Name: termcap
Version: 9.12.6
Release: 15cl
Copyright: none
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source0: http://www.ccil.org/~esr/terminfo/termtypes.tc.gz
Patch0: termcap-linuxlat.patch
Patch1: termcap-sparc.patch

# XXX termcap used to be noarch but that is impossible with per-arch patches
%ifarch sparc
Obsoletes: termfiles_sparc
Provides: termfiles_sparc
%endif

BuildRoot: /var/tmp/%{name}-root

%description
The termcap package provides the /etc/termcap file.  /etc/termcap is
a database which defines the capabilities of various terminals and
terminal emulators.  Certain programs use the /etc/termcap file to
access various features of terminals (the bell, colors, and graphics,
etc.).

%description -l pt_BR
O arquivo /etc/termcap é um banco de dados que define as capacidades
de vários terminais e emuladores de terminais. Programas usam
/etc/termcap para acessar várias características de terminais como
o beep, cores, e gráficos.

%description -l es
El archivo /etc/termcap es un banco de datos que define las
capacidades de varios terminales y emuladores de terminales. Los
programas usan /etc/termcap para acceder a varias características
de terminales como el beep, colores, y gráficos.

%prep
mkdir -p $RPM_BUILD_ROOT/etc
zcat $RPM_SOURCE_DIR/termtypes.tc.gz > $RPM_BUILD_ROOT/etc/termcap
(cd $RPM_BUILD_ROOT/etc;
%patch0 -p0
%ifarch sparc
%patch1 -p0
%endif
)
chmod 644 $RPM_BUILD_ROOT/etc/termcap

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config /etc/termcap

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 29 1999 Jeff Johnson <jbj@redhat.com>
- termcap used to be noarch but that is impossible with per-arch patches

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 14)

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- merge sparc console termcap (from termfiles_sparc).

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- rebuild for glibc 2.1

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- added linux-lat entry
- build rooted

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
