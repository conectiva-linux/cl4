Summary: A public domain Yacc parser generator.
Summary(pt_BR): Yacc, gerador de parser de domínio público
Summary(es): Yacc, generador de parser de dominio público
Name: byacc
Version: 1.9
Release: 13cl
Copyright: public domain
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://ftp.cs.berkeley.edu/ucb/4bsd/byacc.1.9.tar.Z
Patch0: byacc-1.9-fixmanpage.patch
BuildRoot: /var/tmp/byacc-root

%description
Byacc (Berkeley Yacc) is a public domain LALR parser generator which
is used by many programs during their build process.  

If you are going to do development on your system, you will want to install
this package.

%description -l pt_BR
Este é um analisador gramatical yacc de domínio público. Ele é
usado em vários programas durante seu processo de construção. Você
provavelmente vai querer este pacote se você faz desenvolvimento.

%description -l es
Este es un analista gramatical yacc de dominio público. Se usa en
varios programas durante su proceso de construcción. Probablemente
querrás este paquete si te dedicas al desarrollo.

%prep
%setup -q -c
%patch -p1 -b .fixmanpage

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -m 755 -s yacc $RPM_BUILD_ROOT/usr/bin/yacc
install -m 644 yacc.1 $RPM_BUILD_ROOT/usr/man/man1/yacc.1
ln -sf yacc $RPM_BUILD_ROOT/usr/bin/byacc
ln -sf yacc.1 $RPM_BUILD_ROOT/usr/man/man1/byacc.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/yacc
/usr/bin/byacc
/usr/man/man1/yacc.1
/usr/man/man1/byacc.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Apr 07 1999 Preston Brown <pbrown@redhat.com>
- man page fixed.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 10)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- various spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
