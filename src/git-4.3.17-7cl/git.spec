Summary: GIT - GNU Interactive Tools
Summary(pt_BR): GIT - Ferramentas interativas da GNU
Summary(es): GIT - Herramientas interactivas de la GNU
Name: git
Version: 4.3.17
Release: 7cl
Copyright: GNU
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
# was .gz
Source: ftp://prep.ai.mit.edu:/pub/gnu/git-4.3.17.tar.bz2
Patch0: git-4.3.17-path.patch
Buildroot: /var/tmp/git-root
Prereq: info
Summary(de): GIT - GNU Interactive Tools
Summary(fr): GIT - Outils interactifs de GNU
Summary(tr): GNU görsel kabuðu

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- Fixed the dumb requirement for /usr/lib/git/term

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.3.17

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- added BuildRoot to spec file; added the path-correction patch
- added info file handling

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- built against readline library w/ proper soname

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
- Updated to v. 4.3.16

%description
GIT is a file system browser for UNIX systems.
An interactive process viewer/killer, a hex/ascii file
viewer, an auto-mount shell script and a per file type
action script are also available.

The standard ANSI color sequences are used where available.
Manual pages and info documentation are also provided.

%description -l pt_BR
GIT é um browser de sistema de arquivo para sistemas UNIX. Um
visualizador/matador interativo de processos, um visualizador de
arquivo hex/ascii, um script shell auto-mount e um script de ação
por tipo de arquivo também está disponível.  As seqüências-padrão
de cores ANSI são usados onde disponíveis.  Páginas de manual e
documentação de informação também são fornecidas.

%description -l es
GIT es un browser de sistema de archivo para sistemas UNIX. Un
visor/matador interactivo de procesos, un visor de archivo hex/ascii,
un script shell auto-mount y un script de ación por tipo de archivo
que también está disponible.  Las secuencias padrón de colores ANSI
se usan donde están disponibles. También son ofrecidas páginas de
manual y documentación de información.

%description -l de
GIT ist ein Dateisystem-Browser für UNIX-Systeme. Ein 
interaktiver Prozeß-Viewer/Killer, ein Hex/ASCII-Datei-Viewer, 
ein Auto-Mount-Shell-Skript und ein dateiformatbezogenes 
Aktions-Skript sind ebenfalls erhältlich. 

%description -l fr
GIT est un navigateur de systèmes de fichiers pour les systèmes UNIX.
Un visualisateur/destructeur interactif de processus, un visualisateur
de fichiers en hexa/ascii, un script shell d'automontage et un script
d'actions par type de fichier sont aussi disponibles.

Les séquences standard ANSI pour les couleurs sont utilisées
lorsqu'elles sont disponibles. Les pages du manuel et la doc info
sont aussi fournies.

%description -l tr
GIT, UNIX sistemler için bir dosya sistemi arayüzüdür. Etkileþimli bir süreç
görüntüleyici/sonlandýrýcý, bir hex/ascii dosya görüntüleyici, bir otomatik
baðlayýcý (auto-mount) kabuk betiði ve dosya tipine göre betik çalýþtýrma
yetenekleri vardýr.

%prep
rm -rf $RPM_BUILD_ROOT

%setup
%patch0 -p1 -b .path

%build
CFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS" LDFLAGS='-s' ./configure --prefix=/usr \
	--with-terminfo
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr/ install-strip
gzip -9nf $RPM_BUILD_ROOT/usr/info/git.info*

%files
%doc COPYING ChangeLog LSM NEWS PLATFORMS PROBLEMS README INSTALL
/usr/bin/*
/usr/bin/.gitaction
/usr/man/man1/*
/usr/info/*
/usr/lib/git/.gitrc*
%docdir /usr/lib/git/html

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/git.info.gz /usr/info/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/git.info.gz /usr/info/dir
fi
