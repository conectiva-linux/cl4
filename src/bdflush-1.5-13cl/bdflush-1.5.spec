Summary: System Cache flusher
Summary(pt_BR): System Cache flusher
Summary(es): System Cache flusher
Name: bdflush
Version: 1.5
Release: 13cl
Copyright: None
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://tsx-11.mit.edu/pub/linux/sources/system/v1.2/bdflush-1.5.tar.gz
Source700: bdflush-man-pt_BR.tar
Patch: bdflush-1.5-axp.patch
Patch1: bdflush-1.5-glibc.patch
Buildroot: /var/tmp/bdflush-root
Summary(de): System-Cache-Flusher
Summary(fr): Videur de cache système.
Summary(tr): Sistem önbellek temizleyicisi

%description
This program flushes the disk buffers the kernel keeps to prevent them
from growing too stale. 

%description -l pt_BR
Este programa descarrega os buffers de disco que o kernel mantém,
para prevenir que eles cresçam demais.

%description -l es
Este programa descarga los buffers de disco que el kernel mantiene,
para prevenir que crezcan demasiado.

%description -l de
Dieses Programm leert die Disk-Puffer, die der Kernel speichert, damit
sie nicht ranzig werden.

%description -l fr
Ce programme vide les tampons disques du noyau pour éviter qu'ils
deviennent trop anciens.

%description -l tr
Bu program ile çekirdek önbelleði temizleyerek önbellekteki bilginin taze
olmasýný saðlar.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Dec  7 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Sat Dec  5 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Tue Nov 17 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Wed Oct 28 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr


* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- uses a build root
- user %attr()

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- alpha patch should be applied on all architectures

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%prep
%setup -q
%patch -p1
%patch1 -p1 -b .glibc

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8

install -s -m 755 bdflush $RPM_BUILD_ROOT/sbin/update
install -m 644 bdflush.8 $RPM_BUILD_ROOT/usr/man/man8/bdflush.8
ln -sf bdflush.8 $RPM_BUILD_ROOT/usr/man/man8/update.8







mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/bdflush-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) /sbin/update
%attr(-,root,root) /usr/man/man8/bdflush.8
%attr(-,root,root) /usr/man/man8/update.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*
