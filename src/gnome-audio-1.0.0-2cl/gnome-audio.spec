%define  ver     1.0.0
%define  rel     2cl
%define  prefix  /usr

Summary: Sounds for GNOME events.
Summary(pt_BR): Sons para os eventos do GNOME
Summary(es): Sonidos para GNOME.
Name: gnome-audio
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-audio-%{ver}.tar.bz2
BuildRoot:/var/tmp/gnome-audio-guide-%{PACKAGE_VERSION}-root
URL: http://www.gnome.org
BuildArchitectures: noarch

%description
If you use the GNOME desktop environment, you may want to
install this package of complementary sounds.

%description -l pt_BR
Sons para os eventos do GNOME

%description -l es
Sonidos para GNOME.

%prep
%setup -q

%package extra
Summary: Optional sounds for the GNOME desktop.
Summary(pt_BR): Sons opcionais para o ambiente GNOME.
Summary(es): sonidos extras para GNOME.
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas

%description extra
This package contains extra sound files useful for customizing the
sounds that the GNOME desktop environment makes.

%description -l pt_BR extra
Sons opcionais para o ambiente GNOME.

%description -l es extra
sonidos extras para GNOME.

%install

mkdir -p $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/%{prefix} install 

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Mar 07 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.0 - made extra subpackage

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.8

* Tue Jan 26 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.4

* Thu Dec 17 1998 Michael Fulbright <drmike@redhat.com>
- first pass at a spec file

%files
%defattr(-, root, root)
%doc README
%{prefix}/share/sounds/shutdown1.wav
%{prefix}/share/sounds/startup3.wav
%{prefix}/share/sounds/panel
%{prefix}/share/sounds/gtk-events

#symlinks
%{prefix}/share/sounds/login.wav
%{prefix}/share/sounds/logout.wav

%files extra
%{prefix}/share/sounds/card_shuffle.wav
%{prefix}/share/sounds/phone.wav
%{prefix}/share/sounds/startup1.wav
%{prefix}/share/sounds/startup2.wav
