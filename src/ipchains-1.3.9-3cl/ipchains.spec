Summary: IP Firewalling Chains.
Summary(pt_BR): Ferramentas para gerenciamento de regras de firewall.
Summary(es): IP Firewalling Chains.
Name: ipchains
%define version 1.3.9
%define scriptsversion 1.1.2
Version: %{version}
Release: 3cl
Copyright: GPL
Obsoletes: ipfwadm ipchains-scripts
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.rustcorp.com/ipchains/ipchains-%{version}.tar.bz2
Source1: ftp://ftp.rustcorp.com/ipchains/ipchains-scripts-%{scriptsversion}.tar.bz2
Buildroot: /var/tmp/ipchains-root

%description 
Linux IP Firewalling Chains is an update to (and hopefully an
improvement upon) the normal Linux Firewalling code, for 2.0 and 2.1
kernels. It lets you do things like firewalls, IP masquerading, etc.

%description -l pt_BR
As correntes de firewall IP do Linux é uma atualização (e esperamos uma
melhoria em relação) ao código normal de firewall do Linux, para os kernels
2.0, 2.1 e 2.2. Elas lhe permitem usar firewalls, mascaramento IP, etc.

%description -l es
Linux IP Firewalling Chains is an update to (and hopefully an
improvement upon) the normal Linux Firewalling code, for 2.0 and 2.1
kernels. It lets you do things like firewalls, IP masquerading, etc.

%prep
%setup -q -a 1

%build
COPTS=$RPM_OPT_FLAGS make -e

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,usr/man/man4,usr/man/man8}
make install SBIN=$RPM_BUILD_ROOT/sbin MANDIR=$RPM_BUILD_ROOT/usr/man
cp ipchains-scripts-%{scriptsversion}/{ipchains-restore,ipchains-save,ipfwadm-wrapper} \
	$RPM_BUILD_ROOT/sbin
cp ipchains-scripts-%{scriptsversion}/{ipchains-restore.8,ipchains-save.8,ipfwadm-wrapper.8} \
	$RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING HOWTO.txt README ipchains-refcard.letter.ps
/sbin/*
/usr/man/*/*

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated ipchains from 1.3.8 to 1.3.9 and ipchains-scripts from 1.0.2 to 1.1.2

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- oboslete phantom ipchains-scripts package that's been floating around...

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Nov 17 1998 Preston Brown <pbrown@redhat.com>
- initial cut.
