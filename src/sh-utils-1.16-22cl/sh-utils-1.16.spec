Summary: GNU shell utilities
Summary(pt_BR): Utilitários de shell da GNU
Summary(es): Utilitarios de shell de la GNU
Name: sh-utils
Version: 1.16
Release: 22cl
Copyright: GPL
Group: System Environment/Shells
Group(pt_BR): Ambiente do Sistema/Interpretadores de Comandos
Group(es): Ambiente del Sistema/Interpretadores de Comandos
#Source: ftp://prep.ai.mit.edu/pub/gnu/sh-utils-1.16.tar.gz
# recompactado com bzip2
Source: ftp://prep.ai.mit.edu/pub/gnu/sh-utils-1.16.tar.bz2
Source1: su.pamd
Source700: sh-utils-man-pt_BR.tar
Patch1: sh-utils-1.16-hostname.patch
Patch2: sh-utils-1.16-pam.patch
Patch4: sh-utils-1.16-getutent.patch
Patch5: sh-utils-1.16-mktime.patch
Patch6: sh-utils-1.16-paths.patch
Patch7: sh-utils-1.16-newpam.patch
Patch8: sh-utils-1.16-glibc21.patch
Patch9: sh-utils-1.16-nocrypt.patch
Patch10: sh-utils-1.16-mem.patch
Patch100: sh-utils-1.16-pt_BR.patch
Buildroot: /var/tmp/sh-utils
Requires: pam >= 0.59
Prereq: info
Summary(de): GNU-Shell-Utilities 
Summary(fr): Utilitaires shell de GNU
Summary(tr): GNU kabuk araçlarý

%description
The GNU shell utilities provide many of the basic common commands
used (among other things) for shell programming, hence the name.
Nearly all shell scripts use at least one of these programs.

%description -l pt_BR
Os utilitários shell GNU oferecem muitos dos comandos básicos mais
comuns e usados (junto com outras coisas) para programação shell,
conseqüentemente o nome. A maioria dos shell scripts usam pelo
menos um destes programas.

%description -l es
Los utilitarios shell GNU ofrecen muchos de los comandos básicos más
comunes y usados (junto con otras cosas) para programación shell,
de ahí, el nombre. La mayoría de los shell scripts usan por lo
menos uno de estos programas.

%description -l de
Die GNU-Shell-Utilities stellen viele der grundlegenden gemeinsamen 
Befehle zur Verfügung, die unter anderem für die Shell-
Programmierung benutzt werden, woher sich der Name ableitet. Fast 
alle Shell-Skripts benutzen wenigstens eines dieser Programme. 

%description -l fr
Les utilitaires shell de GNU offrent la plupart des commandes de
base utilisées (entre autres) pour la programmation en shell, d'où le nom.
Presque tous les scripts shell utilisent au moins l'un de ces programmes.

%description -l tr
GNU kabuk araçlarý kabuk programlamada da kullanýlan pek çok ana komutu
saðlar. Hemen hemen tüm kabuk programlarý bu programlarýn en azýndan birini
kullanýr.

%prep

%setup -q
%patch1 -p1 -b .hostname
%patch2 -p1 -b .nopam
%patch4 -p1 -b .getutent
%patch5 -p1 -b .mktime
%patch6 -p1 -b .badpaths
%patch7 -p1 -b .newpam
%patch8 -p1 -b .glibc21
%patch9 -p1 -b .nocrypt
%patch10 -p1 -b .mem
%patch100 -p1 -b .pt_BR
autoconf

# this works around autoconf sanity checks
sleep 2

%build
CFLAGS="$RPM_OPT_FLAGS -DUSE_PAM" LDFLAGS=-s ./configure --prefix=/usr
make PAMLIBS="-ldl -lpam -lpam_misc"
make PAMLIBS="-ldl -lpam -lpam_misc" info

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{bin,etc/pam.d,usr/sbin}

make install prefix=$RPM_BUILD_ROOT/usr

( cd $RPM_BUILD_ROOT
  #some files are shell scripts... strip will fail on those
  strip ./usr/bin/* || :

  for i in basename date echo false nice pwd sleep stty su true uname ; do
	install -m 755 -s ./usr/bin/$i ./bin/$i
	rm -f ./usr/bin/$i
  done

  install -m 755 ./usr/bin/chroot ./usr/sbin ; rm -f ./usr/bin/chroot
  install -m 755 ./usr/bin/printf ./bin ; ln -sf /bin/printf ./usr/bin/printf
  rm -f	./usr/bin/{hostname,uptime} ./usr/man/man1/{hostname,uptime}.1

  rm -f ./usr/bin/[
  ln -sf test ./usr/bin/[

  gzip -n -f ./usr/info/sh-utils.info

  mkdir -p ./etc/pam.d
  install -m644 ${RPM_SOURCE_DIR}/su.pamd ./etc/pam.d/su
)



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/sh-utils-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/sh-utils.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/sh-utils.info.gz /usr/info/dir
fi

%files
%defattr(-,root,root)
%doc NEWS README
%config /etc/pam.d/su
/bin/basename
/bin/date
/bin/echo
/bin/false
/bin/nice
/bin/pwd
/bin/printf
/bin/sleep
/bin/stty
%attr(4755,root,root)	/bin/su
/bin/true
/bin/uname
/usr/sbin/chroot
/usr/bin/*
/usr/man/man1/*
/usr/info/sh-utils.info.gz
/usr/share/locale/*/LC_MESSAGES/sh-utils.mo
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- man pages novas/revisadas

* Thu Mar 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- printf goes to /bin, a symlink stays in /usr/bin

* Fri Feb 19 1999 Conectiva <dist@conectiva.com>
- man pages novas/revisadas

* Wed Dec  9 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Sat Dec  5 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Sun Nov 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Thu Oct 29 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- added patch to configure,configure.in & po/pt_BR.po

* Mon Jun  8 1998 Michal Jaegermann <michal@harddata.com>
- fixed reversed test for when to allocate in who.c and an incorrect
  use of xrealloc.

* Thu Apr 30 1998 Donnie Barnes <djb@redhat.com>
- moved /usr/bin/nice to /bin/nice

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild

* Wed Oct 22 1997 Michael K. Johnson <johnsonm@redhat.com>
- added minor patch for glibc 2.1

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the URLs in spec file
- cleaned up the spec file

* Thu Oct 02 1997 Michael K. Johnson <johnsonm@redhat.com>
- BuildRoot
- New pam standard.

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Apr 18 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fixed the sense of the user and root default paths.

* Mon Apr 14 1997 Erik Troan <ewt@redhat.com>
- Fixed getutent patch to define UTMP_READ_INCR
- Modified su.c to define default paths w/o regard to other header files or
  -D style definitions

* Wed Apr 02 1997 Erik Troan <ewt@redhat.com>
- Updated getutent patch for 1.16
- Added mktime patch for 64bit time_t

* Tue Mar 25 1997 Michael K. Johnson <johnsonm@redhat.com>
- DEFPATH handling moved from ...path.patch to _PATH_DEFPATH*

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved from pam.conf to pam.d
