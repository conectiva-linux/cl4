Summary: Privledged helper for utmp/wtmp updates
Summary(pt_BR): Programa para atualização do utmp/wtmp
Summary(es): Privledged helper for utmp/wtmp updates
Name: utempter
%define version 0.5
Version: %{version}
Release: 3cl
Copyright: MIT
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: utempter-%{version}.tar.gz
Prereq: /usr/sbin/groupadd, /sbin/ldconfig, fileutils
BuildRoot: /var/tmp/%{name}-root

%description
Utempter is a utility which allows some non-privileged
programs to have required root access, yet without
compromising system security. It accomplishes this task
by acting as a buffer between root and the programs.

%description -l pt_BR
O Utempter é um utilitários que permite a programas guardar informação
à arquivos privilegiados (/var/run/utmp), sem comprometer a segurança
do sistema. Ele faz esta tarefa atuando como um "buffer" entre o usuário
root e os programas.

%description -l es
Utempter is a utility which allows programs to log information to a
privledged file (/var/run/utmp), without compromising system security.
It accomplishes this task by acting as a buffer between root and the
programs.

%prep
%setup  -q

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%pre 
/usr/sbin/groupadd -r -f utmp

%post
/sbin/ldconfig

if [ -f /var/log/wtmp ]; then
    chown root.utmp /var/log/wtmp
    chmod 664 /var/log/wtmp
fi

if [ -f /var/run/utmp ]; then
    chown root.utmp /var/run/utmp
    chmod 664 /var/run/utmp
fi

%postun -p /sbin/ldconfig

%files
%attr(02755, root, utmp) /usr/sbin/utempter
/usr/lib/libutempter.so*
/usr/include/utempter.h

%changelog
* Sat Jun 12 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun  4 1999 Jeff Johnson <jbj@redhat.com>
- ignore SIGCHLD while processing utmp.
