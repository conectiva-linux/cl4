Summary: Red Hat X Authority Utility
Summary(pt_BR): Utilitário de Autorização X da Red Hat
Summary(es): Utilitario de Autorización X de la Red Hat
Name: mkxauth
Version: 1.7
Release: 12cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source0: mkxauth
Source1: mkxauth.1x
BuildArchitectures: noarch
# Requires: /usr/X11R6/bin/xauth textutils fileutils sh-utils procps gzip
Requires: XFree86 textutils fileutils sh-utils procps gzip
Prefix: /usr/X11R6
BuildRoot: /var/tmp/mkxauth-root
Summary(de): Red Hat X-Autoritäts-Utility  
Summary(fr): Utilitaire Red Hat pour les permissions X
Summary(tr): Red Hat X yetki aracý

%description
`mkxauth' aids in the creation and maintenance of X authentication
databases (.Xauthority files).  Use it to create a ~/.Xauthority file
or merge keys from another local or remote .Xauthority file.  Remote
.Xauthority files can be retrieved via ftp (using ncftp) or via rsh.
For security, mkxauth does not create any temporary files containing
authentication keys.

%description -l pt_BR
'mkxauth' ajuda na criação e manutenção de bancos de dados
de autenticação X (arquivos .Xauthority). Use-o para criar um
arquivo ~/.Xauthority ou para unir uma chaves de outro local ou
arquivo .Xauthority remoto. Arquivos remotos .Xauthority podem
ser recuperados via ftp (usando ncftp) ou via rsh. Por segurança,
mkxauth não cria quaisquer arquivos temporários contendo chaves
de autenticação.

%description -l es
'mkxauth' ayuda en la creación y manutención de bancos de datos
de autentificación X (archivos .Xauthority). Úsalo para crear un
archivo ~/.Xauthority o para unir una llave de otro local o
archivo .Xauthority remoto. Se pueden recuperar archivos remotos
.Xauthority vía ftp (usando ncftp) o vía rsh. Por seguridad,
mkxauth no crea cualquier de los archivos temporales conteniendo
llaves de autentificación.

%description -l de
`mkxauth' hilft beim Erstellen und Verwalten von X-Authentifizierungs-
Datenbanken (.Xauthority-Dateien). Sie können eine ~/.Xauthority-Datei
erstellen oder Schlüssel aus einer anderen lokalen oder entfernten .Xauthority-
Datei einfügen. .Xauthority-Dateien können über ftp (mit ncftp) oder rsh
wiederhergestellt werden. Aus Sicherheitsgründen erstellt mkxauth keine
Temporärdateien, die Authentifizierungsschlüssel enthalten.

%description -l fr
mkxauth aide à la création et la maintenance des bases de données
d'authentification X (fichiers .Xauthority). Utilisez le pour créer
un fichier ~/.Xauthority ou pour fusionner des clés à partir d'un
autre fichier .Xauthority, local ou distant. Les fichiers .Xauthority
distants peuvent être obtenus via ftp (avec ncftp) ou via rsh.
Pour des raisons de sécurité, mkxauth ne crée pas de fichiers
temporaires contenant les clés d'authentification.

%description -l tr
mkxauth, X yetki veritabanlarýnýn (.Xauthority dosyalarý) oluþturulmasý ve
bakýmýnda yardýmcý olur. Güvenlik açýsýndan mkxauth, yetki anahtarlarý içeren
geçici dosyalar oluþturmaz.

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
