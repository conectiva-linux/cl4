Summary: An improved version of the FVWM X-based window manager.
Summary(pt_BR): Gerente de Janelas semelhante ao Windows'95
Summary(es): Administrador de Ventanas semejante al Windows'95
Name: fvwm2
Version: 2.2
Release: 8cl
# was .gz
Source0: ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-2.2.tar.bz2
Source1: fvwm-2.0.46.icons.tar.bz2
Source2: compat-icons.tar.gz
Patch0: fvwm-2.2-redhat.patch
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Buildroot: /var/tmp/fvwm2-root
Requires: wmpixmaps
Url: http://fvwm.math.uh.edu/
Obsoletes: fvwm95

%description
FVWM2 (the F stands for whatever you want, but the VWM stands for
Virtual Window Manager) is an improved version of the FVWM window
manager for the X Window System and shares the same characteristics as
FVWM.  

Install the fvwm2 package if you'd like to use the FVWM2 window manager.
If you install fvwm2, you'll also need to install fvwm2-icons.

%description -l pt_BR
Fvwm2 é uma versão do popular gerenciador de janelas "Feeble Virtual
Window Manager".

%description -l es
Fvwm2 es una versión del popular administrador de ventanas "Feeble
Virtual Window Manager".

%prep
%setup -n fvwm-%{version} -q
%patch0 -p1 -b .redhat

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6 --enable-extras \
	--libexecdir=\${prefix}/lib/X11/fvwm2	\
	--sysconfdir=/etc/X11/fvwm2
make 

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	sysconfdir=$RPM_BUILD_ROOT/etc/X11/fvwm2 \
	INSTALL_PROGRAM="/usr/bin/install -c -s"
mkdir -p $RPM_BUILD_ROOT/etc/X11/fvwm2
install -m 644 sample.fvwmrc/system.fvwm2rc $RPM_BUILD_ROOT/etc/X11/fvwm2
rm -rf $RPM_BUILD_ROOT/usr/share/icons

%files
%defattr(-,root,root)
%doc INSTALL README AUTHORS INSTALL.fvwm NEWS ChangeLog
%doc docs
/usr/X11R6/lib/X11/fvwm2
/usr/X11R6/man/man1/*
/usr/X11R6/bin/*
%dir /etc/X11/fvwm2
%config /etc/X11/fvwm2/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- removed icons package (all files conflicts with wmpixmaps and others)

* Sat Jun 12 1999 Conectiva <dist@conectiva.com>
- some icons have gone to wmpixmaps
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 09 1999 Preston Brown <pbrown@redhat.com> 
- added some icons from kdebase back to this package for upgrade
- compatibility.

* Wed Mar 24 1999 Bill Nottingham <notting@redhat.com>
- don't require xterm-color

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- better default system.fvwm2rc

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Feb 26 1999 Cristian Gafton <gafton@redhat.com>
- package is still not finished yet
- upgraded to 2.2, got rid of all the cruft in the spec file

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.0.47
- mark config files as %config files

* Mon Jun 29 1998 Michael Maher <mike@redhat.com>
- removed duplicate files found in the package Another level.
- fixes bug: 651 

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- long time no new version released :-(. -> misc patch
- major spec file cleanups

* Mon Nov 03 1997 Cristian Gafton <gafton@redhat.com>
- Fixed more bugs (bugs patch)

* Fri Oct 24 1997 Cristian Gafton <gafton@redhat.com>
- fixed Alpha build

* Thu Oct 16 1997 Cristian Gafton <gafton@redhat.com>
- fixed FvwmTaskBar severe bug (taskbar patch)
- misc fixes

* Mon Oct 13 1997 Cristian Gafton <gafton@redhat.com>
- built against glibc; added -rh and -fixes patches

