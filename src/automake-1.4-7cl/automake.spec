Summary: A GNU tool for automatically creating Makefiles.
Summary(pt_BR): GNU automake - ferramentas de configuração de Makefile
Summary(es): GNU automake - herramientas de configuración de Makefile
Name: automake
Version: 1.4
Release: 7cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://ftp.cygnus.com/pub/home/tromey/automake-%{version}.tar.bz2
Patch0: automake-1.4-19980208.patch
Patch1: automake-1.4-armnetwinder.patch
URL: http://sourceware.cygnus.com/automake
Requires: perl
Prereq: /sbin/install-info
BuildArchitectures: noarch
Buildroot: /var/tmp/%{name}-root

%description
Automake is an experimental Makefile generator. Automake was inspired
by the 4.4BSD make and include files, but aims to be portable and to
conform to the GNU standards for Makefile variables and targets.

You should install Automake if you are developing software and would
like to use its capabilities of automatically generating GNU
standard Makefiles. if you install Automake, you will also need to
install GNU's Autoconf package.

%description -l pt_BR
Automake é um gerador experimental de Makefiles. Ele foi inspirado
pelo 4.4BSD make e inclui arquivos, mas visa ser portável e
compatível com os padrões GNU para variáveis e alvos de Makefile.

%description -l es
Automake es un creador experimental de Makefiles. Fue inspirado
en el 4.4BSD make y incluye archivos, pero visa ser portátil y
compatible con los padrones GNU para variables y dianas de Makefile.

%prep
%setup -q
%patch0 -p0 -b .19980208
%patch1 -p1 -b .armnetwinder

%build
#./configure --prefix=/usr

%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
gzip -9nf $RPM_BUILD_ROOT/usr/info/automake*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/automake.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete /usr/info/automake.info.gz /usr/info/dir
fi

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO
/usr/bin/*
/usr/info/automake*
/usr/share/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- arm netwinder patch

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb  8 1999 Jeff Johnson <jbj@redhat.com>
- add patches from CVS for 6.0beta1

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.4.

* Mon Nov 23 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.3b.
- add URL.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- updated to 1.3

* Tue Oct 28 1997 Cristian Gafton <gafton@redhat.com>
- added BuildRoot; added aclocal files

* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- made it a noarch package

* Thu Oct 16 1997 Michael Fulbright <msf@redhat.com>
- Fixed some tag lines to conform to 5.0 guidelines.

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- updated to 1.2

* Wed Mar 5 1997 msf@redhat.com <Michael Fulbright>
- first version (1.0)
