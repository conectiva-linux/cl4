Summary: Berkeley SPICE 3 Circuit Simulator
Summary(pt_BR): SPICE simulador de circuitos
Summary(es): SPICE simulador de circuitos
Name: spice
Version: 3f4
Release: 10cl
Copyright: BSD
Group: Applications/Engineering
Group(pt_BR): Aplicações/Engenharia
Group(es): Aplicaciones/Ingeniería
Requires: readline >= 2.0
#Source0: sunsite.unc.edu:/pub/Linux/apps/circuits/spice3f4.tar.gz
# compactado com o bzip2, original esta como tar.gz
Source0: http://metalab.unc.edu/pub/Linux/apps/circuits/spice3f4.tar.bz2
Source1: http://metalab.unc.edu/pub/Linux/apps/circuits/spice3f4-patches-1.1.tar.gz

%description
SPICE 3 is a general-purpose circuit simulation program for nonlinear
dc, nonlinear transient, and linear ac analyses.  Circuits may contain
resistors, capacitors, inductors, mutual inductors, independent
voltage and current sources, four types of dependent sources,
transmission lines, and the four most common semiconductor devices:
diodes, BJT's, JFET's, and MOSFET's.

This is Spice 3f4 patched to 3f5, and includes the new port patches for
Linux, including GNU Lib C support, GNU Readline command-line editing 
and history file support, and native Spice support for X11R6 and MFB. 

%description -l pt_BR
SPICE é um programa de propósito geral para simulação de circuitos
para dc não linear, transiente não linear e análises de ac
linear. Circuitos podem conter resistores, capacitores, indutores,
indutores mútuos, fontes independentes de voltagem, quatro tipos de
fontes dependentes, linhas de transmissão e quatro dos dispositivos
semicondutores mais comuns: diodos, BJTs, JFETs e MOSFETs.

%description -l es
SPICE es un programa de propósito general para simulación de
circuitos para dc no linear, transiente no linear y análisis de
ac linear. Los circuitos pueden contener resistores, capacitores,
inductores, inductores mutuos, fuentes independientes de voltaje,
cuatro tipos de fuentes dependientes, líneas de transmisión y
cuatro de los dispositivos semiconductores más comunes: diodos,
BJTs, JFETs y MOSFETs.

%package examples
Summary: Berkeley SPICE 3 Example Files
Summary(pt_BR): Arquivos com exemplos para o SPICE 3 de Berkeley
Summary(es): Archivos con ejemplos para  SPICE 3 de Berkeley
Group: Applications/Engineering
Group(pt_BR): Aplicações/Engenharia
Group(es): Aplicaciones/Ingeniería
Requires: spice >= 3f4

%description examples
These are SPICE 3 example files for use with Berkeley SPICE 3.

%description -l pt_BR examples
Arquivos com exemplos para o SPICE 3 de Berkeley

%description -l es examples
Archivos con ejemplos para SPICE 3 de Berkeley

%prep 
%setup -n spice3f4 -a 1
patch -s -p1 -E < spice3f4-patches-1.1/spice3f4.defaults.patch
patch -s -p1 < spice3f4-patches-1.1/spice3f4.3f5.patch
patch -s -p1 < spice3f4-patches-1.1/spice3f4.fixes.patch
patch -s -p1 < spice3f4-patches-1.1/spice3f4.newlnx.patch
patch -s -p1 < spice3f4-patches-1.1/spice3f4.xlibs.patch
patch -s -p1 < spice3f4-patches-1.1/spice3f4.glibc.patch
patch -s -p1 < spice3f4-patches-1.1/spice3f4.dirs.patch
patch -s -p1 < spice3f4-patches-1.1/spice3f4.rdln.patch
rm `find . -name "*.orig" -print`

%build
./util/build linux CC_OPT="$RPM_OPT_FLAGS"

%install
./util/build linux install CC_OPT="$RPM_OPT_FLAGS"
strip /usr/bin/{spice3,help,nutmeg,sconvert,multidec,proc2mod}
cp -r examples /usr/lib/spice
install -m 644 man/man1/spice.1 /usr/man/man1
install -m 644 man/man1/nutmeg.1 /usr/man/man1
install -m 644 man/man1/sconvert.1 /usr/man/man1
install -m 644 man/man3/mfb.3 /usr/man/man3
install -m 644 man/man5/mfbcap.5 /usr/man/man5
cd /usr/man/man1
ln -sf spice.1 spice3.1

%files
%doc readme readme.Linux notes/spice2
%doc spice3f4-patches-1.1/README.patches
%dir /usr/lib/spice
/usr/lib/spice/lib
/usr/bin/spice3
/usr/bin/help
/usr/bin/nutmeg
/usr/bin/sconvert
/usr/bin/multidec
/usr/bin/proc2mod
/usr/man/man1/spice.1
/usr/man/man1/spice3.1
/usr/man/man1/nutmeg.1
/usr/man/man1/sconvert.1
/usr/man/man3/mfb.3
/usr/man/man5/mfbcap.5

%files examples
/usr/lib/spice/examples

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Dec 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- traduções para pt_BR incluídas para Summary, %description e Group
- compactado com bzip2
