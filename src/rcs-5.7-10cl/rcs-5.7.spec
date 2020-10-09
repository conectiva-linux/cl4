Summary: RCS - version control system
Summary(pt_BR): RCS - sistema de controle de vers�es
Summary(es): RCS - sistema de control de versiones
Name: rcs
Version: 5.7
Release: 10cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
# was .gz
Source: ftp://prep.ai.mit.edu:/pub/gnu/rcs-5.7.tar.bz2
Patch: rcs-5.7-stupidrcs.patch
Buildroot: /var/tmp/rcs-root
Summary(de): RCS - Versionssteuersystem
Summary(fr): RCS - Syst�me de contr�le de version
Summary(tr): S�r�m denetleme sistemi

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Nov 04 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Wed Oct 21 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue May 05 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>

- fixed the spec file; added BuildRoot

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>

-built against glibc

%description
The Revision Control System (RCS) manages multiple revisions of files.
RCS automates the storing, retrieval, logging, identification, and
merging of revisions.  RCS is useful for text that is revised
frequently, for example programs, documentation, graphics, papers, and
form letters.

%description -l pt_BR
O Sistema de Controle de Revis�o (RCS) administra m�ltiplas revis�es
de arquivos. RCS automatiza o armazenamento, recupera��o, registro,
identifica��o e a fus�o de revis�es. RCS � �til para texto que �
revisado freq�entemente, como programas, documenta��o, gr�ficos e
formul�rios de cartas.

%description -l es
Sistema de Control de Revisi�n (RCS) administra m�ltiples revisiones
de archivos. RCS automatiza el almacenamiento, recuperaci�n,
registro, identificaci�n y la fusi�n de revisiones. Es �til para
textos se revisan frecuentemente, como programas, documentaci�n,
gr�ficos y formularios de cartas.

%description -l de
Das Revision Control Syste (RCS) verwaltet mehrere Dateirevisionen. 
Es automatisiert das Abspeichern, das Einlesen, das Aufzeichnen, 
die Erkennung und das Zusammenf�hren von Revisionen. RCS ist praktisch
f�r Texte, die h�ufig revidiert werden, etwa Programme, 
Dokumentation, Graphiken, Artikel und Formulare. 

%description -l fr
Le syst�me de contr�le de r�vision (RCS) g�re les nombreuses r�visions
des fichiers. RCS automatise le stockage, la r�cup�ration, l'identification
et le m�lange des r�visions. RCS sert aux textes r�vis�s fr�quemment, par
exemple les "programmes, la documentation, les graphiques, les articles et
les lettres.  

%description -l tr
S�r�m denetim sistemi (Revision Control System - RCS) bir dosyan�n birden
fazla s�r�m�n� denetlemek i�in kullan�l�r. RCS dosya �zerindeki
de�i�ikliklerin tutulmas�n�, saklanmas�n�, kay�tlar�n�n tutulmas� i�lerini
kolayla�t�r�r. �zerinde s�k�a de�i�iklik yap�lan program kodlar�, belgeler ve
makaleler i�in son derece yararl� bir ara�t�r.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr --with-diffutils
touch src/conf.h
make 

%install
./configure --prefix=$RPM_BUILD_ROOT/usr --with-diffutils
touch src/conf.h
make install

strip $RPM_BUILD_ROOT/usr/bin/*

%files
%doc NEWS REFS
/usr/bin/*
/usr/man/man1/*
/usr/man/man5/*

%clean
rm -rf $RPM_BUILD_ROOT
