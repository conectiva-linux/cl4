Summary: X based Mail notification tool
Summary(pt_BR): Ferramenta de notificação de mail baseado em X
Summary(es): Herramienta de notificación de mail basado en X
Name: xmailbox
Version: 2.5
Release: 9cl
Copyright: MIT
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: ftp://ftp.x.org/contrib/applications/xmailbox-2.5.tar.gz
Source800: xmailbox-wmconfig.i18n.tgz
Patch1: xmailbox-2.2-xpm.patch
Patch2: xmailbox-2.4-glibc.patch
BuildRoot: /var/tmp/xmailbox-root
Summary(de): Mail-Benachrichtigungs-Tool für X
Summary(fr): Un outil de notification de courrier sous X
Summary(tr): E-posta geldiði zaman uyaran program

%description
This program will notify you when new mail arrives. It is similar to
xbiff, but offers more features and fancier notification options.

%description -l pt_BR
Este programa irá notificá-lo quando um novo mail chegar. Ele é
similar ao xbiff, oferecendo mais características e opções de
notificação.

%description -l es
Este programa irá notificarlo cuando un nuevo mail llegue. Es similar
al xbiff, ofreciendo más características y opciones de notificación.

%description -l de
Dieses Programm gibt eine Meldung aus, wenn eine neue Mail eintrifft.
Es funktioniert ähnlich wie xbiff, enthält aber mehr Funktionen
und Benachrichtigungsoptionen.

%description -l fr
Ce programme vous avertira lorsqu'un nouveau courrier est arrivé.
Il ressemble à xbiff mais offre plus de possibilités et a des options
de notification plus jolies.

%description -l tr
Bu program yeni bir mesaj geldiði zaman sizi uyaracaktýr. xbiff ile
hemen hemen aynýdýr, ama daha fazla özelliði ve deðiþik uyarý þekilleri
vardýr.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
xmkmf
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

strip xmailbox
make DESTDIR=$RPM_BUILD_ROOT install install.man

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xmailbox <<EOF
#xmailbox name "xmailbox"
#xmailbox description "xmailbox"
#xmailbox group "Utilitários/Correio Eletrônico"
#xmailbox exec "xmailbox &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xmailbox-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/X11R6/bin/xmailbox
/usr/X11R6/man/man1/xmailbox.1x
%config /usr/X11R6/lib/X11/app-defaults/XMailbox
%config /etc/X11/wmconfig/xmailbox

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Mar 27 1999 Conectiva <dist@conectiva.com>
- fix wmconfig translation

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Mon Nov 30 1998 Conectiva <dist@conectiva.com>
- correção wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- updated wmconfig Group line

* Wed Oct 29 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
