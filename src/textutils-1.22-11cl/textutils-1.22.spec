Summary: GNU Text Utilities
Summary(pt_BR): Utilitários para manipulação de textos da GNU
Summary(es): Utilitarios para manipulación de textos de la GNU
Name: textutils
Version: 1.22
Release: 11cl
Copyright: GPL
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Source: ftp://prep.ai.mit.edu/pub/gnu/textutils-1.22.tar.bz2
Source700: textutils-man-pt_BR.tar
Patch: textutils-1.22-glibc21.patch
Patch1: textutils-1.22-tmpfile.patch
Patch100: textutils-1.22-pt_BR.patch
Buildroot: /var/tmp/text-root
Prereq: info
Summary(de): GNU-Text-Utilities 
Summary(fr): Utilitaires texte de GNU
Summary(tr): GNU metin iþleme araçlarý

%description
These are the GNU text file (actually, file contents) processing
utilities.  They include programs to split, join, compare, and
modify files.

%description -l pt_BR
Estes são os utilitários GNU de processamento de arquivos texto. Ele
incluem programas para separar, juntar, comparar e modificar
arquivos.

%description -l es
Estos son los utilitarios GNU de procesamiento de archivos texto.
Incluyen programas para separar, juntar, comparar y modificar
archivos.

%description -l de
Dies sind die GNU-Textdatei- (oder, richtiger gesagt: Dateiinhalt-) 
Utilities. Dazu gehören Programme zum Aufteilen, zum Kombinieren, 
zum Vergleichen und zum Ändern von Dateien. 

%description -l fr
Utilitaires GNU pour le traitement des fichiers texte. Inclut des
programmes pour diviser, joindre, comparer et modifier les fichiers. 

%description -l tr
Bu paket, metin dosyalarýný iþleme araçlarý içerir. Bunlar arasýnda dosyalarý
bölmek, birleþtirmek, karþýlaþtýrmak ve deðiþtirmek için programlar vardýr.

%changelog
* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Dec  5 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Fri Nov  6 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild

* Fri Mar 06 1998 Michael K. Johnson <johnsonm@redhat.com>
- made tmpfile creation safe (even for root) in sort and tac.

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- added patch for glibc 2.1

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot
- added install-info support

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- Rebuilt against glibc

%prep
%setup
%patch -p1
%patch1 -p1 -b .tmpfile
%patch100 -p1 -b .pt_BR

%build
sleep 1
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -f $RPM_BUILD_ROOT/usr/info/textutils*
make prefix=$RPM_BUILD_ROOT/usr install
mkdir -p $RPM_BUILD_ROOT/bin
install -s -m 755 -o 0 -g 0 $RPM_BUILD_ROOT/usr/bin/cat $RPM_BUILD_ROOT/bin/cat
install -s -m 755 -o 0 -g 0 $RPM_BUILD_ROOT/usr/bin/sort $RPM_BUILD_ROOT/bin/sort
rm -f $RPM_BUILD_ROOT/usr/bin/cat $RPM_BUILD_ROOT/usr/bin/sort
gzip -9nf $RPM_BUILD_ROOT/usr/info/textutils*

cd $RPM_BUILD_ROOT
strip usr/bin/md5sum usr/bin/cksum usr/bin/comm usr/bin/csplit
strip usr/bin/cut usr/bin/expand usr/bin/fmt usr/bin/fold usr/bin/head
strip usr/bin/join usr/bin/nl usr/bin/od usr/bin/paste usr/bin/pr
strip usr/bin/split usr/bin/sum usr/bin/tac usr/bin/tail
strip usr/bin/tr usr/bin/unexpand usr/bin/uniq usr/bin/wc




mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/textutils-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%post
/sbin/install-info /usr/info/textutils.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/textutils.info.gz /usr/info/dir
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc NEWS README
/bin/*
/usr/bin/*
/usr/man/man*/*
/usr/info/textutils*
/usr/share/locale/*/*/*
%attr(0644,root,root) /usr/man/pt_BR/man*/*
