Summary: Perl program to mirror FTP sites
Summary(pt_BR): Programa em perl para fazer espelhos de sítios FTP
Summary(es): Programa en perl para hacer espejos de sitios FTP
Name: mirror
Version: 2.9
Release: 4cl
Copyright: distributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source:  ftp://sunsite.org.uk/packages/mirror/mirror.tar.gz  
Url: http://sunsite.doc.ic.ac.uk/packages/mirror/
Patch: mirror-2.9-redhat.patch
BuildRoot: /var/tmp/mirror-root
BuildArchitectures: noarch

%description
Perl program to mirror FTP sites.

%description -l pt_BR
Programa em perl para fazer espelhos de sítios FTP

%description -l es
Programa en perl para hacer espejos de sitios FTP

%prep
%setup -q -c
%patch -p1 -b .redhat

%build 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/mirror
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
make "PLDIR=$RPM_BUILD_ROOT/usr/lib/mirror" "BINDIR=$RPM_BUILD_ROOT/usr/bin" "MANDIR=$RPM_BUILD_ROOT/usr/man/man1" install

install -m 644 mirror.defaults $RPM_BUILD_ROOT/etc

ln -sf mirror.pl $RPM_BUILD_ROOT/usr/bin/mirror

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt *.html CHANGES*
%doc mirror.nightly support/cyber-patches support/lstest.pl
%config /etc/mirror.defaults
/usr/bin/do_unlinks.pl
/usr/bin/mirror
/usr/bin/mirror.pl
/usr/bin/mm.pl
/usr/bin/pkgs_to_mmin.pl
/usr/lib/mirror/dateconv.pl
/usr/lib/mirror/ftp.pl
/usr/lib/mirror/lchat.pl
/usr/lib/mirror/lsparse.pl
/usr/man/man1/mirror.1
/usr/man/man1/mm.1


%changelog
* Wed Jun 16 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr 13 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- built for conectiva

* Tue Oct 27 1998 Cristian Gafton <gafton@redhat.com>
- enhanced redhat patch

* Fri Oct 08 1998 Michael Maher <mike@redhat.com>
- updated package to 2.9
- fixed spec file

* Mon May 18 1998 Michael Maher <mike@redhat.com>
- updated rpm package and cleaned up SRPM.

* Fri Jan  9 1998 Otto Hammersmith <otto@redhat.com>
- grabbed contrib package for powertools.
