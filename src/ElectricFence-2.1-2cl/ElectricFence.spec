Summary: A debugger which detects memory allocation violations.
Summary(pt_BR): Electric Fence biblioteca de depuração de memória em C
Summary(es): Electric Fence biblioteca de depuración de memoria en C
Name: ElectricFence
Version: 2.1
Release: 2cl
Excludearch: alpha
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://ftp.perens.com/pub/ElectricFence/ElectricFence_2.1.tar.gz
Patch0: ElectricFence-2.0.5-glibc.patch
Patch1: ElectricFence-2.0.5-longjmp.patch
BuildRoot: /var/tmp/electricfence-root

%description
If you know what malloc() violations are, you'll be interested in
ElectricFence. ElectricFence is a tool which can be used for
C programming and debugging. It uses the virtual memory 
hardware of your system to detect when software overruns 
malloc() buffer boundaries, and/or to detect any accesses of
memory released by free(). ElectricFence will then stop 
the program on the first instruction that caused a bounds 
violation and you can use your favorite debugger to 
display the offending statement.

This package will install ElectricFence, which you can
use if you're searching for a debugger to find
malloc() violations.

%description -l pt_BR
Electric Fence é uma biblioteca que pode ser usada para programação e
depuração em C. Você o "linka" em tempo de compilação e ele o avisará
sobre possíveis problemas como liberação de memória não alocada, etc.

%description -l es
Electric Fence es una biblioteca que puede ser usada para
programación y depuración en C. Tu lo "linkas" en tiempo de
compilación y te avisará sobre posibles problemas, como liberación
de memoria no alocada, etc.

%prep
%setup -q -c ElectricFence
%patch0 -p1 -b .glibc
%patch1 -p1 -b .jmp

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib,man/man3}

make	LIB_INSTALL_DIR=$RPM_BUILD_ROOT/usr/lib \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT/usr/man/man3 \
	install

echo ".so man3/libefence.3" > $RPM_BUILD_ROOT/usr/man/man3/efence.3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
/usr/lib/libefence.a
/usr/man/man3/efence.3
/usr/man/man3/libefence.3

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Apr 10 1999 Matt Wilson <msw@redhat.com>
- version 2.1

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 13)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- create efence.3 (problem #830)

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- need to use sigsetjmp() and siglongjmp() for proper testing

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use ExcludeArch instead of Exclude

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
