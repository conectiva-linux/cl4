Summary: The GNU interactive spelling checker program.
Summary(pt_BR): GNU ispell - verificador ortogr�fico interativo
Summary(es): GNU ispell - verificador ortogr�fico interactivo
Name: ispell
Version: 3.1.20
Release: 20cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Source0: ftp://prep.ai.mit.edu/pub/gnu/ispell-3.1.20.tar.bz2
Source1: ispell.info
Source2: spell
Source3: ftp://ftp.informatik.uni-kiel.de/pub/kiel/dicts/hk2-deutsch.tar.bz2
Source10: ftp://ftp.ime.usp.br/pub/ueda/br.ispell/br.ispell-2.3.tar.bz2
Source11: ftp://ftp.fi.upm.es/pub/unix/espa~nol-1.5.tar.bz2
Source12: ftp://ftp.pluto.linux.it/pub/pluto/ildp/ispell/italiano-0.03.tar.gz
Source13: ftp://ftp.robot.ireq.ca/pub/ispell/francais-IREQ-1.4.tar.bz2
Source14: http://www.di.uminho.pt/~jj/pln/UMportugues.tar.gz
Patch0: ispell-3.1.20-config-cnc.patch
Patch1: ispell-3.1.20-german.patch 
Patch2: ispell-3.1-info.patch
Patch3: ispell-3.1.20-termio.patch
Patch4: ispell-3.1.20-mask.patch
Patch5: ispell-3.1.20-strcmp.patch
Patch11: spanish-latin1.patch
Patch12: conjugue-verbos.patch
BuildRoot: /var/tmp/ispell-root
Copyright: GPL

%description
Ispell is the GNU interactive spelling checker.  Ispell will check a text
file for spelling and typographical errors.  When it finds a word that is
not in the dictionary, it will suggest correctly spelled words for the
misspelled word.

You should install ispell if you need a program for spell checking (and who
doesn't...).

%description -l pt_BR
Este � o corretor ortogr�fico interativo GNU. Voc� pode rod�-lo em
arquivos de texto e ele verificar� a ortografia interativamente. Isso
significa que ele ir� avis�-lo sobre palavras que ele desconhece,
e ir� sugerir alternativas quando puder.
O br.ispell (http://www.ime.usp.br/~ueda/br.ispell/) em portugu�s
brasileiro � o vocabul�rio padr�o deste pacote.

%description -l es
Este es el corrector ortogr�fico interactivo GNU. Puedes
ejecutarlo en archivos de texto y verificar� la ortograf�a
interactivamente. Esto significa que te ir� contando sobre las
palabras que el desconoce, y ir� sugerir alternativas siempre
que pueda.

%package american
Version: 3.1.20
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for American English
Summary(pt_BR): Dicion�rio de ingl�s americano para o ispell
Summary(es): Diccionario de ingl�s americano para ispell
Requires: ispell

%description american
Ispell dictionary for American English

%description -l pt_BR american
Dicion�rio de ingl�s americano para o ispell

%description -l es american
Diccionario de ingl�s americano para ispell

%package british
Version: 3.1.20
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for British English
Summary(pt_BR): Dicion�rio de ingl�s brit�nico para o ispell
Summary(es): Diccionario de ingl�s brit�nico para ispell
Requires: ispell

%description british
Ispell dictionary for British English

%description -l pt_BR british
Dicion�rio de ingl�s brit�nico para o ispell

%description -l es british
Diccionario de ingl�s brit�nico para ispell

%package brazilian
Version: 2.3
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for Brazilian Portuguese
Summary(pt_BR): Dicion�rio de portugu�s do Brasil para o ispell
Summary(es): Diccionario de portugu�s brasile�o para ispell
Requires: ispell

%description brazilian
Ispell dictionary for Brazilian Portuguese. It contains the br.ispell
package by Ricardo Ueda Karpischek.
See http://www.ime.usp.br/~ueda/br.ispell/ for more information.
There is another package called ispell-portuguese for Portuguese, as
it is spelled in Portugal.

%description -l pt_BR brazilian
Dicion�rio para o ispell do portugu�s falado no Brasil. Cont�m o pacote
br.ispell do Ricardo Ueda Karpischek.
Veja http://www.ime.usp.br/~ueda/br.ispell/ para mais informa��es.
H� um outro pacote chamado ispell-portuguese para o portugu�s falado
em Portugal.

%description -l es brazilian
Diccionario para ispell de portugu�s hablado en Brasil. Contiene
el paquete br.ispell de Ricardo Ueda Karpischek.  Mira
http://www.ime.usp.br/~ueda/br.ispell/ para m�s informaci�n.
Hay otro paquete llamado ispell-portuguese para  portugu�s hablado
en Portugal.

%package -n conjugue
Version: 1.0
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Summary: Script capable to conjugate verbs in the portuguese language
Summary(pt_BR): Conjugador de verbos da l�ngua portuguesa
Summary(es): Conjugador de verbos de la lengua portuguesa

%description -n conjugue
Conjugue is an awk script capable to conjugate verbs in the portuguese
language, using a paradigm data base built by grammar consulting.
Author: Ricardo Ueda Karpischek (ueda@ime.usp.br)

%description -l pt_BR -n conjugue
O conjugue � um script awk capaz de conjugar verbos da l�ngua
portuguesa, a partir de um banco de paradigmas constru�do atrav�s da
consulta a v�rias gram�ticas. Tanto o script quanto o banco est�o
dispon�veis sob os termos da licen�a GNU GPL.  Autor: Ricardo Ueda
Karpischek (ueda@ime.usp.br)

%description -l es -n conjugue
Conjugue es un script awk capaz de conjugar verbos de la lengua
portuguesa, a partir de un banco de paradigmas construido a trav�s
de la consulta a varias gram�ticas. Tanto el script como el banco
est�n disponibles bajo los t�rminos de la licencia GNU GPL.  Autor:
Ricardo Ueda Karpischek (ueda@ime.usp.br)

%package spanish
Version: 1.5
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for Spanish
Summary(pt_BR): Dicion�rio de espanhol para o ispell
Summary(es): Diccionario de espa�ol para ispell
Requires: ispell

%description spanish
Ispell dictionary for Spanish

%description -l pt_BR spanish
Dicion�rio de espanhol para o ispell

%description -l es spanish
Diccionario de espa�ol para ispell

%package italian
Version: 0.3
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for Italian
Summary(pt_BR): Dicion�rio de italiano para o ispell
Summary(es): Diccionario de italiano para ispell
Requires: ispell

%description italian
Ispell dictionary for Italian

%description -l pt_BR italian
Dicion�rio de italiano para o ispell

%description -l es italian
Diccionario de italiano para ispell

%package german
Version: 2
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for German
Summary(pt_BR): Dicion�rio de alem�o para o ispell
Summary(es): Diccionario de alem�n para ispell
Requires: ispell

%description german
Ispell dictionary for German

%description -l pt_BR german
Dicion�rio de alem�o para o ispell

%description -l es german
Diccionario de alem�n para ispell

%package french
Version: 1.4
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for French
Summary(pt_BR): Dicion�rio de franc�s para o ispell 
Summary(es): Diccionario de franc�s para ispell 
Requires: ispell

%description french
Ispell dictionary for French

%description -l pt_BR french
Dicion�rio de franc�s para o ispell 

%description -l es french
Diccionario de franc�s para ispell

%package portuguese
# Version: Set-95
Version: 199509 
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for Portuguese spelled in Portugal
Summary(pt_BR): Dicion�rio de portugu�s de Portugal para o ispell
Summary(es): Diccionario de portugu�s de Portugal para ispell
Requires: ispell

%description portuguese
This package contains the ispell files for Portuguese, as it is
spelled in Portugal (there is another package called ispell-brazilian
for the spelling of Brazilian Portuguese). 

%description -l pt_BR portuguese
Este pacote cont�m o dicion�rio do ispell para o portugu�s de Portugal.
H� um outro pacote chamado ispell-brazilian para o portugu�s do
Brasil.

%description -l es portuguese
Este paquete contiene el diccionario del ispell para  portugu�s
de Portugal.  Hay otro paquete llamado ispell-brazilian para
portugu�s brasile�o.

%prep
%setup -q -n ispell-3.1

tar xIf $RPM_SOURCE_DIR/hk2-deutsch.tar.bz2 -C ./languages/deutsch/ '*.txt' '*.aff' '*README'
tar xIf $RPM_SOURCE_DIR/br.ispell-2.3.tar.bz2 -C ./languages
tar xIf $RPM_SOURCE_DIR/espa~nol-1.5.tar.bz2  -C ./languages
mkdir languages/italiano
tar xzf $RPM_SOURCE_DIR/italiano-0.03.tar.gz -C ./languages/italiano
tar xIf $RPM_SOURCE_DIR/francais-IREQ-1.4.tar.bz2 -C ./languages/francais
tar xzf $RPM_SOURCE_DIR/UMportugues.tar.gz -C ./languages

%patch0
%patch1 
# patch 1 deleted
%patch2 -p1 -b .makeinfo
%patch3 -p1 -b .termio

%ifarch alpha
%patch4 -p1 -b .mask
%endif

%patch5 -p1 -b .strcmp

%patch11 -p0
%patch12 -p0

echo "Getting prebuilt ispell.info file :-(."
cp $RPM_SOURCE_DIR/ispell.info .

%build
rm -rf $RPM_BUILD_ROOT

# Make config.sh first
TMPDIR=/var/tmp PATH=.:$PATH make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" config.sh

# Now save build-rooted version (with time-stamp) for install ...
cp config.sh config.sh.BUILD
sed -e "s,/usr/,$RPM_BUILD_ROOT/usr/,g" < config.sh.BUILD > config.sh.INSTALL

# and then make everything
TMPDIR=/var/tmp PATH=.:$PATH make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

chmod +x languages/espa~nol-1.5/latin1.pl
make -C languages/br.ispell-2.3/ hash
make -C languages/espa~nol-1.5 latin1
make -C languages/italiano/
make -C languages/deutsch/
make -C languages/portugues/ DICTIONARY=portugues.dic

cd languages/francais/
buildhash francais.dico ./francais.aff francais.hash


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/man
mkdir -p $RPM_BUILD_ROOT/usr/lib/emacs/site-lisp
mkdir -p $RPM_BUILD_ROOT/usr/info

# Roll in the build-root'ed version (with time-stamp!)
mv config.sh.INSTALL config.sh
TMPDIR=/var/tmp PATH=.:$PATH make install

mv $RPM_BUILD_ROOT/usr/info/ispell $RPM_BUILD_ROOT/usr/info/ispell.info
gzip -9nf $RPM_BUILD_ROOT/usr/info/ispell.info

install -m 755 ${RPM_SOURCE_DIR}/spell $RPM_BUILD_ROOT/usr/bin/

for file in br.ispell-2.3/br.hash \
            br.ispell-2.3/br.aff \
            italiano/italiano.hash \
            italiano/italiano.aff \
            francais/francais.aff \
            francais/francais.hash \
            deutsch/deutschlxg.hash \
            deutsch/deutschmed.hash \
            deutsch/deutsch.aff \
            english/english.aff \
            portugues/portugues.aff \
            portugues/portugues.hash
do
  install -m 644 languages/$file $RPM_BUILD_ROOT/usr/lib/ispell
done

install -m 644 languages/espa~nol-1.5/espa~nol.hash.latin1 \
	$RPM_BUILD_ROOT/usr/lib/ispell/espa~nol.hash
install -m 644 languages/espa~nol-1.5/espa~nol.aff.latin1 \
	$RPM_BUILD_ROOT/usr/lib/ispell/espa~nol.aff

install -m 644 languages/english/english.4l \
	$RPM_BUILD_ROOT/usr/man/man4/british.4
install -m 644 languages/english/english.4l \
	$RPM_BUILD_ROOT/usr/man/man4/american.4
gzip -9v $RPM_BUILD_ROOT/usr/man/man4/{british,american,english}.4

mkdir -p $RPM_BUILD_ROOT/usr/lib/conjugue/
install -m 755 languages/br.ispell-2.3/conjugue \
	$RPM_BUILD_ROOT/usr/bin/conjugue
install -m 644 languages/br.ispell-2.3/conjugue.1 \
	$RPM_BUILD_ROOT/usr/man/man1/conjugue.1
install -m 644 languages/br.ispell-2.3/verbos \
	$RPM_BUILD_ROOT/usr/lib/conjugue/verbos
gzip -9v $RPM_BUILD_ROOT/usr/man/man1/conjugue.1

cd $RPM_BUILD_ROOT/usr/lib/ispell
ln -s italiano.hash	italian.hash
ln -s espa~nol.hash	spanish.hash
ln -s br.hash		brazilian.hash
ln -s portugues.hash	portuguese.hash
ln -s francais.hash	french.hash
ln -s deutschlxg.hash	deutsch.hash
ln -s deutschlxg.hash	german.hash

%clean
rm -rf $RPM_BUILD_ROOT

%post american
if [ ! -f /usr/lib/ispell/britishmed+.hash ]
then
	ln -sf americanmed+.hash /usr/lib/ispell/english.hash
fi

%post british
if [ ! -f /usr/lib/ispell/americanmed+.hash ]
then
	ln -sf britishmed+.hash /usr/lib/ispell/english.hash
fi

%preun american
if [ -f /usr/lib/ispell/britishmed+.hash ]
then
        ln -sf britishmed+.hash /usr/lib/ispell/english.hash
else
	rm -f /usr/lib/ispell/english.hash
fi

%preun british
if [ -f /usr/lib/ispell/americanmed+.hash ]
then
        ln -sf americanmed+.hash /usr/lib/ispell/english.hash
else
	rm -f /usr/lib/ispell/english.hash
fi

%files
%defattr(-,root,root)
%doc README
/usr/bin/ispell
/usr/bin/spell
/usr/man/man1/ispell.1
/usr/man/man4/ispell.4
/usr/info/ispell.info.gz
#/usr/lib/emacs/site-lisp/ispell.el
/usr/bin/buildhash
/usr/bin/icombine
/usr/bin/ijoin
/usr/bin/munchlist
/usr/bin/findaffix
/usr/bin/tryaffix
/usr/bin/sq
/usr/bin/unsq
/usr/man/man1/sq.1
/usr/man/man1/buildhash.1
/usr/man/man1/munchlist.1
/usr/man/man1/findaffix.1
/usr/man/man1/tryaffix.1
/usr/man/man1/unsq.1
%dir /usr/lib/ispell

%files american
%defattr(0644,root,root)
%doc README
/usr/lib/ispell/americanmed+.hash
/usr/lib/ispell/american.hash
/usr/lib/ispell/english.aff
/usr/man/man4/american.4.gz

%files british
%defattr(0644,root,root)
%doc README
/usr/lib/ispell/britishmed+.hash
/usr/lib/ispell/british.hash
/usr/lib/ispell/english.aff
/usr/man/man4/british.4.gz

%files brazilian
%defattr(0644,root,root)
%doc languages/br.ispell-2.3/{README,COPYING}
/usr/lib/ispell/br.hash
/usr/lib/ispell/br.aff
/usr/lib/ispell/brazilian.hash

%files -n conjugue
%defattr(-,root,root)
%doc languages/br.ispell-2.3/{README,COPYING}
/usr/bin/conjugue
/usr/lib/conjugue/verbos

%files spanish
%defattr(0644,root,root)
%doc languages/espa~nol-1.5/{README,LEAME}
/usr/lib/ispell/espa~nol.hash
/usr/lib/ispell/espa~nol.aff
/usr/lib/ispell/spanish.hash

%files italian
%defattr(0644,root,root)
%doc languages/italiano/{README,COPYING}
/usr/lib/ispell/italiano.hash
/usr/lib/ispell/italiano.aff
/usr/lib/ispell/italian.hash

%files french
%defattr(0644,root,root)
%doc languages/francais/{README,COPYING,LISEZMOI}
/usr/lib/ispell/francais.hash
/usr/lib/ispell/francais.aff
/usr/lib/ispell/french.hash

%files german
%defattr(0644,root,root)
%doc languages/deutsch/README
/usr/lib/ispell/deutsch.aff
/usr/lib/ispell/deutsch.hash
/usr/lib/ispell/deutschlxg.hash
/usr/lib/ispell/deutschmed.hash
/usr/lib/ispell/german.hash

%files portuguese
%defattr(0644,root,root)
%doc languages/portugues/README
/usr/lib/ispell/portugues.hash
/usr/lib/ispell/portugues.aff
/usr/lib/ispell/portuguese.hash

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 13 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- recompressed sources

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to br.ispell-2.3
- included several new languages (spanish, italian, french, german,
  portuguese) 
- splited across several dictionary sub-packages with names inspirated
  on debian.

* Thu Feb 25 1999 Bill Nottingham <notting@redhat.com>
- add a buildroot

* Tue Jan 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- strcmp may have different forms on different systems;
  do not declare it explicitly, just include <string.h>
- use /var/tmp instead of /usr/tmp

* Sun Nov 8 1998 Patricia Jung <trish@freiburg.linux.de>
- Added German dictionary

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- eliminate /usr/lib/emacs/site-lisp/ispell.el -- use emacs-20.3 version.

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- use posix termios (problem #558)
- add build root.

* Sat Jun 27 1998 Trent Jarvi <jarvi@ezlink.com>
- alphahack patch no longer required. struct winsize now in <ioctl-types.h>.
- change MASKWIDTH apropriately on alpha

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 09 1998 Erik Troan <ewt@redhat.com>
- have two Source1 lines isn't terribly brilliant

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to avoid remaking ispell.info

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added a spell program.
- Configured for 8-bit use.
