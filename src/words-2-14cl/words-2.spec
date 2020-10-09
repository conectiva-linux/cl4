Summary: English dictionary for /usr/dict
Summary(pt_BR): Dicion�rio Ingl�s para /usr/dict
Summary(es): Diccionario Ingl�s para /usr/dict
Name: words
Version: 2
Release: 14cl
Copyright: freeware
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://sunsite.unc.edu/pub/Linux/libs/linux.words.2.tar.gz
Patch0: linux.words.2-jbj.patch
BuildArchitectures: noarch
BuildRoot: /var/tmp/words-root
Summary(de): Englisches W�rterbuch f�r /usr/dict
Summary(fr): Dictionnaire anglais pour /etc/dict
Summary(tr): �ngilizce s�zl�k

%description
This package contains the english dictionary in /usr/dict.  It
is used by programs like ispell as a database of words to check
for spelling and so forth.

%description -l pt_BR
Este pacote cont�m um dicion�rio ingl�s em /usr/dict. Ele � usado
por programas como ispell como um banco de dados de palavras para
ser usado como corretor ortogr�fico.

%description -l es
Este paquete contiene un diccionario ingl�s en /usr/dict. Se usa
por programas como ispell como un banco de datos de palabras para
ser usado como corrector ortogr�fico.

%description -l de
Dieses Paket enth�lt das englische W�rterbuch in /usr/dict. Es
wird von Programmen wie ispell als Wortdatenbank, z.B. zum Pr�fen
der Rechtschreibung, verwendet.

%description -l fr
Ce paquetage contient le dictionnaire anglais dans /usr/dict. Il
est utilis� par des programmes comme ispell comme base de donn�es
de mots pour v�rifier l'orthographe.

%description -l tr
Bu paket ingilizce s�zl�k i�ermektedir. Ispell gibi yaz�l�mlar bu s�zc�k
veri taban�n� kullanarak yaz�m hatalar�n� bulmaya �al���rlar.

%prep
%setup -q -c
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/dict

cp usr/dict/linux.words $RPM_BUILD_ROOT/usr/dict
ln -sf linux.words $RPM_BUILD_ROOT/usr/dict/words

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc usr/dict/README.linux.words
%doc usr/dict/README2.linux.words
/usr/dict/linux.words
/usr/dict/words

%changelog
* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Sep 30 1998 Bill Nottingham <notting@redhat.com>
- take out extra.words (they're all in linux.words)

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- correct desiccate (problem #794)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
