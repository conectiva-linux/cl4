%define name cadastro-php3
%define version 1.0
%define release 1cl

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Examples of PHP3 language with database access. 
Summary(pt_BR): Exemplos da linguagem PHP3 com acesso à banco de dados
Summary(es): Examples of PHP3 language with database access. 
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Databases
Group(pt_BR): Aplicações/Banco de Dados
Group(es): Aplicaciones/Bancos de Datos
Copyright: GPL
Source: cadastro.tar.gz
Source1: addphp3pg.sh

BuildRoot: /tmp/build-%{name}-%{version}
Requires: apache
Requires: mod_php3

%description
Cadastro is a set of php3 scripts for use with the Apache HTTP server 
and PHP3.
%description -l pt_BR
O "cadastro" é um conjunto de scripts php3 para uso em conjunto com o
servidor HTTP Apache.

%description -l es
Cadastro is a set of php3 scripts for use with the Apache HTTP server 
and PHP3.

%prep

%setup -n cadastro
%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/home/httpd/html/cadastro
mkdir -p $RPM_BUILD_ROOT/usr/sbin

install -m644 *.php3 *.html *.jpg $RPM_BUILD_ROOT/home/httpd/html/cadastro 
install -m644 $RPM_SOURCE_DIR/addphp3pg.sh $RPM_BUILD_ROOT/usr/sbin/

%files
%doc README
%doc LICENSE
%doc cadastro.sql
/home/httpd/html/cadastro/*
%dir /home/httpd/html/cadastro
/usr/sbin/addphp3pg.sh
