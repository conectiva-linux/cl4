Summary: Red Hat X Authority Utility
Summary(pt_BR): Utilit�rio de Autoriza��o X da Red Hat
Summary(es): Utilitario de Autorizaci�n X de la Red Hat
Name: mkxauth
Version: 1.7
Release: 12cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
Source0: mkxauth
Source1: mkxauth.1x
BuildArchitectures: noarch
# Requires: /usr/X11R6/bin/xauth textutils fileutils sh-utils procps gzip
Requires: XFree86 textutils fileutils sh-utils procps gzip
Prefix: /usr/X11R6
BuildRoot: /var/tmp/mkxauth-root
Summary(de): Red Hat X-Autorit�ts-Utility  
Summary(fr): Utilitaire Red Hat pour les permissions X
Summary(tr): Red Hat X yetki arac�

%description
`mkxauth' aids in the creation and maintenance of X authentication
databases (.Xauthority files).  Use it to create a ~/.Xauthority file
or merge keys from another local or remote .Xauthority file.  Remote
.Xauthority files can be retrieved via ftp (using ncftp) or via rsh.
For security, mkxauth does not create any temporary files containing
authentication keys.

%description -l pt_BR
'mkxauth' ajuda na cria��o e manuten��o de bancos de dados
de autentica��o X (arquivos .Xauthority). Use-o para criar um
arquivo ~/.Xauthority ou para unir uma chaves de outro local ou
arquivo .Xauthority remoto. Arquivos remotos .Xauthority podem
ser recuperados via ftp (usando ncftp) ou via rsh. Por seguran�a,
mkxauth n�o cria quaisquer arquivos tempor�rios contendo chaves
de autentica��o.

%description -l es
'mkxauth' ayuda en la creaci�n y manutenci�n de bancos de datos
de autentificaci�n X (archivos .Xauthority). �salo para crear un
archivo ~/.Xauthority o para unir una llave de otro local o
archivo .Xauthority remoto. Se pueden recuperar archivos remotos
.Xauthority v�a ftp (usando ncftp) o v�a rsh. Por seguridad,
mkxauth no crea cualquier de los archivos temporales conteniendo
llaves de autentificaci�n.

%description -l de
`mkxauth' hilft beim Erstellen und Verwalten von X-Authentifizierungs-
Datenbanken (.Xauthority-Dateien). Sie k�nnen eine ~/.Xauthority-Datei
erstellen oder Schl�ssel aus einer anderen lokalen oder entfernten .Xauthority-
Datei einf�gen. .Xauthority-Dateien k�nnen �ber ftp (mit ncftp) oder rsh
wiederhergestellt werden. Aus Sicherheitsgr�nden erstellt mkxauth keine
Tempor�rdateien, die Authentifizierungsschl�ssel enthalten.

%description -l fr
mkxauth aide � la cr�ation et la maintenance des bases de donn�es
d'authentification X (fichiers .Xauthority). Utilisez le pour cr�er
un fichier ~/.Xauthority ou pour fusionner des cl�s � partir d'un
autre fichier .Xauthority, local ou distant. Les fichiers .Xauthority
distants peuvent �tre obtenus via ftp (avec ncftp) ou via rsh.
Pour des raisons de s�curit�, mkxauth ne cr�e pas de fichiers
temporaires contenant les cl�s d'authentification.

%description -l tr
mkxauth, X yetki veritabanlar�n�n (.Xauthority dosyalar�) olu�turulmas� ve
bak�m�nda yard�mc� olur. G�venlik a��s�ndan mkxauth, yetki anahtarlar� i�eren
ge�ici dosyalar olu�turmaz.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}

install -m 0755 $RPM_SOURCE_DIR/mkxauth $RPM_BUILD_ROOT/usr/X11R6/bin/mkxauth
install -m 0444 $RPM_SOURCE_DIR/mkxauth.1x $RPM_BUILD_ROOT/usr/X11R6/man/man1/mkxauth.1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/mkxauth
/usr/X11R6/man/man1/mkxauth.1x

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 17 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- fixed Requires

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added more dependency information.

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
