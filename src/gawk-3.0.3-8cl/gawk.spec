Summary: GNU utilities text processor.
Summary(pt_BR): Utilitários GNU para manipulação arquivos texto.
Summary(es): Utilitarios GNU para manipulación de archivos texto.
Name: gawk
Version: 3.0.3
Release: 8cl
Copyright: GPL
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
#was .gz
Source0: ftp://prep.ai.mit.edu/pub/gnu/gawk-3.0.3.tar.bz2
Source1: ftp://prep.ai.mit.edu/pub/gnu/gawk-3.0.3-ps.tar.bz2
Patch: gawk-3.0-unaligned.patch
Buildroot: /var/tmp/gawk-root
Summary(de): GNU-Utilities Text-Prozessor
Summary(fr): Traitement de texte des utilitaires GNU
Summary(tr): GNU araçlarý metin düzenleyici

%description
This is GNU Awk. It should be upwardly compatible with the Bell Labs
research version of awk.  It is almost completely compliant with the
1993 POSIX 1003.2 standard for awk.

Gawk can be used to process text files and is considered a standard
Linux tool.

%description -l pt_BR
Este é o GNU Awk. Ele deve ser compatível com a versão de pesquisa de
awk do Bell Labs. Ele é quase completamente vinculado com o padrão
1993 POSIX 1003.2 para awk. Gawk pode ser usado para processar
arquivos texto e é considerado uma ferramenta padrão do Linux.

%description -l es
Este es el GNU Awk. Debe ser compatible con la versión de pesquisa
de awk del Bell Labs. Es casi completamente vinculado con el padrón
1993 POSIX 1003.2 para awk. Gawk puede ser usado para procesar
archivos texto y se considera una herramienta padrón del Linux.

%description -l de
Dies ist GNU Awk. Es sollte aufwärtskompatibel mit der Bell Labs-
Version von awk sein. Es ist fast vollständig konform mit dem 1993 
POSIX 1003.2-Standard für awk.
Gawk läßt sich zum Verarbeiten von Textdateien einsetzen und gilt als
ein Standard-Linux-Tool.

%description -l fr
awk de GNU, compatible vers le haut avec les versions awk des Bell Labs.
Il est presque totalement conforme au standard 1993 POSIX 1003.2 de awk.

gawk sert à traiter les fichiers texte est est considéré comme un outil
standard de Linux.

%description -l tr
Gawk metin dosyalarýný iþlemek için kullanýlan standart Linux araçlarýndan
biridir.

%package doc
Summary: Documentation on awk
Summary(pt_BR): Documentação sobre o gnu awk
Summary(es): Documentación sobre gnu awk
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación

%description doc
This package contains documentation on the text utility awk.

%description -l pt_BR doc
Este pacote contém documentação sobre o gnu awk.

%description -l es doc
Este paquete contiene documentación sobre el gnu awk.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 18 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Dec 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- final rebuild for 3.0
- criado subpacote doc

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- don't package /usr/info/dir

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 3.0.3
- added documentation and buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%prep
%setup -b 1
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr bindir=$RPM_BUILD_ROOT/bin
strip $RPM_BUILD_ROOT/bin/gawk
rm -f $RPM_BUILD_ROOT/usr/info/dir
gzip -9f $RPM_BUILD_ROOT/usr/info/gawk.info*
mkdir -p $RPM_BUILD_ROOT/usr/bin
ln -sf gawk.1 $RPM_BUILD_ROOT/usr/man/man1/awk.1
ln -sf ../../bin/gawk $RPM_BUILD_ROOT/usr/bin/awk 
ln -sf ../../bin/gawk $RPM_BUILD_ROOT/usr/bin/gawk 

%files
%doc README COPYING ACKNOWLEDGMENT FUTURES INSTALL LIMITATIONS NEWS PORTS 
%doc README_d POSIX.STD
/bin/*
/usr/bin/*
/usr/man/*/*
/usr/info/*info*
/usr/libexec/awk
/usr/share/awk

%files doc
%doc doc/gawk.ps doc/awkcard.ps

%clean
rm -rf $RPM_BUILD_ROOT
