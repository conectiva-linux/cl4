Summary: A PostScript(TM) interpreter and renderer.
Summary(pt_BR): Interpretador e "renderizador" PostScript
Summary(es): Interpretador Y "renderizador" PostScript
Name: ghostscript
%define version	5.10
Version: %{version}
Release: 9cl
License: GPL
Icon: ghost.gif
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
# was .gz
Source0: ftp://prep.ai.mit.edu:/pub/gnu/ghostscript-%{version}.tar.bz2
Source1: ftp://prep.ai.mit.edu:/pub/gnu/ghostscript-%{version}jpeg.tar.bz2
Patch0: ghostscript-5.10-config.patch
Patch1: gs5.10-rth.patch
Requires: urw-fonts ghostscript-fonts
BuildRoot: /var/tmp/ghostscript-root

%description
Ghostscript is a set of software that provides a PostScript(TM)
interpreter, a set of C procedures (the Ghostscript library, which
implements the graphics capabilities in the PostScript language) and an
interpreter for Portable Document Format (PDF) files.  Ghostscript
translates PostScript code into many common, bitmapped formats, like those
understood by your printer or screen.  Ghostscript is normally used to
display PostScript files and to print PostScript files to non-PostScript
printers.

If you need to display PostScript files or print them to non-PostScript
printers, you should install ghostscript.  If you install ghostscript, you
also need to install the ghostscript-fonts package.

%description -l pt_BR
Ghostscript é um interpretador PostScript. Ele pode reproduzir
arquivos PostScript e PDF em dispositivos que incluem X Window,
vários formatos de impressão (incluindo suporte para impressoras
coloridas), e formatos de arquivos gráficos comuns.

%description -l es
Ghostscript es un interpretador PostScript. Puede reproducir
archivos PostScript y PDF en dispositivos que incluyen X Window,
varios formatos de impresión (incluyendo soporte para impresoras
coloridas), y formatos de archivos gráficos comunes.

%prep
%setup -q -n gs%{version}
%setup -q -T -D -a 1 -n gs%{version}
%patch0 -p1 -b .config
%patch1 -p1 -b .rth
ln -s unix-gcc.mak Makefile

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" prefix=/usr

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man,doc}
make install prefix=$RPM_BUILD_ROOT/usr
ln -sf gs.1 $RPM_BUILD_ROOT/usr/man/man1/ghostscript.1
ln -sf gs $RPM_BUILD_ROOT/usr/bin/ghostscript
strip $RPM_BUILD_ROOT/usr/bin/gs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/doc/ghostscript-%{PACKAGE_VERSION}
/usr/bin/*
%dir /usr/share/ghostscript
%dir /usr/share/ghostscript/%{PACKAGE_VERSION}
/usr/share/ghostscript/%{PACKAGE_VERSION}/*ps
/usr/share/ghostscript/%{PACKAGE_VERSION}/*upp
%config /usr/share/ghostscript/%{version}/Fontmap
/usr/share/ghostscript/%{PACKAGE_VERSION}/examples
/usr/man/*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr  5 1999 Conectiva <dist@conectiva.com>
- fixes config patch (thanks to Andre Freller)
- final rebuild for 3.0 spanish edition

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Cristian Gafton <gafton@redhat.com>
- added patch from rth to fix alignement problems on the alpha.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb 08 1999 Bill Nottingham <notting@redhat.com>
- add uniprint .upp files

* Sat Feb 06 1999 Preston Brown <pbrown@redhat.com>
- fontpath update.

* Wed Dec 23 1998 Preston Brown <pbrown@redhat.com>
- updates for ghostscript 5.10

* Fri Nov 13 1998 Preston Brown <pbrown@redhat.com>
- updated to use shared urw-fonts package.

* Mon Nov 09 1998 Preston Brown <pbrown@redhat.com>
- turned on truetype (ttf) font support.

* Thu Jul  2 1998 Jeff Johnson <jbj@redhat.com>
- updated to 4.03.

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- enabled more printer drivers
- buildroot

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Made /usr/share/ghostscript/3.33/Fontmap a config file.
