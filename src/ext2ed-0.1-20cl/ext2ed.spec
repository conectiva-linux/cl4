Summary: An ext2 filesystem editor.
Summary(pt_BR): Editor do sistema de arquivos ext2 - somente para hackers!!!
Summary(es): Editor del sistema de archivos ext2 - ¡¡¡solamente para hackers!!!
Name: ext2ed
Version: 0.1
Release: 20cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/system/filesystems/ext2/ext2ed-0.1.tar.gz
Patch: ext2ed-0.1-config.patch
Patch1: ext2ed-0.1-inode.patch
Patch2: ext2ed-0.1-glibc.patch
Patch3: ext2ed-0.1-compat21.patch
Patch4: ext2ed-0.1-noreadline.patch
BuildRoot: /var/tmp/%{name}-root
# this should only be built on little endian machines!
ExclusiveArch: alpha i386

%description
Ext2ed is a program which provides a text and window interface for
examining and editing an ext2 filesystem.  Ext2ed is supposed to be
easier to use than debugfs, but debugfs is more powerful.  Note that
this program should only be used by someone who is very experienced at
hacking filesystems.  

Install ext2ed if you want to examine and/or edit your ext2 filesystem,
and you know what you're doing.

%description -l pt_BR
Este é um pacote que permite editar sistema de arquivos ext2fs. Ele
é para hackers *somente* e deve somente ser utilizado por pessoas
experientes. Se você não tem certeza se você é, é porque você não
é. Também, não fume perto deste software. Você foi avisado. Isso
não é uma gravação.

%description -l es
Este es un paquete que permite editar sistema de archivos ext2fs. Es
*solamente* para hackers y debe sólo ser utilizado por expertos. Si
no estás seguro de serlo, es porque no lo es. También, no fume
cerca de este software. Te hemos avisado. Esto no es una grabación.

%prep
%setup -q
%patch -p0 -b .config
%patch1 -p1 -b .inode
%patch2 -p1 -b .glibc
%patch3 -p1 -b .compat21
%patch4 -p1 -b .noreadline

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{usr/bin,usr/man/man8,var/lib}

make	BIN_DIR=$RPM_BUILD_ROOT/usr/bin \
	MAN_DIR=$RPM_BUILD_ROOT/usr/man/man8 \
	VAR_DIR=$RPM_BUILD_ROOT/var/lib/ext2ed \
	install

strip $RPM_BUILD_ROOT/usr/bin/ext2ed

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/var/lib/ext2ed
/usr/bin/ext2ed
/usr/man/man8/ext2ed.8
%doc doc/user-guide-0.1.sgml
%doc doc/user-guide-0.1.ps
%doc doc/Ext2fs-overview-0.1.sgml

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 25 1999 Erik Troan <ewt@redhat.com>
- only build on little endian machines

* Tue Mar 23 1999 Erik Troan <ewt@redhat.com>
- mixing readling and ncurses is evil

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 17)

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses
- updated bad patch (!)

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- various spec file clean ups

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- build against readline library w/ proper soname

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
