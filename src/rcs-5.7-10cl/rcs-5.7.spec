Summary: RCS - version control system
Summary(pt_BR): RCS - sistema de controle de versões
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
Summary(fr): RCS - Système de contrôle de version
Summary(tr): Sürüm denetleme sistemi

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
O Sistema de Controle de Revisão (RCS) administra múltiplas revisões
de arquivos. RCS automatiza o armazenamento, recuperação, registro,
identificação e a fusão de revisões. RCS é útil para texto que é
revisado freqüentemente, como programas, documentação, gráficos e
formulários de cartas.

%description -l es
Sistema de Control de Revisión (RCS) administra múltiples revisiones
de archivos. RCS automatiza el almacenamiento, recuperación,
registro, identificación y la fusión de revisiones. Es útil para
textos se revisan frecuentemente, como programas, documentación,
gráficos y formularios de cartas.

%description -l de
Das Revision Control Syste (RCS) verwaltet mehrere Dateirevisionen. 
Es automatisiert das Abspeichern, das Einlesen, das Aufzeichnen, 
die Erkennung und das Zusammenführen von Revisionen. RCS ist praktisch
für Texte, die häufig revidiert werden, etwa Programme, 
Dokumentation, Graphiken, Artikel und Formulare. 

%description -l fr
Le système de contrôle de révision (RCS) gère les nombreuses révisions
des fichiers. RCS automatise le stockage, la récupération, l'identification
et le mélange des révisions. RCS sert aux textes révisés fréquemment, par
exemple les "programmes, la documentation, les graphiques, les articles et
les lettres.  

%description -l tr
Sürüm denetim sistemi (Revision Control System - RCS) bir dosyanýn birden
fazla sürümünü denetlemek için kullanýlýr. RCS dosya üzerindeki
deðiþikliklerin tutulmasýný, saklanmasýný, kayýtlarýnýn tutulmasý iþlerini
kolaylaþtýrýr. Üzerinde sýkça deðiþiklik yapýlan program kodlarý, belgeler ve
makaleler için son derece yararlý bir araçtýr.

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
