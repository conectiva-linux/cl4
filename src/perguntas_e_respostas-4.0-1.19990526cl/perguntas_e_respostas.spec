Summary: Conectiva Linux FAQ Package
Summary(pt_BR): Perguntas e respostas do Conectiva Linux
Summary(es): Conectiva Linux FAQ Package
Name: perguntas_e_respostas
%define version 4.0
%define date 19990526
Version: %{version}
Release: 1.%{date}cl
Source: http://www.conectiva.com/faq/PR19990526.tar.gz
Copyright: distributable
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
BuildArchitectures: noarch
Buildroot: /var/tmp/perguntas_e_respostas_root

%description
This is a package of the Frequently Asked Questions (FAQ)
about the Conectiva Linux.

%description -l pt_BR
Este é um pacote das Questões Freqüentemente Perguntadas (FAQ)
sobre o Conectiva Linux.

%description -l es
This is a package of the Frequently Asked Questions (FAQ)
about the Conectiva Linux.

%prep
%setup -q -n PR

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/doc/perguntas_e_respostas
for diretorio in `find . -type d`; do
    install -d $RPM_BUILD_ROOT/usr/doc/perguntas_e_respostas/$diretorio
done
for arquivo in `find . -type f`; do
    install -m 644 $arquivo $RPM_BUILD_ROOT/usr/doc/perguntas_e_respostas/$arquivo
done

%files
%defattr(-,root,root)
%docdir /usr/doc/perguntas_e_respostas
%dir /usr/doc/perguntas_e_respostas
/usr/doc/perguntas_e_respostas/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jun 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- first build for Conectiva Linux
