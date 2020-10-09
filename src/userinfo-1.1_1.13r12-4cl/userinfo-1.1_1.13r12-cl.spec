Summary: Manage extra information for each user account
Summary(pt_BR): Gerencia informa��es adicionais de usu�rios no Linuxconf
Summary(es): Gestiona informaci�n adicional de usuarios en Linuxconf
Name: userinfo
Version: 1.1_1.13r12
Release: 4cl
Source: userinfo-1.1_1.13r12.src.tar.gz
Patch1: userinfo-1.1_1.13r12.traducoes.patch
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
BuildRoot: /tmp/rpm-userinfo-root
Requires: linuxconf

%description
This modules lets you define extra fields in the user account dialog.
For each field, you define the type and title. This module could be
used as a basis for small to medium size Internet service provider
administration.

%description -l pt_BR
Este m�dulo lhe deixa definir campos adicionais � caixa de di�logo de
contas de usu�rios do Configurador Linux. Para cada campo, voc� define
o tipo e um t�tulo. Este m�dulo pode ser usado como a base de administra��o
de um provedor de acesso � Internet de pequeno/m�dio porte.

%description -l es
Este m�dulo te deja definir campos adicionales a la caja de
di�logo de cuentas de usuarios del Configurador Linux. Para cada campo,
defines el tipo y un t�tulo. Este m�dulo puede ser usado como la
base de administraci�n de un proveedor de acceso a la Internet de
peque�o/medio porte.

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
# enable the managerpm module without use the linuxconf --setmodule - aur�lio
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

* Tue Mar  2 1999 aur�lio marinho jargas <dist@conectiva.com>
- updated to 1.1_1.13r12
- translations updated

* Fri Nov 20 1998 aur�lio marinho jargas <aurelio@conectiva.com>
- enable the module without --setmodule
- added pt_BR translations
