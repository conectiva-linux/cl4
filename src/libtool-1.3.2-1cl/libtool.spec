Name: libtool
Version: 1.3.2
Release: 1cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Summary: The GNU libtool, which simplifies the use of shared libraries.
Summary(pt_BR): GNU libtool, uma ferramenta de geração de bibliotecas compartilhadas.
Summary(es): GNU libtool, una herramienta de creación de bibliotecas compartidas.
Source: ftp://alpha.gnu.org/gnu/libtool-%{version}.tar.gz
Patch0: libtool-%{version}-arm.patch
Patch1: libtool-1.2f-cache.patch
Prefix: %{_prefix}
PreReq: info
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-root

%description
The libtool package contains the GNU libtool, a set of shell scripts
which automatically configure UNIX and UNIX-like architectures to
generically build shared libraries.  Libtool provides a consistent,
portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, you
should install libtool.

%description -l pt_BR
GNU libtool é um conjunto de scripts shell para configurar
automaticamente a geração de bibliotecas compartilhadas para várias
arquiteturas UNIX de uma maneira genérica.

%description -l es
GNU libtool es un conjunto de scripts shell para configurar
automáticamente la creación de bibliotecas compartidas para varias
arquitecturas UNIX de una manera genérica.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure --prefix=%{_prefix} --disable-ltdl-install
make -k -C doc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}
make prefix=${RPM_BUILD_ROOT}%{_prefix} install

cd $RPM_BUILD_ROOT
  gzip -9nf .%{_prefix}/info/*.info*
# XXX remove zero length file
  rm -f .%{_prefix}/share/libtool/libltdl/stamp-h.in
# XXX forcibly break hardlinks
  mv .%{_prefix}/share/libtool/libltdl .%{_prefix}/share/libtool/libltdl-X
  mkdir .%{_prefix}/share/libtool/libltdl
  cp .%{_prefix}/share/libtool/libltdl-X/* .%{_prefix}/share/libtool/libltdl
  rm -rf .%{_prefix}/share/libtool/libltdl-X

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_prefix}/info/libtool.info.gz %{_prefix}/info/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete %{_prefix}/info/libtool.info.gz %{_prefix}/info/dir
fi

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README
%doc THANKS TODO ChangeLog demo
%{_prefix}/bin/*
%{_prefix}/info/libtool.info*
%{_prefix}/share/libtool
%{_prefix}/share/aclocal/libtool.m4

%changelog
* Tue Jun 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- traduções para pt_BR incluídas para Summary, %description e Group

* Mon Jun 14 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.3.2.

* Tue May 11 1999 Jeff Johnson <jbj@redhat.com>
- explicitly disable per-arch libraries (#2210)
- undo hard links and remove zero length file (#2689)

* Sat May  1 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.3.

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- disable the --cache-file passing to ltconfig; this breaks the older
  ltconfig scripts found around.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.2f

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- completed arm patch
- added patch to make it more arm-friendly
- upgrade to version 1.2d

* Thu May 07 1998 Donnie Barnes <djb@redhat.com>
- fixed busted group

* Sat Jan 24 1998 Marc Ewing <marc@redhat.com>
- Update to 1.0h
- added install-info support

* Tue Nov 25 1997 Elliot Lee <sopwith@redhat.com>
- Update to 1.0f
- BuildRoot it
- Make it a noarch package
