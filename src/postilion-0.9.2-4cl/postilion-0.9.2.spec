%define name postilion
%define version 0.9.2
%define release 4cl
%define pathdir /usr/X11R6
%define serial 3

Summary: Postilion is a mail user agent based upon the popular TkRat program.
Summary(pt_BR): O Postilion é um cliente de e-mail baseado no popular programa TkRat.
Summary(es): Postilion is a mail user agent based upon the popular TkRat program.
Name: %{name}
Version: %{version}
Release: %{release}
Serial: %{serial}
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Copyright: GPL
Url: http://www.postilion.org
Source: %{name}-%{version}.tar.bz2
Source900: %{name}.wmconfig
Patch: %{name}-%{version}.patch.bz2
Requires: TkStep >= 8.0.4
Buildroot: /var/tmp/%{name}_root

%description
Postilion is a mail user agent based upon the popular TkRat program.
The main changes to TkRat are in the user interface portion, so all
of the underlying functionality of TkRat remains. This includes MIME
support, Virtual folders, PGP support, support for unix mail files,
MH folders, POP and IMAP.

%description -l pt_BR
O Postilion é um cliente de e-mail baseado no popular programa TkRat.
As principais mudanças em relação ao TkRat estão na parte da interface
com o usuário, desta forma todas as funcionalidades do TkRat foram
preservadas. Isto inclui suporte a MIME, pastas virtuais, PGP, arquivos
de correio eletrônico Unix, pastas MH, POP e IMAP.

%description -l es
Postilion is a mail user agent based upon the popular TkRat program.
The main changes to TkRat are in the user interface portion, so all
of the underlying functionality of TkRat remains. This includes MIME
support, Virtual folders, PGP support, support for unix mail files,
MH folders, POP and IMAP.

%prep

%setup -q
%patch -p1

CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=%{pathdir}

%build
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT%{pathdir}
make prefix=$RPM_BUILD_ROOT%{pathdir} install
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 644 $RPM_SOURCE_DIR/postilion.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/postilion

## Strip Binaries
strip $RPM_BUILD_ROOT%{pathdir}/lib/postilion/postilion.exec

%clean
rm -r $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root)
%doc doc BLURB CONFIGURATION COPYING COPYRIGHT.TkRat
%doc COPYRIGHT.images CREDITS 
%doc INSTALL Postilion.html README gpl.html index.html
%config (missingok) /etc/X11/wmconfig/postilion
%{pathdir}/bin/postilion
%{pathdir}/lib/postilion

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
  [postilion-0.9.2-3cl]
- Updated to 0.9.2-2 and merged changelog with the spec of ryanw@infohwy.com

* Tue May 25 1999 Ryan Weaver <ryanw@infohwy.com>
  [postilion-0.9.2-2]
- Took hint from .deb maker Dale James Thompson <thompd1@texhoma.net>
  and added his patch to make /usr/lib/postilionlib /usr/lib/postilion
  and fixes LIBDIR line in postilion wrapper script.
- Modified Mr. Thompson's patch to add RPM_OPT_FLAGS to the BASECFLAGS
  of the imap Makefile.

* Mon Apr 19 1999 Ryan Weaver <ryanw@infohwy.com>
  [postilion-0.9.2-1]
- Fixed bugs with send/save, bounce and Send bug reort. I really
  mean it this time!!
- Added "Flag as answered" command.
- Changed all "Falg as ..." commands to act as toggles.
- Fixed bug with "Import MH Directory" function.
- Fixed bugs introduced into DND functions.
- Fixed Sender style dynamic folders to create files with usable
  names. For example, a message sent by "John Smith" <jsmith@abcdef.com> 
  used to get saved as John Smith which Postilion could then not open.
  Now it will be saved as John Smith which Postilion can open. (Thanks to Tim Wundke!).
- Cleaned up mailbox list maintenance code. This should reduce the
  size of "vfolderlist" files.
- Removed the HTML parsing code. This was the single largest source
  of bug reports, so it is now gone. I am working with some
  replacements, and should have something worked out soon.
- Updated Swedish translation (Thanks to Martin S.!).

* Tue Mar 23 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Modified file path for /usr/X11R6
- Added pt_BR translations
- Added wmconfig

* Mon Feb 15 1999 Ryan Weaver <ryanw@infohwy.com>
  [postilion-0.9.1a-1]
- Applied pgp.patch
- Postilion 0.9.1 (February 8, 1999)
- Changes copyright on all images to the OpenContent License (OPL)
- Added new Bounce command, which will bounce a message to a new
  address or addresses.
- Fixed bug with saving messages with no From: header to a dynamic
  mailbox (thanks Luke!).
- Fixed memory leak in folder sort code (Luke again).
- Fixed bugs introduced into printing code, and other areas, in
  last release.
- Fixed bug which prevented salvaging messages which couldn't be
  sent properly.
- Fixed some bugs with the message hold.
- Fixed bug which caused preferences window to think you had made
  changes when you hadn't.
- Fixed bug in expire code.
- Fixed Changes alerting system (what you're reading right now).

* Wed Feb 10 1999 Ryan Weaver <ryanw@infohwy.com>
  [postilion-0.9.1-2]
- Applied a patch to fix some problems in the initial release of 0.9.1

* Tue Feb  9 1999 Ryan Weaver <ryanw@infohwy.com>
  [postilion-0.9.1-1]
- Now building rpm with TkStep-8.0.4 installed.
- Postilion 0.9.1 (February 8, 1999)
- Changes copyright on all images to the OpenContent License (OPL)
- Added new Bounce command, which will bounce a message to a new
  address or addresses.
- Fixed bug with saving messages with no From: header to a dynamic
  mailbox (thanks Luke!).
- Fixed memory leak in folder sort code (Luke again).
- Fixed bugs introduced into printing code, and other areas, in
  last release.
- Fixed bug which prevented salvaging messages which couldn't be
  sent properly.
- Fixed some bugs with the message hold.
- Fixed bug which caused preferences window to think you had made
  changes when you hadn't.
- Fixed bug in expire code.
- Fixed Changes alerting system (what you're reading right now).


* Mon Feb  1 1999 Ryan Weaver <ryanw@infohwy.com>
  [postilion-0.9.0-1]
- Postilion 0.9.0 (January 31, 1999)
- Added new PGP buttons to the compose window when PGP is enabled.
  Note: The meaning of the PGP lock button is now encrypt, where it
  used to be attach keys. There are now separate buttons for attach
  keys and sign. There is also now a button for DSN notification
  request. These buttons will auto size and auto arrange to account
  for different PGP confiigurations, so your compose windows may
  appear different from the picture on the web site.
- Fixed longstanding bug with mailbox sorting. Much thanks to Luke
  Kendall <luke@zeta.org.au>, the newset member of the Postilion
  development team.
- Added CREDITS and COPYRIGHT.images files.
- Added check for tkstepConfig.sh to the configure script.
- Proper detection and configuration for AIX4.2.
- Added option to expunge deleted messages on mailbox close.
- Fixed bug with password caching.
- Added option to display a Syncronize button in the browser
  window. The operation mode of this button is configurable.
- Added option to not print non-text attachments.
- Added options to open selected mailboxes on startup. Such
  mailboxes may be opened minimized or not.
- Added option to append to an existing file when saving message
  parts from the message window.
- Numerous bug fixes in address book.
- When quoting a message, if text is selected in the message being
  quoted, only that text will be quoted.
- Bug fixed in importing mailrc file aliases.
- Fixed the behavior of the New button in the Mailboxes window.
- Fixed a bug with clicking on URLs with commas in them.

* Wed Nov 25 1998 Ryan Weaver <ryanw@infohwy.com>
  [postilion-0.8.9-1]
- Postilion 0.8.9 (September 26, 1998)
  * French language translations for many texts (thanks to didier
    Belot <dib@avo.fr>. More is comming, didier's hard drive crashed,
    which ceased progress for a while.
  * Fixed focus problem when new mail comes in to a different window
    than the currently active one.
  * Fixed bug with message flagging.
  * Other minor bug fixes.
  * Upgraded c-client toolkit.
