Summary: Runtime and developemnt libraries for Red Hat Linux 5.2 backwards compatibility
Summary(pt_BR): Bibliotecas dinâmicas e de desenvolvimento para o Conectiva Linux 4.0
Summary(es): Runtime and developemnt libraries for Red Hat Linux 5.2 backwards compatibility
Name: compat-libs
Version: 3.0
Release: 1cl
Copyright: LGPL
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Buildroot: /var/tmp/compat-libs-root
%define LIBRARIES ICE PEX5 SM X11 XIE Xaw Xext Xi Xmu Xp Xt Xtst Xpm form menu ncurses panel termcap
AutoReq: false
AutoProv: false

%description
This package includes a number of run-time libraries that are compiled on
Red Hat Linux 5.2. This package is required if you want to do development
for Red Hat Linux 5.2 and other glibc 2.0 based systems.

%description -l pt_BR
Este pacote inclui varias bibliotecas dinâmicas que são compiladas para o
Conectiva Linux 3.0 Este pacote é requerido se você deseja desenvolver
para o Conectiva Linux 3.0 e outros sistemas baseados na glibc 2.0.

%description -l es
This package includes a number of run-time libraries that are compiled on
Red Hat Linux 5.2. This package is required if you want to do development
for Red Hat Linux 5.2 and other glibc 2.0 based systems.

%prep
%setup -c -T

%build
rm -f *
for lib in %{LIBRARIES} ; do 
    candidates=$(ls /lib/lib$lib.so.* /usr/lib/lib$lib.so.* /usr/X11R6/lib/lib$lib.so.* 2>/dev/null ||:)
    for file in $candidates ; do 
	if [ -f $file -a ! -L $file ] ; then cp $file . ; fi
    done
done
# we don't need the ncurses 3 things anymore...
rm -fv lib*.1.9.9*
# and create the .so links for compilig
for lib in lib*.so.* ; do 
    ln -s $lib ${lib%%.so.*}.so
done
#create the soname links
/sbin/ldconfig -n -N -v .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/i386-glibc20-linux/lib
tar cf - . | tar xf - -C $RPM_BUILD_ROOT/usr/i386-glibc20-linux/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/i386-glibc20-linux/lib/*

%changelog
* Wed Jun 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Apr 18 1999 Cristian Gafton <gafton@redhat.com>
- created the first version, just like anotehr anonftp package...
