Summary: GNU fast lexical analyzer generator
Summary(pt_BR): Gerador rápido de analisadores léxicos da GNU
Summary(es): Generador rápido de analizadores léxicos de la GNU
Name: flex
Version: 2.5.4a
Release: 8cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
# was .gz
Source: ftp://prep.ai.mit.edu:/pub/gnu/flex-2.5.4a.tar.bz2
BuildRoot: /var/tmp/flex-root
Summary(de): GNU - schneller lexikalischer Analysegenerator 
Summary(fr): Générateur rapide d'analyseur lexical de GNU
Summary(tr): GNU sözdizim çözümleyici

%description
This is the GNU fast lexical analyzer generator. It generates lexical
tokenizing code based on a lexical (regular expression based) description
of the input. It is designed to work with both yacc and bison, and is
used by many programs as part of their build process.

%description -l pt_BR
Este é o gerador GNU de análise léxica rápida. Ele gera códigos
léxicos tokenizados baseados em uma descrição léxica (baseado em
expressões regulares) da entrada. Ele é designado para trabalhar
tanto com yacc como com bison, e é utilizado em vários programas
como parte do seu processo de programação.

%description -l es
Este es el creador GNU de análisis léxica rápida. Crea códigos
léxicos tokenizados basados en una descripción léxica (basado en
expresiones regulares) de la entrada. Está designado a trabajar
tanto con yacc como con bison, y se utiliza en varios programas
como parte del su proceso de programación.

%description -l de
GNU, der schnelle lexikalische Analysengenerator. Er erzeugt lexikalischen 
Token-Code, basierend auf einer lexikalischen Beschreibung (reguläre 
Ausdrucksbasis) der Eingabe. Ausgelegt zum Arbeiten mit yacc und bison, 
wird er von vielen Programmen als Teil des Build-Vorgangs verwendet. 

%description -l fr
Générateur rapide d'analyseur lexical de GNU. Il génère du code lexical
sous forme de tokens basé sur une description lexicale (basé sur les
expressions rationnelles) de son entrée. Il est conçu pour fonctionner
avec yacc et bison, et est utilisé par de nombreux programmes comme
faisant partie de leur phase de construction.

%description -l tr
Bu paket, giriþ olarak okuduðu bilgiyi kendisine düzgün deyimler olarak
belirtilen kurallar çerçevesinde birimlere böler. yacc ve bison paketleri
ile birlikte çalýþacak þekilde tasarlanmýþtýr. Pek çok programýn derlenme
aþamasýnda kullanýlýr.

%prep
%setup -q -n flex-2.5.4

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

( cd $RPM_BUILD_ROOT
  strip ./usr/bin/flex
  ln -sf flex ./usr/bin/lex
  ln -s flex.1 ./usr/man/man1/lex.1
  ln -s flex.1 ./usr/man/man1/flex++.1
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING NEWS README
/usr/bin/lex
/usr/bin/flex
/usr/bin/flex++
/usr/man/man1/lex.1
/usr/man/man1/flex.1
/usr/man/man1/flex++.1
/usr/lib/libfl.a
/usr/include/FlexLexer.h

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Oct 21 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 2.5.4 to 2.5.4a

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
- Updated to v. 2.5.4
