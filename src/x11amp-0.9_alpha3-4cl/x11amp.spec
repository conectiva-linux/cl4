%define name x11amp
%define version 0.9_alpha3
%define release 4cl

Summary: X11 mp3 player with features not unlike WinAMP.
Summary(pt_BR): Player mp3 com características semelhantes ao WinAMP
Summary(es): X11 mp3 player with features not unlike WinAMP.
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
URL: http://www.x11amp.org/
Source: %{name}-0.9-alpha3.tar.bz2
Source1: %{name}.wmconfig
Source1: mp3license 
Source3: x11amp.tif
Requires: gtk+ >= 1.2.0
BuildRoot: /var/tmp/%{name}-%{version}

%description
X11amp is a X Windows based mp3 player with a nice interface
borrowed from WinAMP.

For information on the MP3 License, please visit:
http://www.mpeg.org/

%description -l pt_BR
O x11amp é um player de mp3 para o X Window System semelhante
ao WinAMP (para o Windows)

Para maiores informações sobre a licença MP3, por favor visite:
http://www.mpeg.org/

%description -l es
X11amp is a X Windows based mp3 player with a nice interface
borrowed from WinAMP.

For information on the MP3 License, please visit:
http://www.mpeg.org/

%package devel
Summary: Static libraries and header files for x11amp.
Summary(pt_BR): Arquivos de inclusão e bibliotecas estáticas para o x11amp
Summary(es): Static libraries and header files for x11amp.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: %{name}

%description devel
Static libraries and header files for building x11amp plugins.

%description -l pt_BR devel
Bibliotecas estáticas e arquivos de inclusão para desenvolvimento
de plugins para o x11amp

%description -l es devel
Static libraries and header files for building x11amp plugins.

%prep
%setup -q -n x11amp-0.9-alpha3
if [ ! -e configure ]; then
	CFLAGS=$RPM_OPT_FLAGS \
	./autogen.sh --prefix=/usr/X11R6
else
	CFLAGS=$RPM_OPT_FLAGS \
	./configure --prefix=/usr/X11R6
fi

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 644 $RPM_SOURCE_DIR/x11amp.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/x11amp
mkdir -p $RPM_BUILD_ROOT/usr/share/icons
install -m 644 $RPM_SOURCE_DIR/x11amp.tif $RPM_BUILD_ROOT/usr/share/icons/x11amp.tif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
/usr/X11R6/bin/x11amp
/usr/X11R6/lib/libx11amp.so.0
/usr/X11R6/lib/libx11amp.so.0.9.0
/usr/X11R6/lib/x11amp
/etc/X11/wmconfig/x11amp
/usr/share/icons/x11amp.tif

%files devel
%defattr(-,root,root)
/usr/X11R6/include/x11amp
/usr/X11R6/lib/libx11amp.a
/usr/X11R6/lib/libx11amp.la
/usr/X11R6/lib/libx11amp.so

%changelog
* Fri Jun 25 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Added icon

* Wed Jun 23 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations

* Mon Feb 15 1999 Michael Maher <mike@redhat.com>
- built pacakge for 6.0
- changed spec file, added mp3 licenses.

* Mon Feb 15 1999 Ryan Weaver <ryanw@infohwy.com>
  [x11amp-0.9-alpha3-1]
- Updated to alpha3 see ChangLog for changes.

* Wed Jan 13 1999 Ryan Weaver <ryanw@infohwy.com>
  [x11amp-0.9-alpha2-1]
- fixed close button in PL/EQ windows
- fixed shuffel/randomize functions
- removed imlib, no need for imlib anymore
- mpg123 plugin now works on SMP machines, also reduced cpu usage
- fixed so mainwindow will be positioned correct at startup in some windowmanagers
- fixed the playlistwindow buttons that ended up behind the window
- added mikmod plugin into the source tree
- now you can configure the OSS drivers and mpg123 plugin
- SKINSDIR variable can be used again
- added bars as analyzer mode
- in playlistwindow the player control buttons now work, also time window works
