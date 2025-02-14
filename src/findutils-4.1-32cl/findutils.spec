Summary: The GNU versions of find utilities (find, xargs, and locate).
Summary(pt_BR): Utilit�rios de procura da GNU (find, xargs e locate)
Summary(es): Utilitarios de b�squeda de la GNU (find, xargs y locate)
Name: findutils
Version: 4.1
Release: 32cl
Copyright: GPL
Group: Applications/File
Group(pt_BR): Aplica��es/Arquivo
Group(es): Aplicaciones/Archivo
Source0: ftp://prep.ai.mit.edu/pub/gnu/findutils-4.1.tar.gz
Source1: updatedb.cron
Source700: findutils-man-pt_BR.tar
Patch0: findutils-4.1-fsstnd.patch
Patch1: findutils-4.1-basename.patch
Patch2: findutils-4.1-glibc.patch
Patch3: findutils-4.1-mktemp.patch
Patch4: findutils-4.1-getshort.patch
Patch5: findutils-4.1-glibc21.patch
Patch6: findutils-4.1-xargsoverflow.patch
Prereq: /sbin/install-info
### not needed with slocate
#Requires: mktemp
Prefix: %{_prefix}
Buildroot: /var/tmp/find-root

%description
The findutils package contains programs which will help you locate files
on your system.  The find utility searches through a hierarchy of
directories looking for files which match a certain set of criteria
(such as a filename pattern).  The locate utility searches a database
(create by updatedb) to quickly find a file matching a given pattern.
The xargs utility builds and executes command lines from standard input
arguments (usually lists of file names generated by the find command).  

You should install findutils because it includes tools that are very useful
for finding things on your system.

%description -l pt_BR
Esse pacote cont�m programas para ajud�-lo a localizar arquivos
em seu sistema. O programa find pode procurar atrav�s de uma
hierarquia de diret�rios procurando por arquivos que obede�am
um certo conjunto de crit�rios (como nome de arquivo modelo). O
programa locate procura um banco de dados (criado por updatedb)
para rapidamente achar um arquivo que corresponda ao modelo dado.

%description -l es
Este paquete contiene programas para ay�dalo a localizar archivos
en tu sistema. El programa find puede pesquisar, a trav�s de una
jerarqu�a de directorios, buscando por archivos que obedezcan a un
cierto conjunto de criterios (como nombre de archivo modelo). El
programa locate busca un banco de datos (creado por updatedb)
para r�pidamente encontrar un archivo que corresponda al modelo dado.

%prep
%setup -q
%patch0 -p1 -b .fsstnd
%patch1 -p1 -b .basename
%patch2 -p1 -b .glibc
%patch3 -p1 -b .mktemp
%patch4 -p1 -b .getshort
%patch5 -p1 -b .glibc21

%build
#./configure --prefix=%{_prefix} --exec-prefix=%{_prefix}
#make CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" LDFLAGS=-s

%define	optflags $RPM_OPT_FLAGS -D_GNU_SOURCE
%configure --exec-prefix=%{_prefix}
%undefine optflags

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/findutils
make prefix=${RPM_BUILD_ROOT}%{_prefix} exec_prefix=${RPM_BUILD_ROOT}%{_prefix} install

{ cd $RPM_BUILD_ROOT
  chmod 755 .%{_prefix}/lib/findutils
  mkdir -p ./etc/cron.daily
  install -m755 %SOURCE1 ./etc/cron.daily
  gzip -9fn .%{_prefix}/info/find.info*
  strip .%{_prefix}/bin/* || :
}





mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/findutils-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%post
/sbin/install-info %{_prefix}/info/find.info.gz %{_prefix}/info/dir

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_prefix}/info/find.info.gz %{_prefix}/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README
%attr(0644,root,root) /usr/man/pt_BR/man*/*
%{_prefix}/bin/find
%{_prefix}/bin/xargs
%{_prefix}/man/man1/find.1
%{_prefix}/man/man1/xargs.1
%{_prefix}/info/find.info*

# these are excluded as we ship slocate (ewt)
#%config /etc/cron.daily/updatedb.cron
#%{_prefix}/lib/findutils
#%{_prefix}/man/man1/updatedb.1
#%{_prefix}/man/man5/locatedb.5
#%{_prefix}/bin/locate
#%{_prefix}/bin/updatedb
#%{_prefix}/man/man1/locate.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 29 1999 Preston Brown <pbrown@redhat.com>
- patch to fix xargs out of bounds overflow (bug # 1279)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 30)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.

* Mon Feb  8 1999 Jeff Johnson <jbj@redhat.com>
- remove further updatedb remnants (#1072).

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- added patch for glibc21

* Mon Nov 16 1998 Erik Troan <ewt@redhat.com>
- removed locate stuff (as we now ship slocate)

* Wed Jun 10 1998 Erik Troan <ewt@redhat.com>
- updated updatedb cron script to not look for $TMPNAME.n (which was
  a relic anyway)
- added -b parameters to all of the patches

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Mar 09 1998 Michael K. Johnson <johnsonm@redhat.com>
- make updatedb.cron use mktemp correctly
- make updatedb use mktemp

* Sun Nov 09 1997 Michael K. Johnson <johnsonm@redhat.com>
- nobody should own tmpfile
- ignore /net

* Wed Nov 05 1997 Michael K. Johnson <johnsonm@redhat.com>
- made updatedb.cron do a better job of cleaning up after itself.

* Tue Oct 28 1997 Donald Barnes <djb@redhat.com>
- fixed 64 bit-ism in getline.c, patch tacked on to end of glibc one

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- added patch for glibc 2.1

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot support

* Tue Oct 14 1997 Michael K. Johnson <johnsonm@redhat.com>
- made updatedb.cron work even if "nobody" can't read /root
- use mktemp in updatedb.cron

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- added missing info pages
- uses install-info

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built with glibc

* Mon Apr 21 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed updatedb.cron
