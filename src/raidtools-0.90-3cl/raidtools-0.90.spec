Summary: Tools for creating and maintaining software RAID devices.
Summary(pt_BR): Ferramentas para criar e manter dispositivos RAID por software
Summary(es): Herramientas para crear y mantener dispositivos RAID por software
Name: raidtools
Version: 0.90
Release: 3cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.kernel.org/pub/linux/daemons/raid/alpha/raidtools-19990309-0.90.tar.gz
BuildRoot: /var/tmp/raidtools-root
Obsoletes: md
Obsoletes: md-tools
Conflicts: kernel < 2.2

%description
This package includes the tools you need to set up and maintain a software RAID
device under Linux. It only works with Linux 2.2 kernels and later, or 2.0
kernel specifically patched with newer raid support.

%description -l pt_BR
Este pacote fornece as ferramentas necessárias a configuração e manutenção
de dispositivos RAID por software no Linux.

%description -l es
Este paquete ofrece las herramientas necesarias a la configuración
y manutención de dispositivos RAID por software en Linux.

%prep
%setup -q

%build
./autogen.sh
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/dev
make ROOTDIR=$RPM_BUILD_ROOT install_bin install_doc
for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
  mknod -m 0600 $RPM_BUILD_ROOT/dev/md$i b 9 $i
done

%files
%defattr(-,root,root)
/sbin/*
/usr/man/man5/*
/usr/man/man8/*
/dev/*
%doc COPYING README *.sample
%doc Software-RAID.HOWTO/Software-RAID.HOWTO.txt

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- traduções para pt_BR incluídas para Summary, %description e Group

* Tue Apr 06 1999 Cristian Gafton <gafton@redhat.com>
- updated sources from mingo

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Feb 08 1999 Erik Troan <ewt@redhat.com>
- updated to 0.90 19980128

* Mon Oct 12 1998 Erik Troan <ewt@redhat.com>
- backrev'd to 0.50beta10 (which works with old md)
- patched to actually work with old level md support

* Fri Oct 09 1998 Cristian Gafton <gafton@redhat.com>
- put some real Summary and description fields
- obsoletes the md and md-tools package that are floating around on the net

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- tweak description/summary for uniqueness.

* Wed Sep 16 1998 Jeff Johnson <jbj@redhat.com>
- repackage for RH 5.2.
