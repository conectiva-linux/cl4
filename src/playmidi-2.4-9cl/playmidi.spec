Summary: Play midi files on FM, GUS and MIDI devices
Summary(pt_BR): Toca arquivos midi em dispositivos FM, GUS e MIDI
Summary(es): Reproduce archivos midi en dispositivos FM, GUS y MIDI
Name: playmidi
Version: 2.4
Release: 9cl
# was .gz
Source: ftp://ftp.linpeople.org/pub/People/nathan/playmidi-2.4.tar.bz2
Source1: playmidi.wmconfig
Source2: awe_voice.h
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Patch0: playmidi-2.3-hertz.patch
Patch1: playmidi-2.3-awe2.patch
Patch2: playmidi-2.4-make.patch
Patch3: playmidi-2.4-midimap.patch
BuildRoot: /var/tmp/playmidi-root
Summary(de): Zum Abspielen von midi-Dateien auf FM-, GUS- und MIDI-Geräten
Summary(fr): Joue des fichiers midi sur des périphériques FM, GUS et MIDI.
Summary(tr): FM, GUS ve MIDI aygýtlarý üzerindeki midi dosyalarýný çalar

%package X11
Summary: X windows interface to MIDI sound player
Summary(pt_BR): Interface X Window para o tocador de som MIDI
Summary(es): Interface X Window para el reproductor de sonido MIDI
Requires: playmidi = 2.4
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Summary(de): X-Windows-Schnittstelle für den MIDI-Soundplayer
Summary(tr): MIDI ses çalýcý için X arayüzü

%description
Plays MIDI sound files through a sound card synthesizer. It includes 
basic drum samples for use with simple FM synthesizers.

%description -l pt_BR
Toca arquivos de som MIDI através de uma placa sintetizadora. Inclui
um exemplo básico de um tambor para uso com um sintetizador FM.

%description -l es
Toca archivos de sonido MIDI a través de una tarjeta sintetizadora.
Incluye un ejemplo básico de un tambor para uso con un sintetizador
FM.

%description X11
X program for playing MIDI sound files through a sound card synthesizer. It 
includes basic drum samples for use with simple FM synthesizers.

%description -l pt_BR X11
Programa X para tocar arquivos de som MIDI no sintetizador de uma
placa de som. Inclui exemplos simples para uso com sintetizadores
FM simples.

%description -l es X11
Programa X para tocar archivos de sonido MIDI en el sintetizador
de una tarjeta de sonido. Incluye ejemplos sencillos para uso con
sintetizadores FM simple.

%description -l de X11
X-Programm zum Abspielen von MIDI-Sounddateien über einen Soundkarten-
Synthesizer. Enthält einfache Schlagzeug-Samples für einfache FM-Synthesizers.

%description -l de
Spielt MIDI-Sounddateien über einen Soundkarten-Synthesizer ab. Enthält
einfache Schlagzeug-Samples für einfache FM-Synthesizer.

%description -l fr X11
Programme X pour jouer des fichiers MIDI par le synthétiseur d'une carte son.
Il contient des exemples de batterie de base pour les synthétiseurs FM simples.

%description -l fr
Programme X pour jouer des fichiers MIDI par le synthétiseur d'une carte son.
Il contient des exemples de batterie de base pour les synthétiseurs FM simples.

%description -l tr X11
MIDI ses dosyalarýný çalan playmidi uygulamasýnýn X arayüzü.

%description -l tr
Bir ses kartýnýn ses birleþtiricisi aracýlýðýyla MIDI ses dosyalarýný çalar.
FM ses birleþtirici ile kullaným için ana davul sesi örneklerý içerir.

%prep
%setup -q
cp $RPM_SOURCE_DIR/awe_voice.h .
%patch0 -p1 -b .consthertz
%patch1 -p1 -b .awe2
%patch2 -p1 -b .make
%patch3 -p1 -b .midimap

%build
PATH=.:$PATH

%ifarch i386
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" playmidi splaymidi xplaymidi <<EOF
2
EOF
%else
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" playmidi xplaymidi <<EOF
2
EOF
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/midi
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,X11R6/bin,X11R6/lib/X11/app-defaults}

install -s -m 755 playmidi $RPM_BUILD_ROOT/usr/bin
install -s -m 755 xplaymidi $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 644 XPlaymidi.ad $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/XPlaymidi

%ifarch i386
install -s -m 755 splaymidi $RPM_BUILD_ROOT/usr/bin
%endif

install -m 644 playmidi.1 $RPM_BUILD_ROOT/usr/man/man1

for n in std.o3 drums.o3 std.sb drums.sb
do
	install -m 644 $n $RPM_BUILD_ROOT/etc/midi/$n
done
#install -m 644 $RPM_SOURCE_DIR/playmidi.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/playmidi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc QuickStart COPYING BUGS
/usr/bin/playmidi 
%config /etc/midi/std.o3
%config /etc/midi/std.sb
%config /etc/midi/drums.o3
%config /etc/midi/drums.sb
%ifarch i386
/usr/bin/splaymidi
%endif
/usr/man/man1/playmidi.1

%files X11
%defattr(-,root,root)
%config /usr/X11R6/lib/X11/app-defaults/XPlaymidi
/usr/X11R6/bin/xplaymidi
#/etc/X11/wmconfig/playmidi

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed find-requires

* Thu Mar 25 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- removed wmconfig/playmidi (playmidi requires a file list on the cmd line)

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Mon Nov 30 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- traduções para pt_BR incluídas para Summary, %description e Group
- wmconfig também traduzido

* Mon Nov 23 1998 Bill Nottingham <notting@redhat.com>
- oops. We broke FM synth. Fixed.

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- updated to version 2.4

* Wed Sep  9 1998 Bill Nottingham <notting@redhat.com>
- added AWE32 support

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root
- sound font data in /etc/midi

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
