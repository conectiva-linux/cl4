%define name wmeyes
%define version 1.0
%define release 1cl

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: xeyes for WindowMaker
Summary(pt_BR): xeyes para o WindowMaker
Summary(es): xeyes for WindowMaker

Name: %{name}
Version: %{version}
Release: %{release}
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Copyright: Freely distributable
Source0: %{name}.tgz
Source1: %{name}.wmconfig
Patch: %{name}-%{version}-sigalarm.patch.gz
Buildroot: /var/tmp/%{name}-%{version}-root
Icon: %{name}.gif

%description 
Wmeyes is an implementation of the classic X
Windows program xeyes for WindowMaker. Now
you will never loose your pointer again.

%description -l pt_BR
O wmeyes é uma implementação do xeyes clássico
do X Window System, para o WindowMaker. Agora
você nunca mais perderá o seu ponteiro do mouse
de novo.

%description -l es
Wmeyes is an implementation of the classic X
Windows program xeyes for WindowMaker. Now
you will never loose your pointer again.

%prep

%setup -c

%patch -p1

%build
xmkmf
make CFLAGS="$RPM_OPT_FLAGS"

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin $RPM_BUILD_ROOT/etc/X11/wmconfig
strip %{builddir}/wmeyes
cp %{builddir}/wmeyes $RPM_BUILD_ROOT/usr/X11R6/bin
cp $RPM_SOURCE_DIR/%{name}.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

%files
%doc README
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/wmeyes
%attr(755,root,root) /usr/X11R6/bin/wmeyes

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}

%changelog
* Thu Jul 01 1999 Eliphas Levy <eliphas@conectiva.com>
- Added to Conectiva Linux.
