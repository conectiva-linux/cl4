%define kdeprefix /usr
%define version 1.1.1
%define kderelease 2cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source

%define compiler egcs
%define conectiva versão-conectiva >= 3.0
%define qtver  qt >= 1.42

%define omit --without-libjpeg --without-libgif --without-libgdbm 
%define omittedlibs jpeglib6a giflib30 gdbm
%define extrareq libungif libjpeg >= 6b-5 gdbm
%define kdename kdesupport

Name: %{kdename}
Summary: K Desktop Environment - Support Libraries
Summary(pt_BR): K Desktop Environment - bibliotecas de suporte
Summary(es): K Desktop Environment - bibliotecas de soporte
Version: %{version}
Release: %{kderelease}
Source: ftp://ftp.kde.org:/pub/kde/{sourcedir}/%{kdename}-%{version}.tar.bz2
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Copyright: GPL/LGPL
BuildRoot: /var/tmp/%{kdename}-buildroot
Requires: %{qtver} %{extrareq}
Prefix: %{kdeprefix}
Obsoletes: kde-devel

%description
Support Libraries used by the K Desktop Environment, but which are not
part of KDE itself.

Libraries included: uulib, mimelib; depending on the Red Hat release,
libraries gdbm, jpeg and gif are either also included, or the versions
supplied by Red Hat are required.
library QwSpriteField and js is also included.


%description -l pt_BR
Bibliotecas de suporte para o KDE.

Incluídos neste pacote:


giflib30: biblioteca de rotinas para trabalhar com imagens GIF
jpeglib6a: programa free JPEG do 'Independent JPEG Group' mimelib:
biblioteca para manipular mensagens em formato MIME

%description -l es
Bibliotecas de soporte para KDE.  Incluidos en este paquete:
giflib30: biblioteca de rutinas para trabajar con imágenes GIF
jpeglib6a: programa free JPEG del 'Independent JPEG Group' mimelib:
biblioteca para manipular mensajes en formato MIME

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{kdename}-%{version}

%build
export KDEDIR=%{kdeprefix}
CC=%{compiler} ./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check %{omit}
make CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -frtti"

%install
export KDEDIR=%{kdeprefix}
rm -rf $RPM_BUILD_ROOT/*
cd $RPM_BUILD_DIR/%{kdename}-%{version}
make prefix=$RPM_BUILD_ROOT%{kdeprefix} install-strip
chmod a+x $RPM_BUILD_ROOT%{kdeprefix}/lib/*

#file list
cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
    $RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
    -e '/\/config\//s|^|%config|' >> \
    $RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
    $RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT/%{kdename}-%{version}
rm -f $RPM_BUILD_DIR/file.list.%{kdename}

%post
grep -q '%{kdeprefix}/lib' /etc/ld.so.conf || echo "%{kdeprefix}/lib" >> \
	/etc/ld.so.conf
/sbin/ldconfig

%postun
if [ "$1" = "0" ]; then
	if ! [ -d %{kdeprefix}/lib ] ; then
	mv /etc/ld.so.conf /etc/ld.so.conf.orig
	grep -v '^%{kdeprefix}/lib$' /etc/ld.so.conf.orig > /etc/ld.so.conf
	rm /etc/ld.so.conf.orig
	/sbin/ldconfig
	fi
fi

%files  -f ../file.list.%{kdename}

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 30 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 1.1.1
- Merged spec file with the KDE Team's original

* Sat Apr 03 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Obsoletes kde-devel from parolin

* Mon Mar 29 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 29 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Mar 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added -frtti to spec file, as kdenetwork needs it

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Removed RedHat support files, and moved them to kdestart

* Fri Feb 26 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Compiled with -fno-exceptions -fno-rtti

* Thu Jan 18 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added pt_BR translations

* Tue Jan 05 1998 Preston Brown <pbrown@redhat.com>
- again, integrated changes from Duncan Haldane
