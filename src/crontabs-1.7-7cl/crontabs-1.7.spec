Summary: Root crontab files used to schedule the execution of programs.
Summary(pt_BR): Arquivo root crontab
Summary(es): Archivo root crontab
Name: crontabs
Version: 1.7
Release: 7cl
Copyright: public domain
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source0: crontab
Source1: run-parts
Requires: tmpwatch
BuildArchitectures: noarch
BuildRoot: /var/tmp/crontabs-root

%description
The crontabs package contains root crontab files.  Crontab is the
program used to install, uninstall or list the tables used to drive the
cron daemon.  The cron daemon checks the crontab files to see when
particular commands are scheduled to be executed.  If commands are
scheduled, it executes them.

Crontabs handles a basic system function, so it should be installed on
your system.

%description -l pt_BR
Arquivo crontab do root que é usado para agendar execuções de
vários programas.

%description -l es
Archivo crontab del root que se usa para agendar ejecuciones de
varios programas.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/cron.{hourly,daily,weekly,monthly}
mkdir -p $RPM_BUILD_ROOT/usr/bin

install -m644 $RPM_SOURCE_DIR/crontab $RPM_BUILD_ROOT/etc/crontab
install -m755 $RPM_SOURCE_DIR/run-parts $RPM_BUILD_ROOT/usr/bin/run-parts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/crontab
/usr/bin/run-parts
%dir /etc/cron.hourly
%dir /etc/cron.daily
%dir /etc/cron.weekly
%dir /etc/cron.monthly

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- don't run .rpm{save,new,orig} files (bug #2190)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Mon Nov 30 1998 Bill Nottingham <notting@redhat.com>
- crontab: set HOME=/

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- run-parts: skip sub-directories (e.g. CVS) found instead of complaining

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- moved crontab jobs up a bit to make sure they aren't confused by
  switching to and fro daylight savings time
  
* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- removed tmpwatch and at entries

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
