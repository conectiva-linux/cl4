Summary: root dot files
Summary(pt_BR): Arquivos do super-usuário (root) que começam com ponto(.)
Summary(es): Archivos del superusuario (root) que empiezan con punto(.)
Name: rootfiles
Version: 5.2
Release: 6cl
Copyright: public domain
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: rootfiles.tar.gz
Patch0: rootfiles-jbj.patch
Patch1: rootfiles-cnc.patch
BuildRoot: /var/tmp/rootfiles
BuildArchitectures: noarch

%description
This package contains all the startup files for the root user.
These are basically the same files that are in the etcskel package.

%description -l pt_BR
Este pacote contém todos os arquivos de inicialização para o
usuário root. Estes são basicamente os mesmos arquivos que estão
no pacote etcskel.

%description -l es
Este paquete contiene todos los archivos de arranque para el usuario
root. Estos son básicamente los mismos archivos que están en el
paquete etcskel.

%prep
%setup -q -n rootfiles
%patch -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/root
tar -cvSpf- . | (cd $RPM_BUILD_ROOT/root ; tar -xSpf-)

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# we used to put .Xclients in this package -- back it up if it's been
# customized
cd /root
if [ -f .Xclients -a -x /bin/awk ]; then
    m=`md5sum .Xclients | awk '{ print $1 }'`
    if [ $m != "506b9496f2853fc9fee6c6b1c5f3ee48" ]; then
	mv .Xclients .Xclients.rpmsave
    fi
fi

%files
%defattr(-,root,root)
%config /root/.[A-z]*

%changelog
* Wed Jun 23 1999 Wanderlei Cavassin <dist@conectiva.com>
- removed *xterm definitions from /root/.Xdefaults

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Oct  9 1998 Bill Nottingham <notting@redhat.com>
- remove /root from %files (it's in filesystem)

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- portability fix for .cshrc (problem #235)
- change version to be same as release.

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Thu Mar 20 1997 Erik Troan <ewt@redhat.com>
- Removed .Xclients and .Xsession from package, added %pre to back up old
  .Xclients if necessary.
