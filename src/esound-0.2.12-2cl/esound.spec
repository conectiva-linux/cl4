# Note that this is NOT a relocatable package
%define ver      0.2.12
%define rel      2cl
%define prefix   /usr

Summary: The Enlightened Sound Daemon.
Summary(pt_BR): O servidor de som do Enlightenment
Summary(es): El servidor de sonido del Enlightenment
Name:      esound
Version:   %ver
Release:   %rel
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0:   esound-%{PACKAGE_VERSION}.tar.gz
URL:       http://pw1.netcom.com/~ericmit/EsounD.html
BuildRoot: /var/tmp/esound-%{PACKAGE_VERSION}-root

%description
EsounD -- the Enlightened Sound Daemon -- is a server process
that allows multiple applications to share a single sound
card. For example, when you're listening to music from your CD
and you receive a sound-related event from ICQ, your applications
won't have to jockey for the attention of your sound card.

EsounD mixes several audio streams for playback by a single
audio device.

Install esound if you'd like to allow for such event sharing
by your audio device.

%description -l pt_BR
O servidor de som "iluminado" é um processo que permite que múltiplas
aplicações compartilhem uma placa de som.

%description -l es
El servidor de sonido "iluminado" es en proceso que permite que
múltiples aplicaciones compartan una misma tarjeta de sonido.

%package devel
Summary: Libraries, includes and more to develop EsounD applications.
Summary(pt_BR): Bibliotecas, arquivos de inclusão, etc para desenvolver aplicações EsounD
Summary(es): Bibliotecas, archivos de inclusión, etc para desarrollar aplicaciones EsounD
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: esound

%description devel
Libraries, include files and other resources you can use
to develoop EsounD applications.

%description -l pt_BR devel
Bibliotecas, arquivos de inclusão, etc, para que você possa
desenvolver aplicações que usem o servidor de som EsounD.

%description -l es devel
Bibliotecas, archivos de inclusión, etc, para que puedas desarrollar
aplicaciones que usen el servidor de sonido EsounD.

%prep
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
./configure --prefix=%prefix
make

%install

make prefix=$RPM_BUILD_ROOT%{prefix} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog EsounD.html INSTALL NEWS README TIPS TODO
%{prefix}/bin/*
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/include/*
%{prefix}/share/aclocal/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue May 04 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Version 0.2.12

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- version 0.2.8

* Wed Feb 3 1999 Jonathan Blandford <jrb@redhat.com>
- bug fixes -- new release.

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated in preparation of GNOME freeze

* Sat Nov 21 1998 Pablo Saratxaga <srtxg@chanae.alphanet.ch>
- added %{prefix}/share/aclocal/* to %files devel
- added spanish and french translations for rpm

* Thu Oct 1 1998 Ricdude <ericmit@ix.netcom.com>
- make autoconf do the version updating for us.

* Wed May 13 1998 Michael Fulbright <msf@redhat.com>
- First try at an RPM
