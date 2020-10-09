Summary: Plays MPEG 2 audio files in 16 bit stereo
Summary(pt_BR): Toca arquivos de �udio MPEG 2 em modo est�reo 16 bits
Summary(es): Reproduce archivos de audio MPEG 2 en modo stereo 16 bits
Name: maplay
Version: 1.2
Release: 12cl
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplica��es/Multim�dia
Group(es): Aplicaciones/Multimedia
Source: ftp://ftp.iuma.com/audio_utils/mpeg_players/Workstations/maplay1_2.tar.Z
Patch0: maplay-1.2.patch
Patch1: maplay-1.2-sparc.patch
BuildRoot: /var/tmp/maplay-root
Summary(de): Spielt MPEG-2-Audiodateien in 16-Bit-Stereo ab 
Summary(fr): Joue des fichiers audio MPEG2 en 16 bits st�r�o
Summary(tr): MPEG 2 ses dosyalar�n� 16 bit stereo olarak �alar

%description
This program plays MPEG 2 format audio files through your PC's sound
card. MPEG audio files are popular for sending high fidelity music over
the Internet, and http://www.iuma.com contains a large archive of
MPEG 2 sound files.

%description -l pt_BR
Este programa toca arquivos de �udio de formato MPEG 2
atrav�s da placa de som do seu PC. Arquivos de �udio MPEG s�o
populares para enviar m�sica com alta fidelidade pela Internet,
e http://www.iuma.com cont�m um longo estoque de arquivos de som
MPEG 2.

%description -l es
Este programa toca archivos de audio de formato MPEG 2 a trav�s
de la tarjeta de sonido de tu PC. Los archivos de audio MPEG son
populares para enviar m�sica con alta fidelidad por Internet,
y http://www.iuma.com contiene una gran cantidad de archivos de
sonido MPEG 2.

%description -l de
Dieses Programm spielt Audiodateien im MPEG-2-Format �ber die Sound-
karte ab. MPEG ist ein beliebtes Format zum Senden von HiFi-Musik �ber
das Internet. Unter http://www.iuma.com finden Sie ein gro�es Archiv mit
MPEG-2-Sounddateien.

%description -l fr
Ce programme joue des fichiers audio au format MPEG 2 en utilisant la
carte son du PC. Les fichiers audio MPEG sont pouplaires pour l'envoi
de musique en haute fid�lit� sur l'Internet. http://www.iuma.com
contient une archive importante de fichiers son MPEG 2.

%description -l tr
Bu program bilgisayar�n�z�n ses kart� yard�m�yla MPEG 2 format�ndaki ses
dosyalar�n� �alar. MPEG ses dosyalar� Internet �zerinden y�ksek kaliteli
m�zik aktar�m�nda yayg�n olarak kullan�l�rlar. http://www.iuma.com adresinde
geni� bir MPEG 2 ses dosyalar� ar�ivi bulabilirsiniz.

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
