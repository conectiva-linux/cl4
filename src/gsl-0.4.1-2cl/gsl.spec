Summary: GNU Scientific library
Summary(pt_BR): Biblioteca científica do GNU.
Summary(es): Biblioteca científica del GNU.
Name: gsl
Version: 0.4.1
Release: 2cl
URL: http://www.gnu.org
# was .gz
Source: ftp://nis-ftp.lanl.gov/pub/users/rosalia/gsl-%{version}.tar.bz2
Copyright: GPL 
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
BuildRoot: /var/tmp/gsl-root

%description
This is the GNU scientific library.  Linking against it gives access
to functions for handling many problems that arise in scientific computing.

#%description devel
#These are the static libraries, header files, and documentation for using the
#GNU scientific  library in your own programs.  With these, you can
#create your own own programs that use this library.

%description -l pt_BR
Esta é a biblioteca científica do GNU. Fornece acesso a funções
para tratar muitos problemas que surgem em computação científica.

%description -l es
Esta es la biblioteca científica del GNU. Ofrece acceso a funciones
para manejar muchos problemas que aparecen en computación científica.

%prep
%setup

%build
./configure --prefix=${RPM_BUILD_ROOT}/usr
make CFLAGS="${RPM_OPT_FLAGS}"

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/lib ${RPM_BUILD_ROOT}/usr/info \
         ${RPM_BUILD_ROOT}/usr/include

make CFLAGS="${RPM_OPT_FLAGS}" install
cd ${RPM_BUILD_ROOT}/usr/lib
#strip *

%post
/sbin/ldconfig

# change back when shared libs working
#%post devel
/sbin/install-info /usr/info/gsl-ref.info.gz /usr/info/dir > /dev/null 2>&1
exit 0

%postun
/sbin/ldconfig

# change back to devel when shared libs working
#%preun devel
%preun 
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/gsl-ref.info.gz /usr/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Mar 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 0.4.1

* Thu Mar 25 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Mar 25 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations


* Wed Sep 2 1998 Michael Fulbright <msf@redhat.com>
- updated for RH 5.2

%files
#/usr/lib/lib*.so

#%files devel
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
#/usr/lib/libgmp.so
/usr/lib/lib*.a
/usr/include/*
/usr/info/gsl-ref.info*
