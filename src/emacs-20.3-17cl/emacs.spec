Summary: The libraries needed to run the GNU Emacs text editor.
Summary(pt_BR): GNU Emacs
Summary(es): GNU Emacs
Name: emacs
%define	version	20.3
Version: %{version}
Release: 17cl
Copyright: GPL
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Source0: ftp://ftp.gnu.org/pub/gnu/emacs-%{version}.tar.gz
Source1: ftp://ftp.gnu.org/pub/gnu/leim-%{version}.tar.gz
Source2: emacs.wmconfig
Source3: mh-utils.elc
Source800: emacs-wmconfig.i18n.tgz
Patch0: emacs-20.3-gnu.patch
Patch1: emacs-20.2-xaw3d.patch
Patch2: emacs-20.2-gctags.patch
# patch4 (signal patch) not needed for emacs > 20.2
Patch4: emacs-20.2-signal.patch
Patch5: emacs-20.3-tmprace.patch
Patch6: emacs-20.3-ufix.patch
Patch7: emacs-armconfig.patch
Patch8: emacs-20.3-linkscr.patch
Patch9: emacs-20.3-nmhlocation.patch
Patch10: emacs-20.3-dxpc.patch
Buildroot: /var/tmp/%{name}-root
#
# more info on multibyte support: http://sourcery.naggum.no/emacs/
#

%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news and more without
leaving the editor.

This package includes the libraries you need to run the Emacs editor, so
you need to install this package if you intend to use Emacs.  You also
need to install the actual Emacs program package (emacs-nox or emacs-X11).
Install emacs-nox if you are not going to use the X Window System; install
emacs-X11 if you will be using X.

%description -l pt_BR
Emacs é um editor comum, personalizável, e mostra os próprios
documentos em tempo real. Emacs possui um modo de código especial
para edição, uma linguagem script (elisp), e vem com vários pacotes
para mail, news, e mais, tudo no seu editor.  Este pacote inclui
as bibliotecas necessárias para rodar o editor emacs - o programa
atual pode ser achado nos pacotes emacs-nox ou emacs-X11, dependendo
se você usa ou não X Window.

%description -l es
Emacs es un editor común, que se puede personalizar, y muestra los
propios documentos en tiempo real. Emacs posee un modo de código
especial para edición, un lenguaje script (elisp), y viene con
varios paquetes para mail, news, y más cosas, todo en tu editor. Este
paquete incluye las bibliotecas necesarias para ejecutar el editor
emacs - el programa actual puede ser encontrado en los paquetes
emacs-nox o emacs-X11, dependiendo de que uses o no el X Window.

%package el
Summary: The sources for elisp programs included with Emacs.
Summary(pt_BR): Fontes .el -- não são necessários para rodar o emacs
Summary(es): Fuentes .el -- no son necesarios para ejecutar emacs
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Requires: emacs

%description el
Emacs-el contains the emacs-elisp sources for many of the elisp
programs included with the main Emacs text editor package.

You need to install emacs-el only if you intend to modify any of the
Emacs packages or see some elisp examples.

%description -l pt_BR el
Este pacote contém os fontes emacs-lisp para muitos dos programas
elisp incluído com o programa principal do pacote emacs. Você não
necessita deste pacote a menos que você queira modificar estes
pacotes ou ver alguns exemplos de programas elisp.

%description -l es el
Este paquete contiene los fuentes emacs-lisp para muchos de los
programas elisp incluido en el programa principal del paquete
emacs. Tu no necesitas de este paquete a menos que quieras
modificarlos o mirar algunos ejemplos de programas elisp.

%package leim
Summary: Emacs Lisp code for input methods for internationalization.
Summary(pt_BR): Código Lisp para para internacionalização no Emacs
Summary(es): Emacs Lisp code for input methods for internationalization.
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Requires: emacs

%description leim
The Emacs Lisp code for input methods for various international
character scripts.

%description -l pt_BR leim
Código Lisp para para internacionalização no Emacs.

%description -l es leim
The Emacs Lisp code for input methods for various international
character scripts.

%package nox
Summary: The Emacs text editor without support for the X Window System.
Summary(pt_BR): Emacs-nox -- emacs sem precisar de bibliotecas X
Summary(es): Emacs-nox -- emacs sin necesidad de bibliotecas X
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Requires: emacs

%description nox
Emacs-nox is the Emacs text editor program without support for
the X Window System.

You need to install this package only if you plan on exclusively using
Emacs without the X Window System (emacs-X11 will work both in X and out
of X, but emacs-nox will only work outside of X).  You'll also need to
install the emacs package in order to run Emacs.

%description -l pt_BR nox
Este pacote contém um binário emacs sem suporte ao X Window. Embora
o binário emacs no pacote principal funcione bem fora do X Window (na
console por exemplo) o que está neste pacote utiliza menos memória.

%description -l es nox
Este paquete contiene un binario emacs sin soporte al X
Window. Aunque el binario emacs, en el paquete principal, funcione
bien fuera del X Window (en la consola, por ejemplo) lo que se
encuentra en este paquete utiliza menos memoria.

%package X11
Summary: The Emacs text editor for the X Window System.
Summary(pt_BR): Emacs-X11 -- emacs com bibliotecas X-Windows
Summary(es): Emacs-X11 -- emacs con bibliotecas X-Windows
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Requires: emacs

%description X11
Emacs-X11 includes the Emacs text editor program for use with the
X Window System (it provides support for the mouse and other GUI
elements). Emacs-X11 will also run Emacs outside of X, but it has
a larger memory footprint than the 'non-X' Emacs package
(emacs-nox).

Install emacs-X11 if you're going to use Emacs with the X Window System.
You should also install emacs-X11 if you're going to run Emacs both
with and without X (it will work fine both ways). You'll also need to
install the emacs package in order to run Emacs.

%description -l pt_BR X11
Este pacote contém um binário emacs com suporte ao X Window. Ele
funciona bem fora do X Window (na console por exemplo) porém suporta
mouse e elementos GUI quando utilizado no X Window.

%description -l es X11
Este paquete contiene un binario emacs con soporte al X
Window. Funciona bien fuera del X Window (en la consola, por ejemplo)
pero soporta ratón y elementos GUI cuando utilizado en el X Window.

%prep
%setup -q -b 1
cp -f $RPM_SOURCE_DIR/mh-utils.elc lisp/mail

%patch0 -p1
%patch1 -p1
%patch2 -p1
# patch4 (signal patch) not needed for emacs > 20.2
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p2

# clean out remnants of patching
find . -name "*.orig" -exec rm -f {} \;

%build
PUREDEF=""
XPUREDEF=""
libtoolize --force --copy
CONFOPTS="--prefix=/usr --libexecdir=/usr/lib --sharedstatedir=/var --with-gcc --with-pop"

#Build binary without X support
[ -d build-nox ] && rm -rf build-nox
mkdir build-nox && cd build-nox
CFLAGS="$RPM_OPT_FLAGS -g -O0 $PUREDEF" LDFLAGS=-s \
  ../configure ${CONFOPTS} --with-x=no ${RPM_ARCH}-conectiva-linux
make
cd ..

#Build binary with X support
[ -d build-withx ] && rm -rf build-withx
mkdir build-withx && cd build-withx
CFLAGS="$RPM_OPT_FLAGS -g -O0 $XPUREDEF" LDFLAGS=-s \
  ../configure ${CONFOPTS} --with-x-toolkit ${RPM_ARCH}-conectiva-linux
make 
cd ..

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

ARCHDIR=${RPM_ARCH}-conectiva-linux
make install -C build-withx \
	prefix=$RPM_BUILD_ROOT/usr \
	libexecdir=$RPM_BUILD_ROOT/usr/lib \
	sharedstatedir=$RPM_BUILD_ROOT/var

rm -f $RPM_BUILD_ROOT/usr/info/dir
gzip -9nf $RPM_BUILD_ROOT/usr/info/*
install -m755 build-nox/src/emacs $RPM_BUILD_ROOT/usr/bin/emacs-nox

# For some reason, when emacs is stripped on the Alpha, it dumps core
# Lucky for us it started doing this on the Intel as well. Yeah.
#strip $RPM_BUILD_ROOT/usr/bin/* ||:
for I in cvtmail digest-doc emacsserver fakemail hexl movemail profile \
	sorted-doc timer wakeup yow; do
	strip $RPM_BUILD_ROOT/usr/lib/emacs/$RPM_PACKAGE_VERSION/$ARCHDIR/$I||:
done

chown root.mail $RPM_BUILD_ROOT/usr/lib/emacs/$RPM_PACKAGE_VERSION/$ARCHDIR/movemail
chmod 2755 $RPM_BUILD_ROOT/usr/lib/emacs/$RPM_PACKAGE_VERSION/$ARCHDIR/movemail

mkdir -p $RPM_BUILD_ROOT/usr/lib/emacs/site-lisp

mv $RPM_BUILD_ROOT/usr/man/man1/ctags.1 $RPM_BUILD_ROOT/usr/man/man1/gctags.1
mv $RPM_BUILD_ROOT/usr/bin/ctags $RPM_BUILD_ROOT/usr/bin/gctags

# wmconfig file
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 0644 $RPM_SOURCE_DIR/emacs.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/emacs

#
# create file lists
#

find $RPM_BUILD_ROOT/usr/share/emacs/%{PACKAGE_VERSION}/lisp \
  -name '*.elc' -print | sed "s^$RPM_BUILD_ROOT^^" > elc-filelist
find $RPM_BUILD_ROOT/usr/lib/emacs/%{PACKAGE_VERSION} -type f | \
    sed "s^$RPM_BUILD_ROOT^^" | grep -v movemail >> elc-filelist

find $RPM_BUILD_ROOT/usr/share/emacs/%{PACKAGE_VERSION}/leim \
  -name '*.elc' -print | sed "s^$RPM_BUILD_ROOT^^" > leim-filelist

#
# be sure to exclude some files which are need in core package
#
find $RPM_BUILD_ROOT/usr/share/emacs/%{PACKAGE_VERSION}/lisp \
  -name '*.el' -print | sed "s^$RPM_BUILD_ROOT^^" |\
  grep -v "international\/latin-[0-9]*.el" > el-filelist

find $RPM_BUILD_ROOT/usr/share/emacs/%{PACKAGE_VERSION}/leim \
  -name '*.el' -print | sed "s^$RPM_BUILD_ROOT^^" |\
  grep -v "leim\/leim-list.el" >> el-filelist





tar xvfpz $RPM_SOURCE_DIR/emacs-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf build-nox
rm -rf build-withx

%post
/sbin/install-info /usr/info/ccmode.gz /usr/info/dir --entry="* CC mode: (ccmode).    The GNU Emacs mode for editing C, C++, Objective-C and Java code." --section="Emacs"
/sbin/install-info /usr/info/ediff.gz /usr/info/dir --entry="* Ediff: (ediff).       A comprehensive visual interface to diff & patch." --section="Emacs"
/sbin/install-info /usr/info/dired-x.gz /usr/info/dir --entry="* Dired-X: (dired-x).   Dired Extra Features." --section="Emacs"
/sbin/install-info /usr/info/sc.gz /usr/info/dir --entry="* SC: (sc).             Supercite lets you cite parts of messages you're replying to, in flexible ways." --section="Emacs"
/sbin/install-info /usr/info/cl.gz /usr/info/dir --entry="* CL: (cl).             Partial Common Lisp support for Emacs Lisp." --section="Emacs"
/sbin/install-info /usr/info/mh-e.gz /usr/info/dir --entry="* MH-E: (mh-e).         Emacs interface to the MH mail system." --section="Emacs"
/sbin/install-info /usr/info/message.gz /usr/info/dir --entry="* Message: (message).   Mail and news composition mode that goes with Gnus." --section="Emacs"
/sbin/install-info /usr/info/gnus.gz /usr/info/dir --entry="* Gnus: (gnus).         The news reader Gnus." --section="Emacs"
/sbin/install-info /usr/info/forms.gz /usr/info/dir --entry="* Forms: (forms).       Emacs package for editing data bases by filling in forms." --section="Emacs"
/sbin/install-info /usr/info/viper.gz /usr/info/dir --entry="* VIPER: (viper).       The new VI-emulation mode in Emacs-19.29." --section="Emacs"
/sbin/install-info /usr/info/vip.gz /usr/info/dir --entry="* VIP: (vip).           A VI-emulation for Emacs." --section="Emacs"
/sbin/install-info /usr/info/emacs.gz /usr/info/dir --entry="* Emacs: (emacs).       The extensible self-documenting text editor." --section="Emacs"
/sbin/install-info /usr/info/info.gz /usr/info/dir --entry="* Info: (info).         Documentation browsing system." --section="Emacs"
/sbin/install-info /usr/info/reftex.gz /usr/info/dir --entry="* RefTeX: (reftex).         Manage labels, references, and citations with Emacs." --section="Emacs"
/sbin/install-info /usr/info/widget.gz /usr/info/dir --entry="* Widget: (widget).         Emacs widget library." --section="Emacs"
/sbin/install-info /usr/info/customize.gz /usr/info/dir --entry="* Customize: (customize).         Declaring customization items." --section="Emacs"

%preun
if [ "$1" = 0 ]; then
/sbin/install-info --delete /usr/info/ccmode.gz /usr/info/dir --entry="* CC mode: (ccmode).    The GNU Emacs mode for editing C, C++, Objective-C and Java code." --section="Emacs"
/sbin/install-info --delete /usr/info/ediff.gz /usr/info/dir --entry="* Ediff: (ediff).       A comprehensive visual interface to diff & patch." --section="Emacs"
/sbin/install-info --delete /usr/info/dired-x.gz /usr/info/dir --entry="* Dired-X: (dired-x).   Dired Extra Features." --section="Emacs"
/sbin/install-info --delete /usr/info/sc.gz /usr/info/dir --entry="* SC: (sc).             Supercite lets you cite parts of messages you're replying to, in flexible ways." --section="Emacs"
/sbin/install-info --delete /usr/info/cl.gz /usr/info/dir --entry="* CL: (cl).             Partial Common Lisp support for Emacs Lisp." --section="Emacs"
/sbin/install-info --delete /usr/info/mh-e.gz /usr/info/dir --entry="* MH-E: (mh-e).         Emacs interface to the MH mail system." --section="Emacs"
/sbin/install-info --delete /usr/info/message.gz /usr/info/dir --entry="* Message: (message).   Mail and news composition mode that goes with Gnus." --section="Emacs"
/sbin/install-info --delete /usr/info/gnus.gz /usr/info/dir --entry="* Gnus: (gnus).         The news reader Gnus." --section="Emacs"
/sbin/install-info --delete /usr/info/forms.gz /usr/info/dir --entry="* Forms: (forms).       Emacs package for editing data bases by filling in forms." --section="Emacs"
/sbin/install-info --delete /usr/info/viper.gz /usr/info/dir --entry="* VIPER: (viper).       The new VI-emulation mode in Emacs-19.29." --section="Emacs"
/sbin/install-info --delete /usr/info/vip.gz /usr/info/dir --entry="* VIP: (vip).           A VI-emulation for Emacs." --section="Emacs"
/sbin/install-info --delete /usr/info/emacs.gz /usr/info/dir --entry="* Emacs: (emacs).       The extensible self-documenting text editor." --section="Emacs"
/sbin/install-info --delete /usr/info/info.gz /usr/info/dir --entry="* Info: (info).         Documentation browsing system." --section="Emacs"
/sbin/install-info /usr/info/reftex.gz /usr/info/dir --entry="* RefTeX: (reftex).         Manage labels, references, and citations with Emacs." --section="Emacs"
/sbin/install-info --delete /usr/info/widget.gz /usr/info/dir --entry="* Widget: (widget).         Emacs widget library." --section="Emacs"
/sbin/install-info --delete /usr/info/customize.gz /usr/info/dir --entry="* Customize: (customize).         Declaring customization items." --section="Emacs"
fi

%files -f elc-filelist
%defattr(-,root,root)
%doc etc/NEWS BUGS README etc/FAQ
/usr/bin/b2m
/usr/bin/emacsclient
/usr/bin/etags
/usr/bin/gctags
/usr/bin/rcs-checkin
/usr/man/*/*
/usr/info/*
#%dir /var/lock/emacs

%dir /usr/lib/emacs
%attr(2755,root,mail) /usr/lib/emacs/%{PACKAGE_VERSION}/%{_target_cpu}-conectiva-linux/movemail
%dir /usr/lib/emacs/site-lisp

%dir /usr/share/emacs/site-lisp
%dir /usr/share/emacs/%{PACKAGE_VERSION}
%dir /usr/share/emacs/%{PACKAGE_VERSION}/site-lisp
%dir /usr/share/emacs/%{PACKAGE_VERSION}/leim
%dir /usr/share/emacs/%{PACKAGE_VERSION}/lisp
%dir /usr/share/emacs/%{PACKAGE_VERSION}/lisp/term
/usr/share/emacs/%{PACKAGE_VERSION}/etc

# handled by dynamically generated file lists
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*.elc
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*/*.elc
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*.elc
#/usr/share/emacs/20.2/lisp/mail/*.elc

/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/README
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/AT386.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/bobcat.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/internal.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/keyswap.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/lk201.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt102.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt125.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt201.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt220.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt240.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt300.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt320.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt400.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term/vt420.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/COPYING
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/forms-d2.dat
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/README
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/mail/blessmail.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/forms-d2.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/forms-pass.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/loaddefs.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/loadup.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/patcomp.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/paths.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/mail/sc.el
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/term-nasty.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/version.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/subdirs.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-1.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-2.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-3.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-4.el
/usr/share/emacs/%{PACKAGE_VERSION}/lisp/international/latin-5.el

%files -f el-filelist el
%defattr(-,root,root)
# handled by dynamically generated file lists
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*.el
#/usr/share/emacs/%{PACKAGE_VERSION}/lisp/*/*.el
#/usr/share/emacs/%{PACKAGE_VERSION}/leim/*.el
#/usr/share/emacs/%{PACKAGE_VERSION}/leim/*/*.el

%files -f leim-filelist leim
%defattr(-,root,root)
/usr/share/emacs/%{PACKAGE_VERSION}/leim/leim-list.el
# handled by dynamically generated file lists
#/usr/share/emacs/%{PACKAGE_VERSION}/leim/*.elc
#/usr/share/emacs/%{PACKAGE_VERSION}/leim/*/*.elc

%files nox
%defattr(-,root,root)
/usr/bin/emacs-nox

%files X11
%defattr(-,root,root)
/usr/bin/emacs
/usr/bin/emacs-%{version}
%config(missingok) /etc/X11/wmconfig/emacs

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Injected new groups into packages
- Revised summaries and descriptions of packages

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 16 1999 Owen Taylor <otaylor@redhat.com>
- replace bad xemacs compiled .elc file for mh-e with one compiled
  on emacs

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- make sure movemail doesn't get %defattr()'d to root.root

* Wed Apr 14 1999 Cristian Gafton <gafton@redhat.com>
- patch to make it work with dxpc

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- updated mh-utils emacs lisp file to match our nmh path locations

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 9)

* Fri Feb 26 1999 Cristian Gafton <gafton@redhat.com>
- linker scripts hack to make it build on the alpha

* Fri Jan  1 1999 Jeff Johnson <jbj@redhat.com>
- add leim package (thanks to Pavel.Janik@inet.cz).

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- backed up changes to uncompress.el (it seems that the one from 20.2 works
  much better)

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- eliminate /tmp race in rcs2log

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to 20.3

* Tue Jun  9 1998 Jeff Johnson <jbj@redhat.com>
- add --with-pop to X11 compile.
- include contents of /usr/share/.../etc with main package.

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Mon Jun 01 1998 David S. Miller <davem@dm.cobaltmicro.com>
- fix signals when linked with glibc on non-Intel architectures
  NOTE: This patch is not needed with emacs >20.2

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- added /usr/lib/emacs/20.2/*-redhat-linux directory in the filelist

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- alpha started to like emacs-nox again :-)

* Thu Nov  6 1997 Michael Fulbright <msf@redhat.com>
- alpha just doesnt like emacs-nox, taking it out for now

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- added multibyte support back into emacs 20.2
- added wmconfig for X11 emacs
- fixed some errant buildroot references

* Thu Oct 23 1997 Michael Fulbright <msf@redhat.com>
- joy a new version of emacs! Of note - no lockdir any more.
- use post/preun sections to handle numerous GNU info files

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- stopped stripping it as it seems to break things

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- turned off ecoff support on the Alpha (which doesn't build anymore)

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved ctags to gctags to fit in the more powerful for C (but less
  general) exuberant ctags as the binary /usr/bin/ctags and the
  man page /usr/man/man1/ctags.1
