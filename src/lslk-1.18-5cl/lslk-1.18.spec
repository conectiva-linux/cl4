Summary: Lists lock files held by processes.
Summary(pt_BR): Lista arquivos de travamento (lock files) mantidos por processos.
Summary(es): Lista archivos de bloqueo (lock files) mantenidos por procesos.
Name: lslk
Version: 1.18
Release: 5cl
Copyright: Free
Group: Development/Debuggers
Group(pt_BR): Desenvolvimento/Depuradores
Group(es): Desarrollo/Depuradores
Source: ftp://vic.cc.purdue.edu/pub/tools/unix/lslk/lslk_%{version}_W.tar.gz
Prefix: /usr
Buildroot: /var/tmp/%{name}-%{version}-root

%description
The UNIX lock file lister, lslk, attempts to list all the locks
held on the local files of the executing system -- i.e., on the
active inodes.  The locks may come from local processes or remote
ones on NFS clients, served by the executing system.  Note:  Linux
and PTX 2.1.9 lslk don't report on locks held by remote NFS client
processes.

%description -l pt_BR
O listador de arquivos de travamento (lock files) do UNIX, lslk,
tenta listar todos os travamentos mantidos nos arquivos locais do
sistema -- i.e., em inodes ativos. Os travamentos podem ter sido
feitos por processos locais ou remotos em clientes NFS, servidos
pelo sistema. Nota: o lslk Linux e PTX 2.1.9 não reportam travamentos
mantidos por processos em clientes NFS remotos.

%description -l es
El listador de archivos de bloqueo (lock files) del UNIX, lslk,
intenta listar todos los bloqueos mantenidos en los archivos locales
del sistema -- i.e., en inodes activos. Los bloqueos pueden haber
sido hechos por procesos locales o remotos en clientes NFS, servidos
por el sistema. Nota: lslk Linux y PTX 2.1.9 no reportan bloqueos
mantenidos por procesos en clientes NFS remotos.

%prep
%setup -q -c -n lslk
tar xf lslk_%{version}.tar
cd lslk_%{version}

%build
rm -rf $RPM_BUILD_ROOT
cd lslk_%{version}
./Configure -n linux
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}

cd lslk_%{version}
install -s lslk $RPM_BUILD_ROOT/usr/sbin
install lslk.8 $RPM_BUILD_ROOT/usr/man/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# XXX should be mode 4755, but for now leave the setuid off
%attr(2755,root,kmem) /usr/sbin/lslk
/usr/man/man8/lslk.8

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- create.
- leave the setuid root off.
