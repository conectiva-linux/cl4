Summary: A Perl interpreter for the Apache Web server.
Summary(pt_BR): mod_perl - módulo do apache para embutir comandos PERL em arquivos HTML
Summary(es): mod_perl - módulo del apache para empotrar comandos PERL en archivos HTML
Name: mod_perl
Version: 1.20
Release: 7cl
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
# was .gz
Source0: http://www.perl.com/CPAN/by-module/Apache/%{name}-%{version}.tar.bz2
Patch0: %{name}-1.16-rh.patch
Copyright: GPL
BuildRoot: /var/tmp/%{name}-root
Requires: webserver perl >= 5.004-4

%description
Mod_perl incorporates a Perl interpreter into the Apache web
server, so that the Apache web server can directly execute Perl
code.  Mod_perl links the Perl runtime library into the Apache
web server and provides an object-oriented Perl interface for
Apache's C language API.  The end result is a quicker CGI script
turnaround process, since no external Perl interpreter has to
be started.

Install mod_perl if you're installing the Apache web server and
you'd like for it to directly incorporate a Perl interpreter.

%description -l pt_BR
mod_perl - módulo do apache para embutir comandos PERL em arquivos HTML.

%description -l es
mod\_perl es un potente módulo que habilita el uso del lenguaje
PERL dentro de archivos HTML.

%prep
%setup -q
%patch -p1 -b .rh

%build
perl Makefile.PL \
	USE_APXS=1 \
	WITH_APXS=/usr/sbin/apxs \
	EVERYTHING = 1

(cd apaci; ln -s ../src/modules .; chmod +x find_source)
make

%install
%ifarch i386
%define buildarch i386
%endif
%ifarch alpha
%define buildarch alpha
%endif
%ifarch sparc
%define buildarch sparc
%endif

rm -rf $RPM_BUILD_ROOT
make pure_install PREFIX=$RPM_BUILD_ROOT/usr
mkdir -p $RPM_BUILD_ROOT/usr/lib/apache
install -m 755 apaci/libperl.so $RPM_BUILD_ROOT/usr/lib/apache
mkdir -p $RPM_BUILD_ROOT/home/httpd/html/manual/mod
install -m 644 htdocs/manual/mod/mod_perl.html \
	$RPM_BUILD_ROOT/home/httpd/html/manual/mod

PACKLIST=$RPM_BUILD_ROOT/usr/lib/perl5/site_perl/5.005/%{buildarch}-linux/auto/mod_perl/.packlist
mv $PACKLIST $PACKLIST.old
sed -e "s|$RPM_BUILD_ROOT||g" < $PACKLIST.old > $PACKLIST
rm -f $PACKLIST.old
find $RPM_BUILD_ROOT -type f -o -type l | \
	sed -e "s|$RPM_BUILD_ROOT||g" > file-list.lst
cd faq; make

%clean
rm -rf $RPM_BUILD_ROOT
rm -f file-list.lst

%files -f file-list.lst
%doc README INSTALL faq/*.html eg
%doc ToDo apache-modlist.html
%dir /usr/lib/perl5/site_perl/5.005/%{buildarch}-linux/auto/Apache
%dir /usr/lib/perl5/site_perl/5.005/%{buildarch}-linux/auto/Apache/Symbol
%dir /usr/lib/perl5/site_perl/5.005/%{buildarch}-linux/auto/mod_perl
%dir /usr/lib/perl5/site_perl/5.005/%{buildarch}-linux/Apache/Constants
%dir /usr/lib/perl5/site_perl/5.005/%{buildarch}-linux/Bundle

%changelog
* Sat Jun 12 1999 Marcelo Tosatti <marcelo@conectiva.com>
- update to 1.20
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Apr 10 1999 Marcelo Tosatti <marcelo@conectiva.com>
- update to 1.19

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sun Feb 07 1999 Preston Brown <pbrown@redhat.com>
- upgraded to mod_perl 1.18.

* Mon Dec 21 1998 Preston Brown <pbrown@redhat.com>
- Upgraded to mod_perl 1.16.

* Thu Sep 03 1998 Preston Brown <pbrown@redhat.com>
- disabled stacked_handlers.  They still seem busted!
- minor updates so no conflicts with either apache / secureweb
- fixed bug building on multiple architectures

* Wed Sep 02 1998 Preston Brown <pbrown@redhat.com>
- Updates for apache 1.3.x, and mod_perl 1.15

* Fri Feb 27 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to compile it as a shared object for the apache/ssl (and
  future revisions of apache)
