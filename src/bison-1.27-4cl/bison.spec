Summary: A GNU general-purpose parser generator.
Summary(pt_BR): Gerador de parser da GNU
Summary(es): Generador de parser de la GNU
Name: bison
Version: 1.27
Release: 4cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://prep.ai.mit.edu/pub/gnu/bison-%{version}.tar.gz
Prereq: info
Buildroot: /var/tmp/%{name}-root

%description
Bison is a general purpose parser generator which converts a grammar
description for an LALR context-free grammar into a C program to parse
that grammar.  Bison can be used to develop a wide range of language
parsers, from ones used in simple desk calculators to complex programming
languages.  Bison is upwardly compatible with Yacc, so any correctly
written Yacc grammar should work with Bison without any changes.  If
you know Yacc, you shouldn't have any trouble using Bison (but you do need
to be very proficient in C programming to be able to use Bison).  Many
programs use Bison as part of their build process. Bison is only needed
on systems that are used for development.

If your system will be used for C development, you should install Bison
since it is used to build many C programs.

%description -l pt_BR
Este é o gerador de análise gramatical GNU que é mais compatível
com yacc. Vários programas o utilizam como parte do seu processo de
construção. Bison é somente necessário em sistemas que são usados
para desenvolvimento.

%description -l es
Este es el creador de análisis gramatical GNU  más compatible
con yacc.  Varios programas lo utilizan como parte del su proceso
de construcción.  Bison solamente hace falta en sistemas que se
usan para desarrollo.

%prep
%setup -q

%build
#./configure --prefix=/usr

%configure --datadir=/usr/lib
make LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr datadir=$RPM_BUILD_ROOT/usr/lib
gzip -n -9f $RPM_BUILD_ROOT/usr/info/bison.info*
strip $RPM_BUILD_ROOT/usr/bin/*

%post
/sbin/install-info /usr/info/bison.info.gz /usr/info/dir --entry="* bison: (bison).                        The GNU parser generator."

%preun
if [ $1 = 0 ]; then
  /sbin/install-info --delete /usr/info/bison.info.gz /usr/info/dir --entry="* bison: (bison).                        The GNU parser generator."
fi

%files
/usr/man/*/*
/usr/lib/*
/usr/info/bison.info*
/usr/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Fixed prereqs

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Mon Mar  8 1999 Jeff Johnson <jbj@redhat.com>
- configure with datadir=/usr/lib (#1386).

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- updated text in spec file.
- update to 1.27

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- built for Manhattan
- added build root

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- various spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
