Summary: System log watcher and alarm
Summary(pt_BR): Alarme e analisador dos log do sistema
Summary(es): Alarma y analista de los log del sistema
Name: swatch
Version: 2.2
Release: 6cl
Copyright: Distributable
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://ftp.stanford.edu/general/security-tools/swatch/swatch-2.2.tar.gz
Patch0: swatch-2.2-redhat.patch
Patch1: swatch-2.2-nobr.patch
BuildArchitectures: noarch
BuildRoot: /var/tmp/swatch-root

%description
Swatch is used to monitor log files.  When it sees a line matching
a pattern you specify, it can highlight it and print it out, or run
external programs to notify you through mail or some other means.

%description -l pt_BR
Swatch é usado para monitorar arquivos log. Quando ele vê uma linha
combinando com o modelo que você especifica, ele pode destacá-la
e imprimí-la, ou rodar programas externos para notificá-lo através
de mail ou outros meios.

%description -l es
Swatch se usa para monitorar archivos log. Cuando ve una línea
combinando con el modelo que tu especificas, puede destacarla y
imprimirla, o ejecutar programas externos para notificarlo a través
de mail o otros medios.

%prep
%setup -q
%patch0 -p1 -b .redhat
%patch1 -p1 -b .nobr

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,man/man5,man/man8}

perl install.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/swatch
/usr/lib/sw_actions.pl
/usr/lib/sw_history.pl
/usr/man/man5/swatch.5
/usr/man/man8/swatch.8
%doc *.ps config_files README Changes

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- fixed paths

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- updated to 2.2

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
