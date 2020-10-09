Summary: autofs daemon
Summary(pt_BR): Servidor autofs
Summary(es): Servidor autofs
Name: autofs
%define version 3.1.3
Version: %{version}
Release: 2cl
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source: ftp://ftp.kernel.org/pub/linux/daemons/autofs/autofs-%{version}.tar.bz2
Source1: autofs.init
Patch: autofs-3.1.3-conectiva.patch
Buildroot: /var/tmp/autofs-tmp
Prereq: chkconfig
Requires: bash mktemp sed textutils sh-utils grep procps
Summary(de): autofs daemon 
Summary(fr): d�mon autofs
Summary(tr): autofs sunucu s�reci

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%description -l pt_BR
O autofs � um servidor que monta automaticamente sistemas de arquivos
quando estes forem usados, desmontando-os mais tarde quando n�o
estiverem mais em uso. Incluindo sistemas de arquivo em rede,
CD-ROMS, disquetes, etc.

%description -l es
autofs es un servidor que monta autom�ticamente sistemas de archivos
cuando los usa, y los desmonta, m�s tarde, al terminar de usarlos.
Incluyendo sistemas de archivo en red, CD-ROMS, disquetes, etc.

%description -l de
autofs ist ein D�mon, der Dateisysteme automatisch montiert, wenn sie 
benutzt werden, und sie sp�ter bei Nichtbenutzung wieder demontiert. 
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und �hnliches einschlie�en. 

%description -l fr
autofs est un d�mon qui monte automatiquement les syst�mes de fichiers
lorsqu'on les utilise et les d�monte lorsqu'on ne les utilise plus. Cela
inclus les syst�mes de fichiers r�seau, les CD-ROMs, les disquettes, etc.

%description -l tr
autofs, kullan�lan dosya sistemlerini gerek olunca kendili�inden ba�lar
ve kullan�mlar� sona erince yine kendili�inden ��zer. Bu i�lem, a� dosya
sistemleri, CD-ROM'lar ve disketler �zerinde yap�labilir.

%prep
%setup -q
%patch -p1 -b .rh

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/lib/autofs
mkdir -p $RPM_BUILD_ROOT/usr/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/man/man8

make install prefix=$RPM_BUILD_ROOT/usr
install -m 755 $RPM_SOURCE_DIR/autofs.init $RPM_BUILD_ROOT/etc/rc.d/init.d/autofs
install -m 644 samples/auto.master $RPM_BUILD_ROOT/etc
install -m 644 samples/auto.misc $RPM_BUILD_ROOT/etc
install -m 755 -d $RPM_BUILD_ROOT/misc
chmod 755 $RPM_BUILD_ROOT/usr/lib/autofs/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%post
#chkconfig --add autofs

%postun
if [ "$1" = 0 ] ; then
  chkconfig --del autofs
fi

%files
%defattr(-,root,root)
%doc COPYRIGHT NEWS README TODO
%config /etc/rc.d/init.d/autofs
%config /etc/auto.master
%config(missingok) /etc/auto.misc
/usr/sbin/automount
%dir /misc
/usr/lib/autofs
/usr/man/*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start
- updated from 3.1.1 to 3.1.3
- hacked autofs-3.1.3-conectiva.patch

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed requires

* Fri Mar 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscripts i18n
- added Group, Summary and %description translations

* Fri Nov 20 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Corre��o do uso de crase em � medida (Gra�as a interven��o salvadora
  do Cavassin "por uma raz�o obscura que ningu�m mais lembra")

* Fri Nov 20 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Corre��es do aur�lio para conviv�ncia com o linuxconf

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- internationalized and translated autofs.init to pt_BR

* Tue Oct  6 1998 Bill Nottingham <notting@redhat.com>
- fix bash2 breakage in init script

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- typo in man page.

* Mon Jul 20 1998 Jeff Johnson <jbj@redhat.com>
- added sparc to ExclusiveArch.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- updated to 3.1.1

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscripts

* Fri Dec 05 1997 Michael K. Johnson <johnsonm@redhat.com>
- Link with -lnsl for glibc compliance.

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- exclusivearch for i386 for now, since our kernel packages on
  other platforms don't include autofs yet.
- improvements to initscripts.

* Thu Oct 16 1997 Michael K. Johnson <johnsonm@redhat.com>
- Built package from 0.3.14 for 5.0
