Summary: A version control system.
Summary(pt_BR): Controle de versões em modo concorrente
Summary(es): Control de versiones en modo concurrente
Name: cvs
Version: 1.10.5
Release: 4cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://download.cyclic.com/pub/cvs-%{version}/cvs-%{version}.tar.bz2
Patch0: cvs-1.10-tmprace.patch
Prereq: /sbin/install-info
Prefix: %{_prefix}
Buildroot: /var/tmp/%{name}-root

%description
CVS means Concurrent Version System; it is a version control
system which can record the history of your files (usually,
but not always, source code). CVS only stores the differences
between versions, instead of every version of every file
you've ever created. CVS also keeps a log of who, when and
why changes occurred, among other aspects.

CVS is very helpful for managing releases and controlling
the concurrent editing of source files among multiple
authors. Instead of providing version control for a
collection of files in a single directory, CVS provides
version control for a hierarchical collection of
directories consisting of revision controlled files.

These directories and files can then be combined together
to form a software release.

Install the cvs package if you need to use a version
control system.

%description -l pt_BR
CVS é um front end para o rcs(1) - revision control system - que
estende a noção de controle de revisão de uma coletânea de arquivo
em um único diretório para uma coleção hierárquica de diretórios que
contém arquivos controlados por revisão. Esses diretórios e arquivos
podem ser combinados juntos para criar uma release de software. CVS
oferece as funções necessárias para administrar essas release de
software e para controlar a edição concorrente de arquivos fonte
por múltiplos programadores.

%description -l es
CVS es un front end para el rcs(1) - revisión control system -
que extiende la noción de control de revisión de una colectánea
de archivo en un único directorio para una colección jerárquica de
directorios que contiene archivos controlados por revisión. Estos
directorios y archivos pueden ser combinados juntos para crear una
release de software. CVS nos ofrece las funciones necesarias para
administrar esta release de software y para controlar la edición
concurrente de archivos fuente por múltiples programadores.

%package doc
Summary: Additional CVS documentation
Summary(pt_BR): Documentação adicional para o CVS
Summary(es): Documentación de CVS
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación

%description doc
Additional CVS documentation

%description -l pt_BR doc
Documentação adicional para o CVS

%description -l es doc
Documentación de CVS

%prep
%setup -q
%patch0 -p1 -b .tmprace

%build
#./configure --prefix=/usr

%configure
make LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/%{_prefix} install install-info

gzip -9nf $RPM_BUILD_ROOT/%{_prefix}/info/cvs*
strip $RPM_BUILD_ROOT/%{_prefix}/bin/cvs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /%{_prefix}/info/cvs.info.gz /%{_prefix}/info/dir --entry="* cvs: (cvs).          A version control system for multiple developers."
/sbin/install-info /%{_prefix}/info/cvsclient.info.gz /%{_prefix}/info/dir --entry="* cvsclient: (cvsclient).                       The CVS client/server protocol."

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete /%{_prefix}/info/cvs.info.gz /%{_prefix}/info/dir --entry="* cvs: (cvs).		A version control system for multiple developers."
	/sbin/install-info --delete /%{_prefix}/info/cvsclient.info.gz /%{_prefix}/info/dir --entry="* cvsclient: (cvsclient).                       The CVS client/server protocol."
fi

%files
%defattr(-,root,root)
%doc BUGS FAQ MINOR-BUGS NEWS PROJECTS TODO README
/%{_prefix}/bin/cvs
/%{_prefix}/bin/cvsbug
/%{_prefix}/bin/rcs2log
/%{_prefix}/man/man1/cvs.1
/%{_prefix}/man/man5/cvs.5
/%{_prefix}/man/man8/cvsbug.8
/%{_prefix}/info/cvs*
/%{_prefix}/lib/cvs

%files doc
%doc doc/*.ps

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun 01 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- created the cvs-doc subpackage

* Tue Jun  1 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- updated text in spec file.

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.10.5.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.10.4.

* Tue Oct 20 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.3.

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.2.

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- remove trailing characters from rcs2log mktemp args

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.1

* Mon Aug 31 1998 Jeff Johnson <jbj@redhat.com>
- fix race conditions in cvsbug/rcs2log

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.9.30.

* Mon Jun 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Mon Jun  8 1998 Jeff Johnson <jbj@redhat.com>
- build root
- update to 1.9.28

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added install-info stuff
- added changelog section
