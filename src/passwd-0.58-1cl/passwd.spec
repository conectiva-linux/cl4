Summary: The passwd utility for setting/changing passwords using PAM.
Summary(pt_BR): Atribua ou atualize uma senha usando PAM
Summary(es): Atribuye o actualiza una contraseña usando PAM
Name: passwd
Version: 0.58
Release: 1cl
Copyright: BSD
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: passwd-%{version}.tar.gz
Source700: passwd-man-pt_BR.tar
Buildroot: /var/tmp/passwd-root
Requires: pam >= 0.59
Requires: pwdb >= 0.58

%description
The passwd package contains a system utility (passwd) which
sets and/or changes passwords, using PAM (Pluggable Authentication
Modules).

To use passwd, you should have PAM installed on your system.

%description -l pt_BR
Este programa de troca de senha utiliza PAM (Módulos de Autenticação
Plugáveis) para criar ou alterar uma senha. Como todas as aplicações
PAM, ele pode ser configurado usando um arquivo no diretório
/etc/pam.d/.

%description -l es
Esta alteración de contraseña usa PAM (modulo de autentificación
anexables) para configurar o cambiar la contraseña. Así como,
las aplicaciones que soportan PAM, puede ser configurado usando un
archivo en etc/pam.d/directory.

%prep
%setup -q

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}
make install TOP_DIR=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/bin/passwd
mkdir -p $RPM_BUILD_ROOT/etc/pam.d/
install -m 644 passwd.pamd $RPM_BUILD_ROOT/etc/pam.d/passwd


mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/passwd-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/pam.d/passwd
%attr(4511,root,root) /usr/bin/passwd
/usr/man/man1/passwd.1
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Apr 10 1999 Cristian Gafton <gafton@redhat.com>
- first build from the new source code base.
