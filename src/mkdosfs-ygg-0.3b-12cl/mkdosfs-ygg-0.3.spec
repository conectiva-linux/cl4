Summary: Creates a DOS FAT filesystem on a device
Summary(pt_BR): Cria um sistema de arquivos FAT DOS em um dispositivo
Summary(es): Crea un sistema de archivos FAT DOS en un dispositivo
Name: mkdosfs-ygg
Version: 0.3b
Release: 12cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp.yggdrasil.com:/pub/dist/mkdosfs/mkdosfs-ygg-0.3b.tar.gz
Patch0: mkdosfs-ygg-0.3b-fix.patch
BuildRoot: /var/tmp/mkdosfs-ygg-root
Summary(de): Erstellt ein DOS-FAT-Dateisystem auf einem Gerät 
Summary(fr): Crée un système de fichiers DOS FAT sur un périphérique
Summary(tr): Bir aygýt üzerinde DOS FAT dosya sistemi oluþturur

%description
This is the mkdosfs package.  You can use this under Linux to
create MS-DOS FAT file systems.

%description -l pt_BR
Este é o pacote mkdosfs. Você pode usá-lo no Linux para criar
sistema de arquivos MS-DOS FAT.

%description -l es
Este es el paquete mkdosfs. Tu le puedes usar en el Linux para
crear sistema de archivos MS-DOS FAT.

%description -l de
Dies ist das mkdosfs-Paket, das Sie unter Linux benutzen können, 
um MS-DOS-FAT-Dateisysteme anzulegen. 

%description -l fr
Paquetage mkdosfs. Vous pouvez l'utiliser sous Linux pour créer des systèmes
de fichiers MS-DOS FAT.

%description -l tr
Bu program disk ya da disketlerin MSDOS formatýnda formatlanmalarýný saðlar.

%prep
%setup -q
%patch0 -p1 -b .fix

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,usr/man/man8}

install -m755 -s mkdosfs $RPM_BUILD_ROOT/sbin/mkfs.msdos
ln -sf mkfs.msdos $RPM_BUILD_ROOT/sbin/mkdosfs
install -m 644 mkdosfs.8 $RPM_BUILD_ROOT/usr/man/man8
ln -sf mkdosfs.8 $RPM_BUILD_ROOT/usr/man/man8/mkfs.msdos.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/mkfs.msdos 
/sbin/mkdosfs
/usr/man/man8/mkfs.msdos.8
/usr/man/man8/mkdosfs.8

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Oct 13 1998 Cristian Gafton <gafton@redhat.com>
- avoid using unsinged long on alphas 

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
