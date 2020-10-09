Summary: f2c program and static libraries
Summary(pt_BR): F2c e bibliotecas est�ticas
Summary(es): F2c y bibliotecas est�ticas
Name: f2c
Version: 19970805
Release: 8cl
Copyright: Distributable
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source: ftp://ftp.netlib.org/f2c.tar
Patch0: f2c-redhat.patch
Buildroot: /var/tmp/f2c-root
Obsoletes: f2c-libs
Summary(de): f2c-Programm- und statische Libraries 
Summary(fr): programme f2c et biblioth�ques statiques
Summary(tr): f2c program� ve statik kitapl�klar�

%description
f2c is a Fortran to C translation and building program.  It can
take fortran source code, convert it to C, and then use gcc to
compile it into an executable.  

%description -l pt_BR
f2c � um programa para tradu��o de fortran para C e para gera��o
de programas fortran. Ele converte o fonte fortran para C e usa o
gcc para compil�-lo e gerar seu execut�vel.

%description -l es
f2c es un programa para traducci�n de fortran para C y para
generaci�n de programas fortran. Convierte el fuente fortran para
C y usa gcc para compilarlo y crear su ejecutable.

%description -l de
f2c ist ein Fortran-auf-C-�bersetzer und -Compiler. Es kann
Fortran-Quellcode in C umwandeln und dann mit 'gcc' in eine
ausf�hrbare Datei kompilieren.

%description -l fr
f2c est un programme de traduction et de construction de Fortran
vers C. Il peut prendre un code source fortran, le convertir en C,
et utiliser gcc pour le compiler et en faire un  ex�cutable.

%description -l tr
f2c, Fortran dilinde yaz�lan bir kaynak dosyas�n� C'ye �evirerek gcc
yard�m�yla derleyebilir. Spice, Scilab gibi baz� yaz�l�mlar bu paket
i�erisinde bulunan matematik kitapl���n� kullan�rlar.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 29 1997 Cristian Gafton <gafton@redhat.com>
- upgraded to version 19970805
- added buildroot; removed libs subpackage and made it obsoleted

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Apr 17 1997 Erik Troan <ewt@redhat.com>
- Changed axp tag to alpha

* Fri Apr 11 1997 Michael Fulbright <msf@redhat.com>
- Fixed man page and made it install the troff version in correct place.
- Removed checksum calculation on sources, otherwise we cant patch source!

%prep
%setup -n f2c
unzip libf2c.zip
cp libf2c/makefile.u libf2c/Makefile
%patch0 -p 1 -b .redhat

%build
%ifarch axp
MFLAG=-mieee
%endif

make -C src RPM_OPT_FLAGS="$RPM_OPT_FLAGS" MFLAG="$MFLAG" f2c
make -C libf2c RPM_OPT_FLAGS="$RPM_OPT_FLAGS" MFLAG="$MFLAG" 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib,include,bin,man/man1}
install -m 644 libf2c/libf2c.a $RPM_BUILD_ROOT/usr/lib
install -m 644 f2c.h $RPM_BUILD_ROOT/usr/include
install -s -m 755 src/f2c $RPM_BUILD_ROOT/usr/bin/f2c
install -m 644 src/f2c.1t $RPM_BUILD_ROOT/usr/man/man1/f2c.1
install -m 755 libf2c/libf2c.so.0.22 $RPM_BUILD_ROOT/usr/lib
ln -sf libf2c.so.0.22 $RPM_BUILD_ROOT/usr/lib/libf2c.so
 

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc f2c.ps readme permission disclaimer changes src/Notice src/README
/usr/lib/*
/usr/include/*
/usr/bin/*
/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT
