Summary: Network Time Protocol utilities
Summary(pt_BR): Utilitários para o Protocolo de Tempo em Rede (NTP)
Summary(es): Utilitarios para  Protocolo de Tiempo en Red (NTP)
Name: xntp3
Version: 5.93
Release: 9cl
Copyright: distributable
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://ftp.udel.edu/pub/ntp/xntp3-%{version}.tar.bz2
Source1: ntp.conf
Source2: ntp.keys
Source3: xntpd.rc
Patch0: xntp3-5.93a.diff.gz
Patch1: xntp3-5.93b.diff.gz
Patch2: xntp3-5.93c.diff.gz
Patch3: xntp3-5.93d.diff.gz
Patch4: xntp3-5.93e.diff.gz
BuildRoot: /var/tmp/xntp3-root

%description
This package contains utilities and daemons to help synchronize your
computer's time to UTC standard time. It includes ntpdate, a program
similar to rdate, and xntpd, a daemon which adjusts the system time
continuously.

%description -l pt_BR
Este pacote contém utilitários e servidores que ajudam a sincronizar
o horário do seu computador para o horário padrão UTC. Ele inclui o
ntpdate, um programa similar ao rdate, e o xntpd, um servidor que ajusta
o horário do sistema continuamente.

%description -l es
Este paquete contiene utilitarios y servidores que ayudan a
sincronizar el horario de tu ordenador para el horario padrón
UTC. Incluye ntpdate, un programa similar al rdate, y xntpd, un
servidor que ajusta el horario del sistema continuamente.

%prep 
%setup -q -n xntp3-%{version}
%patch0 -p1 -b pata
%patch1 -p1 -b patb
%patch2 -p1 -b patc
%patch3 -p1 -b patd
%patch4 -p1 -b pate

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--sysconfdir=/etc --bindir='${prefix}/sbin' \
	--host=$RPM_ARCH-conectiva-linux
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc
strip $RPM_BUILD_ROOT/usr/sbin/* || :

( cd $RPM_BUILD_ROOT
  mkdir -p ./etc/{ntp,rc.d/init.d}
  install -m644 $RPM_SOURCE_DIR/ntp.conf ./etc/ntp.conf
  install -m600 $RPM_SOURCE_DIR/ntp.keys ./etc/ntp/keys
  touch ./etc/ntp/step-tickers
  install -m755 $RPM_SOURCE_DIR/xntpd.rc ./etc/rc.d/init.d/xntpd
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/ntp.conf
%config /etc/ntp/keys
%ghost %config(missingok) /etc/ntp/step-tickers
%doc html/* NEWS TODO 
/usr/sbin/*
/etc/rc.d/init.d/xntpd

%changelog
* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- changed --host in ./configure

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Mar 13 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Mar 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscript i18n

* Fri Dec 11 1998 Conectiva <dist@conectiva.com>
- final rebuild for 3.0
- updated to 5.93e

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Thu Aug  6 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.93c.
- implement suggestions from James Youngman <JYoungman@vggas.com>:
-   correct default /etc/ntp/keys 
-   use /etc/ntp/step-tickers for ntpdate hosts

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- start it after named

* Mon May 04 1998 Jeff Johnson <jbj@redhat.com>
- Update to 5.93.

* Mon Feb  2 1998 Jeff Johnson <jbj@jbj.org>
- Fiddles for RH-5.0. Update to xntp3-5.92.

* Mon Feb  2 1998 Jeff Johnson <jbj@jbj.org>
- Fiddles for RH-5.0. Update to xntp3-5.92.

* Sat Oct 18 1997 Manoj Kasichainula <manojk@io.com>
- Initial release for 5.91
