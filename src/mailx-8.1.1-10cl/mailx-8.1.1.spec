Summary: /bin/mail - the "traditional" way to mail via shell scripts, etc
Summary(pt_BR): /bin/mail
Summary(es): /bin/mail
Name: mailx
Version: 8.1.1
Release: 10cl
Copyright: BSD
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
#Source: ftp://ftp.debian.org/pub/debian/hamm/source/mail/mailx-8.1.1.tar.gz
# recompactado com bzip2
Source: ftp://ftp.debian.org/pub/debian/hamm/source/mail/mailx-8.1.1.tar.bz2
Patch0: mailx-8.1.1.debian.patch
Patch1: mailx-8.1.1.security.patch
Patch2: mailx-8.1.1.nolock.patch
Patch3: mailx-8.1.1.debian2.patch
BuildRoot: /var/tmp/mailx-root

%description
The /bin/mail program can be used to send quick mail messages, and
is often used in shell scripts.

%description -l pt_BR
O programa /bin/mail pode ser usado para enviar rapidamente mensagens
de mail, e é geralmente usado em shell scripts.

%description -l es
El programa /bin/mail se puede usar para enviar rápidamente mensajes
de mail, y generalmente se usa en shell scripsts.

%description -l de
Das /bin/mail-Programm dient zum Versenden von Quick-Mail-
Nachrichten und wird häufig in Shell-Skripts verwendet.

%description -l fr
Le programme /bin/mail peut être utilisé pour envoyer des mails
rapides et est souvent utilisé dans les scripts shell.

%description -l tr
/bin/mail programý hýzlý olarak mektup göndermek için kullanýlabilir.
Genellikle kabuk yorumlayýcýlarý içinde kullanýlýr.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{bin,etc,usr/bin,usr/lib,usr/man/man1}

make DESTDIR=$RPM_BUILD_ROOT install

( cd $RPM_BUILD_ROOT
  mv ./usr/bin/mail ./bin/mail
  chmod g-s ./bin/mail
  ln -sf ../../bin/mail ./usr/bin/Mail
  ln -sf mail.1 ./usr/man/man1/Mail.1
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,mail)	/bin/mail
/usr/bin/Mail
/usr/lib/mail.help
/usr/lib/mail.tildehelp
%config /etc/mail.rc
/usr/man/man1/mail.1
/usr/man/man1/Mail.1

%changelog
* Tue May 25 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Aug 27 1998 Alan Cox <alan@redhat.com>
- Synchronized with the Debian people (more small edge case cures)

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 24 1998 Alan Cox <alan@redhat.com>
- Switched dotlocking off. This fits the Red Hat model of not having setgid
  mail agents and fixes the "lock" problem reported.

* Mon Jun 22 1998 Alan Cox <alan@redhat.com>
- Buffer overrun patches. These dont bite us when we don't run mailx setgid
  but do want to be in as mailx needs to be setgid

* Fri Jun 12 1998 Alan Cox <alan@redhat.com>
- Moved from 5.5 to the OpenBSD 8.1 release plus Debian patches

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc
