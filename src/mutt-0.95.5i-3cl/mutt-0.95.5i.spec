Summary: The Mutt Mail User Agent
Summary(pt_BR): Mutt, cliente de correio eletrônico
Summary(es): Mutt, cliente de correo electrónico
Name: mutt
%define version 0.95.5i
Version: %{version}
Release: 3cl
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
# was .gz
Source: ftp://ftp.guug.de/pub/mutt/mutt-%{PACKAGE_VERSION}.tar.bz2
Source800: mutt-wmconfig.i18n.tgz
Patch: mutt.rc.patch
Patch1: mutt-nosetgid.patch
Url: http://www.mutt.org/
Requires: slang >= 0.99.38, smtpdaemon, gpg
Buildroot: /var/tmp/mutt-root
Summary(de): Der Mutt Mail-User-Agent 
Summary(fr): Agent courrier Mutt
Summary(tr): Mutt elektronik posta programý

%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

GPG must be installed and PGP is highly recommended.

%description -l pt_BR
O Mutt é um pequeno mas muito poderoso cliente de correio em tela
cheia.  Inclui suporte a tipos MIME, cor, POP3, encadeamento de
mensagens, teclas configuráveis e classificação por encadeamento.

%description -l es
Mutt es un pequeño, pero muy potente cliente de correo en pantalla
llena. Incluye soporte a tipos MINE, color, POP3; encadenamiento de
mensajes, teclas configurables y clasificaciones por encadenamiento.

%description -l de
Mutt ist ein kleiner aber leistungsfähiger Vollbild-Mail-Client für Unix mit
MIME-Unterstützung, Farbe, POP3-Unterstützung, Nachrichten-Threading,
zuweisbaren Tasten und Sortieren nach Threads.

%description -l fr
mutt est un client courrier Unix plein écran, petit mais très puissant.
Il dispose de la gestion MIME, des couleurs, de la gestion POP, des fils
de discussion, des touches liées et d'un mode de tri sur les fils.

%description -l tr
Mutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME desteði,
renk ve POP3 desteði içerir.

%prep
%setup -q -n %{name}-0.95.5
%patch -p1
#%patch1 -p1

%build
# Construção com suporte a PGP quer ele exista ou não. Não parece
# haver maiores problemas (como o programa morrer) caso o PGP
# não esteja instalado.
unset LINGUAS
PGP=/usr/bin/pgp PGPK=/usr/bin/pgpk CFLAGS="$RPM_OPT_FLAGS \
-I/usr/include/slang" LDFLAGS=-s ./configure --prefix=/usr \
--with-sharedir=/etc --enable-pop --enable-imap --disable-warnings \
--with-slang --disable-domain --sysconfdir=/etc

make
#make manual.txt -C doc

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc sharedir=$RPM_BUILD_ROOT/etc docdir=$RPM_BUILD_ROOT/usr/doc/mutt-%{version} install

( cd $RPM_BUILD_ROOT
  #mkdir -p ./etc/X11/wmconfig
  #install -m 644 $RPM_SOURCE_DIR/mutt.wmconfig ./etc/X11/wmconfig/mutt
  chmod g-s ./usr/bin/mutt
)

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/





tar xvfpz $RPM_SOURCE_DIR/mutt-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/Muttrc
%doc contrib/Mush.rc contrib/Pine.rc README contrib/sample.* NEWS
%doc COPYRIGHT doc/manual.txt
/usr/bin/mutt
/usr/bin/mutt_dotlock
/usr/man/man1/mutt.1
/etc/X11/wmconfig/mutt

%changelog
* Fri May 7 1999 Guilherme Manika <gwm@conectiva.com>
- Atualizado para versão 0.95.5 internacional
- Requer GNU Privacy Guard

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Tue Oct 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmconfig translated to pt_BR

* Fri Jul 31 1998 Bill Nottingham <notting@redhat.com>
- backport some 0.94.2 security fixes
- fix un-setgid
- update to 0.93.2

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- security fix
- update to 0.93.1.
- turn off setgid mail.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.91.1

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to mutt-0.89.1

* Thu Oct 16 1997 Otto Hammersmith <otto@redhat.com>
- Updated to mutt 0.85.
- added wmconfig entries.
- removed mime.types

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- Rebuilt to insure all sources were fresh and patches were clean.

* Wed Aug 6 1997 Manoj Kasichainula <manojk@io.com>
 - Initial version for 0.81(e)
