Summary: Finds files on a system via a central database.
Summary(pt_BR): Localiza arquivos em um sistema via um banco de dados central
Summary(es): Finds files on a system via a central database.
Name: slocate
Version: 2.0
Release: 8cl
Copyright: GPL
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
Source: ftp://ftp.mkintraweb.com/pub/linux/slocate/slocate-2.0.tar.gz
Source1: slocate.cron
Source2: slocate-man-pt_BR.tgz
Buildroot: /var/tmp/slocate-root
Prereq: shadow-utils

%description
slocate searches through a central database (updated nightly) for files
which match a given glob pattern. This allows you to quickly find files
anywhere on your system.

%description -l pt_BR
O slocate localiza arquivos em um sistema via um banco de dados central
(Atualizado toda madrugada). Isto permite a você localizar  rapidamente
arquivos em qualquer parte do seu sistema.

%description -l es
slocate searches through a central database (updated nightly) for files
which match a given glob pattern. This allows you to quickly find files
anywhere on your system.

%prep
%setup -q
%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/etc/cron.daily
mkdir -p $RPM_BUILD_ROOT/var/lib/slocate
install -s slocate $RPM_BUILD_ROOT/usr/bin
ln -sf slocate $RPM_BUILD_ROOT/usr/bin/locate
ln -sf slocate $RPM_BUILD_ROOT/usr/bin/updatedb
install slocate.1.linux $RPM_BUILD_ROOT/usr/man/man1/slocate.1
install updatedb.1 $RPM_BUILD_ROOT/usr/man/man1/
gzip -9 $RPM_BUILD_ROOT/usr/man/man1/*
ln -sf slocate.1.gz $RPM_BUILD_ROOT/usr/man/man1/locate.1.gz
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily

mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR
cd $RPM_BUILD_ROOT/usr/man/pt_BR
tar xvfpz $RPM_SOURCE_DIR/slocate-man-pt_BR.tgz
gzip -9 $RPM_BUILD_ROOT/usr/man/pt_BR/man1/*
ln -sf locate.1.gz $RPM_BUILD_ROOT/usr/man/pt_BR/man1/slocate.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -g 21 -r -f slocate

%files
%defattr(-,root,root)
%attr(2755,root,slocate) /usr/bin/slocate
%attr(-,root,slocate) /usr/bin/locate
%attr(-,root,slocate) /usr/bin/updatedb
%attr(644,root,root) /usr/man/man1/locate.1.gz
%attr(644,root,root) /usr/man/pt_BR/man1/locate.1.gz
%attr(-,root,root) /usr/man/pt_BR/man1/slocate.1.gz
%attr(644,root,root) /usr/man/man1/slocate.1.gz
%attr(644,root,root) /usr/man/man1/updatedb.1.gz
%attr(644,root,root) /usr/man/pt_BR/man1/updatedb.1.gz
%attr(755,root,root) /etc/cron.daily/slocate.cron
%dir %attr(755,root,slocate) /var/lib/slocate

%changelog
* Thu Jul 1 1999 Guilherme Manika <gwm@conectiva.com>
- Updated to 2.0

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added pt_BR and es translations
- Added pt_BR man pages (Stolen from the old findutils package ;)

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- fix updatedb cron script

* Mon Apr 12 1999 Bill Nottingham <notting@redhat.com>
- add updatedb as a link to slocate
- add an updatedb man page

* Fri Mar 26 1999 Michael Maher <mike@redhat.com>
- added man page

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Mon Feb 15 1999 Bill Nottingham <notting@redhat.com>
- %post groupadd changed to %pre 
