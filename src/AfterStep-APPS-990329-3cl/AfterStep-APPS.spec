Summary: Applets you can use with AfterStep and compatible window managers.
Summary(pt_BR): Applets para a coleção de gerenciadores de janelas *Step (AfterStep, Window Maker, etc)
Summary(es): Applets para la colección de administradores de ventanas *Step (AfterStep, Window Maker, etc)
Name: AfterStep-APPS
Version: 990329
Release: 3cl
Copyright: GPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
BuildRoot: /var/tmp/afterstep-apps-root
Source0: http://www.tigr.net/afterstep/as-apps/download/as-apps-%{version}.tar
Patch0: AfterStep-APPS-1.5beta1-glibc.patch
Patch1: ascp-paths.patch
Patch2: as-apps-compile.patch
Patch3: aterm-utmp.patch
Patch4: xiterm-utmp.patch
Prereq: ldconfig
Requires: utempter

%description
What's a cool window manager without some cool applets?
Well... it's still cool, but these applets which can
be used in the Wharf module for AfterStep or Window
Maker can add both spice and productivity to your
preferred window manager, such as a handy clock and
information about system resources.

If you've installed the AfterStep packages, you
should also install these packages. Enjoy! 

%description -l pt_BR
Este pacote inclui alguns applets que podem ser usados no módulo Wharf usado
pelos gerenciadores de janelas como AfterStep e Window Maker.

Todos são muito bons e tornarão seu ambiente de trabalho mais bonito a
medida que você os adiciona ao módulo Wharf.

%description -l es
Este paquete incluye algunos applets que pueden ser usados en el
módulo Wharf usado por los administradores de ventanas como AfterStep
y Window Maker.  Todos son muy buenos y harán tu ambiente de trabajo
más bonito a medida que los adiciones al módulo Wharf.

%prep
%setup -q -c
rm -f *.asc
for archive in *.tar.gz ; do
	tar xzf $archive
	rm -f $archive
done
%patch0 -p1 -b .glibc
%patch1 -p1 -b .paths
%patch3 -p0 -b .autmp
%patch4 -p1 -b .xiutmp

%build
for package in `ls` ; do
    cd $package 
    case $package in
	ascd-* )
	    ./configure << EOF
1

1



EOF
	    patch -p2 -b --suffix .compile < %{PATCH2}
	    xmkmf
	    make Makefiles
	    make MANDIR=/usr/X11R6/man/man1 \
		BINDIR=/usr/X11R6/bin \
		SHLIBDIR=/usr/X11R6/lib \
	    ;;
	
	asmount* | asDrinks* | asbutton* | asdm* | aspbm* | aspostit* | ascdc-* | astuner* | ASFiles* | as[R-W]* | asfaces* | asmon* | astrash* | asxmcd* )
	    # we don't compile these
	    ;;

	aterm*)
	    CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6 \
		--enable-utmp
	    make
	    ;;

	xiterm*)
	    # cough cough, hack hack -- ewt
	    CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6 \
		--enable-xpm-background --enable-utmp --enable-wtmp \
		--enable-menubar --enable-next-scroll
	    xmkmf
	    make Makefiles
	    cd src
	    sed -e "s/EXTRA_LIBRARIES =/EXTRA_LIBRARIES = -lutempter/" \
	       Makefile > Makefile.foo
	    sed -e "s/-lsocket //" Makefile.foo > Makefile
	    make
	    ;;
	asclock*)
	    CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6 << EOF
classic

EOF
             make
	     ;;
	*)
	    #just about every other thing supports autoconf
	    CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6 --datadir=/usr/share
	    make
	    ;;
    esac
    cd ..
done

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man1

for package in `ls` ; do
    cd $package 
    case $package in
	ascd-* | xiterm*)
	    make install install.man \
	        AFTER_BIN_DIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
		AFTER_MAN_DIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
		MANDIR=/usr/X11R6/man/man1 \
		BINDIR=/usr/X11R6/bin \
		SHLIBDIR=/usr/X11R6/lib \
		DESTDIR=$RPM_BUILD_ROOT	
	    ;;

	asmount* | asDrinks* | asbutton* | asdm* | aspbm* | aspostit* | ascdc-* | astuner* | ASFiles* | as[R-W]* | asfaces* | asmon* | astrash* | asxmcd* )
	    # we don't install this
	    ;;

        ascp-* )
	    make install \
	        ASCP_BIN_DIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
		ASCP_MAN_DIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
		prefx=$RPM_BUILD_ROOT \
		DESTDIR=$RPM_BUILD_ROOT
	    ;;
	

	asppp* | aterm* )
	    make install \
	        AFTER_BIN_DIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
		AFTER_MAN_DIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
		DESTDIR=$RPM_BUILD_ROOT
	    ;;
	*)
	    make install install.man \
	        AFTER_BIN_DIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
		AFTER_MAN_DIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
		DESTDIR=$RPM_BUILD_ROOT
	    ;;
    esac
    cd ..
done
rm -f $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}/{sessreg,xpmroot,qplot}*
strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/X11R6/bin/*
/usr/share/afterstep/*
/usr/X11R6/man/man1/*

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Fixed Prereq

* Mon Apr  5 1999 Bill Nottingham <notting@redhat.com>
- strip binaries

* Mon Mar 29 1999 Bill Nottingham <notting@redhat.com>
- update source archive
- fix ascp

* Wed Mar 24 1999 Erik Troan <ewt@redhat.com>
- utempter support
- got xiterm building again

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- updated source archive
- remove  conflicting files with XFree86

* Wed Sep 16 1998 Cristian Gafton <gafton@redhat.com>
- split from afterstep and packaged for RH 5.2
