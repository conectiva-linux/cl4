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
Summary(fr): Assembleur 80x86 en mode réel et éditeur de liens
Summary(tr): Gerçek kip 80x86 çeviricisi ve baðlayýcýsý

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
Este pacote provê um assembler e um linker para instruções 80x86
modo real. Programas que rodam em modo real, incluindo LILO e o
código de boot do kernel, necessitam ter este pacote instalado para
serem construídos dos fontes.

%description -l es
Este paquete provee un assembler y un linker para instrucciones 80x86
modo real. Los programas que se ejecutan en modo real, incluyendo
LILO y el código de boot del kernel, necesitan tener este paquete
instalado para que se construyan los fuentes.

%description -l de
Dieses Paket enthält einen Assembler und Linker für Real-Mode 80x86-
Instruktione. Für Programme, die in Real-Mode laufen, einschließlich LILO
und der Bootstrapping-Code des Kernels, muß dieses Paket installiert sein, 
damit sie von den Quellen gebaut werden können.

%description -l fr
Ce package fournit un assembleur et un éditeur de liens pour les
instructions du mode réel 80x86. Les programmes tournat en mode réel
dont LILO et code de bootstrapping du noyau, ont besoin de ce package
pour être reconstruits à partir des sources.

%description -l tr
Bu paket, gerçek kip 80x86 yönergeleri için bir çevirici ve baðlayýcý saðlar.
LILO ve çekirdeðin önyükleme kodlarý gibi gerçek kipte koþan programlar, bu
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
