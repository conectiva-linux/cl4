Summary: GNU fast lexical analyzer generator
Summary(pt_BR): Gerador r�pido de analisadores l�xicos da GNU
Summary(es): Generador r�pido de analizadores l�xicos de la GNU
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
Summary(fr): G�n�rateur rapide d'analyseur lexical de GNU
Summary(tr): GNU s�zdizim ��z�mleyici

%description
This is the GNU fast lexical analyzer generator. It generates lexical
tokenizing code based on a lexical (regular expression based) description
of the input. It is designed to work with both yacc and bison, and is
used by many programs as part of their build process.

%description -l pt_BR
Este � o gerador GNU de an�lise l�xica r�pida. Ele gera c�digos
l�xicos tokenizados baseados em uma descri��o l�xica (baseado em
express�es regulares) da entrada. Ele � designado para trabalhar
tanto com yacc como com bison, e � utilizado em v�rios programas
como parte do seu processo de programa��o.

%description -l es
Este es el creador GNU de an�lisis l�xica r�pida. Crea c�digos
l�xicos tokenizados basados en una descripci�n l�xica (basado en
expresiones regulares) de la entrada. Est� designado a trabajar
tanto con yacc como con bison, y se utiliza en varios programas
como parte del su proceso de programaci�n.

%description -l de
GNU, der schnelle lexikalische Analysengenerator. Er erzeugt lexikalischen 
Token-Code, basierend auf einer lexikalischen Beschreibung (regul�re 
Ausdrucksbasis) der Eingabe. Ausgelegt zum Arbeiten mit yacc und bison, 
wird er von vielen Programmen als Teil des Build-Vorgangs verwendet. 

%description -l fr
G�n�rateur rapide d'analyseur lexical de GNU. Il g�n�re du code lexical
sous forme de tokens bas� sur une description lexicale (bas� sur les
expressions rationnelles) de son entr�e. Il est con�u pour fonctionner
avec yacc et bison, et est utilis� par de nombreux programmes comme
faisant partie de leur phase de construction.

%description -l tr
Bu paket, giri� olarak okudu�u bilgiyi kendisine d�zg�n deyimler olarak
belirtilen kurallar �er�evesinde birimlere b�ler. yacc ve bison paketleri
ile birlikte �al��acak �ekilde tasarlanm��t�r. Pek �ok program�n derlenme
a�amas�nda kullan�l�r.

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
