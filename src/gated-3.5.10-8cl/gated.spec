Summary: GateD daemon for 2.0.x kernels
Summary(pt_BR): Servidor GateD para kernels 2.0.x
Summary(es): Servidor GateD para kernels 2.0.x
Name: gated
Version: 3.5.10
Release: 8cl
Copyright: distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
#was .gz
Source0: ftp://ftp.gated.org/net-research/gated/gated-3-5-10.tar.bz2
Source1: gated-3-5-7-init
Source2: gated-3-5-7-Config
Source3: gated-3-5-7-gated.conf
Patch0: gated-3-5-7-linux.patch
Patch1: gated-3-5-8-glibc.patch
Patch2: gated-3-5-10-tmprace.patch
Buildroot: /var/tmp/gated-root
Prereq: chkconfig
Url: http://www.gated.org/
Summary(de): GateD-Dämon für 2.0.x-Kernel 
Summary(fr): Démon gated pour les noyaux 2.0.x
Summary(tr): Yönlendirme sunucu süreci

%description
GateD is a routing daemon that  handles  multiple  routing protocols and
replaces routed and egpup.  GateD currently handles the RIP, BGP, EGP,
HELLO, and OSPF routing protocols. The gated process can be configured to
perform all routing protocols or any subset of them. It is curently 
maintained by Merit.

%description -l pt_BR
GateD é um daemon de roteamento que manipula múltiplos protocolos
de roteamento e substitui os programas routed e egpup. O GateD
atualmente suporta os protocolos RIP, BGP, EGP, HELLO, e OSPF. O
processo gated pode ser configurado para executar todos os protocolos
ou algum subconjunto deles. Ele é atualmente mantido pela Merit.

%description -l es
GateD es un daemon de rutado que manipula múltiples protocolos
de rutado y sustituye los programas routed y egpup. GateD actualmente
soporta los protocolos RIP, BGP, EGP, HELLO, y OSPF. El proceso
gated puede ser configurado para ejecutar todos los protocolos o
algún subconjunto de ellos. Es actualmente mantenido por la Merit.

%description -l de
GateD ist ein Routing-Dämon zur Behandlung mehrfacher Routing-Protokolle. 
Er ersetzt ROUTED und EGPUP. Die vorliegende Version von GateD 
unterstützt RIP-, BGP-, EGP-, HELLO- und OSPF-Routing-Protokolle. 
Der GATED-Prozeß kann zur Abarbeitung aller Routing-Protokolle bzw. 
beliebiger Teile davon konfiguriert werden. Die Wartung besorgt zur Zeit
Merit. 

%description -l fr
GateD est un démon de routage gérant plusieurs protocoles de routage et qui
remplace routed et egpup. Pour l'instant, GateD gère les protocoles RIP, BGP,
EGP, HELLO et OSPF. Le processus gated peut être configuré pour réaliser tous
les protocoles de routage ou juste un sous-ensemble. Il est maintenu par
'Merit actuellement.

%description -l tr
GateD birçok yönlendirme protokolunu destekleyen bir yönlendirme sunucu
sürecidir. routed ve egup'un yerini alýr. Þu anda RIP, BGP, EGP, HELLO ve
OSPF yönlendirme protokollarýný desteklemektedir.

%prep
%setup -n gated-3-5-10
%patch1 -p1 -b .glibc
%patch2 -p1
cd src
mkdir obj
install $RPM_SOURCE_DIR/gated-3-5-7-Config obj/Config

%build
cd src
make config
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{usr/{sbin,bin,man/man8},etc/rc.d/init.d}
cd src
make install	BINDIR=$RPM_BUILD_ROOT/usr/bin \
		SBINDIR=$RPM_BUILD_ROOT/usr/sbin
cd ../man
install -m 0644 *.8 $RPM_BUILD_ROOT/usr/man/man8
cd ..
install -m 0750 $RPM_SOURCE_DIR/gated-3-5-7-init \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/gated
install -m 0640 $RPM_SOURCE_DIR/gated-3-5-7-gated.conf \
	$RPM_BUILD_ROOT/etc/gated.conf.sample

%post
/sbin/ldconfig
#chkconfig --add gated

%preun
if [ $1 = 0 ] ; then
        chkconfig --del gated
fi

%files
/usr/sbin/gated
%attr(755,root,root) /usr/bin/*
%doc doc/*
%doc Acknowledgements BUGS CHANGES README README.bgp TODO
%doc ISIS-config.ps
%doc man/gated-2.0-impl.txt
%doc RELEASE 
/usr/man/man8/*
/etc/rc.d/init.d/gated
%config /etc/gated.conf.sample

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Tue Mar 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed prereq

* Sat Mar 13 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Mar 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscript i18n

* Thu Nov 19 1998 Marcelo Tosatti <marcelo@conectiva.com>
- Fixed tmp race in trace.c

* Tue Nov 10 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- gated.init.pt_BR included

* Thu Sep 03 1998 Cristian Gafton <gafton@redhat.com>
- version 3.5.10

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscript

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 3.5.9

* Thu Jan  8 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 3.5.8
- added glibc patch to aid glibc's brain-dead define of IFF_ constants 
  as enums instead of #defines
- we install now gated.conf.sample instead of gated.conf, so gated won't be
  started accidentaly anymore

* Tue Oct 27 1997 Cristian Gafton <gafton@redhat.com>
- build against glibc; added BuildRoot

