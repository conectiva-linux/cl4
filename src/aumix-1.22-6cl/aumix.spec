Summary: curses based audio mixer
Summary(pt_BR): Mixador de áudio baseado em curses
Summary(es): Mezclador de audio basado en curses
Name: aumix
Version: 1.22
Release: 6cl
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: ftp://sunsite.unc.edu/pub/Linux/apps/sound/mixers/aumix-%{version}.tar.gz
Buildroot: /var/tmp/aumix-root
Summary(de): Audio-Mixer auf curses-Basis
Summary(fr): Mixer audio basé sur curses.
Summary(tr): Metin ekranlý ses karýþtýrýcý

%description
This program provides a tty based, interactive method of controlling a 
sound cards mixer. It lets you adjust the input levels from the CD,
microphone, and on board synthesizers as well as the output volume.

%description -l pt_BR
Este programa oferece um método interativo baseado em tty de
controle de mixagem de placas de som. Ele deixa você ajustar os
níveis de entrada do CD, microfone, e sintetizadores assim como o
volume de saída.

%description -l es
Este programa nos ofrece un método interactivo basado en tty de
control de mezclas de tarjetas de sonido. Deja que se ajuste los
niveles de entrada del CD, micrófono, y sintetizadores, así como
el volumen de salida.

%description -l de
Dieses Programm bietet eine interaktive Methode auf tty-Basis zur 
Steuerung eines Soundkarten-Mixers. Sie können damit die 
Eingangspegel der CD, des Mikrophons und von Synthesizer-Karten 
sowie auch die Ausgabelautstärke regeln. 

%description -l fr
Ce programme offre une méthode intaractive en mode texte pour contrôler
le mixer des cartes son. Il permet d'ajuster les niveaux d'entrée du CD,
du micro et des synthétiseurs de la carte, tout comme le volume de sortie.

%description -l tr
Bu program metin ekranda, etkileþimli olarak ses kartý mixer denetimi
yapmanýzý saglar. Çýktý sesinin yanýsýra, CD, mikrofon ve panel üzerindeki
birleþtiriciden girdi seviyelerini ayarlamanýza olanak verir.

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 11 1999 Marcelo Tosatti <marcelo@conectiva.com>
- update to 1.22

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Fri Oct  2 1998 Bill Nottingham <notting@redhat.com>
- updated to 1.13

* Fri Aug 28 1998 Bill Nottingham <notting@redhat.com>
- updated to 1.12

* Mon Aug 17 1998 Bill Nottingham <notting@redhat.com>
- updated to 1.11

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.8

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source url
- updated version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built with glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
- Updated to v. 1.6.1.

%prep
%setup
%build
automake
autoconf
./configure --prefix=/usr --without-alsa
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
( cd po ; make prefix=$RPM_BUILD_ROOT/usr install )

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO NEWS ChangeLog
/usr/bin/aumix
/usr/man/man1/aumix.1
/usr/share/locale/*/*/*
