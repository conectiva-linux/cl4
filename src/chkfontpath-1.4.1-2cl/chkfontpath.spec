Summary: Simple interface for editing the font path for the X font server.
Summary(pt_BR): Interface simples para editar a rota de fontes do servidor X.
Summary(es): Interfaz simple para corregir el camino de las fuentes para el servidor X 
Name: chkfontpath
%define version	1.4.1
Version: %{version}
Release: 2cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
BuildRoot: /var/tmp/%{name}-root
Source: %{name}-%{version}.tar.gz
Requires: XFree86-xfs

%description 
This is a simple terminal mode program for adding, removing and listing
the directories contained in the X font server's path. It is mostly
intended to be used 'internally' by RPM when packages with fonts are
added or removed, but it may be useful as a stand-alone utility in
some instances.

%description -l pt_BR
Este é um programa simples para adicionar, remover e listar os diretórios
de fontes do servidor X. Ele é usado internamente pelo programa RPM
quando instala ou remove pacotes com fontes.

%description -l es
Esto es un programa simple del modo terminal para agregar, quitar y
enumerar los directorios de fuentes del servidor X. Usado internamente 
por RPM cuando hace fuentes para agregar o quitar,

%prep
%setup -q

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make INSTROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root)/usr/sbin/chkfontpath
%attr(-,root,root)/usr/man/man8/chkfontpath.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Apr 14 1999 Preston Brown <pbrown@redhat.com>
- preserve permissions on config file

* Thu Apr 07 1999 Preston Brown <pbrown@redhat.com>
- if /proc isn't mounted, don't do a killall

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- don't use psmisc, use pidof from SysVinit

* Fri Mar 12 1999 Preston Brown <pbrown@redhat.com>
- made psmisc a requirement.

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- added "quiet" option.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- injected new group / description.

* Tue Feb 16 1999 Preston Brown <pbrown@redhat.com>
- important fix - kill font server with USR1 instead of HUP.

* Mon Feb 15 1999 Preston Brown <pbrown@redhat.com>
- initial spec file
