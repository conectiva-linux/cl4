Summary: Serial interface configuration program
Summary(pt_BR): Programa de configuração de interface serial	
Summary(es): Programa de configuración de interface serial	
Name: setserial
%define	version	2.14
Version: %{version}
Release: 8cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://tsx-11.mit.edu/pub/linux/sources/sbin/setserial-%{version}.tar.gz
Buildroot: /var/tmp/setserial-root
Summary(de): Konfigurationsprogramm für die serielle Schnittstelle
Summary(fr): Programme de configuration de l'interface série
Summary(tr): Seri arayüz ayarlama programý

%description
Setserial is a program which allows you to look at and change various
attributes of a serial device, including its port, its IRQ, and other
serial port options.

%description -l pt_BR
O setserial é um programa que permite visualizar e alterar vários
atributos de um dispositivo serial, incluindo porta, IRQ, e outras
opções.

%description -l es
setserial es un programa que permite visualizar y alterar varios
atributos de un dispositivo serial, incluyendo puerto, IRQ, y
otras opciones.

%description -l de
Setserial ist ein Programm zum Einsehen und Ändern verschiedener
Attribute eines seriellen Geräts, z.B. Port, IRQ und andere 
Optionen des seriellen Ports.

%description -l fr
setserial est un programme permettant de consulter et de modifier les
différents attributs d"un périphérique série, dont son port, son IRQ et
autres options du port série.

%description -l tr
Setserial, bir seri aygýtýn baðlantý noktasý, kesme numarasý gibi
özelliklerini denetlemenizi ve deðiþtirmenizi saðlayan bir programdýr.

%prep
%setup -q

%build
rm -f config.cache
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] || exit 1
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/{bin,usr/man/man8}
install -s setserial $RPM_BUILD_ROOT/bin
install setserial.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] || exit 1
rm -rf $RPM_BUILD_ROOT

%files
%doc README rc.serial
%attr(755,root,bin) /bin/setserial
%attr(444,root,man) /usr/man/man8/setserial.8

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Oct 28 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sat Jun 20 1998 Jeff Johnson <jbj@redhat.com>
- upgraded to 2.1.14

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- pulled into distribution
- used setserial-2.12_CTI.tgz instead of setserial-2.12.tar.gz (former is
  all that sunsite has) - not sure what the difference is.

* Thu Sep 25 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- added %attr's
- added sanity check for RPM_BUILD_ROOT
- setserial is now installed into /bin, where util-linux puts it and all
  startup scripts expect it.
