# Note that this is NOT a relocatable package
%define ver      0.4.9.5
%define rel      1cl
%define prefix   /usr

Summary:   Balsa Mail Client
Summary(pt_BR): Balsa é um leitor de e-mail. Usa o toolkit GTK.
Summary(es): Balsa es un lector de e-mail. Usa el toolkit GTK.
Name:      balsa
Version:   %ver
Release:   %rel
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source0:   balsa-%{PACKAGE_VERSION}.tar.bz2
URL:       http://www.balsa.net/
BuildRoot: /tmp/balsa-%{PACKAGE_VERSION}-root
Requires: gtk+ >= 1.2.0
Requires: gnome-libs >= 1.0.0
Docdir: %{prefix}/doc

%description
Balsa is a e-mail reader.  This client is part of the GNOME
desktop environment.  It supports local mailboxes, POP3 and
IMAP.

%description -l pt_BR
Balsa é um leitor de e-mail. Usa o toolkit GTK.

%description -l es
Balsa es un lector de e-mail. Usa el toolkit GTK.

%prep
%setup -q

%build
unset LINGUAS

# Needed for snapshot releases.
if [ ! -f configure ]; then
%ifarch alpha
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --host=alpha-conectiva-linux --prefix=%prefi
x 
%else
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix 
%endif
else
%ifarch alpha
CFLAGS="$RPM_OPT_FLAGS" ./configure --host=alpha-conectiva-linux --prefix=%prefix
%else
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix 
%endif
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,profile.d,X11/wmconfig}

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog NEWS TODO
%{prefix}/bin/balsa
%{prefix}/share/*
#%{prefix}/man/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Apr 28 1999 Guilherme Manika <gwm@conectiva.com>
- Inicial para Conectiva
- unset LINGUAS

* Mon Dec 14 1998 Stuart Parmenter <pavlov@pavlov.net>
- Updated to version 0.4.8.

* Sun Sep 09 1998 Stuart Parmenter <pavlov@pavlov.net>
- Updated to version 0.4.7.

* Sun Aug 23 1998 Stuart Parmenter <pavlov@pavlov.net>
- Updated to version 0.4.5.

* Mon Aug  3 1998 Stuart Parmenter <pavlov@pavlov.net>
- Updated to version 0.4.0.

* Sun Jul 26 1998 Stuart Parmenter <pavlov@pavlov.net>
- Updated RPM file to reflect recent changes with the
  removal of c-client.

* Thu Apr 02 1998 Michael Fulbright <msf@redhat.com>
- First try at an RPM
