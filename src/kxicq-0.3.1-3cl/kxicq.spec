%define name kxicq
%define version 0.3.1
%define release 3cl

Summary: KXicq is the KDE ICQ clone for Linux/Unix!
Summary(pt_BR): O KXicq é o clone KDE do ICQ para o Linux/Unix!
Summary(es): KXicq es elclone KDE del ICQ para Linux/Unix!
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
URL: http://www.caiw.nl/~herwinjs/kxicq
Source: http://www.caiw.nl/~herwinjs/kxicq/%{name}-%{version}.tar.bz2
Patch: kxicq-0.3.1-aclocal.patch
Requires: kdelibs >= 1.1
BuildRoot: /tmp/%{name}-%{version}

%description
KXicq is the KDE ICQ client. It is the continuous work of the
XTrophy Xicq library. KXicq supports sending and retrieving of
messages and URLs, adding/removing users and playing sounds when
retrieving info/msg/URLs. Having a KDE like interface it looks
in no way like the windows ICQ version. KXicq has realtime
changing of window view and KDE docking.

%description -l pt_BR
O KXicq é um cliente ICQ para o KDE. É o trabalho contínuo da
biblioteca Xicq XTrophy. Suporta envio e recepção de mensagens
e URLs, adição/remoção de usuários e reprodução de sons quando
mensagens/informações/URLs são recebidas.

%description -l es
KXicq es un cliente ICQ para KDE. Es el trabajo continuo de la
biblioteca Xicq XTrophy. Soporta envío y recepción de mensajes y
URLs, adición/remoción de usuarios y reproducción de sonidos cuando
se recibe mensajes/información/URLs.

%prep
%setup -q
%patch -p1
./configure --prefix=/usr

%build
make

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/share/applnk/Internet
install -d $RPM_BUILD_ROOT/usr/share/apps/kxicq/pics
install -d $RPM_BUILD_ROOT/usr/share/apps/kxicq/wav
install -d $RPM_BUILD_ROOT/usr/share/locale/nl/LC_MESSAGES

install -c -s src/kxicq $RPM_BUILD_ROOT/usr/bin/kxicq
install -c -m 644 src/KXicq.kdelnk $RPM_BUILD_ROOT/usr/share/applnk/Internet
install -c -m 644 src/pics/*.xpm $RPM_BUILD_ROOT/usr/share/apps/kxicq/pics
install -c -m 644 src/wav/*.wav $RPM_BUILD_ROOT/usr/share/apps/kxicq/wav
install -c po/nl.gmo $RPM_BUILD_ROOT/usr/share/locale/nl/LC_MESSAGES/KXicq.mo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
/usr/bin/kxicq
/usr/share/applnk/Internet/KXicq.kdelnk
/usr/share/apps/kxicq
/usr/share/locale/nl/LC_MESSAGES/KXicq.mo

%changelog
* Sun Jun  6 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 05 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- recompressed sources

* Mon May 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with qt 1.44 + KDE 1.1.1

* Wed Mar 31 1999 Conectiva <dist@conectiva.com>
- included patch to aclocal.m4
- final rebuild for 3.0 spanish edition

* Sun Mar 14 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Feb 22 1999 Ryan Weaver <ryanw@infohwy.com>
  [kxicq-0.3.1-1]
- new in 0.3.1
- KXicq now remembers the send items !
- new history system
- WindowMaker Dock.app support !!! ( COOL !! )
  with full functional menu, do everything only
  with the WindowMaker Dock ;-)
- Debug can be switched on/off on startup
- i got a patch from ... with
  - Auto-unaway now react on Keyboard input
  - Dock enhanchments
  - some bugs removed
  - lots more ;-)
- more stable, by checking memory beter
- reconnect works beter
- Web Presence
- fixed lots of bugs
- fixed some chat color bugs
- redraw bugs fixed
- lots more configurable options
- configurable blinking 'new message' dock icon
  in WindowMaker you see a Dot blinking !
- configurable Save Geometry option
- connection free bug removed ?? ( please let me know !! )
- fixed authrization bug
- fixed add new user refresh bug ( looks like he didn't 
  add the user ! )
- new users must now enter password AND nick
- more i can't remeber ;-))

* Mon Feb  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [kxicq-0.3.0-1]
- new in 0.3.0
  i know 0.3.0 was mean to had more functions.. but i cannot
  add more numbers on the 0.2.x serie for my self ;-)
- changes a bug in the i18n
- lots of cosmetic changes:
  + better docking icon handling
  + beter repaint 
  + added KDE style too search users widget
  + better session support
- URL sending bug removed
- KFM or netscape are called OK ( still a work-around )
- Chat bug removed and support for 99a
- Chat cancel is displayd
- Chat keeps his colors on next sessions
- on Chat start the colors are received OK, no more gray
  display
- added Popupmenu item for opening the main Window even
  if there are unread messages
- Search is working a bit better ( one click KDE support )
- auto unaway
- better non-Linux support

* Tue Jan 26 1999 Ryan Weaver <ryanw@infohwy.com>
  [kxicq-0.2.28-1]
- Updated to 0.2.28.
- new in 0.2.28
- authorization
- new user view widget
- lots of bugs removed
- i18n is working, you can start translations ;-)

* Mon Dec 21 1998 Ryan Weaver <ryanw@infohwy.com>
  [kxicq-0.2.27-1]
- Updated to 0.2.27.
- new in 0.2.27
  * new send Dialog for Chat request, Messages and URL
  * new Docking options ( with menu )
  * auto away !!
  * new away settings
  * KDE 'one-click' style ( configurable )
  * big TCP bug removed

* Mon Dec 14 1998 Ryan Weaver <ryanw@infohwy.com>
  [kxicq-0.2.26-1]
- Updated to 0.2.26.
- new in 0.2.26
  * KURLlabel bug fixed....
- new in 0.2.25
  * Chat
  * tested Socks 5 support ( 0.2.24 was not working )
  * TCP bugs removes ( i hope most of them )
  * support for ecgs 1.1.x ( all egcs compiler should work now !! )
  * 100 users now, instead of 50 ( will be unlimited !! )
  * soms GUI changes ( sending of Messages and URL are now WorkWrap )
  * handeling unknown UIN and Password
  * couple of bug fixes

* Thu Dec  3 1998 Ryan Weaver <ryanw@infohwy.com>
  [kxicq-0.2.24-1]
- New in 0.2.24
  * Nick completion on adding users
  * Lots of bugs fixes
  * Removed a lot of mem leaks
