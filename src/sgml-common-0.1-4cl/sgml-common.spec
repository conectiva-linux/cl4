Summary: Common SGML catalog and DTD files
Summary(pt_BR): Arquivos DTD e catálogos SGML.
Summary(es): Archivos DTD e catálogos comunes.
Name: sgml-common
%define version 0.1
%define release 4cl
version: %{version}
release: %{release}
Source: sgml-common.tgz
Copyright: (C) International Organization for Standardization 1986
Group: Utilities/Text
Group(pt_BR): Utilitários/Texto
Group(es): Utilitarios/Texto
BuildRoot: /tmp/sgmlroot
%define sgmlbase /usr

%description
  sgml-common is a collection of entities and dtds that are useful for
SGML processing, but shouldn't need to be included in multiple packages.
It also includes an up-to-date Open Catalog file.

%description -l pt_BR
O sgml-common é uma coleção de entidades e dtds que são úteis para o
processamento SGML, mas não é necessário inclui-lo em vários pacotes.
Também inclui um arquivo atualizado Open Catalog.

%description -l es
Archivos DTD e catálogos comunes.

%prep
%setup -c
%build
gawk --posix '/Typical invocation:/,/\-\-\>/ { print }' sgml-common/* |
gawk --posix '/PUBLIC/ { sys=$3 } 
	/8879:1986.*\"\>/ { saveline=""; print "PUBLIC " $0 " " sys; next }
	/8879:1986[^>]*$/ { saveline = $0; next }
	/\"\>/ { print "PUBLIC " saveline  $0 " " sys; saveline="";next }
' |
sed 's/\">/\"/' > newcat

cat > install-catalog << '__EOF__'
#!/bin/sh
set -e
sgmlbase=%{sgmlbase}/lib/sgml
state=""
package=""
version=""

for i in $*; do
  case $state in 
	"")
	  case $i in
	  --install) state="--install" ; action="install";;
	  --remove) state="--remove"   ; action="remove";;
	  --sgmlbase) state="--sgmlbase" ;;
	  --version) state="--version" ;;
	  *) cat <<__USAGE__
Usage:
 --install pkg:		installs pkg.cat in CATALOG
 --remove pkg:		removes pkg.cat from CATALOG
 --version ver:		qualify version of package
 --sgmlbase path:	changes directory for pkg.cat and CATALOG
__USAGE__
 exit 0
 ;;
	  esac
	;;
	--install) state="" ; package=$i ;; 
	--remove) state="" ; package=$i ;;
	--sgmlbase) state="" ; sgmlbase=$i;;
	--version) state="" ; version=$i ;;
  esac
done

echo "install-catalog: $action of $package DTD"

cat=$sgmlbase/CATALOG

SBEG=" -- start $package $version"
SEND=" -- end $package $version"

case $action in
  install)
	if grep -q "$SBEG" $cat
	then
	  echo "$package DTD already in catalog"
	else
	  echo "adding $package DTD to catalog"
	(echo "$SBEG -- "; 
	 cat $sgmlbase/$package.cat ;
	 echo "$SEND -- ") >> $cat
	fi
  ;;
  remove)
	if grep -q "$SBEG" $cat
	then
	  echo "removing $package$version DTD from catalog"
          sed -e "/$SBEG/,/$SEND/d" < $cat > ${cat}.new
                mv ${cat}.new ${cat}
	else
	  echo "No $package$version DTD found in catalog"
	fi
  ;;
  *) echo "install-catalog: Invalid action $action"; exit 1 ;;
esac
__EOF__
chmod +x install-catalog

%install
mkdir -p $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml
install sgml-common/* $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml
install newcat $RPM_BUILD_ROOT%{sgmlbase}/lib/sgml/sgml-common.cat
mkdir -p $RPM_BUILD_ROOT/%{sgmlbase}/bin
cp install-catalog $RPM_BUILD_ROOT/%{sgmlbase}/bin

%post
touch %{sgmlbase}/lib/sgml/CATALOG
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{sgmlbase}/bin/install-catalog --install sgml-common --version $V > /dev/null 2>&1 | :

%postun
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{sgmlbase}/bin/install-catalog --remove sgml-common --version $V > /dev/null 2>&1 | :

%files
%{sgmlbase}/lib/sgml/*
%{sgmlbase}/bin/install-catalog

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 16 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition

* Mon Apr  5 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- fixes %post script

* Thu Apr  1 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 spanish edition

* Thu Apr 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Redirected %post and %postun to /dev/null
