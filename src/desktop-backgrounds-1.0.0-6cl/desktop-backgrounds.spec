%define  ver     1.0.0
%define  rel     6cl
%define  prefix  /usr

Summary: Desktop Background Images.
Summary(pt_BR): Imagens de fundo para o seu desktop
Summary(es): Desktop Background Images.
Name: desktop-backgrounds
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: space-1.0.0.tar.gz
Source1: gnome-tiles-1.0.0.tar.gz
Source2: Propaganda-1.0.0.tar.gz
Source3: README.Propaganda
Source4: README.space
Source5: PHOTO_FAQ.ps

BuildRoot:/var/tmp/desktop-backgrounds-%{PACKAGE_VERSION}-root

Obsoletes: gnome-imglib

BuildArchitectures: noarch

%description
If you use a desktop environment like GNOME you can use these images
to spruce up your background.

%description -l pt_BR
Se você utiliza um ambiente de trabalho como o GNOME ou o KDE, você
pode utilizar estas imagens para modificar o fundo da sua tela.

%description -l es
If you use a desktop environment like GNOME you can use these images
to spruce up your background.

%prep
%setup -c desktop-backgrounds-%{ver} -T -D

cp %{SOURCE3} $RPM_BUILD_DIR/desktop-backgrounds-%{ver}
cp %{SOURCE4} $RPM_BUILD_DIR/desktop-backgrounds-%{ver}
cp %{SOURCE5} $RPM_BUILD_DIR/desktop-backgrounds-%{ver}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/pixmaps/backgrounds
cd $RPM_BUILD_ROOT%{prefix}/share/pixmaps/backgrounds
tar xzf %{SOURCE0}
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr  2 1999 Jonathan Blandford <jrb@redhat.com>
- added propaganda tiles.  Spruced it up a bit
- moved README files out of tarball, and into docs dir.

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- First attempt

%files
%defattr(-, root, root)
%doc README.space README.Propaganda PHOTO_FAQ.ps
%{prefix}/share/pixmaps/backgrounds/space
%{prefix}/share/pixmaps/backgrounds/tiles
%{prefix}/share/pixmaps/backgrounds/Propaganda
