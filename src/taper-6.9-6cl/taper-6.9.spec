Summary: Menu driven backup system with support for compression
Summary(pt_BR): Sistema de backups com menus e suporte a compressão
Summary(es): Sistema de copias de seguridad con menús y soporte a compresión
Name: taper
Version: 6.9
Release: 6cl
Copyright: GPL
Group: Applications/Archiving
Group(pt_BR): Aplicações/Arquivamento
Group(es): Aplicaciones/Almacenaje
# was .gz
Source: http://www.omen.com.au/~yusuf/taper-%{version}.tar.bz2
URL: http://www.omen.com.au/~yusuf
Patch0: taper-%{version}-rh.patch
Patch1: taper-%{version}-sparc.patch
Patch2: taper-%{version}-fix.patch
Buildroot: /var/tmp/taper-root
Summary(de): Menügesteuertes Backupsystem mit Unterstützung für Komprimierung 
Summary(fr): Système de sauvegarde par menus avec gestion de la compression
Summary(tr): Sýkýþtýrma desteði sunan, menü tabanlý yedekleme sistemi

%description
This is a tape backup and restore program that provides a friendly user 
interface to allow backing/restoring files to a tape drive. Alternatively, 
files can be backed up to hard disk files. Selecting files for backup and 
restore is very similar to the Midnight Commander interface and allows easy 
traversal of directories. Recursively selected directories are supported. 
Incremental backup and automatic most recent restore are defaults settings. 
SCSI, ftape, zftape, and removable drives are supported

%description -l pt_BR
Este é um programa de backup e restore de fita, que oferece uma
interface amigável ao usuário. Arquivos podem ter sua cópia de
segurança em arquivos no disco rígido. A seleção de arquivos para
backup e restore é muito similar à interface do Midnight Commander
e permite fácil "navegação" de diretórios. Backup incremental e
restauração automática de arquivos mais recentes são configurações
default. SCSI, ftape, zftape e drives removíveis são suportados.

%description -l es
Este es un programa de backup y restore de cinta, que nos ofrece una
interface amigable al usuario. Los archivos pueden tener su copia
de seguridad en archivos en el disco duro. La selección de archivos
para backup y restore es muy similar a la interface del Midnight
Commander y permite fácil "navegación" de directorios. Backup
incremental y restauración automática de archivos más recientes,
son configuraciones por defecto. Son soportados SCSI, ftape, zftape
y drives removibles.

%description -l de
Ein Band-Backup- und Wiederherstellungsprogramm mit einer freundlichen
Bedienungsoberfläche zum Sichern/Wiederherstellen von Dateien in 
Kombination mit einem Bandlaufwerk. Alternativ können Dateien auch 
auf Festplatte gespeichert werden. Die Auswahl der zu sichernden bzw. 
wiederherzustellenden Dateien ist ähnlich wie beim Midight Commander - 
mit einfachem Verzeichniswechsel. Rekursiv ausgewählte Verzeichnisse 
werden unterstützt; inkrementelle Backups und automatische 
Wiederherstellung der zuletzt gespeicherten Version sind 
Standardeinstellungen. SCSI, ftape, zftape und Wechselplatten werden
unterstützt. 

%description -l fr
Programme de sauvegarde et de restauration sur bandes offrant une interface
utilisateur agréable. Les fichiers peuvent aussi être sauvegardés dans des
fichiers sur disque. La sélection des fichiers à sauvegarder er restaurer
est très similaire à l'interface de Midnight Commander et permet un parcours
facile des répertoires. La sélection récursive des répertoires est possible.
La sauvegarde incrémentale et la restauration automatique de la plus récente
sont les valeurs par défaut. Les lecteurs amovibles, SCSI, ftape, zftape sont
reconnus.

%description -l tr
Bu yazýlým, sevimli bir kullanýcý arayüzüne sahip bir manyetik bant yedekleme
ve geri yükleme sistemidir. Midnight Commander yazýlýmýnýn arayüzüne oldukça
benzeyen arayüzü sayesinde, dizinleri gezerek yedeklenecek ya da geri
yüklenecek dosyalarý seçmek oldukça kolaydýr. SCSI, ftape, zftape ve
takýlýr/çýkarýlýr sürücüler desteklenmektedir.

%prep
%setup -q
%patch0 -p1 -b .rh

%ifarch sparc
%patch1 -p1 -b .sparc
%endif

%patch2 -p1

find . -name CVS -type d | xargs rm -rf

%build
make CFLAGS="-g"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/*
/usr/bin/*
%doc docs/*

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Sep 28 1998 Cristian Gafton <gafton@redhat.com>
- fixed bg_backup and bg_restore segv when called from command line

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- upgraded to 6.9.
- move to /usr/{bin,sbin}
- sparc is big endian.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 6.8.4
- buildroot

* Tue Jan  6 1998 Otto Hammersmith <otto@redhat.com>
- readded -DGLIBC_2 to Makefile.common

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- upgraded to 6.8.0

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
