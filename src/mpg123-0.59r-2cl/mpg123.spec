Summary: MP3 Audio Player
Summary(pt_BR): Tocador de arquivos MP3
Summary(es): MP3 Audio Player
Name: mpg123
Version: 0.59r
Release: 2cl
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Url: http://www-ti.informatik.uni-tuebingen.de/~hippm/mpg123.html
Source: http://www-ti.informatik.uni-tuebingen.de/~hippm/mpg123-0.59r.tar.gz
Source1: mp3license
Patch0: mpg123.patch
Copyright: distributable
Buildroot: /var/tmp/mpg123-root

%description
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 (\"mp3\" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a Pentium CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on 486 CPUs.

For information on the MP3 License, please visit:
http://www.mpeg.org/

%description -l pt_BR
O mpg123 é um tocador de áudio MPEG para o Unix. Ele suporta MPEG
1.0/2.0 camadas 1, 2 e 3 (Arquivos .mp3).

Para informações na licença MP3, por favor visite:
http://www.mpeg.org/

%description -l es
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 (\"mp3\" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a Pentium CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on 486 CPUs.

For information on the MP3 License, please visit:
http://www.mpeg.org/

%prep
%setup -q 
%patch0 -p1 -b .mike

%build
make linux

%install
rm -rf $RPM_BUILD_ROOT/ 
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1

make install INSTALL=$RPM_BUILD_ROOT

%clean
rm -r $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc BUGS CHANGES COPYING INSTALL JUKEBOX README  TODO
%doc $RPM_SOURCE_DIR/mp3license
/usr/bin/mpg123
/usr/man/man1/mpg123.1

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 17 1999 Domingos Parra Novo <domingos@conectiva.com>
- Updated version to 0.59r

* Tue May 18 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux

* Sat Apr 17 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Rebuilt without esd support

* Mon Mar 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations

* Sat Mar  6 1999 Matt Wilson <msw@redhat.com>
- rebuilt against new libaudio and esd

* Fri Feb 26 1999 Michael Maher <mike@redhat.com>
- update package

* Tue Jan 12 1999 Michael Maher <mike@redhat.com>
- allowed to ship ... finally.

* Wed Jan 21 1998 Otto Hammersmith <otto@redhat.com>
- more cleanup
