Summary: PHP/FI - a powerful apache module
Summary(pt_BR): PHP/FI - módulo para o apache
Summary(es): PHP/FI - módulo para apache
Name: mod_php
Version: 2.0.1
Release: 10cl
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
#Source0: http://www.vex.net/files/php-2.0.1.tar.gz
# recompressed with bzip2
Source0: http://www.vex.net/files/php-2.0.1.tar.bz2
Source1: php-2.0.1-std.config
Patch1: php-2.0.1-dynamic.patch
Patch2: php-2.0.1-rh.patch
Copyright: GPL
BuildRoot: /tmp/php-root
Requires: webserver

%description
PHP is a powerful apache module that adds scripting and database connection
capabilities to the apache server. 

%description -l pt_BR
PHP/FI é um poderoso módulo para o apache, adicionando uma linguagem de
script embutido em HTML, com características avançadas como o acesso
a banco de dados.

Este módulo permanece para compatibilidade com aplicações antigas em
php/fi. Se você vai começar a desenvolver em PHP, use o módulo PHP3.

%description -l es
PHP/FI es un potente módulo para apache, que adiciona un lenguaje
de script incluso en HTML, con características avanzadas como el
acceso a banco de datos.  Este módulo permanece para compatibilidad
con aplicaciones antiguas en php/fi. Si vas empezar a desarrollar
en PHP, usa el módulo PHP3.

%prep
%setup -q -n php-2.0.1
%patch1 -p1 -b .dynamic
%patch2 -p1 -b .rh

%build
autoconf
# this is gross
cat $RPM_SOURCE_DIR/php-2.0.1-std.config | grep -v "^#" | \
        CFLAGS="$RPM_OPT_FLAGS" ./install
cd src; make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/apache
/usr/bin/install -m 755 src/mod_php.so $RPM_BUILD_ROOT/usr/lib/apache

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jun 16 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- recompiled for apache-1.3.3

* Thu Sep 03 1998 Preston Brown <pbrown@redhat.com>
- Updates for Apache 1.3.x
- made configure look for gdbm again
- name changed back to mod_php from php2.

* Fri Feb 27 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to compile it as a shared object for the apache/ssl (and
  future revisions of apache)

%files
/usr/lib/apache/mod_php.so
%doc doc/* README examples
