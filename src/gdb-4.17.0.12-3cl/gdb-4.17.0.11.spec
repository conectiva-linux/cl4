Summary: A GNU source-level debugger for C, C++ and Fortran.
Summary(pt_BR): Depurador de programas C e outras linguagens
Summary(es): Depurador de programas C y otras lenguajes
Name: gdb
Version: 4.17.0.12
Release: 3cl
Copyright: GPL
Group: Development/Debuggers
Group(pt_BR): Desenvolvimento/Depuradores
Group(es): Desarrollo/Depuradores
Source: ftp://ftp.gnu.org/pub/gdb/gdb-4.17.tar.bz2
Patch0: ftp://ftp.varesearch.com/pub/support/hjl/gdb/gdb-4.17-4.17.0.12.diff.gz
Patch1: gdb-4.17.0.11-sparc.patch
Patch2: gdb-4.17-xref.patch
Patch3: gdb-4.17.0.11-kern22.patch
Buildroot: /var/tmp/%{name}-root
Prereq: /sbin/install-info

%description
Gdb is a full featured, command driven debugger. Gdb allows you
to trace the execution of programs and examine their internal state at any
time.  Gdb works for C and C++ compiled with the GNU C compiler gcc.

If you are going to develop C and/or C++ programs and use the GNU gcc
compiler, you may want to install gdb to help you debug your programs.

%description -l pt_BR
Este é um debugger orientado a comandos repleto de
características. Ele permite à você rastrear a execução de programas
e examinar o seu estado interno a qualquer momento. Ele funciona
para para C e C++ compilado com o compilador GNU C.

%description -l es
Este es un debugger orientado a comandos repleto de características.
Te permite rastrear la ejecución de programas y examinar su estado
interno a cualquier momento. Funciona para C y C++ compilado con
el compilador GNU C.

%prep
%setup -q -n gdb-4.17
%patch0 -p2
%patch1 -p1 -b .sparc
%patch2 -p1

%patch3 -p1 -b .kern22

%build
#OS=`echo ${RPM_OS} | tr '[A-Z]' '[a-z]'`
#CC=egcs CFLAGS="-O2 -g" ./configure --prefix=/usr ${RPM_ARCH}-redhat-${OS}

%configure
make
make info

%install
rm -rf $RPM_BUILD_ROOT

make install install-info prefix=$RPM_BUILD_ROOT/usr

rm -f $RPM_BUILD_ROOT/usr/info/dir $RPM_BUILD_ROOT/usr/info/dir.info*
rm -f $RPM_BUILD_ROOT/usr/info/bfd*
rm -f $RPM_BUILD_ROOT/usr/info/readline* $RPM_BUILD_ROOT/usr/info/history*
rm -f $RPM_BUILD_ROOT/usr/info/standard*
rm -f $RPM_BUILD_ROOT/usr/bin/{texindex,texi2dvi,makeinfo,install-info,info}
rm -f $RPM_BUILD_ROOT/usr/info/texinfo* ./usr/info/info*
gzip -9nf $RPM_BUILD_ROOT/usr/info/*info*
strip $RPM_BUILD_ROOT/usr/bin/*
rm -rf $RPM_BUILD_ROOT/usr/include $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/share


%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/gdb.info.gz /usr/info/dir
/sbin/install-info /usr/info/gdbint.info.gz /usr/info/dir
/sbin/install-info /usr/info/mmalloc.info.gz /usr/info/dir
/sbin/install-info /usr/info/stabs.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/gdb.info.gz /usr/info/dir
    /sbin/install-info --delete /usr/info/gdbint.info.gz /usr/info/dir
    /sbin/install-info --delete /usr/info/mmalloc.info.gz /usr/info/dir
    /sbin/install-info --delete /usr/info/stabs.info.gz /usr/info/dir
fi

%files
%defattr(-,root,root)
/usr/bin/*
/usr/man/*/*
/usr/info/*info*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 4.17.0.11 to 4.17.0.12

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- updated the kern22 patch with stuff from davem

* Thu Apr  1 1999 Jeff Johnson <jbj@redhat.com>
- sparc with 2.2 kernels no longer uses sunos ptrace (davem)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Mon Mar  8 1999 Jeff Johnson <jbj@redhat.com>
- Sparc fiddles for Red Hat 6.0.
