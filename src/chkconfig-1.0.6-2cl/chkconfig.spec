Summary: A system tool for maintaining the /etc/rc.d hierarchy.
Summary(pt_BR): Ferramenta para atualizar e listar serviços do sistema, pelo nível de execução (runlevel)
Summary(es): Herramienta para actualizar y listar servicios del sistema, por nivel de ejecución (runlevel)
Name: chkconfig
%define version 1.0.6
Version: %{version}
Release: 2cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.redhat.com/pub/redhat/code/chkconfig/chkconfig-%{version}.tar.gz
BuildRoot: /var/tmp/chkconfig.root

%description
Chkconfig is a basic system utility.  It updates and queries runlevel
information for system services.  Chkconfig manipulates the numerous
symbolic links in /etc/rc.d, so system administrators don't have to
manually edit the symbolic links as often.

%description -l pt_BR
Chkconfig provê uma ferramenta simples na linha de comando
para manter a hierarquia de diretórios /etc/rc.d, aliviando os
administradores do sistema da manipulação direta de numerosos
links simbólicos.

%description -l es
Chkconfig provee una herramienta sencilla en la línea de comando
para mantener la jerarquía de directorios /etc/rc.d, atenuando
los administradores del sistema del manejo directo de numerosos
links simbólicos.

%package -n ntsysv
Summary: A system tool for maintaining the /etc/rc.d hierarchy.
Summary(pt_BR): Interface com menus para configuração de informações de níveis de execução
Summary(es): Interface con menús para configuración de información de niveles de ejecución
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base

%description -n ntsysv
ntsysv updates and queries runlevel information for system
services.  ntsysv relieves system administrators of having to
directly manipulate the numerous symbolic links in /etc/rc.d.

%description -l pt_BR -n ntsysv
O ntsysv fornece uma ferramenta baseada em menus para atualizar a
hierarquia de diretórios /etc/rc.d, que controla a inicialização
e a terminação de serviços do sistema.

%description -l es -n ntsysv
ntsysv ofrece una herramienta basada en menús para actualizar la
jerarquía de directorios /etc/rc.d, que controla el arranque y el
cierre de servicios del sistema.

%prep
%setup -q

%build

%ifarch sparc
LIBMHACK=-lm
%endif

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" LIBMHACK=$LIBMHACK

%install
rm -rf $RPM_BUILD_ROOT
make instroot=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
for n in 0 1 2 3 4 5 6; do
    mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc${n}.d
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/chkconfig
/usr/man/man8/chkconfig.8
%dir /etc/rc.d
%dir /etc/rc.d/*
/usr/share/locale/*/LC_MESSAGES/chkconfig.mo

%files -n ntsysv
%defattr(-,root,root)
/usr/sbin/ntsysv
/usr/man/man8/ntsysv.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- release for Red Hat 6.0

* Thu Apr  8 1999 Matt Wilson <msw@redhat.com>
- added support for a "hide: true" tag in initscripts that will make
  services not appear in ntsysv when run with the "--hide" flag

* Thu Apr  1 1999 Matt Wilson <msw@redhat.com>
- added --hide flag for ntsysv that allows you to hide a service from the
  user.

* Mon Mar 22 1999 Bill Nottingham <notting@redhat.com>
- fix glob, once and for all. Really. We mean it.

* Thu Mar 18 1999 Bill Nottingham <notting@redhat.com>
- revert fix for services@levels, it's broken
- change default to only edit the current runlevel

* Mon Mar 15 1999 Bill Nottingham <notting@redhat.com>
- don't remove scripts that don't support chkconfig

* Tue Mar 09 1999 Erik Troan <ewt@redhat.com>
- made glob a bit more specific so xinetd and inetd don't cause improper matches

* Thu Feb 18 1999 Matt Wilson <msw@redhat.com>
- removed debugging output when starting ntsysv

* Thu Feb 18 1999 Preston Brown <pbrown@redhat.com>
- fixed globbing error
- fixed ntsysv running services not at their specified levels.

* Tue Feb 16 1999 Matt Wilson <msw@redhat.com>
- print the value of errno on glob failures.

* Sun Jan 10 1999 Matt Wilson <msw@redhat.com>
- rebuilt for newt 0.40 (ntsysv)

* Tue Dec 15 1998 Jeff Johnson <jbj@redhat.com>
- add ru.po.

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide (slang-1.2.2)

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- translation updates

* Thu Oct 08 1998 Cristian Gafton <gafton@redhat.com>
- updated czech translation (and use cs instead of cz)

* Tue Sep 22 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- added more translatable strings
- support for i18n init.d scripts description

* Sun Aug 02 1998 Erik Troan <ewt@redhat.com>
- built against newt 0.30
- split ntsysv into a separate package

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- added numerous translations

* Mon Mar 23 1998 Erik Troan <ewt@redhat.com>
- added i18n support

* Sun Mar 22 1998 Erik Troan <ewt@redhat.com>
- added --back
