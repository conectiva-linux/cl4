%define name garl
%define version 0.21

Summary: LDP Network Administrator's Guide (Spanish translation)
Summary(pt_BR): LDP Guia do Administrador de Rede (Tradução para o espanhol)
Summary(es): LDP Guía del Administrador de Red (En Español)
Name: %{name}
Version: %{version}
Release: 2cl
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Source0: %{name}-%{version}.txt.gz
Copyright: distributable
Buildroot: /var/tmp/garl
BuildArchitectures: noarch

%description
This is a generic guide to the Network Administration of Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l pt_BR
Este é um guia genérico para Administração de Redes em sistemas
Linux. Veja http://sunsite.unc.edu/LDP para mais informações sobre
o Projeto de Documentação do Linux, e possíveis atualizações.

%description -l es
Este es un guía genérico para Administración de Redes en sistemas
Linux. Mira http://sunsite.unc.edu/LDP para más información sobre
el Proyecto de Documentación del Linux, y posibles actualizaciones.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- created the package

%install

mkdir -p $RPM_BUILD_ROOT/usr/doc/LDP/garl
chmod 755 $RPM_BUILD_ROOT/usr/doc/LDP/garl
cp -a %{SOURCE0} $RPM_BUILD_ROOT/usr/doc/LDP/garl

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/doc/LDP/garl
