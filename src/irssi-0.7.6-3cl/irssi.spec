Name: irssi
Version: 0.7.6
Release: 3cl
Summary: Irssi is a GTK based IRC client
Summary(pt_BR): Cliente IRC baseado em gtk
Summary(es): Cliente IRC basado en gtk
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
URL: http://www.sicom.fi/~ikioma/irssi.html
Source: http://www.sicom.fi/~ikioma/%{name}-%{version}.tar.bz2
Source800: irssi-wmconfig.i18n.tgz
Patch0: %{name}-%{version}-slang.patch
Requires: gtk+
Prefix: /usr
BuildRoot: /tmp/%{name}-%{version}
Obsoletes: yagirc, bezerc

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr  1 1999 Conectiva <dist@conectiva.com>
- obsoletes
- final rebuild for 3.0 spanish edition

* Mon Mar 29 1999 JT Traub <jtraub@dragoncat.net>
- Updated to 0.7.6.
- text mode client re-added.

* Thu Mar 25 1999 JT Traub <jtraub@dragoncat.net>
- Updated sources

* Sat Mar 13 1999 JT Traub <jtraub@dragoncat.net>
- Updated to 0.7.4 sources
- Added the irssi-text bin to the package.

* Mon Feb 22 1999 JT Traub <jtraub@dragoncat.net>
- Made spec file compliant with RHCN guidelines.

* Sun Feb 13 1999 JT Traub <jtraub@dragoncat.net>
- Updated to 0.6.0 sources.
- Cleaned up spec file to make it relocatable on install

* Sun Feb 7 1999  JT Traub <jtraub@dragoncat.net>
- Updated sources to 0.5.0
- removed obsolete patch lines

* Sat Feb 3 1999  JT Traub <jtraub@dragoncat.net>
- Updated sources to 0.4.0
- Deleted old patch line

* Sat Jan 30 1999  JT Traub <jtraub@dragoncat.net>
- Updated sources to 0.3.6
- Updated spec to install the .desktop file.
- Removed the now obsolete patch lines

* Wed Jan 27 1999  JT Traub <jtraub@dragoncat.net>
- Upgraded to 0.3.5

* Sun Jan 24 1999  JT Traub <jtraub@dragoncat.net>
- First attempt at building this

%description
Irssi is a GTK based GUI IRC client by Timo Sirainen <a@sicom.fi>.
More information can be found at http://www.sicom.fi/~ikioma/irssi.html.


%description -l pt_BR
Cliente irc baseado em GTK

%description -l es
Cliente IRC basado en gtk

%prep
%setup
%patch0 -p1 -b .slang

%build
./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install
strip $RPM_BUILD_ROOT%{prefix}/bin/irssi
strip $RPM_BUILD_ROOT%{prefix}/bin/irssi-text

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig




tar xvfpz $RPM_SOURCE_DIR/irssi-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr (-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog README TODO NEWS
%attr(755,root,root) %{prefix}/bin/irssi
%attr(755,root,root) %{prefix}/bin/irssi-text
%attr(644,root,root) %config %{prefix}/etc/irssi.conf
%attr(644,root,root) %{prefix}/etc/CORBA/servers/irssi.gnorba
%attr(644,root,root) %{prefix}/share/applets/Network/irssi.desktop
%attr(644,root,root) %{prefix}/lib/irssi/plugins/*.so
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/irssi
#%attr(644,root,root) %{prefix}/lib/irssi/scripts/perl/test.pl
