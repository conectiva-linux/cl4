Summary: SANE -- Easy local and networked scanner access
Summary(pt_BR): SANE - acesso a scanners locais e em rede
Summary(es): SANE -- Easy local and networked scanner access
Name: sane
Version: 1.0.1
Release: 2cl
URL: http://www.mostang.com/sane/
Source:	ftp://ftp.mostang.com/pub/sane/%{name}-%{version}.tar.bz2
Copyright: GPL (programs), relaxed LGPL (libraries), and public domain (docs)
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Icon: sane.xpm
Provides: libsane.so.1
Requires: gtk+ >= 0.99.13
Buildroot: /var/tmp/%{name}-%{version}-root

%description
SANE (Scanner Access Now Easy) is a sane and simple interface
to both local and networked scanners and other image acquisition devices
like digital still and video cameras.  SANE currently includes modules for
accessing a range of scanners, including models from Agfa SnapScan, Apple,
Artec, Canon, CoolScan, Epson, HP, Microtek, Mustek, Nikon, Siemens,
Tamarack, UMAX, Connectix, QuickCams and other SANE devices via network.

For the latest information on SANE, the SANE standard definition, and
mailing list access, see http://www.mostang.com/sane/

This package does not enable network scanning by default; if you wish
to enable it, read the saned(1) manpage.

%description -l pt_BR
O SANE (Scanner Access Now Easy) é uma interface simples para scanners e outros
dispositivos de captura de imagens como câmeras fotográficas digitais e de vídeo
conectados diretamente ou através da rede.

%description -l es
SANE (Scanner Access Now Easy) is a sane and simple interface
to both local and networked scanners and other image acquisition devices
like digital still and video cameras.  SANE currently includes modules for
accessing a range of scanners, including models from Agfa SnapScan, Apple,
Artec, Canon, CoolScan, Epson, HP, Microtek, Mustek, Nikon, Siemens,
Tamarack, UMAX, Connectix, QuickCams and other SANE devices via network.

For the latest information on SANE, the SANE standard definition, and
mailing list access, see http://www.mostang.com/sane/

This package does not enable network scanning by default; if you wish
to enable it, read the saned(1) manpage.

%package devel
Summary: SANE (Scanner Access Now Easy) development toolkit
Summary(pt_BR): Arquivos necessários ao desenvolvimento de programas que usem o SANE.
Summary(es): SANE (Scanner Access Now Easy) development toolkit
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: %{name} = %{version}

%description devel
Static libraries and header files for writing SANE modules.

%description -l pt_BR devel
Arquivos necessários ao desenvolvimento de programas que usem o SANE.

%description -l es devel
Static libraries and header files for writing SANE modules.

%package clients
Summary:  SANE (Scanner Access Now Easy) clients 
Summary(pt_BR): Clientes para o SANE
Summary(es): SANE (Scanner Access Now Easy) clients 
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Requires: %{name} = %{version}

%description clients
The clients that use the SANE modules.


%description -l pt_BR clients
Cliente que usam os módulos do SANE.

%description -l es clients
The clients that use the SANE modules.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s \
./configure --with-gnu-ld \
            --prefix=/usr \
            --sysconfdir=/etc

make

( cd doc
  install -d /home/httpd/html/sane
  make docs
  rm -rf /home/httpd/html/sane
)

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc install
mv $RPM_BUILD_ROOT/usr/sbin/saned $RPM_BUILD_ROOT/usr/sbin/in.saned
install -m755 tools/find-scanner $RPM_BUILD_ROOT/usr/bin

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/sane/lib*.so.*.*,sbin/*} ||

%post
/sbin/ldconfig
if [ -d /usr/lib/gimp ]; then
  GIMPDIR=`ls -d /usr/lib/gimp/[01]*`
  ln -sf /usr/bin/xscanimage $GIMPDIR/plug-ins/xscanimage
fi

%preun
if [ $1 = 0 ]; then
  if [ -d /usr/lib/gimp ]; then
    GIMPDIR=`ls -d /usr/lib/gimp/[01]*`
    rm -f $GIMPDIR/plug-ins/xscanimage
  fi
fi

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS NEWS doc/*.ps doc/sane doc/icons
%dir /etc/sane.d
%config /etc/sane.d/*
/usr/sbin/*
/usr/lib/lib*.so.*
/usr/lib/lib*.so
/usr/lib/sane/lib*.so.*
/usr/lib/sane/lib*.so
%dir /usr/lib/sane
%config /usr/share/sane-style.rc
%attr(-,root,man) /usr/man/man1/saned.1
%attr(-,root,man) /usr/man/man5/*.5

%files devel
%defattr(-,root,root)
/usr/include/sane
/usr/lib/lib*.a
%dir /usr/lib/sane
/usr/lib/sane/lib*.a

%files clients
/usr/bin/scanimage
/usr/man/man1/scanimage.1
/usr/bin/xscanimage
/usr/man/man1/xscanimage.1
/usr/bin/xcam

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added to Conectiva Linux

* Fri Apr 23 1999 Hugo van der Kooij <hvdkooij@caiw.nl>
- Fixed packaging a bit.

* Wed Apr 21 1999 Hugo van der Kooij <hvdkooij@caiw.nl>
- Updated package to 1.01

* Fri Apr 09 1999 Hugo van der Kooij <hvdkooij@caiw.nl>
- Split off the clients
- Fixed a Alpha system anomaly by removing the specific backend.

* Mon Nov 23 1998 Jonathan Miller <jlm@mvhi.com>
 [1.00-1]
- upgraded to 1.00 (and made description less space-consuming)
- included the post 1.00 fixed "configure" script available 22 Nov 1998.

* Sat Aug 08 1998 Arne Coucheron <arneco@online.no>
  [0.74-3]
- added /etc/sane.d to %dir in file list

* Sat Aug 01 1998 Arne Coucheron <arneco@online.no>
  [0.74-2]
- devel Group: reverted back to Development/Libraries
- some changes to the %defattr and %attr usage in file list

* Tue Jul 28 1998 Binaire <binaire@binaire.ml.org>
  [0.74-1]

* Fri May 22 1998 Arne Coucheron <arneco@online.no>
  [0.73-3]
- added use of %%{name} and %%{version} macros
- added a %postun for running ldconfig after uninstall
- using BuildRoot properly now
- using %defattr and %attr macros in filelist, allows non-root build 
  this means that RPM 2.5 is required to build this spec file now!
- devel Group: changed to X11/Libraries
- added using RPM_OPT_FLAGS during make 
- added striping of programs and libraries
- added Requires: gtk+ >= 0.99.13 to main package
- added Requires: %%{name} = %%{version} to devel package
- added a %clean section for removing the buildroot dir
- simplified the filelist and added %config for sane-style.rc
- moved lib*.so to %files devel and dropped the *.la files
- added -q parameter to %setup
- removed some older changelog entries
- removed the "fix ldconfig brokenness..." stuff
- removed the Packager: line; use /etc/rpmrc if you want your name in
- if GIMP is installed, make symlink from xscanimage to plug-ins dir
- install the find-scanner program from the tools dir

* Mon May 18 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Version 0.73 was created: May 13 1998
- gimp (original was build against 0.99.29)
- gtk+ (original was build against 1.0.1)
- dlh (original was build against 0.7d)
- X11 development tree including xpm libraries.

* Wed Apr 22 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Binaries are now BuildRoot proof.

* Wed Apr 22 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Binaries are not BuildRoot proof. release 3 is done without BuildRoot!

* Tue Apr 21 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Temp. fix for some documentations problems with BuildRoot.

* Sat Apr 11 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Formal 0.72 now made as RPM! (Build against GTK+ 0.99.10 and GIMP 0.99.24)
- Original package was released: Tue Apr 7 1998
