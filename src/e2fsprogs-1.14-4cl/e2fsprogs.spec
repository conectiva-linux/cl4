Summary: Tools for the second extended (ext2) filesystem 
Summary(pt_BR): Ferramentas para o sistema de arquivos ext2
Summary(es): Herramientas para el sistema de archivos ext2
Name: e2fsprogs
Version: 1.14
Release: 4cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
# Source: ftp://tsx-11.mit.edu/pub/linux/packages/ext2fs/e2fsprogs-1.14.tar.gz
# recompressed with bzip2
Source: ftp://tsx-11.mit.edu/pub/linux/packages/ext2fs/e2fsprogs-1.14.tar.bz2
Source700: e2fsprogs-man-pt_BR.tar
BuildRoot: /tmp/e2fsprogs-root

%description
This package includes a number of utilities for creating, checking,
and repairing ext2 filesystems.

%description -l pt_BR
Este pacote inclui vários utilitários para criação, checagem e
reparo de sistema  de arquivos ext2.

%description -l es
Este paquete incluye varios utilitarios para creación, chequeo y
arreglo de sistema de archivos ext2.

%package devel
Summary: e2fs static libs and headers
Summary(pt_BR): Bibliotecas estáticas e arquivos de inclusão para e2fs
Summary(es): Bibliotecas estáticas y archivos de inclusión para e2fs
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: e2fsprogs

%description devel 
Libraries and header files needed to develop ext2 filesystem-specific
programs.

%description -l pt_BR devel
Bibliotecas e arquivos de inclusão para desenvolvimento de programas
específicos para sistema de arquivo ext2.

%description -l es devel
Bibliotecas y archivos de inclusión para desarrollo de programas
específicos para sistema de archivo ext2.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --enable-elf-shlibs

make libs progs docs

%install
export PATH=/sbin:$PATH
make install DESTDIR="$RPM_BUILD_ROOT"
make install-libs DESTDIR="$RPM_BUILD_ROOT"






mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/e2fsprogs-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr (-, root, root)
%doc README RELEASE-NOTES
/sbin/e2fsck
/sbin/e2label
/sbin/fsck.ext2
/sbin/debugfs
/sbin/mke2fs
/sbin/badblocks
/sbin/tune2fs
/sbin/dumpe2fs
/sbin/fsck
/usr/sbin/mklost+found
/sbin/mkfs.ext2

/lib/libe2p.so.2.3
/lib/libext2fs.so.2.4
/lib/libss.so.2.0
/lib/libcom_err.so.2.0
/lib/libuuid.so.1.2

/usr/bin/chattr
/usr/bin/lsattr
/usr/man/man8/e2fsck.8
/usr/man/man8/e2label.8
/usr/man/man8/debugfs.8
/usr/man/man8/tune2fs.8
/usr/man/man8/mklost+found.8
/usr/man/man8/mke2fs.8
/usr/man/man8/dumpe2fs.8
/usr/man/man8/badblocks.8
/usr/man/man8/fsck.8
/usr/man/man1/chattr.1
/usr/man/man1/lsattr.1
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%files devel
%defattr (-, root, root)
/usr/info/libext2fs.info*
/usr/lib/libe2p.a
/usr/lib/libext2fs.a
/usr/lib/libss.a
/usr/lib/libcom_err.a
/usr/lib/libuuid.a
/usr/include/ss
/usr/include/ext2fs
/usr/include/et
/usr/include/uuid
/usr/lib/libe2p.so
/usr/lib/libext2fs.so
/usr/lib/libss.so
/usr/lib/libcom_err.so
/usr/lib/libuuid.so
/usr/bin/mk_cmds
/usr/bin/compile_et
/usr/share/et/et_c.awk
/usr/share/et/et_h.awk
/usr/share/ss/ct_c.awk
/usr/share/ss/ct_c.sed
/usr/man/man1/compile_et.1
/usr/man/man3/com_err.3

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 19 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 02 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- traduções para pt_BR incluídas para Summary, %description e Group
- manuais traduzidos para pt_BR
- %defattr (-, root, root)

* Sat Dec  5 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Tue Nov 17 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Tue Jul 14 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- i18n patches
