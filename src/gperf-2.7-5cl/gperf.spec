Summary: GNU gperf -- perfect hash function generator.
Summary(pt_BR): Gerador de funções perfeitas de hash.
Summary(es): Generador de funciones perfectas de hash.
Name: gperf
Version: 2.7
Release: 5cl
Copyright: GPL
# was .gz
Source: ftp://prep.ai.mit.edu/pub/gnu/gperf-2.7.tar.bz2
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Prereq: info
BuildRoot: /var/tmp/gperf-root

%description
GNU gperf generates perfect hash functions for sets of key words.  A
perfect hash function is simply:

          A hash function and a data structure that allows
          recognition of a key word in a set of words using
          exactly 1 probe into the data structure.

%description -l pt_BR
O GNU gperf gera funções perfeitas de hash para conjuntos de palavras
chave. Uma função perfeita de hash é:

	Uma função hash e uma estrutura de dados que permite o
	reconhecimento de uma palavra chave em um conjunto de
	palavras usando somente uma pesquisa na estrutura de
	dados.

%description -l es
GNU gperf crea funciones perfectas de hash para conjuntos de palabras
llave. Una función perfecta de hash es: Una función hash y una
estructura de datos que permite el reconocimiento de una palabra
llave en un conjunto de palabras usando solamente una pesquisa en
la estructura de datos.

%prep
%setup -q

%build
CC=egcs CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

make prefix=$RPM_BUILD_ROOT/usr install

( cd $RPM_BUILD_ROOT
  gzip -9nf ./usr/info/gperf.info*
  rm -rf usr/man/{dvi,html}
)

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/gperf.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/gperf.info.gz /usr/info/dir
fi

%files
%defattr(-,root,root)
%doc README NEWS doc/gperf.html
/usr/bin/gperf
/usr/man/man1/gperf.1
/usr/info/gperf.info*

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- fixed prereq

* Tue Dec 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- create.
