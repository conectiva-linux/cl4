%define kdeprefix /usr
%define version 1.1.1
%define kderelease 2cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source

%define compiler egcs
%define conectiva versão-conectiva >= 3.0
%define qtver  qt >= 1.42

%define kdename kdelibs
Name: %{kdename}
Summary: K Desktop Environment - Libraries
Summary(pt_BR): K Desktop Environment - bibliotecas
Summary(es): K Desktop Environment - bibliotecas
Version: %{version}
Release: %{kderelease}
Source: ftp://ftp.kde.org:/pub/kde/%{sourcedir}/%{kdename}-%{version}.tar.bz2
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Copyright: LGPL
BuildRoot: /var/tmp/%{kdename}-buildroot
Requires: %{qtver} %{conectiva} kdesupport
Prefix: %{kdeprefix}

%define packages main
%define main kdecore kdeui jscript kimgio khtmlw kfmlib kfile mediatool kspell kab po doc toolbar
%define subdirs %main

%description
Libraries for the K Desktop Environment: 
KDE Libraries included: kdecore (KDE core library), kdeui (user interface), 
kfm (file manager), khtmlw (HTML widget), kfile (file access), kspell 
(spelling checker), jscript (javascript), kab (addressbook), kimgio (image 
manipulation), mediatool (sound, mixing and animation).

%description -l pt_BR
Bibliotecas para o KDE.

Incluídos neste pacote:

jscript: biblioteca javascript kdecore: biblioteca base kdeui:
biblioteca da interface do usuário kfmlib: biblioteca do gerenciador
de arquivos khtmlw: widgets HTML mediatool: biblioteca para
ferramentas multimídia

%description -l es
Bibliotecas para KDE.  Incluidos en este paquete: jscript: biblioteca
javascript kdecore: biblioteca base kdeui: biblioteca de la interface
del usuario kfmlib: biblioteca del administrador de archivos khtmlw:
widgets HTML mediatool: biblioteca para herramientas multimedia

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{kdename}-%{version}

%build
[ "$LINGUAS" ] && unset LINGUAS
export KDEDIR=%{kdeprefix}
CC=%{compiler} ./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check 

make CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions" KDEDIR=%{kdeprefix}

%install
export KDEDIR=%{kdeprefix}
for subdir in %{subdirs} ; do
    rm -rf $RPM_BUILD_ROOT/*
    cd $RPM_BUILD_DIR/%{kdename}-%{version}/$subdir
    make prefix=$RPM_BUILD_ROOT%{kdeprefix} install-strip
    cd $RPM_BUILD_ROOT
    tar -cvf $RPM_BUILD_DIR/$subdir.tar .%{kdeprefix}
done

cd $RPM_BUILD_ROOT
for package in %{packages} ; do
    #Erase all
    rm -rf $RPM_BUILD_ROOT/*
    pkgdirs=""
    if [ "$package" = "main" ] ; then pkgdirs="%{main}" ; fi
    for subdir in $pkgdirs ; do
       tar -xvf $RPM_BUILD_DIR/$subdir.tar
       rm $RPM_BUILD_DIR/$subdir.tar
    done
    chmod a+x $RPM_BUILD_ROOT%{kdeprefix}/lib/*
    tar -cvf $RPM_BUILD_DIR/$package.pkg.tar .

    # Get the file list
    find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
        $RPM_BUILD_DIR/file.list.%{kdename}.$package

    find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
        -e '/\/config\//s|^|%config|' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}.$package

    find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}.$package
    # Ok. Let's go again with other packages
done

# Now put back subpackage files
cd $RPM_BUILD_ROOT
for package in %{packages} ; do
    tar -xvf $RPM_BUILD_DIR/$package.pkg.tar
done

%clean
# Let's clean the garbage
rm -rf $RPM_BUILD_ROOT
for package in %{packages} ; do
    rm -f $RPM_BUILD_DIR/file.list.%{kdename}.$package
    rm -f $RPM_BUILD_DIR/$package.pkg.tar
done

%post 
# Refresh the ldlibraries
/sbin/ldconfig

%postun
# Refresh the ldlibraries
/sbin/ldconfig

%files -f ../file.list.%{kdename}.main

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 30 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 1.1.1
- Merged spec file with the kde team's original
- Files in KDEDIR/share/applnk is no longer treated as %config files

* Mon Mar 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- with exceptions

* Mon Mar 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed findrequires and libungif 4.1

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Mar 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- removed -no-rtti, it is needed by kpilot, among others...

* Wed Mar 03 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Fix for tmp race

* Fri Feb 26 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Compiled with -fno-exceptions -fno-rtti

* Thu Jan 18 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- added pt_BR translations
