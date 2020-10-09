Summary: Tools for creating virtual consoles
Summary(pt_BR): Ferramentas para cria��o de consoles virtuais
Summary(es): Herramientas para creaci�n de consolas virtuales
Name: open
Version: 1.4
Release: 9cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/utils/console/open-1.4.tar.gz
Patch: open-1.4-includes.patch
BuildRoot: /var/tmp/open-root
Summary(de): Tools zum Erstellen virtueller Konsolen
Summary(fr): Outils pour cr�er des consoles virtuelles
Summary(tr): Sanal konsol yaratmak i�in ara�lar

%description
This program runs a command on an given virtual console number. It can
also run the program on the first virtual console which isn't already
in use.

%description -l pt_BR
Este programa executa um comando numa determinada console
virtual. Tamb�m pode executar o programa no primeiro console virtual
que n�o est� mais em uso.

%description -l es
Este programa ejecuta un comando en una determinada consola
virtual. Tambi�n puede ejecutar el programa en la primera consola
virtual que no est� m�s en uso.

%description -l de
Dieses Programm f�hrt einen Befehl auf eine angegebene virtuelle Konsolennummer
aus. Es ist auch m�glich, den Befehl auf die erste, noch nicht in Gebrauch befindliche
Konsole auszuf�hren.

%description -l fr
Ce programme ex�cute une commande sur un num�ro de console donn�. il
peut aussi ex�cuter le programme sur la premi�re console virtuelle qui
n'est pas encore utilis�e.

%description -l tr
Bu program sayesinde bir kullan�c� istedi�i sanal konsolda bir program
ko�turabilir. �stenirse program kullan�mda olmayan ilk sanal konsolda
�al��t�r�labilir.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make BINDIR=$RPM_BUILD_ROOT/usr/bin MANDIR=$RPM_BUILD_ROOT/usr/man/man1 install

strip $RPM_BUILD_ROOT/usr/bin/{open,switchto}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/open
/usr/bin/switchto
/usr/man/man1/open.1
/usr/man/man1/switchto.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated version
- changed source url to ftp://...
- fixed braindeadness with NAME_MAX

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
