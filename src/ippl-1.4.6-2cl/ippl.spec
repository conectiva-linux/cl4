%define name ippl 
%define version 1.4.6
%define release 2cl

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: IP packet logger
Summary(pt_BR): Analisador de pacotes IP
Summary(es): Analizador de paquetes IP
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Copyright: GPL
Source: %{name}-%{version}.tar.gz
URL:  http://www.via.ecp.fr/~hugo/ippl
BuildRoot: /tmp/build-%{name}-%{version}

%description
IPPL logs IP packets sent to a system. 

%description -l pt_BR
O IPPL registra pacotes IP enviados à um sistema

%description -l es
El IPPL registra paquetes IP enviados a un sistema.

%prep
%setup -q

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
mkdir -p $RPM_BUILD_ROOT/usr/man/man5   
mkdir -p $RPM_BUILD_ROOT/etc

install -o root -g root -m755 Source/ippl  $RPM_BUILD_ROOT/usr/sbin/ippl
install -o root -g root -m 0644 Docs/ippl.8 $RPM_BUILD_ROOT/usr/man/man8/ippl.8
install -o root -g root -m 0644 Docs/ippl.conf.5 $RPM_BUILD_ROOT/usr/man/man5/ippl.conf.5
install -o root -g root -m 0644 ippl.conf $RPM_BUILD_ROOT/etc/ippl.conf		

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%doc README
%doc LICENSE
%doc HISTORY
/etc/ippl.conf
/usr/sbin/ippl
/usr/man/man5/ippl.conf.5
/usr/man/man8/ippl.8
