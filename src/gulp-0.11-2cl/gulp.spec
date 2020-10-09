%define name gulp
%define version 0.11

Summary: LDP Programmer's Guide (Spanish translation)
Summary(pt_BR): LDP Guia do Programador (Vers�o em espanhol)
Summary(es): LDP Gu�a del Programador (En espa�ol)
Name: %{name}
Version: %{version}
Release: 2cl
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Source: %{name}-%{version}.txt.gz
Copyright: distributable
Buildroot: /var/tmp/gulp
BuildArchitectures: noarch

%description
This is a generic guide to the Programming on Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l pt_BR
[root@plucky summaries]# cat > gulp
Este � um guia gen�rico de programa��o em sistemas Linux. Verifique
http://sunsite.unc.edu/LDP para mais informa��es sobre o Projeto
de Documenta��o do Linux, e possivelmente atualizar esta vers�o.
(Vers�o em espanhol)

%description -l es
Este es un gu�a gen�rico de programaci�n en sistemas Linux. Verifica
http://sunsite.unc.edu/LDP para m�s informaci�n sobre el Proyecto
de Documentaci�n del Linux, y posiblemente actualizar esta versi�n.
(Versi�n en espa�ol)

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- created the package

%install

mkdir -p $RPM_BUILD_ROOT/usr/doc/LDP/gulp
chmod 755 $RPM_BUILD_ROOT/usr/doc/LDP/gulp
cp -a %{SOURCE0} $RPM_BUILD_ROOT/usr/doc/LDP/gulp

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/doc/LDP/gulp
