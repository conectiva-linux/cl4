Summary: Tracks and displays system calls associated with a running process.
Summary(pt_BR): Mostra as chamadas de sistema de um processo rodando
Summary(es): Enseña las llamadas de sistema de un proceso en ejecución
Name: strace
Version: 3.1
Release: 18cl
Copyright: distributable
Group: Development/Debuggers
Group(pt_BR): Desenvolvimento/Depuradores
Group(es): Desarrollo/Depuradores
Source: ftp.std.com:/pub/jrs/strace-3.1.tar.bz2
Patch0: strace-3.0.14elf.patch.bz2
Patch1: ftp://ftp.azstarnet.com/pub/linux/axp/glibc/strace-3.1-glibc.patch
Patch2: strace-3.1-sparc.patch.bz2
Patch3: strace-3.1-sparcglibc.patch
Patch4: strace-3.1-sparc2.patch
Patch5: strace-3.1-sparc3.patch
Patch6: strace-3.1-sparc4.patch
Patch7: strace-3.1-prctldomainname.patch
Patch8: strace-3.1-alpha.patch
Patch9: strace-3.1-gafton.patch
Patch10: strace-3.1-sparc5.patch
Patch11: strace-3.1-jbj.patch
Patch12: strace-3.1-arm.patch
Patch13: strace-3.1-compat21.patch
Patch14: strace-3.1-clone.patch
Patch15: strace-3.1-vfork.patch
BuildRoot: /var/tmp/%{name}-root

%description
The strace program intercepts and records the system calls called
and received by a running process.  Strace can print a record of
each system call, its arguments and its return value.  Strace is useful
for diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%description -l pt_BR
Strace imprime uma "gravação" de cada chamada de sistema que o
programa faz, incluindo todos os argumentos passados para ele e se
o retorno de cada chamada de sistema é verdadeiro ou gerou erro.

%description -l es
Strace imprime una "grabación" de cada llamada de sistema que el
programa hace, incluyendo todos los argumentos pasados para él,
si la vuelta de cada llamada de sistema es verdadera, o si hay
creado error.

%prep
%setup -q

%patch0 -p1 -b .elf
%patch1 -p1 -b .glibc
%patch2 -p1 -b .sparc
%patch3 -p1 -b .sparcglibc
%patch4 -p1 -b .sparc2
%patch5 -p1 -b .sparc3
%patch6 -p1 -b .sparc4
%patch7 -p1 -b .misc
%patch8 -p1 -b .alpha
%patch9 -p1 -b .gafton
%patch10 -p1 -b .sparc5
%patch11 -p1 -b .jbj
%patch12 -p1 -b .arm
%patch13 -p1 -b .compat21
%patch14 -p0 -b .clone
%patch15 -p1 -b .vfork

%build
autoconf
OS=`echo ${RPM_OS} | tr '[A-Z]' '[a-z]'`
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr ${RPM_ARCH}-redhat-${OS}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}
make install prefix=$RPM_BUILD_ROOT/usr
strip $RPM_BUILD_ROOT/usr/bin/strace

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/strace
/usr/man/man1/strace.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  1 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binary

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 16)

* Tue Feb  9 1999 Jeff Johnson <jbj@redhat.com>
- vfork est arrive!

* Tue Feb  9 1999 Christopher Blizzard <blizzard@redhat.com>
- Add patch to follow clone() syscalls, too.

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- patch to build alpha/sparc with glibc 2.1.

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch to build on ARM

* Wed Sep 30 1998 Jeff Johnson <jbj@redhat.com>
- fix typo (printf, not tprintf).

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- fix compile problem on sparc.

* Tue Aug 18 1998 Cristian Gafton <gafton@redhat.com>
- buildroot

* Mon Jul 20 1998 Cristian Gafton <gafton@redhat.com>
- added the umoven patch from James Youngman <jay@gnu.org>
- fixed build problems on newer glibc releases

* Mon Jun 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
