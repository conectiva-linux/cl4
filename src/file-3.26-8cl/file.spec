Summary: A utility for determining file types.
Summary(pt_BR): Comando file
Summary(es): Comando file
Name: file
Version: 3.26
Release: 8cl
Copyright: distributable
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
Source: ftp://ftp.astron.com/pub/file/file-%{version}.tar.gz
Source1: gimp.magic
Source700: file-man-pt_BR.tar
Patch0: file-3.22-glibc.patch
Patch1: file-3.26-sparcv9.patch
Patch2: file-3.26-realmedia.patch
Prefix: %{_prefix}
Buildroot: /var/tmp/%{name}-root

%description
The file command is used to identify a particular file according to the
type of data contained by the file.  File can identify many different
file types, including ELF binaries, system libraries, RPM packages, and
different graphics formats.

You should install the file package, since the file command is such a
useful utility.

%description -l pt_BR
Este pacote é útil para descobrir que tipo de arquivo você está
procurando em seu sistema. Por exemplo, se um fsck resulta em um
arquivo forem armazenado no "lost+found", você pode rodar file
nele para descobrir se é seguro lê-lo com o "more" ou se ele é um
binário. Ele reconhece vários tipos de arquivos, incluindo binários
ELF, bibliotecas de sistema, pacotes RPM e vários formatos gráficos
diferentes.

%description -l es
Este paquete es útil para descubrir que tipo de archivo estás
buscando en tu sistema. Por ejemplo, si fsck resulta un archivo
que fue almacenado en el "lost+found", tu puedes ejecutar file
en él para descubrir si es seguro leerlo con el "more" o si es un
binario. Reconoce varios tipos de archivos, incluyendo binarios ELF,
bibliotecas de sistema, paquetes RPM y varios formatos gráficos
diferentes.

%prep
%setup -q
%patch0 -p1 -b .glibc
%patch1 -p1
%patch2 -p1 -b .realmedia

# This overwrites -- check on version change.
rm -f ./Magdir/gimp
cp %SOURCE1 ./Magdir/gimp

%build
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr

%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/man
make prefix=${RPM_BUILD_ROOT}%{_prefix} install

{ cd $RPM_BUILD_ROOT
  strip .%{_prefix}/bin/file
}

gzip -9f $RPM_BUILD_ROOT/usr/man/*/*
mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/file-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_prefix}/bin/file
%defattr(644,root,root)
%{_prefix}/share/magic
%{_prefix}/man/man1/file.1.gz
%{_prefix}/man/man4/magic.4.gz
%{_prefix}/man/pt_BR/man*/*

%changelog
* Thu Jul 01 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- fixed permissions
- compressed man pages

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added pt_BR and es translations
- Added pt_BR man pages

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- experimental support for realmedia files added

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binary.

* Fri Nov 27 1998 Jakub Jelinek <jj@ultra.linux.cz>
- add SPARC V9 magic.

* Tue Nov 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.26.

* Mon Aug 24 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.25.
- detect gimp XCF versions.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 3.24
- buildrooted

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 31 1997 Erik Troan <ewt@redhat.com>
- Fixed problems caused by 64 bit time_t.

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Improved recognition of Linux kernel images.
