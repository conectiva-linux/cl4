Summary: Default startup script for X Windows
Summary(pt_BR): Script de inicialização default para X Window
Summary(es): Script de inicialización por defecto para X Window
Name: xinitrc
Version: 2.4.1
Release: 1cl
Copyright: Public Domain
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
Source0: xinitrc-xinitrc
Source1: xinitrc-Xclients
Source2: xinitrc-RunWM
Source3: xinitrc-Xmodmap
Source10: xinitrc-Xclients.conectiva
Source11: xinitrc-RunWM.conectiva
Source12: Xmodmaps.tar.gz
Source13: wmchooser
Buildroot: /var/tmp/xinitrc-root
Requires: XFree86 /bin/sh
#Requires: newt # for wmchooser
BuildArchitectures: noarch

%description
This package contains the basic X windows startup script used by the "startx"
command.

%description -l pt_BR
Este pacote contém o script de inicialização básico do X Window
usado pelo comando "startx".

%description -l es
Este paquete contiene el script de arranque básico del X Window
usado por el comando "startx".

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/xinit $RPM_BUILD_ROOT/usr/X11R6/bin

for i in xinitrc Xclients Xmodmap ; do
   install $RPM_SOURCE_DIR/xinitrc-$i $RPM_BUILD_ROOT/etc/X11/xinit/$i
done
install $RPM_SOURCE_DIR/xinitrc-RunWM $RPM_BUILD_ROOT/usr/X11R6/bin/RunWM
for i in Fvwm95 MWM AfterStep WindowMaker icewm ; do
	ln -sf RunWM $RPM_BUILD_ROOT/usr/X11R6/bin/RunWM.$i
done

# overwriting...
install $RPM_SOURCE_DIR/xinitrc-Xclients.conectiva $RPM_BUILD_ROOT/etc/X11/xinit/Xclients
install $RPM_SOURCE_DIR/xinitrc-RunWM.conectiva $RPM_BUILD_ROOT/usr/X11R6/bin/RunWM

# our Xmodmaps
tar xvfz $RPM_SOURCE_DIR/Xmodmaps.tar.gz -C $RPM_BUILD_ROOT/etc/X11/xinit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644,root,root) %config /etc/X11/xinit/Xmodmap*
%attr(755,root,root) %config /etc/X11/xinit/xinitrc
%attr(755,root,root) %config /etc/X11/xinit/Xclients
%attr(755,root,root) /usr/X11R6/bin/RunWM
%attr(-,root,root)   /usr/X11R6/bin/RunWM.*

%changelog
* Fri Jun 18 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to 2.4.1
- %attr

* Thu Jun 17 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- look for not only .Xmodmap/.Xresources, but also Xmodmap/Xresources
- added /etc/sysconfig/desktop support
- Updated Xmodmaps from "casantos" and included spanish Xmodmap into
  our Xmodmaps.tar.gz

* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- wmchoser will be included soon
- added Group, Summary and %description translations

* Thu Mar 18 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- RunWM now runs wmaker.inst for the first use of WindowMaker

* Sat Mar 06 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Modified KDE support for compatibility with 1.0 and 1.1

* Fri Feb 26 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added KDE support
- Fixed bug with RunWM erasing WMRootMenu
- Added wmchooser, for terminal choice of WM

* Thu Dec 03 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- wmaker -nocpp

* Mon Nov 30 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- RunWM pega menu em portugues para o WindowMaker, e dispara wmconfig
  para o icewm

* Sat Nov 21 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- /etc/X11/Xclients with WindowMaker default
- RunWM with icewm support
- Xmodmaps

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Sep 18 1998 Cristian Gafton <gafton@redhat.com>
- added the RunWM script and modified Xclients to use this new script

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- included WindowMaker hints

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 22 1998 Cristian Gafton <gafton@redhat.com>
- handle AfterStep (and possibly other window managers)

* Tue Nov 11 1997 Michael K. Johnson <johnsonm@redhat.com>
- export the BROWSER variable.

* Fri Nov 08 1997 Cristian Gafton <gafton@redhat.com>
- added handling for the BROWSER variable

* Wed Oct 15 1997 Cristian Gaftin <gafton@redhat.com>
- updated for AnotherLevel

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built for glibc, added dependencies

* Thu Mar 20 1997 Erik Troan <ewt@redhat.com>
- Added /etc/X11/xinitrc/Xclients to this file and removed it from rootfiles
  and etcskel.
