Summary: A utility for removing files based on when they were last accessed.
Summary(pt_BR): Limpa arquivos em diretórios baseado em suas idades
Summary(es): Limpia archivos en directorios basado en sus edades
Name: tmpwatch
%define version 1.7
Version: %{version}
Release: 1cl
Source: tmpwatch-%{version}.tar.gz
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
BuildRoot: /var/tmp/tmpwatch-root

%description
The tmpwatch utility recursively searches through specified directories
and removes files which have not been accessed in a specified period of
time.  Tmpwatch is normally used to clean up directories which are used
for temporarily holding files (for example, /tmp).  Tmpwatch ignores
symlinks, won't switch filesystems and only removes empty directories
and regular files.

%description -l pt_BR
Este pacote oferece um programa que pode ser usado para limpar
diretórios. Ele periodicamente vasculha o diretório (ignorando
symlinks) e remove arquivos que não foram acessados em um tempo
especificado pelo usuário.

%description -l es
Este paquete nos ofrece un programa que puede ser usado para
limpiar directorios. Periódicamente remueve el directorio (ignorando
symlinks) y elimina archivos que no fueron accedidos en un tiempo
especificado por el usuario.

%changelog
* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 08 1999 Preston Brown <pbrown@redhat.com>
- I am the new maintainer
- fixed cleanup of directories
- added --quiet flag
- freshen manpage
- nice patch from Kevin Vajk <kvajk@ricochet.net> integrated

* Wed Jun 10 1998 Erik Troan <ewt@redhat.com>
- make /etc/cron.daily/tmpwatch executable

* Tue Jan 13 1998 Erik Troan <ewt@redhat.com>
- version 1.5
- fixed flags passing
- cleaned up message()

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added man page to package
- uses a buildroot and %attr
- fixed error message generation for directories
- fixed flag propagation

* Mon Mar 24 1997 Erik Troan <ewt@redhat.com>
- Don't follow symlinks which are specified on the command line
- Added a man page

* Sun Mar 09 1997 Erik Troan <ewt@redhat.com>
- Rebuilt to get right permissions on the Alpha (though I have no idea
- how they ended up wrong).

%prep
%setup

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT/etc/cron.daily
echo '/usr/sbin/tmpwatch 240 /tmp /var/tmp /var/catman/cat?' \
	> $RPM_BUILD_ROOT/etc/cron.daily/tmpwatch
chmod +x $RPM_BUILD_ROOT/etc/cron.daily/tmpwatch

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/sbin/tmpwatch
/usr/man/man8/tmpwatch.8
%config /etc/cron.daily/tmpwatch
