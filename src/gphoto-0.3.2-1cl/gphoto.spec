%define ver	0.3.2
%define rel	1cl
%define prefix	/usr

Summary: GNU Photo (gphoto)
Summary(pt_BR): GNU Photo (gphoto)
Summary(es): GNU Photo (gphoto)
Name: gphoto        
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: http://www.mustec.eu.org/~psj/downloads/gphoto-%{ver}.tar.bz2
BuildRoot: /var/tmp/gphoto-root
URL: http://www.gphoto.org/
Docdir: %{prefix}/doc
Requires: gtk+ >= 1.2.0

%description
gphoto is part of the GNOME project and is
a fine interface for a wide variety of digital
cameras

%description -l pt_BR
O programa gphoto faz parte do projeto GNOME e é uma interface
para uma grande variedade de câmeras fotográficas digitais.

%description -l es
gphoto is part of the GNOME project and is
a fine interface for a wide variety of digital
cameras

%prep
%setup -q

%build
unset LINGUAS
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%post
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING CREDITS ChangeLog FAQ MANUAL NEWS README THEMES
%{prefix}/man/man1/gphoto.1
%{prefix}/bin/*
%{prefix}/share/gphoto/drivers/*
%{prefix}/share/gphoto/gallery/Default/*
%{prefix}/share/gphoto/gallery/RedNGray/*

