Summary: Menu driven backup system with support for compression
Summary(pt_BR): Sistema de backups com menus e suporte a compress�o
Summary(es): Sistema de copias de seguridad con men�s y soporte a compresi�n
Name: taper
Version: 6.9
Release: 6cl
Copyright: GPL
Group: Applications/Archiving
Group(pt_BR): Aplica��es/Arquivamento
Group(es): Aplicaciones/Almacenaje
# was .gz
Source: http://www.omen.com.au/~yusuf/taper-%{version}.tar.bz2
URL: http://www.omen.com.au/~yusuf
Patch0: taper-%{version}-rh.patch
Patch1: taper-%{version}-sparc.patch
Patch2: taper-%{version}-fix.patch
Buildroot: /var/tmp/taper-root
Summary(de): Men�gesteuertes Backupsystem mit Unterst�tzung f�r Komprimierung 
Summary(fr): Syst�me de sauvegarde par menus avec gestion de la compression
Summary(tr): S�k��t�rma deste�i sunan, men� tabanl� yedekleme sistemi

%description
This is a tape backup and restore program that provides a friendly user 
interface to allow backing/restoring files to a tape drive. Alternatively, 
files can be backed up to hard disk files. Selecting files for backup and 
restore is very similar to the Midnight Commander interface and allows easy 
traversal of directories. Recursively selected directories are supported. 
Incremental backup and automatic most recent restore are defaults settings. 
SCSI, ftape, zftape, and removable drives are supported

%description -l pt_BR
Este � um programa de backup e restore de fita, que oferece uma
interface amig�vel ao usu�rio. Arquivos podem ter sua c�pia de
seguran�a em arquivos no disco r�gido. A sele��o de arquivos para
backup e restore � muito similar � interface do Midnight Commander
e permite f�cil "navega��o" de diret�rios. Backup incremental e
restaura��o autom�tica de arquivos mais recentes s�o configura��es
default. SCSI, ftape, zftape e drives remov�veis s�o suportados.

%description -l es
Este es un programa de backup y restore de cinta, que nos ofrece una
interface amigable al usuario. Los archivos pueden tener su copia
de seguridad en archivos en el disco duro. La selecci�n de archivos
para backup y restore es muy similar a la interface del Midnight
Commander y permite f�cil "navegaci�n" de directorios. Backup
incremental y restauraci�n autom�tica de archivos m�s recientes,
son configuraciones por defecto. Son soportados SCSI, ftape, zftape
y drives removibles.

%description -l de
Ein Band-Backup- und Wiederherstellungsprogramm mit einer freundlichen
Bedienungsoberfl�che zum Sichern/Wiederherstellen von Dateien in 
Kombination mit einem Bandlaufwerk. Alternativ k�nnen Dateien auch 
auf Festplatte gespeichert werden. Die Auswahl der zu sichernden bzw. 
wiederherzustellenden Dateien ist �hnlich wie beim Midight Commander - 
mit einfachem Verzeichniswechsel. Rekursiv ausgew�hlte Verzeichnisse 
werden unterst�tzt; inkrementelle Backups und automatische 
Wiederherstellung der zuletzt gespeicherten Version sind 
Standardeinstellungen. SCSI, ftape, zftape und Wechselplatten werden
unterst�tzt. 

%description -l fr
Programme de sauvegarde et de restauration sur bandes offrant une interface
utilisateur agr�able. Les fichiers peuvent aussi �tre sauvegard�s dans des
fichiers sur disque. La s�lection des fichiers � sauvegarder er restaurer
est tr�s similaire � l'interface de Midnight Commander et permet un parcours
facile des r�pertoires. La s�lection r�cursive des r�pertoires est possible.
La sauvegarde incr�mentale et la restauration automatique de la plus r�cente
sont les valeurs par d�faut. Les lecteurs amovibles, SCSI, ftape, zftape sont
reconnus.

%description -l tr
Bu yaz�l�m, sevimli bir kullan�c� aray�z�ne sahip bir manyetik bant yedekleme
ve geri y�kleme sistemidir. Midnight Commander yaz�l�m�n�n aray�z�ne olduk�a
benzeyen aray�z� sayesinde, dizinleri gezerek yedeklenecek ya da geri
y�klenecek dosyalar� se�mek olduk�a kolayd�r. SCSI, ftape, zftape ve
tak�l�r/��kar�l�r s�r�c�ler desteklenmektedir.

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
