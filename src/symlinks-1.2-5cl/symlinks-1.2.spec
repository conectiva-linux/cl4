Summary: symbolic link sanity checker
Summary(pt_BR): Verificador de validade para links simbólicos
Summary(es): Verificador de validez para links simbólicos
Name: symlinks
Version: 1.2
Release: 5cl
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Copyright: distributable
Source: sunsite.unc.edu:/pub/Linux/utils/file/symlinks-1.2.tar.gz
Buildroot: /var/tmp/symlink-root
Summary(de): Symbolic-Link-Sanity-Checker 
Summary(fr): Vérificateur de la cohérence des liens symboliques
Summary(tr): Simgesel baðlantý denetleyici

%description
This program check for a number of problems with symlinks on a system,
including symlinks which point to nonexistant files (dangling symlinks).
It can also automatically convert absolute symlinks to relative symlinks.

%description -l pt_BR
Este programa checa vários problemas com symlinks em um sistema,
incluindo symlinks que apontam para arquivo inexistentes. Ele pode
também automaticamente converter symlinks absolutos para symlinks
relativos.

%description -l es
Este programa chequea varios problemas con symlinks en un sistema,
incluido symlinks que apuntan para archivo inexistente. Puede
también, automáticamente, convertir symlinks absolutos a symlinks
relativos.

%description -l de
Dieses Programm prüft das System auf eine Reihe von Problemen im 
Zusammenhang mit Symlinks, einschließlich Symlinks, die auf nicht 
vorhandene Dateien zeigen (baumelnde Symlinks). Außerdem kann es 
absolute Symlinks automatisch in relative verwandeln. 

%description -l fr
Ce programme vérifie un certain nombre de problèmes avec les liens
symboliques sur un système, dont ceux qui pointent vers des fichiers
absents (liens pendants). Il peut aussi convertir automatiquement les
liens absolus en liens relatifs.

%description -l tr
Bu program sistemdeki simgesel baðlantýlarla ilgili sorunlarý (varolmayan
bir dosyayý gösteren simgesel baðlantýlar gibi) kontrol eder. Ayrýca,
mutlak simgesel baðlantýlarý baðýl simgesel baðlantýlara dönüþtürür.

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
