Summary: The GNU interactive spelling checker program.
Summary(pt_BR): GNU ispell - verificador ortográfico interativo
Summary(es): GNU ispell - verificador ortográfico interactivo
Name: ispell
Version: 3.1.20
Release: 20cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
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
Este é o corretor ortográfico interativo GNU. Você pode rodá-lo em
arquivos de texto e ele verificará a ortografia interativamente. Isso
significa que ele irá avisá-lo sobre palavras que ele desconhece,
e irá sugerir alternativas quando puder.
O br.ispell (http://www.ime.usp.br/~ueda/br.ispell/) em português
brasileiro é o vocabulário padrão deste pacote.

%description -l es
Este es el corrector ortográfico interactivo GNU. Puedes
ejecutarlo en archivos de texto y verificará la ortografía
interactivamente. Esto significa que te irá contando sobre las
palabras que el desconoce, y irá sugerir alternativas siempre
que pueda.

%package american
Version: 3.1.20
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for American English
Summary(pt_BR): Dicionário de inglês americano para o ispell
Summary(es): Diccionario de inglés americano para ispell
Requires: ispell

%description american
Ispell dictionary for American English

%description -l pt_BR american
Dicionário de inglês americano para o ispell

%description -l es american
Diccionario de inglés americano para ispell

%package british
Version: 3.1.20
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for British English
Summary(pt_BR): Dicionário de inglês britânico para o ispell
Summary(es): Diccionario de inglés británico para ispell
Requires: ispell

%description british
Ispell dictionary for British English

%description -l pt_BR british
Dicionário de inglês britânico para o ispell

%description -l es british
Diccionario de inglés británico para ispell

%package brazilian
Version: 2.3
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for Brazilian Portuguese
Summary(pt_BR): Dicionário de português do Brasil para o ispell
Summary(es): Diccionario de portugués brasileño para ispell
Requires: ispell

%description brazilian
Ispell dictionary for Brazilian Portuguese. It contains the br.ispell
package by Ricardo Ueda Karpischek.
See http://www.ime.usp.br/~ueda/br.ispell/ for more information.
There is another package called ispell-portuguese for Portuguese, as
it is spelled in Portugal.

%description -l pt_BR brazilian
Dicionário para o ispell do português falado no Brasil. Contém o pacote
br.ispell do Ricardo Ueda Karpischek.
Veja http://www.ime.usp.br/~ueda/br.ispell/ para mais informações.
Há um outro pacote chamado ispell-portuguese para o português falado
em Portugal.

%description -l es brazilian
Diccionario para ispell de portugués hablado en Brasil. Contiene
el paquete br.ispell de Ricardo Ueda Karpischek.  Mira
http://www.ime.usp.br/~ueda/br.ispell/ para más información.
Hay otro paquete llamado ispell-portuguese para  portugués hablado
en Portugal.

%package -n conjugue
Version: 1.0
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Summary: Script capable to conjugate verbs in the portuguese language
Summary(pt_BR): Conjugador de verbos da língua portuguesa
Summary(es): Conjugador de verbos de la lengua portuguesa

%description -n conjugue
Conjugue is an awk script capable to conjugate verbs in the portuguese
language, using a paradigm data base built by grammar consulting.
Author: Ricardo Ueda Karpischek (ueda@ime.usp.br)

%description -l pt_BR -n conjugue
O conjugue é um script awk capaz de conjugar verbos da língua
portuguesa, a partir de um banco de paradigmas construído através da
consulta a várias gramáticas. Tanto o script quanto o banco estão
disponíveis sob os termos da licença GNU GPL.  Autor: Ricardo Ueda
Karpischek (ueda@ime.usp.br)

%description -l es -n conjugue
Conjugue es un script awk capaz de conjugar verbos de la lengua
portuguesa, a partir de un banco de paradigmas construido a través
de la consulta a varias gramáticas. Tanto el script como el banco
están disponibles bajo los términos de la licencia GNU GPL.  Autor:
Ricardo Ueda Karpischek (ueda@ime.usp.br)

%package spanish
Version: 1.5
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for Spanish
Summary(pt_BR): Dicionário de espanhol para o ispell
Summary(es): Diccionario de español para ispell
Requires: ispell

%description spanish
Ispell dictionary for Spanish

%description -l pt_BR spanish
Dicionário de espanhol para o ispell

%description -l es spanish
Diccionario de español para ispell

%package italian
Version: 0.3
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for Italian
Summary(pt_BR): Dicionário de italiano para o ispell
Summary(es): Diccionario de italiano para ispell
Requires: ispell

%description italian
Ispell dictionary for Italian

%description -l pt_BR italian
Dicionário de italiano para o ispell

%description -l es italian
Diccionario de italiano para ispell

%package german
Version: 2
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for German
Summary(pt_BR): Dicionário de alemão para o ispell
Summary(es): Diccionario de alemán para ispell
Requires: ispell

%description german
Ispell dictionary for German

%description -l pt_BR german
Dicionário de alemão para o ispell

%description -l es german
Diccionario de alemán para ispell

%package french
Version: 1.4
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for French
Summary(pt_BR): Dicionário de francês para o ispell 
Summary(es): Diccionario de francés para ispell 
Requires: ispell

%description french
Ispell dictionary for French

%description -l pt_BR french
Dicionário de francês para o ispell 

%description -l es french
Diccionario de francés para ispell

%package portuguese
# Version: Set-95
Version: 199509 
Release: 4cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Summary: Ispell dictionary for Portuguese spelled in Portugal
Summary(pt_BR): Dicionário de português de Portugal para o ispell
Summary(es): Diccionario de portugués de Portugal para ispell
Requires: ispell

%description portuguese
This package contains the ispell files for Portuguese, as it is
spelled in Portugal (there is another package called ispell-brazilian
for the spelling of Brazilian Portuguese). 

%description -l pt_BR portuguese
Este pacote contém o dicionário do ispell para o português de Portugal.
Há um outro pacote chamado ispell-brazilian para o português do
Brasil.

%description -l es portuguese
Este paquete contiene el diccionario del ispell para  portugués
de Portugal.  Hay otro paquete llamado ispell-brazilian para
portugués brasileño.

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
