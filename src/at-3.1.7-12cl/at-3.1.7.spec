Summary: at job spooler
Summary(pt_BR): Spooler de jobs at
Summary(es): Spooler de jobs at
Name: at
Version: 3.1.7
Release: 12cl
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
#Source: ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/at-3.1.7.tar.gz
# recompactado com o bzip2
Source: ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/at-3.1.7.tar.bz2
Source2: atd.init
Source700: at-man-pt_BR.tar
Patch: at-3.1.7-lockfile.patch
Patch2: at-3.1.7-paths.patch
Patch3: at-config.sub.patch
Buildroot: /var/tmp/at-root
Prereq: fileutils chkconfig
Conflicts: crontabs <= 1.5
Summary(de): at-Job-Spooler
Summary(fr): Gestionnaire de taches at.
Summary(tr): Ýþ düzenleyici

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Mar 13 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 10 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscript i18n (gprintf)

* Thu Feb 18 1999 Conectiva <dist@conectiva.com>
- man pages novas/revisadas

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- at.init internationalized and translated to pt_BR

* Tue May 05 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>

- enhanced initscript

* Sun Nov 09 1997 Michael K. Johnson <johnsonm@redhat.com>

- learned to spell

* Wed Oct 22 1997 Michael K. Johnson <johnsonm@redhat.com>

- updated to at version 3.1.7
- updated lock and sequence file handling with %ghost
- Use chkconfig and atd, now conflicts with old crontabs packages

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>

- built against glibc

%description
at and batch read commands from standard input or a specified file
which are to be executed at a later time, using /bin/sh.

%description -l pt_BR
at e batch lêem comandos da entrada padrão ou de um arquivo
especificado que são executados mais tarde, usando /bin/sh.

%description -l es
at y batch leen comandos de la entrada padrón o de un archivo
especificado que son ejecutados más tarde, usando /bin/sh.

%description -l de
Stapelverarbeitung von Lesebefehlen von einer Standard- oder einer 
genannten Datei zu einem späteren Zeitpunkt unter Verwendung von /bin/sh.

%description -l fr
at et batch lisent, sur l'entrée standard ou dans un fichier, des
commandes qui doivent être exécutées plus tard en utilisant /bin/sh.

%description -l tr
at ve batch /bin/sh kabuðunu kullanarak, belli bir saatte çalýþtýrmak üzere
standart giriþden ya da bir dosyadan komut okur.

%prep
%setup
%patch3 -p0
%patch -p1 -b .lockfile
# The next path is a brute-force fix that will have to be updated
# when new versions of at are released.
%patch2 -p1 -b .paths
./configure --with-atspool=/var/spool/at/spool --with-jobdir=/var/spool/at

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
make install IROOT=$RPM_BUILD_ROOT
echo > $RPM_BUILD_ROOT/etc/at.deny
mkdir docs
cp $RPM_BUILD_ROOT/usr/doc/at/* docs/
install -o 0 -g 0 -m 755 $RPM_SOURCE_DIR/atd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/atd





mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/at-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch /var/spool/at/.SEQ
chmod 600 /var/spool/at/.SEQ
chown daemon.daemon /var/spool/at/.SEQ
/sbin/chkconfig --add atd

%preun
if [ "$1" = 0 ] ; then
  /sbin/chkconfig --del atd
fi

%files
%doc docs/*
%dir /var/spool/at
%dir /var/spool/at/spool
%config /etc/at.deny
%config /etc/rc.d/init.d/atd
%attr(0644,root,root) /usr/man/pt_BR/man*/*
%ghost /var/spool/at/.SEQ
/usr/sbin/atrun
/usr/sbin/atd
/usr/man/man8/atrun.8
/usr/man/man8/atd.8
/usr/man/man1/batch.1
/usr/man/man1/atrm.1
/usr/man/man1/atq.1
/usr/man/man1/at.1
/usr/bin/batch
/usr/bin/atrm
/usr/bin/atq
/usr/bin/at
