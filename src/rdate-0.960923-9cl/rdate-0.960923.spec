Summary: Remote clock reader (and local setter)
Summary(pt_BR): Leitor de rel�gio remoto (e ajustador local)
Summary(es): Lector de reloj remoto (y ajuste local)
Name: rdate
Version: 0.960923
Release: 9cl
Copyright: none
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/misc/rdate-960923.tar.gz
Source700: rdate-man-pt_BR.tar
Patch: rdate-960923-make.patch
BuildRoot: /var/tmp/rdate-root
Summary(de): Entfernter Uhrenleser (lokaler Einsteller)
Summary(fr): Lecteur d'horloge distante (et configurateur local)
Summary(tr): A� �zerinden sistem saatini ayarlayan yaz�l�m

%description
rdate is a program that can retrieve the time from another
machine on your network.  If run as root, it will also set
your local time to that of the machine you queried.  It is
not super accurate; get xntpd if you are really worried
about milliseconds.

%description -l pt_BR
Rdate � um programa que pode retornar o tempo (data/hora) de outra
m�quina na sua rede. Se rodar como root, ele tamb�m ir� configurar o
hora local como o da m�quina requisitada. Ele n�o � super preciso;
pegue xntpd se voc� realmente se preocupa com milisegundos.

%description -l es
Rdate es un programa que puede retornar el tiempo (fecha/hora) de
otra m�quina en tu red. Si le ejecutas como root, tambi�n configurar�
el tiempo local como el de la m�quina solicitada. No es muy riguroso;
coge xntpd, si realmente te preocupa los milisegundos.

%description -l de
rdate ist ein Programm, das die Uhrzeit von einem anderen
Netzwerkrechner lesen kann. Wenn Sie es als root ausf�hren,
stellt es Ihre Ortszeit auf die des abgefragten Rechners ein. Es ist 
nicht sehr genau. Wenn Sie auf die Millisekunde genau sein 
wollen, besorgen Sie sich xntpd .

%description -l fr
rdate permet de r�cup�rer l'heure d'une autre machine du r�seau.
s'il est lanc� par root, il configurera aussi votre heure locale
avec celle de la machine que vous avez interrog�. Il n'est pas
tr�s pr�cis ; si vous vous souciez des millisecondes, r�cup�rez
xntpd.

%description -l tr
rdate ile herhangi ba�ka bir makinadan sistem saatini sorgulanabilir. Yetkili
kullan�c� taraf�ndan �al��t�r�l�rsa sistem saatini ayarlamak da m�mk�nd�r. Ne
var ki bu uygulama �ok hassas de�ildir.

%prep
%setup -q -n rdate
%patch -p1

%build
make clean
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -m755 -s rdate $RPM_BUILD_ROOT/usr/bin
install -m644 rdate.1 $RPM_BUILD_ROOT/usr/man/man1



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/rdate-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/rdate
/usr/man/man1/rdate.1
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Dec  5 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Tue Nov 17 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- fixed the url to the source

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
