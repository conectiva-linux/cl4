%define name icmpinfo
%define version 1.11
%define release 2cl

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: ICMP message logger
Summary(pt_BR): Programa para "logging" de mensagens ICMP
Summary(es): Herramienta para "logar" mensajes ICMP
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Copyright: GPL
Source: %{name}-%{version}.tar.gz
URL: http://hplyot.obspm.fr/~dl/icmpinfo.html
BuildRoot: /tmp/build-%{name}-%{version}
Patch: icmpinfo-1.11-libc6.patch

%description
Icmpinfo is a tool for looking at the icmp messages received on
the running host.
	  
%description -l pt_BR
O icmpinfo é uma ferramenta para analisar os pacotes ICMP recebidos
na máquina em que ele esteja rodando.

%description -l es
El icmpinfo es una herramienta para analizar las messages ICMP
recibidas en el post destino.

%prep
%setup 
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -o root -g root -m755 icmpinfo $RPM_BUILD_ROOT/usr/bin/icmpinfo
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
install -o root -g root -m 0644 icmpinfo.man $RPM_BUILD_ROOT/usr/man/man8/icmpinfo.8
		

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%doc README
%doc LICENSE
%doc DOC
%doc CHANGES
%doc TODO
/usr/man/man8/icmpinfo.8
/usr/bin/icmpinfo
