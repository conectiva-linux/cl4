%define name wmcdplay
%define version 1.0Beta1
%define release 7cl

%define builddir $RPM_BUILD_DIR/%{name}

Summary: CD player applet
Summary(pt_BR): applet para reproduzir CDs no Window Maker
Summary(es): applet para reproducir CDs en el Window Maker

Name: %{name}
Version: %{version}
Release: %{release}
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL
Url: http://www.geocities.com/SiliconValley/Vista/2471/wmcdplay.htm
Source0: %{name}.tgz
Source1: %{name}.wmconfig
Source800: wmcdplay-wmconfig.i18n.tgz
Patch: %{name}-c++.patch.gz
Buildroot: /tmp/%{name}-%{version}-%{release}-root
Icon: %{name}.gif
Patch1: wmcdplay-security.patch

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition
- Removed suid bit from /usr/X11R6/bin/wmcdplay

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Thu Feb  4  1999 Marcelo Tosatti <marcelo@conectiva.com>
- fixed buffers overflows 

* Tue Dec  8 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Nov 16 1998 Fryguy_ <fryguy@falsehope.com>
  [wmcdplay-1.0Beta1-1]
- Added setuid bit on wmcdplay binary so non root users can access
  the /dev/cdrom.
- Release 1.0 Beta1 05/09/98
  - Added some error checking.
  - "-a artwork_file" is now "-f artwork_file", sorry ;-).
  - Added "-a" command line argument for AfterStep users.
  - Added "-position position" command line argument.
  - Command line arguments, "-a", "-w" and "-s" are now toggle,
     so if you enable one at compile-time, you can override
     it at run-time.
  - Track selection actually works now??
      (anyone notice a recurring theme here??)
  - Seperate update interval for when drive is empty.
      (thanks to .....)
  - Fixed problem with (some?) SCSI devices refusing to
      give LBA values. Thanks to the linux ide-scsi-emulator.
  - Now looks in some known directories for artwork files as
      a last resort.
  - Improved artwork loading (it was very brain-dead).
  - Formatting changes in artwork files (ARTWORK documentation
      is now up-to-date).

%description 
Wmcdplay is a CD player applet designed for the
Windowmaker dock.

%description -l pt_BR
O wmcdplay é um applet reprodutor de CDs projetado
para o dock do Window Maker.

%description -l es
Applet para reproducir CDs en el Window Maker

%prep

%setup -n %{name}

%patch -p1
%patch1 -p1 

%build
xmkmf
make CFLAGS="$RPM_OPT_FLAGS"

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,share/wmcdplay}
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
strip %{builddir}/wmcdplay
rm -f %{builddir}/XPM/standard.art
cp %{builddir}/wmcdplay $RPM_BUILD_ROOT/usr/X11R6/bin
cp %{builddir}/XPM/*.art $RPM_BUILD_ROOT/usr/X11R6/share/wmcdplay
#cp $RPM_SOURCE_DIR/%{name}.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}




tar xvfpz $RPM_SOURCE_DIR/wmcdplay-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc README ARTWORK COPYING
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/wmcdplay
%attr(755,root,root) /usr/X11R6/bin/wmcdplay
%attr(755,root,root) %dir /usr/X11R6/share/wmcdplay
%attr(644,root,root) /usr/X11R6/share/wmcdplay/*.art

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}
