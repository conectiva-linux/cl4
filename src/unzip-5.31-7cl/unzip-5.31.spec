Summary: unpacks .zip files such as those made by pkzip under DOS
Summary(pt_BR): Descompacta arquivos com extensão .zip, como os criados pelo pkzip no DOS
Summary(es): unpacks .zip files such as those made by pkzip under DOS
Name: unzip
Version: 5.31
Release: 7cl
Copyright: distributable
Group: Applications/Archiving
Group(pt_BR): Aplicações/Arquivamento
Group(es): Aplicaciones/Almacenaje
# was .gz
Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/unzip531.tar.bz2
BuildRoot: /var/tmp/unzip-root
Summary(de): entpackt .zip-Dateien (etwa mit pkzip unter DOS erstellte) 
Summary(fr): décompresse les fichiers .zip créés par pkzip sous DOS
Summary(tr): pkzip ve benzeri programlarýn ürettiði zip arþivlerini açar

%description
unzip will list, test, or extract files from a ZIP archive, commonly
found on MS-DOS systems.  A companion program, zip, creates ZIP
archives; both programs are compatible with archives created by
PKWARE's PKZIP and PKUNZIP for MS-DOS, but in many cases the program
options or default behaviors differ.

%description -l pt_BR
Descompacta arquivos com extensão .zip, como os criados pelo pkzip no DOS

%description -l es
unzip will list, test, or extract files from a ZIP archive, commonly
found on MS-DOS systems.  A companion program, zip, creates ZIP
archives; both programs are compatible with archives created by
PKWARE's PKZIP and PKUNZIP for MS-DOS, but in many cases the program
options or default behaviors differ.

%description -l de
unzip dient zum Auflisten, Testen und Extrahieren von Dateien aus 
ZIP-Archiven, wie sie oft unter MS-DOS erstellt werden. Das 
Partnerprogramm ZIP erstellt ZIP-Archive. Beide Programme sind kompatibel 
zu Archiven, die mit PKWARE ZIP und PKUNZIP für MS-DOS komprimiert 
wurden, doch viele der Optionen und Standardeinstellungen sind anders. 

%description -l fr
unzip liste, teste ou extrait des fichiers d'une archive ZIP. zip crée
des archives ZIP ; les deux programmes sont compatibles avec les archives
créées avec PKZIP et PKUNZIP de PKWARE pour MS-DOS, mais les options ou
comportements par défaut diffèrent fréquemment


%description -l tr
unzip, MS-DOS sistemlerinde sýkça rastlanan ZIP arþivlerini listeler,
içeriklerini doðrular ve açar. Bu programa eþlik eden zip, ZIP arþivleri
oluþturmakta kullanýlýr. Her iki program da MS-DOS için PKWARE'in PKZIP
ve PKUNZIP uygulamalarý ile uyumludur ancak çoðu durumda seçeneklerinin
kullanýlýþý farklýdýr.

%prep
%setup -q -c
ln -s unix/Makefile Makefile

%build
%ifarch i386
make linux
%else
make linux_noasm
%endif

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/bin/{unzip,funzip,unzipsfx}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README BUGS COPYING INSTALL
/usr/bin/unzip
/usr/bin/funzip
/usr/bin/unzipsfx
/usr/bin/zipinfo
/usr/man/man1/unzip.1
/usr/man/man1/unzipsfx.1
/usr/man/man1/zipinfo.1
/usr/man/man1/funzip.1

%changelog
* Sun Jun 13 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- builds on non i386 platforms

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated the version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
