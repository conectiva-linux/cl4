Summary: The Red Hat package management system.
Summary(pt_BR): Gerenciador de pacotes Red Hat
Summary(es): Gestor de paquetes Red Hat
Name: rpm
%define version 3.0.2
Version: %{version}
Release: 2cl
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
# was .gz
Source0: ftp://ftp.rpm.org/pub/rpm/dist/rpm-3.0.x/rpm-%{version}.tar.bz2
Source1: find-requires.conectiva
Source700: rpm-man-pt_BR.tar
Patch0: rpm-3.0.2-conectiva.patch
Copyright: GPL
Conflicts: patch < 2.5
%ifos linux
Prereq: gawk fileutils textutils sh-utils mktemp
%endif
BuildRoot: /var/tmp/rpm-%{version}-root

%description
The Red Hat Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages.  Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%description -l pt_BR
RPM é um poderoso gerenciador de pacotes, que pode ser usado
para construir, instalar, pesquisar, verificar, atualizar e
desinstalar pacotes individuais de software. Um pacote consiste
em uma armazenagem de arquivos, e informações sobre o pacote,
incluindo nome, versão e descrição.

%description -l es
RPM es un poderoso administrador de paquetes, que puede ser usado
para construir, instalar, pesquisar, verificar, actualizar y
desinstalar paquetes individuales de software. Un paquete consiste
en un almacenaje de archivos, y información sobre el paquete,
incluyendo nombre, versión y descripción.

%package devel
Summary: Development files for applications which will manipulate RPM packages.
Summary(pt_BR): Arquivos de inclusão e bibliotecas para programas de manipulação de pacotes rpm
Summary(es): Archivos de inclusión y bibliotecas para programas de manipulación de paquetes rpm
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: popt

%description devel
This package contains the RPM C library and header files.  These
development files will simplify the process of writing programs
which manipulate RPM packages and databases and are intended to make
it easier to create graphical package managers or any other tools
that need an intimate knowledge of RPM packages in order to function.

This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.

%description -l pt_BR devel
O sistema de empacotamento RPM inclui uma biblioteca C que torna
fácil a manipulação de pacotes e bases de dados RPM. Seu objetivo
é facilitar a criação de gerenciadores gráficos de pacotes e outras
ferramentas que precisem de conhecimento profundo de pacotes RPM.

%description -l es devel
El sistema de empaquetado RPM incluye una biblioteca C que vuelve
fácil la manipulación de paquetes y bases de datos RPM. Su objetivo
es facilitar la creación de administradores gráficos de paquetes
y otras herramientas que necesiten un conocimiento profundo de
paquetes RPM.

%prep
%setup -q
%patch0 -p1

%build
[ "$LINGUAS" ] && unset LINGUAS
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib

mkdir -p $RPM_BUILD_ROOT/usr/src/rpm/SOURCES
mkdir -p $RPM_BUILD_ROOT/usr/src/rpm/SPECS
mkdir -p $RPM_BUILD_ROOT/usr/src/rpm/SRPMS
mkdir -p $RPM_BUILD_ROOT/usr/src/rpm/BUILD
mkdir -p $RPM_BUILD_ROOT/usr/src/rpm/RPMS/${RPM_ARCH}
mkdir -p $RPM_BUILD_ROOT/usr/src/rpm/RPMS/noarch

make DESTDIR="$RPM_BUILD_ROOT" install

{ cd $RPM_BUILD_ROOT
  strip ./bin/rpm
  strip ./usr/bin/rpm2cpio
  strip ./usr/lib/rpm/rpmputtext ./usr/lib/rpm/rpmgettext
}

cp -f $RPM_SOURCE_DIR/find-requires.conectiva \
	$RPM_BUILD_ROOT/usr/lib/rpm/find-requires






mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/rpm-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/rpm --initdb
%ifos linux
if [ ! -e /etc/rpm/macros -a -e /etc/rpmrc -a -f /usr/lib/rpm/convertrpmrc.sh ] 
then
	sh /usr/lib/rpm/convertrpmrc.sh 2>&1 > /dev/null
fi
%endif

%files
%defattr(-,root,root)
%doc RPM-PGP-KEY CHANGES GROUPS
%doc docs/*
/bin/rpm
/usr/bin/rpm2cpio
/usr/bin/gendiff
/usr/man/man8/rpm.8
/usr/man/man8/rpm2cpio.8
/usr/lib/rpm
#/usr/lib/rpmrc
#/usr/lib/rpmpopt
%dir /usr/src/rpm
%dir /usr/src/rpm/BUILD
%dir /usr/src/rpm/SPECS
%dir /usr/src/rpm/SOURCES
%dir /usr/src/rpm/SRPMS
%dir /usr/src/rpm/RPMS
/usr/src/rpm/RPMS/*
/usr/share/locale/*/LC_MESSAGES/rpm.mo
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%files devel
%defattr(-,root,root)
/usr/include/rpm
/usr/lib/librpm.a
/usr/lib/librpmbuild.a

%changelog
* Mon Jun 28 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated rpm to 3.0.2-SNAP-19990628
  (Just in case we need to do it again:
  export CVSROOT=':pserver:anonymous@cvs.rpm.org:/cvs/devel'
  cvs login
  <enter>
  cvs -z3 checkout rpm
  cvs logout
  ;)

* Sat Jun 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated rpm to 3.0.2 (Snapshot version)
- Ported conectiva patch to rpm 3.0.2

* Thu Jun 10 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated rpm to 3.0.1 (final)
- Ajusted some rpm macros to work with conectiva
- Added /usr/lib/librpmbuild.a to rpm-devel filelist

* Thu May 20 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Updated rpm to 3.0.1 (Snapshot version)
- Compiled with glibc 2.1.x, egcs 1.1.x and kernel 2.2.x
- traduções para pt_BR incluídas para Summary, %description e Group
- use /usr/src/rpm, instead of /usr/src/redhat
- Added pt_BR man pages
- unset LINGUAS
- use our own modified find-requires
