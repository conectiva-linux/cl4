Summary: Maintains identical copies of files on multiple machines.
Summary(pt_BR): Distribuidor de arquivo - mantém arquivos replicados em várias máquinas
Summary(es): Distribuidor de archivo - mantiene réplicas de archivos en varias máquinas
Name: rdist
Version: 6.1.5
Release: 7cl
Copyright: BSD
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: http://www.MagniComp.com/download/rdist/rdist-%{version}.tar.gz
Patch0: rdist-6.1.5-linux.patch
Patch1: rdist-6.1.5-links.patch
Patch2: rdist-6.1.5-oldpath.patch
URL: http://www.MagniComp.comA/rdist
BuildRoot: /var/tmp/%{name}-root

%description
The rdist program maintains identical copies of files on multiple
hosts.  If possible, rdist will preserve the owner, group, mode and
mtime of files and it can update programs that are executing.

%description -l pt_BR
Rdist é um programa para manter cópias idênticas de arquivos em
várias máquinas. Ele preserva o dono, grupo, modo e tempo (mtime)
dos arquivos, se possível, e pode atualizar programas que estão
sendo executados.

%description -l es
Rdist es un programa para mantener copias idénticas de archivos en
múltiples hosts . Preserva el dueño, grupo, modo y tiempo (mtime)
de los archivos, si es posible, puede actualizar programas que
están siendo ejecutados.

%prep
%setup -q

%patch0 -p1 -b .linux
%patch1 -p1 -b .links
%patch2 -p1 -b .oldpath

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,man/man8,sbin}

install -s -m755 src/rdist $RPM_BUILD_ROOT/usr/bin
install -s -m755 src/rdistd $RPM_BUILD_ROOT/usr/sbin
ln -sf ../sbin/rdistd $RPM_BUILD_ROOT/usr/bin/rdistd

install -m644 doc/rdist.man $RPM_BUILD_ROOT/usr/man/man1/rdist.1
install -m644 doc/rdistd.man $RPM_BUILD_ROOT/usr/man/man8/rdist.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/bin/rdist
/usr/bin/rdistd
/usr/sbin/rdistd
/usr/man/man1/rdist.1
/usr/man/man8/rdist.8

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr 13 1999 Jeff Johnson <jbj@redhat.com>
- add /usr/bin/rdistd symlink (#2154)
- update docs to reflect /usr/bin/oldrdist change.

* Mon Apr 12 1999 Jeff Johnson <jbj@redhat.com>
- use /usr/bin/oldrdist for old rdist compatibility path (#2044).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Wed Feb 17 1999 Jeff Johnson <jbj@redhat.com>
- dynamic allocation for link info (#1046)

* Thu Nov 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 6.1.5

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- fixed the url to the source
- fixed the copyright field

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
