Summary: Red Hat Backup Utility
Summary(pt_BR): Utilitário de backup Red Hat
Summary(es): Utilitario de copia de seguridad Red Hat
Name: rhbackup
Version: 0.2
Release: 4cl
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://ftp.redhat.com/pub/code/rhbackup/rhbackup-%{PACKAGE_VERSION}.tar.gz
Copyright: GPL
BuildRoot: /var/tmp/rhbackup
#Requires: tar, /usr/bin/rsh, mt-st, /bin/hostname, fileutils, grep, sh-utils
Requires: tar
Requires: rsh
Requires: mt-st
Requires: net-tools
Requires: fileutils
Requires: grep
Requires: sh-utils
BuildArchitectures: noarch

%description
rhbackup is a backup utility that can be used for local and remote
backups.  This should be considered alpha quality software and should
be used with care.

%description -l pt_BR
Rhbackup é um utilitário de backup que pode ser usado para backup
local e remoto. Deve ser considerado um software de qualidade alfa
e ser usado com cuidado.

%description -l es
Rhbackup es un utilitario de copias de seguridad que puede ser
usado para copia local y remota. Debe ser considerado un software
de calidad alfa y ser usado con cuidado.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- fixed prereqs

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations


* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>

- updated from 0.1 to 0.2 (seems to have been tested a bit)
- man page cleanups

%prep
%setup

rm -rf $RPM_BUILD_ROOT

%install
./Install $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README
/usr/sbin/rhbackup
/usr/man/man8/rhbackup.8
%config /etc/backuptab
%config /etc/sysconfig/tape
