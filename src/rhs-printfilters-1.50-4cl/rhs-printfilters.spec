Summary: Red Hat print filters, for use with the printtool.
Summary(pt_BR): Sistema de filtro de impressão Red Hat
Summary(es): Sistema de filtro de impresión Red Hat
Name: rhs-printfilters
Version: 1.50
Release: 4cl
Copyright: GPL
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Source: rhs-printfilters-%{PACKAGE_VERSION}.tar.gz
Requires: mpage >= 2.4, lpr >= 0.17, ghostscript >= 5.10, findutils >= 4.1-23
Buildroot: /var/tmp/rhs-printfilters-root
#
# these conflcts exists because Dr Mike changes the location of the filters
#
Conflicts: libgr-progs < 2.0.9-7

%description
The rhs-printfilters package contains a set of print filters which
are primarily meant to be used with the Red Hat printtool.  These
print filters provide an easy way for users to handle printing
numerous file formats.

%description -l pt_BR
O sistema de filtros de impressão Red Hat oferece uma maneira fácil
de manipular a impressão de vários formatos de arquivos. Feito
primariamente para ser usado em conjunto com o RedHat printtool.

%description -l es
El sistema de filtros de impresión Red Hat nos ofrece una manera
fácil de manipular la impresión de varios formatos de archivos. Se
lo hizo, primeramente, para ser usado en conjunto con el RedHat
printtool.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p INSTALL_DIR=$RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters
make INSTALLBIN="install -m0755" INSTALLDATA="install -m0644" \
	INSTALL_DIR=$RPM_BUILD_ROOT install

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%dir /usr/lib/rhs/rhs-printfilters
/usr/lib/rhs/rhs-printfilters/asc-to-printer.fpi
/usr/lib/rhs/rhs-printfilters/asc-to-ps.fpi
/usr/lib/rhs/rhs-printfilters/general.cfg.in
/usr/lib/rhs/rhs-printfilters/master-filter
/usr/lib/rhs/rhs-printfilters/postscript.cfg.in
/usr/lib/rhs/rhs-printfilters/printerdb
/usr/lib/rhs/rhs-printfilters/ps-to-printer.fpi
/usr/lib/rhs/rhs-printfilters/rewindstdin
/usr/lib/rhs/rhs-printfilters/rpm-to-asc.fpi
/usr/lib/rhs/rhs-printfilters/ncpprint
/usr/lib/rhs/rhs-printfilters/smbprint
/usr/lib/rhs/rhs-printfilters/testpage.asc
/usr/lib/rhs/rhs-printfilters/testpage.ps
/usr/lib/rhs/rhs-printfilters/testpage-a4.ps
/usr/lib/rhs/rhs-printfilters/textonly.cfg.in

%changelog
* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- returns to old Group

* Fri Mar 19 1999 Bill Nottingham <notting@redhat.com>
- remove some obsolete text

* Mon Feb  8 1999 Bill Nottingham <notting@redhat.com>
- uniprint support

* Tue Dec 29 1998 Bill Nottingham <notting@redhat.com>
- add workaround for Adobe(!) postscript driver

* Mon Dec 28 1998 Bill Nottingham <notting@redhat.com>
- remove 1bpp from cdj-based drivers, 'cos it's broken.

* Wed Nov 18 1998 Bill Nottingham <notting@redhat.com>
- add workgroup support to smbprint, fix quoting issues

* Wed Sep 30 1998 Bill Nottingham <notting@redhat.com>
- fix typo in ncpprint

* Wed Sep 15 1998 Bill Nottingham <notting@redhat.com>
- Added ncpprint to %files section (oops!)

* Thu Sep  2 1998 Bill Nottingham <notting@redhat.com>
- Added NCP printing support

* Tue Jun 30 1998 Michael Maher <mike@redhat.com>
- Fixed BUG 703,  added findutils dependecy.
- Added buildroot.

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- Fixed printerdb to include 300x300 resolution for LaserJet 4 models
- Restored troff file handling now troff fpi is 'safe'

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- Fixed master-filter to NOT handle troff files automatically

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Wed Apr 23 1997 Michael Fulbright <msf@redhat.com>
- Fixed problem with asc-to-printer.fpi not handling cr/lf trans correct

* Fri Apr 18 1997 Michael Fulbright <msf@redhat.com>
- fixed up Canon 600/4000 printerdb def
- added some HP Deskjets which I know work

* Thu Apr 10 1997 Michael Fulbright <msf@redhat.com>
- Added requirement that gs is installed. Pretty useless w/o it if
  you print anything interesting.

* Fri Mar 13 1997 Michael Fulbright <msf@redhat.com>
- Added conflicts so that packages with old filter loc won't hurt us.
- Moved to version 1.2.
- Added mpage support to allow nup printing.

* Wed Mar 13 1997 Michael Fulbright <msf@redhat.com>
- Added a DeskJet500Mono driver which links to the gs driver djet500.
- Added a A4 paper size test page.
- Fixed Makefile to build .ps test pages from the .fig files.

* Mon Mar 10 1997 Michael Fulbright <msf@redhat.com>
- Split filters off from printtool into this package .
