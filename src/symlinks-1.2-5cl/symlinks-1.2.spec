Summary: symbolic link sanity checker
Summary(pt_BR): Verificador de validade para links simb�licos
Summary(es): Verificador de validez para links simb�licos
Name: symlinks
Version: 1.2
Release: 5cl
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
Copyright: distributable
Source: sunsite.unc.edu:/pub/Linux/utils/file/symlinks-1.2.tar.gz
Buildroot: /var/tmp/symlink-root
Summary(de): Symbolic-Link-Sanity-Checker 
Summary(fr): V�rificateur de la coh�rence des liens symboliques
Summary(tr): Simgesel ba�lant� denetleyici

%description
This program check for a number of problems with symlinks on a system,
including symlinks which point to nonexistant files (dangling symlinks).
It can also automatically convert absolute symlinks to relative symlinks.

%description -l pt_BR
Este programa checa v�rios problemas com symlinks em um sistema,
incluindo symlinks que apontam para arquivo inexistentes. Ele pode
tamb�m automaticamente converter symlinks absolutos para symlinks
relativos.

%description -l es
Este programa chequea varios problemas con symlinks en un sistema,
incluido symlinks que apuntan para archivo inexistente. Puede
tambi�n, autom�ticamente, convertir symlinks absolutos a symlinks
relativos.

%description -l de
Dieses Programm pr�ft das System auf eine Reihe von Problemen im 
Zusammenhang mit Symlinks, einschlie�lich Symlinks, die auf nicht 
vorhandene Dateien zeigen (baumelnde Symlinks). Au�erdem kann es 
absolute Symlinks automatisch in relative verwandeln. 

%description -l fr
Ce programme v�rifie un certain nombre de probl�mes avec les liens
symboliques sur un syst�me, dont ceux qui pointent vers des fichiers
absents (liens pendants). Il peut aussi convertir automatiquement les
liens absolus en liens relatifs.

%description -l tr
Bu program sistemdeki simgesel ba�lant�larla ilgili sorunlar� (varolmayan
bir dosyay� g�steren simgesel ba�lant�lar gibi) kontrol eder. Ayr�ca,
mutlak simgesel ba�lant�lar� ba��l simgesel ba�lant�lara d�n��t�r�r.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr


* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>

- changed build root to /var/tmp, not /var/lib
- updated to version 1.2

* Wed Jul 09 1997 Erik Troan <ewt@redhat.com>

- built against glibc
- build-rooted

%prep
%setup

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
install -s -m 755 -o root -g root symlinks $RPM_BUILD_ROOT/usr/bin
install -m 644 -o root -g root symlinks.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/symlinks
/usr/man/man8/symlinks.8
