%define name statnet 
%define version 3.5
%define release 2cl

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Network traffic analyzer 
Summary(pt_BR): Analisador de tráfego de rede
Summary(es): Analizador de trafago de Red
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Copyright: GPL
Source: %{name}-%{version}.tar.gz
URL: http://www.skypoint.com/~sewilco/statnet.htm
BuildRoot: /tmp/build-%{name}-%{version}
Patch: statnet-3.5-compat21.patch


%description
Statnet views the statistics of your Ethernet and PLIP/PPP/SLIP for TCP, IP,
IPX, Appletalk, and whatever else it notices.

%description -l pt_BR
O statnet faz estatísticas para a sua Ethernet, TCP, IP, IPX e Appletalk.

%description -l es
Un analizador de trafago de red.

%prep
%setup 
%patch -p1
%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m755 -o root -g root statnet  $RPM_BUILD_ROOT/usr/sbin/statnet
install -m755 -o root -g root statnetd  $RPM_BUILD_ROOT/usr/sbin/statnetd
		

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%doc README
%doc CHANGES
/usr/sbin/statnet
/usr/sbin/statnetd
