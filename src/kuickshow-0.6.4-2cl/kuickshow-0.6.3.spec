%define version 0.6.4
%define release 2cl
%define prefix	/usr

Summary: KuickShow
Summary(pt_BR): Kuickshow - visualizador de imagens muito rápido para o KDE
Summary(es): Kuickshow - visualizador de imágenes bastante rápido para KDE
Name: kuickshow
Version: %{version}
Release: %{release}
Source: http://www.millenniumx.de/packages/source/kuickshow-%{version}.tar.bz2
URL: http://www.millenniumx.de/kuickshow.html
Copyright: GPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
BuildRoot: /tmp/kuickshow-%{version}-root
Prefix: %{prefix}
Requires: qt >= 1.40 imlib

%description
KuickShow is a fast and comfortable imagebrowser /-viewer for the KDE.
It is based on Imlib and therefore loads many imageformats pretty fast,
e.g. jpeg, gif, tiff, png, xpm, xbm, ...

KuickShow has a clever user interface, that allows you to browse large amounts
of images in a short time. It can zoom, mirror, rotate images, adjust
brightness, contrast and gamma and can do a slideshow, of course.
It is fully configurable thru GUI dialogs.

Besides that, it offers a nice filebrowser with basic filemanager capabilities
like renaming, deleting, creating directories, ...

%description -l pt_BR
Um visualizador de imagens muito rápido para o KDE que usa
a biblioteca imlib.

%description -l es
Un visor de imágenes muy rápido para KDE que usa la biblioteca imlib.

%prep

%setup -n kuickshow-%{version}

%build
CXX=egcs CC=egcs CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions" LDFLAGS=-s ./configure --with-install-root=$RPM_BUILD_ROOT
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/%{prefix} KDEDIR=$RPM_BUILD_ROOT/%{prefix} install

cd $RPM_BUILD_ROOT

find . -type d | grep -v "\/usr\/share\/locale" | \
	sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{name}

find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{name}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}

%changelog
* Wed Jun 30 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Injected new group into package

* Tue Jun 15 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 0.6.3 to 0.6.4

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with qt 1.44 + KDE 1.1.1

* Tue Mar 23 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt agains imlib 1.9.4

* Wed Mar 17 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
