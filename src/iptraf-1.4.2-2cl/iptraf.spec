%define name iptraf
%define version 1.4.2
%define release 2cl

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Console based network monitoring program 
Summary(pt_BR): Ferramenta baseada no console para monitoração de rede
Summary(es): Console based network monitoring program 
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Copyright: GPL
Source: %{name}-%{version}.tar.gz
URL: http://cebu.mozcom.com/riker/iptraf
BuildRoot: /tmp/build-%{name}-%{version}

%description
IPTraf is a console-based network monitoring program for Linux that
displays information about IP traffic.
%description -l pt_BR
O IPTraf é uma ferramenta de monitoração baseada no modo console,
para o Linux que mostra informações sobre o tráfego IP.

%description -l es
IPTraf is a console-based network monitoring program for Linux that
displays information about IP traffic.

%prep
%setup -q

%build
cd src/
make

%install
cd src/
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin 
mkdir -p $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/var/log

install -m 0700 -o root -g root -s iptraf $RPM_BUILD_ROOT/usr/sbin
install -m 0700 -o root -g root -s rvnamed $RPM_BUILD_ROOT/usr/sbin
install -m 0700 -o root -g root -d $RPM_BUILD_ROOT/var/local/iptraf
install -m 0700 -o root -g root -d $RPM_BUILD_ROOT/var/log/iptraf
	

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%doc README
%doc CHANGES
%doc WHATELSE 
%doc README.rvnamed
%doc README.interfaces
%doc README.platforms
%doc Documentation/manual.txt
%doc Documentation/manual.html
/usr/sbin/iptraf
/usr/sbin/rvnamed
%dir /var/local/iptraf/
%dir /var/log/iptraf/
