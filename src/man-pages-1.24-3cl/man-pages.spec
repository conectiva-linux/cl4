Summary: Man (manual) pages from the Linux Documentation Project.
Summary(pt_BR): Páginas de manual, do Projeto de Documentação do Linux (LDP)
Summary(es): Páginas de manual, del Proyecto de Documentación del Linux (LDP)
Name: man-pages
%define	version	1.24
Version: %{version}
Release: 3cl
Copyright: distributable
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Source: ftp://ftp.win.tue.nl/pub/linux/docs/manpages/man-pages-%{version}.tar.bz2
Source1: rpcgen.1
Source2: netman-cvs.tar.gz
Source3: http://www.muppetlabs.com/linux/man9/man9-snapshot.tar.bz2
Source700: man-pages-man-pt_BR.tar
Patch0: man-pages.patch 
Patch1: man-pages-1.23-spell.patch
Patch2: man-pages-1.23-ftw.patch
Buildroot: /var/tmp/man-pages
Autoreqprov: false
BuildArchitectures: noarch

%description
A large collection of man pages (reference material) from the Linux 
Documentation Project (LDP).  The man pages are organized into the
following sections:

        Section 1:  User commands (intro only)
        Section 2:  System calls
        Section 3:  Libc calls
        Section 4:  Devices (e.g., hd, sd)
        Section 5:  File formats and protocols (e.g., wtmp, /etc/passwd,
                nfs)
        Section 6:  Games (intro only)
        Section 7:  Conventions, macro packages, etc. (e.g., nroff, ascii)
        Section 8:  System administration (intro only)
        Section 9:  kernel functions

%description -l pt_BR
Uma larga coleção de páginas de manuais cobrindo programação APIs,
formatos de arquivos, protocolos, etc.

Seção 1 = comandos de usuário (somente introdução)
Seção 2 = chamadas de sistema
Seção 3 = chamadas libc
Seção 4 = dispositivos (ex.: hd, sd)
Seção 5 = formatos de arquivos e protocolos (ex: wtmp, /etc/passwd, nfs)
Seção 6 = jogos (somente introdução)
Seção 7 = convenções, pacotes de macros, etc. (ex: nroff, ascii)
Seção 8 = administração de sistema (somente introdução)
Seção 9 = kernel

%description -l es
Una larga colección de páginas de manuales cubriendo programación
APIs, formatos de archivos, protocolos, etc.

Seción 1 = comandos de usuario (solamente introducción)
Seción 2 = llamadas de sistema
Seción 3 = llamadas libc
Seción 4 = dispositivos (ej.: hd, sd)
Seción 5 = formatos de archivos y protocolos (ej: wtmp, /etc/passwd, nfs)
Seción 6 = juegos (solamente introducción)
Seción 7 = convenciones, paquetes de macros, etc. (ej: nroff, ascii)
Seción 8 = administración de sistema (solamente introducción)
Seción 9 = kernel

%prep
%setup -q -a 2
# I left the .b off of this to keep from having old versions in file lists
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp -a %{SOURCE1} man1
tar xvfI $RPM_SOURCE_DIR/man9-snapshot.tar.bz2
for i in 2 3 4 ; do 
    mv *.$i man$i
done

%build
rm -fv man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install}.1
rm -fv man1/{ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,touch}.1
rm -fv man2/modules.2 man2/quotactl.2 man2/get_kernel_syms.2 
rm -fv man2/{create,delete,init,query}_module.2
rm -fv man3/resolver.3
rm -fv man3/getnetent.3
rm -fv man4/console.4
rm -fv man5/exports.5
rm -fv man5/nfs.5
rm -fv man5/fstab.5

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/man
for n in 1 2 3 4 5 6 7 8 9; do
	mkdir $RPM_BUILD_ROOT/usr/man/man$n
done
for n in man?/*; do
	cp -a $n $RPM_BUILD_ROOT/usr/man/$n
done


rm $RPM_BUILD_ROOT/usr/man/man1/{README,COPYING}
gzip -9f $RPM_BUILD_ROOT/usr/man/man*/*



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/man-pages-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,man,2755)
/usr/man/man*/*
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Wed Jun 23 1999 Wanderlei Cavassin <cavassin@conectiva.com>
- compressed all man pages

* Wed Jun 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 1.23 to 1.24, included kernel man pages (man9)

* Mon Jun 14 1999 Conectiva <dist@conectiva.com>
- included pt_BR man pages

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- fiox man page fro ftw

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- spellnig fixse

* Tue Mar 30 1999 Bill Nottingham <notting@redhat.com>
- updated to 1.23

* Thu Mar 25 1999 Cristian Gafton <gafton@redhat.com>
- added kernel net manpages

* Mon Mar 22 1999 Erik Troan <ewt@redhat.com>
- updated printf man page
- added rpcgen man page

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- leave the lilo man pages alone (oops)

* Fri Feb 12 1999 Michael Maher <mike@redhat.com>
- fixed bug #413

* Mon Jan 18 1999 Cristian Gafton <gafton@redhat.com>
- remove lilo man pages too
- got rebuilt for 6.0

* Tue Sep 08 1998 Cristian Gafton <gafton@redhat.com>
- version 1.21

* Sat Jun 20 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.20

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- get rid of the modutils man pages
- updated to 1.19

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 1.18

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to 1.17
- moved build root to /var

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
