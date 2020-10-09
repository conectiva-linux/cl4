Summary: creates and expand lharc format archives
Summary(pt_BR): Cria e expande arquivos no formato lharc
Summary(es): Crea y expande archivos en formato lharc
Name: lha
Version: 1.00
Release: 13cl
Copyright: freeware
Group: Applications/Archiving
Group(pt_BR): Aplica��es/Arquivamento
Group(es): Aplicaciones/Almacenaje
Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/lha-1.00.tar.Z
Patch: lha-1.00-fsstnd.patch
BuildRoot: /var/tmp/lha-root
Summary(de): erstellt und erweitert Archive im lharc-Format 
Summary(fr): cr�e et d�compresse des archives au format lharc
Summary(tr): lharc bi�imindeki ar�ivleri yarat�r ve geni�letir

%description
This is an archiving and compression utility.  It is mostly used
in the DOS world, but can be used under Linux to extract DOS 
files from LHA archives.

%description -l pt_BR
Este � um utilit�rio de armazenamento e compress�o. Ele � mais
utilizado no mundo DOS, mas pode ser usado no Linux para extrair
arquivos DOS.

%description -l es
Este es un utilitario de almacenaje y compresi�n. Es m�s utilizado
en el mundo DOS, pero puede ser usado en el Linux para extraer
archivos DOS.

%description -l de
Dies ist ein Archivierungs- und Komprimierungsdienstprogramm.
Es wird �berwiegend unter DOS verwendet, kann aber auch unter Linux
eingesetzt werden, um DOS-Dateien aus LHA-Archiven zu extrahieren.

%description -l fr
Un utilitaire d'archivage et de compression. il est surtout utilis� dans
le monde DOS, mais peut �tre utilis� sous Linux pour extraire des fichiers
dans des archives LHA.

%description -l tr
Bu bir dosya ar�ivleme ve s�k��t�rma program�d�r. Genelde DOS d�nyas�nda
kullan�lmakla birlikte LHA ar�ivlerinden DOS dosyalar�n� a�mak i�in Linux
alt�nda da kullan�labilir.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin

install -m755 -s src/lha $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc	README.Linux
/usr/bin/lha

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- add english doco.

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- removed man page, wasn't ASCII and caused more harm than good
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
