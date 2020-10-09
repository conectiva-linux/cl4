Summary: Real mode 80x86 assembler and linker
Summary(pt_BR): Assembler e Linker para modo real 80x86
Summary(es): Assembler y Linker para modo real 80x86
Name: bin86
Version: 0.4
Release: 9cl
Exclusivearch: i386
Copyright: distributable
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://sunsite.unc.edu/pub/Linux/GCC/bin86-0.4.tar.gz
Summary(de): Real-Mode 80x86 Assembler und Linker
Summary(fr): Assembleur 80x86 en mode r�el et �diteur de liens
Summary(tr): Ger�ek kip 80x86 �eviricisi ve ba�lay�c�s�

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Tue May 05 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use ExclusiveArch instead of Exclusive

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- minor spec file cleanups
- build rooted
- usees %attr() now

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%description
This package provides an assembler and linker for real mode 80x86
instructions. Programs that run in real mode, including LILO and the
kernel's bootstrapping code, need to have this package installed to
be built from the sources.

%description -l pt_BR
Este pacote prov� um assembler e um linker para instru��es 80x86
modo real. Programas que rodam em modo real, incluindo LILO e o
c�digo de boot do kernel, necessitam ter este pacote instalado para
serem constru�dos dos fontes.

%description -l es
Este paquete provee un assembler y un linker para instrucciones 80x86
modo real. Los programas que se ejecutan en modo real, incluyendo
LILO y el c�digo de boot del kernel, necesitan tener este paquete
instalado para que se construyan los fuentes.

%description -l de
Dieses Paket enth�lt einen Assembler und Linker f�r Real-Mode 80x86-
Instruktione. F�r Programme, die in Real-Mode laufen, einschlie�lich LILO
und der Bootstrapping-Code des Kernels, mu� dieses Paket installiert sein, 
damit sie von den Quellen gebaut werden k�nnen.

%description -l fr
Ce package fournit un assembleur et un �diteur de liens pour les
instructions du mode r�el 80x86. Les programmes tournat en mode r�el
dont LILO et code de bootstrapping du noyau, ont besoin de ce package
pour �tre reconstruits � partir des sources.

%description -l tr
Bu paket, ger�ek kip 80x86 y�nergeleri i�in bir �evirici ve ba�lay�c� sa�lar.
LILO ve �ekirde�in �ny�kleme kodlar� gibi ger�ek kipte ko�an programlar, bu
pakete gereksinim duyarlar.

%prep
%setup -q

%build
export PATH=$PATH:.
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -s -m 755 as/as86 $RPM_BUILD_ROOT/usr/bin
install -s -m 755 ld/ld86 $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%attr(-,root,root) /usr/bin/as86
%attr(-,root,root) /usr/bin/ld86
