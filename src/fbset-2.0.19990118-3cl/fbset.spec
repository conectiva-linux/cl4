Summary: Framebuffer utilities for changing video modes.
Summary(pt_BR): Utilitários para configuração do framebuffer no Linux
Summary(es): Framebuffer utilities for changing video modes.
Name: fbset
Version: 2.0.19990118
Release: 3cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: http://www.cs.kuleuven.ac.be/~geert/bin/fbset-19990118.tar.gz
Patch: fbset-2.0-pre-19981028.patch
BuildRoot: /var/tmp/%{name}-root

%description
fbset is a utility for querying and changing video modes of fbcon consoles.

%description -l pt_BR
O fbset é um utilitários para consulta e modificação de modos de vídeo
para consoles fbcon (Ie: com suporte à framebuffer)

%description -l es
fbset is a utility for querying and changing video modes of fbcon consoles.

%prep
%setup -q -n fbset
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/dev
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make install PREFIX=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/sbin/fbset
%ifarch sparc sparc64
mkdir -p $RPM_BUILD_ROOT/etc
cp etc/fb.modes.ATI $RPM_BUILD_ROOT/etc/fb.modes
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/dev/*
/usr/sbin/*
/usr/man/man[58]/*
%ifarch sparc sparc64
%config /etc/fb.modes
%endif

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- include fb devs too (#1515)
- update to 19990118 version.

* Thu Nov  5 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.
- upgrade to 19981104.

* Thu Oct 29 1998 Jakub Jelinek <jj@ultra.linux.cz>
- new package
