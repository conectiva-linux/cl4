Summary: full screen text mode program for playing audio CD's
Summary(pt_BR): Programa modo texto para tocar CD's de áudio
Summary(es): Programa modo texto para reproducir CD's de audio
Name: cdp
Version: 0.33
Release: 16cl
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: ftp://sunsite.unc.edu/pub/Linux/apps/sound/cdrom/curses/cdp-0.33.tgz
Patch: cdp-0.33-fsstnd.patch
Patch1: cdp-0.33-cdplay.patch
Patch2: cdp-0.33-ncurses.patch
Patch3: cdp-0.33-glibc.patch
Patch4: cdp-0.33-nobr.patch
Patch5: cdp-0.33-glibc-2.1.patch

BuildRoot: /var/tmp/cdp-root
Summary(de): Vollbildprogramm in Textmodus zum Abspielen von Audio-CDs
Summary(fr): Programme en mode texte plein écran pour lire les CD audio.
Summary(tr): Müzik CD'lerini çalmak için bir metin ekran programý

%description
This program allows you to play audio CD's on your computers CDROM drive. It
provides a version with a full screen interface as well as a command line
version.

%description -l pt_BR
Este programa permite a você tocar CDs de áudio no CD-ROM do seu
computador. Ele oferece uma versão com interface tela cheia assim
como uma versão com linha de comando.

%description -l es
Este programa te permite tocar CDs de audio en el CD-ROM de tu
ordenador. Se nos ofrece una versión con interface de pantalla llena,
así como una versión con línea de comando.

%description -l de
Mit diesem Programm können Sie die auf dem CD-ROM-Laufwerk Ihres Computers 
Audio-CDs abspielen. Es liegt in zwei Versionen vor: Einmal als Voll-
bildschirm-, einmal als Befehlszeilen-Version. 

%description -l fr
Ce programme permet de jouer des CDs audio sur le lecteur CDROM. Il offre
une version plein écran et une version en ligne de commande.

%description -l tr
Bu program, bilgisayarýnýzýn CDROM sürücüsünde müzik CD'lerini çalmanýza
yarar. Komut modunda veya tam ekran arayüzüyle kullanabilirsiniz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build

make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/cdp
/usr/bin/cdplay
/usr/man/man1/cdp.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 5 1999 Marcelo Tosatti <marcelo@conectiva.com>
- fixed glibc 2.1 problems

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Aug 15 1998 Jeff Johnson
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
