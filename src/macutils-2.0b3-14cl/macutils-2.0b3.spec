Summary: utilities for manipulating Macintosh file formats
Summary(pt_BR): Utilitários para manipulação de arquivos no formato MacIntosh (Apple)
Summary(es): Utilitarios para manipulación de archivos en formato MacIntosh (Apple)
Name: macutils
Version: 2.0b3
Release: 14cl
Copyright: disributable
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
# was .gz
Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/macutils.tar.bz2
Patch: macutils-misc.patch
BuildRoot: /var/tmp/macutils-root
Summary(de): Dienstprogramme zum Bearbeiten von Macintosh-Dateiformaten
Summary(fr): Utilitaires pour manipuler les fichiers au format Macintosh 
Summary(tr): Macintosh tipi dosyalarý iþlemek için araçlar

%description
This is a set of utilities for manipulating files from the
Macintosh.  Popular utilities like macunpack, hexbin, and
binhex are included.

%description -l pt_BR
Este é um conjunto de utilitários para manipulação de arquivos do
Macintosh. Utilitários populares como macunpack, hexbin e binhex
estão incluídos.

%description -l es
Este es un conjunto de utilitarios para la manipulación de archivos
del Macintosh. Están incluidos utilitarios populares como macunpack,
hexbin y binhex .

%description -l de
Dies ist eine Reihe von Dienstprogramme zum Bearbeiten von
Macintosh-Dateien. Enthalten sind u.a.: macunpack, hexbin und
binhex.

%description -l fr
C'est un ensemble d'utilitaires pour manipuler des fichiers provenant de
Macintosh. Des utilitaires populaires comme macunpack, hexbin, et binhex
sont inclus.

%description -l tr
Bu pakette Macintosh dosyalarýnýn iþlenmesinde kullanýlabilecek araçlar yer
almaktadýr. Paket macunpack, hexbin ve binhex gibi yaygýn olarak kullanýlan
programlarý içermektedir.

%prep
%setup -q -n macutils
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make BINDIR=$RPM_BUILD_ROOT/usr/bin install
cp man/* $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/bin/macunpack
/usr/bin/hexbin
/usr/bin/macsave
/usr/bin/macstream
/usr/bin/binhex
/usr/bin/tomac
/usr/bin/frommac
/usr/man/man1/binhex.1
/usr/man/man1/frommac.1
/usr/man/man1/hexbin.1
/usr/man/man1/macsave.1
/usr/man/man1/macstream.1
/usr/man/man1/macunpack.1
/usr/man/man1/macutil.1
/usr/man/man1/tomac.1

%changelog
* Wed Jun 16 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
