Summary: X/Tk based SYSV Runlevel Editor
Summary(pt_BR): Editor de Níveis de Execução (Runlevel) SYSV feito em Tk/X
Summary(es): Editor de Niveles de Ejecución (Runlevel) SYSV hecho en Tk/X
Name: tksysv
Version: 1.0
Release: 6cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: tksysv-1.0.tar.gz
Source800: wmconfig.i18n.tgz
Requires: tcl tk chkconfig
BuildArchitectures: noarch
Buildroot: /var/tmp/tksysv-root
Summary(de): X/Tk-basierender SYSV-Runlevel-Editor 
Summary(fr): Éditeur de Runlevels SYSV, basé sur X/Tk
Summary(tr): SysV çalýþma düzeyi düzenleyici

%description
This is a graphical tool for manipulating run levels. It allows you to
control what services get started and stopped for every run level.

%description -l pt_BR
Esta é uma ferramenta gráfica para manipular níveis de execução (runlevels).
Ela permite controlar quais serviços irão iniciar ou parar para cada run level.

%description -l es
Esta es una herramienta gráfica para manipular niveles de ejecución
(runlevels).  Permite controlar cuales servicios irán iniciar o
parar para cada run level.

%description -l de
Dies ist ein grafischen Tool zum Bearbeiten von Betriebsebenen. Sie können
bestimmen, welche Systemdienste gestartet bzw. angehalten werden.

%description -l fr
Ceci est un outil graphique pour manipuler les niveaux d'exécution.
Il vous permet de controller quel services sont lancés et stoppés pour
chacun des niveau d'exécution.

%description -l tr
Çalýþma düzeylerini deðiþtirmek için grafik bir araçtýr. Her çalýþma düzeyi
için hangi servislerin çalýþtýrýlýp durdurulacaðýný denetlemenizi saðlar.

%changelog
* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Thu Apr 23 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 23 1998 Donnie Barnes <djb@redhat.com>
- fixed version number in title bar

%prep
%setup -q

%install
PREFIX=$RPM_BUILD_ROOT ./Install
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGELOG COPYING
/usr/lib/tksysv
/usr/X11R6/bin/tksysv
/usr/lib/rhs/control-panel/tksysv.init
/usr/lib/rhs/control-panel/tksysv.gif
/usr/lib/rhs/control-panel/tksysv.xpm
/usr/man/man8/tksysv.8
%config /etc/X11/wmconfig/tksysv
