Summary: Utilities for monitoring your system and processes on your system.
Summary(pt_BR): Utilitários de monitoração de processos
Summary(es): Utilitarios de monitoración de procesos
Name: procps
%define major_version 2
%define minor_version 0
%define revision 2
%define version %{major_version}.%{minor_version}.%{revision}
Version: %{version}
Release: 2cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/procps-%{version}.tar.gz
Source700: procps-man-pt_BR.tar
Source800: procps-wmconfig.i18n.tgz
BuildRoot: /var/tmp/procps-root

%package X11
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Summary: X based process monitoring utilities.
Summary(pt_BR): Utilitários de monitoração de processos para X Window
Summary(es): Utilitarios de monitoración de procesos para X Window

%description
The procps package contains a set of system utilities which provide
system information.  Procps includes ps, free, skill, snice,
tload, top, uptime, vmstat, w, and watch.  The ps command displays
a snapshot of running processes.  The top command provides a
repetitive update of the statuses of running processes.  The free
command displays the amounts of free and used memory on your system.
The skill command sends a terminate command (or another
specified signal) to a specified set of processes.  The snice
command is used to change the scheduling priority of specified
processes.  The tload command prints a graph of the current system
load average to a specified tty.  The uptime command displays the
current time, how long the system has been running, how many users
are logged on and system load averages for the past one, five and
fifteen minutes.  The w command displays a list of the users who
are currently logged on and what they're running.  The watch program
watches a running program.  The vmstat command displays virtual
memory statistics about processes, memory, paging, block I/O, traps
and CPU activity.

%description -l pt_BR
Um pacote de utilitários que relatam o estado do sistema. É dado
ênfase aos processos em execução, total de memória disponível e
aos usuários que estão logados no sistema.

%description -l es
Un paquete de utilitarios que relatan el estado del sistema. Se da
énfasis a los procesos en ejecución, total de memoria disponible
y a los usuarios que están "logados" en el sistema.

%description X11
The procps-X11 package contains the XConsole shell script, a backwards
compatibility wrapper for the xconsole program.

%description -l pt_BR X11
Um pacote de utilitários X que reportam o estado do sistema.
Estes utilitários geralmente fornecem apresentações gráficas de
informações disponíveis a partir de ferramentas no conjunto procps.

%description -l es X11
Un paquete de utilitarios X que hacen referencia al estado del
sistema.  Estos utilitarios generalmente ofrecen presentaciones
gráficas de la información disponible a partir de herramientas en
el conjunto procps.

%prep
%setup -q

%build
PATH=/usr/X11R6/bin:$PATH

make CC="gcc $RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1 $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/usr/X11R6/bin

make DESTDIR=$RPM_BUILD_ROOT install

# Since this is specific to Red Hat Linux, we'll leave this in the spec file.
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 644 top.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/top





mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/procps-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

tar xvfpz $RPM_SOURCE_DIR/procps-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post
# add libproc to the cache
/sbin/ldconfig
# remove obsolete files
rm -f /etc/psdevtab /etc/psdatabase

%files
%defattr(0644,root,root,755)
%attr(0644,root,root) %config(missingok) /etc/X11/wmconfig/top
%doc NEWS BUGS TODO
%attr(755,root,root) /lib/libproc.so.2.0.0
%attr(555,root,root) /bin/ps
%attr(555,root,root) /usr/bin/oldps
%attr(555,root,root) /usr/bin/uptime
%attr(555,root,root) /usr/bin/tload
%attr(555,root,root) /usr/bin/free
%attr(555,root,root) /usr/bin/w
%attr(555,root,root) /usr/bin/top
%attr(555,root,root) /usr/bin/vmstat
%attr(555,root,root) /usr/bin/watch
%attr(555,root,root) /usr/bin/skill
%attr(555,root,root) /usr/bin/snice
%attr(0644,root,root) /usr/man/man1/free.1
%attr(0644,root,root) /usr/man/man1/ps.1
%attr(0644,root,root) /usr/man/man1/oldps.1
%attr(0644,root,root) /usr/man/man1/skill.1
%attr(0644,root,root) /usr/man/man1/snice.1
%attr(0644,root,root) /usr/man/man1/tload.1
%attr(0644,root,root) /usr/man/man1/top.1
%attr(0644,root,root) /usr/man/man1/uptime.1
%attr(0644,root,root) /usr/man/man1/w.1
%attr(0644,root,root) /usr/man/man1/watch.1
%attr(0644,root,root) /usr/man/man8/vmstat.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%files X11
%attr(0755,root,root) /usr/X11R6/bin/XConsole

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- i18n wmconfig
