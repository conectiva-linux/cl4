Summary: RPM package management (install/updates/reports)
Summary(pt_BR): Gerenciador de pacotes RPM (instala/atualiza/pesquisa)
Summary(es): Gestor de paquetes RPM (instala/actualiza/pesquisa)
Name: managerpm
Version: 1.13
Release: 5cl
Source: managerpm-1.13_1.16r0.1.src.tar.gz
Patch: managerpm-bug.patch
Patch1: managerpm-1.11_1.13r12.guarani.patch
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
BuildRoot: /tmp/rpm-managerpm-root
requires: linuxconf

%description
The managerpm module provide an interface to the RPM system. It allows
one to do the following

	-update one or more packages (find which one to update)
	-show package which were updated on a workstation
	-inspect installed package

%description -l pt_BR
O módulo managerpm para o configurador do Linux (linuxconf) provê
uma interface ao sistema RPM. Com ele você pode:

        - atualiza um ou mais pacotes (pesquisa quais atualizar)
        - mostra os pacotes que foram atualizados numa máquina
        - pesquisa os pacotes instalados

%description -l es
El módulo managerpm para el configurador del Linux (linuxconf)
provee una interface al sistema RPM. Con él tu puedes: - actualizar
uno o más paquetes (pesquisa que actualizar) - enseñar los paquetes
que fueron actualizados en una máquina - pesquisar los paquetes
instalados

%prep
%setup -n managerpm-1.13_1.16r0.1
%patch -p0
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/linuxconf
make install

%post
#linuxconf --setmod managerpm
# enable the module without use the linuxconf --setmodule - aurélio
if ! grep -qs "module.list [01] managerpm" /etc/conf.linuxconf
then echo "module.list 1 managerpm" >> /etc/conf.linuxconf
fi

%postun
if [ "$1" = "0" ] ; then
linuxconf --unsetmod managerpm
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/linuxconf

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 17 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Feb 26 1999 aurélio marinho jargas <aurelio@conectiva.com>
- upgraded to 1.11_1.13r12
- translations updated

* Thu Nov 19 1998 aurélio marinho jargas <aurelio@conectiva.com>
- enable the module without --setmodule
- upgraded to 1.8_1.13r5

* Thu Nov 12 1998 aurélio marinho jargas <aurelio@conectiva.com>
- added pt_BR translations
- patch for the pt_BR help screens
