Summary: System logging and kernel message trapping daemons.
Summary(pt_BR): Registrador de log do sistema linux
Summary(es): Registrador de log del sistema linux
Name: sysklogd
Version: 1.3.31
Release: 8cl
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://sunsite.unc.edu/pub/Linux/system/daemons/sysklogd-1.3-31.tar.gz
Source1: syslog.conf.rhs
Source2: syslog.init
Source3: syslog.log
Patch1: sysklogd-1.3-alpha.patch
Patch2: sysklogd-1.3-rh.patch
Patch3: sysklogd-1.3-utmp-process.patch
Patch4: sysklogd-1.3-sparc.patch
# needed for 4.2 alpha
Patch5: sysklogd-1.3-alphafoo.patch
Prereq: fileutils, chkconfig
Requires: logrotate
BuildRoot: /var/tmp/syslog-root

%description
The sysklogd package contains two system utilities (syslogd and klogd)
which provide support for system logging.  Syslogd and klogd run as
daemons (background processes) and log system messages to different
places, like sendmail logs, security logs, error logs, etc.

%description -l pt_BR
Este é o programa de log para o kernel e o sistema Linux. Ele roda
como um daemon (processo em background) para registrar mensagens
em diferentes lugares. Estes são geralmente registros do sendmail,
segurança, e mensagens de outros daemons.

%description -l es
Este es el programa de log para el kernel y el sistema Linux. Se
ejecuta como un daemon (proceso en background) para registrar
mensajes en diferentes lugares. Estos son generalmente registros
del sendmail, seguridad, y mensajes de otros daemons.

%prep
%setup -q -n sysklogd-1.3-31
%patch1 -p1 -b .alpha
%patch2 -p1 -b .rh
%patch3 -p1 -b .utmp
%patch4 -p1 -b .sparc
%patch5 -p1 -b .alphafoo

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc,usr/{bin,man/man{5,8},sbin}}

make install TOPDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
install -m644 $RPM_SOURCE_DIR/syslog.conf.rhs ./etc/syslog.conf
strip $RPM_BUILD_ROOT/usr/sbin/*

mkdir -p $RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d}
install -m755 $RPM_SOURCE_DIR/syslog.init $RPM_BUILD_ROOT/etc/rc.d/init.d/syslog
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc{0,1,2,3,4,5,6}.d
ln -sf ../init.d/syslog $RPM_BUILD_ROOT/etc/rc.d/rc0.d/K99syslog
ln -sf ../init.d/syslog $RPM_BUILD_ROOT/etc/rc.d/rc1.d/K99syslog
ln -sf ../init.d/syslog $RPM_BUILD_ROOT/etc/rc.d/rc2.d/S30syslog
ln -sf ../init.d/syslog $RPM_BUILD_ROOT/etc/rc.d/rc3.d/S30syslog
ln -sf ../init.d/syslog $RPM_BUILD_ROOT/etc/rc.d/rc5.d/S30syslog
ln -sf ../init.d/syslog $RPM_BUILD_ROOT/etc/rc.d/rc6.d/K99syslog
install -m644  $RPM_SOURCE_DIR/syslog.log $RPM_BUILD_ROOT/etc/logrotate.d/syslog

chmod 755 $RPM_BUILD_ROOT/usr/sbin/syslogd
chmod 755 $RPM_BUILD_ROOT/usr/sbin/klogd

%clean
rm -rf $RPM_BUILD_ROOT

%post
for n in /var/log/{messages,secure,maillog,spooler}
do
	[ -f $n ] && continue
	touch $n
	chmod 600 $n
done
/sbin/chkconfig --add syslog

%preun
if [ $1 = 0 ]; then
   /sbin/chkconfig --del syslog
fi

%files
%defattr(-,root,root)
%doc ANNOUNCE README* NEWS INSTALL Sysklogd-1.3.lsm
%config /etc/syslog.conf
%config /etc/logrotate.d/syslog
%config /etc/rc.d/init.d/syslog
%config(missingok) /etc/rc.d/rc0.d/K99syslog
%config(missingok) /etc/rc.d/rc3.d/S30syslog
%config(missingok) /etc/rc.d/rc1.d/K99syslog
%config(missingok) /etc/rc.d/rc5.d/S30syslog
%config(missingok) /etc/rc.d/rc2.d/S30syslog
%config(missingok) /etc/rc.d/rc6.d/K99syslog
/usr/sbin/*
/usr/man/*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Fixed Prereq

* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- i18n initscripts

* Tue Apr 13 1999 Bill Nottingham <notting@redhat.com>
- log boot messages to boot.log
- actually put the sysklogd links in the new place

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- disable mark ticks by default

* Thu Apr  1 1999 Bill Nottingham <notting@redhat.com>
- stop klogd/syslogd as late as possible.

* Fri Mar 26 1999 Bill Nottingham <notting@redhat.com>
- twiddle initscript to avoid confusion

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Wed Feb 24 1999 Bill Nottingham <notting@redhat.com>
- update to sysklogd-1.3-31
- stop klogd *before* syslogd

* Tue Feb  9 1999 Jeff Johnson <jbj@redhat.com>
- escape naked percent chars in kernel messages (#1088).

* Thu Dec 17 1998 Jeff Johnson <jbj@redhat.com>
- rework last-gasp address-in-module oops trace for both 2.0.x/2.1.x modules.

* Mon Dec  7 1998 Jakub Jelinek <jj@ultra.linux.cz>
- make klogd translate SPARC register dumps and oopses.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- add %clean

* Tue Aug  4 1998 Chris Adams <cadams@ro.com>
- only log to entries that are USER_PROCESS (fix #822)

* Mon Jul 27 1998 Jeff Johnson <jbj@redhat.com>
- remove RPM_BUILD_ROOT from %post

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- patch to support Buildroot
- package is now buildrooted

* Wed Apr 29 1998 Michael K. Johnson <johnsonm@redhat.com>
- Added exit patch so that a normal daemon exit is not flagged as an error.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added (missingok) to init symlinks

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- added status|restart support to syslog.init
- added chkconfig support
- various spec file cleanups

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
