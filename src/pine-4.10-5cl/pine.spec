Summary: MIME compliant mail reader w/ news support as well
Summary(pt_BR): Leitor de mail com suporte a MIME e news
Summary(es): Lector de mail con soporte a MIME y news
Name: pine
Version: 4.10
Release: 5cl
Copyright: distributable
Url: http://www.washington.edu/pine/
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://ftp.cac.washington.edu/pine/pine%{version}.tar.gz
Source800: pine-wmconfig.i18n.tgz
Patch0: pine4.10-glibc.patch
Patch5: pine-4.02-filter.patch
Patch6: pine4.04-noflock.patch
Patch7:	pine4.05-ioctl.patch
Patch8: pine4.10-quote.patch
Buildroot: /tmp/pine-build
Summary(de): MIME-konformer Mail-Reader mit News-Support 
Summary(fr): Lecteur de courrier conforme à MIME avec gestion des news"
Summary(tr): MIME uyumlu ileti okuyucusu (haber servisi desteði de vardýr)


%description
Pine is a very full featured text based mail and news client. It is
aimed at both novice and expert users. It includes an easy to use editor,
pico, for composing messages. Pico has gained popularity as a stand
alone text editor in it's own right. It features MIME support, address
books, and support for IMAP, mail, and MH style folders.

%description -l pt_BR
Pine é um programa cliente de mail ("leitor de mail") baseado em
texto e cliente de news. Ele é dirigido tanto para novatos como para
usuários experientes. Inclui um editor fácil de usar - pico - para
compor mensagens. O pico ganhou popularidade como editor isolado
por seus próprios méritos. Possui suporte para MIME, agendas de
endereço, e suporte para folders de estilo IMAP, mail e MH.

%description -l es
Pine es un programa cliente de mail ("lector de mail") basado en
texto y cliente de news. Está orientado tanto a principiantes como
a usuarios más expertos. Incluye un editor de uso fácil - pico -
para componer mensajes. Pico ganó popularidad como editor aislado por
sus propios méritos. Posee soporte para MINE, agendas de dirección,
y soporte para folders de estilo IMAP, mail y MH.

%description -l de
Pine ist ein kompletter textbasierender Mail- und New-Client, der sich 
sowohl an Neueinsteiger als auch an Experten richtet. Er umfaßt einen 
einfachen Editor (Pico), der zum Verfassen der Nachrichten dient, sich 
jedoch inzwischen einen Namen als autonomer Texteditor gemacht hat. Pine
unterstützt MIME, Adreßbücher, IMAP, Mail- und HM-Ordner. 

%description -l fr
pine est un client courrier et news très complet en mode texte. Il est
destiné aux débutants comme aux experts. Il comprend un éditeur simple à
utiliser, pico, pour composer les messages. pico est devenu populaire comme
éditeur de texte par lui-même. Il reconnait la gestion MIME, les carnets
d'adresse et la gestion IMAP, mail et des dossiers du style MH.

%description -l tr
Pine, metin tabanlý bir ileti ve haber servisi (news) istemcisidir. Hem acemi
hem de uzman kullanýcýlar için uygundur. Ýleti yazmak için kullanýmý oldukça
kolay olan pico adlý metin düzenleyicisini kullanýr. Pico kendi baþýna da bir
metin düzenleyici olarak ilgi görmüþtür. Pine, MIME desteði, adres defteri ve
IMAP, MH gibi ileti arþivi biçimlerini destekleme özelliklerini taþýr.

%prep
%setup -q -n pine%{version}
%patch0 -p1 -b .glibc
%patch5 -p1 -b .filter
%patch6 -p1 -b .noflock
%patch7 -p1 -b .ioctl
%patch8 -p1 -b .quote

# this wants /usr/local/bin/perl
chmod 644 contrib/utils/pwd2pine

%build
./build CC=egcs \
	OPTIMIZE="$RPM_OPT_FLAGS" \
	DEBUG="" \
        OPTIMIZE="$RPM_OPT_FLAGS" \
        EXTRACFLAGS="-DIGNORE_LOCK_EACCES_ERRORS" slx 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/doc $RPM_BUILD_ROOT/usr/lib
install -m 644 doc/mime.types $RPM_BUILD_ROOT/usr/lib/mime.types
for n in pine pico pilot; do
    install -m 755 -s bin/$n $RPM_BUILD_ROOT/usr/bin/$n
done

cd doc
for n in pine.1 pico.1 pilot.1; do
    install -m 644 $n $RPM_BUILD_ROOT/usr/man/man1
done
cat <<EOF > $RPM_BUILD_ROOT/usr/lib/pine.conf
#
# Pine system-wide defaults file -- customize as needed.
#
# This file sets the system-wide configuration defaults used by Pine.
# If you have questions about specific settings see the section on
# configuration options in the Pine notes.  On Unix, run pine -conf to
# see how system defaults have been set.  For variables that accept
# multiple values, list elements are separated by commas.  A line
# beginning with a space or tab is considered to be a continuation of
# the previous line.  For a variable to be unset its value must be
# blank.  To set a variable to the empty string its value should be
# "". Switch variables are set to either "yes" or "no", and default to
# "no".  Lines beginning with "#" are comments, and ignored by Pine.

EOF
cat <<EOF > $RPM_BUILD_ROOT/usr/lib/pine.conf.fixed
#
# Pine system-wide enforced configuration file - customize as needed
#
# This file holds the system-wide enforced values for pine configuration
# settings. Any values set in it will override values set in the
# system-wide default configuration file (/usr/lib/pine.conf) and
# the user's own configuration file (~/.pinerc).
# For more information on the format of this file, read the
# comments at the top of /usr/lib/pine.conf

EOF

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig



tar xvfpz $RPM_SOURCE_DIR/pine-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%defattr(-,root,root)
%doc README CPYRIGHT doc/*.txt doc/pine-ports doc/tech-notes doc/mailcap.unx contrib
/usr/bin/pine
/usr/bin/pico
/usr/bin/pilot
/usr/man/man1/pico.1
/usr/man/man1/pine.1
/usr/man/man1/pilot.1
%attr(0644,root,root)	%config /usr/lib/mime.types
%attr(0644,root,root)	%config /usr/lib/pine.conf
%attr(0644,root,root)	%config /usr/lib/pine.conf.fixed
%attr(0644,root,root)	%config(missingok) /etc/X11/wmconfig/pine
%attr(0644,root,root)	%config(missingok) /etc/X11/wmconfig/pico

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun  4 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Feb 18 1999 Cristian Gafton <gafton@redhat.com>
- add quote patch for mailcap from Terence C. Haddock <thaddock@POBOXES.COM>

* Fri Nov 13 1998 Cristian Gafton <gafton@redhat.com>
- patch to enable SIGWINCH processing (why do the pine folks keep 
  disabling this stuff?!)

* Fri Oct 09 1998 Cristian Gafton <gafton@redhat.com>
- use termios instead of termio (patch used to be in here...)
- use terminfo instead of termcap and link against ncurses instead of termcap
- supply -lcrypt as a standard lib

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 4.04 (compatibility with some client imaps).

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- use only fcntl locking.

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.03

* Fri Aug 14 1998 Jeff Johnson <jbj@redhat.com>
- patch to 4.02A.
- disable stupid EACCESS warnings.

* Wed Jul 22 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.02.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jan 15 1998 Erik Troan <ewt@redhat.com>
- added patch to fix pine filters

* Tue Dec 30 1997 Erik Troan <ewt@redhat.com>
- fixed resizing in pine and pico

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- removed patch for SIGCHLD race -- it shouldn't be necessary
- added patch to avoid longjmp() from SIGCHLD handler -- SIGCHLD handling
  is sane now

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- added a patch for handling a SIGCHLD race condition

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- fix for locks w/ long st_dev field
- use termios rather then termio

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- removed exec bit from /usr/doc/pine-3.96-1/contrib/utils/pwd2pine
