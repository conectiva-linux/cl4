%define name sxid
%define version 3.2.4
%define release 3cl

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: sXid is a suid, sgid file and directory checking program.
Summary(pt_BR): O sXid é um programa para checar arquivos e diretórios suid ou sgid
Summary(es): El sXid es un programa para checar arquivos suid y sgid
Name: %{name} 
Version: %{version}
Release: %{release}
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
Copyright: GPL
Source: %{name}_%{version}.tar.gz
BuildRoot: /tmp/build-%{name}-%{version}

%description
sXid is a suid, sgid file and directory checking program.

%description -l pt_BR
O sXid é um programa para checar arquivos e diretórios suid e sgid

%description -l es
sXid es un programa para checar arquivos suid y sgid.

%prep
%setup -n sxid-3.2.4 -q

%build
./configure --prefix=/usr --sysconfdir=/etc
make

%install

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%changelog 
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Apr 18 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition
- Adjusted tag Group in spec file

* Fri Apr 16 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Adjusted some stuff in the call to configure and to make install

* Thu Apr 15 1999 Marcelo Tosatti <marcelo@conectiva.com>
- spec file creation

%files
%doc README
%doc docs/*.example
%doc docs/TODO
%doc docs/REVISIONS

/usr/bin/sxid
/etc/sxid.conf
/usr/man/man1/sxid.1
/usr/man/man5/sxid.conf.5
