Name: qt
Summary: Shared library for the Qt GUI toolkit
Summary(pt_BR): Estrutura para rodar aplicações GUI Qt: biblioteca compartilhada
Summary(es): Estructura para ejecutar aplicaciones GUI Qt: biblioteca compartida
Version: 1.44
Release: 4cl
Source: ftp://ftp.troll.no/qt/source/%{name}-%{version}.tar.bz2
Patch0: qt-1.44-enablegif.patch
URL: http://www.troll.no
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Buildroot: /var/tmp/qt-buildroot
Serial: 1

%package devel
Summary: Development files and documentation for the Qt GUI toolkit
Summary(pt_BR): Arquivos de inclusão e documentação necessária para compilar aplicações Qt.
Summary(es): Archivos de inclusión y documentación necesaria para compilar aplicaciones Qt.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description
Qt is a GUI software toolkit. Qt simplifies the task of writing and
maintaining GUI (graphical user interface) applications for X Windows.

Qt is written in C++ and is fully object-oriented. It has everything
you need to create professional GUI applications. And it enables you
to create them quickly.

Qt is a multi-platform toolkit. When developing software with Qt, you
can run it on the X Window System (Unix/X11) or Microsoft Windows NT
and Windows 95/98. Simply recompile your source code on the platform
you want.

This package contains the shared library needed to run Qt applications,
as well as the README files for Qt.

%description -l pt_BR
Contém as bibliotecas compartilhadas necessárias para rodar
aplicações Qt, bem como os arquivos README.

%description -l es
Contiene las bibliotecas compartidas necesarias para ejecutar
aplicaciones Qt, bien como los archivos README.

%description devel
Contains the files necessary to develop applications using Qt: header
files, the Qt meta object compiler, man pages, HTML documentation and
example programs.  See http://www.troll.no for more information about
Qt, or file:/usr/lib/qt/html/index.html for Qt documentation in HTML.

%description -l pt_BR devel
Contém os arquivos necessários para desenvolver aplicaçõese
usando Qt: arquivos de inclusão, compilador de meta-objetos Qt,
páginas de manual, documentação HTML e programas exemplo. Veja
http://www.troll.no para mais informações sobre o Qt, ou o arquivo
file:/usr/lib/qt/html/index.html na documentação em HTML.


%description -l es devel
Contiene los archivos necesarios para desarrollar aplicaciones
usando Qt: archivos de inclusión, compilador de metaobjetos Qt,
páginas de manual, documentación HTML y programas ejemplo. Mira
http://www.troll.no para más información sobre el Qt, o el
archivo file:/usr/lib/qt/html/index.html en la documentación
en HTML.

%prep
%setup -q
%patch -p1 -b .enablegif
rm src/kernel/qt_gif.h.enablegif

%build
QTDIR=`/bin/pwd` export QTDIR
make linux-g++-shared
make
make linux-g++-static
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/lib 
mkdir -p $RPM_BUILD_ROOT/usr/man
install -s -m 755 bin/moc $RPM_BUILD_ROOT/usr/bin/moc
cp lib/libqt.a $RPM_BUILD_ROOT/usr/lib
cp lib/libqt.so.%{version} $RPM_BUILD_ROOT/usr/lib
ln -sf libqt.so.%{version} $RPM_BUILD_ROOT/usr/lib/libqt.so.1
ln -sf libqt.so.1 $RPM_BUILD_ROOT/usr/lib/libqt.so
cp -fR man/. $RPM_BUILD_ROOT/usr/man
gzip -9f $RPM_BUILD_ROOT/usr/man/man*/*
mkdir -p $RPM_BUILD_ROOT/usr/lib/qt $RPM_BUILD_ROOT/usr/include/qt 
mkdir -p $RPM_BUILD_ROOT/usr/lib/qt/html $RPM_BUILD_ROOT/usr/lib/qt/tutorial 
mkdir -p $RPM_BUILD_ROOT/usr/lib/qt/examples
cp -fR html $RPM_BUILD_ROOT/usr/lib/qt
strip tutorial/*/* || :
strip examples/*/* || :
cp -fR tutorial $RPM_BUILD_ROOT/usr/lib/qt
cp -fR examples $RPM_BUILD_ROOT/usr/lib/qt
cp -fR include/. $RPM_BUILD_ROOT/usr/include/qt
for a in $RPM_BUILD_ROOT/usr/lib/qt/*/*/Makefile ; do
  sed 's-^SYSCONF_MOC.*-SYSCONF_MOC		= /usr/bin/moc-' < $a > ${a}.2
  mv -v ${a}.2 $a
done
rm $RPM_BUILD_ROOT/usr/lib/qt/*/*/*.o
chmod -R a+r $RPM_BUILD_ROOT/usr/lib/libqt.so* $RPM_BUILD_ROOT/usr/lib/qt

%post -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ANNOUNCE LICENSE README.QT FAQ PORTING README changes-1.40 changes-1.41 changes-1.42 changes-1.43 changes-1.44
/usr/lib/libqt.so.%{version}
/usr/lib/libqt.so.1
/usr/lib/libqt.so

%files devel
/usr/bin/moc
/usr/man/man1/moc.1.gz
/usr/man/man3/*.3qt.gz
/usr/lib/libqt.a
/usr/lib/qt/
/usr/include/qt/

%changelog
* Fri Jun 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed
- man pages compressed

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Apr 17 1999 Preston Brown <pbrown@redhat.com>
- static library supplied in dev package.

* Wed Apr 07 1999 Preston Brown <pbrown@redhat.com>
- turn on internal GIF reading support

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Mon Mar 15 1999 Preston Brown <pbrown@redhat.com>
- upgrade to qt 1.44.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Jan 19 1999 Preston Brown <pbrown@redhat.com>
- moved includes to /usr/include/qt

* Mon Jan 04 1999 Preston Brown <pbrown@redhat.com>
- made setup phase silent.

* Fri Dec 04 1998 Preston Brown <pbrown@redhat.com>
- upgraded to qt 1.42, released today.

* Tue Dec 01 1998 Preston Brown <pbrown@redhat.com>
- took Arnt's RPM and made some minor changes for Red Hat.
