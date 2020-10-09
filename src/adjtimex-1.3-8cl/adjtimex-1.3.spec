Summary: Kernel clock management
Summary(pt_BR): Gerenciamento do rel�gio do Kernel
Summary(es): Gesti�n del reloj del Kernel
Name: adjtimex
Version: 1.3
Release: 8cl
Exclusiveos: Linux
Copyright: distributable
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://sunsite.unc.edu/pub/Linux/system/admin/time/adjtimex-1.3.tar.gz
Buildroot: /var/tmp/adjtimex-root
Patch: adjtimex-1.3-glibc.patch
Summary(de): Kernel-Taktverwaltung  
Summary(fr): Gestion de l'horloge du noyau
Summary(tr): �ekirdek saat y�netimi

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>
- builds on all architectures

%description
adjtimex is a kernel clock management system.  It is useful in adjusting
the system clock for accuracy.

%description -l pt_BR
adjtimex � um sistema de administra��o do rel�gio do kernel. Ele
� �til no ajuste preciso do rel�gio do sistema.

%description -l es
adjtimex es un sistema de gesti�n del reloj del kernel. Es �til en
el ajuste exacto del reloj del sistema.

%description -l de
adjtimex ist ein Kernel-Uhr-Verwaltungssystem zum Anpassen der
Genauigkeit der Systemuhr.

%description -l fr
adjtimex est un syst�me de gestion de l'horloge du noyau. Il est utile
pour ajuster l'horloge syst�me afin d'obtenir une plus grande pr�cision.

%description -l tr
adjtimex bir �ekirdek saat y�netim sistemidir. Sistem saatini ayarlamak
i�in kullan�l�r.

%prep
%setup
%patch -p1 -b .glibc

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure 
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
install -s -m755 adjtimex $RPM_BUILD_ROOT/sbin/adjtimex
install -m644 adjtimex.man $RPM_BUILD_ROOT/usr/man/man8/adjtimex.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
/sbin/adjtimex
/usr/man/man8/adjtimex.8
