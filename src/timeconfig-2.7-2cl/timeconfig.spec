Summary: Text mode tools for setting system time parameters.
Summary(pt_BR): Ferramenta modo Texto para configuração de fuso horário (timezone) e modo do relógio
Summary(es): Herramienta modo Texto para configuración de zona horaria (timezone) y modo del reloj
Name: timeconfig
%define version 2.7
Version: %{version}
Release: 2cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: timeconfig-%{version}.tar.gz
Source1: timeconfig-2.7-pt_BR.po
Patch: timeconfig-2.7-Brazil-East.patch
Requires: initscripts >= 2.81, glibc >= 2.0.5-5
Prereq: fileutils, gawk
BuildRoot: /var/tmp/timeconfig-root

%description
The timeconfig package contains two utilities:  timeconfig and setclock.
Timeconfig provides a simple text mode tool for configuring the time
parameters in /etc/sysconfig/clock and /etc/localtime. The setclock tool
sets the hardware clock on the system to the current time stored in the
system clock.

%description -l pt_BR
Esta é uma ferramenta simples para ajustar tanto o fuso horário
(timezone) quanto o modo com que o seu relógio do sistema armazena
o tempo. Ele roda em modo texto usando um sistema simples de janelas.

%description -l es
Esta es una herramienta sencilla para ajustar tanto la zona horaria
(timezone) como el modo con que tu reloj del sistema almacena
el tiempo. Se ejecuta en modo texto usando un sistema sencillo
de ventanas.

%prep
%setup -q
%patch -p1
cp -f $RPM_SOURCE_DIR/timeconfig-2.7-pt_BR.po po/pt_BR

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install
rm -f /usr/lib/zoneinfo

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -L /etc/localtime -a ! -e /etc/localtime ]; then
    ln -sf `ls -ld /etc/localtime | awk '{ print $11}' | sed 's/lib/share/'` /etc/localtime
fi

%files
%defattr(-,root,root)
/usr/sbin/timeconfig
/usr/sbin/setclock
/usr/man/man8/timeconfig.8
/usr/man/man8/setclock.8
/usr/share/locale/*/LC_MESSAGES/timeconfig.mo

%changelog
* Thu Jul 01 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated pt_BR translation
- defaults to Brazil/East

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- release for Red Hat Linux 6.0

* Tue Mar  9 1999 Jeff Johnson <jbj@redhat.com>
- add in_ID.po

* Sun Jan 10 1999 Matt Wilson <msw@redhat.com>
- rebuilt against newt 0.40

* Tue Dec 15 1998 Jeff Johnson <jbj@redhat.com>
- add ru.po.

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- built for Raw Hide (slang-1.2.2)

* Thu Oct 08 1998 Cristian Gafton <gafton@redhat.com>
- updated czech translation (and use cs instead of cz)

* Fri Sep 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- pt_BR man translations
- man tree, with Makefile
- top level Makefile calls make -C po clean & make -C man install

* Fri Sep 25 1998 Jeff Johnson <jbj@redhat.com>
- add sr.po.

* Sun Aug 02 1998 Erik Troan <ewt@redhat.com>
- added NEWT_FLAG_SCROLL to listbox creation for newt 0.30
- added --test

* Fri Jun 05 1998 Erik Troan <ewt@redhat.com>
- return 0 on success

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- many more translations

* Mon Apr 20 1998 Erik Troan <ewt@redhat.com>
- uses a build root
- added de and en_RN translations

* Mon Mar 23 1998 Erik Troan <ewt@redhat.com>
- shortended window a bit -- white (rather, blue) space is a good thing

* Sun Mar 22 1998 Erik Troan <ewt@redhat.com>
- added --back option

* Sat Oct 11 1997 Erik Troan <ewt@redhat.com>
- use proper flags for hwclock

* Tue Sep 16 1997 Erik Troan <ewt@redhat.com>
- instead of creating /usr/lib/zoneinfo, just update /etc/localtime

* Wed Sep 10 1997 Erik Troan <ewt@redhat.com>
- look for zoneinfo in /usr/share instead of /usr/lib
- provide /usr/lib/zoneinfo symlink
