%define kdeprefix /usr
%define version 1.1.1
%define kderelease 4cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source

%define kdename kdebase
%define pamservice kde
Name: %{kdename}
Summary: K Desktop Environment - core files
Summary(pt_BR): K Desktop Environment - arquivos básicos
Summary(es): K Desktop Environment - archivos básicos
Version: %{version}
Release: %{kderelease}
Source: ftp://ftp.kde.org:/pub/kde/{sourcedir}/%{kdename}-%{version}.tar.bz2
Source1: cnc-logo.xpm
Source2: fvwm-2.0.46.icons.tar.gz
Patch: kdebase-%{version}-cnc.patch
Patch2: kdebase-%{version}-redhat.patch
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL/Artistic
BuildRoot: /var/tmp/%{kdename}-buildroot
Requires: qt >= 1.42 versão-conectiva >= 3.0 kdesupport kdelibs wmpixmaps wmconfig >= 0.6-3 rman
Prefix: %{kdeprefix}
Prereq: XFree86
Obsoletes: kde

%description
Core applications for the K Desktop Environment.
Included are:  kdm (replacement for xdm), kwm (window manager), kfm 
(filemanager, web browser, ftp client, ...), konsole (xterm replacement), 
kpanel (application starter and desktop pager), kaudio (audio server), 
kdehelp (viewer for kde help files, info and man pages), plus other KDE 
components (kcheckpass, kikbd, kvt, kscreensaver, kcontrol, kfind, 
kfontmanager, kmenuedit, kappfinder).

PAM password authentication is supported via PAM service: %{pamservice}.

%description -l pt_BR
Aplicações básicas para o KDE.

Incluídos neste pacote:

kaudio:       servidor de áudio
kcontrol:     ferramenta de configuração
kdehelp:      visualizador dos arquivos de ajuda, info e páginas de manual
kdm:          substituto do xdm
kfind:        ferramenta de busca
kfm:          gerenciador de arquivos, browser, cliente ftp...
kfontmanager: seletor de fontes
kmenuedit:    ferramenta para adicionar aplicação ao painel
kpanel:       paginador da área de trabalho
kscreensaver: diversos salvadores de tela
kvt:          substituto do xterm
kwm:          gerenciador de janelas do kde
kappfinder:   procura aplicações não-kde

%description -l es
Aplicaciones básicas para KDE.
Incluidos en este paquete:

kaudio:       servidor de audio
kcontrol:     herramienta de configuración
kdehelp:      visor de los archivos de ayuda, info y páginas de manual
kdm:          substituto del xdm
kfind:        herramienta de búsqueda
kfm:          administrador de archivos, browser, cliente ftp...
kfontmanager: selector de fuentes
kmenuedit:    herramienta para adicionar aplicación al panel
kpanel:       paginador del área de trabajo
kscreensaver: diversos guardadores de pantalla
kvt:          substituto del xterm
kwm:          administrador de ventanas del kde
kappfinder:   búsqueda aplicaciones en -kde

%package -n wmpixmaps
Summary: Icons and pixmaps for many Window Managers
Summary(pt_BR): Ícones e mapas de píxeis para gerenciadores de janelas
Summary(es): Iconos y "pixmaps" para administradores de ventanas
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Obsoletes: fvwm95-icons

%description -n wmpixmaps
This package contain various pixmaps for many Window
Managers

%description -l pt_BR -n wmpixmaps
Ícones e mapas de píxeis para gerenciadores de janelas.

%description -l es -n wmpixmaps
Iconos y "pixmaps" para administradores de ventanas.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n kdebase-%{version} -a 2

%patch -p1
%patch2 -p1

#Remove duplicates found in AnotherLevel
rm -rf bomb.xpm question.xpm xterm.xpm mini-xboing.xpm folder.xpm

%build
[ "$LINGUAS" ] && unset LINGUAS
export KDEDIR=%{kdeprefix}
./configure  \
	--prefix=%{kdeprefix} \
	--with-pam=%{pamservice}  \
	--with-install-root=$RPM_BUILD_ROOT

make CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti"

%install

mkdir -p $RPM_BUILD_ROOT/usr/share/icons $RPM_BUILD_ROOT/usr/share/icons/mini
cd $RPM_BUILD_DIR/%{kdename}-%{version}
cp -fR icons/*.xpm $RPM_BUILD_ROOT/usr/share/icons
mv $RPM_BUILD_ROOT/usr/share/icons/mini*.xpm \
	$RPM_BUILD_ROOT/usr/share/icons/mini

make prefix=$RPM_BUILD_ROOT%{kdeprefix} RUN_KAPPFINDER=no install-strip

# remove unsupported control center information services
#cd $RPM_BUILD_ROOT%{kdeprefix}/share/applnk/Settings/Information
#rm -f partitions.kdelnk

# install cnc-logo icon for kdm
install -m 644 $RPM_SOURCE_DIR/cnc-logo.xpm \
	$RPM_BUILD_ROOT%{kdeprefix}/share/apps/kdm/pics/cnc-logo.xpm
cd $RPM_BUILD_ROOT%{kdeprefix}/share/config
install -m 644 $RPM_BUILD_DIR/%{kdename}-%{version}/kdm/config/kdmrc \
	$RPM_BUILD_ROOT%{kdeprefix}/share/config/kdmrc-temp
sed -e "s.^#Logo.Logo." kdmrc-temp > kdmrc
rm -f kdmrc-temp

# install linux console fonts
install -d $RPM_BUILD_ROOT%{kdeprefix}/X11R6/fonts
for file in $RPM_BUILD_DIR/%{kdename}-%{version}/konsole/other/linux*.pcf.gz ; do
    install -m 644 $file $RPM_BUILD_ROOT%{kdeprefix}/X11R6/fonts
done

#enable suid bit for konsole_grantpty
chmod u+s $RPM_BUILD_ROOT/usr/bin/konsole_grantpty

#install pam configuration file
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
install -m 0644 $RPM_BUILD_DIR/%{kdename}-%{version}/kde.pamd \
	$RPM_BUILD_ROOT/etc/pam.d/%{pamservice}

cd $RPM_BUILD_ROOT
find . -type d | grep -v "/usr/share/locale" | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
	-e '/\/config\//s|^|%config |' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

grep "\.xpm" $RPM_BUILD_DIR/file.list.%{kdename} | \
	grep "\/usr\/share\/icons" > \
	$RPM_BUILD_DIR/wmpixmaps.filelist

grep -vf $RPM_BUILD_DIR/wmpixmaps.filelist $RPM_BUILD_DIR/file.list.%{kdename} > $RPM_BUILD_DIR/filelist.01
grep -v "%attr(-,root,root) /usr/bin/rman" $RPM_BUILD_DIR/filelist.01 > $RPM_BUILD_DIR/filelist.02
grep -v "%attr(-,root,root) /usr/bin/kde$" $RPM_BUILD_DIR/filelist.02 > $RPM_BUILD_DIR/filelist.01
mv -f $RPM_BUILD_DIR/filelist.01 $RPM_BUILD_DIR/file.list.%{kdename}

%post
# add the linux fonts for the console
cp $RPM_INSTALL_PREFIX/X11R6/fonts/linux*.pcf.gz /usr/X11R6/lib/X11/fonts/misc
/usr/X11R6/bin/mkfontdir /usr/X11R6/lib/X11/fonts/misc

%preun
# remove the linux fonts added for the console
rm -f /usr/X11R6/lib/X11/fonts/misc/linux*.pcf.gz
/usr/X11R6/bin/mkfontdir /usr/X11R6/lib/X11/fonts/misc

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/files.list.%{kdename} \
       $RPM_BUILD_DIR/wmpixmaps.filelist $RPM_BUILD_DIR/filelist.01 \
       $RPM_BUILD_DIR/filelist.02

%files -f ../file.list.%{kdename} 

%files -n wmpixmaps -f ../wmpixmaps.filelist

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue May 11 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- fixed @KDEDIR@ in kdmrc (in cnc.patch)

* Tue May 11 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Changed prereqs to XFree86

* Wed May 05 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- unset LINGUAS
- updated for KDE-1.1.1
- install linux console fonts for konsole.
- files in KDEDIR/share/applnk no longer treated as %config files

* Sat Apr 03 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- obsoletes kde from parolin

* Sun Mar 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed find-requires

* Fri Mar 19 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- kdehelp back to package! :)
- correct folder.xpm back to package :)
- added Group, Summary and %description translations

* Wed Mar 03 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Created new package, wmpixmaps, that holds all kde and fvwm pixmaps

* Thu Feb 25 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Compiled with -fno-exceptions -fno-rtti
- Added postinstall script for kappfinder and wmconfig

* Mon Jan 18 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added pt_BR translations

* Tue Jan 05 1999 Preston Brown <pbrown@redhat.com>
- re-merged from Duncan Haldane's stuff
