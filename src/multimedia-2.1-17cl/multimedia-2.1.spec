Summary: A CD player and audio mixer for X11
Summary(pt_BR): Um CD player e mixador de áudio para X11
Summary(es): Un CD player y mezclador de audio para X11
Name: multimedia
Version: 2.1
Release: 17cl
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Icon: speaker.gif
Source: ftp://sunsite.unc.edu/pub/Linux/apps/sound/suites/multimedia-2.1.tar.bz2
Source1: xplaycd.wmconfig
Source2: xmixer.wmconfig
Source800: multimedia-wmconfig.i18n.tgz
Patch: multimedia-2.1-misc.patch
Patch1: multimedia-2.1-scsi.patch
Patch2: multimedia-2.1-res.patch
Patch3: multimedia-2.1-64bit.patch
Patch4: multimedia-2.1-ustat.patch
Buildroot: /var/tmp/multimedia-root
Summary(de): Ein CD-Player und Audio-Mixer für X11
Summary(fr): Un lecteur CD audio et un mixer pour X11.
Summary(tr): X11 için CD çalýcý ve ses mikseri

%description
This package contains XPlaycd, XMixer and XGetfile.  XPlaycd is a
program to play audio cd's using a cdrom drive.  XMixer is used to
control the mixer on a soundcard.  XGetfile is a versatile file
browser, made for use in shell-scripts.

%description -l pt_BR
Este pacote contém XPlaycd, XMixer e XGetfile. XPlaycd é um programa
para tocar cds de áudio usando o drive de cdrom. XMixer é usado
para controlar a mixagem na placa de som. XGetfile é um versátil
navegador de arquivo, feito para usar em shell scripts.

%description -l es
Este paquete contiene XPlaycd, XMixer y XGetfile. XPlaycd es
un programa para reproducir cds de audio usando el drive de
cdrom. XMixer se usa para controlar las mezclas en la tarjeta de
sonido. XGetfile es un versátil navegador de archivo, hecho para
usar en shell scripts.

%description -l de
Dieses Paket enthält Xplaycd, Xmixer und Xgetfile. Xplaycd ist 
ein Programm zum Abspielen von Audio-CDs im CD-ROM-Laufwerk. Xmixer 
dient zur Steuerung des Mixers auf einer Soundkarte, und Xgetfile
ist ein Allround-Datei-Browser zur Benutzung in Shell-Skripts. 

%description -l fr
Ce paquetage contient XPlaycd, XMixer et XGetfile. XPlaycd est un programme pour
lire des CDs audio en utilisant le lecteur de CD-ROM. XMixer sert à commander le
mixer d'une carte son. XGetfile est un navigateur de fichier, créé pour être
utilisé dans des scripts shell.

%description -l tr
Bu paket XPlaycd, XMixer ve XGetfile programlarýný içerir. XPlaycd, cdrom
sürücü yoluyla ses cdlerini çalan bir programdýr. XMixer, ses kartý
üzerindeki mikserin kontrol edilmesini saðlar. XGetfile ise kabuk
yorumlayýcýlarýnda kullanýlabilecek bir dosya tarayýcýsýdýr.

%prep
%setup -q -n multimedia
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" LIBOPTS=-L/usr/X11R6/lib

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1,lib/X11/app-defaults} 
make install \
	BINDIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
	MANDIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
	DEFAULTDIR=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults \
	LIBDIR=$RPM_BUILD_ROOT/usr/X11R6/lib \
	MKDIR="mkdir -p"

chmod 644 $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/*
chmod 644 $RPM_BUILD_ROOT/usr/X11R6/man/man1/*
strip $RPM_BUILD_ROOT/usr/X11R6/bin/*
#mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
#install -m 0644 $RPM_SOURCE_DIR/xplaycd.wmconfig \
	#$RPM_BUILD_ROOT/etc/X11/wmconfig/xplaycd
#install -m 0644 $RPM_SOURCE_DIR/xmixer.wmconfig \
	#$RPM_BUILD_ROOT/etc/X11/wmconfig/xmixer

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/



tar xvfpz $RPM_SOURCE_DIR/multimedia-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/X11/wmconfig/*
/usr/X11R6/bin/*
/usr/X11R6/man/man1/*
%config /usr/X11R6/lib/X11/app-defaults/*
%doc INSTALL

%changelog
* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmixer & xplaycd wmconfig translated to pt_BR

* Thu Sep 17 1998 Jeff Johnson <jbj@redhat.com>
- use "mkdir -p" rather than mkdirhier to avoid IFS problem with bash-2.02.

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- spec install fix

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- Manhattan build
- buildroot

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated spec file
- added wmconfig stuff, but not included in file lists
  because users genarally cant control /dev/cdrom or /dev/mixer.
  Once users can do this we should include the wmconfig files.

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- incorporated 64bit cleanliness patch
- incorporated pointer init patch w/ makes xmplay work on Alphas
- built against glibc
