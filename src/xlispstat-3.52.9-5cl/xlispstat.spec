Summary: An implementation of the Lisp language with statistics extensions.
Summary(pt_BR): Xlisp de David Betz com extensões estatísticas
Summary(es): Xlisp de David Betz con extensiones estadísticas
Name: xlispstat
Version: 3.52.9
Release: 5cl
Copyright: Distributable
Group: Applications/Engineering
Group(pt_BR): Aplicações/Engenharia
Group(es): Aplicaciones/Ingeniería
Source: ftp://umnstat.stat.umn.edu:/pub/xlispstat/3-52/xlispstat-3-52-9.tar.gz
URL: http://lib.stat.cmu.edu/xlispstat
BuildRoot: /var/tmp/xlispstat-root

%description
The xlispstat package contains XLISP-PLUS, an implementation of the Lisp
programming language for the X Window System.  XLISP-PLUS also includes
extensions for performing advanced statistical computations.

Install the xlispstat package if you need a version of the Lisp
programming language for X with statistics extensions.

%description -l pt_BR
Uma implementação da linguagem de programação Lisp para X Window,
com extensões para cálculos estatísticos avançados.

%description -l es
Una implementación al lenguaje de programación Lisp para X Window,
con extensiones para cálculos estadísticos avanzados.

%prep
%setup -q -n xlispstat-3-52-9

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/lib/xlispstat/xlisp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README RELEASE doc
/usr/bin/xlispstat
/usr/lib/xlispstat

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 3.52.9

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Wed Jan 20 1999 Preston Brown <pbrown@redhat.com>
- fixed building against glibc 2.1.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.52.5.
- remove ExclusiveArch
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new version

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
