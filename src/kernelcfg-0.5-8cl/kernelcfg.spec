Summary: Kernel Configuration Tool
Summary(pt_BR): Ferramenta de configuração do Kernel
Summary(es): Herramienta de configuración del Kernel
Name: kernelcfg
Icon: kernelcfg.gif
Version: 0.5
Release: 8cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: kernelcfg-%{PACKAGE_VERSION}.tar.gz
Source800: kernelcfg-wmconfig.i18n.tgz
Excludearch: alpha
Requires: pythonlib >= 1.8, python, tkinter, module-info
BuildRoot: /var/tmp/kernelcfg-root
Summary(de): Kernel-Konfigurations-Tool
Summary(fr): Outil de configuration du noyau.
Summary(tr): Çekirdek yapýlandýrma aracý

%description
Red Hat Linux kernelcfg provides a GUI interface which allows you to
easily administrate your kerneld configuration.

%description -l pt_BR
Red Hat Linux kernelcfg provê uma interface gráfica que permite
uma administração facilitada de sua configuração kerneld.

%description -l es
Red Hat Linux kernelcfg provee una interface gráfica que permite
una administración facilitada de su configuración kerneld.

%description -l de
Red-Hat-Linux-kernelcfg stellt eine GUI-Oberfläche zur unkomplizierten 
Administration der kerneld-Konfiguration bereit.

%description -l fr
kernelcfg de Red Hat offre une interface utilisateur graphique vous permettant
d'administrer facilement votre configuration de kerneld.

%description -l tr
RedHat tarafýndan geliþtirilen bu araç hangi modüllerin yükleneceðini ve
sisteminizin nelere destek vereceðini grafik bir arayüz yardýmýyla
düzenlemenizi saðlar.

%prep
%setup -q

%build
unset DISPLAY || true
export PYTHONPATH=/usr/lib/rhs/python
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib}

unset DISPLAY || true
###mkdir -p $RPM_BUILD_ROOT/usr/lib/rhs/control-panel
###rm -rf /usr/lib/rhs/kernelcfg
export PYTHONPATH=/usr/lib/rhs/python
make DESTDIR=$RPM_BUILD_ROOT install

( cd $RPM_BUILD_ROOT
  mkdir -p ./usr/share/icons
  cp ./usr/lib/rhs/control-panel/kernelcfg.xpm ./usr/share/icons/
)

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
chmod 600 $RPM_BUILD_ROOT/etc/X11/wmconfig/kernelcfg




tar xvfpz $RPM_SOURCE_DIR/kernelcfg-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/kernelcfg
/usr/lib/rhs/kernelcfg
/usr/lib/rhs/control-panel/kernelcfg.init
/usr/lib/rhs/control-panel/kernelcfg.xpm
/usr/share/icons/kernelcfg.xpm
%config(missingok) /etc/X11/wmconfig/kernelcfg

%changelog
* Sat Jun 12 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Oct 13 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Thu Jun 11 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Jun 10 1998 Erik Troan <ewt@redhat.com>
- needs to understand release numbers on module-info file -- use 
  /lib/preferred for a first try, if that fails, just glob

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- wmconfig only for root
- noarch doesn't go very well with "ExcludeArch: alpha"...

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- no paths allowed in wmconfig files

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- requires tkinter

* Tue Oct 28 1997 Otto Hammersmith <otto@redhat.com>
- fixed icon reference in .init file

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Mon Jun 02 1997 Michael K. Johnson <johnsonm@redhat.com>
- Look for /boot/module-info-$(uname -r) as well as /boot/module-info
- Tell the user what went wrong if the file doesn't exist.
