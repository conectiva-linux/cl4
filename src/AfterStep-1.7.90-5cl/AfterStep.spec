Summary: AfterStep Window Manager
Summary(pt_BR): Gerenciador de Janelas AfterStep
Summary(es): Administrador de Ventanas AfterStep
Name: AfterStep
Version: 1.7.90
Release: 5cl
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source0: ftp://ftp.afterstep.org/devel/snapshots/AfterStep-%{version}.tar.gz
Source1: AfterStep-redhat.tar.gz
BuildRoot: /var/tmp/afterstep-root
Prereq: ldconfig
Requires: wmconfig >= 0.9.4, xinitrc >= 1.4, AfterStep-APPS

%description
AfterStep is a continuation of the BowMan window manager which was
originally put together by Bo Yang. BowMan was based on the fvwm window
manager, written by Robert Nation. Fvwm was based on code from twm. And so
on... It was originally designed to emulate some of the look and feel of the
NEXTSTEP user interface, but has since taken steps towards adding more
useful, requested, and neat features especially in 1.4 version ! The changes
which comprise AfterStep's personality were originally part of bowman
development, but due to a desire to move past simple emulation and into a
niche as its own valuable window manager, AfterStep designers decided to
change the project name and move on.

Important features of AfterStep include:

1. Wharf: a free-floating application loader which can "Swallow" running
programs and also can contain "Folders" of more applications.
2. Gradient filled TitleBars with 5 button : help/zap, action/tasks,
iconize/maximise, shade/stick & close/destroy buttons
3. Gradient filled root window PopUp menus which can be configured to
accomodate different tastes and styles of management
4. NEXTSTEP style icons which give a consistent look to the entire desktop
5. Pixmapped Pager with desktop pixmmaping
6. Easy to use look files, to share you desktop appearance with your friends
7. Start menu entries in a hierarchy of directories
8. WinList : a tasklist which can be horizontal or vertical
9. Many modules & asapps to give a good look to your X window station

%description -l pt_BR
Afterstep é a continuação do gerenciador de janelas BowMan que foi
originalmente montado por Bo Yang. BowMan foi baseado no gerenciador
de janelas fvwm do Robert Nation. Fvwm foi baseado em código do
twm. E assim por diante... Foi originalmente projetado para emular
um pouco da aparência do NEXTSTEP, mas desde então tem recebido
características interessantes, pedidas e úteis, especialmente na
versão 1.4!

%description -l es
Afterstep es la continuación del administrador de ventanas BowMan
que fue originalmente montado por Bo Yang. BowMan fue basado en
el administrador de ventanas fvwm del Robert Nation. Fvwm fue
basado en código del twm. Y así por delante... Fue originalmente
proyectado para emular un poco de la apariencia del NEXTSTEP,
pero desde entonces tiene recibido características interesantes,
pedidas y útiles, especialmente en la versión 1.4!

%prep
%setup -q
rm -rf afterstep/start
tar xzf $RPM_SOURCE_DIR/AfterStep-redhat.tar.gz

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6 --datadir=/usr/share \
	--with-imageloader="xv -root -quit" \
	--with-helpcommand="xterm -e man" \
	--with-desktops=1 \
	--with-deskgeometry=2x3 \
	--disable-availability \
	--enable-makemenusonboot \
	--with-xpm
make CCFLAGS="$RPM_OPT_FLAGS"
sgml2html doc/afterstep.sgml

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/usr/X11R6/bin/{sessreg,xpmroot}
	
%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/X11R6/bin/*
/usr/share/afterstep
/usr/X11R6/man/*/*
%doc doc/code doc/languages doc/licences NEW README TEAM README.RedHat 
%doc UPGRADE *.html TODO

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- optimizations are making it sick

* Sun Apr 11 1999 Preston Brown <pbrown@redhat.com>
- fixed up menus from 5.2 to work with new AfterStep

* Thu Apr 08 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 1.7.90 (bugfix release), now 99 percent GNOME compliant.

* Wed Mar 24 1999 Bill Nottingham <notting@redhat.com>
- don't require xterm-color

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Oct 13 1998 Cristian Gafton <gafton@redhat.com>
- Fixed problem with the Feels menu showing the bacjkground change entries

* Wed Sep 16 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5
- requires AfterStep-APPS for the cool dockable applications

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- 1.4.5.3 is out
- wmconfig hacks
- can start AnotherLevel

* Fri Apr 17 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.4.5.1
- went through the sources and fixed some of the bugs

* Fri Mar 27 1998 Cristian Gafton <gafton@redhat.com>
- packaged 1.4.4 with a patch to better support BuildRoot.
