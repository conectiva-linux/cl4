%define name GXedit
%define version 1.23
%define release 2cl
%define prefix /usr

Summary: A multi-function text editor using GTK+
Summary(pt_BR): Editor de textos multifun��o que usa o GTK+
Summary(es): Editor de textos multifunciones que usa GTK+

Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Editors
Group(pt_BR): Aplica��es/Editores
Group(es): Aplicaciones/Editores

Copyright: Freely distributable
Url: http://devplanet.fastethernet.net/gxedit.html
Source: %{name}%{version}.tar.bz2
Source1: GXedit.desktop
Source2: gxedit-config.h

Patch: gxedit-1.23-makefile.patch

Buildroot: /var/tmp/%{name}-%{version}-%{release}-root

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 01 1999 Michael Fulbright <drmike@redhat.com>
- version 1.23

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries

* Sun Mar 06 1999 Michael Fulbright <drmike@redhat.com>
- version 1.22

* Wed Jan 27 1998 Michael Fulbright <drmike@redhat.com>
- first attempt at spec file

%description
Here is a fast, easy-to-use editor which is both network-
oriented and very secure. GXedit is a graphical text editor
which features a toolbar, network bar and tooltips, spell
checking, inline help, the ability to send text as e-mail, 
macros and more. GXedit was designed to balance these and
many other features without becoming too bloated.

You'll need GTK+ to use GXedit.

%description -l pt_BR
O GXedit � um editor de textos gr�ficos com m�ltiplas fun��es que
utiliza o GTK+.

%description -l es
Editor de textos multifunciones que usa GTK+

%prep
%setup -n GXedit%{version} -q
%patch -p1
cd ${RPM_BUILD_DIR}/%{name}%{version}
cp %{SOURCE2} ./config.h

sed s^/usr/doc/GXedit/^/usr/doc/GXedit-%{version}/^g gxedit.c > gxedit.c.new
mv gxedit.c.new gxedit.c

%build
make gxe

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
make SHARE=$RPM_BUILD_ROOT%{prefix}/share INSTALL_DIR=$RPM_BUILD_ROOT%{prefix}/bin/ install

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications
install -c -m 664 %{SOURCE1} $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications

# strip binaries
strip `file $RPM_BUILD_ROOT/%{prefix}/bin/* | awk -F':' '/executable/ { print $1 }'`


%files
%doc docs/manual.txt docs/manual.ps docs/quickref.txt docs/quickref.ps
%doc docs/COPYING README CHANGELOG
%attr(755,root,root) %{prefix}/bin/
%{prefix}/share/gnome/apps/Applications/GXedit.desktop
%{prefix}/share/GXedit

%clean
rm -r $RPM_BUILD_ROOT
