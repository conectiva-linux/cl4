Summary: configuration tool for /dev/modem
Summary(pt_BR): Ferramenta de configura��o de modem
Summary(es): Herramienta de configuraci�n de m�dem
Name: modemtool
Version: 1.21
Release: 7cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
Source: modemtool-1.21.tar.gz
Source800: modemtool-wmconfig.i18n.tgz
Requires: python pythonlib
BuildArchitectures: noarch
BuildRoot: /var/tmp/modemtool-root
Summary(de): Konfigurations-Tool f�r /dev/modem
Summary(fr): Outil de configuration pour /dev/modem.
Summary(tr): /dev/modem ayg�t�n�n �zelliklerini de�i�tirmek i�in bir ara�

%description
The modem tool is a graphical simple configuration tool for selecting which
of your serial ports is connected to a modem.

%description -l pt_BR
O modemtool � uma ferramenta gr�fica simples de configura��o para
selecionar qual das portas seriais o seu modem est� conectado.

%description -l es
modemtool es una herramienta gr�fica sencilla de configuraci�n para
seleccionar el puerto serial donde est� conectado tu m�dem.

%description -l de
Das Modem-tool ist ein einfaches grafisches Konfigurations-Tool zur 
Bestimmung des seriellen Ports f�r den Modemanschlu�. 

%description -l fr
L'outil modem est un outil de configuration graphique simple pour choisir le
port s�rie sur lequel est connect� votre modem.

%description -l tr
modemtool, hangi seri portun modeme ba�l� oldu�unu se�mek i�in
kullan�labilecek, grafik temelli, basit bir ara�t�r.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/rhs/control-panel}
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make	PREFIX=$RPM_BUILD_ROOT/usr \
	INSTALLBIN="install -m755" INSTALLDATA="install -m644" \
	install



tar xvfpz $RPM_SOURCE_DIR/modemtool-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/modemtool
/usr/lib/rhs/control-panel/modemtool.init
/usr/lib/rhs/control-panel/modemtool.xpm
/usr/lib/rhs/control-panel/python/modem.py
%attr(600,root,root) /etc/X11/wmconfig/modemtool

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Mar 27 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sat Mar 27 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmconfig created, in pt_BR

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
