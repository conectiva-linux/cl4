Summary: An easy to use, modeless text editor.
Summary(pt_BR): Editor fácil de usar
Summary(es): Editor fácil de usar
Name: joe
Version: 2.8
Release: 20cl
Copyright: GPL
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Source: ftp://ftp.std.com/src/editors/joe2.8.tar.bz2
Patch0: joe2.8-config.patch
Patch1: joe2.8-time.patch
Patch2: joe2.8-axphack.patch
Patch3: joe2.8-make.patch
Patch4: joe2.8-locale.patch
Patch5: joe-2.8-port.patch
Patch6: joe-2.8-mips.patch
Buildroot: /var/tmp/%{name}-root

%description
Joe is an easy to use, modeless text editor which would be very
appropriate for novices.  Joe uses the same WordStar keybindings used in
Borland's development environment.

You should install joe if you've used it before and you liked it, or if
you're still deciding what text editor you'd like to use, or if you have a
fondness for WordStar.  If you're just starting out, you should probably
install joe because it is very easy to use.

%description -l pt_BR
Joe é um editor amigável e fácil de usar. Possui uma boa interface e
seria a melhor opção para um novato precisando de um editor. Ele usa
a mesma combinação de teclas do WordStar que também são utilizadas
pelo ambiente de desenvolvimento da Borland.

%description -l es
Joe es un editor amigable y fácil de usar. Posee una buena interface
y sería la mejor opción para un principiante que necesite de
un editor.  Usa la misma combinación de teclas del WordStar, que
también son utilizadas por el ambiente de desarrollo de la Borland.

%prep
%setup -q -n joe
%patch0 -p1 -b .config
%patch1 -p1 -b .time

%ifarch axp
%patch2 -p1 -b .axp
%endif

%patch3 -p1 -b .make
%patch4 -p0 -b .locale

%patch5 -p1 -b .port

%ifarch mipsel mipseb
%patch6 -p1 -b .mips
%endif

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DUSE_LOCALE"

%install
rm -rf $RPM_BUILD_ROOT
make install TOPDIR=$RPM_BUILD_ROOT
 
%files
%defattr(-,root,root)
/usr/bin/*
%dir /usr/lib/joe 
%config /usr/lib/joe/*
/usr/man/man1/joe.1

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun May 16 1999 Jeff Johnson <jbj@redhat.com>
- don't rely on (broken!) rpm %patch (#2735)

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- added locale patch from  Petr Kolar <PETR.KOLAR@vslib.cz>
  (yeah, finally!)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 17)

* Wed Jan 20 1999 Alex deVries <puffin@redhat.com>
- added mipseb support

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Sep 15 1998 Cristian Gafton <gafton@redhat.com>
- built with Alan's -port patch

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- enable -asis in the config files so international keyboards will be better
  supported

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- /usr/lib/joe/* are config files

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- manhattan build

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- fixed termcap problems for terms other than 80x25
- added support for buildroot and BuildRoot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

