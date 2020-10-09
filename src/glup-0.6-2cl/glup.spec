%define name glup
%define version 0.6

Summary: LDP Users' Guide (Spanish translation)
Summary(pt_BR): Guia do Usu�rio do Sistema - do LDP (Tradu��o para o espanhol)
Summary(es): Gu�a del Usu�rio do Sistema - del LDP (En espa�ol)
Name: %{name}
Version: %{version}
Release: 2cl
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Source: %{name}-%{version}.txt.gz
Copyright: distributable
Buildroot: /var/tmp/glup-root
BuildArchitectures: noarch

%description
LDP Users' Guide (Spanish translation)

%description -l pt_BR
Guia do Usu�rio do Sistema - do LDP (Tradu��o para o espanhol)

%description -l es
Gu�a del Usu�rio do Sistema - del LDP (En espa�ol)

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- created the package

%install

mkdir -p $RPM_BUILD_ROOT/usr/doc/LDP/glup
chmod 755 $RPM_BUILD_ROOT/usr/doc/LDP/glup
cp -a %{SOURCE0} $RPM_BUILD_ROOT/usr/doc/LDP/glup

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/doc/LDP/glup
