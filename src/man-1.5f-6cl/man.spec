Summary: manual page reader
Summary(pt_BR): Leitor de páginas de manuais (man)
Summary(es): Lector de páginas de manual (man)
Name: man
Version: 1.5f
Release: 6cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
#Source0: ftp://sunsite.unc.edu/pub/Linux/apps/doctools/man-1.5f.tar.gz
# recompactado com o bzip2
Source0: ftp://sunsite.unc.edu/pub/Linux/apps/doctools/man-1.5f.tar.bz2
Source1: makewhatis.cron
Source2: man-1.5f-conectiva.patch
Source700: man-man-pt_BR.tar
Patch0: man-1.5f-manpath.patch
Buildroot: /var/tmp/man-root
Requires: groff
Summary(de): Manual-Page-Reader
Summary(fr): Lecteur de pages de man.
Summary(tr): Kýlavuz sayfasý okuyucusu

%description
The man page suite, including man, apropos, and whatis.  These
programs are used to read most of the documentation available
on a Linux system.  The whatis and apropos programs can be used
to find documentation related to a particular subject.

%description -l pt_BR
É um conjunto de páginas de manual, incluindo man, apropos e
whatis. Estes programas são usados para ler a maioria da documentação
disponível no sistema Linux. Os programas whatis e apropos podem ser
usados para achar documentação relacionada com um assunto particular.

%description -l es
Es un conjunto de páginas de manual, incluyendo man, apropos
y whatis. Estos programas se usan para leer la mayoría de la
documentación disponible en el sistema Linux. Los programas whatis
y apropos pueden ser usados para encontrar documentación relacionada
con un asunto particular.

%description -l de
Die man-Seiten-Suite, einschließlich Handbuch, Apropos und Whatis. 
Diese Programme dienen zum Einsehen des Großteils der Dokumentation, 
die auf einem Linux-System verfügbar ist. Die Whatis- und 
Apropos-Programme dienen dazu, Beschreibungen zu bestimmten Themen 
zu finden. 

%description -l fr
Ensemble des pages man. Contient man, apropos et whatis. Ces programmes
servent à lire la plupart de la documentation disponible sur un
système Linux. Les programmes whatis et apropos servent à trouver
la documentation relative à un sujet précis.

%description -l tr
Kýlavuz sayfa takýmý: man, apropos, whatis. Bu programlar Linux sisteminde
bulunan birçok belgenin okunmasýnda kullanylyr. whatis ve apropos programlarý
özel bir konu ile alakalý belgeleri bulmak için kullanýlabilir.

%changelog
* Fri May 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Dec  5 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Sun Nov 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Fri Sep 04 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated do 1.5f

* Sat Jun 13 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- use latin1

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5d

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.5a

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- uses a build root

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- updated to man-1.4j, which fixes some security problems; release 1 is
  for RH 4.2, release 2 is for glibc
 
* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Added /usr/lib/perl5/man to default manpath

%prep
%setup
%patch0 -p1 -b .manpath

%build
./configure -default
patch -p0 -s < $RPM_SOURCE_DIR/man-1.5f-conectiva.patch
make CC="gcc $RPM_OPT_FLAGS -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p  $RPM_BUILD_ROOT/usr/bin
mkdir -p  $RPM_BUILD_ROOT/usr/sbin
mkdir -p  $RPM_BUILD_ROOT/usr/man
mkdir -p  $RPM_BUILD_ROOT/etc/cron.weekly

make install BINROOTDIR="$RPM_BUILD_ROOT"
chmod 755 $RPM_BUILD_ROOT/usr/sbin/makewhatis
chown root.man $RPM_BUILD_ROOT/usr/bin/man
chmod 2755 $RPM_BUILD_ROOT/usr/bin/man

install -m755 $RPM_SOURCE_DIR/makewhatis.cron $RPM_BUILD_ROOT/etc/cron.weekly

mkdir -p $RPM_BUILD_ROOT/var/catman
chown root.man $RPM_BUILD_ROOT/var/catman
chmod 775 $RPM_BUILD_ROOT/var/catman
mkdir -p $RPM_BUILD_ROOT/var/catman/local
chown root.man $RPM_BUILD_ROOT/var/catman/local
chmod 775 $RPM_BUILD_ROOT/var/catman/local
mkdir -p $RPM_BUILD_ROOT/var/catman/X11
chown root.man $RPM_BUILD_ROOT/var/catman/X11
chmod 775 $RPM_BUILD_ROOT/var/catman/X11
for i in 1 2 3 4 5 6 7 8 9 n; do
	mkdir -p $RPM_BUILD_ROOT/var/catman/cat$i
	chown root.man $RPM_BUILD_ROOT/var/catman/cat$i
	chmod 775 $RPM_BUILD_ROOT/var/catman/cat$i
	mkdir -p $RPM_BUILD_ROOT/var/catman/local/cat$i
	chown root.man $RPM_BUILD_ROOT/var/catman/local/cat$i
	chmod 775 $RPM_BUILD_ROOT/var/catman/local/cat$i
	mkdir -p $RPM_BUILD_ROOT/var/catman/X11/cat$i
	chown root.man $RPM_BUILD_ROOT/var/catman/X11/cat$i
	chmod 775 $RPM_BUILD_ROOT/var/catman/X11/cat$i
done

strip $RPM_BUILD_ROOT/usr/bin/man



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/man-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config /etc/cron.weekly/makewhatis.cron
/usr/bin/man
/usr/bin/apropos
/usr/bin/whatis
/usr/sbin/makewhatis
%config /etc/man.config
/usr/man/man5/man.conf.5
/usr/man/man1/whatis.1
/usr/man/man1/man.1
/usr/man/man1/apropos.1

%dir /var/catman
%dir /var/catman/cat1
%dir /var/catman/cat2
%dir /var/catman/cat3
%dir /var/catman/cat4
%dir /var/catman/cat5
%dir /var/catman/cat6
%dir /var/catman/cat7
%dir /var/catman/cat8
%dir /var/catman/cat9
%dir /var/catman/catn
%dir /var/catman/local
%dir /var/catman/local/cat1
%dir /var/catman/local/cat2
%dir /var/catman/local/cat3
%dir /var/catman/local/cat4
%dir /var/catman/local/cat5
%dir /var/catman/local/cat6
%dir /var/catman/local/cat7
%dir /var/catman/local/cat8
%dir /var/catman/local/cat9
%dir /var/catman/local/catn
%dir /var/catman/X11
%dir /var/catman/X11/cat1
%dir /var/catman/X11/cat2
%dir /var/catman/X11/cat3
%dir /var/catman/X11/cat4
%dir /var/catman/X11/cat5
%dir /var/catman/X11/cat6
%dir /var/catman/X11/cat7
%dir /var/catman/X11/cat8
%dir /var/catman/X11/cat9
%dir /var/catman/X11/catn
%attr(0644,root,root) /usr/man/pt_BR/man*/*
