Summary: The Vixie cron daemon for executing specified programs at set times.
Summary(pt_BR): Deamon cron vixie
Summary(es): Deamon cron vixie
Name: vixie-cron
Version: 3.0.1
Release: 34cl
Copyright: distributable
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source0: ftp://ftp.vix.com/pub/vixie/vixie-cron-3.0.1.tar.bz2
Source1: vixie-cron.init
Source2: cron.log
Source700: vixie-cron-man-pt_BR.tar
Patch0: vixie-cron-3.0.1-redhat.patch
Patch1: vixie-cron-3.0.1-security.patch
Patch3: vixie-cron-3.0.1-badsig.patch
Patch4: vixie-cron-3.0.1-crontab.patch
Patch5: vixie-cron-3.0.1-sigchld.patch
Patch6: vixie-cron-3.0.1-sprintf.patch
Patch7: vixie-cron-3.0.1-sigchld2.patch
Patch8: vixie-cron-3.0.1-crond.patch
Patch9: vixie-cron-3.0.1-dst.patch
Buildroot: /var/tmp/cron-root
Prereq: chkconfig

%description
The vixie-cron package contains the Vixie version of cron.  Cron is a
standard UNIX daemon that runs specified programs at scheduled times.
Vixie cron adds better security and more powerful configuration options
to the standard version of cron.

%description -l pt_BR
O cron é um programa padrão do UNIX que roda programas especificados
pelo usuário em horários e dias agendados. O vixie cron adiciona
várias características ao cron básico do UNIX, incluindo melhor
segurança e opções mais poderosas de configuração.

%description -l es
cron es un programa padrón del UNIX que ejecuta programas
especificados por el usuario en horarios y días agendados.
Vixie cron adiciona varias características al cron básico del UNIX,
incluido mejor seguridad y opciones más potentes de configuración.

%prep
%setup
%patch0 -p1 -b .norh
%patch1 -p1 -b .nomisc
%patch3 -p1 -b .badsig
%patch4 -p1 -b .crontabhole
%patch5 -p1 -b .sigchld
%patch6 -p1 -b .sprintf
%patch7 -p1 -b .sigchld
%patch8 -p1 -b .crond
%patch9 -p1 -b .dst

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man{1,5,8},sbin}
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/{init.d,rc{0,1,2,3,4,5,6}.d}
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/spool/cron
chmod 700 $RPM_BUILD_ROOT/var/spool/cron
mkdir -p $RPM_BUILD_ROOT/etc/cron.d
chmod 755 $RPM_BUILD_ROOT/etc/cron.d

install -m755 $RPM_SOURCE_DIR/vixie-cron.init $RPM_BUILD_ROOT/etc/rc.d/init.d/crond
cd $RPM_BUILD_ROOT/etc/rc.d
ln -sf ../init.d/crond rc0.d/K60crond
ln -sf ../init.d/crond rc1.d/K60crond
ln -sf ../init.d/crond rc2.d/S40crond
ln -sf ../init.d/crond rc3.d/S40crond
ln -sf ../init.d/crond rc5.d/S40crond
ln -sf ../init.d/crond rc6.d/K60crond

mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m644 $RPM_SOURCE_DIR/cron.log $RPM_BUILD_ROOT/etc/logrotate.d/cron



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/vixie-cron-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add crond

%postun
if [ $1 = 0 ]; then 
    /sbin/chkconfig --del crond
    rm -fr /var/log/cron.*
fi

%files
%defattr(-,root,root)

/usr/sbin/crond
/usr/bin/crontab
/usr/man/man8/crond.8
/usr/man/man8/cron.8
/usr/man/man5/crontab.5
/usr/man/man1/crontab.1
%dir /var/spool/cron
%dir /etc/cron.d
%config(missingok) /etc/rc.d/rc0.d/K60crond
%config(missingok) /etc/rc.d/rc1.d/K60crond
%config(missingok) /etc/rc.d/rc2.d/S40crond
%config(missingok) /etc/rc.d/rc3.d/S40crond
%config(missingok) /etc/rc.d/rc5.d/S40crond
%config(missingok) /etc/rc.d/rc6.d/K60crond
%config /etc/rc.d/init.d/crond
%config /etc/logrotate.d/cron
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Thu May 20 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- i18n vixie-cron.init
- Added translations to pt_BR and es
- Added pt_BR man pages to package
- Fixed prereqs to chkconfig

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- add note to man page about DST conversion causing strangeness
- documented cron.d patch

* Tue Apr 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- improved cron.d patch

* Mon Apr 12 1999 Erik Troan <ewt@redhat.com>
- added cron.d patch

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate changes

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- clean up log files on deinstallation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 28)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- reset SIGCHLD before grandchild execle (problem #732)

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- added a patch to get rid of the dangerous sprintf() calls
- added BuildRoot and Prereq: /sbin/chkconfig

* Sun Nov 09 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed cron/crond dichotomy in init file.

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- fixed bad init symlinks

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- force it to use SIGCHLD instead of defunct SIGCLD

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- updated for chkconfig
- added status, restart options to init script

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Wed Feb 19 1997 Erik Troan <ewt@redhat.com>
- Switch conditional from "axp" to "alpha" 

