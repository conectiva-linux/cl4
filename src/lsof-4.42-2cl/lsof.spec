Summary: Lists files open by processes
Summary(pt_BR): Lista os arquivos abertos pelos processos que estão rodando.
Summary(es): Lista los archivos abiertos por los procesos que están en ejecución.
Name: lsof
Version: 4.42
Release: 2cl
Copyright: Free
Group: Development/Debuggers
Group(pt_BR): Desenvolvimento/Depuradores
Group(es): Desarrollo/Depuradores
Source0: ftp://vic.cc.purdue.edu/pub/tools/unix/lsof/lsof_%{version}_W.tar.gz
Patch1: lsof-4.40-K22.patch
Prefix: %{_prefix}
Buildroot: /var/tmp/%{name}-root

%description
Lsof's name stands for LiSt Open Files, and it does just that. It lists
information about files that are open by the processes running on a UNIX
system.

%description -l pt_BR
O nome lsof significa LiSt Open Files, e faz isto: lista os arquivos
abertos. Ele lista várias informações sobre os arquivos abertos
pelos processos que estão rodando em um sistema UNIX.

%description -l es
El nombre lsof significa LiSt Open Files, y lo que hace es: lista
los archivos abiertos. Hace una relación, con información variada,
sobre los archivos abiertos por los procesos en ejecución en un
sistema UNIX.

%prep
%setup -q -c -n lsof_%{version}

# add -a 1 above
#tar xzf %SOURCE1

#
# Sort out whether this is the wrapped or linux specific tar ball.
#
[ -f lsof_%{version}.tar ] && tar xf lsof_%{version}.tar
[ -d lsof_%{version}.linux -a ! -d lsof_%{version} ] && \
	mv lsof_%{version}.linux lsof_%{version}
[ -d lsof_%{version} ] && cd lsof_%{version}

%patch1 -p2 -b .K22

%build
rm -rf $RPM_BUILD_ROOT
[ -d lsof_%{version} ] && cd lsof_%{version}

#LINUX_KERNEL=`pwd`/../linux LSOF_INCLUDE=`pwd`/../linux/include \
#LSOF_VERS=20036 LSOF_VSTR=2.0.36 LINUX_BASE=/dev/kmem \
LSOF_VERS=22009 LSOF_VSTR=2.2.9 LINUX_BASE=/proc \
	./Configure -n linux

make

%install
rm -rf $RPM_BUILD_ROOT
#
# Sort out whether this is the wrapped or linux specific tar ball.
#
[ -d lsof_%{version} ] && cd lsof_%{version}
install -d ${RPM_BUILD_ROOT}%{_prefix}/{sbin,man/man8}
install -s lsof ${RPM_BUILD_ROOT}%{_prefix}/sbin
install lsof.8 ${RPM_BUILD_ROOT}%{_prefix}/man/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lsof_%{version}/00*
%attr(0755,root,kmem) %{_prefix}/sbin/lsof
%{_prefix}/man/man8/lsof.8

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 08 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 4.42 (security fix)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- turn off setgid kmem "just in case".

* Thu Feb 18 1999 Jeff Johnson <jbj@redhat.com>
- buffer overflow patch.
- upgrade to 4.40.

* Wed Dec 30 1998 Jeff Johnson <jbj@redhat.com>
- update to "official" 4.39 release.

* Wed Dec 16 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.39B (linux) with internal kernel src.

* Tue Dec 15 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.39A (linux)

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.37

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.36

* Thu Jul 23 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 4.35.
- rewrap for RH 5.2.

* Mon Jun 29 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [4.34-1]
- New version
- Spec rewriten to use %{name} and %{version} macros
- Removed old log enteries

* Tue Apr 28 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Built under RH5
- %install was changed
