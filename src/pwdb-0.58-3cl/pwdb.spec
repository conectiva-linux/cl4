Summary: The password database library.
Summary(pt_BR): Biblioteca para manipulação do banco de dados de senhas
Summary(es): Biblioteca para manipulación del banco de datos de contraseñas
Name: pwdb
Version: 0.58
Release: 3cl
Copyright: GPL or BSD
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: pwdb-%{PACKAGE_VERSION}.tar.gz
BuildRoot: /var/tmp/pwdb-root

%description
The pwdb package contains libpwdb, the password database library.
Libpwdb is a library which implements a generic user information
database.  Libpwdb was specifically designed to work with Linux's
PAM (Pluggable Authentication Modules).  Libpwdb allows configurable
access to and management of security tools like /etc/passwd,
/etc/shadow and network authentication systems including NIS and
Radius.

%description -l pt_BR
pwdb (Biblioteca de base de dados de senhas) permite acesso
configurável e gerenciamento do /etc/passwd, /etc/shadow e
autenticação via rede para sistemas incluindo NIS e Radius.

%description -l es
pwdb (Biblioteca de base de datos de contraseñas) permite el acceso
a configuración y administración del /etc/passwd, /etc/shadow y
autentificación, vía red, para sistemas incluyendo NIS y Radius.

%prep
%setup -q -c
rm default.defs
ln -s defs/redhat.defs default.defs
# checking out of the CVS sometimes preserves the setgid bit on
# directories...
chmod -R g-s .

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc,lib,usr/include/pwdb}

make	INCLUDED=$RPM_BUILD_ROOT/usr/include/pwdb \
	LIBDIR=$RPM_BUILD_ROOT/lib \
	LDCONFIG=":" \
	install

install -m 644 conf/pwdb.conf $RPM_BUILD_ROOT/etc/pwdb.conf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Copyright doc/pwdb.txt doc/html
%config /etc/pwdb.conf
/usr/include/pwdb
/lib/libpwdb.a
/lib/libpwdb.so
/lib/libpwdb.so.%{PACKAGE_VERSION}

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 20 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- traduções para pt_BR incluídas para Summary, %description e Group
