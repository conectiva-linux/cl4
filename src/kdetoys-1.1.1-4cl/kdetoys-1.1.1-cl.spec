%define kdeprefix /usr
%define version 1.1.1
%define kderelease 4cl
%define sourcedir stable/1.1.1/distribution/tar/generic/source
%define tag -1.1.1
%define topdirtag -1.1.1

%define conectiva versão-conectiva >= 4.0
%define qtversion  qt >= 1.42

%define kdename kdetoys
%define topdir %{kdename}%{topdirtag}
Name: %{kdename}
Summary: K Desktop Environment - Toys
Summary(pt_BR): Acessórios para o KDE
Summary(es): Accesorios para KDE
Version: %{version}
Release: %{kderelease}
URL: http://www.kde.org
# was .gz
Source: ftp://ftp.kde.org:/pub/kde/%{sourcedir}/%{kdename}%{tag}.tar.bz2
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
BuildRoot: /var/tmp/%{kdename}-buildroot
Copyright: GPL
Requires: %{qtversion} %{conectiva} kdebase
Prefix: %{kdeprefix}
%define packages moonphase worldwatch mousepedometer
%define moonphase kmoon
%define worldwatch kworldwatch
%define mousepedometer mouse
%define subdirs %{moonphase} %{worldwatch} %{mousepedometer}

%description
"Toys" for the K Desktop Environment. 
Included with this package are: "Kmoon" (moon phases), "Kworldwatch" (world 
map with daylight regions), and a "mouse-pedometer".

%description -l pt_BR
Acessórios para o KDE. Este pacote contém:

- kmoon: (fases da lua)
- kworldwatch: mapa mundi com fusos horários
- mouse-pedometer: registra a quilometragem do mouse :)

%description -l es
Accesorios para KDE. Este paquete contiene: 
- kmoon: (fases de la luna)
- kworldwatch: mapa mundial con zonas horarias
- mouse-pedometer: registra el kilometraje del ratón :)

%package moonphase
Summary: K Desktop Environment - Toys - kmoon
Summary(pt_BR): kmoon - fases da lua
Summary(es): kmoon - fases de la luna
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Obsoletes: kdetoys
Copyright: GPL
Prefix: %{kdeprefix}
%description moonphase
This is the application "kmoon" from the "kdetoys" collection of KDE \
applications. It places an icon showing the current phase of the moon in the 
KDE Desktop panel.

%description -l pt_BR moonphase
Este é o aplicativo kmoon da coleção de aplicativos kdetoys para o KDE.
Mostra um ícone com a fase corrente da lua no painel do ambiente KDE.

%description -l es moonphase
Esta es la aplicación kmoon de la colección de aplicaciones kdetoys
para KDE.  Enseña un icono con la fase corriente de la luna en el
panel del ambiente KDE.

%package worldwatch
Summary: K Desktop Environment - Toys - kworldwatch
Summary(pt_BR): kworldwatch: mapa mundi com fusos horários
Summary(es): kworldwatch: mapa mundial con zonas horarias
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Obsoletes: kdetoys
Copyright: GPL
Prefix: %{kdeprefix}
%description worldwatch
This is the application "kworldwatch" from the "kdetoys" collection of KDE 
applications.  It shows a world map divided into current day/night regions, 
and reports the local and GMT time.

%description -l pt_BR worldwatch
Esta é a aplicação kworldwatch da coleção de aplicativos kdetoys para o kde.
Mostra um mapa mundi dividido em regiões de noite/dia e mostra o horário
local e GMT.

%description -l es worldwatch
Esta es la aplicación kworldwatch de la colección de aplicaciones
kdetoys para kde.  Enseña un mapa mundi dividido en regiones de
noche/día y enseña la hora local y GMT.

%package mousepedometer
Summary: K Desktop Environment - Toys - mouse (kodo)
Summary(pt_BR): kodo: registra e mostra a quilometragem do mouse.
Summary(es): kodo: registra y enseña el kilometraje del ratón.
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Obsoletes: kdetoys
Copyright: GPL
Prefix: %{kdeprefix}
%description mousepedometer
This is the application "kodo" (alias "mouse") from the "kdetoys" collection 
of KDE applications.   It is a "mouse pedometer" which measures the total 
distance your mouse pointer travels across the computer screen.

%description -l pt_BR mousepedometer
Este é o aplicativo kodo da coleção de aplicativos kdetoys para o kde.
Trata-se de um odômetro para medir a distância total percorrida pelo seu
mouse.

%description -l es mousepedometer
Esta es la aplicación kodo de la colección de aplicaciones kdetoys
para kde.  Consiste de un odómetro para medir la distancia total
recorrida por tu ratón.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{topdir}

%build
export KDEDIR=%{kdeprefix}
[ "$LINGUAS" ] && unset LINGUAS
./configure --prefix=%{kdeprefix} --with-install-root=$RPM_BUILD_ROOT
make 

%install

cd $RPM_BUILD_DIR/%{topdir}/po
rm -rf $RPM_BUILD_ROOT/*
[ "$LINGUAS" ] && unset LINGUAS
make prefix=$RPM_BUILD_ROOT%{kdeprefix} install-strip
rm -rf $RPM_BUILD_DIR/%{kdename}-po
mkdir $RPM_BUILD_DIR/%{kdename}-po
cp -a $RPM_BUILD_ROOT/* $RPM_BUILD_DIR/%{kdename}-po

for subdir in %{subdirs} ; do
	rm -rf $RPM_BUILD_ROOT/*
	cd $RPM_BUILD_DIR/%{kdename}-po
        find . -name "$subdir*" | cpio -dpv $RPM_BUILD_ROOT       
        find $RPM_BUILD_ROOT -type d -exec chmod 0755 {} ';'      
	cd $RPM_BUILD_DIR/%{topdir}/$subdir
	make prefix=$RPM_BUILD_ROOT%{kdeprefix} install-strip
	cd $RPM_BUILD_ROOT
	tar -cvf $RPM_BUILD_DIR/$subdir.tar .%{kdeprefix}
done

cd $RPM_BUILD_ROOT
for package in %{packages} ; do
	rm -rf $RPM_BUILD_ROOT/*
        pkgdirs=""
	if [ "$package" = "moonphase" ] ; then pkgdirs="%{moonphase}"
	elif [ "$package" = "worldwatch" ] ; then pkgdirs="%{worldwatch}"
	elif [ "$package" = "mousepedometer" ] ; then pkgdirs="%{mousepedometer}"
	fi
	for subdir in $pkgdirs ; do
		tar -xvf $RPM_BUILD_DIR/$subdir.tar
		rm $RPM_BUILD_DIR/$subdir.tar
	done
	tar -cvf $RPM_BUILD_DIR/$package.pkg.tar .

	find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' \
        | grep -v "\/usr\/share\/locale" >> \
		$RPM_BUILD_DIR/file.list.%{kdename}.$package

    find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
        -e '/\/config\//s|^|%config|' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}.$package

    find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}.$package
done

cd $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/*
for package in %{packages} ; do
	tar -xvf $RPM_BUILD_DIR/$package.pkg.tar
done

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{kdename}-po
for package in %{packages} ; do
	rm -f $RPM_BUILD_DIR/file.list.%{kdename}.$package
	rm -f $RPM_BUILD_DIR/$package.pkg.tar
done

%files moonphase -f ../file.list.%{kdename}.moonphase
%files worldwatch -f ../file.list.%{kdename}.worldwatch
%files mousepedometer -f ../file.list.%{kdename}.mousepedometer

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Injected new group into package

* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- requires versão-conectiva >= 4.0 (glibc 2.1, etc)
- fixed specfile wrt rpm 3.0

* Fri May 07 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Updated to 1.1.1

* Thu Apr  1 1999 Conectiva <dist@conectiva.com>
- fixed LINGUAS

* Mon Mar 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed find-requires

* Thu Mar 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- unset LINGUAS

* Mon Mar 08 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- adapted to Conectiva Linux
- %dir /usr/share/locale removed from %filelists
- added pt_BR translations

* Sat Feb 13 1999 <duncan@kde.org>
- files in KDEDIR/share/applnk no longer treated as %config files
- fix bad /opt/kde directory permissions bug 

* Mon Feb 8 1999 <duncan@kde.org>
- new rpm packaging for KDE-1.1
- relocatable rpms
- individual apps in subpackages
