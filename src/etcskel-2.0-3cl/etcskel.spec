Summary: Red Hat Linux default files for new users' home directories.
Summary(pt_BR): Esqueleto dos arquivos . dos diretórios dos usuários
Summary(es): Esqueleto de los archivos . dos directorios de los usuarios
Name: etcskel
Version: 2.0
Release: 3cl
Copyright: public domain
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: etcskel.tar.gz
Patch: etcskel-cnc.patch
BuildRoot: /tmp/etcskel-root
Requires: bash
BuildArchitectures: noarch

%description
The etcskel package is part of the basic Red Hat system.  Etcskel
provides the /etc/skel directory's files.  These files (.Xdefaults,
.bash_logout, .bash_profile, .bashrc) are then placed in every new
user's home directory when new accounts are created.

%description -l pt_BR
Este pacote é parte do sistema básico Red Hat. Ele contém os arquivos
que vão em /etc/skel. Estes arquivos são copiados para o diretório
home dos usuários novos.

%description -l es
Este paquete es parte del sistema básico Red Hat. Contiene los
archivos que van en /etc/skel. Estos archivos son copiados para el
directorio home de los nuevos usuarios.

%prep
%setup -n skel
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT/etc/skel
mkdir -p $RPM_BUILD_ROOT/etc/skel

for f in .Xdefaults .bash_logout .bash_profile .bashrc ; do
   install -m644 $f $RPM_BUILD_ROOT/etc/skel/
done

%clean
if [ "${RPM_BUILD_ROOT}X" != "X" ]; then
    rm -rf ${RPM_BUILD_ROOT}
fi

%files
%defattr(-,root,root)
%config /etc/skel

%changelog
* Wed Jun 23 1999 Conectiva <dist@conectiva.com>
- Removed *xterm definitions from .Xdefaults

* Fri Apr 16 1999 Preston Brown <pbrown@redhat.com>
- removed .inputrc -- it is migrating to /etc/inputrc elsewhere

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- fixes for .inputrc

* Mon Mar 29 1999 Preston Brown <pbrown@redhat.com>
- more minor updates to .Xdefaults

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- fixed up .Xdefaults to not scroll back with pgup/pgdown
- added .inputrc

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- glibc 2.1

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- clean out more stuff from the default .Xdefaults

* Sat Aug 22 1998 Jeff Johnson <jbj@redhat.com>
- use BASH_ENV=~/.bashrc -- leave ENV for ksh (change #459)

* Fri Nov 08 1997 Cristian Gafton <gafton@redhat.com>
- .Xdefaults file was broken; it is not processed by any macro thing.

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- converted to a noarch package

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- added bash dependencie 

* Thu Mar 20 1997 Erik Troan <ewt@redhat.com>
- Moved .Xclients and .xsession to xinitrc package
