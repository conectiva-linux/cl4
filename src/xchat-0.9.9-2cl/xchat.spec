%define name xchat
%define version 0.9.9
%define release 2cl
%define prefix /usr

Summary: Gtk+ IRC client
Summary(pt_BR): Cliente IRC usando GTK+
Summary(es): Cliente IRC GTK+
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Copyright: Freely distributable
Url: http://xchat.linuxpower.org
Source: http://xchat.linuxpower.org/files/xchat-%{version}.tar.bz2
Source1: xchat.desktop
Source2: xchat.png
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root

%changelog

* Sun Jun 20 1999 Marcelo Tosatti <marcelo@conectiva.com>
- updated to 0.9.9

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 29 1999 Conectiva <dist@conectiva.com>
- updated to 0.9.4

* Wed Mar 24 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 22 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.3

* Mon Mar 8 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.2

%description
X-Chat is yet another IRC client for the X Window
System, using the Gtk+ toolkit. It is pretty easy
to use compared to the other Gtk+ IRC clients and
the interface is quite nicely designed.

%description -l pt_BR
Cliente IRC usando GTK+.

%description -l es
Cliente IRC GTK+.

%prep

%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
unset LINGUAS
./configure --prefix=%{prefix} \
			--enable-gnome --enable-perl
make

%install

mkdir -p $RPM_BUILD_ROOT%{prefix}
make prefix=$RPM_BUILD_ROOT%{prefix} install-strip

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Internet
install -c -m 664 %{SOURCE1} $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Internet/

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/pixmaps
install -c -m 664 %{SOURCE2} $RPM_BUILD_ROOT%{prefix}/share/pixmaps/

%files
%doc README ChangeLog
%attr(755,root,root) %{prefix}/bin/xchat
%{prefix}/share/gnome/apps/Internet/xchat.desktop
%{prefix}/share/pixmaps/xchat.png

%clean
rm -r $RPM_BUILD_ROOT
