Summary: configures kernel parallel port driver
Summary(pt_BR): Configura o driver da porta paralela
Summary(es): Configura el driver del puerto paralelo
Name: tunelp
Version: 1.3
Release: 12cl
Copyright: GPL
Group: Utilities/System
Group(pt_BR): Utilitários/Sistema
Group(es): Utilitarios/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/system/printing/tunelp-1.3.tar.gz
Patch: tunelp-1.3-make.patch
BuildRoot: /var/tmp/tunelp-root
Summary(de): konfiguriert den Kerneltreiber für den parallelen Port
Summary(fr): Configure le pilote du port parallèle dans le noyau
Summary(tr): Çekirdeðin paralel baðlantý noktasý sürücüsünü ayarlar

%description
`tunelp' aids in configuring the kernel parallel port driver.

%description -l pt_BR
Tunelp ajuda na configuração do driver de porta paralela do kernel.

%description -l es
Tunelp ayuda en la configuración del driver de puerto paralelo
del kernel.

%description -l de
TUNELP hilft bei der Konfiguration des Kernel-Parallelport-Treibers 

%description -l fr
« tunelp » aide à configurer le pilote du noyau pour le port parallèle

%description -l tr
Paralel baðlantý noktasý sürücüsünü ayarlar

%prep
%setup -q
rm tunelp
%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{man/man8,sbin}

install -m 755 -s tunelp $RPM_BUILD_ROOT/usr/sbin
install -m 644 tunelp.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/tunelp
/usr/man/man8/tunelp.8

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 16 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition

* Thu Apr  1 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 spanish edition

* Wed Mar 31 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.1

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Dec 11 1998 Conectiva <dist@conectiva.com>
- final rebuild for 3.0

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
