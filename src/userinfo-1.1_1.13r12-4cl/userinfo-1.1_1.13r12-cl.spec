Summary: Manage extra information for each user account
Summary(pt_BR): Gerencia informações adicionais de usuários no Linuxconf
Summary(es): Gestiona información adicional de usuarios en Linuxconf
Name: userinfo
Version: 1.1_1.13r12
Release: 4cl
Source: userinfo-1.1_1.13r12.src.tar.gz
Patch1: userinfo-1.1_1.13r12.traducoes.patch
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
BuildRoot: /tmp/rpm-userinfo-root
Requires: linuxconf

%description
This modules lets you define extra fields in the user account dialog.
For each field, you define the type and title. This module could be
used as a basis for small to medium size Internet service provider
administration.

%description -l pt_BR
Este módulo lhe deixa definir campos adicionais à caixa de diálogo de
contas de usuários do Configurador Linux. Para cada campo, você define
o tipo e um título. Este módulo pode ser usado como a base de administração
de um provedor de acesso à Internet de pequeno/médio porte.

%description -l es
Este módulo te deja definir campos adicionales a la caja de
diálogo de cuentas de usuarios del Configurador Linux. Para cada campo,
defines el tipo y un título. Este módulo puede ser usado como la
base de administración de un proveedor de acceso a la Internet de
pequeño/medio porte.

%prep
%setup
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/linuxconf
make install

%post
# linuxconf --unsetmod userinfo
# enable the managerpm module without use the linuxconf --setmodule - aurélio
egrep -qs "module.list [01] userinfo" /etc/conf.linuxconf || \
echo "module.list 1 userinfo" >> /etc/conf.linuxconf

%postun
if [ "$1" = "0" ] ; then
linuxconf --unsetmod userinfo
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/linuxconf

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 18 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar  2 1999 aurélio marinho jargas <dist@conectiva.com>
- updated to 1.1_1.13r12
- translations updated

* Fri Nov 20 1998 aurélio marinho jargas <aurelio@conectiva.com>
- enable the module without --setmodule
- added pt_BR translations
