Summary: A tool for finding out information about a specified file.
Summary(pt_BR): Reporta informações sobre arquivos
Summary(es): Reporta información sobre archivos
Name: stat
Version: 1.5
Release: 12cl
Copyright: none
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
Source: stat-1.5.tar.gz
Patch0: stat-1.5-misc.patch
Patch1: stat-1.5-exit.patch
Patch2: stat-1.5-dev.patch
BuildRoot: /var/tmp/%{name}-root

%description
The stat utility prints out filesystem level information about a
specified file, including size, permissions, link count, inode, etc.

%description -l pt_BR
O programa stat mostra informações a nível de sistema de arquivo
sobre um determinado arquivo, incluindo permissões, contagem de link,
inode, etc.

%description -l es
El programa stat enseña información a nivel de sistema de archivo
sobre un determinado archivo, incluyendo permisos, contador de link,
inode, etc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1

make BIN=$RPM_BUILD_ROOT/usr/bin MAN=$RPM_BUILD_ROOT/usr/man/man1 install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/stat
/usr/man/man1/stat.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 11)

* Tue Dec 15 1998 Jeff Johnson <jbj@redhat.com>
- 64bit dev_t causes stack alignment problem (from baccala@freesoft.org)

* Fri Jul 31 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu Jul 30 1998 Alan Iwi <iwi@atm.ox.ac.uk>
- handle stat errors w/o failing

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
