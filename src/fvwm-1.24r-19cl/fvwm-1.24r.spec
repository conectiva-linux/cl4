Summary: Feeble (Fine?) Virtual Window Manager
Summary(pt_BR): Gerenciador de Janelas: Feeble (Fine?) Virtual Window Manager
Summary(es): Administrador de Ventanas: Feeble (Fine?) Virtual Window Manager
Name: fvwm
Version: 1.24r
Release: 19cl
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Icon: fvwm.gif
Requires: wmpixmaps
#Source0: sunsite.unc.edu:/pub/Linux/X11/window-managers/fvwm-1.24r.tar.gz
# recompressed with bzip2
Source0: sunsite.unc.edu:/pub/Linux/X11/window-managers/fvwm-1.24r.tar.bz2
Source1: fvwm-1.24r-system.fvwmrc
Patch0: fvwm-1.24r-fsstnd.patch
Patch1: fvwm-1.24r-imake.patch
Patch2: fvwm-1.24r-security.patch
Patch3: fvwm-1.24r-fvwmman.patch
Buildroot: /var/tmp/fvwm-root
Summary(de): Feeble (Fine?) Virtual Window Manager 
Summary(fr): Feeble (Fine ?) Virtual Window Manager
Summary(tr): X11 için pencere denetleyicisi

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Nov 27 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- acertada a permissão do /etc/X11/fvwm/system.fvwmrc para 644

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- tagged config files correctly
- buildroot

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- fixed it for AnotherLevel (icon paths, etc)

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 24 1997 Michael Fulbright <msf@redhat.com>
- Fixed system.fvwmrc to point at /usr/X11R6/include/X11/bitmaps and pixmaps. 
  Fvwm wasn't find icons otherwise, which is why they disappeared if someone
  upgraded from 4.0 to 4.1! 

%description
fvwm is a small, fast, and very flexible window manager.  It can be
configured to look like Motif, and has a useful "button bar".

%description -l pt_BR
fvwm é um gerente de janelas pequeno, rápido e muito flexível. Ele
pode ser configurado para parecer com Motif, e possui uma útil
"barra de botões".

%description -l es
fvwm es un administrador de ventanas pequeño, rápido y muy flexible.
Puede ser configurado para parecer con Motif, y posee una útil
"barra de botones".

%prep
%setup
%patch0 -p1 -b .fsstnd
%patch1 -p1 -b .imake
%patch2 -p1 -b .security
%patch3 -p1 -b .fvwmman

%build
export PATH=$PATH:/usr/X11R6/bin
xmkmf
make Makefiles
make

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/fvwm/
install -m644 $RPM_SOURCE_DIR/fvwm-1.24r-system.fvwmrc $RPM_BUILD_ROOT/etc/X11/fvwm/system.fvwmrc
strip $RPM_BUILD_ROOT/usr/X11R6/bin/fvwm
strip $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fvwm/* || :

%files
/usr/X11R6/lib/X11/fvwm
/usr/X11R6/bin/fvwm
%dir /etc/X11/fvwm
%config /etc/X11/fvwm/system.fvwmrc
/usr/X11R6/man/*/*
%doc sample.fvwmrc/*

%clean
rm -rf $RPM_BUILD_ROOT
