Summary: display bar graphs of system load
Summary(pt_BR): Mostra a carga do sistema com gr�fico de barras
Summary(es): Ense�a la carga del sistema con gr�fico de barras
Name: xsysinfo
Version: 1.6
Release: 7cl
Copyright: MIT
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/xsysinfo-1.6.tar.gz
Source800: xsysinfo-wmconfig.i18n.tgz
BuildRoot: /var/tmp/xsysinfo-root
Summary(de): pr�sentiert Balkendiagramme der Systemauslastung 
Summary(fr): affiche la charge syst�me sous forme d'histogrammes
Summary(tr): Sistem y�k�n� grafiksel olarak belirtir

%description
Many aspects of system performance can be monitored with xsysinfo, including 
network traffic, CPU load, disk space, disk usage, and more. Displays a history 
of performance in a window so you can easily see changes.

%description -l pt_BR
V�rios aspectos da performance do sistema podem ser monitorados com o
xsysinfo, incluindo tr�fego de rede, carga da CPU, espa�o em disco,
uso de disco, e mais. Mostra tamb�m um hist�rico da performance em
uma janela para que voc� possa ver as mudan�as facilmente.

%description -l es
Varios aspectos del desempe�o del sistema pueden ser monitorados
con xsysinfo, incluyendo tr�fico de red, carga de la CPU, espacio
en disco, uso de disco, y m�s. Ense�a tambi�n un hist�rico del
desempe�o en una ventana para que puedas ver los cambios f�cilmente.

%description -l de
Viele Aspekte der Systemleistung k�nnen mit xsysinfo �berwacht werden, u.a.
Netzwerk- und CPU-Auslastung, Festplattenspeicher u. -nutzung, usw. Stellt
�nderungen der Systemleistung leicht erkennbar in einem Fenster dar.

%description -l fr
De nombreux aspects des performances du syst�me peuvent �tre observ�s avec
xsysinfo, dont le trafic sur le r�seau, la charge CPU, l'espace disque,
l'utilisation des disques, et plus encore. Il affiche une historique des
performances dans une fen�tre pour que vous puissiez facilement suivre
l'�volution.

%description -l tr
Sistem performans�n� g�steren baz� i�aretler (CPU y�k�, bo� disk alan�,
kullan�m�, a� trafi�i, vs) xsysinfo yard�m�yla g�zlemlenebilir ve bir
pencere i�inde sistemin y�k� zamana ba�l� olarak izlenebilir.

%prep
%setup -q
make clean

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xsysinfo <<EOF
#xsysinfo name "xsysinfo"
#xsysinfo description "Informa��es do Sistema"
#xsysinfo group Administra��o
#xsysinfo exec "xsysinfo &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xsysinfo-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/X11R6/bin/xsysinfo
%config /usr/X11R6/lib/X11/app-defaults/XSysinfo
%config /usr/X11R6/lib/X11/app-defaults/XSysinfo-color
%config /etc/X11/wmconfig/xsysinfo

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
