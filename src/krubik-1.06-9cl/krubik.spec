%define	version 1.06
%define name krubik
Name: %{name}
Summary: KRubik
Summary(pt_BR): KRubik
Summary(es): KRubik
Version: %{version}
Release: 9cl
Source: http://www.fys.ruu.nl/~eendebak/kde/krubik-%{version}.tar.bz2
URL: http://www.fys.ruu.nl/~eendebak/kde/krubik.html
Patch: krubik-1.04-pt_BR.patch
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Copyright: GPL
BuildRoot: /tmp/realhot_%{name}
Requires: qt >= 1.40 kdelibs libstdc++ >= 2.8.0 

%description
Rubik's cube games.

%description -l pt_BR
Jogo cubo de rubik.

%description -l es
Juego cubo de rubik.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n krubik-%{version}
%patch -p1

%build
export KDEDIR=/usr
./configure --prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT    
make KDEDIR=$KDEDIR

%install
export KDEDIR=/usr
make prefix=$RPM_BUILD_ROOT$KDEDIR install

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name} 

%changelog
* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 06 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed specfile wrt rpm 3.0
- included correct URL and Source locations

* Mon May 10 1999 Conectiva <dist@conectiva.com>
- Recopiled against qt 1.44 + KDE 1.1.1

* Wed Mar 17 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- upgraded from 1.04 to 1.06

* Mon Dec 07 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17
- kdelnk traduzido para pt_BR
- po/pt_BR incluido

* Sat Dec 05 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- inclusão no 3.0
- traduções para pt_BR incluídas para Summary, %description e Group
