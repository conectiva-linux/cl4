Summary: Tools needed to create Texinfo format documentation files.
Summary(pt_BR): Formatador texinfo e leitor de arquivos info
Summary(es): Formateador texinfo y lector de archivos info
Name: texinfo
Version: 3.12f
Release: 4cl
Copyright: GPL
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Source0: ftp://prep.ai.mit.edu/pub/gnu/texinfo-%{version}.tar.gz
Source1: info-dir
Source2: info.wmconfig
Source800: texinfo-wmconfig.i18n.tgz
Patch0: texinfo-3.12f-exe.patch
Patch1: texinfo-3.12-fix.patch
Patch2: texinfo-3.12f-alpha-tioc.patch
Patch3: texinfo-3.12-zlib.patch
Prereq: info
Buildroot: /var/tmp/texinfo-root

%description
Texinfo is a documentation system that can produce both online information
and printed output from a single source file.  Normally, you'd have to
write two separate documents: one for online help or other online
information and the other for a typeset manual or other printed work.
Using Texinfo, you only need to write one source document.  Then when the
work needs revision, you only have to revise one source document.  The GNU
Project uses the Texinfo file format for most of its documentation.

Install texinfo if you want a documentation system for producing both
online and print documentation from the same source file and/or if you are
going to write documentation for the GNU Project.

%description -l pt_BR
O projeto GNU usa o formato de arquivo texinfo para a maior parte
da sua documentação. Este pacote inclui um browser para visualizar
estes arquivos.

%description -l es
El proyecto GNU usa el formato de archivo texinfo para la mayor
parte de su documentación. Este paquete incluye un browser para
visualizar estos archivos.

%package -n info
Summary: A stand-alone TTY-based reader for GNU texinfo documentation.
Summary(pt_BR): Leitor baseado em tty para documentos texinfo GNU
Summary(es): Lector basado en tty para documentos texinfo GNU
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
# By making info prereq bash, other packages which have triggers based on
# info don't run those triggers until bash is in place as well. This is an
# ugly method of doing it (triggers which fire on set intersection would
# be better), but it's the best we can do for now. Talk to Erik before
# removing this.
Prereq: bash 

%description -n info
The GNU project uses the texinfo file format for much of its
documentation. The info package provides a standalone TTY-based browser
program for viewing texinfo files.

You should install info, because GNU's texinfo documentation is a valuable
source of information about the software on your system.

%description -l pt_BR -n info
O projeto GNU usa o formato de arquivos texinfo para a maioria de
sua documentação. Este pacote inclui um browser para visualização
destes arquivos.  ~

%description -l es -n info
El proyecto GNU usa el formato de archivos texinfo para la mayoría de
su documentación. Este paquete incluye un browser para visualización
de estos archivos.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .zlib

%build
unset LINGUAS
CFLAGS="-g" ./configure --prefix=/usr
make 
rm util/install-info
make -C util LIBS=/usr/lib/libz.a

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc,sbin}

make install prefix=$RPM_BUILD_ROOT/usr

( cd $RPM_BUILD_ROOT
  gzip -n -9f ./usr/info/*info*
  install -m644 $RPM_SOURCE_DIR/info-dir ./etc/info-dir
  ln -sf ../../etc/info-dir $RPM_BUILD_ROOT/usr/info/dir
  for i in makeinfo texindex info install-info ; do
    strip ./usr/bin/$i
  done
  mv -f ./usr/bin/install-info ./sbin
  mkdir -p ./etc/X11/wmconfig
  install -m 644 $RPM_SOURCE_DIR/info.wmconfig ./etc/X11/wmconfig/info
)


tar xvfpz $RPM_SOURCE_DIR/texinfo-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/texinfo.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/texinfo.gz /usr/info/dir
fi

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL INTRODUCTION NEWS README TODO
%doc info/README
/usr/bin/makeinfo
/usr/bin/texindex
/usr/bin/texi2dvi
/usr/info/info-stnd.info*
/usr/info/texinfo*
/usr/share/locale/*/*/*

%files -n info
%defattr(-,root,root)
%config(missingok) /etc/X11/wmconfig/info
%config(noreplace) /etc/info-dir
%config(noreplace) /usr/info/dir
/usr/bin/info
/usr/info/info.info*
/sbin/install-info

%changelog
* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- unset LINGUAS
- i18n wmconfig

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Mar 17 1999 Erik Troan <ewt@redhat.com>
- hacked to use zlib to get rid of the requirement on gzip

* Wed Mar 17 1999 Matt Wilson <msw@redhat.com>
- install-info prerequires gzip

* Thu Mar 11 1999 Cristian Gafton <gafton@redhat.com>
- version 3.12f
- make /usr/info/dir to be a %config(noreplace)
* Wed Nov 25 1998 Jeff Johnson <jbj@redhat.com>
- rebuild to fix docdir perms.

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- fix allocation problems in install-info

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- /sbin/install-info should not depend on /usr/lib/libz.so.1 -- statically
  link with /usr/lib/libz.a.

* Fri Aug 07 1998 Erik Troan <ewt@redhat.com>
- added a prereq of bash to the info package -- see the comment for a
  description of why that was done

* Tue Jun 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Tue Jun  9 1998 Jeff Johnson <jbj@redhat.com>
- add %attr to permit non-root build.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Apr 12 1998 Cristian Gafton <gafton@redhat.com>
- added %clean
- manhattan build

* Wed Mar 04 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 3.12
- added buildroot

* Sun Nov 09 1997 Donnie Barnes <djb@redhat.com>
- moved /usr/info/dir to /etc/info-dir and made /usr/info/dir a
  symlink to /etc/info-dir.

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry for info

* Wed Oct 01 1997 Donnie Barnes <djb@redhat.com>
- stripped /sbin/install-info

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added info-dir to filelist

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- added patch from sopwith to let install-info understand gzip'ed info files
- use skeletal dir file from texinfo tarball (w/ bash entry to reduce
  dependency chain) instead (and install-info command everywhere else)
- patches install-info to handle .gz names correctly

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Feb 25 1997 Erik Troan <ewt@redhat.com>
- patched install-info.c for glibc.
- added /usr/bin/install-info to the filelist

* Tue Feb 18 1997 Michael Fulbright <msf@redhat.com>
- upgraded to version 3.9.
