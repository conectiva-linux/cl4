Summary: An X Window System based file manager.
Summary(pt_BR): Gerenciador de arquivos
Summary(es): Administrador de archivos
Name: xfm
Version: 1.3.2
Release: 14cl
Copyright: freeware
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source0: ftp://ftp.x.org/contrib/applications/xfm-1.3.2.tar.gz
Source1: xfm.wmconfig
Source800: xfm-wmconfig.i18n.tgz
Patch0: xfm-1.3.2-nobr.patch
Patch1: xfm-1.3.2-flags.patch
Patch2: xfm-1.3.2-string.patch
BuildRoot: /var/tmp/xfm-root

%description
Xfm is a file manager for the X Window System.  Xfm supports moving
around the directory tree, multiple windows, moving/copying/deleting
files, and launching programs.

Install xfm if you would like to use a graphical file manager program.

%description -l pt_BR
O xfm é um gerenciador de arquivos para X Window que permite
manipular arquivos e diretórios de uma maneira intuitiva e fácil
de entender, assim como permite sua extensão com outros programas.

%description -l es
xfm es un administrador de archivos para X Window que permite
manipular archivos y directorios de una manera intuitiva y fácil
de entender, así como permite su extensión con otros programas.

%prep
%setup -q
%patch0 -p1 -b .nobr
%patch1 -p1 -b .flags
%patch2 -p1 -b .string

%build
xmkmf
make Makefiles
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man
install -m644 $RPM_SOURCE_DIR/xfm.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/xfm


tar xvfpz $RPM_SOURCE_DIR/xfm-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc MANIFEST COPYING ChangeLog README README-1.2
%config /etc/X11/wmconfig/xfm
/usr/X11R6/bin/xfm
/usr/X11R6/bin/xfmtype
/usr/X11R6/bin/xfm.install
%config /usr/X11R6/lib/X11/app-defaults/Xfm
%dir /usr/X11R6/lib/X11/xfm
/usr/X11R6/lib/X11/xfm/dot.xfm
/usr/X11R6/lib/X11/xfm/bitmaps
/usr/X11R6/lib/X11/xfm/pixmaps
/usr/X11R6/man/man1/xfm.1x
/usr/X11R6/man/man1/xfmtype.1x

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 13)

* Thu Feb 25 1999 Bill Nottingham <notting@redhat.com>
- new summary/descriptions
- club with glibc2.1 stick

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- removed the old config stuff we had since 2.1 :-)
- spec file cleanups

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
