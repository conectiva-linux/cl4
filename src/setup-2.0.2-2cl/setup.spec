Summary: A set of system configuration and setup files.
Summary(pt_BR): Vários arquivos básicos de configuração
Summary(es): Varios archivos básicos de configuración
Name: setup
Version: 2.0.2
Release: 2cl
Copyright: public domain
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: setup-%{version}.tar.gz
Patch: setup.securetty.patch
Buildroot: /var/tmp/%{name}-root
BuildArchitectures: noarch

%description
The setup package contains a set of very important system
configuration and setup files, such as passwd, group,
profile and more.

You should install the setup package because you will
find yourself using its many features for system
administration.

%description -l pt_BR
Este pacote contém uma variedade de arquivos de configuração e
setup muito importantes, incluindo o passwd, group, arquivos de
"perfil", etc.

%description -l es
Este paquete contiene una variedad de archivos de configuración
y setup muy importantes, incluyendo el passwd, group, archivos de
"perfil", etc.

%prep
%setup -q -n setup
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
chmod 600 etc/securetty
cp -ar * $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/log
cp /dev/null $RPM_BUILD_ROOT/var/log/lastlog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%verify(not md5 size mtime) %config(noreplace) /etc/passwd
%verify(not md5 size mtime) %config(noreplace) /etc/group
%config /etc/services
%config /etc/exports
%config /etc/host.conf
%config /etc/hosts.allow
%config /etc/hosts.deny
%config /etc/motd
%config /etc/printcap
%config /etc/profile
%config /etc/protocols
%config(missingok) /etc/securetty
%config /etc/csh.cshrc
%dir /etc/profile.d
%verify(not md5 size mtime) /var/log/lastlog

%changelog
* Mon Jun 21 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- include tty9 thru tty12 in securetty

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- always use /etc/inputrc

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- added alias pointing to imap from imap2

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- updated protocols/services from debian to comply with more modern 
- IETF/RFC standards

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Thu Feb 18 1999 Jeff Johnson <jbj@redhat.com>
- unset variables used in /etc/csh.cshrc (#1212)

* Mon Jan 18 1999 Jeff Johnson <jbj@redhat.com>
- compile for Raw Hide.

* Tue Oct 13 1998 Cristian Gafton <gafton@redhat.com>
- fix the csh.cshrc re: ${PATH} undefined

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- /etc/profile uses $i, which needs to be unset

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- made /etc/passwd and /etc/group %config(noreplace)

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- removed /etc/inetd.conf, /etc/rpc
- flagged /etc/securetty as missingok
- fixed buildroot stuff in spec file

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Don't verify md5sum, size, or timestamp of /var/log/lastlog, /etc/passwd,
  or /etc/group.

