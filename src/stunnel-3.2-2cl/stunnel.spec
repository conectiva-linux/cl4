%define name stunnel
%define version 3.2
%define release 2cl

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: SSL Wrapper 
Summary(pt_BR): Um Wrapper SSL
Summary(es): Un Wrapper SSL
Name: %{name}
Version: %{version}
Release: %{release}
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /tmp/build-%{name}-%{version}
Patch: stunnel-3.2-opesslnew.patch

%description
The stunnel program is designed to work  as  SSL  encryption
wrapper between remote client and local (inetd-startable) or
remote server.

%description -l pt_BR
O stunnel foi desenvolvido para trabalhar como um wrapper
para encriptação SSL entre clientes remotos e servidores locais.

%description -l es
Un Wrapper SSL.

%prep

%setup -n stunnel
%patch -p1
%build
./configure --prefix=/usr
make

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8

/usr/bin/install -c -m 711 stunnel $RPM_BUILD_ROOT/usr/sbin
/usr/bin/install -c -m 644 stunnel.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%doc README
%doc HISTORY
%doc INSTALL
/usr/sbin/stunnel
/usr/man/man8/stunnel.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added a patch to compile with openssl
