Summary: An implementation of the Scheme programming language.
Summary(pt_BR): Interpretador de esquema da Universidade de Massachusetts em Boston
Summary(es): Interpretador de esquema de la Universidad de Massachusetts en Boston
Name: umb-scheme
Version: 3.2
Release: 9cl
Copyright: GPL
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source: ftp://ftp.cs.umb.edu/pub/scheme/umb-scheme-3.2.tar.gz
Patch0: umb-scheme-3.2-misc.patch
Patch1: umb-scheme-3.2-texinfo.patch
Patch2: umb-scheme-3.2-config.patch
Patch3: umb-scheme-3.2-man.patch
BuildRoot: /var/tmp/umb-scheme-root

%description
UMB Scheme is a public domain implementation of the Scheme programming
language.  Scheme is a statically scoped and properly tail-recursive
dialect of the Lisp programming language, designed with clear and
simple semantics and a minimal number of ways to form expressions.

Install the umb-scheme package if you need an implementation of the
Scheme programming language.

%description -l pt_BR
UMB Scheme é uma implementação da linguagem descrita no padrão IEEE
para a linguagem de programação Scheme (Dezembro de 1990).

%description -l es
UMB Scheme es una implementación al lenguaje descrito en el padrón
IEEE para el lenguaje de programación Scheme (Diciembre de 1990).

%prep
%setup -q -n scheme-3.2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"
makeinfo scheme.texinfo

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,info,lib/umb-scheme,man/man1}

install -s -m755 scheme $RPM_BUILD_ROOT/usr/bin/umb-scheme
install -m755 scheme.1 $RPM_BUILD_ROOT/usr/man/man1/umb-scheme.1

cp -r slib $RPM_BUILD_ROOT/usr/lib/umb-scheme
install -m644 prelude.scheme $RPM_BUILD_ROOT/usr/lib/umb-scheme
install -m644 SLIB-for-umb-scheme.init $RPM_BUILD_ROOT/usr/lib/umb-scheme

install -m644 scheme.info $RPM_BUILD_ROOT/usr/info/umb-scheme.info
gzip -9nf $RPM_BUILD_ROOT/usr/info/umb-scheme.info

%clean
rm -rf $RPM_BUILD_ROOT

%post

/sbin/install-info /usr/info/umb-scheme.info.gz /usr/info/dir \
  --entry="* umb-scheme: (umb-scheme).                     UMB Scheme Interpreter."

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/umb-scheme.info.gz /usr/info/dir \
      --entry="* umb-scheme: (umb-scheme).                     UMB Scheme Interpreter."
fi

%files
%defattr(-,root,root)
%doc slib/ANNOUNCE slib/FAQ slib/README
/usr/lib/umb-scheme
/usr/bin/umb-scheme
/usr/man/man1/umb-scheme.1
/usr/info/umb-scheme.info.gz

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 9)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- install-info

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
