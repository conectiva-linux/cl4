Summary: displays status of the serial lines in a terminal
Summary(pt_BR): Mostra o estado de uma linha serial em um terminal
Summary(es): Enseña el estado de una línea serial en un terminal
Name: statserial
Version: 1.1
Release: 13cl
Copyright: BSD
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/system/serial/statserial-1.1.tar.gz
Patch: statserial-1.1-config.patch
BuildRoot: /var/tmp/statserial-root
Summary(de): zeigt den Status der seriellen Leitungen in einem Terminal an. 
Summary(fr): Affiche l'état des lignes série dans un terminal
Summary(tr): Bir uçbirimde seri hatlarýn durumlarýný gösterir

%description
Statserial displays a table of the signals on a standard 9-pin or
25-pin serial port, and indicates the status of the handshaking lines.
It can be useful for debugging problems with serial ports or modems.

%description -l pt_BR
Statserial mostra uma tabela dos sinais em uma porta serial padrão
de 9 ou 25 pinos e indica o status das linhas de handshaking.
Pode ser útil na depuração de problemas com portas seriais ou modems.

%description -l es
Statserial enseña una tabla de las señales en un puerto serial padrón
de 9 o 25 pinos y indica el estado de las líneas de handshaking.
Puede ser útil en la depuración de problemas con puertos seriales
o módems.

%description -l de
Statserial zeigt eine Tabelle mit den Signalen auf einem Standard-9-Pin
oder 25-Pin seriellen Port an und meldet den Status der Handshaking-
Leitungen. Nützlich zum Debuggen von Problemen mit seriellen Ports
oder Modems.

%description -l fr
Statserial affiche une table des signaux sur un port série standard 9 ou 25
broches, et indique l'état des lignes reliées. il peut être utile pour
déboguer des problèmes de port série ou de modem.

%description -l tr
Statserial, seri baðlantý noktasý üzerindeki iþaretlerin bir tablosunu
gösterir ve elsýkýþma hatlarýnýn durumunu belirtir. Seri baðlantý noktalarý
ya da modemlerle ilgili hatalarý belirlemekte kullanýlabilir.

%prep
%setup -q
%patch -p1 -b .config

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -m 755 -s statserial $RPM_BUILD_ROOT/usr/bin/statserial
install -m 444 statserial.1 $RPM_BUILD_ROOT/usr/man/man1/statserial.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/statserial
/usr/man/man1/statserial.1

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root
- include arch sparc

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
