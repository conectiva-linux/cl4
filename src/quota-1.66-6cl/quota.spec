Name: quota
Summary: System administration tools for monitoring users' disk usage.
Summary(pt_BR): Pacote de administração quota
Summary(es): Paquete de administración cuota
Version: 1.66
Release: 6cl
Source: sunsite.unc.edu:/pub/Linux/system/Admin/quota-%{version}.tar.gz
Copyright: BSD
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Patch0: quota-1.66-misc.patch
Patch1: quota-1.66-dbtob.patch
Patch2: quota-1.66-glibc.patch
Patch3: quota-1.66-rsquash.patch
Patch4: quota-1.66-sparc.patch
Buildroot: /var/tmp/%{name}-root

%description
The quota package contains system administration tools for
monitoring and limiting users' and or groups' disk usage, per
filesystem.

%description -l pt_BR
Quotas permite ao administrador do sistema limitar o uso de disco
por um usuário e/ou grupo por sistema de arquivos. Este pacote
contém as ferramentas que são necessárias para ativar, modificar
e atualizar quotas.

%description -l es
Cuotas permite al administrador del sistema limitar el uso de disco
por un usuario y/o grupo por sistema de archivos. Este paquete
contiene las herramientas que son necesarias para activar, modificar
y actualizar cuotas.

%prep
%setup -q -c

cd utils
tar xzf quota-1.66.tar.gz
%patch0 -p2 -b .misc
%patch1 -p2 -b .dbtob
%patch2 -p2 -b .glibc
%patch3 -p2 -b .rsquash
%patch4 -p2 -b .sparc

%build
make -C utils RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,usr/bin,usr/sbin,usr/man/man{1,2,3,8}}

make -C utils ROOTDIR=$RPM_BUILD_ROOT DEF_BIN_MODE=0555 install

mv $RPM_BUILD_ROOT/usr/sbin/quota $RPM_BUILD_ROOT/usr/bin/quota
# ln -s rquotad.8 $RPM_BUILD_ROOT/usr/man/man8/rpc.rquotad.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/quotacheck
/sbin/quotaon
/sbin/quotaoff
/usr/bin/quota
/usr/sbin/edquota
/usr/sbin/repquota
/usr/sbin/warnquota
/usr/sbin/quotastats
# /usr/sbin/rpc.rquotad

/usr/man/man1/quota.1
/usr/man/man2/quotactl.2
/usr/man/man3/rquota.3
/usr/man/man8/edquota.8
/usr/man/man8/quotacheck.8
/usr/man/man8/quotaon.8
/usr/man/man8/repquota.8
# /usr/man/man8/rquotad.8
# /usr/man/man8/rpc.rquotad.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr 13 1999 Jeff Johnson <jbj@redhat.com>
- fix for sparc64 quotas (#2147)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Mon Dec 28 1998 Cristian Gafton <gafton@redhat.com>
- don't install rpc.rquotad - we will use the one from the knfsd package
  instead

* Thu Dec 17 1998 Jeff Johnson <jbj@redhat.com>
- merge ultrapenguin 1.1.9 changes.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- removed patch for mntent

* Fri Mar 27 1998 Jakub Jelinek <jj@ultra.linux.cz>
- updated to quota 1.66

* Tue Jan 13 1998 Erik Troan <ewt@redhat.com>
- builds rquotad
- installs rpc.rquotad.8 symlink

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- removed /usr/include/rpcsvc/* from filelist
- uses a buildroot and %attr

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Moved /usr/sbin/quota to /usr/bin/quota
