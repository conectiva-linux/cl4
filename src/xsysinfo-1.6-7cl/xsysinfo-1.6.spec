Summary: display bar graphs of system load
Summary(pt_BR): Mostra a carga do sistema com gráfico de barras
Summary(es): Enseña la carga del sistema con gráfico de barras
Name: xsysinfo
Version: 1.6
Release: 7cl
Copyright: MIT
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/xsysinfo-1.6.tar.gz
Source800: xsysinfo-wmconfig.i18n.tgz
BuildRoot: /var/tmp/xsysinfo-root
Summary(de): präsentiert Balkendiagramme der Systemauslastung 
Summary(fr): affiche la charge système sous forme d'histogrammes
Summary(tr): Sistem yükünü grafiksel olarak belirtir

%description
Many aspects of system performance can be monitored with xsysinfo, including 
network traffic, CPU load, disk space, disk usage, and more. Displays a history 
of performance in a window so you can easily see changes.

%description -l pt_BR
Vários aspectos da performance do sistema podem ser monitorados com o
xsysinfo, incluindo tráfego de rede, carga da CPU, espaço em disco,
uso de disco, e mais. Mostra também um histórico da performance em
uma janela para que você possa ver as mudanças facilmente.

%description -l es
Varios aspectos del desempeño del sistema pueden ser monitorados
con xsysinfo, incluyendo tráfico de red, carga de la CPU, espacio
en disco, uso de disco, y más. Enseña también un histórico del
desempeño en una ventana para que puedas ver los cambios fácilmente.

%description -l de
Viele Aspekte der Systemleistung können mit xsysinfo überwacht werden, u.a.
Netzwerk- und CPU-Auslastung, Festplattenspeicher u. -nutzung, usw. Stellt
Änderungen der Systemleistung leicht erkennbar in einem Fenster dar.

%description -l fr
De nombreux aspects des performances du système peuvent être observés avec
xsysinfo, dont le trafic sur le réseau, la charge CPU, l'espace disque,
l'utilisation des disques, et plus encore. Il affiche une historique des
performances dans une fenêtre pour que vous puissiez facilement suivre
l'évolution.

%description -l tr
Sistem performansýný gösteren bazý iþaretler (CPU yükü, boþ disk alaný,
kullanýmý, að trafiði, vs) xsysinfo yardýmýyla gözlemlenebilir ve bir
pencere içinde sistemin yükü zamana baðlý olarak izlenebilir.

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
#xsysinfo description "Informações do Sistema"
#xsysinfo group Administração
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
