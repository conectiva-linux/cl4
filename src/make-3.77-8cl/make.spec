Summary: GNU Make
Summary(pt_BR): GNU Make
Summary(es): GNU Make
Name: make
Version: 3.77
Release: 8cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
# was .gz
Source: ftp://prep.ai.mit.edu:/pub/gnu/make-3.77.tar.bz2
Patch0: make-3.77-fixes.patch
Prereq: info
Buildroot: /var/tmp/make-root
Summary(de): GNU Make
Summary(fr): L'utilitaire make de GNU
Summary(tr): GNU Make

%description
The program make is used to coordinate the compilation and
linking of a set of sources into a program, recompiling
only what is necessary, thus saving a developer a lot of time.
In fact, make can do a lot more - read the info docs.

%description -l pt_BR
O programa make é usado para coordenar a compilação e linkedição
de um conjunto de programas fontes em programas executáveis,
recompilando somente o que é necessário, desse modo economizando um
grande tempo do programador. De fato, make pode fazer muito mais -
leia a documentação.

%description -l es
El programa make se usa para coordinar la compilación y linkedición
de un conjunto de programas fuentes en programas ejecutables,
recompilando solamente lo que es necesario, de este modo ahorra
mucho tiempo del programador. De hecho, make puede hacer mucho más -
lee la documentación.

%description -l de
Das MAKE-Programm dient zur Koordination der Kompilierung und 
zum Linken eines Satzes von Quellen in ein Programm, wobei nur die
erforderlichen Komponenten neu kompiliert werden, so daß der 
Entwickler eine Menge Zeit spart. Aber damit sind die 
Fähigkeiten von MAKE noch lange nicht erschöpft - lesen Sie 
die Info-Dokumente. 

%description -l fr
make sert à coordonner la compilation et l'édition de liens d'un ensemble
de sources pour produire un programme, ne recompilant que ce qui est
nécessaire et économisant ainsi beaucoup de temps. En fait, make peut faire
beaucoup plus -- voir les docs info.

%description -l tr
Bu program kaynak kodlarýnýn derlenmesini ve baðlanmasýný koordine etmek
için kullanýlýr. Sadece gerekli olan programlarý tekrar derleyerek zaman
yitirilmesini önler.

%prep
%setup -q
%patch0 -p1 -b .fixes

%build
autoconf
./configure --prefix=/usr
make "CFLAGS=$RPM_OPT_FLAGS" 

%install
rm -f $RPM_BUILD_ROOT/usr/info/make.info*
make prefix=$RPM_BUILD_ROOT/usr install

( cd $RPM_BUILD_ROOT
  rm ./usr/info/dir
  gzip -9nf ./usr/info/make.info*
  strip ./usr/bin/make
  ln -sf make ./usr/bin/gmake
)

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/make.info.gz /usr/info/dir --entry="* GNU make: (make).           The GNU make utility."

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/make.info.gz /usr/info/dir --entry="* GNU make: (make).           The GNU make utility."
fi

%files
%defattr(-,root,root)
%doc NEWS README
/usr/bin/make
/usr/bin/gmake
/usr/man/man1/make.1
/usr/info/make.info*

%changelog
* Mon May 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 04 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Wed Sep 16 1998 Cristian Gafton <gafton@redhat.com>
- added a patch for large file support in glob
 
* Tue Aug 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.77

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- udpated from 3.75 to 3.76
- various spec file cleanups
- added install-info support

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
