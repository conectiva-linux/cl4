Summary: Traffic shaper device configurator
Summary(pt_BR): Configurador do dispositivo traffic shaper
Summary(es): Configurador del dispositivo traffic shaper
Name: shapecfg
Version: 2.0.36
Release: 5cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: shaper.36.tar.gz
Patch: shapercfg-2.0.36-glibc.patch
Buildroot: /var/tmp/shaper-root
Requires: kernel >= 2.0.36
ExclusiveArch: i386

%description
Configure and adjust traffic shaper bandwidth limiters. This package
requires a kernel that has support for the shaper module. Currently this is
the case with the 2.0.36 or later kernels and with late 2.1.X kernels.

%description -l pt_BR
Configura os traffic shaper, limitador de banda . Este pacote requer um
kernel que tenha suporte para o módulo shaper. Atualmente este é o caso
do 2.0.36 e do kernel em desenvolvimento (2.1.12*).

%description -l es
Configura los traffic shaper, limitador de banda. Este
paquete requiere un kernel que tenga soporte para el módulo
shaper. Actualmente este es el caso del  2.0.36 y del kernel en
desarrollo (2.1.12*).

%prep
%setup -n shaper
%patch0 -p1 -b .glibc

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/sbin
install -s -m 755 shapecfg $RPM_BUILD_ROOT/sbin/shapecfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/shapecfg

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Oct 13 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Fri Oct 02 1998 Cristian Gafton <gafton@redhat.com>
- exclusive arch i386 for now
