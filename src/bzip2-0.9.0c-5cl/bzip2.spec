Summary: Extremely powerful file compression utility
Summary(pt_BR): Um compactador de arquivos com um novo algoritmo
Summary(es): Un compresor de archivos con un nuevo algoritmo
Name: bzip2
Version: 0.9.0c
Release: 5cl
Copyright: GPL
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
# was .gz
URL: http://www.muraroa.demon.co.uk
Source: http://www.digistar.com/bzip2/bzip2-%{version}.tar.bz2
BuildRoot: /var/tmp/bzip2-root

%description
Bzip2  compresses  files  using the Burrows-Wheeler block-sorting text
compression algorithm, and Huffman coding. Compression is generally
considerably better than that achieved by more conventional LZ77/LZ78-based
compressors, and approaches the performance of the PPM family of statistical
compressors.

The command-line options are deliberately very similar to those of GNU Gzip,
but they are not identical.

%description -l pt_BR
Bzip2 é um programa de compressão/descompressão. Tipicamente o
arquivo compactado fica 20 a 30 por cento menor do que se fosse
compactado com o gzip.

Note que o bzip2 não entende os arquivos do bzip original, nem os
arquivos do gzip.

%description -l es
Bzip2 es un programa de compresión/descompresión. Típicamente el
archivo compactado queda entre 20 la 30 por ciento menor de que
se fuera compactado con gzip.  Observa que bzip2 no entiende los
archivos del bzip original, ni los archivos del gzip.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS" CC=egcs

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,include,lib}
install -s -m 755 bzip2 bzip2recover $RPM_BUILD_ROOT/usr/bin
ln -sf bzip2 $RPM_BUILD_ROOT/usr/bin/bunzip2
ln -sf bzip2 $RPM_BUILD_ROOT/usr/bin/bzcat
install -m 644 bzip2.1 $RPM_BUILD_ROOT/usr/man/man1
ln -sf bzip2.1 $RPM_BUILD_ROOT/usr/man/man1/bunzip2.1
ln -sf bzip2.1 $RPM_BUILD_ROOT/usr/man/man1/bzcat.1
install -m 644 libbz2.a $RPM_BUILD_ROOT/usr/lib
install -m 644 bzlib.h $RPM_BUILD_ROOT/usr/include

cat > $RPM_BUILD_ROOT/usr/bin/bzless <<EOF
#!/bin/sh
/usr/bin/bunzip2 -c "\$@" | /usr/bin/less
EOF
chmod 755 $RPM_BUILD_ROOT/usr/bin/bzless

%files
%doc  README *.html
/usr/bin/*
/usr/man/man1/*
/usr/lib/libbz2.a
/usr/include/bzlib.h

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr  1 1999 Conectiva <dist@conectiva.com>
- Updated to 0.9.0c

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 12 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- added pt_BR translations

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- force compilation with egcs to avoid gcc optimization bug (thank God 
  we haven't been beaten by it)

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- version 0.9.0b

* Tue Sep 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.9.0

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- first build for Manhattan
