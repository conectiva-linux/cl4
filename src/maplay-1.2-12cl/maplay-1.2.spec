Summary: Plays MPEG 2 audio files in 16 bit stereo
Summary(pt_BR): Toca arquivos de áudio MPEG 2 em modo estéreo 16 bits
Summary(es): Reproduce archivos de audio MPEG 2 en modo stereo 16 bits
Name: maplay
Version: 1.2
Release: 12cl
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: ftp://ftp.iuma.com/audio_utils/mpeg_players/Workstations/maplay1_2.tar.Z
Patch0: maplay-1.2.patch
Patch1: maplay-1.2-sparc.patch
BuildRoot: /var/tmp/maplay-root
Summary(de): Spielt MPEG-2-Audiodateien in 16-Bit-Stereo ab 
Summary(fr): Joue des fichiers audio MPEG2 en 16 bits stéréo
Summary(tr): MPEG 2 ses dosyalarýný 16 bit stereo olarak çalar

%description
This program plays MPEG 2 format audio files through your PC's sound
card. MPEG audio files are popular for sending high fidelity music over
the Internet, and http://www.iuma.com contains a large archive of
MPEG 2 sound files.

%description -l pt_BR
Este programa toca arquivos de áudio de formato MPEG 2
através da placa de som do seu PC. Arquivos de áudio MPEG são
populares para enviar música com alta fidelidade pela Internet,
e http://www.iuma.com contém um longo estoque de arquivos de som
MPEG 2.

%description -l es
Este programa toca archivos de audio de formato MPEG 2 a través
de la tarjeta de sonido de tu PC. Los archivos de audio MPEG son
populares para enviar música con alta fidelidad por Internet,
y http://www.iuma.com contiene una gran cantidad de archivos de
sonido MPEG 2.

%description -l de
Dieses Programm spielt Audiodateien im MPEG-2-Format über die Sound-
karte ab. MPEG ist ein beliebtes Format zum Senden von HiFi-Musik über
das Internet. Unter http://www.iuma.com finden Sie ein großes Archiv mit
MPEG-2-Sounddateien.

%description -l fr
Ce programme joue des fichiers audio au format MPEG 2 en utilisant la
carte son du PC. Les fichiers audio MPEG sont pouplaires pour l'envoi
de musique en haute fidélité sur l'Internet. http://www.iuma.com
contient une archive importante de fichiers son MPEG 2.

%description -l tr
Bu program bilgisayarýnýzýn ses kartý yardýmýyla MPEG 2 formatýndaki ses
dosyalarýný çalar. MPEG ses dosyalarý Internet üzerinden yüksek kaliteli
müzik aktarýmýnda yaygýn olarak kullanýlýrlar. http://www.iuma.com adresinde
geniþ bir MPEG 2 ses dosyalarý arþivi bulabilirsiniz.

%prep
%setup -q -c
%patch -p0
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin

install -m 755 -s maplay $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/bin/maplay

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Dec 07 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Wed Oct 21 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
