Summary: A program to build tty dialog boxes
Summary(pt_BR): Programa para desenvolver caixas de diálogo em tty
Summary(es): Programa para desarrollar cajas de diálogo en tty
Name: dialog
Version: 0.6
Release: 17cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
# was .gz
Source: ftp.redhat.com:/pub/misc/dialog-0.6.tar.bz2
Patch0: dialog-0.6-ncurses.patch
Patch1: dialog-0.6-opt.patch
Patch2: dialog-0.6-loop.patch
Patch3: dialog-0.6-i18n.patch.bz2
BuildRoot: /var/tmp/dialog-root
Summary(de): Ein Programm zum Erstellen von tty-Dialogfeldern  
Summary(fr): Programme pour construire des boîtes de dialogue en mode texte
Summary(tr): tty diyalog kutularý oluþturan bir program

%description
Dialog is a utility that allows you to build user interfaces in
a TTY (text mode only).  You can call dialog from within a shell
script to ask the user questions or present with choices in a more
user friendly manner.  See /usr/doc/dialog-*/samples for some
examples.

%description -l pt_BR
Dialog é um utilitário que lhe permite programar interfaces de
usuário em um TTY (modo texto somente). Você pode chamar dialog de um
script shell para fazer perguntas ao usuário ou apresentar as opções
de uma maneira mais amigável. Veja /usr/doc/dialog-0.6-7/samples
para mais exemplos.

%description -l es
Dialog es un utilitario que te permite programar interfaces de
usuario en un TTY (modo texto solamente). Puedes llamar dialog de un
script shell para hacer preguntas al usuario o presentar las opciones
de una manera más amigable. Mira /usr/doc/dialog-0.6-7/samples para
más ejemplos.

%description -l de
Dialog ist ein Dienstprogramm, das das Erstellen einer Benutzeroberfläche
in einem TTY ermöglicht (nur Textmodus). Sie können dialog mit einem
Shell-Script aufrufen, um dem Benutzer auf benutzerfreundliche Weise
Fragen zu stellen oder eine Auswahl anzubieten. Unter
/usr/doc/dialog-*/samples finden Sie einige Beispiele.

%description -l fr
dialog est un utilitaire permettant de construire des interfaces
utilisateur en mode texte. On peut appeler dialog à partir d'un
script shell pour poser des questions à l'utilisateur ou lui
proposer des choix de façon conviviale. Voir /usr/doc/dialog-*/samples
pour quelques exemples.

%description -l tr
Dialog, metin ekran için kullanýcý arayüzleri oluþturmayý saðlayan bir
araçtýr. Kullanýcýya seçenekleri göstermek veya sorular sormak için, dialog
programýný bir kabuk programcýðý içinden çaðýrabilirsiniz. Örnekler için
/usr/doc/dialog-*/samples dizinine bakýnýz.

%prep
%setup -q
%patch0 -p1 -b .ncurses
%patch1 -p1 -b .opt
%patch2 -p1 -b .loop
%patch3 -p1 -b .i18n
cd src
make depend

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make PREFIX=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/bin/dialog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING dialog.lsm INSTALL README samples
/usr/bin/dialog
/usr/man/man1/dialog.1
/usr/share/locale/*/*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu Jul 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- i18n patch & pt_BR translation

* Thu May 7 1998 Michael Maher <mike@redhat.com> 
- Added Sean Reifschneider <jafo@tummy.com> patches for 
  infinite loop problems.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
