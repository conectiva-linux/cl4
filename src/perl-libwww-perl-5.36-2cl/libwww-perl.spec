Summary: libwww-perl module for perl
Summary(pt_BR): M�dulo libwww-perl para o Perl
Summary(es): M�dulo libwww-perl para el Perl
Name: perl-libwww-perl
Version: 5.36
Release: 2cl
Copyright: distributable
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source0: libwww-perl-5.36.tar.gz
Url: http://www.cpan.org
BuildRoot: /var/tmp/libwww-perl-buildroot/
Requires: perl >= 5.004


%description
libwww-perl module for perl

%description -l pt_BR
M�dulo libwww-perl para o Perl

%description -l es
M�dulo libwww-perl para el Perl

%prep
%setup -q -n libwww-perl-5.36

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make PREFIX=$RPM_BUILD_ROOT/usr install
find $RPM_BUILD_ROOT/usr -type f -print | sed "s@^$RPM_BUILD_ROOT@@g" | grep -v perllocal.pod > libwww-perl-5.36-filelist

%files -f libwww-perl-5.36-filelist
%defattr(-,root,root)

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun 16 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Oct 17 1998  <root@kenny.devel.redhat.com>
- Spec file was autogenerated. 