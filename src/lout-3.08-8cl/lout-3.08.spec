Summary: Lout text formatting system
Summary(pt_BR): Sistema de formata��o de texto
Summary(es): Sistema de formateado de texto
Name: lout
Version: 3.08
Release: 8cl
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
Icon: lout.gif
# was .gz
Source: ftp://ftp.cs.su.oz.au/jeff/lout.3.08.tar.bz2
Patch0: lout-3.08-make.patch
Patch1: lout-3.08-nobr.patch
Copyright: GPL
BuildRoot: /var/tmp/lout-root
Summary(de): Lout Textformatierungssystem 
Summary(fr): Syst�me de formatage de texte Lout
Summary(tr): Lout metin bi�imleme sistemi

%description
The Lout system reads a high-level description of a document similar
in style to LaTeX and produces a PostScript file which can be printed
on many laser printers and graphic display devices.  Plain text output
is also available.

Lout offers an unprecedented range of advanced features, including
optimal paragraph and page breaking, automatic hyphenation, PostScript
EPS file inclusion and generation, equation formatting, tables, diagrams,
rotation and scaling, sorted indexes, bibliographic databases, running
headers and odd-even pages, automatic cross referencing, multilingual
documents including hyphenation (most European languages are supported,
including Russian), formatting of C/C++ programs, and much more, all
ready to use.  Furthermore, Lout is easily extended with definitions
which are very much easier to write than troff of TeX macros because
Lout is a high-level language, the outcome of an eight-year research
project that went back to the beginning.

%description -l pt_BR
O sistema lout l� uma descri��o de alto n�vel de um documento
similar em estilo ao LaTeX e produz um arquivo PostScript, que pode
ser impresso em muitas impressoras laser e dispositivos gr�ficos
de display. Sa�da em formato texto tamb�m esta dispon�vel. Lout
oferece muitas caracter�sticas avan�adas, incluindo otimiza��o de
quebras de par�grafos e p�ginas, hifeniza��o autom�tica, inclus�o e
gera��o de arquivos PostScript EPS, formata��o de equa��es, tabelas,
diagramas, rota��o e escalamento, �ndices ordenados, bancos de dados
bibliogr�ficos, headers e pagina��o par-�mpar, refer�ncia cruzada
autom�tica, documentos de m�ltiplos idiomas incluindo hifeniza��o
(a maioria dos idiomas europeus s�o suportados, inclusive russo),
formata��o de programas C/C++, e muito mais, tudo pronto para usar.

%description -l es
El sistema lout lee una descripci�n de altonivel de un documento
similar en estilo al LaTeX y produce un archivo PostScript,
que puede ser impreso en muchas impresoras laser y dispositivos
gr�ficos de display.  Tambi�n se encuentra disponible la salida
en formato texto. Lout ofrece muchas caracter�sticas avanzadas,
incluyendo optimizaci�n de saltos de p�rrafos y p�ginas, separaci�n
autom�tica, inclusi�n y creaci�n de archivos PsotScript EPS, formatos
de ecuaciones, tablas, gr�ficos, rotaci�n y escalonamiento, �ndices
ordenados, banco de datos bibliogr�ficos, documentos de m�ltiples
idiomas que incluye separaci�n (soporta la mayor�a de los idiomas
europeos, incluso el ruso), formatos de programas C/C++, y mucho
m�s. Todo listo para usar.

%package doc
Summary: Full lout documentation
Summary(pt_BR): Documenta��o completa sobre o lout
Summary(es): Documentaci�n completa sobre lout
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
Summary(de): Komplette Lout-Dokumentation 
Summary(fr): Documentation compl�te de Lout
Summary(tr): lout belgeleri

%description doc
This package includes the complete Lout documentation, including
the "user" and "expert" manuals, written in Lout and with PostScript
output.  Good examples of writing large docs with Lout.

%description -l pt_BR doc
Este pacote inclui a documenta��o completa do Lout, incluindo os
manuais "usu�rio" e "experiente", escritos em Lout e com sa�da
PostScript. Cont�m exemplos de como escrever documentos extensos
com Lout.

%description -l es doc
Este paquete incluye la documentaci�n completa del Lout, los manuales
"usuario" y "experto", escritos en Lout y con salida PostScript.
Contiene ejemplos de como escribir documentos largos con Lout.

%description -l de
Das Lout-System liest eine High-Level-Beschreibung eines Dokuments
im LaTex-Stil und erzeugt eine PostScript-Datei, die auf vielen Laserdruckern
und Grafikanzeigeger�ten ausgegeben werden kann. Auf Wunsch ist auch
reine Textausgabe m�glich.

Lout bietet eine bislang unerreichte Auswahl an fortgeschrittenen Funktionen, u.a.
optimalen Umbruch von Abs�tzen und Seiten, autom. Silbentrennung, PostScript-
EPS-Datei-Integration sowie Erstellen und Formatieren von Gleichungen, Tabellen,
Diagrammen, Drehen und Skalieren, Index-Sortierung, bibliographische Datenbanken,
Kopfleisten und linke und rechte Seiten, autom. Querverweise, mehrsprachige Dokumente
einschlie�lich Silbentrennung (Unterst�tzung der meisten europ�ischen Sprachen,
inkl. Russisch), Formatieren von C/C++-Programmen und vieles mehr - alles sofort
einsatzbereit. Au�erdem l��t sich Lout ohne weiteres durch Definitionen erweitern, die sehr
viel einfacher zu schreiben sind als troff oder TeX-Makros, da Lout eine High-Level-
Sprache ist und das Ergebnis von 8 Jahren Forschungsarbeit.

%description -l fr
Le syst�me Lout lit une description de haut-niveau d'un document, du
style LaTeX, et produit un fichier PostScript pouvant �tre imprim�
sur la plupart des imprimantes laser ou sur la plupart des p�riph�riques
graphiques. La sortie en texte plein est �galement possible.

Lout offre une gamme de possibilit�s sans pr�c�dent, dont un d�coupage 
par page ou paragraphe optimal, inclusion ou g�n�ration de fichiers
PostScript EPS, formattage d'�quations, bases de donn�es bibliographiques
formattage de programmes C/C++, et bien plus encore. De plus Lout est
facilement extensible avec des d�finitions bien plus simple que des macros
groff ou TeX, car Lout est un langage de haut-niveau, l'aboutissement de
huit ans de recherches revenues � leur d�but.

%description -l tr
Lout sistemi, LaTeX'e benzer �ekilde, bir belgenin y�ksek d�zeyli tan�m�n�
al�r ve PostScript'e �evirir. Sat�r sonlar�nda hece b�lme, denklem yaz�m�,
tablo ve diagram haz�rlanmas�, dizin ve �apraz ba�vurular�n y�netimi gibi
yetenekleri vard�r.

%prep
%setup -q -n lout.3.08
%patch0 -p1
%patch1 -p1 -b .nobr

%build
%ifarch sparc
make CC="sparc-redhat-linux-gcc" RPM_OPT_FLAGS="$RPM_OPT_FLAGS" lout c2lout
%else
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" lout c2lout
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,doc,lib,man/man1}

make DESTDIR=$RPM_BUILD_ROOT install installman installdoc

for i in user slides expert design; do
    chmod 755 $RPM_BUILD_ROOT/usr/doc/lout/$i
done
strip $RPM_BUILD_ROOT/usr/bin/{lout,c2lout}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc blurb README maillist whatsnew notes.dsc
/usr/bin/lout
/usr/man/man1/lout.1
/usr/bin/c2lout
/usr/man/man1/c2lout.1
/usr/lib/lout

%files doc
%defattr(-,root,root)
/usr/doc/lout

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Nov 04 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Wed Oct 21 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root
- use gcc on sparc to avoid egcs bug

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
