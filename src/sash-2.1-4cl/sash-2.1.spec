Summary: Statically linked shell w/ some basic commands built in
Summary(pt_BR): Interpretador de Comandos ligado estaticamente com alguns comandos básicos
Summary(es): Interpretador de Comandos conectado estáticamente con algunos comandos básicos
Name: sash
Version: 2.1
Release: 4cl
Copyright: GPL
Group: System Environment/Shells
Group(pt_BR): Ambiente do Sistema/Interpretadores de Comandos
Group(es): Ambiente del Sistema/Interpretadores de Comandos
Source0: http://www.tip.net.au/~dbell/sash-2.1.tar.gz
Patch0: sash-2.1-misc.patch
Buildroot: /var/tmp/sash-root

%description
Sash is a very simple, statically linked shell. It includes simplified versions
built in commands like ls, dd, and gzip. Sash can be quite usefull for system
recovery.

%description -l pt_BR
O sash é um interpretador de comandos simples ligado
estaticamente. Inclui versões simplificadas de comandos como ls, dd
e gzip. O sash pode ser útil em situações de recuperação do sistema.

%description -l es
Sash es un interpretador de comandos sencillos encendido
estáticamente.  Incluye versiones simplificadas de comandos como
ls, dd y gzip. Sash puede ser útil en situaciones de recuperación
del sistema.

%prep
%setup -q
%patch0 -p1 -b ".misc"

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8

install -s -m755 sash $RPM_BUILD_ROOT/sbin
install -m644 sash.1 $RPM_BUILD_ROOT/usr/man/man8/sash.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/sash
/usr/man/man8/sash.8

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Sep 22 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
