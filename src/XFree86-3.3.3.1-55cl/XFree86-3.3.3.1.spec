Summary: Part of the XFree86 implementation of the X Window System.
Summary(pt_BR): Programas básicos e servidores para o sistema de janelas XFree86
Summary(es): Programas básicos y servidores para el sistema de ventanas XFree86
Name: XFree86
Version: 3.3.3.1
Release: 55cl
Serial: 1
Copyright: MIT
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
Requires: pam >= 0.66-13, XFree86-xfs, util-linux
Prereq: chkconfig utempter
BuildPrereq: utempter, freetype-devel, ncurses-devel

# was .gz and some big patchs have been recompressed with bz2
Source0: ftp://ftp.xfree86.org/pub/XFree86/3.3.3/X333src-1.tar.bz2
Source1: ftp://ftp.xfree86.org/pub/XFree86/3.3.3/X333src-2.tar.bz2
Source2: ftp://ftp.xfree86.org/pub/XFree86/3.3.3/X333src-3.tar.bz2
Source3: xserver.pamd
Source4: xdm.pamd
Source5: xfs.init
Source6: xfs.config
Source7: Xsession.redhat
Source8: xdm.init
Source700: XFree86-man-pt_BR.tar

Source102: XFree86-Xsession.conectiva
Source103: XFree86-Xsetup_0.conectiva
# already on freetype package
Source105: ttmkfdir.tar.gz
# Just to get some docs - truetype already's on XFree86-3.3.3.1-xfsft.patch.bz2
Source106: xfsft-1.0.3.tar.gz
# app-defaults/XTerm
Source107: XTerm

Patch0: XFree86-3.3.3-rh.patch
Patch1: XFree86-3.3.3.1-rhxdm.patch
Patch2: XFree86-3.3.2-fsstnd.patch
Patch3: XFree86-3.3.3.1-nopam.patch
Patch4: XFree86-3.3.3.1-pamconsole.patch
Patch5: XFree86-3.3.3-alpha-sockets.patch
Patch10: XFree86-3.3.3-sparc.patch.bz2
Patch11: XFree86-3.3.2-ffb.patch.bz2
Patch12: XFree86-3.3.3-fbdev.patch
Patch13: XFree86-3.3.3-xinput.patch
Patch14: XFree86-3.3.3.1-suncards.patch
Patch15: XFree86-3.3.3-sparc2.patch.bz2
Patch16: XFree86-3.3.3.1-creator2.patch.bz2
Patch17: XFree86-3.3.3.1-newcreator.patch.bz2
Patch18: XFree86-3.3.3.1-sparc3.patch.bz2
Patch19: XFree86-3.3.3.1-mach64.patch.gz
Patch20: XFree86-3.3.3.1-creator4.patch.bz2

Patch42: XFree86-3.3.2.3-jay.patch

Patch50: XFree86-3.3.2.3-86setup.patch
Patch51: XFree86-3.3.3.1-czskkbd.patch
Patch52: XFree86-3.3.3.1-is_keyboard.patch
Patch53: XFree86-3.3.3.1-nosuidxterm.patch
Patch54: XFree86-3.3.3-joy.patch
Patch55: XFree86-3.3.3-arm.patch
Patch56: XFree86-3.3.3.1-xfsft.patch.bz2
Patch57: XFree86-3.3.3-ru_SU.patch
Patch58: XFree86-3.3.3.1-startx_xauth.patch
Patch59: XFree86-3.3.3.1-xfsredhat.patch
Patch60: XFree86-3.3.3.1-mgafix.patch
Patch61: XFree86-3.3.3.1-alphadga.patch
# already OK in 3.3.4
Patch62: XFree86-3.3.3.1-dga1.1.patch
Patch63: XFree86-3.3.3.1-thinkingmouse.patch
Patch64: XFree86-3.3.3.1-dvorak.patch

Patch65: XFree86-3.3.3.1-ffbcrash.patch
Patch66: XFree86-3.3.3.1-G200dga.patch
Patch67: XFree86-3.3.3.1-ru_sparc.patch
Patch68: XFree86-3.3.3.1-xinitrace.patch
Patch69: XFree86-3.3.3.1-fixiso8859-2.patch

# already OK in 3.3.4
Patch75: XFree86-3.3.3.1-tmpdir.patch

Patch100: 3.3.3-3.3.3.1.diff

# already OK in 3.3.4
# ftp://ftp1.detonator.nvidia.com/pub/drivers/english/riva-tnt-tnt2-vanta/linux
Patch103: XFree86-3.3.3.1-NvidiaTNT_TNT2.patch.bz2

# fica aqui por enquanto, pois deve sair com o 3.3.4 ou algo parecido
Patch190: 3.3.3.1-3.3.3.1a.diff.bz2
Patch191: 3.3.3.1a-3.3.3.1b.diff.bz2
Patch192: 3.3.3.1b-3.3.3.1c.diff.bz2
Patch193: 3.3.3.1c-3.3.3.1d.diff.bz2
Patch194: 3.3.3.1d-3.3.3.1e.diff.bz2
Patch195: 3.3.3.1e-3.3.3.1f.diff.bz2
Patch196: 3.3.3.1f-3.3.3.1Z.diff.bz2

Patch197: 3.3.3.1Z-S3-Aurora.patch
Patch198: 3.3.3.1Z-atiprobe.patch
Patch199: 3.3.3.1Z-manpages.patch

# our patchs
Patch110: XFree86-3.3.1-dead-keys.diff
Patch111: xkb-brazilian.patch
Patch112: XFree86-3.3.3.1-trident9x5.patch
Patch113: XFree86-libtermcap.patch
Patch777: Cards.patch
Patch778: Cards-SiS.patch

Exclusivearch: i386 alpha sparc m68k armv4l

%ifarch sparc
Obsoletes: X11R6.1
%endif
Obsoletes: xserver-wrapper xterm-color

BuildRoot: /var/tmp/%{name}-root

%description
If you want to install the X Window System (TM) on
your machine, you'll need to install XFree86.

The X Window System provides the base technology
for developing graphical user interfaces. Simply stated,
X draws the elements of the GUI on the user's screen and
builds methods for sending user interactions back to the
application. X also supports remote application deployment--running an
application on another computer while viewing the input/output 
on your machine.  X is a powerful environment which supports
many different applications, such as games, programming tools,
graphics programs, text editors, etc.  XFree86 is the version of
X which runs on Linux, as well as other platforms.

This package contains the basic fonts, programs and documentation
for an X workstation.  However, this package doesn't provide the
program which you will need to drive your video hardware.  To
control your video card, you'll need the particular X server
package which corresponds to your computer's video card.

In addition to installing this package, you will need to install 
the XFree86 package which corresponds to your video card, the 
X11R6-contrib package, the Xconfigurator package and the XFree86-libs 
package. You may also need to install one of the XFree86 fonts packages.  

And finally, if you are going to develop applications that run as 
X clients, you will also need to install XFree86-devel.

%description -l pt_BR
X Window é uma interface gráfica completa com múltiplas janelas,
múltiplos clientes e diferentes estilos de janelas. É usado na
maioria das plataformas Unix, e clientes também podem rodar em
outros sistemas de janelas populares.  O protocolo X permite que
aplicações possam rodar tanto na máquina local como através da rede,
provendo flexibilidade em implementações cliente/servidor.

Este pacote contém as fontes básicas, programas e documentação para
uma estação de trabalho X. Ele não fornece um servidor X que acessa
seu hardware de vídeo -- estes são disponibilizados em outro pacote.

%description -l es
X Window es una interface gráfica completa con múltiples ventanas,
múltiples clientes y diferentes estilos de ventanas. Se usa en la
mayoría de las plataformas Unix, y los clientes también pueden
ejecutar en otros sistemas de ventanas populares.  El protocolo
X permite que las aplicaciones puedan ejecutarse tanto en la
máquina local como a través de la red, y proveer flexibilidad
en implementaciones cliente/servidor.  Este paquete contiene las
fuentes básicas, programas y documentación para una estación de
trabajo X. No ofrece un servidor X que acceda tu hardware de vídeo --
estos son puestos a disposición  en otro paquete.

%package 75dpi-fonts
Summary: A set of 75 dpi resolution fonts for the X Window System.
Summary(pt_BR): Fontes X11R6 75dpi - somente necessários no lado do servidor
Summary(es): Fuentes X11R6 75dpi - solamente necesarios en el lado del servidor
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
Prereq: chkfontpath
%ifarch sparc
Obsoletes: X11R6.1-75dpi-fonts
%endif

%description 75dpi-fonts
XFree86-75dpi-fonts contains the 75 dpi fonts used
on most X Window Systems. If you're going to use the 
X Window System, you should install this package, unless 
you have a monitor which can support 100 dpi resolution. 
In that case, you may prefer the 100dpi fonts available in 
the XFree86-100dpi-fonts package.

You may also need to install other XFree86 font packages.

To install the X Window System, you will need to install
the XFree86 package, the XFree86 package corresponding to
your video card, the X11R6-contrib package, the Xconfigurator
package and the XFree86-libs package.

Finally, if you are going to develop applications that run
as X clients, you will also need to install the
XFree86-devel package.

%description -l pt_BR 75dpi-fonts
As fontes 75dpi usadas na maioria dos sistemas Linux. Usuários
com monitores de alta resolução podem preferir as fontes de 100dpi
disponíveis em um pacote separado.

%description -l es 75dpi-fonts
Las fuentes 75dpi usadas en la mayoría de los sistemas
Linux. Usuarios con monitores de alta resolución pueden preferir
las fuentes de 100dpi disponibles en un paquete a parte.

%package 100dpi-fonts
Summary: X Window System 100dpi fonts.
Summary(pt_BR): Fontes X11R6 100dpi - somente necessários no lado do servidor
Summary(es): Fuentes X11R6 100dpi - solamente necesarios en el lado del servidor
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
Prereq: chkfontpath
%ifarch sparc
Obsoletes: X11R6.1-100dpi-fonts
%endif

%description 100dpi-fonts
If you're going to use the X Window System and you have a
high resolution monitor capable of 100 dpi, you should install
XFree86-100dpi-fonts. This package contains a set of
100 dpi fonts used on most Linux systems.

If you are installing the X Window System, you will also
need to install the XFree86 package, the XFree86
package corresponding to your video card, the X11R6-
contrib package, the Xconfigurator package and the
XFree86-libs package. If you need to display certain
fonts, you may also need to install other XFree86 fonts
packages.

And finally, if you are going to develop applications that
run as X clients, you will also need to install the
XFree86-devel package.

%description -l pt_BR 100dpi-fonts
As fontes 100dpi usadas na maioria dos sistemas Linux. Aconselhado
à usuários com monitores de alta resolução.

%description -l es 100dpi-fonts
Las fuentes 100dpi usadas en la mayoría de los sistemas Linux. Se
recomienda a usuarios con monitores de alta resolución.

%package cyrillic-fonts
Summary: Cyrillic fonts - only needed on the server side.
Summary(pt_BR): Fontes cirílicas
Summary(es): Fontes cirílicas
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
Prereq: chkfontpath

%description cyrillic-fonts
The Cyrillic fonts included with XFree86 3.3.2 and higher. Those who
use a language requiring the Cyrillic character set should install
this package.

%description -l pt_BR cyrillic-fonts
Fontes cirílicas incluídas com o XFree86. Usuários de idiomas baseados
em caracteres cirílicos devem instalar este pacote.

%description -l es cyrillic-fonts
Fuentes cirílicas se incluyen con XFree86. Los usuarios de idiomas
basados en caracteres cirílicos deben instalar este paquete.

%package libs
Summary: Shared libraries needed by the X Window System version 11 release 6.
Summary(pt_BR): Bibliotecas compartilhadas X11R6
Summary(es): Bibliotecas compartidas X11R6
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Prereq: grep /sbin/ldconfig
%ifarch sparc
Obsoletes: X11R6.1-libs
%endif

%description libs
XFree86-libs contains the shared libraries that most X programs
need to run properly. These shared libraries are in a separate package in
order to reduce the disk space needed to run X applications on a machine
without an X server (i.e, over a network).

If you are installing the X Window System on your machine, you will need to
install XFree86-libs.  You will also need to install the XFree86 package,
the XFree86-75dpi-fonts package or the XFree86-100dpi-fonts package
(depending upon your monitor's resolution), the Xconfigurator package and
the X11R6-contrib package.  And, finally, if you are going to be developing
applications that run as X clients, you will also need to install
XFree86-devel.

%description -l pt_BR libs
Este pacote contém bibliotecas compartilhadas que a maioria dos
programas X precisam para rodar corretamente. Eles estão em um
pacote separado para reduzir o espaço em disco necessário para rodar
aplicações X em uma máquina sem um servidor X (através da rede).

%description -l es libs
Este paquete contiene bibliotecas compartidas que la mayoría de
los programas X necesitan para ejecutarse correctamente. Están en
un paquete a parte, para reducir el espacio en disco necesario para
ejecutar aplicaciones X en una máquina sin un servidor X (a través
de la red).

%package devel
Summary: X11R6 static libraries, headers and programming man pages.
Summary(pt_BR): Bibliotecas estáticas X11R6, arquivos de inclusão e man pages de programação
Summary(es): Bibliotecas estáticas X11R6, archivos de inclusión y man pages de programación
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
%ifarch sparc
Obsoletes: X11R6.1-devel
%endif

%description devel
XFree86-devel includes the libraries, header files and documentation
you'll need to develop programs which run in X clients. XFree86 includes
the base Xlib library as well as the Xt and Xaw widget sets.

For guidance on programming with these libraries, O'Reilly & Associates
produces a series on X programming which you might find useful.

Install XFree86-devel if you are going to develop programs which
will run as X clients.

%description -l pt_BR devel
Bibliotecas, arquivos de inclusão e documentação para o
desenvolvimento de programas que rodam como clientes X. Inclui
a biblioteca base Xlib bem como os conjuntos de widgets Xt e
Xaw. Para maiores informações sobre a programação destas bibliotecas
a Conectiva recomenda a série de livros sobre programação X produzida
pela O'Reilly and Associates.

%description -l es devel
Bibliotecas, archivos de inclusión y documentación para el desarrollo
de programas que se ejecutan como clientes X. Incluye
la biblioteca base Xlib, bien como los conjuntos de widgets Xt
y Xaw. Para mayor información sobre la programación de estas
bibliotecas Conectiva recomienda la serie de libros sobre
programación X producida por la O'Reilly and Associates.

%package doc
Summary: Documentation on various X11 programming interfaces
Summary(pt_BR): Documentação de várias interfaces de programação X11
Summary(es): Documentação de várias interfaces de programação X11
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación

%description doc
XFree86-doc provides a great deal of extensive PostScript documentation
on the various X APIs, libraries, and other interfaces.  If you need
low level X documentation, you will find it here.  Topics include the
X protocol, the ICCCM window manager standard, ICE session management,
the font server API, etc.

%description -l pt_BR doc
Este pacote provê uma extensiva documentação em PostScript para
as várias APIs X, bibliotecas e outras interfaces. Se você precisa
de documentação para o X em baixo nível, você irá encontrá-la neste
pacote. Tópicos incluídos: protoloco X, gerenciador de janelas padrão
ICCM, gerenciamento de sessão ICE, API do servidor de fontes, etc.

%description -l es doc
Este pacote provê uma extensiva documentação em PostScript para
as várias APIs X, bibliotecas e outras interfaces. Se você precisa
de documentação para o X em baixo nível, você irá encontrá-la neste
pacote. Tópicos incluídos: protoloco X, gerenciador de janelas padrão
ICCM, gerenciamento de sessão ICE, API do servidor de fontes, etc.

%package S3
Summary: The XFree86 server for video cards based on the S3 chip.
Summary(pt_BR): Servidor XFree86 S3
Summary(es): Servidor XFree86 S3
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description S3
XFree86-S3 is the X server for video cards based on S3 chips,
including most #9 cards, many Diamond Stealth cards, Orchid Farenheits,
Mirco Crystal 8S, most STB cards, and some motherboards with built-in
graphics accelerators (such as the IBM ValuePoint line).  Note that if you
have an S3 ViRGE based video card, you'll need XFree86-S3V instead of
XFree86-S3.

If you are installing the X Window System and you have a video card based
on an S3 chip, you should install XFree86-S3.  You will also need to
install the XFree86 package, one or more XFree86 fonts packages, the
X11R6-contrib package, the Xconfigurator package and the XFree86-libs
package.  And, finally, if you are going to develop applications that
run as X clients, you will also need to install XFree86-devel.

%description -l pt_BR S3
Servidor X para placas baseadas em chips da S3, incluindo a maioria
das placas #9, Diamond Stealth, Orchid Farenheits, Mirco Crystal
8S, a maioria das placas STB e algumas placas mãe com aceleradores
gráficos embutidos (como a linha IBM ValuePoint).

%description -l es S3
Servidor X para tarjetas basadas en chips de la S3, incluyendo la
mayoría de las tarjetas #9, Diamond Stealth, Orchid Farenheits, Mirco
Crystal 8S, la mayoría de las tarjetas STB y algunas placas madre
con aceleradores gráficos empotrados (como la línea IBM ValuePoint).

%package I128
Summary: The XFree86 server for #9 Imagine 128 video cards.
Summary(pt_BR): Servidor XFree86 #9 Imagine 128
Summary(es): Servidor XFree86 #9 Imagine 128
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description I128
This is the X server for the #9 Imagine 128 and similar
video boards.

%description -l pt_BR I128
Servidor X para a placa #9 Imagine 128.

%description -l es I128
Servidor X para la tarjeta #9 Imagine 128.

%package S3V
Summary: The XFree86 server for video cards based on the S3 Virge chip.
Summary(pt_BR): Servidor XFree86 S3 Virge
Summary(es): Servidor XFree86 S3 Virge
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description S3V
XFree86-S3V is the X server for video cards based on the S3
ViRGE chipset.

If you are installing the X Window System and you have a video card based
on an S3 ViRGE chip, you should install XFree86-S3V.  You will also need
to install the XFree86 package, one or more of the XFree86 fonts packages,
the X11R6-contrib package, the Xconfigurator package and the XFree86-libs
package.  And, finally, if you are going to develop applications that
run as X clients, you will also need to install XFree86-devel.

%description -l pt_BR S3V
Servidor X para placas baseadas no chipset S3 Virge.

%description -l es S3V
Servidor X para tarjetas basadas en el chipset S3 Virge.

%package Mach64
Summary: The XFree86 server for Mach64 based video cards.
Summary(pt_BR): Servidor XFree86 Mach64
Summary(es): Servidor XFree86 Mach64
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description Mach64
XFree86-Mach64 is the server package for cards based on ATI's
Mach64 chip, such as the Graphics Xpression, GUP Turbo, and WinTurbo cards.
Note that this server is known to have problems with some Mach64 cards.
Check http://www.xfree86.org for current information on updating this
server.

If you are installing the X Window System and the video card in your system
is based on the Mach64 chip, you need to install XFree86-Mach64.  You will
also need to install the XFree86 package, one or more of the XFree86 fonts
packages, the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package.  And, finally, if you are going to be developing
applications that run as X clients, you will also need to install
XFree86-devel.

%description -l pt_BR Mach64
Servidor X para placas baseadas no chip ATI Mach64, como a Graphics
Xpression, GUP Turbo e WinTurbo.

%description -l es Mach64
Servidor X para tarjetas basadas en el chip ATI Mach64, como la
Graphics Xpression, GUP Turbo y WinTurbo.

%package Sun
Summary: X server for Suns with monochrome and 8-bit color SBUS framebuffers.
Summary(pt_BR): Servidor XFree86 Sun para framebuffers coloridos SBUS de 8 bits e monocromáticos
Summary(es): Servidor XFree86 Sun para framebuffers coloridos SBUS de 8 bits e monocromáticos.
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware
Obsoletes: X11R6.1-Sun

%description Sun
To run X Windows programs requires an X server for your specific hardware.
This package includes the X server for Sun computers with monochrome and
8-bit color SBUS framebuffers, like the CG3 and CGSIX.

%description -l pt_BR Sun
Para executar programas X Window é necessário um servidor X específico
para seu hardware. Este pacote inclui o servidor X para computadores Sun
com framebuffers SBUS coloridos de 8 bits e monocromáticos.

%description -l es Sun
Para ejecutar programas X Window hace falta un servidor X específico
para tu hardware. Este paquete incluye el servidor X para ordenadores
Sun con framebuffers SBUS coloridos de 8 bits y monocromáticos.

%package SunMono
Summary: X server for Sun computers with monochrome SBUS framebuffers only.
Summary(pt_BR): Servidor XFree86 Sun para framebuffers SBUS monocromáticos.
Summary(es): Servidor XFree86 Sun para framebuffers SBUS monocromáticos.
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware
Obsoletes: X11R6.1-SunMono

%description SunMono
The XFree86-SunMono package includes an X server for Sun computers with
monochrome SBUS framebuffers only.

If you're installing the X Window System on a Sun computer with
monochrome SBUS framebuffers only, you'll need to install the
XFree86-SunMono package.

%description -l pt_BR SunMono
Para executar programas X Window é necessário um servidor X específico para
seu hardware. Este pacote inclui o servidor X para computadores Sun com 
framebuffers SBUS monocromáticos.

%description -l es SunMono
Para ejecutar programas X Window hace falta un servidor X específico
para tu hardware. Este paquete incluye el servidor X para ordenadores
Sun con framebuffers SBUS monocromáticos.

%package Sun24
Summary: X server for Suns with all supported SBUS framebuffers.
Summary(pt_BR): Servidor XFree86 Sun para todos os framebuffers SBUS suportados.
Summary(es): Servidor XFree86 Sun para todos los framebuffers SBUS soportados.
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware
Obsoletes: X11R6.1-Sun24

%description Sun24
The XFree86-Sun24 package contains the X server for Sun computers with
all supported SBUS framebuffers.

If you are installing the X Window System on a Sun computer with all
supported framebuffers, you should install the XFree86-Sun24 package.

%description -l pt_BR Sun24
Para executar programas X Window é necessário um servidor X específico
para seu hardware. Este pacote inclui o servidor X para computadores Sun
com todos os framebuffers SBUS suportados.

%description -l es Sun24
Para ejecutar programas X Window hace falta un servidor X específico
para tu hardware. Este paquete incluye el servidor X para ordenadores
Sun con todos los framebuffers SBUS soportados.

%package Xvfb
Summary: A virtual framebuffer X Windows System server for XFree86.
Summary(pt_BR): Servidor XFree86 Xvfb
Summary(es): Servidor XFree86 Xvfb
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X Windows System server
that is capable of running on machines with no display hardware and no
physical input devices.  Xvfb emulates a dumb framebuffer using virtual
memory.  Xvfb doesn't open any devices, but behaves otherwise as an X
display.  Xvfb is normally used for testing servers.  Using Xvfb, the mfb
or cfb code for any depth can be exercised without using real hardware
that supports the desired depths.  Xvfb has also been used to test X
clients against unusual depths and screen configurations, to do batch
processing with Xvfb as a background rendering engine, to do load testing,
to help with porting an X server to a new platform, and to provide an
unobtrusive way of running applications which really don't need an X
server but insist on having one. 

If you need to test your X server or your X clients, you may want to
install Xvfb for that purpose.

%description -l pt_BR Xvfb
Servidor X para framebuffer virtual.

%description -l es Xvfb
Servidor X para framebuffer virtual.

%package Xnest
Summary: A nested XFree86 server.
Summary(pt_BR): Servidor XFree86 Xnest
Summary(es): Servidor XFree86 Xnest
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description Xnest
Xnest is an X Window System server which runs in an X window.
Xnest is a 'nested' window server, actually a client of the 
real X server, which manages windows and graphics requests 
for Xnest, while Xnest manages the windows and graphics 
requests for its own clients.

You will need to install Xnest if you require an X server which
will run as a client of your real X server (perhaps for
testing purposes).

%description -l pt_BR Xnest
Servidor X que roda em uma janela X.

%description -l es Xnest
Servidor X que se ejecuta en una ventana X.

%package 8514
Summary: The XFree86 server program for older IBM 8514 or compatible video cards.
Summary(pt_BR): Servidor XFree86 8514
Summary(es): Servidor XFree86 8514
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description 8514
If you are installing the X Window System and the video card in
your system is an older IBM 8514 or a compatible from a company
such as ATI, you should install XFree86-8514.

To install the X Window System, you will need to install the
XFree86 package, one or more of the XFree86 fonts packages,
the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package.

If you are going to develop applications that run as X clients,
you will also need to install the XFree86-devel package.

%description -l pt_BR 8514
Servidor X para placas IBM 8514 antigas e compatíveis de várias
companhias como a ATI.

%description -l es 8514
Servidor X para tarjetas IBM 8514 antiguas y compatibles de varias
compañías como la ATI.

%package AGX
Summary: The XFree86 server for AGX-based video cards.
Summary(pt_BR): Servidor XFree86 AGX
Summary(es): Servidor XFree86 AGX
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description AGX
This is the X server for AGX-based cards, such as the Boca
Vortex, Orchid Celsius, Spider Black Widow and Hercules
Graphite.

If you are installing the X Window System and the video card in
your system is an AGX, you'll need to install XFree86-AGX.
To install the X Window System, you will need to install the
XFree86 package, one or more of the XFree86 fonts packages,
the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package.

Finally, if you are going to develop applications that run as
X clients, you will also need to install the XFree86-devel 
package.

%description -l pt_BR AGX
Servidor X para as placas baseadas em AGX, como Boca Vortex, Orchid
Celsius, Spider Black Window e Hercules Graphite.

%description -l es AGX
Servidor X para las tarjetas basadas en AGX, como Boca Vortex,
Orchid Celsius, Spider Black Window y Hercules Graphite.

%package Mach32
Summary: The XFree86 server for Mach32 based video cards.
Summary(pt_BR): Servidor XFree86 Mach32
Summary(es): Servidor XFree86 Mach32
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description Mach32
XFree86-Mach32 is the X server package for video cards built
around ATI's Mach32 chip, including the ATI Graphics Ultra Pro and Ultra
Plus.

If you are installing the X Window System and the video card in your system
is based on the Mach32 chip, you need to install XFree86-Mach32.  You will
also need to install the XFree86 package, one or more of the XFree86 fonts
packages, the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package.  And, finally, if you are going to develop
applications that run as X clients, you will also need to install
XFree86-devel.

%description -l pt_BR Mach32
Servidor X para placas baseadas no chip ATI Mach32, incluindo a
ATI Graphics Ultra e Ultra Plus.

%description -l es Mach32
Servidor X para tarjetas basadas en el chip ATI Mach32, incluyendo
la ATI Graphics Ultra y Ultra Plus.

%package Mach8
Summary: The XFree86 server for Mach8 video cards.
Summary(pt_BR): Servidor XFree86 Mach8
Summary(es): Servidor XFree86 Mach8
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description Mach8
XFree86-Mach 8 is the X server for video cards built around
ATI's Mach8 chip, including the ATI 8514 Ultra and Graphics Ultra.

If you are installing the X Window System and the video card in your system
is based on the Mach8 chip, you need to install XFree86-Mach8.  You will
also need to install the XFree86 package, one or more of the XFree86 fonts
packages, the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package.  And, finally, if you are going to be developing
applications that run as X clients, you will also need to install
XFree86-devel.

%description -l pt_BR Mach8
Servidor X para placas baseadas no chip ATI Mach8, incluindo a ATI
8514 Ultra e Graphics Ultra.

%description -l es Mach8
Servidor X para tarjetas basadas en el chip ATI Mach8, incluyendo
la ATI 8514 Ultra y Graphics Ultra.

%package Mono
Summary: A generic XFree86 monochrome server for VGA cards.
Summary(pt_BR): Servidor XFree86 Mono
Summary(es): Servidor XFree86 Mono
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description Mono
XFree86-Mono is a generic monochrome (2 color) server for VGA cards.
XFree86-Mono will work for nearly all VGA compatible cards, but will
only support a monochrome display.

If you are installing the X Window System and your VGA card is not
currently supported, you should install and try either XFree86-Mono or
XFree86-VGA16, depending upon the capabilities of your display.  You
will also need to install the XFree86 package, one or more of the XFree86
fonts packages, the X11R6-contrib package, the Xconfigurator package and
the XFree86-libs package.  And, finally, if you are going to develop
applications that run as X clients, you will also need to install
XFree86-devel.

%description -l pt_BR Mono
Servidor X monocromático genérico para placas VGA, que funciona em
quase todas as placas estilo VGA com resoluções limitadas.

%description -l es Mono
Servidor X monocromático genérico para tarjetas VGA, que funciona
en casi todas las tarjetas estilo VGA con resoluciones limitadas.

%package P9000
Summary: The XFree86 server for P9000 cards.
Summary(pt_BR): Servidor XFree86 P9000
Summary(es): Servidor XFree86 P9000
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description P9000
XFree86-P9000 is the X server for video cards built around the
Weitek P9000 chip, such as most Diamond Viper cards and the Orchid P9000
card.  

If you are installing the X Window System and you have a Weitek P9000
based video card, you should install XFree86-P9000.  You will also need
to install the XFree86 package, one or more of the XFree86 fonts packages,
the X11R6-contrib package, the Xconfigurator package and the XFree86-libs
package.  And, finally, if you are going to develop applications that
run as X clients, you will also need to install XFree86-devel.

%description -l pt_BR P9000
Servidor X para placas baseadas em chips Weitek P9000 como a maioria
das placas Diamond Viper e a Orchid P9000.

%description -l es P9000
Servidor X para tarjetas basadas en chips Weitek P9000 como la
mayoría de las tarjetas Diamond Viper y la Orchid P9000.

%package SVGA
Summary: An XFree86 server for most simple framebuffer SVGA devices.
Summary(pt_BR): Servidor XFree86 SVGA
Summary(es): Servidor XFree86 SVGA
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description SVGA
X server for most simple framebuffer SVGA devices, including cards built
from ET4000 chips, Cirrus Logic chips, Chips and Technologies laptop chips,
Trident 8900 and 9000 chips, and Matrox chips. It works for Diamond Speedstar,
Orchid Kelvins, STB Nitros and Horizons, Genoa 8500VL, most Actix boards,
the Spider VLB Plus, etc. It also works for many other chips and cards, so try
this server if you are having problems.

%description -l pt_BR SVGA
Servidor X para a maioria dos dispositivos SVGA framebuffer simples,
incluindo placas baseadas nos chips ET4000, Cirrus Logic, Chips and
Technologies para laptops, Trident 8900 e 9000. Funciona em placas
Diamond Speedstar, Orchid Kelvins, STB Nitros e Horizons, Genoa
8500VL, maioria das Actix e na Spider VLB Plus. Também funciona em
muitas outros chips e placas, então tente este servidor se estiver
tendo problemas.

%description -l es SVGA
Servidor X para la mayoría de los dispositivos SVGA framebuffer
sencillos, incluyendo tarjetas basadas en los chips ET4000,
Cirrus Logic, Chips and Technologies para laptops, Trident 8900
y 9000. Funciona en tarjetas Diamond Speedstar, Orchid Kelvins,
STB Nitros y Horizons, Genoa 8500VL, mayoría de las Actix y en la
Spider VLB Plus. También funciona en muchos otros chips y tarjetas,
por esto, intente este servidor si tienes problemas.

%package VGA16
Summary: A generic XFree86 server for VGA16 boards.
Summary(pt_BR): Servidor XFree86 VGA16
Summary(es): Servidor XFree86 VGA16
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description VGA16
XFree86-VGA16 is a generic 16 color server for VGA boards.
XFree86-VGA16 will work on nearly all VGA style graphics boards, but will
only support a low resolution, 16 color display.

If you are installing the X Window System and your VGA video card is not
specifically supported by another X server package, you should install
either XFree86-Mono or XFree86-VGA16, depending upon the capabilities of
your display.  You will also need to install the XFree86 package, one or
more of the XFree86 fonts packages, the X11R6-contrib package, the
Xconfigurator package and the XFree86-libs package.  And, finally, if you
are going to be develop applications that run as X clients, you will also
need to install XFree86-devel.

%description -l pt_BR VGA16
Servidor X genérico para placas VGA de 16 cores. Funciona em quase
todas as placas gráficas VGA, mas somente em baixa resolução e com
poucas cores.

%description -l es VGA16
Servidor X genérico para tarjetas VGA de 16 colores. Funciona en casi
todas las tarjetas gráficas VGA, pero solamente en baja resolución
y con pocos colores.

%package W32
Summary: The XFree86 server for video cards based on ET4000/W32 chips.
Summary(pt_BR): Servidor XFree86 W32
Summary(es): Servidor XFree86 W32
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description W32
XFree86-W32 is the X server for cards built around ET4000/W32
chips, including the Genoa 8900 Phantom 32i, the Hercules Dynamite, the
LeadTek WinFast S200, the Sigma Concorde, the STB LightSpeed, the TechWorks
Thunderbolt, and the ViewTop PCI.

If you are installing the X Window System and your VGA video card is based
on the ET4000/W32 chipset, you should install XFree86-W32.  You will also
need to install the XFree86 package, one or more of the XFree86 fonts
packages, the X11R6-contrib package, the Xconfigurator package and the
XFree86-libs package.  And, finally, if you are going to develop
applications that run as X clients, you will also need to install
XFree86-devel.

%description -l pt_BR W32
Servidor X para placas baseadas nos chips ET4000/W32, incluindo as
placas Genoa 8900 Phantom 32i, Hercules Dynamite, LeadTek WinFast
S200, Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt e
ViewTop PCI.

%description -l es W32
Servidor X para tarjetas basadas en los chips ET4000/W32, incluyendo
las tarjetas Genoa 8900 Phantom 32i, Hercules Dynamite, LeadTek
WinFast S200, Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt
y ViewTop PCI.

%package 3DLabs 
Summary: XFree86 3DLabs server.
Summary(pt_BR): Servidor XFree86 3DLabs
Summary(es): Servidor XFree86 3DLabs
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description 3DLabs
X server for cards built around 3D Labs GLINT and 
Permedia chipsets, including GLINT 500TX with IBM RGB526
RAMDAC, GLINT MX with IBM RGB526 and IBM RGB640
RAMDAC, Permedia with IBM RGB526 RAMDAC and the 
Permedia 2 (classic, 2a, 2v).

%description -l pt_BR 3DLabs
Servidor X para placas feitas com os chipsets 3DLabs, tais como GLINT
500TX, GLINT MX, Permedia e Permedia 2.

%description -l es 3DLabs
Servidor X para tarjetas hechas con los chipsets 3DLabs, como GLINT
500TX, GLINT MX, Permedia y Permedia 2.

%package TGA
Summary: X server for systems with Digital TGA boards based on DC21040 chips.
Summary(pt_BR): Servidor XFree86 TGA 
Summary(es): Servidor XFree86 TGA 
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description TGA
The XFree86-TGA package contains an 8-bit X server for Digital TGA boards
based on the DC21040 chip.  These adapters are very popular in Alpha
workstations and are included with Alpha UDB (Multia) machines.

If you are installing the X Window System and your system uses a
Digital TGA board based on the DC21040 chip, you'll need to install
the XFree86-TGA package.

%description -l pt_BR TGA
Servidor X de 8 bits para placas Digital TGA baseadas nos chips DC21040.
Estas placas são muito populares em estações de trabalho Alpha e vem 
com máquinas Alpha UDB (Multia).

%description -l es TGA
Servidor X de 8 bits para tarjetas Digital TGA basadas en los
chips DC21040.  Estas tarjetas son muy populares en estaciones de
trabajo Alpha y vienen con máquinas Alpha UDB (Multia).

%package FBDev
Summary: The X server for the generic frame buffer device on some machines.
Summary(pt_BR): Servidor XFree68 FBDev
Summary(es): Servidor XFree68 FBDev
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware

%description FBDev
This is the X server for the generic frame buffer device used on
Amiga, Atari and Macintosh/m68k machines.

Support for Intel and Alpha architectures is included in the Linux
2.2 kernel, as well.

%description -l pt_BR FBDev
Servidor X para dispositivos frame buffer genéricos usados em máquinas
Amiga, Atari e Macintosh/m68k.

%description -l es FBDev
Servidor X para dispositivos frame buffer genéricos usados en
máquinas Amiga, Atari y Macintosh/m68k.

%package XF86Setup
Group: User Interface/X Hardware Support
Group(pt_BR): Interface do Usuário/Suporte X a Hardware
Group(es): Interfaz del Usuario/Soporte X a Hardware
Summary: A graphical user interface configuration tool for the X Window System.
Summary(pt_BR): Ferramenta gráfica de configuração para o XFree86
Summary(es): Herramienta gráfica de configuración para XFree86
%ifarch i386
Requires: XFree86-VGA16
%endif

%package xfs
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Summary: Font server for XFree86
Summary(pt_BR): Servidor de fontes para o XFree86 com suporte a TrueType
Summary(es): Servidor de fuentes para XFree86 con soporte a TrueType
Prereq: shadow-utils
Requires: initscripts >= 4.01

%description xfs
This is a font server for XFree86.  You can serve fonts to other X servers
remotely with this package, and the remote system will be able to use all
fonts installed on the font server, even if they are not installed on the
remote computer.

%description -l pt_BR xfs
Versão modificada do servidor de fontes xfs para X, com suporte
a fontes TrueType via FreeType. Com o servidor de fontes, você
pode fornecer fontes truetype para outros servidores X que não
tenham este suporte.

%description -l es xfs
Versión modificada del servidor de fuentes xfs para X, con soporte a
fuentes TrueType vía FreeType. Con el servidor de fuentes, puedes
ofrecer fuentes truetype para otros servidores X que no tengan
este soporte.

%description XF86Setup
XF86Setup is a graphical user interface configuration tool for setting
up and configuring XFree86 servers.  XF86Setup can configure video
settings, keyboard layouts, mouse types, etc.  XF86Setup can't be used
with non-VGA compatible video cards, with fixed-frequency monitors, or
with OS/2.

Install XF86Setup if you have used it before and prefer to keep using
it to configure your X server.  If you do not have a preference for
XF86Setup, you should instead install and use Xconfigurator, Red Hat's
graphical user interface configuration tool for the X Window System.

%description -l pt_BR XF86Setup
O XF86Setup é uma ferramenta gráfica de configuração para a família de
servidores XFree86. Permite a configuração do vídeo, layouts de
teclados, tipo de mouse e outras opções. É um pouco lento e necessita
do servidor VGA 16 genérico.

%description -l es XF86Setup
XF86Setup es una herramienta gráfica de configuración para la
familia de servidores XFree86. Permite la configuración del vídeo,
visuales de teclados, tipo de ratón y otras opciones. Es un poco
lento y necesita del servidor VGA 16 genérico.

%prep
# -a 106 only for some TrueType docs
%setup -q -c -a 1 -a 2 -a 106

# Clean up to save a *lot* of disk space
find . -name "*.orig" -print | xargs rm -f
find . -size 0 -print | xargs rm -f

%patch0 -p1 -b .rh
%patch1 -p1 -b .rhxdm
%patch2 -p1 -b .fsstnd
%patch3 -p1 -b .nopam
%patch4 -p1 -b .pamconsole

# the following upgrades the tree to 3.3.3.1
patch -d xc -p1 -b -z .3.3.3.1 -s < %PATCH100

# and the following upgrades the tree to 3.3.4 beta :|
#bzip2 -cd %PATCH190 | patch -d xc -p1 -b -z .3.3.3.1a -s
#bzip2 -cd %PATCH191 | patch -d xc -p1 -b -z .3.3.3.1b -s
#bzip2 -cd %PATCH192 | patch -d xc -p1 -b -z .3.3.3.1c -s
#bzip2 -cd %PATCH193 | patch -d xc -p1 -b -z .3.3.3.1d -s
#bzip2 -cd %PATCH194 | patch -d xc -p1 -b -z .3.3.3.1e -s
#bzip2 -cd %PATCH195 | patch -d xc -p1 -b -z .3.3.3.1f -s
#bzip2 -cd %PATCH196 | patch -d xc -p1 -b -z .3.3.3.1Z -s

# 3.3.3.1Z
#%patch197 -p0 -b .s3_aurora
#%patch198 -p0 -b .atiprobe
#%patch199 -p0 -b .manpages

# the following patch is in CVS diff format, needs POSIXLY_CORRECT env var.
#POSIXLY_CORRECT=1 patch -p1 -b -z .alpha-sockets -s < %PATCH5

# sparc patches from ultrapenguin
%ifarch sparc
%patch10 -p1 -b .sparc
%patch11 -p1 -b .ffb
%endif

# enable FBDev device on alpha / intel
%patch12 -p1 -b .fbdev

# fix xinput problems with threads / GTK+ -- Owen Taylor's fix
%patch13 -p1 -b .xinput

# more sun patches from ultrapenguin
%ifarch sparc
%patch14 -p1 -b .suncards
%patch15 -p1 -b .sparc2
%patch16 -p1 -b .creator2
%patch17 -p1 -b .newcreator
%patch18 -p1 -b .sparc3
%endif
# the following was causing problems with RagePRO based ATI
# chipsets, but this has been fixed
%ifarch sparc
%patch19 -p1 -b .mach64
%patch20 -p1 -b .creator4
%endif

%patch42 -p1 -b .jay

#%patch51 -p1 -b .czskkbd
#%patch52 -p1 -b .is_keyboard

# use glibc 2.1 routines for utmp, doesn't require xterm to be setuid
%patch53 -p1 -b .nosuidxterm
%patch54 -p1 -b .joy
%patch55 -p1 -b .arm
%patch56 -p1 -b .xfsft
# ru_SU is redundant now in 3.3.4
%patch57 -p1 -b .ru_SU
%patch58 -p1 -b .startx_xauth
%patch59 -p1 -b .xfsredhat
%patch60 -p1 -b .mgafix

# the following patch is incomplete..broken..and thus commented out.
#%patch61 -p1 -b .alphadga

# Already OK in 3.3.4
# work by VMWare, inc. to provide hardware accelerated DGA "XFree86 3.4"
%patch62 -p0 -b .dga1.1

# Patch from Ian Reid Remmler <ian@marmoset.resnet.tamu.edu> to fix mouse
# movement with Kensington ExpertMouse / ThinkingMouse
# The code has changed. BTW, I would like to have one mouse that think :)
# not applied in 3.3.4
%patch63 -p1 -b .thinkingmouse

# fix keymap error for dvorak keyboards
# already OK in 3.3.4
%patch64 -p0 -b .dvorak

%ifarch sparc
%patch65 -p1 -b .ffbcrash
%endif
%patch66 -p1 -b .G200dga
%patch67 -p1 -b .ru_sparc
%patch68 -p1 -b .xinitrace
%patch69 -p1 -b .fixiso8859-2

# already OK in 3.3.4
# Fix dainbramage where the X server chmods whatever .X11-unix points to
%patch75 -p1 -b .dainbramage

# already OK in 3.3.4
#%patch101 -p0 -b .banshee
#%patch102 -p0 -b .rush
%patch103 -p1 -b .nvidia

%patch110 -p0 -b .dead-keys
%patch111 -p0 -b .xkbbr
%patch112 -p0 -b .trident9x5
%patch113 -p0 -b .libtermcap
%patch777 -p0 -b .cards
%patch778 -p0 -b .cards-SiS

%build
%ifarch alpha
make World -C xc CDEBUGFLAGS="$RPM_OPT_FLAGS -Wa,-m21164a"
%else
make World -C xc CDEBUGFLAGS="$RPM_OPT_FLAGS"
%endif

# silly, but it works around an apparent egcs bug that breaks netscape
# REMOVE THIS WHEN FIXED!!!
%ifarch i386
rm xc/lib/{X11,X11/unshared}/{imLcFlt.o,FilterEv.o}
rm xc/lib/{Xt,Xt/unshared}/{Event.o,Callback.o,Destroy.o,NextEvent.o}
cd xc/lib
make CDEBUGFLAGS=""
cd ../..
%endif

echo PACKAGING DOCUMENTATION
# get rid of old formatted docs
find xc/doc/hardcopy -name \*.PS.Z | xargs gzip -d
find xc/doc/hardcopy -name \*.PS | xargs gzip

groff -Tascii -ms xc/doc/misc/RELNOTES.ms > xc/doc/hardcopy/RELNOTES.txt
rm xc/doc/hardcopy/BDF/*
groff -Tascii -ms xc/doc/specs/BDF/bdf.ms > xc/doc/hardcopy/BDF/bdf.txt
rm xc/doc/hardcopy/CTEXT/*
groff -Tascii -ms xc/doc/specs/CTEXT/ctext.tbl.ms > xc/doc/hardcopy/CTEXT/ctext.tbl.txt
mkdir -p xc/doc/hardcopy/DPMS
groff -Tascii -ms xc/doc/specs/DPMS/DPMS.ms > xc/doc/hardcopy/DPMS/DPMS.txt
groff -Tascii -ms xc/doc/specs/DPMS/DPMSLib.ms > xc/doc/hardcopy/DPMS/DPMSLib.txt
rm xc/doc/hardcopy/FSProtocol/*
groff -Tascii -ms xc/doc/specs/FSProtocol/protocol.ms > xc/doc/hardcopy/FSProtocol/protocol.txt
rm xc/doc/hardcopy/ICCCM/*
groff -Tascii -ms xc/doc/specs/ICCCM/icccm.ms > xc/doc/hardcopy/ICCCM/icccm.txt
rm xc/doc/hardcopy/ICE/*
groff -Tascii -ms xc/doc/specs/ICE/ICElib.ms > xc/doc/hardcopy/ICE/ICElib.txt
groff -Tascii -ms xc/doc/specs/ICE/ice.ms > xc/doc/hardcopy/ICE/ice.txt
cp xc/doc/specs/PM/PM_spec xc/doc/hardcopy/ICE
rm xc/doc/hardcopy/SM/*
groff -Tascii -ms xc/doc/specs/SM/SMlib.ms > xc/doc/hardcopy/SM/SMlib.txt
rm xc/doc/hardcopy/XDMCP/*
groff -Tascii -ms xc/doc/specs/XDMCP/xdmcp.ms > xc/doc/hardcopy/XDMCP/xdmcp.txt
rm xc/doc/hardcopy/XIM/*
groff -Tascii -ms xc/doc/specs/XIM/xim.ms > xc/doc/hardcopy/XIM/xim.txt
rm xc/doc/hardcopy/XLFD/*
groff -Tascii -ms xc/doc/specs/XLFD/xlfd.tbl.ms > xc/doc/hardcopy/XLFD/xlfd.tbl.txt

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/pam.d
install -m 644 ${RPM_SOURCE_DIR}/xserver.pamd $RPM_BUILD_ROOT/etc/pam.d/xserver
install -m 644 ${RPM_SOURCE_DIR}/xdm.pamd $RPM_BUILD_ROOT/etc/pam.d/xdm
mkdir -p $RPM_BUILD_ROOT/etc/security/console.apps
touch $RPM_BUILD_ROOT/etc/security/console.apps/xserver

mkdir -p $RPM_BUILD_ROOT/usr/include
rm -f $RPM_BUILD_ROOT/usr/include/X11

make DESTDIR=$RPM_BUILD_ROOT install install.man -C xc

# we don't want the libz.a from XFree86 -- it's broken
rm -f $RPM_BUILD_ROOT/usr/X11R6/lib/libz.a

# setup the default X server
rm -f $RPM_BUILD_ROOT/usr/X11R6/bin/X
ln -s Xwrapper $RPM_BUILD_ROOT/usr/X11R6/bin/X

# don't make SuperProbe setuid
# don't make the servers setuid
(	cd $RPM_BUILD_ROOT/usr/X11R6/bin
	chmod 755 SuperProbe XF86_* Xsun* XF68_*
)

# we now provide a backwards compatible link for color-xterm/nxterm
{	
	pushd $RPM_BUILD_ROOT/usr/X11R6/bin
	ln -f xterm nxterm
	popd
}

# Move config config stuff to /etc/X11
mkdir -p $RPM_BUILD_ROOT/etc/X11
ln -sf ../../../../etc/X11/XF86Config $RPM_BUILD_ROOT/usr/X11R6/lib/X11/XF86Config

for i in xdm twm fs xsm; do
    rm -rf $RPM_BUILD_ROOT/etc/X11/$i
    cp -ar $RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i $RPM_BUILD_ROOT/etc/X11
    rm -rf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i
    ln -sf ../../../../etc/X11/$i $RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i
done

# explicitly create X authdir
mkdir -p $RPM_BUILD_ROOT/etc/X11/xdm/authdir
chmod 0700 $RPM_BUILD_ROOT/etc/X11/xdm/authdir

# xkb 'compiled' files need to be in /var/lib/xkb, so
# /usr is NFS / read-only mountable
mkdir -p $RPM_BUILD_ROOT/var/lib/xkb
cp -a $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xkb/compiled/* \
	$RPM_BUILD_ROOT/var/lib/xkb
rm -rf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xkb/compiled
ln -sf ../../../../../var/lib/xkb \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/xkb/compiled

# install replacement Xsession file for xdm
install -m 755 $RPM_SOURCE_DIR/Xsession.redhat \
	$RPM_BUILD_ROOT/etc/X11/xdm/Xsession

# some docs from TrueType
mkdir $RPM_BUILD_ROOT/usr/X11R6/lib/X11/doc/TrueType
install -m 644 xfsft-1.0.3/{README,CHANGES,USAGE,LICENSE} \
		$RPM_BUILD_ROOT/usr/X11R6/lib/X11/doc/TrueType/

# the nice /usr/doc/ link!
mkdir -p $RPM_BUILD_ROOT/usr/doc/
ln -sf /usr/X11R6/lib/X11/doc/ \
      $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}-%{release}

# install conectiva Xsession and Xsetup over the above...
install -m755 $RPM_SOURCE_DIR/XFree86-Xsession.conectiva \
              $RPM_BUILD_ROOT/etc/X11/xdm/Xsession
install -m755 $RPM_SOURCE_DIR/XFree86-Xsetup_0.conectiva \
              $RPM_BUILD_ROOT/etc/X11/xdm/Xsetup_0

# we install our own config file for the xfs package
install -m 644 $RPM_SOURCE_DIR/xfs.config \
	$RPM_BUILD_ROOT/etc/X11/fs/config
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 $RPM_SOURCE_DIR/xfs.init \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/xfs

# install service for xdm
#install -m 755 $RPM_SOURCE_DIR/xdm.init \
#	$RPM_BUILD_ROOT/etc/rc.d/init.d/xdm

# we get xinit from a separate package
rm -rf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xinit
ln -sf ../../../../etc/X11/xinit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xinit

# Fix up symlinks
mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/man
mkdir -p $RPM_BUILD_ROOT/usr/include $RPM_BUILD_ROOT/usr/lib
ln -sf ../X11R6/bin $RPM_BUILD_ROOT/usr/bin/X11
ln -sf ../X11R6/man $RPM_BUILD_ROOT/usr/man/X11
ln -sf ../X11R6/include/X11 $RPM_BUILD_ROOT/usr/include/X11
ln -sf ../X11R6/lib/X11 $RPM_BUILD_ROOT/usr/lib/X11

(set +x; strip $RPM_BUILD_ROOT/usr/X11R6/bin/*)

for n in libX11.so.6.1 libICE.so.6.3 libSM.so.6.0 libXext.so.6.3 libXt.so.6.0 \
	 libXmu.so.6.0 libXaw.so.6.1 libXIE.so.6.0 libXi.so.6.0 \
	 libXtst.so.6.1; do
	ln -sf $n $RPM_BUILD_ROOT/usr/X11R6/lib/`echo $n | sed "s/\.so.*/\.so/"`
done

# this gets the wrong permissions by default -- I don't know or care why
chmod 755 $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xkb/geometry/sgi

# this certainly doesn't need to be setuid
chmod 755 $RPM_BUILD_ROOT/usr/X11R6/bin/dga


%ifarch i386 sparc m68k
  ln -sf libPEX5.so.6.0 $RPM_BUILD_ROOT/usr/X11R6/lib/libPEX5.so.6
%endif

# conectiva
install -m 444 $RPM_SOURCE_DIR/XTerm \
               $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/XTerm
gzip -9 $RPM_BUILD_ROOT/usr/X11R6/man/man*/*.[0-9]x

#%post
#/sbin/chkconfig --add xdm







mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/XFree86-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%pre
# here, we put things that we have moved around (like directories)
# that need to be cleaned up prior to the RPM's installation.  
# Ugly. Necessary.
if [ ! -L /usr/X11R6/lib/X11/xkb/compiled ]; then
  if [ -d /usr/X11R6/lib/X11/xkb/compiled ]; then
    mkdir -p /var/lib/xkb 2>/dev/null
    mv -f /usr/X11R6/lib/X11/xkb/compiled/* /var/lib/xkb /var/lib/xkb 2>/dev/null || :
    rmdir /usr/X11R6/lib/X11/xkb/compiled 2> /dev/null
    ln -sf ../../../../../var/lib/xkb /usr/X11R6/lib/X11/xkb/compiled 2>/dev/null || :
  fi
fi

#%postun
#if [ $1 = 0 ]; then
#    /sbin/chkconfig --del xdm
#fi

%post libs
grep "^/usr/X11R6/lib$" /etc/ld.so.conf >/dev/null 2>&1
[ $? -ne 0 ] && echo "/usr/X11R6/lib" >> /etc/ld.so.conf
/sbin/ldconfig

%postun libs
if [ "$1" = "0" ]; then
        grep -v "/usr/X11R6/lib" /etc/ld.so.conf > /etc/ld.so.conf.new
	mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi
/sbin/ldconfig

%verifyscript libs
echo -n "Looking for /usr/X11R6/lib in /etc/ld.so.conf... "
if ! grep "^/usr/X11R6/lib$" /etc/ld.so.conf > /dev/null; then
    echo "missing"
    echo "/usr/X11R6/lib missing from /etc/ld.so.conf" >&2
else
    echo "found"
fi

%post 75dpi-fonts
/usr/sbin/chkfontpath -q -a /usr/X11R6/lib/X11/fonts/75dpi

%postun 75dpi-fonts
if [ "$1" = "0" ]; then
	/usr/sbin/chkfontpath -q -r /usr/X11R6/lib/X11/fonts/75dpi
fi

%post 100dpi-fonts
/usr/sbin/chkfontpath -q -a /usr/X11R6/lib/X11/fonts/100dpi

%postun 100dpi-fonts
if [ "$1" = "0" ]; then
	/usr/sbin/chkfontpath -q -r /usr/X11R6/lib/X11/fonts/100dpi
fi

%post cyrillic-fonts
/usr/sbin/chkfontpath -q -a /usr/X11R6/lib/X11/fonts/cyrillic

%postun cyrillic-fonts
if [ "$1" = "0" ]; then
	/usr/sbin/chkfontpath -q -r /usr/X11R6/lib/X11/fonts/cyrillic
fi

%pre xfs
/usr/sbin/useradd -c "X Font Server" \
	-s /bin/false -r -d /etc/X11/fs xfs 2>/dev/null || :

%post xfs
/sbin/chkconfig --add xfs

%preun xfs
if [ $1 = 0 ]; then
    /sbin/chkconfig --del xfs
    /usr/sbin/userdel xfs 2>/dev/null || :
    /usr/sbin/groupdel xfs 2>/dev/null || :
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config %doc /usr/X11R6/lib/X11/XF86Config.eg
%docdir /usr/X11R6/lib/X11/doc
/usr/doc/%{name}-%{version}-%{release}

%ifarch i386 alpha sparc
%doc /usr/X11R6/lib/X11/Cards
%endif

%dir /usr/X11R6
%dir /usr/X11R6/lib
%dir /usr/X11R6/lib/X11
%dir /usr/X11R6/lib/X11/rstart
%dir /usr/X11R6/lib/X11/rstart/commands
%dir /usr/X11R6/lib/X11/rstart/commands/x11r6
%dir /usr/X11R6/lib/X11/rstart/contexts
%dir /usr/X11R6/lib/X11/etc
%dir /usr/X11R6/lib/X11/fonts
%dir /usr/X11R6/lib/X11/xserver
%ifarch i386 alpha m68k armv4l
/usr/X11R6/lib/modules
%endif

%dir /usr/X11R6/bin

%dir /etc/X11/twm
%dir /etc/X11/xdm
%dir %attr(0700,root,root) /etc/X11/xdm/authdir
%dir /etc/X11/xsm

#%config /etc/rc.d/init.d/xdm
%config /etc/pam.d/xserver
%config /etc/pam.d/xdm
%config(missingok) /etc/security/console.apps/xserver
%config /etc/X11/twm/system.twmrc
%config /etc/X11/xsm/system.xsm
%config /etc/X11/xdm/xdm-config
%config /etc/X11/xdm/chooser
%config /etc/X11/xdm/Xsetup_0
%config /etc/X11/xdm/Xsession
%config /etc/X11/xdm/Xservers
%config /etc/X11/xdm/Xresources
%config /etc/X11/xdm/Xaccess
%config /etc/X11/xdm/TakeConsole
%config /etc/X11/xdm/GiveConsole

/usr/X11R6/lib/X11/XErrorDB
/usr/X11R6/lib/X11/XKeysymDB
/usr/X11R6/lib/X11/locale
/usr/X11R6/lib/X11/lbxproxy
/usr/X11R6/lib/X11/proxymngr
%config /usr/X11R6/lib/X11/app-defaults/*

/usr/X11R6/lib/X11/xkb
/var/lib/xkb
/usr/X11R6/lib/X11/xinit
/usr/X11R6/lib/X11/xdm
/usr/X11R6/lib/X11/twm
/usr/X11R6/lib/X11/xsm

/usr/X11R6/lib/X11/xserver/SecurityPolicy
/usr/X11R6/lib/X11/XF86Config
/usr/X11R6/lib/X11/rstart/rstartd.real
%config /usr/X11R6/lib/X11/rstart/config
/usr/X11R6/lib/X11/rstart/commands/x11r6/@List
/usr/X11R6/lib/X11/rstart/commands/x11r6/LoadMonitor
/usr/X11R6/lib/X11/rstart/commands/x11r6/Terminal
/usr/X11R6/lib/X11/rstart/commands/@List
/usr/X11R6/lib/X11/rstart/commands/ListContexts
/usr/X11R6/lib/X11/rstart/commands/ListGenericCommands
/usr/X11R6/lib/X11/rstart/contexts/@List
/usr/X11R6/lib/X11/rstart/contexts/default
/usr/X11R6/lib/X11/rstart/contexts/x11r6
/usr/X11R6/lib/X11/x11perfcomp
/usr/X11R6/lib/X11/doc
/usr/X11R6/lib/X11/etc/sun.termcap
/usr/X11R6/lib/X11/etc/sun.terminfo
/usr/X11R6/lib/X11/etc/xterm.termcap
/usr/X11R6/lib/X11/etc/xterm.terminfo

%ifarch i386 alpha sparc
/usr/X11R6/lib/X11/etc/et4000clock.c
%endif

/usr/X11R6/lib/X11/etc/xmodmap.std
/usr/X11R6/lib/X11/etc/postinst.sh
/usr/X11R6/lib/X11/etc/preinst.sh
%attr(4711,root,root)		/usr/X11R6/bin/Xwrapper
/usr/X11R6/bin/X
/usr/X11R6/bin/Xprt
/usr/X11R6/bin/lbxproxy
/usr/X11R6/bin/proxymngr
/usr/X11R6/bin/rstartd
/usr/X11R6/bin/xfindproxy
/usr/X11R6/bin/xfwp
/usr/X11R6/bin/xrx
/usr/X11R6/bin/lndir
/usr/X11R6/bin/mkdirhier
/usr/X11R6/bin/gccmakedep
/usr/X11R6/bin/mergelib
/usr/X11R6/bin/makeg
/usr/X11R6/bin/appres
/usr/X11R6/bin/bdftopcf
/usr/X11R6/bin/beforelight
/usr/X11R6/bin/bitmap
/usr/X11R6/bin/bmtoa
/usr/X11R6/bin/atobm
/usr/X11R6/bin/editres
/usr/X11R6/bin/iceauth
/usr/X11R6/bin/mkfontdir
/usr/X11R6/bin/showrgb
#/usr/X11R6/bin/ttmkfdir
/usr/X11R6/bin/rstart
/usr/X11R6/bin/smproxy
/usr/X11R6/bin/twm
/usr/X11R6/bin/x11perf
/usr/X11R6/bin/x11perfcomp
/usr/X11R6/bin/Xmark
/usr/X11R6/bin/xauth
/usr/X11R6/bin/xclipboard
/usr/X11R6/bin/xcutsel
/usr/X11R6/bin/xclock
/usr/X11R6/bin/xcmsdb
/usr/X11R6/bin/xconsole
/usr/X11R6/bin/xdm
/usr/X11R6/bin/sessreg
/usr/X11R6/bin/xdpyinfo
%attr(0755,root,root)		/usr/X11R6/bin/dga
/usr/X11R6/bin/xfd
/usr/X11R6/bin/xhost
/usr/X11R6/bin/xieperf
/usr/X11R6/bin/xinit
%config /usr/X11R6/bin/startx
/usr/X11R6/bin/setxkbmap
/usr/X11R6/bin/xkbcomp
/usr/X11R6/bin/xkbevd
/usr/X11R6/bin/xkbprint
/usr/X11R6/bin/xkbvleds
/usr/X11R6/bin/xkbwatch
/usr/X11R6/bin/xkbbell
/usr/X11R6/bin/xkill
/usr/X11R6/bin/xlogo
/usr/X11R6/bin/xlsatoms
/usr/X11R6/bin/xlsclients
/usr/X11R6/bin/xlsfonts
/usr/X11R6/bin/xmag
/usr/X11R6/bin/xmh
/usr/X11R6/bin/xmodmap
/usr/X11R6/bin/xprop
/usr/X11R6/bin/xrdb
/usr/X11R6/bin/xset
/usr/X11R6/bin/xrefresh
/usr/X11R6/bin/xsetmode
/usr/X11R6/bin/xsetpointer
/usr/X11R6/bin/xsetroot
/usr/X11R6/bin/xsm
/usr/X11R6/bin/xstdcmap
/usr/X11R6/bin/xterm
/usr/X11R6/bin/nxterm
/usr/X11R6/bin/resize
/usr/X11R6/bin/xvidtune
/usr/X11R6/bin/xwd
/usr/X11R6/bin/xwininfo
/usr/X11R6/bin/xwud
/usr/X11R6/bin/xon

%ifarch i386 alpha sparc
/usr/X11R6/bin/reconfig
/usr/X11R6/bin/xf86config
/usr/X11R6/bin/scanpci
/usr/X11R6/bin/SuperProbe
%endif

/usr/X11R6/include/X11/bitmaps

%dir /usr/X11R6/man
/usr/X11R6/man/man1/lbxproxy.1x.gz
/usr/X11R6/man/man1/proxymngr.1x.gz
/usr/X11R6/man/man1/xfindproxy.1x.gz
/usr/X11R6/man/man1/xfwp.1x.gz
/usr/X11R6/man/man1/xrx.1x.gz
/usr/X11R6/man/man1/lndir.1x.gz
/usr/X11R6/man/man1/makestrs.1x.gz
/usr/X11R6/man/man1/makeg.1x.gz
/usr/X11R6/man/man1/mkdirhier.1x.gz
/usr/X11R6/man/man1/appres.1x.gz
/usr/X11R6/man/man1/bdftopcf.1x.gz
/usr/X11R6/man/man1/beforelight.1x.gz
/usr/X11R6/man/man1/bitmap.1x.gz
/usr/X11R6/man/man1/bmtoa.1x.gz
/usr/X11R6/man/man1/atobm.1x.gz
/usr/X11R6/man/man1/editres.1x.gz
/usr/X11R6/man/man1/iceauth.1x.gz
/usr/X11R6/man/man1/mkfontdir.1x.gz
/usr/X11R6/man/man1/showrgb.1x.gz
/usr/X11R6/man/man1/rstart.1x.gz
/usr/X11R6/man/man1/rstartd.1x.gz
/usr/X11R6/man/man1/smproxy.1x.gz
/usr/X11R6/man/man1/twm.1x.gz
/usr/X11R6/man/man1/x11perf.1x.gz
/usr/X11R6/man/man1/x11perfcomp.1x.gz
/usr/X11R6/man/man1/xauth.1x.gz
/usr/X11R6/man/man1/xclipboard.1x.gz
/usr/X11R6/man/man1/xcutsel.1x.gz
/usr/X11R6/man/man1/xclock.1x.gz
/usr/X11R6/man/man1/xcmsdb.1x.gz
/usr/X11R6/man/man1/xconsole.1x.gz
/usr/X11R6/man/man1/xdm.1x.gz
/usr/X11R6/man/man1/sessreg.1x.gz
/usr/X11R6/man/man1/xdpyinfo.1x.gz
/usr/X11R6/man/man1/dga.1x.gz
/usr/X11R6/man/man1/xfd.1x.gz
/usr/X11R6/man/man1/xhost.1x.gz
/usr/X11R6/man/man1/xieperf.1x.gz
/usr/X11R6/man/man1/xinit.1x.gz
/usr/X11R6/man/man1/startx.1x.gz
/usr/X11R6/man/man1/setxkbmap.1x.gz
/usr/X11R6/man/man1/xkbcomp.1x.gz
/usr/X11R6/man/man1/xkbevd.1x.gz
/usr/X11R6/man/man1/xkbprint.1x.gz
/usr/X11R6/man/man1/xkill.1x.gz
/usr/X11R6/man/man1/xlogo.1x.gz
/usr/X11R6/man/man1/xlsatoms.1x.gz
/usr/X11R6/man/man1/xlsclients.1x.gz
/usr/X11R6/man/man1/xlsfonts.1x.gz
/usr/X11R6/man/man1/xmag.1x.gz
/usr/X11R6/man/man1/xmh.1x.gz
/usr/X11R6/man/man1/xmodmap.1x.gz
/usr/X11R6/man/man1/xprop.1x.gz
/usr/X11R6/man/man1/xrdb.1x.gz
/usr/X11R6/man/man1/xrefresh.1x.gz
/usr/X11R6/man/man1/xset.1x.gz
/usr/X11R6/man/man1/xsetmode.1x.gz
/usr/X11R6/man/man1/xsetpointer.1x.gz
/usr/X11R6/man/man1/xsetroot.1x.gz
/usr/X11R6/man/man1/xsm.1x.gz
/usr/X11R6/man/man1/xstdcmap.1x.gz
/usr/X11R6/man/man1/xterm.1x.gz
/usr/X11R6/man/man1/resize.1x.gz
/usr/X11R6/man/man1/xvidtune.1x.gz
/usr/X11R6/man/man1/xwd.1x.gz
/usr/X11R6/man/man1/xwininfo.1x.gz
/usr/X11R6/man/man1/xwud.1x.gz
/usr/X11R6/man/man1/xon.1x.gz
/usr/X11R6/man/man1/Xserver.1x.gz
/usr/X11R6/man/man1/XFree86.1x.gz
/usr/X11R6/man/man5/XF86Config.5x.gz

%ifarch i386 alpha sparc
/usr/X11R6/man/man1/reconfig.1x.gz
/usr/X11R6/man/man1/xf86config.1x.gz
/usr/X11R6/man/man1/SuperProbe.1x.gz
%endif

/usr/X11R6/lib/X11/fonts/Speedo
/usr/X11R6/lib/X11/fonts/Type1
/usr/X11R6/lib/X11/fonts/misc

%config /usr/X11R6/lib/X11/rgb.txt

%ifarch i386 sparc m68k armv4l
/usr/X11R6/lib/X11/fonts/PEX
%endif
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%files libs
%defattr(-,root,root,-)
/usr/X11R6/lib/*.so.6*

%files devel
%defattr(-,root,root,-)
/usr/X11R6/include
/usr/include/X11
/usr/X11R6/man/man3

/usr/X11R6/lib/X11/config
/usr/X11R6/bin/imake
/usr/X11R6/bin/makedepend
/usr/X11R6/bin/xmkmf

/usr/X11R6/man/man1/imake.1x.gz
/usr/X11R6/man/man1/makedepend.1x.gz
/usr/X11R6/man/man1/xmkmf.1x.gz

/usr/X11R6/lib/*.a

/usr/X11R6/lib/*.so

%files doc
%defattr(-,root,root,-)
%doc xc/doc/hardcopy/*

%files Xvfb
%defattr(-,root,root,-)
/usr/X11R6/bin/Xvfb
/usr/X11R6/man/man1/Xvfb.1x.gz

%files Xnest
%defattr(-,root,root,-)
/usr/X11R6/bin/Xnest
/usr/X11R6/man/man1/Xnest.1x.gz

%ifarch i386 alpha
%files SVGA
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_SVGA
/usr/X11R6/man/man1/XF86_SVGA.1x.gz
%endif

%ifarch i386 sparc
%files VGA16
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_VGA16
/usr/X11R6/man/man1/XF86_VGA16.1x.gz
%endif

%ifarch i386
%files W32
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_W32
/usr/X11R6/man/man1/XF86_W32.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386 alpha
%files Mono
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_Mono
/usr/X11R6/man/man1/XF86_Mono.1x.gz
%endif

%ifarch i386 alpha
%files S3
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_S3
/usr/X11R6/man/man1/XF86_S3.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386 alpha
%files S3V
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_S3V
/usr/X11R6/man/man1/XF86_S3.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386
%files 8514
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_8514
/usr/X11R6/man/man1/XF86_8514.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386
%files Mach8
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_Mach8
/usr/X11R6/man/man1/XF86_Mach8.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386
%files Mach32
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_Mach32
/usr/X11R6/man/man1/XF86_Mach32.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386 alpha sparc
%files Mach64
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_Mach64
/usr/X11R6/man/man1/XF86_Mach64.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386 alpha
%files P9000
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_P9000
/usr/X11R6/man/man1/XF86_P9000.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386
%files AGX
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_AGX
/usr/X11R6/man/man1/XF86_AGX.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386
%files I128
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_I128
/usr/X11R6/man/man1/XF86_I128.1x.gz
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch i386 alpha
%files 3DLabs
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_3DLabs
/usr/X11R6/man/man1/XF86_Accel.1x.gz
%endif

%ifarch alpha
%files TGA
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_TGA
%endif

%ifarch m68k armv4l
%files FBDev
%defattr(-,root,root,-)
/usr/X11R6/bin/XF68_FBDev
/usr/X11R6/man/man1/XF68_FBDev.1x.gz
%endif

%ifarch i386 alpha
%files FBDev
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86_FBDev
%endif

%ifarch sparc
%files Sun
%defattr(-,root,root,-)
/usr/X11R6/bin/Xsun
%endif

%ifarch sparc
%files SunMono
%defattr(-,root,root,-)
/usr/X11R6/bin/XsunMono
%endif

%ifarch sparc
%files Sun24
%defattr(-,root,root,-)
/usr/X11R6/bin/Xsun24
%endif

%files 75dpi-fonts
%defattr(-,root,root,-)
%dir /usr/X11R6/lib/X11/fonts/75dpi
/usr/X11R6/lib/X11/fonts/75dpi/*.gz
%config /usr/X11R6/lib/X11/fonts/75dpi/fonts.alias
%config /usr/X11R6/lib/X11/fonts/75dpi/fonts.dir

%files 100dpi-fonts
%defattr(-,root,root,-)
%dir /usr/X11R6/lib/X11/fonts/100dpi
/usr/X11R6/lib/X11/fonts/100dpi/*.gz
%config /usr/X11R6/lib/X11/fonts/100dpi/fonts.alias
%config /usr/X11R6/lib/X11/fonts/100dpi/fonts.dir

%files cyrillic-fonts
%defattr(-,root,root,-)
%dir /usr/X11R6/lib/X11/fonts/cyrillic
/usr/X11R6/lib/X11/fonts/cyrillic/*.gz
%config /usr/X11R6/lib/X11/fonts/cyrillic/fonts.alias
%config /usr/X11R6/lib/X11/fonts/cyrillic/fonts.dir

%ifarch i386
%files XF86Setup
%defattr(-,root,root,-)
/usr/X11R6/bin/XF86Setup
/usr/X11R6/bin/xmseconfig
/usr/X11R6/lib/X11/XF86Setup
/usr/X11R6/man/man1/XF86Setup.1x.gz
/usr/X11R6/man/man1/xmseconfig.1x.gz
%endif

%files xfs
%defattr(-,root,root,-)
%attr(-,xfs,xfs) %dir /etc/X11/fs
%attr(-,xfs,xfs) %config(noreplace) /etc/X11/fs/config
%config /etc/rc.d/init.d/xfs
/usr/X11R6/lib/X11/fs
/usr/X11R6/bin/fsinfo
/usr/X11R6/bin/fslsfonts
/usr/X11R6/bin/fstobdf
/usr/X11R6/bin/xfs
/usr/X11R6/man/man1/xfs.1x.gz
/usr/X11R6/man/man1/fsinfo.1x.gz
/usr/X11R6/man/man1/fslsfonts.1x.gz
/usr/X11R6/man/man1/fstobdf.1x.gz

%changelog
* Fri Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- jumping back to 3.3.3.1 - using Serial: 1
- calling xmodmap in XSetup_0 (kdm, gdm backspace problem)

* Tue Jun 29 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- cleanups xdm/Xsession and xdm/Xsetup_0
- updated XTerm (keys Delete, Home and End)
- add some patchs from against 3.3.3.1Z

* Mon Jun 21 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- libtermcap -> ncurses
- using new XTerm app-defaults (based on Casantos's XTerm)
- compressed manpages (thanks to gwm :)
- included the first portuguese man page!

* Wed Jun 16 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- i18n xfs.init
- /usr/doc/ link (Raul Dias's suggestion)
- don't requires xbanner (uses xsetroot)
- added some documentation about FreeType

* Mon Jun 07 1999 Preston Brown <pbrown@redhat.com>
- incorporated all patches since release time from myself and jbj
- removed xfs port hardcode hack; changed init script to start on port -1
- package much documentation as text (not PostScript) where easily possible
- iso8859-2 keyboard input of iso8859-1 chars fixed

* Sat Jun 07 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- Added Quinot's patch to dead-keys
- xkb-brazilian (thanks to Igarashi)
- Added modified Xsession and Xsetup_0
- %ifarch sparc to several patchs that doesn't applies to 3.3.3.1e
- Several patchs commented out - already applied
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Apr 17 1999 Preston Brown <pbrown@redhat.com>
- march64 sparc patch seemed to mess with i386 (problems), ifarch'ed.

* Thu Apr 14 1999 Preston Brown <pbrown@redhat.com>
- added JJ's sparc LEO and Creator patch (sparc3.patch)
- icelandic xkb keyboard 

* Wed Apr 13 1999 Preston Brown <pbrown@redhat.com>
- updated PAM patch so that xdm has pam session support
- require latest version of pam
- fix setting of root color in Xsession

* Tue Apr 13 1999 Bill Nottingham <notting@redhat.com>
- don't run *dm from init script, use inittab instead
- add path to sessreg in Give/TakeConsole

* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- xfs has /bin/false as shell
- xfs security patch (disable tcp connections)
- giveconsole, takeconsole from xdm make utmp/wtmp entries

* Fri Apr 09 1999 Preston Brown <pbrown@redhat.com>
- fixing xserver pam-console stuff.
- prereq utempter

* Thu Apr 08 1999 Preston Brown <pbrown@redhat.com>
- fixed pam-console stuff for Xwrapper
- added hide flag to init scripts so they don't show up in installer ntsysv

* Wed Apr 07 1999 Preston Brown <pbrown@redhat.com>
- improved xfs init script not to try to lock process 'su' but instead 'xfs',
- fixing bug # 2037.
- czech keyboard fixes
- documentation subpackage
- pam-console patch for Xwrapper from mkj

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- new improved creator patch (#17)

* Thu Apr 01 1999 Preston Brown <pbrown@redhat.com>
- if I have to touch the %pre stuff for xkb again I will go totally ballistic.
- xfs prereq for shadow-utils

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- xfs gets its own user (xfs), more xkb fixes

* Mon Mar 29 1999 Preston Brown <pbrown@redhat.com>
- added probing section to xdm init script
- xfs is run by user nobody for security reasons

* Sun Mar 28 1999 Preston Brown <pbrown@redhat.com>
- fix xkb link, add nosuid xterm patch.

* Sat Mar 27 1999 Bill Nottingham <notting@redhat.com>
- unlink /tmp/.X11-unix before making directory

* Sat Mar 27 1999 Jeff Johnson <jbj@redhat.com>
- integrate creator acceleration patch.

* Wed Mar 24 1999 Preston Brown <pbrown@redhat.com>
- obsoletes color-xterm, backwards compatible link as nxterm provided
- fixed up xkb stuff

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- xdm init script fixes

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- dvorak keymap fix
- fixed xfs upgrade error (it was turning it off by accident)
- moved xkb/compiled stuff to /var partition

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- fonts.alias and fonts.dir are marked as config files now
- thinkingmouse/expertmouse movement patch included

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- updated xdm.pamd to have pam-console support.
- workaround for netscape problems in %build section
- xdm.init fixes

* Mon Mar 15 1999 Preston Brown <pbrown@redhat.com>
- DGA 1.1 support + fix alpha DGA, fix unaligned trap errors for MGA cards.

* Sat Mar 13 1999 Jakub Jelinek <jj@ultra.linux.cz>
- Creator acceleration.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group, fixed xdm to not start w/o xfs running.

* Thu Feb 18 1999 Preston Brown <pbrown@redhat.com>
- more patches from ultrapenguin for the sparc

* Mon Feb 15 1999 Preston Brown <pbrown@redhat.com>
- made xfs config file "noreplace". font packages use chkfontpath.
- hacked xfs to remove invalid paths w/o dying (used XF86Config code)
- hacked xfs to be a daemon
- improved default xfs config file
- fixed up the init scripts some

* Wed Feb 10 1999 Preston Brown <pbrown@redhat.com>
- updated xdm.init file to be bash 2 compliant.
- xdm.init inadvertently was in xfs package, moved to main package
- patch removed from Xsession, it should get set with -login flag for bash
- fixed KOI8 fontmapping for key 0xB4, also fixed ru_SU patch (bugzilla
  #1109, #1111)

* Sun Feb 07 1999 Preston Brown <pbrown@redhat.com>
- whoops, chkconfig stuff for xfs moved into its own post/postun handler.

* Fri Feb 05 1999 Preston Brown <pbrown@redhat.com>
- added init.d service for gdm/kdm/xdm
- added patch by Owen Taylor for xinput extension

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- freetype fixes for alpha
- Xauth employed in startx script

* Tue Jan 26 1999 Preston Brown <pbrown@redhat.com>
- forward port back to RawHide (Red Hat 6.0)
- newer version of freetype/truetype support
- fbdev enabled on all archs (2.2 kernel!)
- 3dlabs enabled on alpha
- integrate Cristian's arm stuff
- ru_SU (KOI8-R) character set fixes to locale.alias
- xfs made into an init.d service

* Mon Jan 11 1999 Preston Brown <pbrown@redhat.com>
- integrated 3.3.3.1 patch, removed obsoleted patches.

* Mon Dec 14 1998 Preston Brown <pbrown@redhat.com>
- added permedia chipset clockchip bugfix

* Wed Dec 09 1998 Preston Brown <pbrown@redhat.com>
- alpha sockets patch added, all freetype stuff removed, ultrapeng. banner gone

* Thu Dec 03 1998 Preston Brown <pbrown@redhat.com>
- moved lib/modules and lib/X11/xkb dirs into main package to fix conflicts.

* Wed Dec 02 1998 Preston Brown <pbrown@redhat.com>
- backported package to 5.2.

* Mon Nov 30 1998 Preston Brown <pbrown@redhat.com>
- the big update to XFree 3.3.3. Lots of changes, many patches were merged in.

* Wed Nov 11 1998 Jeff Johnson <jbj@redhat.com>
- sync with ultrapenguin 1.1.
- add __alpha__ check to Imake.cf

* Thu Oct 22 1998 Preston Brown <pbrown@redhat.com>
- added empty fonts.dir and fonts.scale to TrueType dir.

* Wed Oct 21 1998 Preston Brown <pbrown@redhat.com>
- rolled in truetype support to X server / xfs via FreeType.
- separated font server stuff into a separate package

* Thu Oct 08 1998 Cristian Gafton <gafton@redhat.com>
- disabled the S3V patch introduced by Preston
- updated czech patch
- added NeoMagic NM2200 chipset support
- updated NeoMagic patches

* Mon Oct  5 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Acceleration for Creator/Creator3D support.
- Show banner on startup for SPARC Mach64 server as well.

* Fri Oct 02 1998 Preston Brown <pbrown@redhat.com>
- patched cards database to use old S3V driver for most cards

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- enhance Xession to read user's .Xmodmap and .Xresources
- TGA patches from Jay
- alpha lnx_video patch from Jay Estabrook
- czech and slovak patches
- added Neomagic patches
- enabled XF86Setup
- added cyrillic fonts to the %files list
- ifarch i386 for XFree86-Setup package

* Thu Aug 27 1998 Jeff Johnson
- another 1386 -> i386 typo (sigh).

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- add PAM_TTY to xdm patch.

* Wed Jul 29 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.3.2.3

* Sat Jun 27 1998 Matti Aarnio <matti.aarnio@sonera.fi>
- Four patches for 64-bit systems.

* Tue Jun 23 1998 Eddie C. Dost <ecd@skynet.be>
- Fix mach64/SPARC PCI.

* Thu Jun 11 1998 Jeff Johnson <jbj@redhat.com>
- Merge in m68k changes.

* Mon Jun  8 1998 Jeff Johnson <jbj@redhat.com>
- Add build root.

* Thu Jun 04 1998 Prospector System <bugs@redhat.com>
- translations modified for fr

* Tue Jun 02 1998 Erik Troan <ewt@redhat.com>
- added more security fixes

* Mon May 25 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Merged SPARC port with 3.3.2
- Show banner on startup for Xsun* servers

* Tue May 19 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Wed May 13 1998 Jeff Johnson <jbj@redhat.com>
- Merge in sparc changes.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue May 05 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Fix colormaps on SBUS cards, add /dev/fb to the list
  of checked devices even for XSunMono

* Mon May 04 1998 Erik Troan <ewt@redhat.com>
- included security fix which fixes a large number of problems

* Wed Apr 22 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Fix fb mapping on non-accelerated SBUS cards
- Further PCI SPARC changes (from ecd).

* Tue Apr 14 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Merge in PCI SPARC support (written by Eddie C. Dost).

* Tue Apr 07 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Unmap all fb mappings before closing fb in SBUS servers,
  otherwise new kernels don't call fb_close and bad things
  happen.

* Mon Mar 30 1998 Erik Troan <ewt@redhat.com>
- switched to using the Xwrapper from XFree86 rather then a separate package

* Sat Mar 21 1998 Jakub Jelinek <jj@ultra.linux.cz>
- built sparc version against glibc

* Sat Mar 21 1998 Michal Rehacek <majkl@iname.com>
- Accelerated support for Creator/Creator3D

* Tue Mar 03 1998 Erik Troan <ewt@redhat.com>
- updated to XFree86 3.3.2

* Fri Jan 16 1998 Erik Troan <ewt@redhat.com>
- turned off setuid bit for X servers
- require xserver-wrapper (which replaces /usr/X11R6/bin/X)

* Wed Nov 05 1997 Erik Troan <ewt@redhat.com>
- removed XF86Setup
- updated file list to include some missing files

* Tue Nov 04 1997 Michael K. Johnson <johnsonm@redhat.com>
- New PAM conversation function conventions

* Mon Sep 29 1997 Erik Troan <ewt@redhat.com>
- built against tcl/tk 8.0

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- set libc version to 6 (which turns on thread support as well)
- used wildcards more liberally in file lists

* Tue Sep 02 1997 Erik Troan <ewt@redhat.com>
- added notiocsltc patch
- added /usr/X11R6/lib/X11/xserver/SecurityPolicy

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- updated to XFree86 3.3.1

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- add shlibs patch, we links shared libraries against -lc

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- Increased release number to 10 for glibc version

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- Updated to XFree86 3.3

* Thu Mar 20 1997 Erik Troan <ewt@redhat.com>
- Changed xdm to use xbanner
- Changed xdm paths to point to /var/run, /var/log, /etc/X11/xdm instead
  of all pointing to /usr/X11R6/lib/X11/xdm

* Thu Mar 06 1997 Erik Troan <ewt@redhat.com>
- Modified to use pam.d.
