Summary: GNU Bourne Again Shell (bash)
Summary(pt_BR): GNU Bourne Again Shell (bash)
Summary(es): GNU Bourne Again Shell (bash)
Name: bash
Version: 1.14.7
Release: 22cl
Group: System Environment/Shells
Group(pt_BR): Ambiente do Sistema/Interpretadores de Comandos
Group(es): Ambiente del Sistema/Interpretadores de Comandos
Copyright: GPL
# was .gz
Source0: ftp://prep.ai.mit.edu/pub/gnu/bash-1.14.7.tar.bz2
Source1: bashrc
Patch0: ftp.azstarnet.com:/pub/linux/axp/misc/bash-1.14.5.patch.gz
Patch1: bash-1.14.6.sparc.patch
Patch2: ftp.azstarnet.com:/pub/linux/axp/misc/bash-1.14.6-rh3.0.3-glibc.patch.gz
Patch3: bash-1.14.7-paths.patch
Patch4: bash-1.14.7-security.patch
Patch5: bash-1.14.7-mips.patch
Patch6: bash-1.14.7-signal.patch
Patch7: bash-1.14.7-winsz.patch
Patch8: bash-1.14.7-race.patch
Patch9: bash-1.14.7-secfix.patch
Patch10: bash-1.14.7-hist.patch
Requires: mktemp
Buildroot: /var/tmp/bash-root
Summary(de): GNU Bourne Again Shell (bash)
Summary(fr): GNU Bourne Again Shell (bash)
Summary(tr): GNU Bourne Again Shell (bash)

%description
Bash is an sh-compatible command language interpreter that
executes commands read from the standard input or from a
file.  Bash also incorporates useful features from the
Korn and C shells (ksh and csh).

Bash is ultimately intended to be a conformant implementation
of the IEEE Posix Shell and Tools specification (IEEE
Working Group 1003.2).

%description -l pt_BR
Bash é um interpretador de comandos compatível com sh, que executa
comandos lidos da entrada padrão ou de um arquivo. Bash também
incorpora características úteis das shells Korn e C (ksh e csh).
Bash tem sido desenvolvido para ser uma implementação compatível
com a especificação IEEE Posix para shells e ferramentas (IEEE
Working Group 1003.2).

%description -l es
Bash es un interpretador de comandos compatible con sh, que ejecuta
comandos leídos de la entrada padrón o de un archivo. Bash también
incorpora características útiles de las shells Korn y C (ksh y csh).
Bash ha sido desarrollado para ser una adición compatible con la
especificación IEEE Posix para shells y herramientas (IEEE Working
Group 1003.2).

%description -l de
Bash ist ein sh-kompatibler Befehlssprachen-Interpreter, der
über die Standardeingabe oder eine Datei gelesene Befehle ausführt.
Bash beinhaltet außerdem nützliche Funktionen der Korn- und der
C-Shell (ksh und csh).

Bash soll eine kompatible Implementierung der
'IEEE Posix Shell and Tools Specification' (IEEE
Working Group 1003.2) sein.

%description -l fr
Bash est un interpréteur de commande compatible sh qui exécute
les commandes lues sur l'entrée standard ou depuis un fichier.
Bash inclue également des fonctionnalités utiles des shells Korn et C
(ksh et csh).

Bash est prévu pour être une implémentation de shell conforme la
spécification Posix IEEE sur les shell et les outils (Groupe de 
travail IEEE 1003.2).

%description -l tr
Bash standart giriþten ya da bir dosyadan komut okuyup çalýþtýran sh uyumlu
bir komut dili yorumlayýcýsýdýr. Ayný zamanda Korn ve C kabuklarýnýn (ksh ve
csh) kullanýþlý özelliklerini de kapsar. Bash, IEEE Posix Kabuk ve Araç
ayrýntýlarýna (IEEE Working Group 1003.2) uyumlu bir uygulama olarak
tasarlanmýþtýr.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1 -b .secfix
%patch10 -p1 -b .hist

%build
make "CFLAGS=-g" prefix=/usr CC=gcc CPPNAME='$(CC) -E'
strip bash

%install
make prefix=$RPM_BUILD_ROOT/usr install
mkdir -p $RPM_BUILD_ROOT/bin $RPM_BUILD_ROOT/etc
mv $RPM_BUILD_ROOT/usr/bin/bash $RPM_BUILD_ROOT/bin/bash
rm -f $RPM_BUILD_ROOT/usr/bin/installed-bash
gzip -9nf $RPM_BUILD_ROOT/usr/info/bash.info
rm -f $RPM_BUILD_ROOT/usr/bin/bash.old
install -m644 $RPM_SOURCE_DIR/bashrc $RPM_BUILD_ROOT/etc/bashrc
ln -sf bash.1 $RPM_BUILD_ROOT/usr/man/man1/sh.1
ln -sf bash $RPM_BUILD_ROOT/bin/sh

%clean
rm -rf $RPM_BUILD_ROOT

# ***** bash doesn't use install-info. It's always listed in /usr/info/dir
# to prevent prereq loops

%post

HASBASH=""
HASSH=""

if [ ! -f /etc/shells ]; then
	> /etc/shells
fi

(while read line ; do
	if [ $line = /bin/bash ]; then
		HASBASH=1
	elif [ $line = /bin/sh ]; then
		HASSH=1
	fi
 done

 if [ -z "$HASBASH" ]; then
	echo "/bin/bash" >> /etc/shells
 fi

 if [ -z "$HASSH" ]; then
	echo "/bin/sh" >> /etc/shells
fi) < /etc/shells

%files
%defattr(-,root,root)
%doc NEWS README RELEASE
%config /etc/bashrc
/bin/bash
/bin/sh
/usr/info/bash.info.gz
/usr/man/man1/bash.1
/usr/man/man1/sh.1
/usr/bin/bashbug

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Provides: /bin/sh to satisfy the stupid Prereq so that we can have
  a small hdlist without RPMTAG_FILELIST

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Jan 21 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- -color=tty nos aliases para o ls no /etc/bashrc

* Tue Oct 27 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binary again

* Wed Oct 07 1998 Michael K. Johnson <johnsonm@redhat.com>
- history privacy fix (.hist)

* Sun Sep 06 1998 Cristian Gafton <gafton@redhat.com>
- security patch fix

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to enable TIOCWINSZ support in the readline lib
- patch for temp race on bashbug

* Fri Aug 07 1998 Erik Troan <ewt@redhat.com>
- rewrote %pre to not use grep anymore
- added %defattr line so package can be built as a user

* Thu Aug 06 1998 Erik Troan <ewt@redhat.com>
- removed %post; if they remove bash, they have bigger problems then extra
  /etc/shells entries! This makes the perreq loops easier to deal with

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Nov 07 1997 Donnie Barnes <djb@redhat.com>
- added signal handling patch from Dean Gaudet <dgaudet@arctic.org> that
  is based on a change made in bash 2.0.  Should fix some early exit
  problems with suspends and fg.

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- added %clean

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- added comment explaining why install-info isn't used
- added mips patch 

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc
