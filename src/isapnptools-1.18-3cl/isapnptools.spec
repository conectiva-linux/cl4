Summary: Utilities for configuring ISA Plug-and-Play (PnP) devices.
Summary(pt_BR): Programas para configurar dispositivos Plug-And-Play ISA numa máquina linux 
Summary(es): Programas para configurar dispositivos Plug-And-Play ISA en una máquina linux 
Name: isapnptools
Version: 1.18
Release: 3cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.demon.co.uk/pub/unix/linux/utils/isapnptools-%{version}.tgz
Patch: isapnptools-1.16.patch
ExclusiveArch: i386 alpha
BuildRoot: /tmp/isapnptools-root

%description
The isapnptools package contains utilities for configuring ISA
Plug-and-Play (PnP) cards/boards which are in compliance with the PnP ISA
Specification Version 1.0a.  ISA PnP cards use registers instead of jumpers
for setting the board address and interrupt assignments.  The cards also
contain descriptions of the resources which need to be allocated.  The BIOS
on your system, or isapnptools, uses a protocol described in the
specification to find all of the PnP boards and allocate the resources so
that none of them conflict.  

Note that the BIOS doesn't do a very good job of allocating resources.  So
isapnptools is suitable for all systems, whether or not they include a PnP
BIOS. In fact, a PnP BIOS adds some complications.  A PnP BIOS may already
activate some cards so that the drivers can find them.  Then these tools
can unconfigure them or change their settings, causing all sorts of nasty
effects. If you have PnP network cards that already work, you should read
through the documentation files very carefully before you use isapnptools.

Install isapnptools if you need utilities for configuring ISA PnP cards.

%description -l pt_BR
Estes programas permitem que dispositivos ISA Plug-And-Play sejam
configurados numa máquina Linux.

Este programa é apropriado para todos os sistemas, mesmo que
não tenham um BIOS PnP. Aliás, um BIOS PnP adiciona algumas
complicações, porque já pode ter ativado algumas placas de modo que
os drivers possam achá-las, e as ferramentas deste pacote podem
desconfigurá-las, ou mudar suas configurações causando efeitos
desagradáveis. Se você tiver (por exemplo) placas de rede plug and
play que já funcionam, sugiro que você leia com cuidado a página
de manual isapnp.conf(5), sobre o formato do arquivo de configuração.

%description -l es
Estos programas permiten que dispositivos ISA Plug-And-Play sean
configurados en una máquina Linux.  Este programa es apropiado para
todos los sistemas, incluso cuando no tienen un BIOS PnP. Además,
un BIOS PnP adiciona algunas complicaciones, porque puede ya
tener activado algunas tarjetas de modo que los drivers las pueden
encontrar, y las herramientas de este paquete pueden desconfigúralas,
o cambiar sus configuraciones causando efectos desagradables. Si
tienes (por ejemplo) tarjetas de red plug and play que ya funcionan,
sugiero que leas con cuidado la página de manual isapnp.conf(5),
sobre el formato del archivo de configuración.

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Feb 16 1999 Bill Nottingham <notting@redhat.com>
- update to version 1.18

* Wed Nov 11 1998 Bill Nottingham <notting@redhat.com>
- update to version 1.17

* Mon Nov  2 1998 Bill Nottingham <notting@redhat.com>
- add /etc/isapnp.gone
- default to not using IRQ 7 on alpha

* Mon Oct 12 1998 Bill Nottingham <notting@redhat.com>
- update to version 1.16

* Mon Oct  5 1998 Bill Nottingham <notting@redhat.com>
- add %post to twiddle readport of old /etc/isapnp.conf files

* Thu Sep 24 1998 Bill Nottingham <notting@redhat.com>
- fixed spec file so it rebuild cleanly

* Fri Aug 07 1998 Bill Nottingham <notting@redhat.com>
- added patch to bump to 1.15a

* Tue Aug 04 1998 Bill Nottingham <notting@redhat.com>
- updated to version 1.15

* Fri Oct 03 1997 Michael Fulbright <msf@redhat.com>
- added code to avoid probing in IO port ranges in /proc/ioports

* Fri Aug 22 1997 Mike Wangsmo <wanger@redhat.com>
- Built against glibc

* Thu Jul 17 1997 Timo Karjalainen <timok@iki.fi>
- Updated to version 1.11
- Added RPM_OPT_FLAGS
- Uses BuildRoot

%prep
%setup -n isapnptools-%{version}

%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
sed -e "s/^\([^#]\)/#\1/" < isapnp.gone > isapnp.tmp
%ifarch alpha
sed -e "s/#IRQ 7/IRQ 7/" < isapnp.tmp > isapnp.tmp2
mv -f isapnp.tmp2 isapnp.tmp
%endif 
mv -f isapnp.tmp isapnp.gone

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/{sbin,usr/man/man5,usr/man/man8,etc}
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES COPYING INSTALL README README.ide README.initrd README.modules
%doc isapnpfaq.txt isapnp.conf isapnp.lsm
%doc config-scripts/YMH0021
%config(missingok) %attr(0644,root,root) /etc/isapnp.gone
/sbin/*
/usr/man/*/*

%post
if [ -f /etc/isapnp.conf ]; then
        NEWPORT=`/sbin/pnpdump | grep READPORT 2>/dev/null`
	if [ -n "$NEWPORT" ]; then
	        mv -f /etc/isapnp.conf /etc/isapnp.conf.rpmsave
		sed -e "s/^[^#]*(READPORT .*/$NEWPORT/" /etc/isapnp.conf.rpmsave > /etc/isapnp.conf
	fi
fi
