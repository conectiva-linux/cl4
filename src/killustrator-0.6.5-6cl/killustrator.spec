Name: killustrator
Version: 0.6.5
Release: 6cl
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Summary: A vector drawing package for KDE.
Summary(pt_BR): Um pacote para desenhos vetoriais para o KDE.
Summary(es): Un paquete para diseños vectoriales para KDE.
Copyright: GPL
Icon: killustrator.xpm
URL: http://wwwiti.cs.uni-magdeburg.de/~sattler/killustrator.html
# was .gz
Source0: http://wwwiti.cs.uni-magdeburg.de/~sattler/pub/killustrator/%{name}-%{version}.tar.bz2
Source1: killustrator-pt_BR.po
Buildroot: /var/tmp/%{name}-buildroot
Prefix: /usr

%description
KIllustrator is a vector drawing package for the K Desktop Environment
(KDE 1.1, see below) with a user interface similar to that of Corel Draw (TM).

%description -l pt_BR
O Killustrator é um pacote para desenho vetorial para o KDE. Com uma interface
similar à do Corel Draw (TM).

%description -l es
Killustrator es un paquete para diseño vectorial para KDE. Con una
interface similar a la del Corel Draw (TM).

%prep
rm -rf $RPM_BUILD_ROOT
%setup -n %{name}-%{version}

%build
cp $RPM_SOURCE_DIR/killustrator-pt_BR.po $RPM_BUILD_DIR/%{name}-%{version}/po/pt_BR.po
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS
./configure --prefix=%{prefix} --with-install-root=$RPM_BUILD_ROOT --disable-path-check
make

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install-strip

cd $RPM_BUILD_ROOT
find . -type d | grep -v "\/usr\/share\/locale" | \
	sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}

%changelog
* Tue Jun 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Jun 06 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 0.6.3 to 0.6.5

* Mon May 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with 1.44 + KDE 1.1.1

* Mon Mar 29 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt with fixed find-requires

* Thu Mar 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- some optimizations

* Thu Mar 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initial packaging
