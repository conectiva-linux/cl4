%define Name kdestart
%define Version 1.1.1
%define kderoot /usr

Summary: Startup skript and kdeinitrc for the K Desktop Environment.
Summary(pt_BR): Script de inicializaçao do KDE
Summary(es): Script de inicialización del KDE
Name: %{Name}
Version: %{Version}
Release: 5cl
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Copyright: GPL
Icon: kde.gif
URL: http://www.kde.org/
BuildRoot: /var/tmp/%{Name}-%{Version}
Source: kdestart-1.1.1.tar.bz2
Source1: kde
BuildArchitectures: noarch

%description
Replacement for startx and xinitrc to start KDE in a convenient way.
You have to use the 'kde' command instead of 'startx' to start KDE.

%description -l pt_BR
Substituto para startx e xinitrc para inicializar o KDE de uma
forma conveniente. Voce somente terá que executar 'kde' no lugar de
'startx' para inicializar o KDE.

%description -l es
Sustituye startx y xinitrc para iniciar KDE de forma conveniente.
Use 'kde' en lugar de 'startx' para entrar en KDE.

%prep
%setup -q -n %{Name}-%{Version}

%install
install -d $RPM_BUILD_ROOT/etc/X11/xinit 
install -d $RPM_BUILD_ROOT/%{kderoot}/bin
install -m 755 kdeinitrc $RPM_BUILD_ROOT/etc/X11/xinit 
#install -m 755 kde $RPM_BUILD_ROOT/%{kderoot}/bin

# using our modified kde script
install -m755 $RPM_SOURCE_DIR/kde $RPM_BUILD_ROOT/%{kderoot}/bin


# install stuff in /usr/share
mkdir -p $RPM_BUILD_ROOT/usr/share
cp -av kdestart/ config/ session/ $RPM_BUILD_ROOT/usr/share

#file list
cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' \
    | grep -v "/etc/X11$" \
    | grep -v "/etc/X11/xinit$" \
    | grep -v "/usr$" \
    | grep -v "/usr/bin$" \
    | grep -v "/usr/bin/kde$" \
    | grep -v "/usr/share$" \
    | grep -v "/usr/share/config$" \
    | grep -v "/usr/share/session$" \
    > $RPM_BUILD_DIR/file.list.%{Name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{Name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{Name}

%clean
rm -rf $RPM_BUILD_ROOT/ $RPM_BUILD_DIR/%{Name}-%{Version} $RPM_BUILD_DIR/file.list.%{Name}

%files -f ../file.list.%{Name}

%changelog
* Mon Jun 28 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- kde script fixes call to xauth

* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Added a check to allow us to run gnome more than once at the same time

* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 04 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- turned this a noarch package

* Mon May 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- updated to 1.1.1
- changed the way to get the file list

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 05 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated kdeinitrc to recreate wmconfig entries for all users
  when entering kde

* Thu Mar 04 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Modified spec file to reflect new KDE (version 1.1)
- Uses /usr instead of /opt/kde

* Tue Dec 01 1998 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added check for template files to kdeinitrc

* Tue Nov 03 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- /etc/X11/xinit/kdeinitrc checks .Xmodmap (user & system)

* Sat Oct 31 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Aug 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- changed group/subgroup
