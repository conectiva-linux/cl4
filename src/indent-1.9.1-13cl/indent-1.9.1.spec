Summary: GNU C indenting program
Summary(pt_BR): Programa de indentação GNU C
Summary(es): Programa de tabulación automática GNU C
Name: indent
Version: 1.9.1
Release: 13cl
Copyright: GPL
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
# was .gz
Source: ftp://prep.ai.mit.edu/pub/gnu/indent-1.9.1.tar.bz2
Prereq: info
BuildRoot: /var/tmp/indent-root
Summary(de): GNU C-Indenting-Programm  
Summary(fr): Programme d'indentation C de GNU
Summary(tr): GNU C girintilendirme programý

%description
This is the GNU indenting program.  It is used to beautify
C program source files.

%description -l pt_BR
Este é o programa de indentação GNU. Ele é usado para organizar
arquivos fontes de programas C.

%description -l es
Este es el programa de tabulación horizontal GNU. Se usa para
organizar archivos fuentes de programas C.

%description -l de
Das GNU-Indenting-Programm. Zur Verschönerung Ihrer  
C-Programmquelldateienattraktiver aussehen! 

%description -l fr
Programme d'indentation de GNU. Utilisé pour embellir les
fichiers source C.

%description -l tr
Bu paket bir C programýnýn kaynak kodunu güzelleþtirmek için kullanýlýr.

%prep
%setup -q

%build
./configure --prefix=/usr
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,info,man/man1}

make prefix=$RPM_BUILD_ROOT/usr install
gzip -9nf $RPM_BUILD_ROOT/usr/info/indent.info*
install -m644 indent.1 $RPM_BUILD_ROOT/usr/man/man1

strip $RPM_BUILD_ROOT/usr/bin/indent

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/indent.info.gz /usr/info/dir --entry="* indent: (indent).				Program to format source code."

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/indent.info.gz /usr/info/dir --entry="* indent: (indent).                 	 Program to format source code."
fi

%files
%defattr(-,root,root)
/usr/bin/indent
/usr/man/man1/indent.1
/usr/info/indent.info*

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Wed Oct 21 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- use install-info

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
