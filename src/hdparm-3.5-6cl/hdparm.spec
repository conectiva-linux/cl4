Summary: utility for setting (E)IDE performance parameters
Summary(pt_BR): Utilitário para ajustar parâmetros de performance (E)IDE
Summary(es): Utilitario para ajustar parámetros de desempeño (E)IDE
Name: hdparm
Version: 3.5
Release: 6cl
Copyright: distributable
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/system/hardware/hdparm-3.5.tar.gz
Buildroot: /var/tmp/hdparm-root
Summary(de): Dienstprogramm zum Einstellen von (E)IDE-Parametern
Summary(fr): Utilitaire pour ajuster les paramétres de performances des unités (E)IDE.
Summary(tr): (E)IDE sabit disklerle ilgili bazý parametreleri deðiþtirir

%description
This is a utility for setting Hard Drive parameters.  It is useful for
tweaking performance and for doing things like spinning down hard drives
to conserve power.

%description -l pt_BR
Este é um utilitário para ajustar parâmetros do disco rígido. Ele é
útil para melhorar a performance e para fazer coisas como diminuir
a rotação do disco para conservar energia.

%description -l es
Este es un utilitario para ajustar parámetros del disco duro. Es
útil para mejorar el desempeño y para hacer cosas como diminuir la
rotación del disco para conservar energía.

%description -l de
Dies ist ein Utility zum Einstellen der Festplatten-Parameter, nützlich zum 
Feintunen der Leistung und zum Verlangsamen der Drehgeschwindigkeit, wenn 
Strom gespart werden soll. 

%description -l fr
Utilitaire pour configurer les paramêtres du disque dur. Utile pour
améliorer les performances et pour ralentir les disques durs afin
d'économiser l'énergie.

%description -l tr
Bu program ile sabit disk parametrelerini deðiþtirebilirsiniz. Sistemin
performansýný arttýrmak ya da örneðin disk hýzýný azaltarak daha az güç
harcamak için kullanabilirsiniz.

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 24 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- atualizado para a versão 3.5

* Tue Oct 27 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr


* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>

- updated to 3.3
- build rooted

* Fri Oct 31 1997 Donnie Barnes <djb@redhat.com>

- fixed spelling error in summary

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>

- built against glibc

%prep
%setup

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/doc
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
install -s -m 755 -o 0 -g 0 hdparm $RPM_BUILD_ROOT/sbin/hdparm
install -m 644 -o 0 -g 0 hdparm.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc hdparm.lsm Changelog
/sbin/hdparm
/usr/man/man8/hdparm.8
