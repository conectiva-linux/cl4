Summary: The Perl interface to the RSA Message Digest Algorithm.
Summary(pt_BR): Módulo MD5 para perl
Summary(es): Módulo MD5 para perl
Name: perl-MD5
%define	version	1.7
Version: %{version}
Release: 6cl
Copyright: distributable
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source0: ftp://ftp.perl.org//pub/CPAN/modules/by-module/MD5/MD5-%{version}.tar.gz
BuildRoot: /var/tmp/MD5-buildroot/
Requires: perl >= 5.004

%description
The perl-MD5 package provides the MD5 module for the Perl
programming language.  MD5 is a Perl interface to the RSA Data
Security Inc. Message Digest Algorithm, which allows Perl
programs to use the algorithm.

The perl-MD5 package should be installed if any Perl programs
on your system are going to use RSA's Message Digest Algorithm.

%description -l pt_BR
Fornece acesso ao algoritmo md5 da RSA para programas escritos
em perl.

%description -l es
Ofrece acceso al algoritmo md5 de RSA para programas escritos
en perl.

%prep
%setup -n MD5-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
FOO=
make PREFIX=$RPM_BUILD_ROOT/usr \
   INSTALLMAN3DIR=$RPM_BUILD_ROOT/`dirname $installarchlib`/man/man3 install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/perl5/site_perl/*/*-linux/MD5.pm
/usr/lib/perl5/site_perl/*/*-linux/auto/MD5
/usr/lib/perl5/*/man/*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Jan 21 1999 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Sun Jun 21 1998 Jeff Johnson <jbj@redhat.com>
- add %clean

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- added the shared lib module to the package

* Sat Apr 11 1998 Bryan C. Andregg <bandregg@redhat.com>
- First build.
