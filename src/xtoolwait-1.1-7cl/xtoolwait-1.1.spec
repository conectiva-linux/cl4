Summary: Starts an X program and waits for its window
Summary(pt_BR): Dispara um programa X e espera pela sua janela
Summary(es): Dispara un programa X y espera por su ventana
Name: xtoolwait
Version: 1.1
Release: 7cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://ftp.x.org/contrib/utilities/xtoolwait-1.1.tar.gz
Prefix: /usr
BuildRoot: /var/tmp/xtoolwait-root
Summary(de): Startet ein X-Programm und wartet auf dessen Fenster
Summary(fr): Lance un programme X et attend sa fenêtre
Summary(tr): X programý açar ve penceresini bekler

%description
Utility to start a program and wait for it to map a window. Not an
end-user program, but useful for writing scripts that run X Windows
programs.

%description -l pt_BR
Utilitário para iniciar um programa e esperar por ele para mapear
uma janela. Não é um programa "end-user", mas é útil para escrever
scripts que rodem programas X Window.

%description -l es
Utilitario para iniciar un programa y esperar por él, para hacer
el mapa de una ventana. ENOes un programa "end-user", pero es útil
para escribir scripts que ejecuten programas X Window.

%description -l de
Utility zum Starten eines Programms und Abwarten des Aufbaus eines
Fensters. Kein Endbenutzer-Programm, jedoch nützlich zum Schreiben
von Skripts, die X-Windows-Programme ausführen. 

%description -l fr
Utilitaire pour lancer un programme et attendre qu'il corresponde à une
fenêtre. Utile pour écrire des scripts qui lancent des programmes  X Window

%description -l tr
Bir programý çalýþtýrýr ve penceresinin yaratýlmasýný bekler. Son kullanýcýya
yönelik bir uygulama deðildir.

%prep
%setup -q

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xtoolwait
/usr/X11R6/man/man1/xtoolwait.1x

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new version

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
