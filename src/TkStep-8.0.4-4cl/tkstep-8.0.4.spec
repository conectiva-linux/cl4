%define version 8.0.4
%define release 4cl
%define prefix /usr
%define name TkStep

Summary: A restyled Tk which looks like n*xtStep.
Summary(pt_BR): Biblioteca tk com estilo parecido ao do n*xtStep.
Summary(es): A restyled Tk which looks like n*xtStep.
Summary(de): Ein umgestaltetes Tk das wie n*xtStep aussieht.
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Icon: tkstep.gif
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Prefix: %{prefix}
Source0: ftp://ftp.smli.com/pub/tcl/tk%{version}.tar.bz2
Source1: ftp://ftp.smli.com/pub/tcl/tcl%{version}.tar.bz2
Patch0: tk%{version}-to-tkstep%{version}-1.patch.bz2
BuildRoot: /var/tmp/%{name}-%{version}_root
Obsoletes: TkStep-replace TkStep-replace-devel TkStep-man

%description
This is a nextified tk%{version} with full OffiX DND 1.0 support.

A short summary of features:
- changed name of tkStepConfig.sh to tkstepConfig.sh
- TIFF read file support (requires libtiff)
- no colors limitation for XPMs
- transparent GIF, XPM and TIFF through masking
- can use any Dnd Types (also not defined ones !!!)

Tk is a X Windows widget set designed to work closely with the tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%description -l pt_BR
Esta é uma versão da biblioteca tk com aparência next, com suporte
completo a DND (Cortar/Copiar/Colar) 1.0 OffiX.
- 

%description -l es
This is a nextified tk%{version} with full OffiX DND 1.0 support.

A short summary of features:
- changed name of tkStepConfig.sh to tkstepConfig.sh
- TIFF read file support (requires libtiff)
- no colors limitation for XPMs
- transparent GIF, XPM and TIFF through masking
- can use any Dnd Types (also not defined ones !!!)

Tk is a X Windows widget set designed to work closely with the tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%description -l de
Dies ist ein nextifiziertes tk%{version} mit voller OffiX DND 1.0
Unterstützung.

Eine kurze Aufzählung der Fähigkeiten:
- tkstepConfig.sh zur Konfiguration von tk Anwendungen
- TIFF nur-lese Unterstützung (benötigt libtiff)
- keine Farbbeschränkung für XPMs
- transparente GIF, XPM und TIFF photos durch Masken
- man kann all DND typen verwenden (auch undefinierte !!!)

Tk ist ein Widget-Satz für X-Windows für den Einsatz mit der Script-
Sprache tcl. Sie können einfache Programme mit voll funktionsfähigen
GUIs in fast genauso schnell schreiben, wie eine zeichenorientierte
Oberfläche. Tcl/Tk-Anwendungen können auch auf Windows-
und Macintosh-Plattformen ausgeführt werden.

%package devel
Summary: TkStep static libraries and header files
Summary(pt_BR): Bibliotecas estáticas e arquivos de inclusão para desenvolvimento TkStep.
Summary(es): TkStep static libraries and header files
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Icon: tkstep-dev.gif
Requires: TkStep = %{version}

%description devel
Libraries and header files for developing C programs using or
extending the TkStep toolkit.  This package is not needed for writing
WishStep scripts, unless you wish to extend Tk using C code.

%description -l pt_BR devel
Bibliotecas estáticas e arquivos de inclusão para desenvolvimento TkStep.

%description -l es devel
Libraries and header files for developing C programs using or
extending the TkStep toolkit.  This package is not needed for writing
WishStep scripts, unless you wish to extend Tk using C code.

%description devel -l de
Bibliotheken und Header Dateien für die Entwicklung von C Erweiterungen
oder Applikationen die TkStep  verwenden. Dieses Paket wird nicht für
die Entwicklung von wish Skripten benötigt, außer Sie möchten TkStep
mit C erweitern.

%prep
if [ -e $RPM_BUILD_ROOT/usr/bin ]
then

%setup99 -D -T

else

%setup -c -a 0 -a 1

cd tk%{version}
%patch0 -p1
#%patch1 -p1
cd ..

#cd tcl%{version}
#%patch1 -p1
#cd ..

fi

%build

RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_REENTRANT"

cd tcl%{version}/unix
./configure --prefix=/usr \
	--enable-shared --enable-gcc --with-optimize="$RPM_OPT_FLAGS"
cd ../..

cd tk%{version}/unix
autoconf
./configure --prefix=/usr \
	--enable-shared --with-tcl=../../tcl%{version}/unix \
	--enable-gcc \
	--enable-dnd \
	--enable-step \
	--enable-xpm \
	--enable-tiff \
	--with-optimize="$RPM_OPT_FLAGS"
cp Makefile Makefile.shared
make
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--with-tcl=../../tcl%{version}/unix \
	--enable-gcc \
	--enable-dnd \
	--enable-step \
	--enable-xpm \
	--enable-tiff \
        --with-optimize="$RPM_OPT_FLAGS"
cp Makefile Makefile.static
make
cd ../..

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

cd tk%{version}/unix

make INSTALL_ROOT=$RPM_BUILD_ROOT install-binaries
cp Makefile.static Makefile
make INSTALL_ROOT=$RPM_BUILD_ROOT install-binaries
ln -sf libtkstep8.0.a $RPM_BUILD_ROOT/usr/lib/libtkstep.a
cp Makefile.shared Makefile
make INSTALL_ROOT=$RPM_BUILD_ROOT install
ln -sf libtkstep8.0.so $RPM_BUILD_ROOT/usr/lib/libtkstep.so
ln -sf wishstep8.0 $RPM_BUILD_ROOT/usr/bin/wishstep

cd ../..

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%files
%doc tk%{version}/README tk%{version}/README.TkStep tk%{version}/changes tk%{version}/license.terms tk%{version}/tkstep/*

/usr/lib/tkstep8.0
/usr/lib/libtkstep8.0.so
/usr/bin/wishstep
/usr/bin/wishstep8.0

%files devel
/usr/lib/tkstepConfig.sh
/usr/lib/libtkstep.a
/usr/lib/libtkstep8.0.a
/usr/lib/libtkstep.so
/usr/include/tkstep.h

%changelog
* Mon Jun 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- TkStep-replace, TkStep-replace-devel & TkStep-man taken out of distro

* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added pt_BR translations

* Fri Jan 22 1999 - Steve Murray (stevem@eng.uts.edu.au)
- borrowed Oliver's rpm SPEC file for tkstep8.0p2 and modified it
  for tkstep8.0.4 - this included accidently integrating the 'replace
  tk' patch.

* Tue Jul 28 1998 Oliver Graf <ograf@fga.de>
- recompiled using egcs 1.0.3 release with pentium optimization
- removed the python stuff, for making a seperate python-_tkinterstep
  package matching Oliver Andrichs RPM distribution (see Olivers
  quarter on starship.skyport.net)
- added prefix support
- fixed optimization
- man package conflicts with tk and TkStep-replace

* Mon Apr 27 1998 Oliver Graf <ograf@fga.de>
- added patch for replace-tk build
- added extra replace tk package
- forked off devel packages for both step and replace
