Summary: Converts plain ASCII to PostScript.
Summary(pt_BR): Converte texto ASCII para postscript
Summary(es): Converts plain ASCII to PostScript.
Name: enscript
Version: 1.6.1
Release: 9cl
Copyright: GNU
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
Source0: ftp://ftp.gnu.org/pub/gnu/enscript-1.6.1.tar.gz
Patch: enscript-1.6.1-config.patch
URL: http://www.ngs.fi/mtr/genscript/index.html
Prefix: %{_prefix}
BuildRoot: /var/tmp/%{name}-root
Obsoletes: nenscript

%description
Enscript is a print filter. It can take ASCII input
and format it into PostScript output. At the same time,
it can also do nice transformations like putting two
ASCII pages on one physical page (side by side) or
changing fonts.

%description -l pt_BR
O enscript é um filtro de impressão. Ele pega texto ascii
e o formata em postscript. Além disto, ele pode também
fazer várias transformações, como por exemplo colocar
duas páginas ascii em uma página física (lado a lado) ou
modificar as fontes do texto.

%description -l es
Enscript is a print filter. It can take ASCII input
and format it into PostScript output. At the same time,
it can also do nice transformations like putting two
ASCII pages on one physical page (side by side) or
changing fonts.

%prep
%setup -q
%patch -p1

%build
[ "$LINGUAS" ] && unset LINGUAS
%configure --with-media=Letter --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/{de,es,fi,fr,nl,sl}/LC_MESSAGES
make DESTDIR=$RPM_BUILD_ROOT install

# XXX note doubled %% in sed script below.
(cd $RPM_BUILD_ROOT;find .%{_prefix}/share/enscript/*) | \
	sed -e 's,^\.,,' | sed -e 's,*font.map,%%config &,' > share.list

{ cd $RPM_BUILD_ROOT
  strip .%{_prefix}/bin/* || :
  ln .%{_prefix}/bin/enscript .%{_prefix}/bin/nenscript
}


%clean
rm -rf $RPM_BUILD_ROOT

%files -f share.list
%defattr(-,root,root)
%{_prefix}/share/locale/*/LC_MESSAGES/enscript.mo
%{_prefix}/bin/diffpp
%{_prefix}/bin/sliceprint
%{_prefix}/bin/enscript
%{_prefix}/bin/nenscript
%{_prefix}/bin/mkafmmap
%{_prefix}/bin/states
%{_prefix}/bin/over

%{_prefix}/man/man1/*
%config /etc/enscript.cfg

%doc AUTHORS ChangeLog FAQ.html NEWS README README.ESCAPES THANKS TODO 

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Mar 24 1999 Erik Troan <ewt@redhat.com>
- marked /usr/share/enscript/font.map as a config file

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- added documentation to the RPM

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.
- include i18n locales.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Wed Nov 11 1998 Preston Brown <pbrown@redhat.com>
- translations ripped out, slight cleanup to build section.

* Mon Nov 09 1998 Preston Brown <pbrown@redhat.com>
- initial build of GNU enscript to replace nenscript.
