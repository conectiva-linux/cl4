Summary: Popular Unix Irc client
Summary(pt_BR): Cliente unix popular para IRC
Summary(es): Cliente unix popular para IRC
Name: ircii
Version: 4.4
Release: 9cl
Copyright: distributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
# was .gz
Source0: ftp://ftp.funet.fi/pub/ircII/ircii-4.4.tar.bz2
Source1: ircii.wmconfig
Source800: ircii-wmconfig.i18n.tgz
Summary(de): Beliebter Unix-IRC-Client
Summary(fr): Client irc UNIX populaire.
Summary(tr): Yaygýn Unix Irc istemcisi
Buildroot: /var/tmp/irc-root
Obsoletes: ircii-help
Requires: wserv

%description
This is a popular Internet Relay Chat (IRC) client.  It
is a program used to connect to IRC servers around the
globe so that the user can ``chat'' with others.

%description -l pt_BR
Este é o popular cliente IRC (Internet Relay Chat). É o programa
usado para conexão a servidores IRC ao redor do globo para que se
possa conversar (chat) como outros usuários.

%description -l es
Este es el popular cliente IRC (Internet Relay Chat). El programa
se usa para conexión a servidores IRC alrededor del mundo para que
se pueda charlar (chat) con otros usuarios.

%description -l de
Dies ist ein beliebter IRC-Client (Internet Relay Chat). Sie können eine
Verbindung zu einem beliebigen IRC-Server aufbauen und mit
anderen Benutzern 'chatten'.

%description -l fr
Le très poulaire client Internet Relay Chat (IRC). C'est
un programme utilisé pour se connecter aux serveurs IRC à
travers le monde entier et ``bavarder'' avec les autres.

%description -l tr
Bu, yaygýn kullanýlan bir IRC (Internet Relay Chat) istemcisidir. Dünya
üzerinde herhangi bir IRC sunucusuna baðlantý saðlar; baðlantý saðlandýktan
sonra kullanýcý diðer insanlarla sohbet edebilir.

%prep
%setup

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install
ln -sf irc-4.4 $RPM_BUILD_ROOT/usr/bin/irc

touch $RPM_BUILD_ROOT/usr/lib/irc/ircII.servers
echo "irc-2.mit.edu" >> $RPM_BUILD_ROOT/usr/lib/irc/ircII.servers
echo "irc-2.escape.com" >> $RPM_BUILD_ROOT/usr/lib/irc/ircII.servers
echo "irc.texas.net" >> $RPM_BUILD_ROOT/usr/lib/irc/ircII.servers
echo "irc.eskimo.com" >> $RPM_BUILD_ROOT/usr/lib/irc/ircII.servers
chmod 644 $RPM_BUILD_ROOT/usr/lib/irc/ircII.servers

mkdir -p $RPM_BUILD_ROOT/etc/X11
#install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
#install -m 644 -o root -g root $RPM_SOURCE_DIR/ircii.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/ircii

strip $RPM_BUILD_ROOT/usr/bin/* || :

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/




tar xvfpz $RPM_SOURCE_DIR/ircii-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/irc
/usr/bin/irc-4.4
/usr/bin/ircbug
/usr/bin/ircio
/usr/bin/ircflush
/usr/lib/irc/script
/usr/lib/irc/translation
/usr/lib/irc/ircII.servers
/etc/X11/wmconfig/ircii

/usr/lib/irc/help
%doc doc/*

%changelog
* Tue Jun 29 1999 Eliphas Levy Theodoro <eliphas@conectiva.com>
- Removed wserv

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Tue Oct 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- ircii.wmconfig translated to pt_BR

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- obsoletes ircii-help (donnie, don't do ever that again!)

* Wed Jun 03 1998 <djb@redhat.com>
- moved help stuff into main package

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 4.4
- changed to use a build root

* Wed Nov  5 1997 Otto Hammersmith <otto@redhat.com>
- moved wmconfig file from ircii-help file list

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- use termios, not termio

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added Erik's patch to fix file closing brokenness.

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated source urls

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

