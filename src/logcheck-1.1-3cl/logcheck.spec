%define name logcheck 
%define version 1.1
%define release 3cl

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Log analyzer 
Summary(pt_BR): Um analisador de logs
Summary(es): Un analizador de logs
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Copyright: GPL
Source: %{name}-%{version}.tar.gz
URL: http://www.psionic.com 
BuildRoot: /tmp/build-%{name}-%{version}

%description
Logcheck is software package that is designed to automatically run and check
system log files for security violations and unusual activity.

%description -l pt_BR
O logcheck é um software que foi desenvolvido para automaticamente rodar e
checar logs do sistema para violações de segurança, e atividade não usual.

%description -l es
El logcheck es un software que fue desarrollado para verificar logs del sistema.

%prep
%setup -q

%build
cd src/
cc logtail.c -o logtail 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/etc

install -m 600 -g root -o root ./systems/linux/logcheck.hacking $RPM_BUILD_ROOT/usr/etc
install -m 600 -g root -o root ./systems/linux/logcheck.violations $RPM_BUILD_ROOT/usr/etc
install -m 600 -g root -o root ./systems/linux/logcheck.violations.ignore $RPM_BUILD_ROOT/usr/etc
install -m 600 -g root -o root ./systems/linux/logcheck.ignore $RPM_BUILD_ROOT/usr/etc
install -m 700 -g root -o root ./systems/linux/logcheck.sh $RPM_BUILD_ROOT/usr/sbin/logcheck
install -m 700 -g root -o root ./src/logtail $RPM_BUILD_ROOT/usr/bin
	

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
/usr/bin/logtail
/usr/sbin/logcheck
/usr/etc/logcheck.ignore
/usr/etc/logcheck.violations.ignore
/usr/etc/logcheck.violations
/usr/etc/logcheck.hacking
%doc README
%doc LICENSE
%doc INSTALL 
%doc CHANGES
%doc LICENSE
%doc README.keywords
%doc README.how.to.interpret
