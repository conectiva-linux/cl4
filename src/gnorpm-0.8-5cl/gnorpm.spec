%define prefix /usr
%define ver    0.8

Summary: A graphical front end to the Red Hat Package Manager, for GNOME
Summary(pt_BR): Uma interface gráfica para o gerenciador de pacotes RPM para o GNOME
Summary(es): Una interface gráfica para el administrador de paquetes RPM para el GNOME.
Name: gnorpm
Version: %ver
Release: 5cl
Copyright: GPL
Group: Utilities/System
Source: ftp://ftp.daa.com.au/pub/james/gnome/gnorpm-%{ver}.tar.gz
Patch0: gnorpm-redhat-config.patch
Patch1: gnorpm-0.8-rpm-3.0.patch
BuildRoot: /var/tmp/gnorpm-%{PACKAGE_VERSION}-root
Obsoletes: glint

%description
Gnome RPM is a graphical front end to RPM, similar to Glint, but written with
the GTK widget set and the GNOME libraries.  It is currently under
development, so there are some features missing, but you can currently query
packages in the filesystem and database, install upgrade, uninstall and
verify packages.

%description -l pt_BR
Uma interface gráfica para o gerenciador de pacotes RPM para o GNOME, similar
ao glint, mas escrita usando o conjunto de componentes GTK e as bibliotecas do
GNOME. Ainda está em desenvolvimento, desta forma algumas características ainda
não foram implementadas, mas é possível consultar pacotes, instalar, atualizar,
desinstalar e verificar pacotes.

%description -l es
Una interface gráfica para el administrador de paquetes RPM para el GNOME.

%prep
%setup -q -n gnorpm-%{ver}
%patch0 -p 1 -b .rhconfig
%patch1 -p 0 -b .rpm30

%build
[ "$LINGUAS" ] && unset LINGUAS
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install
strip $RPM_BUILD_ROOT%{prefix}/bin/gnorpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{prefix}/bin/gnorpm
%{prefix}/share/gnome/apps/*
%{prefix}/share/gnome/help/gnorpm/C/*
%{prefix}/share/locale/*/LC_MESSAGES/gnorpm.mo
%config %{prefix}/share/gnorpmrc
%config %{prefix}/share/mime-info/gnorpm.keys
#%{prefix}/share/pixmaps/defpackage.gif
%doc AUTHORS NEWS README

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- unset LINGUAS

* Fri Apr 16 1999 Matt Wilson <msw@redhat.com>
- fixed upgrade brokenness

* Thu Apr 15 1999 Michael Fulbright <drmike@redhat.com>
- added missing gnorpm.keys file to file list

* Mon Apr 12 1999 Matt Wilson <msw@redhat.com>
- updated to 0.8

* Fri Mar 12 1999 Matt Wilson <msw@redhat.com>
- patched to work with rpm-3.0
- GnoRPM obsoletes glint.
