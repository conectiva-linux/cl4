%define name WindowMaker
%define version 0.60.0
%define release 7cl
%define prefix /usr/X11R6
%define gnustep /usr/X11R6/lib/GNUstep
%define include /usr/X11R6/include/X11
%define localedir /usr/share/locale
%define datadir /usr/X11R6/share
%define extras 0.1
%define libwmfun 0.0.1
#change this to TRUE to make debugs.
%define DEBUG FALSE

#change this to the location of global default docks
%define dockdir /etc/X11/dock

Summary: NeXT-alike window manager
Summary(pt_BR): Gerente de Janelas parecido com o NeXT
Summary(es): Administrador de Ventanas parecido con el NeXT
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source: ftp://ftp.windowmaker.org:/pub/beta/srcs/%{name}-%{version}.tar.bz2
Source2: ftp://ftp.windowmaker.org:/pub/beta/srcs/%{name}-extra-%{extras}.tar.bz2
Source3: plmenu.pt
Source4: plmenu.es
Source7: WindowMaker-pt.po.tar.bz2
Provides: WindowMaker windowmaker
Requires: libPropList
Patch: WindowMaker-menus-conectiva.patch.bz2
Patch2: WindowMaker-ru.po.patch.bz2
Patch3: WindowMaker-wmaker.inst.patch.bz2
Patch5: WindowMaker-dyndock.patch.bz2
Patch7: WindowMaker-libwmfun.patch.bz2
Patch10: WindowMaker-workspace-changing.patch.bz2
Patch11: WindowMaker-fallback.patch.bz2
Patch12: WindowMaker-WMWindowAttributes.patch.bz2
Patch99: WindowMaker-debug.patch.bz2
BuildRoot: /var/tmp/%{name}_root

%description
WindowMaker is a window manager designed to emulate the look and feel of the 
NEXTSTEP(tm) GUI. It's supposed to be fast, relatively small, feature rich, 
and easy to configure, with a simple and elegant appearance borrowed from 
NEXTSTEP(tm).

This package has compiled with kde and gnome support.
Includes the library libwmfun %{libwmfun} and extras %{extras}.
The GNUstep directory is %{gnustep}.

%description -l pt_BR
WindowMaker é um gerente de janelas projetado para emular a
aparência de parte da interface de usuário do NEXTSTEP(tm). Feito
para ser rápido, relativamente pequeno, rico em características e de
configuração fácil, com uma aparência simples e elegante emprestada
do NEXTSTEP(tm).

%description -l es
WindowMaker es un administrador de ventanas proyectado para emular la
apariencia de parte de la interface de usuario del NEXTSTEP(tm). Se
hizo para ser rápido, relativamente pequeño, rico en características
y de configuración fácil, con una apariencia sencilla y elegante
prestada del NEXTSTEP(tm).

%prep
%setup -q -a 2 -a 7

#here come the patches...
gzip -dc libwmfun-%{libwmfun}.tar.gz | tar xv
bzip2 -dc $RPM_SOURCE_DIR/WindowMaker-libwmfun.patch.bz2 | patch -p0
%patch -p0
%patch2 -p0
%patch3 -p0
%patch5 -p0
%patch10 -p1
%patch11 -p0
%patch12 -p0

%build
touch WindowMaker/plmenu.pt
touch WindowMaker/plmenu.es

export LINGUAS=`grep ^supported_locales configure | sed 's/supported_locales="// ; s/\"//g'`
export GNUSTEP_LOCAL_ROOT=$RPM_BUILD_ROOT%{gnustep}
export DOCKDIR=%{dockdir}

if [ "%{DEBUG}" = "TRUE" ];then
    export CFLAGS="$RPM_OPT_FLAGS -g"
    export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -g"
else
    export CFLAGS="$RPM_OPT_FLAGS"
    export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
fi

./configure \
	--enable-kde \
    --enable-gnome \
    --with-x \
	--prefix=%{prefix} \
	--with-pixmapdir=%{datadir}/WindowMaker/Pixmaps \
	--datadir=%{datadir} \
	--includedir=%{include} \
	--with-nlsdir=%{localedir} \
	--with-appspath=%{gnustep}/Apps

cd libwmfun-%{libwmfun}
./configure --prefix=%{prefix}
cd -

if [ "%{DEBUG}" = "TRUE" ]; then
    bzip2 -dc $RPM_SOURCE_DIR/WindowMaker-debug.patch.bz2 | patch -p0
fi

# remove WindowMaker defaults database, which will be created again with the
# new root (why not automatically ?) :)
rm -f WindowMaker/Defaults/WindowMaker
rm -f WindowMaker/Defaults/WMState
# go through the motions
make

# yeah, fun! :P
cd libwmfun-%{libwmfun}
make
mv README README.libwmfun
mv AUTHORS AUTHORS.libwmfun
mv NEWS NEWS.libwmfun
cd -

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install-strip

cd libwmfun-%{libwmfun}
make install DESTDIR=$RPM_BUILD_ROOT
cd -

install -m 644 $RPM_SOURCE_DIR/plmenu.{es,pt} $RPM_BUILD_ROOT%{datadir}/WindowMaker
install -m 644 libwmfun-%{libwmfun}/WMFun-demo.style $RPM_BUILD_ROOT%{datadir}/WindowMaker/Styles
install -d $RPM_BUILD_ROOT%{dockdir}

cd %{name}-extra-%{extras}
./configure --prefix=%{prefix}
make DESTDIR=$RPM_BUILD_ROOT install

# files section

cd $RPM_BUILD_ROOT

cat << EOF > $RPM_BUILD_DIR/file.list.%{name}
%defattr(-,root,root)
%dir /usr/X11R6/etc/WindowMaker
%dir /usr/X11R6/share/WindowMaker
%dir /usr/X11R6/share/WindowMaker/Pixmaps
%dir /usr/X11R6/share/WindowMaker/Icons
%dir /usr/X11R6/share/WindowMaker/Backgrounds
%dir /usr/X11R6/share/WindowMaker/IconSets
%dir /usr/X11R6/share/WindowMaker/Themes
%dir /usr/X11R6/share/WINGs
%dir /usr/X11R6/lib/GNUstep
%dir /usr/X11R6/lib/GNUstep/Apps
%dir /usr/X11R6/lib/GNUstep/Apps/WPrefs.app
%dir /usr/X11R6/lib/GNUstep/Apps/WPrefs.app/xpm
%dir /usr/X11R6/lib/GNUstep/Apps/WPrefs.app/tiff
%dir %{dockdir}
EOF

echo "%doc \
      AUTHORS BUGS BUGFORM COPYING COPYING.OPL ChangeLog \
      FAQ FAQ.I18N INSTALL NEWS README \
      README.GNOME README.KDE TODO MIRRORS \
      libwmfun-%{libwmfun}/README.libwmfun \
      libwmfun-%{libwmfun}/AUTHORS.libwmfun \
      libwmfun-%{libwmfun}/NEWS.libwmfun" \
      >> $RPM_BUILD_DIR/file.list.%{name}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' >> \
    $RPM_BUILD_DIR/file.list.%{name}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
    $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name} $RPM_BUILD_DIR/%{name}-%{version}

%files -f ../file.list.%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Thu Jul 01 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- added and fixed some icons in WMWindowAttributes
- added /usr/share/icons to iconpath
- changed pop-up balloons to yes

* Thu Jun 24 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- fixed sed scripts in wmaker.inst for dyndoc (i.e. changed / to §)
- added more directives for icons in WMWindowAttributes
- redirect errors in wmaker.inst dyndock commands to null
- dis-commented plmenu.{es,pt} in specfile (why is commented ? :P)

* Thu Jun 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- removed kfm in the autostart script
- removed libwmfun - is in the original tarball now
- added a global dock dir feature in wmaker.inst

* Tue Jun 08 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- added new pt_BR potfiles

* Fri Jun 04 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- updated to 0.60.0
- removed some fixes already in sources
- fix location of WPrefs in WMState
- added some debug options
- changed the fallback wm to icewm
- added some more descriptions
- set LINGUAS to all supported locales - thanks rodarvus@conectiva.com

* Fri May 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- unset LINGUAS
- added -fno-rtti -fno-exceptions to CXXFLAGS (And created it! ;)

* Thu May 20 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Default savesession to yes
- Added kfm to autostart script

* Tue May 11 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Fix pixmap/icons path inconsistency

* Mon May 03 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Included missing libwmfun docs

* Thu Apr 22 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Upgraded to 0.53.0
- Added patch for windows style cycling on top
- Added patch to #define windows style cycling
- Removed some patches which don't applied or are already in sources now

* Fri Apr 09 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Fix for a bug in workspace changing
- Added new type of texture - stpixmap
- Added patch for windows style cycling (as option)

* Mon Apr 05 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added libwmfun 0.0.1
- Fix crash in wprefs set pixmap
- Patch for wmsound --hidden

* Thu Apr 01 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 0.52.0

* Wed Mar 31 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added icon definition for wmakerconf
- Changed some pt traductions

* Mon Mar 29 1999 Eliphas <eliphas@conectiva.com>
- changed path of Pixmaps

* Fri Mar 19 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- wmaker.inst to move plmenu.$LANG -> G/D/WMRootMenu, not preprocess...

* Thu Mar 18 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- wmaker.inst now don't create .xinitrc and can be called from RunWM
- wmaker.inst now create menus.$LANG in property list format

* Mon Mar 15 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Fixed some inconsistences with file.list
- Updated (uff...) to 0.51.2 final
- Removed asclock, we don't need since we have wmclock and wmtime :)

* Tue Mar 09 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated (Again!) to 0.51.2pre2

* Mon Mar 08 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 0.51.1
- added libPropList as requires, since is now a separate package

* Thu Dec 03 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- version 0.20.3

* Mon Nov 30 1998 Conectiva <dist@conectiva.com>
- updated to 0.20.2
- menu.pt with wmconfig
- WMRootMenu.pt

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- fixed swicthing to other window managers problem
- updated to 0.20.1
- include all the .mo files, not just WindowMaker...
- added an older version of asclock as wmclock
- include libPropList.a in the %files

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- version 0.19.3

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- version 0.19.2
- don't require asclock as a separate package

* Wed Aug 12 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 0.17.5

* Tue Jul 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.17.2

* Thu Jul 09 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.16.1

- removed asclock (conflicts with AfterStep)

* Fri Feb 27 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.14.0

* Fri Jan 30 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 0.13.0
- added the include files and the development libraries

* Thu Nov 20 1997 Cristian Gafton <gafton@redhat.com>
- first build against glibc
