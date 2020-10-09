Summary: Mike's New/Posix AWK Interpreter
Summary(pt_BR): Novo interpretador (Posix) AWK do Mike
Summary(es): Nuevo interpretador (Posix) AWK del Mike
Name: mawk
Version: 1.2.2
Release: 14cl
Copyright: GPL
Group: Applications/Text
Group(pt_BR): Aplica��es/Texto
Group(es): Aplicaciones/Texto
# was .gz
Source: ftp://ftp.oxy.edu/public/mawk1.2.2.tar.bz2
Patch: mawk1.2.2-prefix.patch
BuildRoot: /var/tmp/mawk-root
Summary(de): Mikes neuer Posix AWK-Interpretierer
Summary(fr): Mike's New/Posix AWK Interpreter : interpr�teur AWK.
Summary(tr): Posix AWK Yorumlay�c�s�

%description
Mawk is a version of awk, which is a powerful text processing program.
In some areas mawk can outperform gawk, which is the standard awk
program on Linux.

%description -l pt_BR
Mawk � uma vers�o do awk, que � um poderoso programa processador
de texto. Em algumas �reas mawk pode superar gawk, que � o programa
awk padr�o do Linux.

%description -l es
Mawk es una versi�n del awk, que es un fuerte programa procesador de
texto. En algunas �reas mawk puede superar gawk, que es el programa
awk padr�n del Linux.

%description -l de
Mawk ist eine Version von awk, einem leistungsf�higen Textverarbeitungsprogramm. In bestimmten Bereichen leistet mawk mehr 
als gawk, das Standard-awk-Programm auf Linux. 

%description -l fr
mawk est une version d'awk, un puissant programme de traitement du texte.
Dans certains cas, mawk peut �tre sup�rieur � gawk, qui est le programme
awk standard sur Linux

%description -l tr
Mawk, �ok g��l� bir metin i�leme program� olan awk'�n bir s�r�m�d�r. Baz�
durumlarda Linux un standart awk program� olan gawk'dan daha �st�nd�r.

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
