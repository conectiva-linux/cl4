Summary: The GNU versions of grep pattern matching utilities.
Summary(pt_BR): Utilitários grep GNU
Summary(es): Utilitarios grep GNU
Name: grep
%define version 2.3
Version: %{version}
Release: 5cl
Copyright: GPL
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
# was .gz
Source: ftp://prep.ai.mit.edu/pub/gnu/grep-%{version}.tar.bz2
Source700: grep-man-pt_BR.tar
Patch: grep-2.3-pt_BR.patch
Buildroot: /var/tmp/grep-root
Requires: info

%description
The GNU versions of commonly used grep utilities.  Grep searches one or
more input files for lines which contain a match to a specified pattern
and then prints the matching lines.  GNU's grep utilities include grep,
egrep and fgrep.  

You should install grep on your system, because it is a very useful utility
for searching through text files, for system administration tasks, etc.

%description -l pt_BR
Esta é a implementação GNU do popular utilitário grep. Permite a
localização rápida de strings em arquivos texto.

%description -l es
Esta es la implementación GNU del popular utilitario grep. Permite
la localización rápida de strings en archivos texto.

%prep
%setup
%patch -p1

%build
unset LINGUAS
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr --exec-prefix=/
make "CFLAGS=$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
make LDFLAGS=-s prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT install

chown -R root.root *



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/grep-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ABOUT-NLS AUTHORS THANKS TODO NEWS README ChangeLog

/bin/*
/usr/info/*.info
/usr/man/man*/*
/usr/share/locale/*/*/grep.*
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%post
/sbin/install-info --quiet --info-dir=/usr/info /usr/info/grep.info

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --quiet --info-dir=/usr/info --delete /usr/info/grep.info
fi

%changelog
* Mon May 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- info included in Requires

* Sun Mar 28 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Mar 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- redid pt_BR.po patch
- unset LINGUAS
- pt_BR man pages

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- upgraded to grep 2.3, added install-info %post/%preun for info

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.2

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- updated from 2.0 to 2.1
- spec file cleanups
- added BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
