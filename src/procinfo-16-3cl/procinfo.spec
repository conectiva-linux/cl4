Summary: A tool for gathering and displaying system information.
Summary(pt_BR): Obtém informações usando o sistema de arquivos /proc
Summary(es): Obtiene información usando el sistema de archivos /proc
Name: procinfo
Version: 16
Release: 3cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://ftp.cistron.nl/pub/people/svm/procinfo-16.tar.gz
Patch0: procinfo-14-misc.patch
Patch1: procinfo-14-jbj.patch
Buildroot: /var/tmp/procinfo-root

%description
The procinfo command gets system data from the /proc directory
(the kernel filesystem), formats it and displays it on standard
output.  You can use procinfo to acquire information about your
system from the kernel as it is running.

Install procinfo if you'd like to use it to gather and display
system data.

%description -l pt_BR
O procinfo é um pacote que permite a você obter informações úteis
do /proc. /proc é o sistema de arquivos do kernel. Este é um lugar
onde você pode ir para obter informações sobre o seu kernel que
está rodando.

%description -l es
procinfo es un paquete que te permite obtener información útil
del /proc, que es el sistema de archivos del kernel. Este es un
lugar donde puedes ir para obtener información sobre el kernel que
estás ejecutando.

%prep
%setup -q
%patch0 -p1 -b .misc
%patch1 -p1 -b .jbj

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make install prefix=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO CHANGES
/usr/bin/procinfo
/usr/bin/lsdev
/usr/bin/socklist
/usr/man/man8/procinfo.8
/usr/man/man8/lsdev.8
/usr/man/man8/socklist.8

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 17 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 12 1999 Michael Maher <mike@redhat.com>
- updated to version 16
- closed bug 1349

* Fri Nov 20 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated to version 15 to fix bugzilla 70.

* Fri Oct  2 1998 Jeff Johnson <jbj@redhat.com>
- calculate time per-cent on non-{alpha,i386} correctly.

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 14
- fixed the spec file 

* Thu Apr 30 1998 Donnie Barnes <djb@redhat.com>
- updated from 0.11 to 13
- added socklist program

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- updated to version 0.11

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
