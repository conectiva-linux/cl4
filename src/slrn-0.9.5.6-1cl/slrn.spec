Name: slrn
Version: 0.9.5.6
Release: 1cl
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://space.mit.edu/pub/davis/slrn/slrn-%{version}.tar.bz2
Source1: slrnpull-expire
Source2: slrnpull.log
Source3: slrn.wmconfig
Source4: README.rpm-slrnpull
Source800: slrn-wmconfig.i18n.tgz
Patch0: slrn-0.9.5.3-config.patch
Patch1: slrn-0.9.5.3-strength.patch
Requires: slang >= 1.2.2
BuildRoot: /var/tmp/slrn-build
URL: http://space.mit.edu/~davis/slrn.html
Summary: A powerful, easy to use, threaded Internet news reader.
Summary(pt_BR): O melhor leitor de notícias do mundo (na opinião da Red Hat)
Summary(es): El mejor lector de news del mundo (en la opinión de Red Hat)

%description
SLRN is a powerful, easy to use, threaded Internet news reader.  SLRN is
highly customizable and allows you to design complex filters to sort or kill
news articles.  SLRN works well over slow network connections, and includes
a utility for reading news off-line.

Install slrn if you need a full-featured news reader, if you have a slow
network connection, or if you'd like to save on-line time by reading your
news off-line.

%description -l pt_BR
Slrn é um leitor de notícias baseado em NNTP fácil de usar mas poderoso
com tela cheia. Ele utiliza a biblioteca de programadores S-Lang
para várias das suas características. Slrn trabalha particularmente
bem com conexões lentas de rede.

%description -l es
Slrn es un lector de news basado en NNTP fácil de usar, pero potente
con pantalla llena. Utiliza la biblioteca de programadores S-Lang
para varias de sus características. Slrn trabaja en especial con
conexiones lentas de red.

%package pull
Summary: Offline news reading support for slrn.
Summary(pt_BR): Suporte para leitura de notícias "offline" para o slrn
Summary(es): Offline news reading support for slrn.
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Requires: slrn = %{version}

%description pull
This package provides slrnpull, which allows set up of a small news
spool for offline news reading.

%description -l pt_BR pull
Este pacote provê o slrnpull, que permite a configuração de um
pequeno spool de notícias, para leitura "offline".

%description -l es pull
This package provides slrnpull, which allows set up of a small news
spool for offline news reading.

%prep
%setup
%patch1 -p1
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" slrn_cv_domain=no ./configure --prefix=/usr
make
make slrnpull

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/slrn,man/man1}
mkdir -p $RPM_BUILD_ROOT/etc/{cron.daily,logrotate.d,X11/wmconfig}
install doc/slrn.rc $RPM_BUILD_ROOT/usr/lib/slrn
install doc/slrn.1 $RPM_BUILD_ROOT/usr/man/man1/slrn.1
install -s src/objs/slrn $RPM_BUILD_ROOT/usr/bin/slrn
install $RPM_SOURCE_DIR/slrn.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/slrn
install -s src/objs/slrnpull $RPM_BUILD_ROOT/usr/bin/slrnpull
install -d $RPM_BUILD_ROOT/var/spool/slrnpull/out.going
install slrnpull/slrnpull.conf $RPM_BUILD_ROOT/var/spool/slrnpull
install $RPM_SOURCE_DIR/slrnpull-expire $RPM_BUILD_ROOT/etc/cron.daily
install $RPM_SOURCE_DIR/slrnpull.log $RPM_BUILD_ROOT/etc/logrotate.d/slrnpull
cp $RPM_SOURCE_DIR/README.rpm-slrnpull slrnpull/README.rpm
chmod 644 slrnpull/*



tar xvfpz $RPM_SOURCE_DIR/slrn-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING COPYRIGHT changes.txt doc/FAQ doc/INSTALL
%doc README doc/README.GroupLens doc/README.macros
%doc doc/SCORE_FAQ doc/*.txt doc/score.sl doc/slrn.sl
%doc macros
%config (missingok) /etc/X11/wmconfig/slrn
%dir /usr/lib/slrn
%config /usr/lib/slrn/slrn.rc
%attr(755,root,root) /usr/bin/slrn
/usr/man/man1/slrn.1

%files pull
%defattr(-,root,root)
%doc slrnpull/*
%attr(755,root,root) /etc/cron.daily/slrnpull-expire
/etc/logrotate.d/slrnpull
%attr(755,root,root) /usr/bin/slrnpull
%attr(775,news,news) %dir /var/spool/slrnpull
%attr(3777,news,news) %dir /var/spool/slrnpull/out.going
%attr(644,news,news) %config /var/spool/slrnpull/slrnpull.conf

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 0.9.5.4 to 0.9.5.6

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- make slrnpull/log missingok

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Feb 24 1999 Bill Nottingham <notting@redhat.com>
- return of wmconfig

* Mon Nov  9 1998 Bill Nottingham <notting@redhat.com>
- add bugfix patch from jed

* Fri Nov  6 1998 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.4

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- built for Raw Hide
- added bugfix patch

* Tue Sep 8 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.3-2]
- Fixed a couple of stupid things I did.
- Took out -fno-strength-reduce. AFAIK, gcc on RH5.1 doesn't have this bug. I
  use egcs which shouldn't have this bug. And if you have this bug, *and* are
  recompiling on your own machin, you should have -fno-strength-reduce in your
  RPM_OPT_FLAGS anyway.

* Tue Sep 8 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.3-1]
- Updated to 0.9.5.3

* Mon Jun 1 1998 Manoj Kasichainula <manojk+rpm@io.com>
- added translations from RH 5.1 (still none for slrn-pull package)

* Mon May 4 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.2-1]
- updated to 0.9.5.2

* Wed Apr 22 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.1-1]
- updated to 0.9.5.1

* Mon Apr 12 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.4.6-3]
- updated to require slang 1.2.1

* Sun Apr 12 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.4.6-2]
- updated to require slang 1.2.0

* Wed Feb 11 1998 Manoj Kasichainula <manojk+rpm@io.com>
(my unreleased 0.9.4.6-1)
- updated to 0.9.4.6

* Tue Feb 3 1998 Manoj Kasichainula <manojk+rpm@io.com>
- docs are now forced to 644 to prevent including /bin/sh as a requirement
- added macros in the doc directory
- should now be buildable by non-root

* Thu Jan 29 1998 Bill Nottingham <wen1@cec.wustl.edu>
- updated to 0.9.4.5
- added wmconfig entry

* Sat Sep 13 1997 Manoj Kasichainula <manojk+rpm@io.com> (0.9.4.3-2)
- Fixes from JED
- default mode for slrnpull posts set to 0640, so slrnpull can read it as
  non-root
- lots of pre-setup for slrnpull
  - directories set up
  - automatic daily expiration
  - moved slrnpull directory to /var/spool/slrnpull, to match (most) docs
  - more 
- minor spec file changes

* Sat Jul 12 1997 Manoj Kasichainula <manojk+rpm@io.com> (0.9.4.3-1)
- Initial release for 0.9.4.3
