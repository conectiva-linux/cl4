Summary: GNU Macro Processor
Summary(pt_BR): Processador de Macros da GNU
Summary(es): Procesador de Macros de la GNU
Name: m4
Version: 1.4
Release: 15cl
Copyright: GPL
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
# was .gz
Source: ftp://prep.ai.mit.edu:/pub/gnu/m4-1.4.tar.bz2
Patch: m4-1.4-glibc.patch
Buildroot: /var/tmp/m4-root
Prereq: info
Summary(de): GNU-Makro-Prozessor
Summary(fr): Processeur de macros de GNU
Summary(tr): GNU Makro Ýþlemcisi

%description
This is the GNU Macro processing language.  It is useful for
writing text files that can be parsed logically.  Many programs
use it as part of their build process.

%description -l pt_BR
Essa é a linguagem de processamento de Macro GNU. Ela é útil para
escrever arquivos texto que podem ser analisado logicamente. Vários
programas usam-no como parte do seu processo de programação.

%description -l es
Este es el lenguaje de procesamiento de Macro GNU. Es útil para
escribir archivos texto que pueden ser analizados lógicamente. Varios
programas lo usan como parte de su proceso de programación.

%description -l de
Dies ist die GNU-Makroverarbeitungssprache. Es ist zum Schreiben von
Textdateien geeignet, die logisch geparst werden können. Viele Programme
nutzen dies als Teil des Build-Vorgangs.

%description -l fr
Le langage de macro commande GNU. Il est utile pour constituer des
fichiers textes devant etre parcourues logiquement. De nombreux 
programmes l'utilisent lors de leur processus de construction.

%changelog
* Tue May 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de and fr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- Manhattan build

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- added info file handling and BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%prep
rm -rf $RPM_BUILD_ROOT

%setup
%patch -p1

%build
./configure --prefix=/usr
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
./configure --prefix=$RPM_BUILD_ROOT/usr
make install
strip $RPM_BUILD_ROOT/usr/bin/m4
gzip -9fn $RPM_BUILD_ROOT/usr/info/*

%files
%doc NEWS README
/usr/bin/m4
/usr/info/*

%post
/sbin/install-info /usr/info/m4.info.gz /usr/info/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/m4.info.gz /usr/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT
