Summary: X based 3270 emulator
Summary(pt_BR): Emulador 3270 baseado em X
Summary(es): Emulador 3270 basado en X
Name: x3270
Version: 3.1.1.6
Release: 7cl
Copyright: MIT
Group: User Interface/X
Group(pt_BR): Interface do Usuário/X
Group(es): Interfaz del Usuario/X
#Source: ftp://ftp.x.org/contrib/applications/x3270/x3270-3.1.1.6.tar.gz
# recompressed with bzip2
Source: ftp://ftp.x.org/contrib/applications/x3270/x3270-3.1.1.6.tar.bz2
Source800: x3270-wmconfig.i18n.tgz
Patch: x3270-3.1.1.6-glibc.patch
Icon: x3270.gif
# Prereq:  /usr/X11R6/bin/mkfontdir
Prereq:  XFree86
BuildRoot: /var/tmp/x3270-root
Summary(de): X-basierter 3270-Emulator
Summary(fr): Emulateur 3270 pour X
Summary(tr): X tabanlý 3270 öykünümcüsü

%description
This program emulates an IBM 3270 terminal, commonly used with mainframe
applications, in an X window.

%description -l pt_BR
Este programa emula um terminal IBM 3270, geralmente usado com
aplicações de mainframe, em um X Window.

%description -l es
Este programa emula un terminal IBM 3270, generalmente usado con
aplicaciones de mainframe, en un X Window.

%description -l de
Dieses Programm emuliert ein IBM 3270-Terminal, das üblicherweise mit
Mainframe-Anwendungen in einem X-Fenster ausgeführt wird.

%description -l fr
Ce programme émule un terminal IBM 3270, couramment utilisé sous X window
avec les gros systèmes.

%description -l tr
Bu program IBM 3270 uçbirim öykünümü yapar. IBM 3270 öykünümü bazý eski
bilgisayar sistemlerine baðlanmak için gerekebilir.

%prep
%setup -q -n x3270-3.1.1
%patch -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

make DESTDIR=$RPM_BUILD_ROOT install install.man
install -m644 X3270.xad $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/X3270

( cd $RPM_BUILD_ROOT
  mkdir -p etc/X11/wmconfig
  #cat > ./etc/X11/wmconfig/x3270 <<EOF
#x3270 name "x3270"
#x3270 description "Emulador de Terminal 3270"
#x3270 group Rede
#x3270 exec "x3270 &"
#EOF
)



tar xvfpz $RPM_SOURCE_DIR/x3270-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/X11R6/bin/mkfontdir /usr/X11R6/lib/X11/fonts/misc

%postun
/usr/X11R6/bin/mkfontdir /usr/X11R6/lib/X11/fonts/misc

%files
%defattr(-,root,root)
%doc Docs
/usr/X11R6/bin/x3270
/usr/X11R6/lib/X11/fonts/misc/3270.pcf.gz     
/usr/X11R6/lib/X11/fonts/misc/3270b.pcf.gz               
/usr/X11R6/lib/X11/fonts/misc/3270-12.pcf.gz  
/usr/X11R6/lib/X11/fonts/misc/3270-12b.pcf.gz
/usr/X11R6/lib/X11/fonts/misc/3270-20.pcf.gz  
/usr/X11R6/lib/X11/fonts/misc/3270-20b.pcf.gz                   
/usr/X11R6/lib/X11/fonts/misc/3270d.pcf.gz             
/usr/X11R6/lib/X11/fonts/misc/3270h.pcf.gz             
/usr/X11R6/lib/X11/fonts/misc/3270gt8.pcf.gz                   
/usr/X11R6/lib/X11/fonts/misc/3270gt12.pcf.gz 
/usr/X11R6/lib/X11/fonts/misc/3270gt12b.pcf.gz
/usr/X11R6/lib/X11/fonts/misc/3270gt16.pcf.gz 
/usr/X11R6/lib/X11/fonts/misc/3270gt16b.pcf.gz                  
/usr/X11R6/lib/X11/fonts/misc/3270gt24.pcf.gz
/usr/X11R6/lib/X11/fonts/misc/3270gt24b.pcf.gz                  
/usr/X11R6/lib/X11/fonts/misc/3270gt32.pcf.gz 
/usr/X11R6/lib/X11/fonts/misc/3270gt32b.pcf.gz
/usr/X11R6/lib/X11/x3270
/usr/X11R6/man/man1/x3270.1x
/usr/X11R6/man/man1/x3270-script.1x
/usr/X11R6/man/man1/ibm_hosts.1x
%config /etc/X11/wmconfig/x3270
%config /usr/X11R6/lib/X11/app-defaults/X3270

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Marc Ewing <marc@redhat.com>
- new version
- added wmconfig entry

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
