Summary: Tool for creating romfs filesystems.
Summary(pt_BR): Ferramenta para criação de sistema de arquivos romfs
Summary(es): Tool for creating romfs filesystems.
Name: genromfs
Version: 0.3
Release: 5cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.banki.hu/pub/linux/local/genromfs-0.3.tar.gz
Patch: genromfs-0.3.patch
BuildRoot: /var/tmp/%{name}-root
ExclusiveOS: Linux

%description
Genromfs is a tool for creating romfs filesystems, which are
lightweight, read-only filesystems supported by the Linux
kernel.

%description -l pt_BR
O genromfs é uma ferramenta para criação de sistemas de arquivos
romfs, que é um sistema de arquivo leve e somente para leitura,
suportado pelo cerne (kernel) do Linux.

%description -l es
Genromfs is a tool for creating romfs filesystems, which are
lightweight, read-only filesystems supported by the Linux
kernel.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make install PREFIX=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/bin/genromfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/*
/usr/man/man8/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Thu Nov  5 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.

* Thu Oct 30 1998 Jakub Jelinek <jj@ultra.linux.cz>
- new package
