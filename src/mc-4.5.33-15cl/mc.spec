# Note that this is NOT a relocatable package
%define ver      4.5.33
%define rel      15cl
%define prefix   /usr

Summary: A user-friendly file manager and visual shell.
Summary(pt_BR): Interpretador de comandos visual Midnight Commander
Summary(es): Interpretador de comandos visual Midnight Commander
Name:      mc
Version:   %ver
Release:   %rel
Copyright: GPL
Group: System Environment/Shells
Group(pt_BR): Ambiente do Sistema/Interpretadores de Comandos
Group(es): Ambiente del Sistema/Interpretadores de Comandos
Source0:   ftp://ftp.nuclecu.unam.mx/linux/local/devel/mc-%{PACKAGE_VERSION}.tar.bz2
Source1:   redhat.links
Source2:   ldp.xpm
Source3:   mc-pt_BR.po
Source4:   mc.ini
Source5:   mcserv.init
Source800: mc-wmconfig.i18n.tgz
URL:       http://www.gnome.org/mc/
BuildRoot: /var/tmp/mc-%{PACKAGE_VERSION}-root
Requires:  pam >= 0.59
#Requires:  redhat-logos

Prereq:    /sbin/chkconfig

Patch0:    mc-4.5.27-xtermcolor.patch
Patch2:    mc-4.5.30-fixwarning.patch

Patch16:   mc-4.5.30-norpmmime.patch
Patch17:   mc-4.5.33-pt_BR.patch

%description
Midnight Commander is a visual shell much like a file manager, only with way
more features.  It is text mode, but also includes mouse support if you are
running GPM.  Its coolest feature is the ability to ftp, view tar, zip
files, and poke into RPMs for specific files.  :-)

%description -l pt_BR
Midnight Commander é um interpretador de comandos visual que mais
parece um gerenciador de arquivos, somente com várias características
a mais. Ele é um programa de modo texto, mas inclui suporte para
mouse se você estiver rodando GPM ou em uma janela xterm. Sua
característica mais legal é a habilidade de bisbilhotar em RPMs
procurando arquivos específicos. :-)

%description -l es
Midnight Commander es un interpretador de comandos visual que
más parece un administrador de archivos, solamente con varias
características a más. Es un programa en modo texto, pero incluye
soporte para ratón, si estuviera ejecutando GPM o en una ventana
xterm. Su característica más genial es la habilidad de cotillear
en RPMs buscando archivos específicos. :-)

%package -n gmc
Summary: Midnight Commander visual shell (GNOME version).
Summary(pt_BR): Shell visual Midnight Commander (Versão GNOME)
Summary(es): Shell visual Midnight Commander (Versión GNOME)
Requires: mc >= %{PACKAGE_VERSION}
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
%description -n gmc
Midnight Commander is a visual shell much like a file manager, only with
way more features.  This is the GNOME version. It's coolest feature is the
ability to ftp, view tar, zip files and poke into RPMs for specific files.
The GNOME version of Midnight Commander is not yet finished though. :-(

%description -l pt_BR -n gmc
Midnight Commander é um interpretador de comandos visual, muito
parecido com um gerenciador de arquivos, somente com _muitas_ outras
capacidades.  Uma de suas características mais interessantes é sua
habilidade de conectar-se a servidores ftp, visualizar arquivos tar,
zip e rpms.

%description -l es -n gmc
Midnight Commander es un interpretador de comandos visual, muy
parecido con un administrador de archivos, solamente que con _muchas_
otras capacidades.  Una de sus características más interesantes es
su habilidad para conectarse a servidores ftp, visualizar archivos
tar, zip y rpms.

%package -n mcserv
Summary: Server for the Midnight Commander network file management system.
Summary(pt_BR): Servidor de arquivos do Midnight Commander
Summary(es): Servidor de archivos del Midnight Commander
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Requires: portmap
%description -n mcserv
The Midnight Commander file management system will allow you to
manipulate the files on a remote machine as if they were local.  This is
only possible if the remote machine is running the mcserv server program.
Mcserv provides clients running Midnight Commander with access to the
host's file systems.

Install mcserv on machines if you want to access their file systems
remotely using the Midnight Commander file management system.

%description -l pt_BR -n mcserv
Mcserv é um servidor para o sistema de arquivos em rede do Midnight
Commander. Ele permite que clientes usando o mc acessem remotamente
o sistema de arquivos da máquina em que está rodando.

%description -l es -n mcserv
Mcserv es un servidor para el sistema de archivos en red del Midnight
Commander. Permite que clientes usando el mc accedan remotamente
al sistema de archivos de la máquina en que está ejecutando.

%prep
%setup -q
%patch -p1 -b .xtermcolor

%patch2 -p1 -b .fixwarning

%patch16 -p1 -b .norpmmime
%patch17 -p1 -b .pt_BR

%build
cp $RPM_SOURCE_DIR/mc-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
export LDFLAGS="$RPM_OPT_FLAGS"
unset LINGUAS
autoconf
CFLAGS="$RPM_OPT_FLAGS -g" ./configure \
	--prefix=%{prefix} --sysconfdir=/etc\
	--with-gnome \
	--without-debug \
	--with-included-slang
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,X11/wmconfig}

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install
strip $RPM_BUILD_ROOT/usr/bin/*
(cd icons; make prefix=$RPM_BUILD_ROOT%{prefix} install_icons)
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv

install lib/mcserv.pamd $RPM_BUILD_ROOT/etc/pam.d/mcserv
install -m644 lib/mc.global $RPM_BUILD_ROOT/etc

# clean up this setuid problem for now
chmod 755 $RPM_BUILD_ROOT/%{prefix}/lib/mc/bin/cons.saver

gzip -9f $RPM_BUILD_ROOT/usr/man/man*/*

# copy redhat desktop default icons
#mkdir -p $RPM_BUILD_ROOT/%{prefix}/lib/desktop-links/
#install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{prefix}/lib/desktop-links/

# ldp icon
#install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{prefix}/share/pixmaps/mc

install -m 644 $RPM_SOURCE_DIR/mc.ini $RPM_BUILD_ROOT/%{prefix}/lib/mc/





tar xvfpz $RPM_SOURCE_DIR/mc-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n mcserv
/sbin/chkconfig --add mcserv

%postun -n mcserv
/sbin/chkconfig --del mcserv

%files
%defattr(-, root, root)

%doc FAQ COPYING NEWS README
%{prefix}/bin/mc
%{prefix}/bin/mcedit
%{prefix}/bin/mcmfmt
%{prefix}/lib/mc/mc.ext
%{prefix}/lib/mc/mc.hint
%{prefix}/lib/mc/mc.hlp
%{prefix}/lib/mc/mc.lib
%{prefix}/lib/mc/mc.menu
%{prefix}/lib/mc/bin/cons.saver
%{prefix}/lib/mc/extfs/*
%{prefix}/man/man1/*
%config %{prefix}/lib/mc/mc.ini
%dir %{prefix}/lib/mc
%dir %{prefix}/lib/mc/bin
#%{prefix}/share/mime-info/*

%files -n mcserv
%defattr(-, root, root)

%attr(0644, root, root) %config /etc/pam.d/mcserv
%config /etc/rc.d/init.d/mcserv
%attr(-, root, man)  %{prefix}/man/man8/mcserv.8.gz
%{prefix}/bin/mcserv

%files -n gmc
%defattr(-, root, root)

%doc lib/README.desktop
%config /etc/mc.global
%{prefix}/bin/gmc
%{prefix}/bin/plain-gmc
%{prefix}/lib/mc/layout
%{prefix}/lib/mc/mc-gnome.ext
%{prefix}/share/pixmaps/mc/*
%{prefix}/share/locale/*/*/*
%{prefix}/share/mime-info/mc.keys

%config /etc/CORBA/servers/*
#%config /usr/lib/desktop-links/*

%changelog
* Thu Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- mode 644 /etc/mc.global

* Sun Jun 27 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fixes c-format in pt_BR.po

* Sun Jun 27 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- updated to 4.5.33
- pt_BR.po, mc.ini, compressed man pages
- get rid of profile.d scripts
- recompressed sources
- optimize flags

* Mon Apr 19 1999 Michael Fulbright <drmike@redhat.com>
- removed rpm menu defs - we depend on gnorpm for these
- fixed bug that caused crash if group doesnt exist for file

* Thu Apr 15 1999 Michael Fulbright <drmike@redhat.com>
- cleanup several dialogs

* Mon Apr 12 1999 Michael Fulbright <drmike@redhat.com>
- true version 4.5.30

* Fri Apr 09 1999 Michael Fulbright <drmike@redhat.com>
- version pre-4.5.30 with patch to make this link on alpha properly
  Mark as version 0.7 to denote not the official 4.5.30 release

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Wed Mar 31 1999 Michael Fulbright <drmike@redhat.com>
- fixed errata support URL

* Tue Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.29
- added default desktop icons for Red Hat desktop
- added redhat-logos to requirements
- added README.desktop to doc list for gmc
- added locale data

* Fri Mar 25 1999 Preston Brown <pbrown@redhat.com>
- patched so that TERM variable set to xterm produces color

* Mon Mar 22 1999 Michael Fulbright <drmike@redhat.com>
- made sure /etc/pam.d/mcserv has right permissions

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.27

* Tue Mar 16 1999 Michael Fulbright <drmike@redhat.com>
- fix'd icon display problem

* Sun Mar 14 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.25 AND 4.5.26

* Wed Mar 10 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.24

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.16
- removed mc.keys from mc file list

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.14
- fixed file list

* Sat Feb 06 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.11

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.10

* Fri Jan 22 1999 Michael Fulbright <drmike@redhat.com>
- added metadata to gmc file list

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.9

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.6

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated for GNOME freeze

* Thu Aug 20 1998 Michael Fulbright <msf@redhat.com>
- rebuilt against gnome-libs 0.27 and gtk+-1.1

* Thu Jul 09 1998 Michael Fulbright <msf@redhat.com>
- made cons.saver not setuid

* Sun Apr 19 1998 Marc Ewing <marc@redhat.com>
- removed tkmc

* Wed Apr 8 1998 Marc Ewing <marc@redhat.com>
- add %{prefix}/lib/mc/layout to gmc

* Tue Dec 23 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added --without-debug to configure,
- modification in %build and %install and cosmetic modification in packages
  headers,
- added %%{PACKAGE_VERSION} macro to Buildroot,
- removed "rm -rf $RPM_BUILD_ROOT" from %prep.
- removed Packager field.

* Thu Dec 18 1997 Michele Marziani <marziani@fe.infn.it>
- Merged spec file with that from RedHat-5.0 distribution
  (now a Hurricane-based distribution is needed)
- Added patch for RPM script (didn't always work with rpm-2.4.10)
- Corrected patch for mcserv init file (chkconfig init levels)
- Added more documentation files on termcap, terminfo, xterm

* Thu Oct 30 1997 Michael K. Johnson <johnsonm@redhat.com>

- Added dependency on portmap

* Wed Oct 29 1997 Michael K. Johnson <johnsonm@redhat.com>

- fixed spec file.
- Updated to 4.1.8

* Sun Oct 26 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>

- updated to 4.1.6
- added %attr macros in %files,
- a few simplification in %install,
- removed glibc patch,
- fixed installing /etc/X11/wmconfig/tkmc.

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>

- updated to 4.1.5
- added wmconfig

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>

- chkconfig is for mcserv package, not mc one

* Tue Oct 14 1997 Erik Troan <ewt@redhat.com>

- patched init script for chkconfig
- don't turn on the service by default

* Fri Oct 10 1997 Michael K. Johnson <johnsonm@redhat.com>

- Converted to new PAM conventions.
- Updated to 4.1.3
- No longer needs glibc patch.

* Thu May 22 1997 Michele Marziani <marziani@fe.infn.it>

- added support for mc alias in /etc/profile.d/mc.csh (for csh and tcsh)
- lowered number of SysV init scripts in /etc/rc.d/rc[0,1,6].d
  (mcserv needs to be killed before inet)
- removed all references to $RPM_SOURCE_DIR
- restored $RPM_OPT_FLAGS when compiling
- minor cleanup of spec file: redundant directives and comments removed

* Sun May 18 1997 Michele Marziani <marziani@fe.infn.it>

- removed all references to non-existent mc.rpmfs
- added mcedit.1 to the %files section
- reverted to un-gzipped man pages (RedHat style)
- removed double install line for mcserv.pamd

* Tue May 13 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>

- added new rpmfs script,
- removed mcfn_install from mc (adding mc() to bash enviroment is in
  /etc/profile.d/mc.sh),
- /etc/profile.d/mc.sh changed to %config,
- removed %{prefix}/lib/mc/bin/create_vcs,
- removed %{prefix}/lib/mc/term.

* Wed May 9 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>

- changed source url,
- fixed link mcedit to mc,

* Tue May 7 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>

- new version 3.5.27,
- %dir %{prefix}/lib/mc/icons and icons removed from tkmc,
- added commented xmc part.

* Tue Apr 22 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>

- FIX spec:
   - added URL field,
   - in mc added missing %{prefix}/lib/mc/mc.ext, %{prefix}/lib/mc/mc.hint,
     %{prefix}/lib/mc/mc.hlp, %{prefix}/lib/mc/mc.lib, %{prefix}/lib/mc/mc.menu.

* Fri Apr 18 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>

- added making packages: tkmc, mcserv (xmc not work yet),
- gziped man pages,
- added /etc/pamd.d/mcserv PAM config file.
- added instaling icons,
- added /etc/profile.d/mc.sh,
- in %doc added NEWS README,
- removed %{prefix}/lib/mc/FAQ,
- added mcserv.init script for mcserv (start/stop on level 86).
