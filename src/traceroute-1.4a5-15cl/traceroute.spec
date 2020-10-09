Summary: Traces the route taken by packets over a TCP/IP network.
Summary(pt_BR): Mostra a rota que os pacotes usam atrav�s de uma rede TCP/IP
Summary(es): Ense�a la ruta que los paquetes usan a trav�s de una red TCP/IP
Name: traceroute
Version: 1.4a5
Release: 15cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
#Source: ftp://ftp.ee.lbl.gov/traceroute-1.4a5.tar.Z
Source: ftp://ftp.ee.lbl.gov/traceroute-1.4a5.tar.bz2
Source700: traceroute-man-pt_BR.tar
Patch0: traceroute-1.4a5-fix.patch
Patch1: traceroute-1.4a5-secfix.patch
Patch2: traceroute-1.4a5-alpha.patch
Patch3: traceroute-1.4a5-autoroute.patch
Prefix: %{_prefix}
BuildRoot: /var/tmp/%{name}-root

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host.  Traceroute displays
the IP number and host name (if possible) of the machines along the
route taken by the packets.  Traceroute is used as a network debugging
tool.  If you're having network connectivity problems, traceroute will
show you where the trouble is coming from along the route.

Install traceroute if you need a tool for diagnosing network connectivity
problems.

%description -l pt_BR
Traceroute imprime a rota que os pacotes fazem atrav�s de uma rede
TCP/IP. S�o impressos os nomes (ou n�meros de IP se os nomes n�o
estiverem dispon�veis) das m�quinas que est�o roteando pacotes
da m�quina traceroute, junto com o tempo que levou para a m�quina
receber o reconhecimento (ack) do pacote. Esta ferramenta pode ser
muito �til para diagnosticar problemas de rede.

%description -l es
Traceroute imprime la ruta que los paquetes hacen a trav�s de una
red TCP/IP. Son impresos los nombres (o n�meros de IP si los nombres
no est�n disponibles) de las m�quinas que est�n en ruta en paquetes
de la m�quina traceroute, junto con el tiempo que ha llevado para
que la m�quina reciba el reconocimiento (ack) del paquete. Esta
herramienta puede ser muy �til para diagnosticar problemas de red.

%prep
%setup -q
%patch0 -p1 -b .fix
%patch1 -p1 -b .secfix
%patch2 -p1 -b .alpha
%patch3 -p1 -b .autoroute

%build

%configure
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/{sbin,man/man8}

make prefix=${RPM_BUILD_ROOT}%{_prefix} install install-man

{ cd $RPM_BUILD_ROOT
  strip .%{_prefix}/sbin/* || :
}

mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/traceroute-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
# this is set as 4555 by make install, which I don't really like
%attr(4755,root,bin)	%{_prefix}/sbin/traceroute
%attr(0644,root,root) /usr/man/pt_BR/man*/*
%{_prefix}/man/man8/traceroute.8

%changelog
* Fri Jun  4 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 14)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.

* Sun Feb 07 1999 Preston Brown <pbrown@redhat.com>
- patch added to automatically determine interface to route through

* Fri Jan 22 1999 Jeff Johnson <jbj@redhat.com>
- use %configure
- fix 64 bit problem on alpha (#919)

* Wed Jan 13 1999 Bill Nottingham <notting@redhat.com>
- configure fix for arm

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Dec 16 1997 Cristian Gafton <gafton@redhat.com>
- updated the security patch (ouch!). Without the glibc fix, it could be
  worthless anyway

* Sat Dec 13 1997 Cristian Gafton <gafton@redhat.com>
- added a security patch fix

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added fix from Christopher Seawood

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- updated to 1.4a5 for security fixes; release 1 is for RH 4.2, release 2
  is against glibc

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
