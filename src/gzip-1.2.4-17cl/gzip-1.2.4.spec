Summary: GNU gzip file compression
Summary(pt_BR): Compressor de arquivos gzip GNU
Summary(es): Compresor de archivos gzip GNU
Name: gzip
Version: 1.2.4
Release: 17cl
Copyright: GPL
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
#Source: ftp://prep.ai.mit.edu/pub/gnu/gzip-1.2.4.tar.gz
# recompressed with bzip2 :)
Source: ftp://prep.ai.mit.edu/pub/gnu/gzip-1.2.4.tar.bz2
Source700: gzip-man-pt_BR.tar
Patch: gzip-1.2.4-basename.patch
Patch1: gzip-1.2.4-gzexe.patch
Patch2: gzip-1.2.4-mktemp.patch
Patch3: gzip-tmprace.patch
Prereq: info
Requires: mktemp
Buildroot: /var/tmp/gzip-root
Summary(de): Dateikomprimierung GNU-gzip
Summary(fr): GNU gzip pour la compression de fichiers.
Summary(tr): GNU gzip dosya sýkýþtýrma aracý

%changelog
* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Dec  5 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Mon Nov 30 1998 Marcelo Tosatti <marcelo@conectiva.com>
- arrumados tmp races no zdiff, zcmp, znew

* Tue Nov 17 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Fri Nov  6 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Tue Oct 27 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- added /usr/bin/gzip and /usr/bin/gunzip symlinks as some programs are too
  brain dead to figure out they should be at least trying to use $PATH
- added BuildRoot

* Wed Jan 28 1998 Erik Troan <ewt@redhat.com>
- fix /tmp races

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info
- applied patch for gzexe

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Marc Ewing <marc@redhat.com>
- (Entry added for Marc by Erik) fixed gzexe to use /bin/gzip

%description
This is the popular GNU file compression and decompression
program, gzip.  

%description -l pt_BR
Este é o popular programa GNU de compressão e descompressão de
arquivos, gzip.

%description -l es
Este es el popular programa GNU de compresión y descompresión de
archivos, gzip.

%description -l de
Dies ist das beliebte GNU-Dateikompressions- und Dekompressionsprogramm, 
gzip. 

%description -l fr
Programme de compression et de décompression gzip de GNU

%description -l tr
gzip, Unix iþletim sistemlerinde çok yaygýn olarak kullanýlan bir dosya
sýkýþtýrma ve açma aracýdýr.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 

%build
./configure --prefix=/usr
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/man
make install prefix=$RPM_BUILD_ROOT/usr
strip $RPM_BUILD_ROOT/usr/bin/gzip
mkdir -p $RPM_BUILD_ROOT/bin
mv -f $RPM_BUILD_ROOT/usr/bin/gzip $RPM_BUILD_ROOT/bin/gzip
rm -f $RPM_BUILD_ROOT/usr/bin/gunzip $RPM_BUILD_ROOT/usr/bin/zcat
ln -f $RPM_BUILD_ROOT/bin/gzip $RPM_BUILD_ROOT/bin/gunzip
ln -f $RPM_BUILD_ROOT/bin/gzip $RPM_BUILD_ROOT/bin/zcat
ln -sf ../../bin/gzip $RPM_BUILD_ROOT/usr/bin/gzip
ln -sf ../../bin/gunzip $RPM_BUILD_ROOT/usr/bin/gunzip
gzip -9nf $RPM_BUILD_ROOT/usr/info/gzip.info*

for i in zcmp zdiff zforce zgrep zmore znew ; do
	sed -e "s|$RPM_BUILD_ROOT||g" < $RPM_BUILD_ROOT/usr/bin/$i > $RPM_BUILD_ROOT/usr/bin/.$i
	rm -f $RPM_BUILD_ROOT/usr/bin/$i
	mv $RPM_BUILD_ROOT/usr/bin/.$i $RPM_BUILD_ROOT/usr/bin/$i
	chmod 755 $RPM_BUILD_ROOT/usr/bin/$i
done

cat > $RPM_BUILD_ROOT/usr/bin/zless <<EOF
#!/bin/sh
/bin/zcat "\$@" | /usr/bin/less
EOF
chmod 755 $RPM_BUILD_ROOT/usr/bin/zless



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/gzip-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%post
/sbin/install-info /usr/info/gzip.info.gz /usr/info/dir --entry="* gzip: (gzip).                 The GNU compression utility."

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/gzip.info.gz /usr/info/dir --entry="* gzip: (gzip).                 The GNU compression utility."
fi

%files
%doc NEWS README
/bin/*
/usr/bin/*
/usr/man/man*/*
/usr/info/gzip.info*
%attr(0644,root,root) /usr/man/pt_BR/man*/*
