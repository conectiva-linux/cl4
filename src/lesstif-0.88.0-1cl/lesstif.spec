Summary: Lesstif is an API compatible clone of the Motif toolkit.
Summary(pt_BR): Um clone do Motif toolkit
Summary(es): Lesstif is an API compatible clone of the Motif toolkit.
Name: lesstif
Version: 0.88.0
Release: 1cl
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://ftp.hungry.com/pub/hungry/lesstif/lesstif-0.88.0.tar.gz
BuildRoot: /tmp/lesstif-root

%description
Lesstif is an API compatible clone of the Motif toolkit.
Currently Lesstif is partially implemented with most of the API in place.
Having said this, some of the internal functionality is still missing.
Many Motif applications compile and run out-of-the-box with LessTif,
and we want to hear about those that don't.

%description -l pt_BR
O Lesstif é um clone do Motif, com a API compatível.

%description -l es
Lesstif is an API compatible clone of the Motif toolkit.
Currently Lesstif is partially implemented with most of the API in place.
Having said this, some of the internal functionality is still missing.
Many Motif applications compile and run out-of-the-box with LessTif,
and we want to hear about those that don't.

%package mwm
Summary: Lesstif Motif window manager clone based on fvwm
Summary(pt_BR): Gerenciador de janelas do Lesstif
Summary(es): Lesstif Motif window manager clone based on fvwm
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio

%description mwm
MWM is a window manager that adheres largely to the Motif mwm specification.

%description -l pt_BR mwm
O MWM é um gerenciador de janelas que adere largamente à especificação
Motif.

%description -l es mwm
MWM is a window manager that adheres largely to the Motif mwm specification.

%package clients
Summary: lesstif clients
Summary(pt_BR): Clientes do lesstif
Summary(es): lesstif clients
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio

%description clients
Uil and xmbind.

%description -l pt_BR clients
Uil e xmbind

%description -l es clients
Uil and xmbind.

%package devel
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Summary: static library and header files for Lesstif/Motif-1.2 developmen
Summary(pt_BR): Bibliotecas e arquivos de inclusão para desenvolvimentos do lesstif
Summary(es): static library and header files for Lesstif/Motif-1.2 developmen

%description devel
This package contains the lesstif static library and header files
required to develop motif-1.2-based applications.
Package also conntains development documentation in html (Lessdox), and
mxmkmf for Lesstif.

%description -l pt_BR devel
Bibliotecas e arquivos de inclusão requeridas para desenvolver
aplicações baseadas no lesstif/motif-1.2

%description -l es devel
This package contains the lesstif static library and header files
required to develop motif-1.2-based applications.
Package also conntains development documentation in html (Lessdox), and
mxmkmf for Lesstif.

%prep
%setup -D -n lesstif-0.88.0
# fix time sync problems with lesstif-current...
# Only needed if you're building from a source tar very soon after release
# and are in a different timezone than the hungry.com folks (who are in PST,
# I think).  Uncomment this if you're bleeding-edge enough to need it.
#  -- Scott <cananian@alumni.princeton.edu>
#touch now
#touch `find . -newer now` now
#rm -f now
#rm -rf $RPM_BUILD_ROOT

LESSTIFTOP=$PWD

./configure --prefix=/usr/X11R6 --enable-shared --enable-static --enable-build-12 --disable-maintainer-mode --disable-build-20 --enable-install-12
( cd lib/Xlt && \
  ./configure --prefix=/usr/X11R6 --enable-shared --enable-static \
              --disable-maintainer-mode \
              --with-motif-includes=$LESSTIFTOP/include/Motif-1.2 \
              --with-motif-libraries=$LESSTIFTOP/lib/Xm/.libs )

%build
make
( cd lib/Xlt && make )

%install
make install prefix=$RPM_BUILD_ROOT/usr/X11R6
( cd lib/Xlt && make install prefix=$RPM_BUILD_ROOT/usr/X11R6 )

strip $RPM_BUILD_ROOT/usr/X11R6/bin/{mwm,uil,xmbind}
strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib{Xm,Mrm,Xlt}.so*

install -d $RPM_BUILD_ROOT/etc/X11
ln -sf ../../usr/X11R6/lib/X11/mwm $RPM_BUILD_ROOT/etc/X11/mwm

install -d $RPM_BUILD_ROOT/usr/X11R6/man
install -d $RPM_BUILD_ROOT/usr/X11R6/man/man1
install -d $RPM_BUILD_ROOT/usr/X11R6/man/man5
install -c -m 644 doc/lessdox/clients/mwmrc.5   $RPM_BUILD_ROOT/usr/X11R6/man/man5
install -c -m 644 doc/lessdox/clients/mwm.1     $RPM_BUILD_ROOT/usr/X11R6/man/man1
install -c -m 644 doc/lessdox/clients/lesstif.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1
install -c -m 644 doc/lessdox/clients/xmbind.1  $RPM_BUILD_ROOT/usr/X11R6/man/man1

# generate config files 
cd $RPM_BUILD_ROOT/usr/X11R6/lib/X11/config;

mv Imake.tmpl Imake-lesstif.tmpl.orig


perl -ne ' 
    if( /#include <Imake.rules>/ ){              
        print $_;
        print "#include <Motif-lesstif.tmpl>\n";
        print "#include <Motif-lesstif.rules>\n";
    }
    elsif ( /IMAKE_CMD = \$\(IMAKE\)/ ){
        print STDERR "found\n";
        s|\$\(IMAKE\)|\$(IMAKE) -T Imake-lesstif.tmpl|;
        print $_;
    }
    else {
        print $_;
    }
' < /usr/X11R6/lib/X11/config/Imake.tmpl > Imake-lesstif.tmpl


mv Motif.rules Motif-lesstif.rules
mv Motif.tmpl  Motif-lesstif.tmpl

cd $RPM_BUILD_ROOT/usr/X11R6/bin
sed -e 's/imake $args/imake -T Imake-lesstif.tmpl $args/' < `which xmkmf` > mxmkmf

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
#do this manually; it's a better idea
#rm -rf $RPM_BUILD_ROOT

%files
%attr(-, root, root) %doc etc/{example.motifbind,motifbind.sun+linux}
%attr(-, root, root) %doc AUTHORS BUG-REPORTING COPYING COPYING.LIB CREDITS 
%attr(-, root, root) %doc CURRENT_NOTES ChangeLog KNOWN_BUGS NEWS NOTES 
%attr(-, root, root) %doc README RELEASE-POLICY TODO
%attr(-, root, root) %doc doc/{*.txt,*.html}
%attr(-, root, root) %doc doc/www.lesstif.org/{*.html,images/*.gif}
%attr(755, root, root) %dir /usr/X11R6/LessTif/Motif1.2/lib/*
%attr(644, root, root) /usr/X11R6/lib/libMrm.so*
%attr(644, root, root) /usr/X11R6/lib/libXm.so*
%attr(644, root, root) /usr/X11R6/lib/libXlt.so*
%attr(644, root, root) /usr/X11R6/man/man1/lesstif.1

%files mwm
%attr(-, root, root) %doc clients/Motif-1.2/mwm/{COPYING,README}
%attr(755, root, root) %dir /etc/X11/mwm
%attr(755, root, root) %dir /usr/X11R6/lib/X11/mwm
%attr(755, root, root) /usr/X11R6/bin/mwm
%attr(644, root, root) %config /usr/X11R6/lib/X11/mwm/*
%attr(644, root, root) %config /usr/X11R6/lib/X11/app-defaults/Mwm
%attr(644, root, root) /usr/X11R6/man/man1/mwm.1
%attr(644, root, root) /usr/X11R6/man/man5/mwmrc.5

%files clients
%attr(755, root, root) /usr/X11R6/bin/uil
%attr(755, root, root) /usr/X11R6/bin/xmbind
%attr(644, root, root) %doc doc/UIL.txt
%attr(644, root, root) /usr/X11R6/man/man1/xmbind.1

%files devel
%attr(-, root, root) %doc etc/README.linuxaout
%attr(-, root, root) %doc doc/lessdox/*
%attr(755, root, root) %dir /usr/X11R6/include/Mrm
%attr(755, root, root) %dir /usr/X11R6/include/Xm
%attr(755, root, root) %dir /usr/X11R6/LessTif/Motif1.2/include
%attr(644, root, root) /usr/X11R6/LessTif/Motif1.2/include/Xm/*
%attr(644, root, root) /usr/X11R6/LessTif/Motif1.2/include/Mrm/*
%attr(644, root, root) /usr/X11R6/lib/libMrm.*a
%attr(644, root, root) /usr/X11R6/lib/libXm.*a
%attr(755, root, root) /usr/X11R6/bin/mxmkmf
#%attr(644, root, root) %config /usr/X11R6/lib/X11/config/*

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Injected new group into package

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat May 15 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Adicionado ao Conectiva Linux
- Modificações ao spec file, para torná-lo compatível com o CL
- traduções para pt_BR incluídas para Summary, %description e Group

* Thu Apr 30 1998 C. Scott Ananian <cananian@alumni.princeton.edu>      (0.83+)
- Updated to lessdoc-current.
- Removes Lessdox package (integrated into lesstif)

* Tue Mar 31 1998 C. Scott Ananian <cananian@alumni.princeton.edu>      (0.83+)
- Removed pedantic.patch
- Removed lesstif-M12 (Motif 1.2 wrapper)
- Reviewed installation and fixed %files sections.
- Added patch to fix a bug which causes mozilla to crash.
- Added patch to fix the include prefix on install.

* Sun Jul 20 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>        (0.80-2)
- added to all %doc %attr macros (this allow build package from normal user
  account),
- some simplification in %files (%doc).
* Wed Jul 9 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added using %%{PACKAGE_VERSION} macro in "Source:" and %files,
- added additional parameter "--enable-build-12" to runing configure,
- added %posun and %clear,
- in %post and %postun ldconfig is called as parameter with "-p"
  (this feature is avalable in rpm >= 2.4.3 and you must have this
  version and if you want recompile package from src.rpm you must have new
  version rpm),
- added package lesstif-M12 simpe Motif 1.2 wrapper,
- simplified %install section,
- added %attr macros in %files sections,
- added striping shared libraries,
- added URL field,
- added Lessdox - a html development documentation to lesstif-devel,
- added lesstif-0.80public-nopedantic.patch, this allow compile lesstif on
  sparc by removing "-pedantic" from CFLAGS.
