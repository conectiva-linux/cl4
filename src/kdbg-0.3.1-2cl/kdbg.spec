%define name kdbg
%define version 0.3.1
%define release 2cl
%define prefix /usr

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: KDbg - KDE Debugging GUI around gdb
Summary(pt_BR): Interface gráfica KDE para o gdb
Summary(es): KDbg - KDE Debugging GUI around gdb
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Group: Development/Debuggers
Group(pt_BR): Desenvolvimento/Depuradores
Group(es): Desarrollo/Depuradores
Copyright: GPL
Source0: %{name}-%{version}.tar.bz2
Source1: kdbg-pt_BR.po
Patch0: kdbg-0.3.1-pt_BR.patch
URL: http://members.telecom.at/~johsixt/kdbg.html
Requires: qt >= 1.30
Requires: kdelibs
BuildRoot: /tmp/build-%{name}-%{version}

%description
This is KDbg, a graphical user interface around gdb using
KDE, the K Desktop Environment.

%description -l pt_BR
Interface gráfica KDE para o gdb.

%description -l es
This is KDbg, a graphical user interface around gdb using
KDE, the K Desktop Environment.

%prep
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%setup
%patch0 -p1 -b .pt_BR
touch `find . -type f -print`

%build
cp $RPM_SOURCE_DIR/kdbg-pt_BR.po %{builddir}/po/pt_BR.po
if [ -z "$KDEDIR" ]; then
        export KDEDIR=%{prefix}
fi
autoconf
LINGUAS= CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
# Build a nice file list
cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}
rm -f $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}

%changelog
* Tue Jun 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR.po to package

* Mon Jun 21 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- included in Conectiva Linux 4.0
