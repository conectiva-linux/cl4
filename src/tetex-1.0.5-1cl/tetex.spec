Summary: TeX typesetting system and MetaFont font formatter
Summary(pt_BR): Sistema de typesetting TeX e formatador de fontes MetaFont
Summary(es): Sistema de typesetting TeX y formateador de fuentes MetaFont
Name: tetex
Version: 1.0.5
Release: 1cl
Copyright: distributable
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
Requires: tmpwatch, dialog, ed
Prereq: info
Source0: ftp://ctan.tug.org/tex-archive/systems/unix/teTeX/1.0/distrib/sources/teTeX-src-1.0.tar.bz2
Source1: ftp://ctan.tug.org/tex-archive/systems/unix/teTeX/1.0/distrib/sources/teTeX-texmf-1.0.tar.bz2
Source2: dvi-to-ps.fpi
Source10: tetex.cron
Source800: tetex-wmconfig.i18n.tgz
Patch0: teTeX-1.0.2.patch
Patch1: teTeX-1.0-conectiva-config.patch  
Patch2: teTeX-1.0-buildr.patch
Patch3: teTeX-1.0-italian.patch
Patch4: teTeX-1.0-iberic.patch
Patch5: ftp://ctan.tug.org/tex-archive/systems/unix/teTeX/1.0/distrib/sources/teTeX-src-1.0.2-1.0.3.diff.gz
Patch6: teTeX-1.0.4.patch
Patch7: teTeX-1.0.5.patch
Url: http://www.tug.org/teTeX/
BuildRoot: /var/tmp/tetex-root
Summary(de): TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(fr): Syst�me de compostion TeX et formatteur de MetaFontes.
Summary(tr): TeX dizgi sistemi ve MetaFont yaz�tipi bi�imlendiricisi
Obsoletes: tetex-texmf-src

%description
TeX formats a file of interspersed text and commands and outputs a
typesetter independent file (called DVI, which is short for DeVice
Independent).  TeX capabilities and language are described in The
TeXbook, by Knuth.

%description -l pt_BR
Tex formata arquivos de texto e comandos para uma sa�da independente
de dispositivo (chamado DVI - DeVice Independent). As capacidades
e a linguagem TeX s�o descritas no The TeXbook, de Knuth.

%description -l es
Tex formatea archivos de texto y comandos para una salida
independiente de dispositivo (llamado DVI - DeVice Independent). Las
capacidades y el lenguaje TeX son descriptos en The TeXbook,
de Knuth.

%package latex
Summary: LaTeX macro package
Summary(pt_BR): Pacote de macros LaTeX
Summary(es): Paquete de macros LaTeX
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
Summary(de): LaTeX-Makropaket
Summary(fr): Package de macros pour LaTeX
Summary(tr): LaTeX makro paketi
Requires: tetex = %{PACKAGE_VERSION}

%description latex
LaTeX is a TeX macro package. The LaTeX macros encourage writers to
think about the content of their documents, rather than the form.  The
ideal, very difficult to realize, is to have no formatting commands
(like ``switch to italic'' or ``skip 2 picas'') in the document at
all; instead, everything is done by specific markup instructions:
``emphasize'', ``start a section''.

%description -l pt_BR latex
LaTeX � um pacote de macros TeX. Os macros LaTeX encorajam escritores
a pensar sobre o conte�do de seus documentos, e n�o na forma. O
ideal, muito dif�cil de realizar, � n�o ter nenhum comando de
formata��o (como ``switch to italic'' ou ``skip 2 picas'') no
documento; no lugar disto, tudo � feito especificando instru��es
de marca��o: ``emphasize'', ``start a section''.

%description -l es latex
LaTeX es un paquete de macros TeX. Las macros LaTeX impulsionan
escritores a pensar sobre el contenido de sus documentos, y no en
su forma. Lo ideal, muy dif�cil de realizar, es no tener ning�n
comando de fomatear (como ''switch to italic'' 0 ''skip 2 points'')
en el documento; en lugar de esto, todo se hace especificando
instrucciones de marcado: : ''emphasize'', ''start la section''.

%package xdvi
Summary: X11 previewer
Summary(pt_BR): Visualizador TeX X11
Summary(es): Visualizador TeX X11
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
Summary(de): X11-Previewer 
Summary(fr): Pr�visualisateur X11
Summary(tr): X11 �ng�r�nt�leyici

%description xdvi
xdvi is a program which runs under the X window system. It is used to
preview dvi files, such as are produced by tex and latex.

%description -l pt_BR xdvi
xdvi � um programa que roda no sistema X Window. � usado para
visualizar arquivos dvi, como os produzidos por tex e latex.

%description -l es xdvi
xdvi es un programa que se ejecuta en el sistema X Window. Se usa
para visualizar archivos dvi, como los producidos por tex y latex.

%package dvips
Summary: dvi to postscript convertor
Summary(pt_BR): Conversor dvi para postscript
Summary(es): Convertidor dvi para postscript
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
Summary(de): dvi-Postscript-Konvertierungsprogramm
Summary(fr): Convertisseur dvi vers PostScript
Summary(tr): dvi'dan postscript'e d�n��t�r�c�
Requires: tetex = %{PACKAGE_VERSION}

%description dvips
The program dvips takes a DVI file file[.dvi] produced by TeX (or by
some other processor such as GFtoDVI) and converts it to PostScript,
normally sending the result directly to the laserprinter.

%description -l pt_BR dvips
O programa dvips toma um arquivo DVI (.dvi) produzido pelo TeX (ou
por outro processador como o GFtoDVI) e o converte para PostScript,
normalmente enviando o resultado diretamente para a impressora laser.

%description -l es dvips
El programa dvips coge un archivo DVI (.dvi) producido por TeX
(o por otro procesador como GFtoDVI) y lo convierte a PostScript,
normalmente enviando el resultado directamente a la impresora l�ser.

%package dvilj
Summary: dvi to laserjet convertor
Summary(pt_BR): Conversor dvi para laserjet
Summary(es): Convertidor dvi para laserjet
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
Summary(de): Ein dvi-->Laserjet-Konvertierer
Summary(fr): convertisseur dvi vers laserjet.
Summary(tr): dvi'dan laserjet'e d�n��t�r�c�
Requires: tetex = %{PACKAGE_VERSION}

%description dvilj
Dvilj and siblings convert TeX-output .dvi files into HP PCL (i.e.  HP
Printer Control Language) commands suitable for printing on a HP
LaserJet+, HP LaserJet IIP (using dvilj2p), HP LaserJet 4 (using
dvilj4), and fully compatible printers.

%description -l pt_BR dvilj
Dvilj e semelhantes convertem arquivos de sa�da TeX .dvi em comandos
HP PCL (i.e. Linguagem de Controle de Impressoras HP) adequados
para impress�o em impressoras HP LaserJet+, HP LaserJet IIP (usando
dvilj2p), HP LaserJet 4 (usando dvilj4) e compat�veis.

%description -l es dvilj
Dvilj y semejantes convierten archivos de salida TeX.dvi en comandos
HP PCL (i.e. Lenguaje de Control de Impresoras HP) adecuados a
impresi�n de impresoras HP LaserJEt+, HP LaserJet IIP (usando
dvilj2p), HP LaserJet 4 (usando dvilj4) y compatibles.

%package afm
Summary: afm (Adobe Font Metrics) fonts and utilities
Summary(pt_BR): Fontes afm (Adobe Font Metrics) e utilit�rios relacionados
Summary(es): Fuentes afm (Adobe Font Metrics) y utilitarios relacionados
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
Summary(de): Fonts und Dienstprogramme f�r afm (Adobe Font Metrics)
Summary(fr): Fontes afm (Adobe Font Metrics) et utilitaires
Summary(tr): afm yaz�tipleri ve yard�mc� programlar�
Requires: tetex = %{PACKAGE_VERSION}

%description afm
PostScript fonts are (or should be) accompanied by font metric files
such as Times-Roman.afm, which describes the characteristics of the
font called Times-Roman.  To use such fonts with TeX, we need TFM
files that contain similar information.  afm2tfm does that conversion.

%description -l pt_BR afm
Fontes PostScript s�o (ou deveriam ser) acompanhadas por arquivos
de m�trica de fontes como Times-Roman.afm, que descrevem as
caracter�sticas da fonte Times-Roman. Para usar tais fontes
com o TeX, precisamos de arquivos TFM que cont�m informa��es
similares. afm2tfm faz esta convers�o.

%description -l es afm
Fuentes PostScript son (o deber�an ser) acompa�adas de archivos
de m�trica de fuentes como Times Roman. Afm, que describen las
caracter�sticas de la fuente Times-Roman. Para usar estas fuentes con
TeX, necesitamos de archivos TFM que contiene informaci�n similar.
Afm2tfm hace esta conversi�n.

%package doc
Summary: Various documentation bits about teTeX
Summary(pt_BR): Documenta��o sobre o teTeX
Summary(es): Documentaci�n sobre teTeX
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n

%description doc
This package contains the documentation files from the teTeX system. Because
of their big size, the documentation is now separated in its own
subpackage.

%description -l pt_BR doc
Este pacote cont�m os arquivos de documenta��o do sistema teTeX. Devido ao
seu tamanho (grande) a documenta��o foi separada em seu pr�prio pacote.

%description -l es doc
Este paquete contiene los archivos de documentaci�n del sistema
teTeX.  Debido a su tama�o (grande) la documentaci�n fue separada
en su propio paquete.

%description -l de latex
LaTeX ist ein TeX-Makropaket. Die LaTeX-Makros regen den Autor an, 
�ber den Inhalt - und nicht die Form - ihrer Dokumente nachzudenken. 
Ideal, wenn auch schwer zu realisieren, w�re ein Dokument, das 
keinerlei Formatierungsbefehle (von der Art 'Kursiv ein/aus' 
oder 'Zeilenabstand um 2 Pica vergr��ern') enthielte. Stattdessen  
w�rde all dies durch spezifische 'redaktionelle' Instruktionen ersetzt 
('auszeichnen', 'neues Kapitel starten'). 

%description -l de dvips
Das dvips-Programm nimmt eine dvi-Datei ([.dvi]), die von TeX
bzw. durch einen anderen Prozessor wie GFtoDVI) erzeugt wurde, und
konvertiert diese in PostScript, wobei das Ergebnis in der Regel direkt
an einen Laserdrucker gesandt wird.

%description -l de afm
PostScript-Fonts werden (oder sollten) von Font-Metric-Dateien
(z.B. Times-Roman.afm) begleitet, die die Eigenschaften des Fonts
(hier: Times-Roman) beschreiben. Um solche Fonts mit TeX verwenden
zu k�nnen, werden TFM-Dateien ben�tigt, die �hnliche Informationen


%description -l de xdvi
xdvi ist ein Programm, das unter dem X-Window-System l�uft und gewohnt 
ist, dvi-Dateien als Vorschau anzuzeigen, etwa solche, die von tex und 
latex erzeugt wurden. 

%description -l de dvilj
Dvilj und Gebr�der konvertieren TeX-Ausgabe-.dvi-Dateien in HP PCL 
 (HP Printer Control Language) Befehle zum Drucken auf HP LaserJet+, 
HP LaserJet IIP (mit dvilj2p), HP LaserJet 4 (mit
 dvilj4) und 
vollst�ndig kompatiblen Druckern. 

%description -l de
TeX formatiert eine Datei, die abwechselnd Text und Befehle enth�lt und
gibt eine ger�teunabh�ngige Datei aus (DVI genannt, Abk. f�r DeVice
Independent). Die Funktionen und Sprache von TeX werden in The
TeXbook von Knuth beschrieben.

%description -l fr latex
LaTeX est un paquetage de macros TeX. Les macros LaTeX permettent aux
auteurs de se concentrer sur le contenu des leurs documents, plut�t que
sur la forme. L'id�al, tr�s difficile � r�aliser, est de n'avoir aucune
commande de formatage (comme � mettre en italique �, ou � sauter 2 picas �)
dans le document ; au lieu de cela, tout est fait par des balises :
� d�but de section �, � gras �.

%description -l fr dvips
Le programme dvips convertit les fichiers DVI en PostScript, en
envoyant normalement le r�sultat directement sur une imprimante Laser.

%description -l fr afm
Les fontes PostScript sont (ou devraient �tre) accompagn�es de
fontes m�triques comme Times-Roman.afm qui d�crivent les caract�ristiques
des fontes appel�es Times-Roman. pour utiliser ces fontes avec TeX, nous
avons besoin de TFM, des fichiers qui contiennent des informations
similaires. afm2tfm r�alise cette conversion.

%description -l fr xdvi
xdvi est un programme s'ex�cutant sous le syst�me X Window. Il sert �
visualiser les fichiers dvi tels que ceux produits par tex et latex.

%description -l fr dvilj
dvilj et ses cousins convertissent les fichiers dvi en commandes HPPCL
(le langage des imprimantes HP) pour les imprimer sur HP LaserJet+,
HP LaserJet IIP (avec dvilj2p), HP LaserJet 4 (avec dvilj4), et autres
imprimantes totalement compatibles.  

%description -l fr
TeX formate un fichier de commandes et de texte m�land�s, et produit un
fichier de ind�pendant de toute plate-forme (appel� DVI, qui est
un raccourci pour Device Independant). Les possibilit�s de TeX et son
langage sont d�crites dans l'ouvrage TeXbook, de Knuth.

%description -l tr latex
LaTeX bir TeX makro paketidir. LaTeX makrolar�, yazarlar� belgelerinin
bi�imlerinden �ok i�erikleri �zerinde yo�unla�mlar�na �zendirir. �dealde,
ger�ekle�tirilmesi �ok zor olsa da, hi� bi�imlendirme komutuna yer
vermeksizin (``2 birim aral�k b�rak'' gibi), yaln�zca �zel i�aretleme
y�nergeleri ile (``yeni bir kesime ge�'' gibi) bunu ba�armaya �al���r.

%description -l tr dvips
dvips program�, dvi bi�iminde bir girdi dosyas� al�r ve onu PostScript'e
d�n��t�r�r. Kaynak dosya TeX taraf�ndan olu�turulmu� olabilece�i gibi ba�ka
i�leyiciler taraf�ndan da (GFtoDVI gibi) �retilmi� olabilir.

%description -l tr afm
PostScript yaz�tipleri, yaz�tipi �l��t dosyalar� ile beraber da��t�l�rlar.
�rne�in Times-Roman.afm, Times-Roman yaz�tipinin karakteristik �zelliklerini
tan�mlar. Bu t�rde yaz�tiplerini TeX ile kullanabilmek i�in, benzer
bilgileri ta��yan TFM dosyalar� gerekir. afm2tfm bu gerekli d�n���m� yapar.

%description -l tr xdvi
xdvi X Windows sistemi alt�nda �al��an bir programd�r. TeX ya da LaTeX
taraf�ndan olu�turulmu� olan dvi dosyalar�n�n g�r�nt�lenmesi amac�yla
kullan�l�r.

%description -l tr dvilj
TeX ��kt�s� dvi dosyalar�n� HP PCL (HP'nin geli�tirdi�i bir yaz�c� denetim
dili) komutlar�na �evirir ve b�ylece bir LaserJet+, HP LaserJet IIP (dvilj2p
ile), HP LaserJet4 (dvilj4 ile) ve tam uyumlular�ndan yaz�c� ��kt�s�
al�nabilir.

%description -l tr
TeX, i�inde metin ve komutlar�n yer ald��� bir dosyay� okur ve dizgi
ayg�t�ndan ba��ms�z bir ��kt� (DeVice Independent - DVI) olu�turur.
TeX'in becerileri ve dizgi dili, dili geli�tiren Knuth'un 'The TeXbook'
ba�l�kl� kitab�nda anlat�lmaktad�r.

%prep
%setup -q -n teTeX-1.0
%patch0 -p1 -b .v1.0.2
%patch5 -p1 -b .v1.0.3
%patch6 -p1 -b .v1.0.4
%patch7 -p1 -b .v1.0.5
%patch1 -p1 -b .rhconfig
%patch2 -p1 -b .buildr
mkdir -p texk/share/texmf
tar xIf $RPM_SOURCE_DIR/teTeX-texmf-1.0.tar.bz2 -C texk/share/texmf
%patch3 -p1
%patch4 -p1

%build
sh ./reautoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--with-system-ncurses --with-system-zlib --with-system-pnglib \
	--disable-multiplatform --without-dialog --without-texinfo \
	--with-fonts-dir=/var/lib/texmf \
	--with-texmf-dir=../share/texmf \
	$RPM_ARCH-conectiva-linux
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share
mkdir -p $RPM_BUILD_ROOT/var/lib/texmf
perl -pi \
	-e "s|\.\./share/texmf|$RPM_BUILD_ROOT/usr/share/texmf|g;" \
	-e "s|/var/lib/texmf|$RPM_BUILD_ROOT/var/lib/texmf|g;" \
	texk/share/texmf/web2c/texmf.cnf
cp -a texk/share/texmf  $RPM_BUILD_ROOT/usr/share/texmf
make install prefix=$RPM_BUILD_ROOT/usr \
	texmf=$RPM_BUILD_ROOT/usr/share/texmf
make init prefix=$RPM_BUILD_ROOT/usr \
	texmf=$RPM_BUILD_ROOT/usr/share/texmf
perl -pi \
	-e "s|\.\./share/texmf|/usr/share/texmf|g;" \
	-e "s|$RPM_BUILD_ROOT/var/lib/texmf|/var/lib/texmf|g;" \
	$RPM_BUILD_ROOT/usr/share/texmf/web2c/texmf.cnf
rm -f $RPM_BUILD_ROOT/usr/info/dir
gzip $RPM_BUILD_ROOT/usr/info/*info*

# install the new magic print filter for converting dvi to ps
mkdir -p $RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters
install -m755 $RPM_SOURCE_DIR/dvi-to-ps.fpi $RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters

mkdir -p $RPM_BUILD_ROOT/etc/cron.daily
install -m755 $RPM_SOURCE_DIR/tetex.cron $RPM_BUILD_ROOT/etc/cron.daily

# Strip binaries
strip $RPM_BUILD_ROOT/usr/bin/* || :

### Files list
find $RPM_BUILD_ROOT -type f -or -type l | \
	sed -e "s|$RPM_BUILD_ROOT||g" | \
	grep -v "^/etc" | \
	sed -e "s|.*\.cnf$|%config &|" > filelist.full

# subpackages
grep -v "/doc/" filelist.full | grep latex 	> filelist.latex
grep -v "/doc/" filelist.full | grep xdvi  	> filelist.xdvi
grep -v "/doc/" filelist.full | grep dvips 	> filelist.dvips
grep -v "/doc/" filelist.full | grep dvilj 	> filelist.dvilj
grep -v "/doc/" filelist.full | grep afm 	> filelist.afm
grep "/doc/" filelist.full 			> filelist.doc

# now files listed only once are in the main  package
cat filelist.full filelist.latex filelist.xdvi filelist.dvips \
   filelist.dvilj filelist.afm  filelist.doc | \
   sort | uniq -u > filelist.main 

#wmconfig things
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xdvi <<EOF
#xdvi name "XDvi"
#xdvi icon "text.xpm"
#xdvi mini-icon "mini-doc1.xpm"
#xdvi exec "xdvi &"
#xdvi group "Gr�ficos/Visualizadores"
#EOF









tar xvfpz $RPM_SOURCE_DIR/tetex-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
[ -d /usr/share/texmf.TeX.build ] && {
    rm -rf /usr/share/texmf
    mv -f /usr/share/texmf.TeX.build /usr/share/texmf
}
rm -rf $RPM_BUILD_ROOT
rm -f filelist.*

# make sure ls-R used by tetex is updated after an install

%post
/sbin/install-info /usr/info/web2c.info.gz /usr/info/dir
/sbin/install-info /usr/info/kpathsea.info.gz /usr/info/dir
/usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post latex
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
/sbin/install-info /usr/info/latex.info.gz /usr/info/dir
exit 0

%post xdvi
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post dvips
/sbin/install-info /usr/info/dvips.info.gz /usr/info/dir
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post dvilj
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post afm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun latex
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun xdvi
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun dvips
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun dvilj
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun afm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/kpathsea.info.gz /usr/info/dir
	/sbin/install-info --delete /usr/info/web2c.info.gz /usr/info/dir
fi

%preun dvips
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/dvips.info.gz /usr/info/dir
fi

%preun latex
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/latex.info.gz /usr/info/dir
fi

%files -f filelist.main
%defattr(-,root,root)
%attr(1777,root,root) %dir /var/lib/texmf
%config /etc/cron.daily/tetex.cron

%files -f filelist.latex latex
%defattr(-,root,root)

%files -f filelist.xdvi xdvi
%defattr(-,root,root)
%config /etc/X11/wmconfig/xdvi

%files -f filelist.dvips dvips
%defattr(-,root,root)
/usr/lib/rhs/rhs-printfilters/dvi-to-ps.fpi

%files -f filelist.dvilj dvilj
%defattr(-,root,root)

%files -f filelist.afm afm
%defattr(-,root,root)

%files -f filelist.doc doc
%defattr(-,root,root)

%changelog
* Wed Jun 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 1.0.4 to 1.0.5

* Tue Jun 15 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Updated from 1.0.3 to 1.0.4

* Fri Jun 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated it from 1.0.2 to 1.0.3

* Wed Jun 09 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 0.9 to 1.0.2
- redid teTeX-1.0-conectiva-config.patch
- redid teTeX-1.0-buildr.patch
- redid teTeX-1.0-italian.patch
- redid teTeX-1.0-iberic.patch

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed find-requires

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Mon Dec 07 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fontes compactados com bzip2
- teTeX-0.9-iberic.patch, habilitando portugues e espanhol para o sistema
  babel (pedido do Rodrigo Stulzer <rodrigo@conectiva.com>)

* Tue Oct 27 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- enable italian formatting

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- requires ed
- Fixed obsoletes line
- credted the doc subpackage
- fully buildroot
- require dialog in the main package
- add support for wmconfig in for the xdvi package

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to 0.9
- texmf-src package is gone
- use /var/lib/texmf instead of /var/tmp/texmf

* Sat Aug 22 1998 Jeff Johnson <jbj@redhat.com>
- make sub-packages depend on tetex (problem #214)

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- eliminate environment when running texhash (problem #849)

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Feb  5 1998 Otto Hammersmith <otto@redhat.com>
- added install-info support (dvips, fontname and kpathsea)
- combined the two changelogs in the spec file.

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- Fixed dvi-to-ps.fpi to create temp files more safely.

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr  8 1997 Michael Fulbright <msf@redhat.com>
- Removed afmdoit from file list (mistakenly added in release 3 rpm)

* Mon Mar 24 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to tetex-lib to 0.4pl8 and fixed cron tmpwatch entry to not
  delete /var/lib/texmf/fonts and /var/lib/texmf/texfonts

* Fri Mar 07 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to 0.4pl7.

* Mon Feb 17 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to 0.4pl6, and fixed file permissions on /var/lib/texmf/texfonts
  so normal users could create fonts on demand.
