Summary: TTY mode communications package ala Telix
Summary(pt_BR): Pacote de comunicações modo texto a la Telix
Summary(es): Paquete de comunicaciones modo texto a la Telix
Name: minicom
Version: 1.82
Release: 7cl
Copyright: GPL
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
# was .gz
Source: ftp://sunsite.unc.edu/pub/Linux/apps/serialcomm/dialout/minicom-%{PACKAGE_VERSION}.src.tar.bz2
Source1: minicom.wmconfig
Source800: minicom-wmconfig.i18n.tgz
Patch0: minicom-1.81-config.patch
Patch1: minicom-1.82-make.patch
Buildroot: /var/tmp/minicom-root
Summary(de): TTY-Modus-Kommunikationspaket (ähnlich Telix)
Summary(fr): Package de communication en mode terminal à la Telix
Summary(tr): Telix benzeri, TTY kipi iletiþim paketi


%description
Minicom is a communications program that resembles the MSDOS Telix
somewhat. It has a dialing directory, color, full ANSI and VT100
emulation, an (external) scripting language and more.

%description -l pt_BR
Minicom é um programa de comunicação que parece com o Telix do
MSDOS. Tem um diretório de discagem, cor, emulação completa ANSI
e VT100, e uma linguagem externa de scripts e mail.

%description -l es
Minicom es un programa de comunicación que se parece con el Telix
del MSDOS. Tiene un directorio de marcado, color, emulación completa
ANSI y VT100, y un lenguaje externo de sxripts y mail.

%description -l de
Minicom ist ein Kommunikationsprogramm, das Ähnlichkeiten mit Telix 
unter MSDOS aufweist. Es enthält ein Wählverzeichnis, Farbe, vollständige ANSI-
und VT100-Emulation, eine (externe) Scriptsprache usw.

%description -l fr
Minicom est un programme de communication ressemblant a Telix sous
MSDOS. Il a un répertoire de numérotation, des couleurs, une émualtion
ANSI et VT100, un langage de script externe et plus encore.

%description -l tr
Minicom, MSDOS Telix programýna benzeyen bir iletiþim programýdýr. Numara
çevirme dizini, renk, tam ANSI uyumu ve VT100 öykünümü ile script gibi
özellikleri vardýr.

%prep
%setup -q
%patch0 -p1 -b .config
%patch1 -p1 -b .make

%build
make -C src
 

%install
rm -rf $RPM_BUILD_ROOT
make -C src install R=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/bin/* ||:
echo "FIX ME !!!!!!!!!" >&2

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/




tar xvfpz $RPM_SOURCE_DIR/minicom-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc demos doc tables
%config /etc/minicom.users
%attr(755,root,root) /usr/bin/minicom
/usr/bin/runscript
/usr/bin/xminicom
/usr/bin/ascii-xfr
/usr/man/*/*
/usr/share/locale/*/LC_MESSAGES/minicom.mo
%config /etc/X11/wmconfig/minicom


%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 25 1999 Conectiva <dist@conectiva.com>
- wmconfig with minicom options "-s -con -L"

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Thu Feb 18 1999 Conectiva <dist@conectiva.com>
- added pt_BR translations
- included .mo to %files list

* Tue Jan 24 1999 Michael Maher <mike@redhat.com>
- fixed bug, changed groups.

* Thu Oct 01 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.82 to include i18n fixes

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- Built package for 5.2.

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- security fixes (alan cox, but he forgot about the changelog)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- BuildRoot; updated .make patch to cope with the buildroot
- fixed the spec file

* Tue May 06 1998 Michael Maher <mike@redhat.com>
- update of package (1.81)

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
