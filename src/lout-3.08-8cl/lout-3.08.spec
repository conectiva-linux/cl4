Summary: Lout text formatting system
Summary(pt_BR): Sistema de formatação de texto
Summary(es): Sistema de formateado de texto
Name: lout
Version: 3.08
Release: 8cl
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Icon: lout.gif
# was .gz
Source: ftp://ftp.cs.su.oz.au/jeff/lout.3.08.tar.bz2
Patch0: lout-3.08-make.patch
Patch1: lout-3.08-nobr.patch
Copyright: GPL
BuildRoot: /var/tmp/lout-root
Summary(de): Lout Textformatierungssystem 
Summary(fr): Système de formatage de texte Lout
Summary(tr): Lout metin biçimleme sistemi

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
O sistema lout lê uma descrição de alto nível de um documento
similar em estilo ao LaTeX e produz um arquivo PostScript, que pode
ser impresso em muitas impressoras laser e dispositivos gráficos
de display. Saída em formato texto também esta disponível. Lout
oferece muitas características avançadas, incluindo otimização de
quebras de parágrafos e páginas, hifenização automática, inclusão e
geração de arquivos PostScript EPS, formatação de equações, tabelas,
diagramas, rotação e escalamento, índices ordenados, bancos de dados
bibliográficos, headers e paginação par-ímpar, referência cruzada
automática, documentos de múltiplos idiomas incluindo hifenização
(a maioria dos idiomas europeus são suportados, inclusive russo),
formatação de programas C/C++, e muito mais, tudo pronto para usar.

%description -l es
El sistema lout lee una descripción de altonivel de un documento
similar en estilo al LaTeX y produce un archivo PostScript,
que puede ser impreso en muchas impresoras laser y dispositivos
gráficos de display.  También se encuentra disponible la salida
en formato texto. Lout ofrece muchas características avanzadas,
incluyendo optimización de saltos de párrafos y páginas, separación
automática, inclusión y creación de archivos PsotScript EPS, formatos
de ecuaciones, tablas, gráficos, rotación y escalonamiento, índices
ordenados, banco de datos bibliográficos, documentos de múltiples
idiomas que incluye separación (soporta la mayoría de los idiomas
europeos, incluso el ruso), formatos de programas C/C++, y mucho
más. Todo listo para usar.

%package doc
Summary: Full lout documentation
Summary(pt_BR): Documentação completa sobre o lout
Summary(es): Documentación completa sobre lout
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Summary(de): Komplette Lout-Dokumentation 
Summary(fr): Documentation complète de Lout
Summary(tr): lout belgeleri

%description doc
This package includes the complete Lout documentation, including
the "user" and "expert" manuals, written in Lout and with PostScript
output.  Good examples of writing large docs with Lout.

%description -l pt_BR doc
Este pacote inclui a documentação completa do Lout, incluindo os
manuais "usuário" e "experiente", escritos em Lout e com saída
PostScript. Contém exemplos de como escrever documentos extensos
com Lout.

%description -l es doc
Este paquete incluye la documentación completa del Lout, los manuales
"usuario" y "experto", escritos en Lout y con salida PostScript.
Contiene ejemplos de como escribir documentos largos con Lout.

%description -l de
Das Lout-System liest eine High-Level-Beschreibung eines Dokuments
im LaTex-Stil und erzeugt eine PostScript-Datei, die auf vielen Laserdruckern
und Grafikanzeigegeräten ausgegeben werden kann. Auf Wunsch ist auch
reine Textausgabe möglich.

Lout bietet eine bislang unerreichte Auswahl an fortgeschrittenen Funktionen, u.a.
optimalen Umbruch von Absätzen und Seiten, autom. Silbentrennung, PostScript-
EPS-Datei-Integration sowie Erstellen und Formatieren von Gleichungen, Tabellen,
Diagrammen, Drehen und Skalieren, Index-Sortierung, bibliographische Datenbanken,
Kopfleisten und linke und rechte Seiten, autom. Querverweise, mehrsprachige Dokumente
einschließlich Silbentrennung (Unterstützung der meisten europäischen Sprachen,
inkl. Russisch), Formatieren von C/C++-Programmen und vieles mehr - alles sofort
einsatzbereit. Außerdem läßt sich Lout ohne weiteres durch Definitionen erweitern, die sehr
viel einfacher zu schreiben sind als troff oder TeX-Makros, da Lout eine High-Level-
Sprache ist und das Ergebnis von 8 Jahren Forschungsarbeit.

%description -l fr
Le système Lout lit une description de haut-niveau d'un document, du
style LaTeX, et produit un fichier PostScript pouvant être imprimé
sur la plupart des imprimantes laser ou sur la plupart des périphériques
graphiques. La sortie en texte plein est également possible.

Lout offre une gamme de possibilités sans précédent, dont un découpage 
par page ou paragraphe optimal, inclusion ou génération de fichiers
PostScript EPS, formattage d'équations, bases de données bibliographiques
formattage de programmes C/C++, et bien plus encore. De plus Lout est
facilement extensible avec des définitions bien plus simple que des macros
groff ou TeX, car Lout est un langage de haut-niveau, l'aboutissement de
huit ans de recherches revenues à leur début.

%description -l tr
Lout sistemi, LaTeX'e benzer þekilde, bir belgenin yüksek düzeyli tanýmýný
alýr ve PostScript'e çevirir. Satýr sonlarýnda hece bölme, denklem yazýmý,
tablo ve diagram hazýrlanmasý, dizin ve çapraz baþvurularýn yönetimi gibi
yetenekleri vardýr.

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
