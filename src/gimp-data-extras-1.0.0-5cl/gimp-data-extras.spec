Summary: The GNU Image Manipulation Program
Summary(pt_BR): Padrões, gradientes, etc para o gimp
Summary(es): Padrones, gradientes, etc para gimp
Name: gimp-data-extras
Version: 1.0.0
Release: 5cl
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
URL: http://www.gimp.org/
#Source: ftp://ftp.gimp.org/pub/gimp/devel/0.99.17/gimp-data-extras-%{PACKAGE_VERSION}.tar.gz
# recompressed with bzip2
Source: ftp://ftp.gimp.org/pub/gimp/devel/0.99.17/gimp-data-extras-%{PACKAGE_VERSION}.tar.bz2
BuildRoot: /var/tmp/gimp-data-extra-root
BuildArchitectures: noarch

%description
Patterns, gradients etc. for gimp. This package isn't required, but contains
lots of goodies for gimp.

%description -l pt_BR
Padrões, gradientes, etc para o gimp. Este pacote não é necessário,
mas contém muitas coisas legais para o gimp.

%description -l es
Padrones, gradientes, etc para gimp. Este paquete no es necesario,
pero contiene muchas cosas interesantes para gimp.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
/usr/share/gimp/*


%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 25 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- packaged for 5.2
