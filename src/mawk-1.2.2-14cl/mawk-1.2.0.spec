Summary: Mike's New/Posix AWK Interpreter
Summary(pt_BR): Novo interpretador (Posix) AWK do Mike
Summary(es): Nuevo interpretador (Posix) AWK del Mike
Name: mawk
Version: 1.2.2
Release: 14cl
Copyright: GPL
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
# was .gz
Source: ftp://ftp.oxy.edu/public/mawk1.2.2.tar.bz2
Patch: mawk1.2.2-prefix.patch
BuildRoot: /var/tmp/mawk-root
Summary(de): Mikes neuer Posix AWK-Interpretierer
Summary(fr): Mike's New/Posix AWK Interpreter : interpréteur AWK.
Summary(tr): Posix AWK Yorumlayýcýsý

%description
Mawk is a version of awk, which is a powerful text processing program.
In some areas mawk can outperform gawk, which is the standard awk
program on Linux.

%description -l pt_BR
Mawk é uma versão do awk, que é um poderoso programa processador
de texto. Em algumas áreas mawk pode superar gawk, que é o programa
awk padrão do Linux.

%description -l es
Mawk es una versión del awk, que es un fuerte programa procesador de
texto. En algunas áreas mawk puede superar gawk, que es el programa
awk padrón del Linux.

%description -l de
Mawk ist eine Version von awk, einem leistungsfähigen Textverarbeitungsprogramm. In bestimmten Bereichen leistet mawk mehr 
als gawk, das Standard-awk-Programm auf Linux. 

%description -l fr
mawk est une version d'awk, un puissant programme de traitement du texte.
Dans certains cas, mawk peut être supérieur à gawk, qui est le programme
awk standard sur Linux

%description -l tr
Mawk, çok güçlü bir metin iþleme programý olan awk'ýn bir sürümüdür. Bazý
durumlarda Linux un standart awk programý olan gawk'dan daha üstündür.

%prep
%setup -q
%patch -p1

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/mawk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/mawk
/usr/man/man1/mawk.1
%doc ACKNOWLEDGMENT CHANGES INSTALL README

%changelog
* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
