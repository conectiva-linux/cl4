%define name gnotepad+
%define version 1.1.3
%define release 4cl
%define prefix /usr

Summary: Simple but versatile editor for X11.
Summary(pt_BR): Editor simples mas versátil para o X11
Summary(es): Sencillo pero versátil editor para el X11.
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Copyright: Freely distributable
Url: http://members.xoom.com/ackahn/gnp
# was .gz
Source: %{name}-%{version}.tar.bz2
Source1: gnotepad+.desktop
Patch0: gnotepad-gnome-menu.patch
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root
Requires: gtk+ >= 1.1.13
Requires: glib >= 1.1.13

%changelog
* Thu Jul 01 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added gnome-menu entries for gnotepad+

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 24 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added Group, Summary and %description translations
- updated to 1.1.3

* Mon Mar 08 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations

* Fri Feb 19 1998 Michael Fulbright <drmike@redhat.com>
- version 1.1.0

* Fri Jan 22 1998 Michael Fulbright <drmike@redhat.com>
- first attempt at spec file

%description
gnotepad+ is an easy-to-use, yet fairly feature-rich, simple text editor
for systems running X11 and using GTK+. It is designed for as little
bloat as possible, while still providing many of the common features found
in a modern GUI-based text editor.

%description -l pt_BR
Editor simples mas versátil para o X11

%description -l es
Sencillo pero versátil editor para el X11.

%prep
%setup -q
%patch0 -p1 -b .gnome-menu

%build

CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
unset LINGUAS
make

%install

mkdir -p $RPM_BUILD_ROOT%{prefix}
make prefix=$RPM_BUILD_ROOT%{prefix} install

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications
install -c -m 664 %{SOURCE1} $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications

%files
%doc AUTHORS NEWS README TODO ChangeLog
%attr(755,root,root) %{prefix}/bin/gnp
%{prefix}/man/man1/gnp.1
%{prefix}/share/gnome/apps/Applications/gnotepad+.desktop
%{prefix}/share/gnotepad+

%clean
rm -r $RPM_BUILD_ROOT
