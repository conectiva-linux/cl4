Name: guavac
Version: 1.2
Release: 6cl
Copyright: GPL
# was .gz
Source: ftp://ftp.yggdrasil.com/pub/dist/devel/compilers/guavac/guavac-1.2.tar.bz2
Url: http://HTTP.CS.Berkeley.EDU/~engberg/guavac/
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Summary: Java -> JVM compiler written in C++ for high performance
Summary(pt_BR): Compilador java -> JVM escrito em C++ para otimizar performance
Summary(es): Compilador java -> JVM escrito en C++ para optimizar desempeño
Buildroot: /var/tmp/guavac-root
Summary(de): Java-JVM-Compiler in C++
Summary(fr): Compilateur Java -> JVM ecrit en C++ pour de grandes performances.
Summary(tr): Java derleyicisi

%description
Guavac is a standalone compiler for the Java programming language. It
was written entirely in C++, and should be portable to any platform
supporting Gnu's C++ compiler or a similarly powered system.

%description -l pt_BR
Guavac é um compilador para a linguagem de programação Java. Ele
foi escrito inteiramente em C++, e deve ser portátil para qualquer
plataforma que tem um compilador C++ Gnu ou um similar.

%description -l es
Guavac es un compilador para el lenguaje de programación Java. Fue
escrito enteramente en C++, y debe ser portátil para cualquier
plataforma que tiene un compilador C++ Gnu o un similar.

%description -l de
Guavac ist ein selbständiger Compiler für die Java-Programmiersprache. 
Komplett in C++ geschrieben, läßt er sich auf jede Plattform übernehmen, 
die den C++-Compiler von GNU oder ein ähnliches System unterstützt. 

%description -l fr
Guavac est un compilateur autonome du langage de programmation Java.
Il a été entièrement écrit en C++ et peut être porté sur toutes les
plates-formes qui disposent du compilateur C++ de GNU, ou d'un système
équivalent

%description -l tr
Guavac tek baþýna çalýþan bir Java dili derleyicisidir. Tamamen C++ ile
yazýlmýþtýr.

%prep
%setup 

%build
%ifarch alpha
CCC=egcs CFLAGS=" " ./configure --prefix=/usr 
%else
CCC=egcs CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
%endif
make CCC=egcs

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
strip $RPM_BUILD_ROOT/usr/bin/guav* || :

%files
/usr/bin/guav*
/usr/man/man*/*
/usr/share/guavac

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Dec 07 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17

* Mon Nov  9 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to version 1.2

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon May 04 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1 (finally found the home site...)
- buildroot

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to version 0.3.1
- removed info pages as they are empty anyway

