%define EGCS_VERSION 1.0.3a
%define STDC_VERSION 2.8.0
Summary: Experimental GNU Compiler System for Conectiva 3.0 backwards compatibility
Summary(pt_BR):  Experimental GNU Compiler System for Conectiva 3.0 backwards compatibility
Summary(es):  Experimental GNU Compiler System for Conectiva 3.0 backwards compatibility
Name: compat-egcs
Version: 3.0
Release: %{EGCS_VERSION}.1cl
Copyright: GPL
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source: ftp://egcs.cygnus.com/pub/egcs/releases/egcs-%{EGCS_VERSION}/egcs-%{EGCS_VERSION}.tar.bz2
Patch0: egcs-1.0.2-sparc.patch
Buildroot: /var/tmp/egcs-root
Url: http://egcs.cygnus.com/
Requires: compat-binutils = %{version}
Requires: compat-glibc = %{version}

%description
This package includes a compiler that can be used to generated binaries that
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc
2.0.X based systems). This package includes the C compiler and required
compiler libraries for those systems.

%description -l pt_BR
This package includes a compiler that can be used to generated binaries that
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc
2.0.X based systems). This package includes the C compiler and required
compiler libraries for those systems.


%description -l es
This package includes a compiler that can be used to generated binaries that
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc
2.0.X based systems). This package includes the C compiler and required
compiler libraries for those systems.


%package c++
Summary: C++ support for Conectiva 3.0 backwards compatibility C compiler
Summary(pt_BR):  C++ support for Conectiva 3.0 backwards compatibility C compiler
Summary(es):  C++ support for Conectiva 3.0 backwards compatibility C compiler
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: %{name} = %{version}

%description c++
This package includes a compiler that can be used to generated binaries that 
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc 
2.0.X based systems). This packge includes the C++ compiler and libraries
for those older systems.

%description -l pt_BR c++
This package includes a compiler that can be used to generated binaries that 
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc 
2.0.X based systems). This packge includes the C++ compiler and libraries
for those older systems.


%description -l es c++
This package includes a compiler that can be used to generated binaries that 
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc 
2.0.X based systems). This packge includes the C++ compiler and libraries
for those older systems.


%package objc
Summary: Ojective C support for Conectiva 3.0 backwards compatibility C compiler
Summary(pt_BR):  Ojective C support for Conectiva 3.0 backwards compatibility C compiler
Summary(es):  Ojective C support for Conectiva 3.0 backwards compatibility C compiler
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: %{name} = %{version}

%description objc
This package includes a compiler that can be used to generated binaries that
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc
2.0.X based systems). This packge includes the Objective C compiler and
libraries for those older systems.

%description -l pt_BR objc
This package includes a compiler that can be used to generated binaries that
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc
2.0.X based systems). This packge includes the Objective C compiler and
libraries for those older systems.


%description -l es objc
This package includes a compiler that can be used to generated binaries that
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc
2.0.X based systems). This packge includes the Objective C compiler and
libraries for those older systems.


%package g77
Summary: Fortran 77 support for Conectiva 3.0 backwards compatibility C compiler
Summary(pt_BR):  Fortran 77 support for Conectiva 3.0 backwards compatibility C compiler
Summary(es):  Fortran 77 support for Conectiva 3.0 backwards compatibility C compiler
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: %{name} = %{version}

%description g77
This package includes a compiler that can be used to generated binaries that
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc
2.0.X based systems). This packge includes the Fortran 77 compiler and
libraries for those older systems.

%description -l pt_BR g77
This package includes a compiler that can be used to generated binaries that
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc
2.0.X based systems). This packge includes the Fortran 77 compiler and
libraries for those older systems.


%description -l es g77
This package includes a compiler that can be used to generated binaries that
will run on older Conectiva Linux systems (namely Conectiva Linux 3.0, or glibc
2.0.X based systems). This packge includes the Fortran 77 compiler and
libraries for those older systems.


%prep
%setup -q -n egcs-%{EGCS_VERSION}
%ifarch sparc
%patch0 -p1 -b .sparc
%endif

%build
rm -rf obj-$RPM_ARCH-linux
mkdir obj-$RPM_ARCH-linux
cd obj-$RPM_ARCH-linux
CFLAGS=-O2 ../configure  --prefix=/usr \
	--enable-shared --enable-threads \
	--program-transform-name="s,^,$RPM_ARCH-glibc20-linux-," \
	$RPM_ARCH-glibc20-linux 
	
PATH=$PATH:/sbin:/usr/sbin
# gperf is most likely broken on alpha and sparc 
touch  ../gcc/c-gperf.h
make MAKEINFO="makeinfo --no-split" bootstrap-lean

%install
rm -rf $RPM_BUILD_ROOT
cd obj-$RPM_ARCH-linux
PATH=$PATH:/sbin:/usr/sbin
make install \
	prefix=$RPM_BUILD_ROOT/usr MAKEINFO="makeinfo --no-split"
# get rid of the texinfo crap
make prefix=$RPM_BUILD_ROOT/usr -C texinfo uninstall
FULLVER=`$RPM_BUILD_ROOT/usr/bin/$RPM_ARCH-glibc20-linux*-gcc --version | cut -d' ' -f1`
FULLPATH=$(dirname $RPM_BUILD_ROOT/usr/lib/gcc-lib/$RPM_ARCH-glibc20-linux/$FULLVER/cc1)
strip $RPM_BUILD_ROOT/usr/bin/*
strip $FULLPATH/{cc1,cc1obj,cc1plus,cpp,f771,ld}

# fix some things
mv $RPM_BUILD_ROOT/usr/lib/libf2c.a $FULLPATH
mv $RPM_BUILD_ROOT/usr/lib/libstdc++.* $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/lib
mv $RPM_BUILD_ROOT/usr/include/g++ $RPM_BUILD_ROOT/usr/$RPM_ARCH-glibc20-linux/include

# this is not needed anymore because of the hack in glibc
#perl -p -i \
#	-e "s|/lib/ld-linux.so.2|/usr/$RPM_ARCH-glibc20-linux/lib/ld-linux.so.2|g;" \
#	$FULLPATH/specs


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/lib/gcc-lib/*-glibc20-linux
%dir /usr/lib/gcc-lib/*-glibc20-linux/egcs-*
%dir /usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include
/usr/bin/*-glibc20-linux-gcc
/usr/*-glibc20-linux/lib/libiberty.a
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/SYSCALLS.c.X
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/cc1
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/cpp
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/libgcc.a
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/specs
%ifnarch alpha
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/*.o
%endif
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/ld
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/README
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/float.h
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/iso646.h
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/limits.h
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/proto.h
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/stdarg.h
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/stddef.h
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/syslimits.h
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/va-*.h
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/varargs.h

%files c++
%defattr(-,root,root)
/usr/bin/*-glibc20-linux-g++
/usr/bin/*-glibc20-linux-c++
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/cc1plus
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/exception
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/new
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/typeinfo
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/new.h
/usr/*-glibc20-linux/include/g++
/usr/*-glibc20-linux/lib/libstdc++.a
/usr/*-glibc20-linux/lib/libstdc++.so
/usr/*-glibc20-linux/lib/libstdc++.so.2.8.0

%files objc
%defattr(-,root,root)
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/cc1obj
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/libobjc.a
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/objc

%files g77
%defattr(-,root,root)
/usr/bin/*-glibc20-linux-g77
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/f771
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/include/f2c.h
/usr/lib/gcc-lib/*-glibc20-linux/egcs-*/libf2c.a

%changelog
* Thu Jun 24 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Jun 23 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- built from the original spec included in RH 5.2
