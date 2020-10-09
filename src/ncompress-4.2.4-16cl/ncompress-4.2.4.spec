Summary: a fast compress utility
Summary(pt_BR): Utilit�rio r�pido de compress�o
Summary(es): Utilitario r�pido de compresi�n
Name: ncompress
Version: 4.2.4
Release: 16cl
Copyright: unknown
Group: Applications/Archiving
Group(pt_BR): Aplica��es/Arquivamento
Group(es): Aplicaciones/Almacenaje
#Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/ncompress-4.2.4.tar.Z
# recompactado com bzip2
Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/ncompress-4.2.4.tar.bz2
Patch: ncompress-4.2.4-make.patch
BuildRoot: /var/tmp/ncompress-root
Summary(de): ein schnelles Komprimierungs-Dienstprogramm
Summary(fr): Utilitaire rapide de compression
Summary(tr): H�zl� bir s�k��t�rma arac�

%description
ncompress is a utility that will do fast compression and decompression
compatible with the original *nix compress utility (.Z extensions).  It will 
not handle gzipped (.gz) images (although gzip can handle compress images).

%description -l pt_BR
ncompress � um utilit�rio que faz compress�o e descompress�o r�pida,
compat�vel com o utilit�rio original de compress�o *nix (extens�es
.Z). Ele n�o ir� manipular imagens gzipadas (.gz) (mas o gzip pode
manipular imagens compactadas com o compress).

%description -l es
ncompress es un utilitario que hace compresi�n y descompresi�n
r�pida, compatible con el utilitario original de compresi�n *nix
(extensiones .Z). No ir� manipular im�genes gzipadas (.gz) (pero
el gzip puede manipular im�genes compactadas con el compress).

%description -l de
ncompress ist ein Utility zur Durchf�hrung schneller Komprimierungen und 
Dekomprimierungen, das zu dem Original *nix-Komprimierungs-Utility (.z-
Erweiterungen) kompatibel ist. gzip-Grafikdateien (.gz) k�nnen damit nicht 
verarbeitet werden (obwohl gzip mit compress-Dateien arbeiten kann). 

%description -l fr
ncompress est un utilitaire qui effectue une compression et une d�compression
rapide avec l'utilitaire de compression *nix original (extension .Z). Il ne
g�re pas les images gzipp�es (.gz) (bien que gzip puisse g�rer les images
compress).

%description -l tr
ncompress, orijinal Un*X compress uygulamas� ile uyumlu (.Z uzant�l�) h�zl�
s�k��t�rma ve a�ma i�lemleri yap�lmas�n� sa�lar. ncompress gzip ile
s�k��t�r�lm�� dosyalarla i�lem yapamaz. (gzip compress ile s�k��t�r�lm��
dosyalar �zerinde �al��abilir)

%prep

%setup -q
%patch -p1

%build

%ifarch i386
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS" ENDIAN=4321
%endif

%ifarch sparc m68k
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS" ENDIAN=1234
%endif

%ifarch alpha
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS -DNOALLIGN=0" ENDIAN=4321
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -s -m755 compress $RPM_BUILD_ROOT/usr/bin
ln -sf compress $RPM_BUILD_ROOT/usr/bin/uncompress
install -m644 compress.1 $RPM_BUILD_ROOT/usr/man/man1
ln -sf compress.1 $RPM_BUILD_ROOT/usr/man/man1/uncompress.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/compress
/usr/bin/uncompress
/usr/man/man1/compress.1
/usr/man/man1/uncompress.1
%doc LZW.INFO README

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun  4 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the spec file

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
